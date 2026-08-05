# 🟨 Roadmap Vol. 4 — ARQUITETO

> Alta disponibilidade, multi-tenancy, legados, FinOps, ADRs, comunicação com stakeholders e governança.
>
> Documento consolidado, gerado das pastas `05_arquiteto/` em 2026-08-05. **Edite as pastas, não este arquivo** — regenere com `python roadmap/gerar_volumes.py`. Método de estudo e marcação 🔴🟡🟢: ver `METODO.md`.

## Índice deste volume

1. 🟨 Guia do Nível — ARQUITETO
2. 🛡️ Alta Disponibilidade de Verdade
3. 🏢 Multi-Tenancy
4. 🏚️ Sistemas Legados e Modernização
5. 💰 FinOps — Custo como Requisito de Arquitetura
6. ⚖️ Decisões Técnicas, Trade-offs e ADRs
7. 🗣️ Comunicação com Stakeholders
8. 🏛️ Governança, Segurança Corporativa e Conformidade

---

# 🟨 Guia do Nível — ARQUITETO

> Escopo e sinal de aprovação. Fonte: Volume 3.

---

## 🟨 Nível 4 — ARQUITETO (foco: o sistema como um todo)

**Objetivo:** decidir. E responder pelas decisões perante o negócio.

| Módulo | Escopo |
|---|---|
| **V2 Módulo F** | Alta disponibilidade, multi-região, RTO/RPO |
| **Novo H.5** | Multi-tenancy |
| **Novo H.6** | Sistemas legados e modernização |
| **Novo H.3** | Migração para cloud (estratégias dos 6 R's) |
| **Novo H.8** | FinOps — custo como requisito de arquitetura |
| **Novo I.1** | ⭐ **ADRs e decisões técnicas explícitas** |
| **Novo I.3** | Comunicação com stakeholders |
| **Novo I.4** | Governança, segurança corporativa, compliance |

**🚩 Sinal:** você consegue explicar uma decisão de arquitetura para um diretor **em termos de risco, custo e prazo** — sem usar jargão técnico — e depois explicar a mesma decisão para o time em termos de implementação.

---

# 🛡️ Alta Disponibilidade de Verdade

> Módulo F (Vol. 2): SLA/SLO, multi-região, RTO/RPO, escala elástica, operação segura.

---

# MÓDULO F — Alta Disponibilidade de Verdade
*(entra nas Fases 14 e 15)*

## F.1 Fundamentos de disponibilidade
- [ ] Disponibilidade em números: 99% = 3,65 dias/ano · 99,9% = 8,77h · 99,95% = 4,38h · **99,99% = 52,6 min** · 99,999% = 5,26 min
- [ ] **Disponibilidade em série multiplica**: 5 dependências de 99,9% = 99,5% no total. Cada dependência derruba seu SLA.
- [ ] Redundância em paralelo aumenta disponibilidade — e o custo disso
- [ ] **SLA vs SLO vs SLI** e **error budget** (quando parar de lançar feature e consertar confiabilidade)
- [ ] **MTBF, MTTR, MTTD** — e por que reduzir MTTR costuma valer mais que aumentar MTBF
- [ ] **SPOF (Single Point of Failure)** — mapear todos os seus

## F.2 Topologia
- [ ] N+1, N+2 redundância
- [ ] Multi-AZ (zona de disponibilidade) — o mínimo aceitável em produção
- [ ] **Multi-região**: active-passive (DR) vs **active-active** (e o inferno de resolução de conflito)
- [ ] Roteamento global: DNS geográfico, **Anycast**, GSLB
- [ ] **RTO** (quanto tempo até voltar) e **RPO** (quanto dado posso perder) — definir isso *antes* de escolher a arquitetura
- [ ] Plano de Disaster Recovery e — o ponto crítico — **testar o restore de backup** (backup não testado não é backup)
- [ ] Failover automático vs manual; quem decide, e o risco de flapping

## F.3 Escala elástica
- [ ] Escala horizontal e o pré-requisito: **aplicação stateless** (Twelve-Factor)
- [ ] Onde colocar o estado quando a app é stateless (Redis, banco, object storage)
- [ ] **Auto-scaling por métrica certa**: CPU é péssimo indicador para serviço I/O-bound. Escale por **tamanho de fila, saturação de conexões, latência p99 ou requests em voo**
- [ ] Predictive scaling e scheduled scaling (pico previsível — ex: início de turno na fábrica)
- [ ] Warm-up: por que instância nova recém-criada tem p99 ruim (JIT frio, cache vazio, pool vazio) e como mitigar (pre-warming, slow start no LB)
- [ ] Kubernetes HPA/VPA/KEDA (escala por métrica de evento)
- [ ] Limites de escala: o banco quase sempre é o gargalo final

## F.4 Operação segura
- [ ] Deploy sem downtime: rolling, **blue-green**, **canary** (com métrica automática de rollback)
- [ ] **Feature flags** — desacoplar deploy de release
- [ ] Migração de schema compatível para frente e para trás (expand → migrate → contract)
- [ ] **Graceful shutdown**: parar de aceitar novas conexões, drenar as em andamento, então morrer (retoma `SIGTERM`, Fase 4.10)
- [ ] Readiness vs liveness probe — e por que confundir os dois causa restart em cascata
- [ ] **Chaos Engineering** — injetar falha de propósito (Chaos Monkey, Litmus); começar em staging
- [ ] **Game days** e simulação de incidente
- [ ] Runbooks e postmortem sem culpa

---

# 🏢 Multi-Tenancy

> Módulo H.5 (Vol. 3). Central para plataforma que atende vários prédios/clientes.

---

## H.5 Multi-Tenancy
> Faltava por completo e é **central** para o tipo de produto que você pode construir (uma plataforma que atende vários prédios/clientes).

- [ ] O que é tenant e por que multi-tenancy é decisão de arquitetura, não de código
- [ ] **Os três modelos de isolamento de dados**:
  - [ ] **Banco por tenant** — isolamento máximo, custo e operação máximos
  - [ ] **Schema por tenant** — meio-termo (Postgres faz bem)
  - [ ] **Tabela compartilhada com `tenant_id`** — mais barato e escalável, mas o risco de vazamento entre tenants é real
- [ ] Como escolher: número de tenants, exigência regulatória, tamanho de cada tenant, custo
- [ ] **Identificação do tenant**: subdomínio, header, claim no JWT, path
- [ ] Propagação do contexto de tenant (ThreadLocal / `ScopedValue`, e o cuidado com pool de threads e código assíncrono)
- [ ] **Row-Level Security** (Postgres) como rede de segurança contra bug de aplicação
- [ ] Filtro automático de tenant no Hibernate (`@Filter`, `@TenantId`)
- [ ] **Noisy neighbor** — um tenant consumindo tudo; mitigar com rate limit e quota por tenant
- [ ] Migração de schema com N tenants (o problema operacional de rodar a mesma migration 500 vezes)
- [ ] Backup, restore e exportação **por tenant** (exigência de LGPD)
- [ ] Onboarding e offboarding automatizado de tenant
- [ ] Customização por tenant: feature flags, configuração, white-label
- [ ] Métricas e custo **por tenant** (conecta com FinOps)

---

# 🏚️ Sistemas Legados e Modernização

> Módulo H.6 (Vol. 3).

---

## H.6 Sistemas legados e modernização
> Você vai passar mais tempo da carreira mexendo em código existente do que criando do zero. Ninguém prepara para isso.

- [ ] Como ler e mapear um sistema que você não escreveu (comece pelo build, depois pelos pontos de entrada, depois pelo banco)
- [ ] **Characterization tests** — criar rede de segurança antes de mudar (Michael Feathers)
- [ ] Seams e pontos de injeção para tornar código legado testável
- [ ] Refatoração incremental e segura (nunca reescrita total — a "Grande Reescrita" quase sempre falha)
- [ ] **Strangler Fig** na prática: rotear tráfego gradualmente do legado para o novo
- [ ] **Anti-Corruption Layer** entre o novo e o legado
- [ ] **Branch by Abstraction**
- [ ] Migração de dados: dual write, backfill, reconciliação, cutover
- [ ] Como decidir: refatorar × reescrever × substituir × manter (e o custo de oportunidade de cada um)
- [ ] Documentar o que existe (muitas vezes você é a primeira pessoa a fazer isso)
- [ ] **Realidade brasileira:** boa parte das vagas pleno/sênior é manutenção e modernização de sistema legado, não greenfield.

---

# 💰 FinOps — Custo como Requisito de Arquitetura

> Módulo H.8 (Vol. 3).

---

## H.8 FinOps — custo como requisito de arquitetura
- [ ] Modelos de precificação: sob demanda, reservado, **spot**, savings plan
- [ ] Os custos que surpreendem: **transferência de dados de saída (egress)**, cross-AZ traffic, NAT gateway, requisições em object storage, log retido
- [ ] Custo por requisição / por tenant / por feature — **unit economics**
- [ ] Rightsizing — a maioria dos ambientes está superdimensionada
- [ ] Trade-off explícito: cache custa memória mas economiza banco; serverless é barato em baixo tráfego e caro em alto
- [ ] Tagging e alocação de custo por time/produto
- [ ] Orçamento e alerta de anomalia de custo
- [ ] **Custo como requisito não-funcional**, ao lado de latência e disponibilidade
- [ ] Custo de arquitetura ≠ custo de infraestrutura: microsserviços custam em observabilidade, deploy, rede e **tempo de gente**

---

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

---

# 🗣️ Comunicação com Stakeholders

> Módulo I.3 (Vol. 3).

---

## I.3 Comunicação com stakeholders
- [ ] Traduzir técnico ↔ negócio: falar em **risco, custo, prazo e impacto no usuário** — não em "precisamos refatorar"
- [ ] Como justificar débito técnico para quem não é técnico (analogia de juros funciona bem)
- [ ] Estimativas: por que são ruins, como dar mesmo assim (faixas, não números; intervalo de confiança)
- [ ] Dizer "não" ou "ainda não" com alternativa concreta
- [ ] Escrita técnica clara: RFC, one-pager, proposta de arquitetura
- [ ] Apresentar decisão técnica para diretoria: comece pela conclusão e pelo impacto, detalhe depois
- [ ] Comunicação durante incidente: status frequente, linguagem simples, sem culpa
- [ ] Gestão de expectativa e negociação de escopo
- [ ] Documentar para o futuro (inclusive para você daqui a 6 meses)

---

# 🏛️ Governança, Segurança Corporativa e Conformidade

> Módulo I.4 (Vol. 3).

---

## I.4 Governança, segurança corporativa e conformidade
- [ ] Gestão de identidade corporativa: SSO, **SAML**, OIDC, Active Directory/LDAP, SCIM (provisionamento)
- [ ] Segregação de ambientes e de funções (quem pode fazer deploy em produção?)
- [ ] Trilha de auditoria (**audit log**) — quem fez o quê, quando; imutável
- [ ] Gestão de segredos corporativa e rotação obrigatória
- [ ] **LGPD** na prática: base legal, consentimento, minimização, **direito ao esquecimento** (e o conflito com event sourcing e backup), anonimização vs pseudonimização, relatório de impacto
- [ ] Classificação de dados e criptografia em repouso e em trânsito
- [ ] Gestão de vulnerabilidade: **SCA** (dependências — Dependabot, Snyk), **SAST**, **DAST**, pentest
- [ ] SBOM e supply chain security (ataques via dependência são crescentes)
- [ ] Frameworks e normas: ISO 27001, SOC 2, NIST, **OWASP SAMM** — saber que existem e o que exigem
- [ ] Continuidade de negócio e plano de resposta a incidente de segurança
- [ ] Governança de arquitetura: guilda/comitê, padrões, exceções documentadas
