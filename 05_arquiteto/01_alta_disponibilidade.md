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
