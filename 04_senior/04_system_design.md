# 📐 System Design e Escala

> Fase 14 (Vol. 1).

---

# FASE 14 — System Design e Escala [AMPLIAÇÃO]

## 14.1 Conceitos fundamentais
- [ ] **Performance vs Escalabilidade** (não são a mesma coisa)
- [ ] **Latência vs Throughput**
- [ ] Escala **vertical** vs **horizontal**
- [ ] **Disponibilidade vs Consistência** — **Teorema CAP** (AP vs CP) e a nuance do **PACELC**
- [ ] Padrões de consistência: fraca, eventual, forte
- [ ] Padrões de disponibilidade: **fail-over** (active-passive, active-active), **replicação** (master-slave, master-master)
- [ ] **Disponibilidade em números**: 99,9% (três noves) = ~8,7h/ano de downtime; 99,99% = ~52min/ano
- [ ] Disponibilidade em série vs em paralelo (por que cada dependência derruba seu SLA)
- [ ] SLA, SLO, SLI e *error budget*

## 14.2 Componentes de sistema
- [ ] **DNS** como camada de roteamento e balanceamento (round-robin, geo, latência)
- [ ] **CDN** — pull vs push, edge, invalidação
- [ ] **Load Balancer**: algoritmos (round-robin, least connections, IP hash, weighted), **Layer 4 vs Layer 7**, health check, LB vs Reverse Proxy
- [ ] Camada de aplicação stateless e service discovery
- [ ] **Caching**: onde cachear (cliente, CDN, web server, aplicação, banco)
- [ ] Estratégias de cache: **Cache-Aside** (lazy loading), **Write-Through**, **Write-Behind**, **Refresh-Ahead**
- [ ] Invalidação de cache, TTL, **cache stampede/thundering herd** e como mitigar
- [ ] **Assincronismo**: task queues, message queues, **back pressure**
- [ ] **Operações idempotentes** — a chave de sistema distribuído confiável
- [ ] Comunicação: HTTP/TCP/UDP, RPC, gRPC, REST, GraphQL — trade-offs em sistema distribuído
- [ ] Background jobs: event-driven vs schedule-driven

## 14.3 Padrões de confiabilidade
- [ ] **Circuit Breaker** (closed → open → half-open)
- [ ] **Retry** com backoff exponencial + jitter
- [ ] **Bulkhead** (isolamento de recursos)
- [ ] **Timeout** em toda chamada externa
- [ ] **Rate Limiting / Throttling**
- [ ] **Graceful Degradation** — degradar funcionalidade em vez de cair
- [ ] **Load Shedding** — recusar carga excedente conscientemente
- [ ] **Queue-Based Load Leveling**
- [ ] Health Endpoint Monitoring
- [ ] Leader Election
- [ ] Compensating Transaction
- [ ] Scheduler Agent Supervisor
- [ ] Federated Identity, Gatekeeper, Valet Key (padrões de segurança)

## 14.4 Padrões de dados e mensageria em nuvem
- [ ] Sharding, Materialized View, Index Table, Event Sourcing, CQRS, Cache-Aside
- [ ] Publisher/Subscriber, Competing Consumers, Priority Queue, Claim Check, Sequential Convoy, Async Request-Reply, Choreography, Pipes and Filters

## 14.5 Prática de System Design
- [ ] Framework de resposta em entrevista: requisitos (funcionais e **não funcionais**) → estimativa de escala → API → modelo de dados → desenho de alto nível → gargalos → trade-offs
- [ ] **Back-of-the-envelope estimation** — QPS, storage, banda
- [ ] Projetar: encurtador de URL, feed de rede social, chat, rate limiter distribuído, sistema de notificação, upload de vídeo, busca de tempo real
- [ ] **Projete o sistema que você já conhece**: uma plataforma de monitoramento de alarmes de incêndio multi-prédio, com ingestão de telemetria, alertas em tempo real e histórico — isso vale mais no seu currículo que qualquer clone genérico

**📚 Livros:**
- ⭐ *Designing Data-Intensive Applications* — **Martin Kleppmann** — de novo. É o livro central desta fase.
- *System Design Interview, Vol. 1 e 2* — Alex Xu (formato de entrevista, muito prático)
- *Understanding Distributed Systems* — Roberto Vitillo (excelente e acessível)
- *Release It!* — **Michael Nygard** (2ª ed.) — padrões de estabilidade (Circuit Breaker vem daqui); leitura obrigatória para quem opera sistema em produção
- *The System Design Primer* (GitHub, **gratuito** — `donnemartin/system-design-primer`) — é a base do roadmap de System Design que você printou
- *Web Scalability for Startup Engineers* — Artur Ejsmont
