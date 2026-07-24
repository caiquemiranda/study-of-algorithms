# ⚖️ Decisões Técnicas, Trade-offs e ADRs

> Módulo I.1 (Vol. 3).

---

## I.1 Decisões técnicas e trade-offs
- [ ] **Não existe solução certa, existe trade-off adequado ao contexto.** Toda decisão de arquitetura troca algo por algo.
- [ ] Os eixos de trade-off recorrentes: consistência × disponibilidade · latência × custo · simplicidade × flexibilidade · velocidade de entrega × qualidade · acoplamento × duplicação
- [ ] **ADR (Architecture Decision Record)** — o formato: contexto, decisão, alternativas consideradas, consequências. **Comece a usar hoje**, mesmo sozinho: em 6 meses você não lembra por que decidiu aquilo.
- [ ] Requisitos **não funcionais** como cidadãos de primeira classe: latência, disponibilidade, segurança, custo, manutenibilidade, observabilidade
- [ ] **Atributos de qualidade** e como priorizá-los com o negócio (você não maximiza todos)
- [ ] Análise de risco: o que acontece se isso falhar? qual o raio de impacto?
- [ ] Decisões reversíveis (**one-way vs two-way doors**, Bezos) — decisão reversível pode ser rápida; irreversível merece rigor
- [ ] Combater o *resume-driven development* — escolher tecnologia pelo problema, não pelo currículo
- [ ] **"Boring technology"** — por que escolher o chato e testado quase sempre vence
- [ ] Documentação de arquitetura: **Modelo C4** (contexto, contêiner, componente, código), diagramas que envelhecem bem
- [ ] Prova de conceito e spike para reduzir incerteza antes de decidir
