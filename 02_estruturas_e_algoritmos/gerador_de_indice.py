# -*- coding: utf-8 -*-
"""Varre problemas/<categoria>/<dificuldade>/*.md e atualiza:

  1. INDICE.md            — índice completo (gerado do zero a cada execução)
  2. PROGRESSO.md         — apenas as partes automáticas:
       - coluna "Problemas resolvidos" da tabela de padrões
       - lista "Problemas resolvidos" entre os marcadores AUTO
     Tudo fora dos marcadores (seus status 🔴🟡🟢, notas) é preservado.

Uso:  python gerador_de_indice.py
"""
import io
import re
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
PROBLEMAS = RAIZ / "problemas"
INDICE = RAIZ / "INDICE.md"
PROGRESSO = RAIZ / "PROGRESSO.md"
DIFICULDADES = ["easy", "medium", "hard"]
EMOJI = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}
MARCA_INI = "<!-- INICIO:PROBLEMAS-AUTO -->"
MARCA_FIM = "<!-- FIM:PROBLEMAS-AUTO -->"

NOMES = {  # nome de exibição por pasta de categoria (com acentos)
    "01_arrays_e_hashing": "Arrays e Hashing",
    "02_two_pointers": "Two Pointers",
    "03_sliding_window": "Sliding Window",
    "04_stack": "Stack",
    "05_busca_binaria": "Busca Binária",
    "06_linked_list": "Linked List",
    "07_arvores": "Árvores",
    "08_tries": "Tries",
    "09_heap_priority_queue": "Heap / Priority Queue",
    "10_backtracking": "Backtracking",
    "11_grafos": "Grafos",
    "12_grafos_avancados": "Grafos Avançados",
    "13_programacao_dinamica_1d": "Programação Dinâmica 1D",
    "14_programacao_dinamica_2d": "Programação Dinâmica 2D",
    "15_greedy": "Greedy",
    "16_intervals": "Intervals",
    "17_matematica_e_geometria": "Matemática e Geometria",
    "18_bit_manipulation": "Bit Manipulation",
}


def nome_categoria(pasta_cat: str) -> str:
    return NOMES.get(pasta_cat, pasta_cat.split("_", 1)[-1].replace("_", " ").title())


def titulo_limpo(titulo: str) -> str:
    """Remove o prefixo '[NNNN] ' do título — o nº já tem coluna própria e
    colchetes dentro de texto de link quebram o markdown."""
    return re.sub(r"^\[\d+\]\s*", "", titulo)


def titulo_e_data(caminho: Path):
    """Primeiro título '# ...' e a data de 'Resolvido em: AAAA-MM-DD', se houver."""
    titulo, data = None, "—"
    try:
        with io.open(caminho, encoding="utf-8") as f:
            for linha in f:
                if titulo is None and linha.startswith("# "):
                    titulo = linha[2:].strip()
                m = re.search(r"Resolvido em:\s*(\d{4}-\d{2}-\d{2})", linha)
                if m:
                    data = m.group(1)
                if titulo and data != "—":
                    break
    except OSError:
        pass
    if titulo is None:
        titulo = caminho.stem.replace("_", " ").replace("-", " ").strip()
    return titulo, data


def coletar():
    """Lista de problemas: dicts com categoria, dif, caminho, titulo, data, numero."""
    itens = []
    if not PROBLEMAS.is_dir():
        raise SystemExit(f"Pasta não encontrada: {PROBLEMAS}")
    for categoria in sorted(p for p in PROBLEMAS.iterdir() if p.is_dir()):
        for dif in DIFICULDADES:
            pasta = categoria / dif
            if not pasta.is_dir():
                continue
            for md in sorted(pasta.glob("*.md")):
                titulo, data = titulo_e_data(md)
                m = re.match(r"(\d+)", md.stem)
                itens.append({
                    "categoria": categoria.name,          # ex.: 05_busca_binaria
                    "cat_num": categoria.name.split("_", 1)[0],
                    "dif": dif,
                    "caminho": md,
                    "titulo": titulo,
                    "data": data,
                    "numero": int(m.group(1)) if m else 10**9,
                })
    return itens


def gerar_indice(itens):
    linhas = [
        "# Índice de Problemas",
        "",
        f"> Gerado automaticamente por `gerador_de_indice.py` em {date.today().isoformat()}. Não edite à mão.",
        "",
        "",  # placeholder do resumo (posição 4)
        "",
    ]
    contagem = {d: 0 for d in DIFICULDADES}
    for cat in sorted({i["categoria"] for i in itens}):
        do_cat = [i for i in itens if i["categoria"] == cat]
        linhas += [f"## {nome_categoria(cat)} ({len(do_cat)})", "",
                   "| # | Problema | Dificuldade |", "|---|---|---|"]
        for it in sorted(do_cat, key=lambda x: x["numero"]):
            rel = it["caminho"].relative_to(RAIZ).as_posix()
            linhas.append(f"| {it['numero']:04d} | [{titulo_limpo(it['titulo'])}]({rel}) "
                          f"| {EMOJI[it['dif']]} {it['dif']} |")
            contagem[it["dif"]] += 1
        linhas.append("")
    resumo = " · ".join(f"{EMOJI[d]} {d}: {contagem[d]}" for d in DIFICULDADES)
    linhas[4] = f"**Total: {len(itens)}** ({resumo})"
    if not itens:
        linhas.append("_Nenhum problema resolvido ainda. Bora começar pelo NeetCode 150!_")
    with io.open(INDICE, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(linhas) + "\n")


def atualizar_progresso(itens):
    if not PROGRESSO.is_file():
        print(f"aviso: {PROGRESSO.name} não encontrado — pulei a atualização.")
        return

    with io.open(PROGRESSO, encoding="utf-8") as f:
        texto = f.read()

    # 1) Coluna "Problemas resolvidos" da tabela de padrões (só o último campo numérico)
    por_cat = {}
    for it in itens:
        por_cat[it["cat_num"]] = por_cat.get(it["cat_num"], 0) + 1

    def troca_contagem(m):
        qtd = por_cat.get(m.group("num"), 0)
        return f"{m.group('inicio')} {qtd} |"

    # [ \t]*$ (e não \s*$): \s engoliria a quebra de linha seguinte
    texto = re.sub(
        r"(?m)^(?P<inicio>\|\s*(?P<num>\d{2})\s*\|[^|]*\|[^|]*\|)\s*\d+\s*\|[ \t]*$",
        troca_contagem,
        texto,
    )

    # 2) Lista de resolvidos entre os marcadores AUTO
    if itens:
        bloco = ["| # | Problema | Categoria | Dificuldade | Resolvido em |", "|---|---|---|---|---|"]
        for it in sorted(itens, key=lambda x: x["numero"]):
            rel = it["caminho"].relative_to(RAIZ).as_posix()
            bloco.append(
                f"| {it['numero']:04d} | [{titulo_limpo(it['titulo'])}]({rel}) | {nome_categoria(it['categoria'])} "
                f"| {EMOJI[it['dif']]} {it['dif']} | {it['data']} |"
            )
        conteudo = "\n".join(bloco)
    else:
        conteudo = "_Nenhum problema resolvido ainda._"

    novo_bloco = f"{MARCA_INI}\n{conteudo}\n{MARCA_FIM}"
    if MARCA_INI in texto and MARCA_FIM in texto:
        texto = re.sub(
            re.escape(MARCA_INI) + r".*?" + re.escape(MARCA_FIM),
            novo_bloco.replace("\\", "\\\\"),
            texto,
            flags=re.DOTALL,
        )
    else:  # marcadores ausentes: acrescenta a seção no fim do arquivo
        texto = texto.rstrip("\n") + f"\n\n## ✅ Problemas resolvidos ({len(itens)})\n\n{novo_bloco}\n"

    # 3) Contador no título da seção, se existir
    texto = re.sub(r"## ✅ Problemas resolvidos \(\d+\)", f"## ✅ Problemas resolvidos ({len(itens)})", texto)

    with io.open(PROGRESSO, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def main():
    itens = coletar()
    gerar_indice(itens)
    atualizar_progresso(itens)
    print(f"INDICE.md e PROGRESSO.md atualizados: {len(itens)} problema(s).")


if __name__ == "__main__":
    main()
