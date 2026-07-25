# -*- coding: utf-8 -*-
"""Orquestrador headless: gera docs de estudo, UM problema por sessão fresca do Claude.

Cada problema roda em `claude -p "/leetcode-doc <id>"` — contexto zerado a cada doc
(zero fadiga de lote). O orquestrador valida mecanicamente cada doc gerado; só doc
aprovado vira 'documentado' na fila. Reprovado vai para rejeitados/ e é retentado 1x.

Uso:
  python gerar_docs.py --n 10          Gera os próximos 10 pendentes da fila (com cache)
  python gerar_docs.py --ids 58,169    Gera problemas específicos
  python gerar_docs.py --dry           Só lista o que seria gerado, sem chamar a IA
  python gerar_docs.py --revisar       Inclui também os marcados como 'revisar'
"""
import argparse
import io
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import lc_fetch  # mesmo diretório: reusa fila, cache e validação

AQUI = Path(__file__).resolve().parent
RAIZ_REPO = lc_fetch.RAIZ_EDA.parent          # skills do projeto vivem em <repo>/.claude/skills
LOGS = AQUI / "logs"
REJEITADOS = AQUI / "rejeitados"
TIMEOUT_SESSAO = 900                          # 15 min por doc é folga generosa


def rodar_claude(numero, log):
    comando = f'claude -p "/leetcode-doc {numero}" --permission-mode acceptEdits'
    with io.open(log, "a", encoding="utf-8", newline="\n") as f:
        f.write(f"\n===== {time.strftime('%Y-%m-%d %H:%M:%S')} | {comando}\n")
        try:
            r = subprocess.run(comando, shell=True, cwd=RAIZ_REPO, timeout=TIMEOUT_SESSAO,
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            f.write(r.stdout or "")
            f.write(r.stderr or "")
            return r.returncode == 0
        except subprocess.TimeoutExpired:
            f.write("TIMEOUT da sessão\n")
            return False


def processar(item):
    """Gera + valida um problema. Retorna (status_final, erros)."""
    numero = item["id"]
    log = LOGS / f"{numero:04d}.log"
    doc = lc_fetch.achar_doc(numero)
    if doc:                                              # já existe: só valida
        erros = lc_fetch.validar_doc(doc, item)
        return ("documentado", []) if not erros else ("revisar", erros)

    for tentativa in (1, 2):
        rodar_claude(numero, log)
        doc = lc_fetch.achar_doc(numero)
        erros = ["doc não foi criado"] if not doc else lc_fetch.validar_doc(doc, item)
        if not erros:
            return "documentado", []
        if doc:                                          # guarda a versão reprovada e tenta de novo
            REJEITADOS.mkdir(exist_ok=True)
            destino = REJEITADOS / f"{doc.stem}_t{tentativa}.md"
            doc.replace(destino)
        with io.open(log, "a", encoding="utf-8", newline="\n") as f:
            f.write(f"REPROVADO (tentativa {tentativa}): {erros}\n")
    return "revisar", erros


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--ids", type=str, default=None)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--revisar", action="store_true")
    args = ap.parse_args()

    fila = lc_fetch.carregar_fila()
    if not fila["problemas"]:
        sys.exit("Fila vazia. Rode: python lc_fetch.py catalogo")
    por_id = {p["id"]: p for p in fila["problemas"]}

    if args.ids:
        selecao = [por_id[int(x)] for x in args.ids.split(",") if int(x) in por_id]
    else:
        aceitos = {"pendente", "baixado"} | ({"revisar"} if args.revisar else set())
        selecao = [p for p in fila["problemas"] if p["status"] in aceitos][:args.n]

    com_cache, sem_cache = [], []
    for p in selecao:
        (com_cache if lc_fetch.caminho_cache(p).is_file() else sem_cache).append(p)
    if sem_cache:
        print(f"aviso: {len(sem_cache)} sem enunciado no cache — rode lc_fetch.py baixar-tudo. Pulados:")
        print("  " + ", ".join(str(p["id"]) for p in sem_cache))
    if not com_cache:
        sys.exit("Nada a gerar.")

    print(f"{len(com_cache)} problema(s) a documentar, um por sessão fresca:")
    for p in com_cache:
        print(f"  {p['id']:>4} [{p['dif']:<6}] {p['categoria']:<28} {p['titulo']}")
    if args.dry:
        return

    LOGS.mkdir(exist_ok=True)
    ok = falhas = 0
    inicio = time.time()
    for i, p in enumerate(com_cache, 1):
        print(f"\n[{i}/{len(com_cache)}] {p['id']} {p['titulo']} ...", flush=True)
        status, erros = processar(p)
        p["status"], p["lote"] = status, None
        lc_fetch.salvar_fila(fila)                       # checkpoint por problema
        if status == "documentado":
            ok += 1
            print(f"  ✔ ok — {lc_fetch.achar_doc(p['id']).relative_to(lc_fetch.RAIZ_EDA)}")
        else:
            falhas += 1
            print(f"  ✖ revisar — {erros[:3]} (log: logs/{p['id']:04d}.log)")

    # fechamento mecânico: índice, progresso e fila sincronizados
    subprocess.run([sys.executable, str(lc_fetch.RAIZ_EDA / "gerador_de_indice.py")], cwd=lc_fetch.RAIZ_EDA)
    minutos = (time.time() - inicio) / 60
    print(f"\nResumo: {ok} documentados, {falhas} para revisar, em {minutos:.1f} min.")
    if falhas:
        print("Reprovados guardados em rejeitados/ — rode com --revisar para retentar, "
              "ou gere manualmente com /leetcode-doc <id> numa sessão interativa.")


if __name__ == "__main__":
    main()
