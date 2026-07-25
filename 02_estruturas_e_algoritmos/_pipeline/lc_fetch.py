# -*- coding: utf-8 -*-
"""Pipeline de problemas do LeetCode — fetcher com fila persistente.

Comandos:
  python lc_fetch.py catalogo [--paginas N]   Baixa o catálogo completo e (re)gera a fila ordenada
  python lc_fetch.py baixar-tudo [N]          Baixa TODOS os enunciados acessíveis p/ enunciados/ (retomável; N = limite p/ teste)
  python lc_fetch.py lote [N]                 Monta lote com os próximos N pendentes (padrão 20) -> lotes/lote_XXX.json (usa o cache se existir)
  python lc_fetch.py sincronizar              Marca como documentado tudo que já tem doc em problemas/
  python lc_fetch.py resetar <lote|orfaos>    Devolve os problemas de um lote à fila (status pendente) e apaga o arquivo
  python lc_fetch.py validar [id ...]         Valida docs contra o padrão do template (sem ids: valida todos)
  python lc_fetch.py status                   Resumo da fila

Ordenação da fila: dificuldade (easy->medium->hard) > categoria (01->18, simples->complexo) > número.
A categoria atribuída aqui é SUGESTÃO por tags; a skill leetcode-problems dá a palavra final.
"""
import io
import json
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ_EDA = AQUI.parent                      # 02_estruturas_e_algoritmos/
FILA = AQUI / "fila.json"
LOTES = AQUI / "lotes"
ENUNCIADOS = AQUI / "enunciados"            # cache local: 1 JSON por problema (fora do git)
GRAPHQL = "https://leetcode.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/problemset/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) study-repo-pipeline/1.0",
}
PAUSA = 1.0                                 # segundos entre requisições: respeito ao servidor
DIF_ORDEM = {"EASY": 0, "MEDIUM": 1, "HARD": 2}

# Regras de classificação tag -> categoria, avaliadas EM ORDEM (específica antes de genérica)
REGRAS = [
    ({"shortest-path", "minimum-spanning-tree", "strongly-connected-component",
      "biconnected-component", "eulerian-circuit"}, "12_grafos_avancados"),
    ({"trie"}, "08_tries"),
    ({"linked-list", "doubly-linked-list"}, "06_linked_list"),
    ({"monotonic-stack"}, "04_stack"),
    ({"sliding-window"}, "03_sliding_window"),
    ({"line-sweep"}, "16_intervals"),
    ({"topological-sort", "union-find", "graph"}, "11_grafos"),
    ({"binary-search-tree", "binary-tree", "tree", "segment-tree", "binary-indexed-tree"}, "07_arvores"),
    ({"heap-priority-queue"}, "09_heap_priority_queue"),
    ({"backtracking"}, "10_backtracking"),
    ({"binary-search"}, "05_busca_binaria"),
    ({"two-pointers"}, "02_two_pointers"),
    ({"stack", "monotonic-queue", "queue"}, "04_stack"),
    ({"bit-manipulation", "bitmask"}, "18_bit_manipulation"),
    ({"greedy"}, "15_greedy"),
    ({"dynamic-programming"}, "13_programacao_dinamica_1d"),   # refinada p/ 14 abaixo
    ({"math", "geometry", "number-theory", "combinatorics", "probability-and-statistics",
      "game-theory", "matrix", "simulation"}, "17_matematica_e_geometria"),
    ({"hash-table", "array", "string", "sorting", "counting", "prefix-sum"}, "01_arrays_e_hashing"),
]


def classificar(tags, titulo):
    t = set(tags)
    titulo_l = titulo.lower()
    if "interval" in titulo_l or "meeting" in titulo_l:
        return "16_intervals"                       # LeetCode não tem tag 'intervals'
    for conjunto, categoria in REGRAS:
        if t & conjunto:
            if categoria == "13_programacao_dinamica_1d" and (t & {"matrix"} or "edit" in titulo_l
                    or "subsequence" in titulo_l and "string" in t):
                return "14_programacao_dinamica_2d"  # heurística: DP sobre 2 dimensões
            return categoria
    return "01_arrays_e_hashing"                     # default seguro


def requisitar(query, variaveis, tentativas=4):
    corpo = json.dumps({"query": query, "variables": variaveis}).encode("utf-8")
    for i in range(tentativas):
        try:
            req = urllib.request.Request(GRAPHQL, data=corpo, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))["data"]
        except Exception as e:                       # backoff exponencial: rede/429
            espera = 2 ** i * 2
            print(f"  aviso: {e} — nova tentativa em {espera}s")
            time.sleep(espera)
    raise SystemExit("Falha de rede persistente. Rode novamente mais tarde — a fila é retomável.")


Q_LISTA = """
query lista($skip: Int!, $limit: Int!) {
  problemsetQuestionList: questionList(categorySlug: "algorithms", limit: $limit, skip: $skip, filters: {}) {
    total: totalNum
    questions: data {
      frontendQuestionId: questionFrontendId
      title titleSlug difficulty
      paidOnly: isPaidOnly
      topicTags { slug }
    }
  }
}"""

Q_DETALHE = """
query detalhe($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId title titleSlug difficulty content
    topicTags { slug }
  }
}"""


def limpar_html(html):
    if not html:
        return ""
    txt = html
    txt = re.sub(r"<sup>(.*?)</sup>", r"^\1", txt)
    txt = re.sub(r"</?(b|strong|em|u)>", "**", txt)
    txt = re.sub(r"<code>", "`", txt); txt = re.sub(r"</code>", "`", txt)
    txt = re.sub(r"<pre>", "\n```\n", txt); txt = re.sub(r"</pre>", "\n```\n", txt)
    txt = re.sub(r"<li>", "\n- ", txt)
    txt = re.sub(r"</?p>", "\n", txt)
    txt = re.sub(r"<img[^>]*src=\"([^\"]+)\"[^>]*>", r"[imagem: \1]", txt)
    txt = re.sub(r"<[^>]+>", "", txt)                # remove o resto das tags
    import html as h
    txt = h.unescape(txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()


def docs_existentes():
    numeros = set()
    for md in (RAIZ_EDA / "problemas").glob("*/*/[0-9]*_*.md"):
        m = re.match(r"(\d+)", md.stem)
        if m:
            numeros.add(int(m.group(1)))
    return numeros


def carregar_fila():
    if FILA.is_file():
        with io.open(FILA, encoding="utf-8") as f:
            return json.load(f)
    return {"gerado_em": None, "problemas": []}


def salvar_fila(fila):
    with io.open(FILA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(fila, f, ensure_ascii=False, indent=1)


def cmd_catalogo(paginas_max=None):
    antigos = {p["id"]: p for p in carregar_fila()["problemas"]}
    problemas, skip, limite = [], 0, 100
    total = None
    pagina = 0
    while total is None or skip < total:
        if paginas_max is not None and pagina >= paginas_max:
            break
        dados = requisitar(Q_LISTA, {"skip": skip, "limit": limite})
        bloco = dados["problemsetQuestionList"]
        total = bloco["total"]
        for q in bloco["questions"]:
            try:
                pid = int(q["frontendQuestionId"])
            except ValueError:
                continue                              # ids não numéricos (raros): fora do escopo
            tags = [t["slug"] for t in q["topicTags"]]
            problemas.append({
                "id": pid,
                "slug": q["titleSlug"],
                "titulo": q["title"],
                "dif": q["difficulty"].lower(),
                "premium": bool(q["paidOnly"]),
                "tags": tags,
                "categoria": classificar(tags, q["title"]),
                "status": "pendente",
                "lote": None,
            })
        skip += limite
        pagina += 1
        print(f"catálogo: {min(skip, total)}/{total}")
        time.sleep(PAUSA)

    # preserva progresso anterior e marca docs já existentes no repositório
    feitos = docs_existentes()
    for p in problemas:
        antigo = antigos.get(p["id"])
        if antigo:
            p["status"], p["lote"] = antigo["status"], antigo["lote"]
        if p["premium"] and p["status"] == "pendente":
            p["status"] = "premium"                  # sem enunciado acessível: fora da fila
        if p["id"] in feitos:
            p["status"] = "documentado"

    # A ORDEM DE ESTUDO: dificuldade > categoria (conceito simples->complexo) > número
    problemas.sort(key=lambda p: (DIF_ORDEM[p["dif"].upper()], p["categoria"], p["id"]))
    salvar_fila({"gerado_em": date.today().isoformat(), "problemas": problemas})
    print(f"fila.json: {len(problemas)} problemas ordenados.")
    cmd_status()


def caminho_cache(p):
    return ENUNCIADOS / f"{p['id']:04d}_{p['slug']}.json"


def baixar_enunciado(p):
    """Busca o enunciado na rede e grava no cache. None = indisponível (premium/removido)."""
    det = requisitar(Q_DETALHE, {"titleSlug": p["slug"]})["question"]
    if not det or not det.get("content"):
        return None
    reg = {k: p[k] for k in ("id", "slug", "titulo", "dif", "tags", "categoria")}
    reg["url"] = f"https://leetcode.com/problems/{p['slug']}/"
    reg["enunciado"] = limpar_html(det["content"])
    ENUNCIADOS.mkdir(exist_ok=True)
    with io.open(caminho_cache(p), "w", encoding="utf-8", newline="\n") as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)
    return reg


def obter_enunciado(p, pausar=True):
    """Cache primeiro; rede como fallback (alimentando o cache)."""
    arq = caminho_cache(p)
    if arq.is_file():
        with io.open(arq, encoding="utf-8") as f:
            return json.load(f)
    reg = baixar_enunciado(p)
    if pausar:
        time.sleep(PAUSA)
    return reg


def cmd_baixar_tudo(limite=None):
    fila = carregar_fila()
    if not fila["problemas"]:
        raise SystemExit("Fila vazia. Rode primeiro: python lc_fetch.py catalogo")
    alvo = [p for p in fila["problemas"]
            if p["status"] not in ("premium", "indisponivel") and not caminho_cache(p).is_file()]
    if limite:
        alvo = alvo[:limite]
    total = len(alvo)
    print(f"{total} enunciados a baixar (~{total * 1.4 / 60:.0f} min). "
          f"Pode interromper (Ctrl+C) à vontade: rodar de novo retoma de onde parou.", flush=True)
    baixados = indisponiveis = 0
    for i, p in enumerate(alvo, 1):
        if baixar_enunciado(p) is None:
            p["status"] = "indisponivel"
            indisponiveis += 1
        else:
            baixados += 1
        if i % 25 == 0 or i == total:
            salvar_fila(fila)                        # checkpoint: interrupção nunca perde progresso
            print(f"  {i}/{total} ({baixados} ok, {indisponiveis} indisponíveis)", flush=True)
        time.sleep(PAUSA + 0.2)
        if i % 100 == 0:
            time.sleep(10)                           # respiro periódico: educação com o servidor
    salvar_fila(fila)
    em_cache = len(list(ENUNCIADOS.glob("*.json"))) if ENUNCIADOS.is_dir() else 0
    print(f"cache completo: {em_cache} enunciados em {ENUNCIADOS.name}/")


def cmd_lote(n=20):
    fila = carregar_fila()
    if not fila["problemas"]:
        raise SystemExit("Fila vazia. Rode primeiro: python lc_fetch.py catalogo")
    pendentes = [p for p in fila["problemas"] if p["status"] == "pendente"][:n]
    if not pendentes:
        raise SystemExit("Nenhum pendente na fila. 🎉")
    LOTES.mkdir(exist_ok=True)
    numero = 1 + max([int(m.group(1)) for f in LOTES.glob("lote_*.json")
                      if (m := re.search(r"lote_(\d+)", f.name))], default=0)
    nome = f"lote_{numero:03d}"
    itens = []
    for i, p in enumerate(pendentes, 1):
        origem = "cache" if caminho_cache(p).is_file() else "rede"
        print(f"[{i}/{len(pendentes)}] {p['id']:>4} {p['titulo']} ({origem})")
        reg = obter_enunciado(p)
        if reg is None:
            p["status"] = "indisponivel"             # premium disfarçado ou removido
            continue
        itens.append({**p, "url": reg["url"], "enunciado": reg["enunciado"]})
        p["status"], p["lote"] = "baixado", nome
    destino = LOTES / f"{nome}.json"
    with io.open(destino, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"lote": nome, "criado_em": date.today().isoformat(), "problemas": itens},
                  f, ensure_ascii=False, indent=1)
    salvar_fila(fila)
    print(f"\n{destino.relative_to(RAIZ_EDA)} pronto com {len(itens)} problemas.")
    print(f"Próximo passo: peça ao Claude — /leetcode-lote {nome}")


def cmd_sincronizar():
    fila = carregar_fila()
    feitos = docs_existentes()
    mudou = 0
    for p in fila["problemas"]:
        if p["id"] in feitos and p["status"] != "documentado":
            p["status"] = "documentado"
            mudou += 1
    salvar_fila(fila)
    print(f"sincronizado: {mudou} problema(s) marcados como documentados.")
    cmd_status()


# ---------- validação do padrão (usada pelo CLI e pelo gerar_docs.py) ----------

SECOES_OBRIGATORIAS = [
    ("## 📜", "O Problema"), ("## 🧭", "Como reconhecer"), ("## 🐢", "Força bruta"),
    ("## 💡", "Ideia otimizada"), ("## 🎬", "Walkthrough"), ("## ⚡", "Complexidade"),
    ("## 💻", "Implementações"), ("### Java", "Java"), ("### Python", "Python"),
    ("### C++", "C++"), ("## ⚠️", "Pegadinhas"), ("## 🧪", "Casos de teste"),
    ("## 🔗", "Conexões"), ("## 📝", "O que eu aprendi"),
]


def validar_doc(caminho, item_fila=None):
    """Confere um doc de problema contra o padrão do _TEMPLATE.md. Retorna lista de erros."""
    caminho = Path(caminho)
    with io.open(caminho, encoding="utf-8") as f:
        texto = f.read()
    erros = []
    for marca, nome in SECOES_OBRIGATORIAS:
        if marca not in texto:
            erros.append(f"seção ausente: {nome} ({marca})")

    m = re.search(r"### Java.*?```java\s*\n(.*?)```", texto, re.S)
    if not m or len(m.group(1).strip()) < 60:
        erros.append("bloco Java vazio ou curto demais (deve conter a solução completa)")
    m = re.search(r"### Python.*?```python\s*\n(.*?)```", texto, re.S)
    if not m or "TODO" not in m.group(1):
        erros.append("bloco Python deve conter apenas TODO (é exercício do usuário)")
    m = re.search(r"### C\+\+.*?```cpp\s*\n(.*?)```", texto, re.S)
    if not m or "TODO" not in m.group(1):
        erros.append("bloco C++ deve conter apenas TODO (é exercício do usuário)")

    m = re.search(r"## 📝[^\n]*\n(.*)\Z", texto, re.S)
    if m and re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S).strip():
        erros.append("'O que eu aprendi' foi preenchida pela IA — deve ficar vazia")

    if "leetcode.com/problems/" not in texto:
        erros.append("sem link para o problema no LeetCode")
    if "Resolvido em:" not in texto:
        erros.append("sem campo 'Resolvido em:'")
    m = re.search(r"## 🎬(.*?)## ⚡", texto, re.S)
    if m and m.group(1).count("|") < 6:
        erros.append("walkthrough sem tabela de trace")

    m = re.match(r"(\d+)", caminho.stem)
    if m:
        numero = int(m.group(1))
        primeira = texto.splitlines()[0] if texto else ""
        if f"[{m.group(1)}]" not in primeira:
            erros.append(f"título não contém [{m.group(1)}] (nome do arquivo e título divergem)")
        if item_fila:
            if caminho.parent.name != item_fila["dif"]:
                erros.append(f"pasta de dificuldade '{caminho.parent.name}' difere da fila ('{item_fila['dif']}')")
    return erros


def achar_doc(numero):
    alvos = list((RAIZ_EDA / "problemas").glob(f"*/*/{numero:04d}_*.md"))
    return alvos[0] if alvos else None


def cmd_validar(ids=None):
    fila = {p["id"]: p for p in carregar_fila()["problemas"]}
    if ids:
        docs = [d for n in ids if (d := achar_doc(int(n)))]
        if len(docs) < len(ids):
            print("aviso: alguns ids não têm doc em problemas/")
    else:
        docs = sorted((RAIZ_EDA / "problemas").glob("*/*/[0-9]*_*.md"))
    falhas = 0
    for doc in docs:
        numero = int(re.match(r"(\d+)", doc.stem).group(1))
        erros = validar_doc(doc, fila.get(numero))
        if erros:
            falhas += 1
            print(f"FALHOU {doc.relative_to(RAIZ_EDA)}")
            for e in erros:
                print(f"   - {e}")
        else:
            print(f"ok     {doc.relative_to(RAIZ_EDA)}")
    print(f"\n{len(docs) - falhas}/{len(docs)} docs no padrão.")
    sys.exit(1 if falhas else 0)


def cmd_resetar(alvo):
    """Devolve à fila os problemas de um lote (ou de todos os lotes cujos arquivos sumiram)."""
    fila = carregar_fila()
    existentes = {f.stem for f in LOTES.glob("lote_*.json")} if LOTES.is_dir() else set()
    voltaram = 0
    for p in fila["problemas"]:
        if p["status"] != "baixado":
            continue                                  # documentado/premium nunca são resetados
        orfao = p["lote"] not in existentes
        if (alvo == "orfaos" and orfao) or p["lote"] == alvo:
            p["status"], p["lote"] = "pendente", None
            voltaram += 1
    salvar_fila(fila)
    arquivo = LOTES / f"{alvo}.json"
    if arquivo.is_file():
        arquivo.unlink()                              # o enunciado é re-baixável; nada se perde
        print(f"{arquivo.name} apagado.")
    print(f"{voltaram} problema(s) de volta à fila como pendente.")
    cmd_status()


def cmd_status():
    fila = carregar_fila()
    cont = {}
    for p in fila["problemas"]:
        cont[p["status"]] = cont.get(p["status"], 0) + 1
    total = len(fila["problemas"])
    print(f"fila: {total} problemas | " + " | ".join(f"{k}: {v}" for k, v in sorted(cont.items())))
    docs = cont.get("documentado", 0)
    if total:
        print(f"progresso de documentação: {docs}/{total} ({100 * docs / max(total - cont.get('premium', 0), 1):.1f}% dos acessíveis)")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)
    cmd = args[0]
    if cmd == "catalogo":
        paginas = None
        if "--paginas" in args:
            paginas = int(args[args.index("--paginas") + 1])
        cmd_catalogo(paginas)
    elif cmd == "baixar-tudo":
        cmd_baixar_tudo(int(args[1]) if len(args) > 1 else None)
    elif cmd == "lote":
        cmd_lote(int(args[1]) if len(args) > 1 else 20)
    elif cmd == "sincronizar":
        cmd_sincronizar()
    elif cmd == "resetar":
        if len(args) < 2:
            raise SystemExit("Uso: python lc_fetch.py resetar <lote_001|orfaos>")
        cmd_resetar(args[1])
    elif cmd == "validar":
        cmd_validar(args[1:] or None)
    elif cmd == "status":
        cmd_status()
    else:
        print(__doc__)
