# -*- coding: utf-8 -*-
"""Gera o INDICE.md a partir das soluções em problemas/<categoria>/<dificuldade>/*.md

Uso:  python gerador_de_indice.py
"""
import io
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
PROBLEMAS = RAIZ / "problemas"
SAIDA = RAIZ / "INDICE.md"
DIFICULDADES = ["easy", "medium", "hard"]
EMOJI = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}


def titulo(caminho: Path) -> str:
    """Usa o primeiro título '# ...' do arquivo; senão, deriva do nome."""
    try:
        with io.open(caminho, encoding="utf-8") as f:
            for linha in f:
                if linha.startswith("# "):
                    return linha[2:].strip()
    except OSError:
        pass
    return caminho.stem.replace("_", " ").replace("-", " ").strip()


def main() -> None:
    linhas = [
        "# Índice de Problemas",
        "",
        f"> Gerado automaticamente por `gerador_de_indice.py` em {date.today().isoformat()}. Não edite à mão.",
        "",
    ]
    total_geral = 0
    contagem = {d: 0 for d in DIFICULDADES}

    if not PROBLEMAS.is_dir():
        raise SystemExit(f"Pasta não encontrada: {PROBLEMAS}")

    for categoria in sorted(p for p in PROBLEMAS.iterdir() if p.is_dir()):
        solucoes = []
        for dif in DIFICULDADES:
            pasta = categoria / dif
            if pasta.is_dir():
                for md in sorted(pasta.glob("*.md")):
                    solucoes.append((dif, md))
        if not solucoes:
            continue

        nome_cat = categoria.name.split("_", 1)[-1].replace("_", " ").title()
        linhas += [f"## {nome_cat} ({len(solucoes)})", "", "| Problema | Dificuldade |", "|---|---|"]
        for dif, md in solucoes:
            rel = md.relative_to(RAIZ).as_posix()
            linhas.append(f"| [{titulo(md)}]({rel}) | {EMOJI[dif]} {dif} |")
            contagem[dif] += 1
            total_geral += 1
        linhas.append("")

    resumo = " · ".join(f"{EMOJI[d]} {d}: {contagem[d]}" for d in DIFICULDADES)
    linhas.insert(4, f"**Total: {total_geral}** ({resumo})")
    linhas.insert(5, "")
    if total_geral == 0:
        linhas.append("_Nenhum problema resolvido ainda. Bora começar pelo NeetCode 150!_")

    with io.open(SAIDA, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(linhas) + "\n")
    print(f"INDICE.md atualizado: {total_geral} problema(s).")


if __name__ == "__main__":
    main()
