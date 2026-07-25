# -*- coding: utf-8 -*-
"""Gera os volumes consolidados (um .md por nível) a partir das pastas de estudo.

As PASTAS (01_junior/, 03_pleno/, ...) são a fonte da verdade — edite lá.
Depois rode:  python roadmap/gerar_volumes.py
"""
import io
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = Path(__file__).resolve().parent

VOLUMES = [
    ("roadmap-vol1-junior.md", "🟦 Roadmap Vol. 1 — JÚNIOR",
     "Fundamentos: ferramentas, computação, SQL, APIs, Java/Spring, testes, debugging — mais a teoria da trilha de Estruturas de Dados e Algoritmos.",
     ["01_junior", "02_estruturas_e_algoritmos"]),
    ("roadmap-vol2-pleno.md", "🟧 Roadmap Vol. 2 — PLENO",
     "A web sem frameworks (16 pilares), SQL avançado, segurança de APIs, JVM, Docker/CI/CD, mensageria, SOLID, FastAPI, TypeScript e IA aplicada.",
     ["03_pleno"]),
    ("roadmap-vol3-senior.md", "🟩 Roadmap Vol. 3 — SÊNIOR",
     "C++, Go, arquiteturas, system design, observabilidade, redes a fundo, latência p99, sistemas distribuídos, alta escrita/leitura, cloud e liderança técnica.",
     ["04_senior"]),
    ("roadmap-vol4-arquiteto.md", "🟨 Roadmap Vol. 4 — ARQUITETO",
     "Alta disponibilidade, multi-tenancy, legados, FinOps, ADRs, comunicação com stakeholders e governança.",
     ["05_arquiteto"]),
    ("roadmap-vol5-normas.md", "⚖️ Roadmap Vol. 5 — NORMAS, QUALIDADE E LEGISLAÇÃO",
     "ISO 25010, CMMI/MPS.BR, ISO 29119, OWASP, métricas de código, acessibilidade, LGPD/GDPR/CRA, sistemas críticos (IEC 61508/62443), IA e governança de TI.",
     ["06_normas_e_legislacao"]),
    ("roadmap-vol6-projetos.md", "🏗️ Roadmap Vol. 6 — PROJETOS-ÂNCORA",
     "Os 7 projetos que integram tudo: do mini-framework web ao capstone de monitoramento predial.",
     ["07_projetos"]),
]

IGNORAR = {"PROGRESSO.md", "INDICE.md"}


def arquivos_de(pasta: Path):
    return [p for p in sorted(pasta.glob("*.md")) if p.name not in IGNORAR]


def titulo_de(md: Path) -> str:
    with io.open(md, encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("# "):
                return linha[2:].strip()
    return md.stem


def main() -> None:
    for nome, titulo, descricao, pastas in VOLUMES:
        fontes = []
        for pasta in pastas:
            fontes += arquivos_de(RAIZ / pasta)
        if not fontes:
            print(f"aviso: nenhuma fonte para {nome}")
            continue

        indice = "\n".join(f"{i+1}. {titulo_de(p)}" for i, p in enumerate(fontes))
        cabecalho = (
            f"# {titulo}\n\n"
            f"> {descricao}\n>\n"
            f"> Documento consolidado, gerado das pastas `{'`, `'.join(pastas)}/` em {date.today().isoformat()}."
            " **Edite as pastas, não este arquivo** — regenere com `python roadmap/gerar_volumes.py`."
            " Método de estudo e marcação 🔴🟡🟢: ver `METODO.md`.\n\n"
            "## Índice deste volume\n\n" + indice
        )
        partes = [cabecalho]
        for p in fontes:
            with io.open(p, encoding="utf-8") as f:
                partes.append(f.read().strip("\n"))

        saida = DESTINO / nome
        with io.open(saida, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n\n---\n\n".join(partes) + "\n")
        linhas = sum(1 for _ in io.open(saida, encoding="utf-8"))
        print(f"ok {nome} ({len(fontes)} seções, {linhas} linhas)")


if __name__ == "__main__":
    main()
