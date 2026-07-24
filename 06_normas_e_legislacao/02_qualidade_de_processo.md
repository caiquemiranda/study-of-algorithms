# 🔄 Qualidade de Processo — 12207, CMMI, MPS.BR, DORA

> Parte II (Vol. 4).

---

# PARTE II — Qualidade de Processo

## II.1 ISO/IEC/IEEE 12207 — Ciclo de vida de software
- [ ] Os grupos de processo: acordo, organizacionais, técnicos de gestão, técnicos
- [ ] Processos técnicos: análise de requisitos → arquitetura → projeto → implementação → integração → verificação → transição → validação → operação → manutenção → descarte
- [ ] **ISO/IEC/IEEE 15288** — o equivalente para sistemas (hardware + software) — mais relevante para você, que trabalha com sistemas físicos
- [ ] Como isso mapeia (ou não) em Scrum/Kanban — as normas descrevem *o que* precisa acontecer, não *como*

## II.2 CMMI — Capability Maturity Model Integration
- [ ] Origem: SEI/Carnegie Mellon; hoje mantido pela ISACA
- [ ] **Os 5 níveis de maturidade**:
  1. **Inicial** — caótico, dependente de heróis
  2. **Gerenciado** — processos existem por projeto, planejamento e controle básicos
  3. **Definido** — processos padronizados na organização
  4. **Gerenciado Quantitativamente** — decisões por dados estatísticos
  5. **Em Otimização** — melhoria contínua baseada em dados
- [ ] Representação por estágios vs contínua
- [ ] Onde aparece: exigência em contrato com governo, multinacional e defesa
- [ ] Crítica honesta: CMMI mal aplicado vira burocracia. Bem aplicado, dá previsibilidade real.

## II.3 MPS.BR — o modelo brasileiro
> Muito relevante no Brasil e quase desconhecido por devs. Aparece em edital público.

- [ ] Criado pela **SOFTEX**, adaptado à realidade de PMEs brasileiras (CMMI é caro para empresa pequena)
- [ ] **7 níveis, de G (mais baixo) a A (mais alto)**:
  - **G** — Parcialmente Gerenciado
  - **F** — Gerenciado
  - **E** — Parcialmente Definido
  - **D** — Largamente Definido
  - **C** — Definido
  - **B** — Gerenciado Quantitativamente
  - **A** — Em Otimização
- [ ] Guias: MPS.BR Software (MPS-SW), Serviços (MPS-SV), Gestão de Pessoas, RH
- [ ] Compatível com CMMI e ISO/IEC 12207
- [ ] **Vantagem para você:** empresa de engenharia que quer vender para governo ou grande cliente frequentemente precisa disso — e alguém tem que entender

## II.4 ISO/IEC 33000 (ex-15504 / SPICE)
- [ ] Avaliação de capacidade de processo
- [ ] Níveis de capacidade 0 a 5 (Incompleto → Executado → Gerenciado → Estabelecido → Previsível → Inovador)
- [ ] Substituiu a antiga ISO/IEC 15504 (SPICE)
- [ ] Derivados setoriais: **Automotive SPICE** (indústria automotiva)

## II.5 Métricas modernas de engenharia (o contraponto ágil)
> As normas acima são pesadas. Estas são leves, orientadas a dados e é o que empresa de tecnologia usa hoje.

- [ ] **DORA — as 4 métricas-chave** (do livro *Accelerate*):
  1. **Frequência de deploy**
  2. **Lead time para mudança** (commit → produção)
  3. **Taxa de falha de mudança** (% de deploys que causam incidente)
  4. **Tempo para restaurar serviço** (MTTR)
  - *(uma quinta foi adicionada: confiabilidade / desempenho operacional)*
- [ ] Os 4 perfis: Elite, High, Medium, Low performers
- [ ] A descoberta contra-intuitiva do *Accelerate*: **velocidade e estabilidade não são trade-off** — quem entrega mais rápido também quebra menos
- [ ] **Framework SPACE** — produtividade de desenvolvedor além de linhas de código: Satisfaction, Performance, Activity, Communication, Efficiency
- [ ] ⚠️ Nunca use métrica de indivíduo como avaliação de pessoa — vira jogo de números e destrói o time

**📚 Referências da Parte II:**
- *Accelerate* — Forsgren, Humble & Kim (**leitura obrigatória**; é o único livro dessa parte que é prazeroso de ler)
- *SWEBOK Guide* (IEEE Computer Society) — o corpo de conhecimento de Engenharia de Software; **v4 disponível gratuitamente**, é o índice mestre da disciplina
- Guias do MPS.BR — **gratuitos** no site da SOFTEX
- *Engenharia de Software* — Ian Sommerville (o livro-texto clássico, em PT-BR — cobre normas e processos)
- *Engenharia de Software: Uma Abordagem Profissional* — Pressman & Maxim
