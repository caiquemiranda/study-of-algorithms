# ⭐ Qualidade de Produto — ISO/IEC 25010

> Parte I (Vol. 4). Se estudar só uma norma, que seja esta.

---

# PARTE I — Qualidade de Produto: ISO/IEC 25010

> **Se você só estudar uma norma da vida, que seja esta.** Ela é o vocabulário universal de qualidade de software.

## A família SQuaRE (ISO/IEC 25000)
- [ ] **ISO/IEC 2500n** — Divisão de gestão de qualidade (conceitos gerais)
- [ ] **ISO/IEC 25010** — ⭐ Modelo de qualidade de produto (o coração)
- [ ] **ISO/IEC 25012** — Modelo de qualidade de **dados**
- [ ] **ISO/IEC 25019** — Qualidade em uso / experiência
- [ ] **ISO/IEC 2502n** — Medição de qualidade (métricas)
- [ ] **ISO/IEC 2503n** — Requisitos de qualidade
- [ ] **ISO/IEC 2504n** — Avaliação de qualidade
- [ ] **ISO/IEC 25040** — Processo de avaliação
- [ ] No Brasil: adotadas como **ABNT NBR ISO/IEC 25010** etc.

## As características de qualidade (ISO/IEC 25010:2023 — 9 características)

> ⚠️ A versão de **2011** tinha 8 características (com *Usabilidade* e *Portabilidade*). A revisão de **2023** reorganizou para 9, incluindo **Segurança física (Safety)**. Muitos editais e livros ainda citam a versão de 2011 — conheça as duas.

| # | Característica | Subcaracterísticas | Onde isso aparece no seu roadmap |
|---|---|---|---|
| 1 | **Adequação Funcional** | Completude, correção, adequação | Requisitos, testes funcionais |
| 2 | **Eficiência de Desempenho** | Comportamento temporal, uso de recursos, capacidade | **Vol 2 Módulo B (p99)** |
| 3 | **Compatibilidade** | Coexistência, interoperabilidade | APIs, protocolos (Vol 2 Módulo A) |
| 4 | **Capacidade de Interação** (antes *Usabilidade*) | Reconhecibilidade, aprendizado, operabilidade, proteção contra erro, estética, **acessibilidade** | Parte VII deste doc |
| 5 | **Confiabilidade** | Maturidade, **disponibilidade**, tolerância a falha, recuperabilidade | **Vol 2 Módulo F** |
| 6 | **Segurança (Security)** | Confidencialidade, integridade, não-repúdio, responsabilização, autenticidade, resistência | Fase 6.8, Parte V deste doc |
| 7 | **Manutenibilidade** | Modularidade, reusabilidade, analisabilidade, modificabilidade, testabilidade | Fases 11 e 13 |
| 8 | **Flexibilidade** (absorveu *Portabilidade*) | Adaptabilidade, **escalabilidade**, instalabilidade, substituibilidade | Vol 2 Módulos D/E/F |
| 9 | **Segurança física (Safety)** 🆕 | Restrição operacional, identificação de risco, à prova de falha, aviso, integração segura | Parte X — **seu domínio** |

**Como usar isso na prática:**
- [ ] Ao levantar requisitos, percorra as 9 características e pergunte: *"qual o requisito não funcional aqui?"* — isso sozinho já te coloca acima da média
- [ ] Transformar cada uma em requisito **mensurável**: não "o sistema deve ser rápido", mas "p95 abaixo de 300ms com 500 usuários concorrentes"
- [ ] Priorizar: você **não maximiza todas**. Segurança conflita com usabilidade; performance conflita com manutenibilidade. Escolher é o trabalho do arquiteto.

**✅ Exercício:** pegue um sistema que você conhece e escreva um requisito mensurável para cada uma das 9 características.
