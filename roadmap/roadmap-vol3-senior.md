# 🟩 Roadmap Vol. 3 — SÊNIOR

> C++, Go, arquiteturas, system design, observabilidade, redes a fundo, latência p99, sistemas distribuídos, alta escrita/leitura, cloud e liderança técnica.
>
> Documento consolidado, gerado das pastas `04_senior/` em 2026-07-24. **Edite as pastas, não este arquivo** — regenere com `python roadmap/gerar_volumes.py`. Método de estudo e marcação 🔴🟡🟢: ver `METODO.md`.

## Índice deste volume

1. 🟩 Guia do Nível — SÊNIOR
2. ⚙️ C++ e Baixa Abstração
3. 🐹 Go — Concorrência
4. 🏛️ Arquiteturas de Aplicação e Sistema + Spring Cloud
5. 📐 System Design e Escala
6. 🔭 Observabilidade e Confiabilidade
7. 🌐 Redes e Protocolos a Fundo
8. ⚡ Engenharia de Latência de Cauda (p99)
9. 🕸️ Sistemas Distribuídos — a Teoria
10. 📈 Backends de Alta Escrita e Alta Leitura
11. 🔬 Metodologia — Provar que é Rápido e Disponível
12. ☁️ Cloud a Sério
13. 👥 Code Review, Mentoria e Liderança Técnica

---

# 🟩 Guia do Nível — SÊNIOR

> Escopo, estimativa e sinal de aprovação (Vol. 3) + cronograma de encaixe do Vol. 2.

---

## 🟩 Nível 3 — SÊNIOR (foco: sistemas escaláveis e resilientes)

**Objetivo:** responsável pela qualidade técnica do sistema, não só pelo código.

| Fase / Módulo | Escopo |
|---|---|
| **Fase 3** | C++ (agora sim; a essa altura você aproveita muito mais) |
| **Fase 8** | Go |
| **Fase 13** | 13.3 a 13.5 (Clean/Hexagonal/DDD/CQRS + antipadrões) |
| **Fase 14** | Toda (System Design) |
| **Fase 15** | Toda (Observabilidade) |
| **V2 Módulo A** | Redes e protocolos a fundo |
| **V2 Módulo B** | ⭐ **Latência de cauda / p99** — é *o* tema de sênior |
| **V2 Módulo C** | ⭐ **Sistemas distribuídos** — consenso, quórum, relógios lógicos |
| **V2 Módulos D/E** | Alta escrita e alta leitura |
| **V2 Módulo G** | Metodologia de performance e teste de carga |
| **Novo** | Módulo H.3 (Cloud) e **Módulo I.2 (code review e mentoria)** |
| **Projeto** | Projeto 7 — o capstone |

**⏱️ Estimativa:** +18 a 24 meses.

**🚩 Sinal de que passou:** te dão um requisito de negócio e você desenha a arquitetura, justifica cada trade-off com dados e antecipa os modos de falha. E outras pessoas melhoram tecnicamente por trabalhar com você.

---

# 🎯 Como encaixar tudo isso no cronograma

Não estude este volume linearmente. Encaixe assim:

| Quando | O que estudar deste volume |
|---|---|
| Durante a **Fase 1** (redes) | Módulo A.1 a A.4 |
| Durante a **Fase 4** (web sem framework) | Módulo A.2, A.6, e a tabela A.7 |
| Durante a **Fase 5** (banco) | Módulo D.1 (LSM vs B-Tree, WAL) |
| Durante a **Fase 6** (APIs) | Módulo A.5 (MQTT — seu diferencial), A.7 |
| Após a **Fase 12** (Docker/CI) | **Módulo B inteiro** + Módulo G |
| Após a **Fase 13** (arquitetura) | **Módulo C inteiro** |
| Durante a **Fase 14** (system design) | Módulos D, E, F |
| Sempre | Papers do Módulo C — um por semana, sem pressa |

---

# ⚙️ C++ e Baixa Abstração

> Fase 3 (Vol. 1). Usar C++ como lente de aumento sobre o que Java/Python escondem.

---

# FASE 3 — C++ e Baixa Abstração [APOIO]

> Objetivo: usar C++ como lente de aumento. Não é virar especialista em C++ enterprise.

- [ ] Pipeline de compilação: pré-processador → compilador → assembler → **linker** → executável
- [ ] Header (`.h`) vs implementação (`.cpp`), *include guards*
- [ ] Tipos primitivos e tamanho real em bytes (`sizeof`)
- [ ] **Ponteiros na prática**: aritmética de ponteiro, ponteiro para ponteiro, ponteiro nulo
- [ ] Referências vs ponteiros
- [ ] Alocação: stack (`int x;`) vs heap (`new` / `malloc`) — e a obrigação de `delete` / `free`
- [ ] **Dangling pointer**, double free, buffer overflow — os bugs que Java/Python te impedem de cometer
- [ ] RAII (Resource Acquisition Is Initialization) — o padrão que define C++ moderno
- [ ] Smart pointers: `unique_ptr`, `shared_ptr`, `weak_ptr`
- [ ] Classes: construtor, destrutor, cópia, *move semantics*
- [ ] Layout de objeto na memória, `vtable` e polimorfismo (como herança funciona por baixo)
- [ ] STL: `vector`, `map`, `unordered_map`, `set` — e comparar com o que você implementou na Fase 2
- [ ] Templates (noção de generics em tempo de compilação)
- [ ] **Projeto:** reimplementar Linked List + Hash Table em C++ com gerenciamento manual de memória, e rodar um detector de leak (`valgrind`)

**✅ Checkpoint da Fase 3:** você explica, com exemplo de código, por que Java "não precisa" de `free()` e qual o preço disso (pausas de GC, uso de memória maior).

**📚 Livros:**
- *C++ Primer* — Lippman, Lajoie & Moo (o melhor livro para aprender C++ de verdade)
- *A Tour of C++* — Bjarne Stroustrup (rápido, do criador da linguagem)
- *Effective Modern C++* — Scott Meyers (depois que já souber o básico)
- *The C Programming Language* (K&R) — Kernighan & Ritchie (se quiser passar por C puro antes; é curto e histórico)

---

# 🐹 Go — Concorrência

> Fase 8 (Vol. 1). Goroutines, channels, context.

---

# FASE 8 — Go [APOIO]

- [ ] Sintaxe, tipagem estática, `struct`, métodos, **interfaces implícitas** (duck typing em tempo de compilação)
- [ ] Tratamento de erro como valor (`if err != nil`) — a filosofia oposta a exceptions
- [ ] Ponteiros em Go (existem, mas sem aritmética)
- [ ] Slices, maps e o modelo de memória por trás deles
- [ ] **Goroutines** — por que são baratas (crescem sob demanda, escalonadas em user space)
- [ ] **Channels** — buffered vs unbuffered, `select`, fechamento de canal
- [ ] "Don't communicate by sharing memory; share memory by communicating"
- [ ] `sync` package: `WaitGroup`, `Mutex`, `Once`
- [ ] `context.Context` — cancelamento e timeout propagados
- [ ] `net/http` da stdlib — servidor e cliente
- [ ] Testes nativos (`testing`, table-driven tests)
- [ ] Módulos (`go mod`) e compilação para binário único
- [ ] **Projeto:** recriar o servidor HTTP da Fase 4 em Go puro e comparar o modelo de concorrência com o event loop que você escreveu em Python

**📚 Livros:**
- *The Go Programming Language* — Donovan & Kernighan (a referência)
- *Learning Go* — Jon Bodner (mais moderno e didático)
- *Concurrency in Go* — Katherine Cox-Buday (excelente, focado no que Go tem de melhor)

---

# 🏛️ Arquiteturas de Aplicação e Sistema + Spring Cloud

> Fase 13.3–13.5 e 7.10 (Vol. 1): Hexagonal, Clean, DDD, CQRS, microsserviços, antipadrões.

---

## 13.3 Arquiteturas de aplicação
- [ ] **Camadas** (Controller → Service → Repository) — o que a maioria faz
- [ ] **Arquitetura Hexagonal / Ports & Adapters**
- [ ] **Clean Architecture** — a regra de dependência apontando para dentro
- [ ] Onion Architecture
- [ ] **DDD (Domain-Driven Design)**: entidade, value object, agregado, repositório, serviço de domínio, bounded context, linguagem ubíqua
- [ ] **CQRS** — separar modelo de leitura e escrita
- [ ] **Event Sourcing** — estado como sequência de eventos
- [ ] MVC, MVP, MVVM (contexto)

## 13.4 Arquiteturas de sistema
- [ ] **Monolito** (e o **monolito modular** — a resposta certa para 90% dos projetos)
- [ ] **Microsserviços**: benefícios reais e os custos escondidos (rede, consistência, observabilidade, deploy, time)
- [ ] SOA
- [ ] **Serverless** — quando compensa, cold start
- [ ] Service Mesh (Istio, Linkerd) — noção
- [ ] **Strangler Fig** — migrar legado incrementalmente
- [ ] Anti-Corruption Layer
- [ ] Sidecar, Ambassador, Gateway (Routing / Offloading / Aggregation)
- [ ] BFF (Backends for Frontends)

## 13.5 Antipadrões de performance (saber reconhecer)
- [ ] Chatty I/O (muitas chamadas pequenas)
- [ ] Busy Database (lógica de negócio no banco)
- [ ] Busy Frontend
- [ ] Extraneous Fetching (buscar mais dados do que precisa — o `SELECT *` da vida)
- [ ] Improper Instantiation (criar cliente HTTP/conexão a cada chamada)
- [ ] Monolithic Persistence
- [ ] Noisy Neighbor
- [ ] Retry Storm
- [ ] Synchronous I/O bloqueante
- [ ] No Caching

---

## 7.10 Microsserviços com Spring Cloud
- [ ] Quando **não** usar microsserviços (comece monolito modular — sério)
- [ ] **Spring Cloud Gateway** — API Gateway
- [ ] **Config Server** — configuração centralizada
- [ ] **Eureka / Service Discovery**
- [ ] **OpenFeign** — cliente HTTP declarativo
- [ ] **Resilience4j** — Circuit Breaker, Retry, Bulkhead, Rate Limiter
- [ ] **Micrometer** — métricas e tracing distribuído

---

**📚 Livros:**
- ⭐ *Clean Architecture* — **Robert C. Martin** — a explicação mais clara de dependência e fronteira
- *Design Patterns* (GoF) — Gamma, Helm, Johnson & Vlissides — o original (denso); **alternativa mais leve:** *Head First Design Patterns* (Freeman) ou o site Refactoring.Guru (excelente e em PT-BR)
- *Domain-Driven Design* — Eric Evans (o "livro azul"; denso) — **comece por** *Implementing Domain-Driven Design* (Vaughn Vernon) ou *Learning DDD* (Vlad Khononov)
- *Patterns of Enterprise Application Architecture* — Martin Fowler
- *Building Microservices* — **Sam Newman** (2ª ed.) — honesto sobre os custos
- *Monolith to Microservices* — Sam Newman
- *Fundamentals of Software Architecture* — Mark Richards & Neal Ford
- *A Philosophy of Software Design* — John Ousterhout (curto, brilhante, e discorda do Clean Code em pontos importantes — ler os dois é formador)

---

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

---

# 🔭 Observabilidade e Confiabilidade

> Fase 15 (Vol. 1).

---

# FASE 15 — Observabilidade e Confiabilidade [AMPLIAÇÃO]

- [ ] Os **três pilares**: logs, métricas, traces (e o quarto emergente: profiling contínuo)
- [ ] **Logging estruturado** (JSON), níveis de log, **correlation ID / trace ID** propagado entre serviços
- [ ] O que **nunca** logar: senha, token, PII
- [ ] **Métricas**: tipos (counter, gauge, histogram, summary); RED (Rate, Errors, Duration) e USE (Utilization, Saturation, Errors)
- [ ] Prometheus + Grafana; Micrometer no Spring
- [ ] **Tracing distribuído**: OpenTelemetry, Jaeger, Zipkin — spans e contexto propagado
- [ ] Agregação de logs: ELK/OpenSearch, Loki
- [ ] **Alertas que importam**: alertar em sintoma (usuário afetado), não em causa; evitar fadiga de alerta
- [ ] Health checks: liveness vs readiness
- [ ] Instrumentação, telemetria, visualização
- [ ] Postmortem sem culpa (*blameless*) e cultura de incidente
- [ ] Chaos Engineering (noção)

**📚 Livros:**
- *Site Reliability Engineering* — Google (**gratuito** em sre.google/books) — e o *SRE Workbook*, também grátis
- *Observability Engineering* — Charity Majors et al.
- *Release It!* — Michael Nygard (de novo — vale as duas fases)

---

# 🌐 Redes e Protocolos a Fundo

> Módulo A (Vol. 2): TCP internals, HTTP/2/3, TLS, MQTT/OPC-UA/Modbus (seu diferencial), WebRTC.

---

# MÓDULO A — Redes e Protocolos: cobertura total
*(entra nas Fases 1.4 e 4 — estude junto com elas)*

## A.1 TCP a fundo — além do handshake
- [ ] Estados da conexão TCP (máquina de estados): `LISTEN`, `SYN_SENT`, `ESTABLISHED`, `FIN_WAIT`, **`TIME_WAIT`** — e por que `TIME_WAIT` acumulado esgota portas em servidor de alto tráfego
- [ ] **Janela deslizante** e controle de fluxo (`rwnd`)
- [ ] **Controle de congestionamento**: slow start, congestion avoidance, fast retransmit/recovery
- [ ] Algoritmos: Reno, CUBIC (padrão do Linux), **BBR** (Google — muda o jogo em rede com perda)
- [ ] **Algoritmo de Nagle** e `TCP_NODELAY` — por que ele adiciona ~40ms de latência em requisições pequenas (bug clássico de p99)
- [ ] **Delayed ACK** e a interação tóxica com Nagle
- [ ] MTU, MSS, fragmentação, Path MTU Discovery
- [ ] **Head-of-line blocking** no TCP — e por que isso motivou o QUIC
- [ ] `SO_REUSEPORT` — múltiplos processos aceitando na mesma porta (escala de accept)
- [ ] Backlog de conexão (`somaxconn`) — a fila invisível que derruba servidores sob pico
- [ ] Keep-alive TCP vs keep-alive HTTP (são coisas diferentes)
- [ ] Tuning de kernel: buffers (`net.core.rmem_max`), `tcp_tw_reuse`, limite de file descriptors (`ulimit -n`)

## A.2 Evolução do HTTP
- [ ] **HTTP/1.0** → **HTTP/1.1**: keep-alive, pipelining (e por que pipelining fracassou)
- [ ] Limite de 6 conexões por domínio e os hacks da época (domain sharding, sprites)
- [ ] **HTTP/2**: binário, **multiplexação de streams**, HPACK (compressão de header), priorização, server push (depreciado)
- [ ] O head-of-line blocking que o HTTP/2 **não** resolveu (porque está no TCP)
- [ ] **HTTP/3 + QUIC**: sobre UDP, streams independentes, handshake em 1-RTT (ou **0-RTT**), migração de conexão (troca de Wi-Fi para 4G sem cair)
- [ ] Compressão de corpo: gzip, deflate, **brotli**, zstd

## A.3 TLS a fundo
- [ ] TLS 1.2 vs **TLS 1.3** (handshake de 1-RTT, 0-RTT resumption e o risco de replay attack)
- [ ] Cipher suites, perfect forward secrecy, ECDHE
- [ ] Certificados X.509, cadeia de confiança, certificado intermediário, SNI
- [ ] Revogação: CRL, OCSP, **OCSP stapling**
- [ ] **mTLS** — autenticação mútua (padrão em service mesh)
- [ ] Custo de CPU do handshake TLS — e por que **terminação TLS no load balancer** + session resumption importam para p99
- [ ] HSTS, certificate pinning

## A.4 A camada abaixo (o que quase ninguém sabe)
- [ ] Ethernet, MAC, **ARP**
- [ ] IPv4 vs IPv6, roteamento, tabela de rotas, TTL/hop limit
- [ ] **ICMP** (por trás do `ping` e do `traceroute`)
- [ ] **DHCP**, **NTP** (sincronização de relógio — e por que isso é crítico em sistema distribuído)
- [ ] **BGP** e **Anycast** — como CDN e DNS global funcionam de verdade
- [ ] NAT, port forwarding, e por que P2P precisa de STUN/TURN
- [ ] Ferramentas de diagnóstico: `tcpdump`, **Wireshark**, `traceroute`, `mtr`, `ss`, `iftop`
- [ ] Noção de kernel bypass: `io_uring`, **eBPF**, DPDK (só para saber que existe e quando entra)

## A.5 Protocolos de aplicação além do HTTP
> **Esta seção é o seu diferencial de mercado.** Ninguém que vem de "curso de backend" conhece a metade disso — e você já vive nesse mundo.

**Mensageria e IoT**
- [ ] **MQTT** — pub/sub leve, QoS 0/1/2, retained message, last will & testament, broker (Mosquitto, EMQX). **É o protocolo padrão de IoT e automação predial**
- [ ] **CoAP** — REST sobre UDP para dispositivos restritos
- [ ] **AMQP** — o protocolo por trás do RabbitMQ
- [ ] Protocolo binário do **Kafka**

**Industrial (seu domínio — leve para o currículo)**
- [ ] **Modbus TCP/RTU** — o mais difundido em automação
- [ ] **BACnet/IP** — automação predial (HVAC, iluminação, incêndio)
- [ ] **OPC-UA** — o padrão de Indústria 4.0, com modelo de informação e segurança embutida
- [ ] Conceito de gateway de protocolo (traduzir Modbus/BACnet → MQTT → API REST) — **este é literalmente o produto que você pode construir**

**Outros**
- [ ] SMTP, IMAP, POP3 (e-mail)
- [ ] FTP, SFTP, SCP, rsync
- [ ] LDAP / Active Directory (autenticação corporativa)
- [ ] SNMP (monitoramento de equipamento de rede)
- [ ] SSH (túnel, port forwarding, jump host)

## A.6 WebRTC — o que faltava
- [ ] Modelo P2P: por que não passa por servidor (e quando precisa passar)
- [ ] **Sinalização (signaling)** — o WebRTC **não** define isso; você implementa com WebSocket
- [ ] **SDP (Session Description Protocol)** — negociação de codec e capacidades
- [ ] **ICE** (Interactive Connectivity Establishment): candidatos, e como atravessar NAT
- [ ] **STUN** — descobrir o próprio IP público
- [ ] **TURN** — relay quando o P2P direto falha (e por que ele custa caro em banda)
- [ ] **DTLS** (segurança sobre UDP) e **SRTP** (mídia segura)
- [ ] Data Channels — trocar dados arbitrários P2P, não só áudio/vídeo
- [ ] Arquiteturas de conferência: Mesh vs **SFU** (Selective Forwarding Unit) vs MCU
- [ ] Quando usar WebRTC vs WebSocket vs SSE

## A.7 Tabela de decisão: qual protocolo usar

| Necessidade | Escolha | Por quê |
|---|---|---|
| CRUD entre sistemas heterogêneos | REST/JSON | Universal, cacheável, simples |
| Comunicação interna entre microsserviços | **gRPC** | Binário, HTTP/2, contrato forte, streaming |
| Cliente precisa de dados sob medida | GraphQL | Evita over/under-fetching |
| Integração corporativa/bancária legada | SOAP | Contrato WSDL, WS-Security |
| Notificar outro sistema de um evento | Webhook | Assíncrono, sem polling |
| Servidor → cliente, unidirecional (ex: streaming de LLM) | **SSE** | Simples, sobre HTTP, reconecta sozinho |
| Bidirecional em tempo real (chat, colaboração) | **WebSocket** | Full-duplex persistente |
| Áudio/vídeo P2P, latência mínima | **WebRTC** | Sem servidor no meio da mídia |
| Dispositivo IoT com pouca banda/energia | **MQTT** | Leve, pub/sub, QoS |
| Desacoplar produtores e consumidores | Kafka/RabbitMQ | Buffer, retry, replay |
| Máxima vazão, perda tolerável | UDP puro | Sem overhead de confiabilidade |

**📚 Referências do Módulo A:**
- *TCP/IP Illustrated, Vol. 1* — W. Richard Stevens
- *High Performance Browser Networking* — Ilya Grigorik (**grátis**, hpbn.co) — cobre HTTP/2, TLS, WebRTC e WebSocket com profundidade rara
- *Bulletproof SSL and TLS* — Ivan Ristić
- *Systems Performance* — Brendan Gregg (capítulos de rede)

---

# ⚡ Engenharia de Latência de Cauda (p99)

> Módulo B (Vol. 2). ⭐ *O* tema de sênior.

---

# MÓDULO B — Engenharia de Latência de Cauda (p99)
*(módulo novo — estude após a Fase 12, revisite sempre)*

> **A premissa:** a média mente. Se 1% das suas requisições demora 3 segundos e você tem 100 chamadas internas por página, **63% dos usuários** vão sentir esse 1%. Latência de cauda é o problema mais mal compreendido de backend.

## B.1 Medição correta
- [ ] Por que **média e mediana escondem o problema**; sempre p50/p90/p95/**p99**/p99.9
- [ ] Percentis **não somam nem tiram média** — p99 de um agregado ≠ média dos p99
- [ ] **HdrHistogram** — por que histogramas comuns perdem precisão na cauda
- [ ] Latência **por endpoint**, não global (um endpoint lento contamina a métrica geral)
- [ ] Distinguir latência do servidor, da rede e percebida pelo usuário
- [ ] Instrumentar desde o primeiro dia — não dá para otimizar o que não se mede

## B.2 Teoria de filas — a matemática que explica tudo
- [ ] **Lei de Little**: `L = λ × W` (itens no sistema = taxa de chegada × tempo no sistema)
- [ ] **Utilização vs latência**: a curva é exponencial. A 80% de utilização a fila já explode; a 95%, o p99 desaparece. **Nunca opere um sistema perto de 100% de utilização.**
- [ ] Teoria de filas M/M/1 e M/M/c (noção)
- [ ] **Lei de Amdahl** — o teto de ganho ao paralelizar (a parte serial limita tudo)
- [ ] **Lei Universal de Escalabilidade (USL)** de Gunther — além da contenção, existe a **coerência** (custo de sincronizar): a partir de certo ponto, **adicionar servidor piora a performance**
- [ ] Saturação e o ponto de joelho (*knee*) da curva

## B.3 As causas reais da cauda longa
- [ ] **Pausas de Garbage Collection** (stop-the-world)
- [ ] **Contenção de lock** — thread esperando thread
- [ ] Fila de conexão cheia (pool esgotado, backlog TCP)
- [ ] **Noisy neighbor** — CPU/disco compartilhado em nuvem
- [ ] Escalonamento do SO e context switching
- [ ] Cache miss e cold start (JIT ainda não compilou, cache vazio, lambda frio)
- [ ] Retentativa e timeout mal configurados (o retry vira o problema)
- [ ] Query lenta esporádica (plano de execução mudou, tabela cresceu, lock no banco)
- [ ] **Head-of-line blocking** em qualquer camada
- [ ] Checkpoint/compactação de banco (LSM compaction, autovacuum do Postgres)
- [ ] Latência de disco e de rede em nuvem (variância natural)

## B.4 Técnicas de mitigação
**No runtime**
- [ ] Escolher o GC certo: **ZGC** ou **Shenandoah** (pausas sub-milissegundo) vs G1 (throughput). Medir, não adivinhar.
- [ ] Reduzir alocação (object pooling onde faz sentido, evitar autoboxing em hot path)
- [ ] Dimensionar heap corretamente (heap grande demais = GC longo; pequeno demais = GC frequente)
- [ ] JIT warmup e Ahead-of-Time (GraalVM native image) para eliminar cold start
- [ ] Java: **Virtual Threads** para trocar thread-per-request por concorrência barata

**Na arquitetura**
- [ ] **Hedged requests** — mandar a mesma requisição para 2 réplicas após o p95 e usar a primeira resposta (técnica do paper *The Tail at Scale*)
- [ ] **Tied requests** — as réplicas se avisam para cancelar a duplicata
- [ ] **Request coalescing / single-flight** — N requisições iguais viram 1 chamada ao backend
- [ ] **Timeout agressivo + fail fast** — melhor errar rápido que travar tudo
- [ ] **Budget de latência**: distribuir o SLA total entre as chamadas em cadeia (se o total é 200ms e há 4 saltos, cada um tem ~50ms)
- [ ] **Load shedding / admission control** — recusar carga excedente para proteger quem já está sendo atendido
- [ ] Isolamento por **Bulkhead** — pool separado por dependência
- [ ] **Backpressure** — propagar "estou cheio" em vez de acumular fila infinita
- [ ] Retry com **backoff exponencial + jitter** e **budget de retry** (nunca retry ilimitado)
- [ ] Processamento assíncrono: tirar do caminho crítico tudo que não precisa ser síncrono

**No I/O**
- [ ] Non-blocking I/O em todo o caminho (um único ponto bloqueante anula o resto)
- [ ] Connection pooling com dimensionamento correto (pool grande demais causa contenção no banco; pequeno demais causa fila na aplicação)
- [ ] Batching de chamadas e de escrita
- [ ] Reduzir round-trips: 1 query que traz tudo > 10 queries pequenas (o oposto do "chatty I/O")

**✅ Checkpoint do Módulo B:** você pega um serviço real, mede o p99, identifica a causa dominante da cauda com dados (não com palpite) e reduz o p99 — documentando a metodologia.

**📚 Referências do Módulo B:**
- 📄 **"The Tail at Scale"** — Jeff Dean & Luiz Barroso (Google, 2013) — **leia este paper. É curto e é o texto fundador do assunto.**
- *Systems Performance* — **Brendan Gregg** (2ª ed.) — a bíblia de performance; método USE
- *BPF Performance Tools* — Brendan Gregg
- *Optimizing Java* — Benjamin Evans, James Gough & Chris Newland
- *The Every Computer Performance Book* — Bob Wescott (curto e acessível)
- Blog e talks de **Gil Tene** (criador do HdrHistogram) sobre *Coordinated Omission* — mudam a forma como você mede

---

# 🕸️ Sistemas Distribuídos — a Teoria

> Módulo C (Vol. 2): falácias, relógios, consenso, quórum, anti-entropia, consistência.

---

# MÓDULO C — Sistemas Distribuídos: a teoria que falta
*(entra entre as Fases 13 e 14)*

> Sem esta base, você aplica padrões distribuídos de forma cargo cult. Com ela, você sabe **por que** cada um existe e **quando ele falha**.

## C.1 As falácias e os fundamentos
- [ ] **As 8 falácias da computação distribuída** (a rede é confiável, a latência é zero, a banda é infinita, a rede é segura, a topologia não muda, há um administrador, o custo de transporte é zero, a rede é homogênea) — cada uma já derrubou sistemas reais
- [ ] Modelos de falha: crash-stop, crash-recovery, omissão, **falha bizantina**
- [ ] Rede síncrona vs assíncrona vs parcialmente síncrona
- [ ] **Teorema FLP** — impossibilidade de consenso determinístico em sistema assíncrono com uma falha
- [ ] **CAP** corretamente entendido (é sobre o comportamento *durante* uma partição, não uma escolha permanente) e **PACELC** (else: Latência vs Consistência)
- [ ] Detecção de falha: heartbeat, timeout, phi accrual failure detector, e por que é impossível distinguir "lento" de "morto"
- [ ] Split brain e como evitar

## C.2 Tempo e ordenação
- [ ] Por que **relógio de parede não serve** para ordenar eventos (clock skew, NTP, salto de relógio)
- [ ] Relógio monotônico vs relógio de parede
- [ ] **Relógios lógicos de Lamport** (happened-before)
- [ ] **Vector clocks** — detectar concorrência e conflito
- [ ] **Version vectors** e resolução de conflito (LWW — last-write-wins — e por que ele perde dados silenciosamente)
- [ ] **TrueTime** (Google Spanner) — resolver com hardware (GPS + relógio atômico)
- [ ] Snowflake IDs / ULID / UUIDv7 — IDs ordenáveis e distribuídos

## C.3 Consenso e coordenação
- [ ] O problema do consenso e para que ele serve (eleição de líder, configuração, lock distribuído)
- [ ] **Raft** — entenda de verdade: eleição de líder, replicação de log, safety. Use a visualização interativa do raft.github.io
- [ ] **Paxos** e Multi-Paxos (noção — Raft foi criado justamente porque Paxos é difícil)
- [ ] **ZAB** (ZooKeeper) e Viewstamped Replication
- [ ] **Two-Phase Commit (2PC)** — e por que ele bloqueia se o coordenador cair
- [ ] Three-Phase Commit (e por que também não resolve)
- [ ] Sistemas de coordenação: **ZooKeeper**, **etcd**, Consul — service discovery, config, lock, eleição
- [ ] **Lock distribuído**: implementação com Redis (Redlock) e as críticas do Kleppmann a ele; fencing token
- [ ] Kafka sem ZooKeeper (**KRaft**) — Raft na prática, num produto que você vai usar

## C.4 Replicação e quórum
- [ ] Replicação **single-leader**, **multi-leader**, **leaderless** (estilo Dynamo)
- [ ] Replicação síncrona vs assíncrona vs semi-síncrona — trade-off durabilidade × latência
- [ ] **Lag de replicação** e as anomalias que ele causa: read-your-writes, monotonic reads, consistent prefix reads
- [ ] **Quórum: R + W > N** — a matemática da consistência ajustável
- [ ] Sloppy quorum e **hinted handoff**
- [ ] Resolução de conflito em multi-leader: LWW, vector clocks, merge no cliente, **CRDTs**
- [ ] **CRDTs** (Conflict-free Replicated Data Types) — G-Counter, PN-Counter, OR-Set; a base de colaboração em tempo real

## C.5 Anti-entropia (o que faltava na sua lista)
- [ ] O que é entropia entre réplicas e por que ela aparece
- [ ] **Merkle Trees** — comparar dois conjuntos gigantes de dados trocando poucos bytes (Dynamo, Cassandra, Git usam isso)
- [ ] **Read repair** — corrigir a réplica divergente no momento da leitura
- [ ] **Hinted handoff** — guardar a escrita destinada ao nó caído e entregar quando ele voltar
- [ ] **Gossip protocol** — disseminação epidêmica de estado de cluster (Cassandra, Consul, Serf)
- [ ] Repair agendado (`nodetool repair` no Cassandra) e o custo dele

## C.6 Modelos de consistência (do mais forte ao mais fraco)
- [ ] **Linearizabilidade** (consistência forte) — o sistema se comporta como se houvesse uma cópia só
- [ ] Consistência sequencial
- [ ] **Consistência causal** — preserva causa e efeito (o meio-termo prático)
- [ ] Garantias de sessão: read-your-writes, monotonic reads, monotonic writes, writes-follow-reads
- [ ] **Consistência eventual** — e o que ela realmente promete (e não promete)
- [ ] Isolamento de transação distribuída: snapshot isolation, serializable snapshot isolation (SSI)
- [ ] A diferença entre **isolamento** (transação) e **consistência** (replicação) — confusão comum

## C.7 Transações e integridade distribuída
- [ ] Por que transação ACID não atravessa serviços
- [ ] **Saga**: coreografia vs orquestração; transação compensatória
- [ ] **Outbox Pattern** e **Inbox Pattern** — publicar evento e gravar no banco atomicamente
- [ ] **Idempotência** como requisito, não como bônus — chave de idempotência, deduplicação
- [ ] Entrega: at-most-once, at-least-once, **"exactly-once"** (e por que só existe como *effectively-once* = at-least-once + idempotência)
- [ ] Two-Generals e Byzantine Generals (os problemas conceituais por trás)

**✅ Checkpoint do Módulo C:** você explica, sem consultar, por que `R+W>N` garante leitura consistente, o que um vector clock detecta que um timestamp não detecta, e por que "exactly-once" é um nome enganoso.

**📚 Referências do Módulo C:**
- ⭐ *Designing Data-Intensive Applications* — **Kleppmann** — capítulos 5 a 9 são literalmente este módulo
- *Understanding Distributed Systems* — Roberto Vitillo (o mais acessível da área)
- *Database Internals* — Alex Petrov (parte II é toda sobre distribuição)
- 📄 **Papers fundadores** (leia os abstracts e os que te interessarem a fundo):
  - *In Search of an Understandable Consensus Algorithm* (**Raft**) — Ongaro & Ousterhout
  - *Dynamo: Amazon's Highly Available Key-value Store* — de onde vêm quórum, hinted handoff e Merkle trees
  - *Spanner: Google's Globally-Distributed Database*
  - *Time, Clocks, and the Ordering of Events* — **Leslie Lamport** (1978)
  - *MapReduce*, *Bigtable*, *The Google File System*
  - *Kafka: a Distributed Messaging System for Log Processing*
  - *"Notes on Distributed Systems for Young Bloods"* — Jeff Hodges (post, não paper — leitura obrigatória e curta)
- Curso **MIT 6.824 / 6.5840 Distributed Systems** (aulas no YouTube, **gratuito**) — se quiser o nível acadêmico de verdade

---

# 📈 Backends de Alta Escrita e Alta Leitura

> Módulos D e E (Vol. 2): LSM vs B-Tree, sharding, CDC, cache multi-camada, CDN.

---

# MÓDULO D — Backends de Alta Escrita
*(entra na Fase 5 e se aprofunda após a Fase 14)*

> Alta escrita e alta leitura exigem arquiteturas **opostas**. Confundir as duas é o erro clássico.

## D.1 Internals de armazenamento — como o banco escreve
- [ ] **B+Tree** — otimizada para leitura; escrita faz *in-place update* e causa I/O aleatório
- [ ] **LSM Tree** (Log-Structured Merge) — otimizada para escrita: memtable → SSTable → compactação. É o motor de Cassandra, RocksDB, LevelDB, ScyllaDB, HBase
- [ ] **Write amplification** vs **read amplification** vs **space amplification** — o triângulo de trade-off (RUM conjecture)
- [ ] **WAL (Write-Ahead Log)** — durabilidade sem pagar I/O aleatório a cada commit
- [ ] `fsync` e o custo real de garantir durabilidade; group commit
- [ ] Page cache do SO, buffer pool do banco, direct I/O
- [ ] Estratégias de compactação (size-tiered vs leveled) e a **latência de cauda que a compactação causa**
- [ ] Bloom filter no caminho de leitura de um LSM

## D.2 Padrões de ingestão massiva
- [ ] **Batching** — agrupar N escritas em uma transação/requisição
- [ ] **Bulk insert** / `COPY` (Postgres) em vez de INSERT linha a linha
- [ ] Append-only e evitar update in-place
- [ ] Escrita assíncrona com fila na frente (**Kafka como buffer de escrita**)
- [ ] **Queue-Based Load Leveling** — a fila absorve o pico e o consumidor escreve no ritmo sustentável
- [ ] Desabilitar/recriar índice em carga massiva
- [ ] Particionamento por tempo (tabelas particionadas por dia/mês) — e `DROP PARTITION` como retenção barata
- [ ] Time-series: compressão delta-of-delta e Gorilla; TimescaleDB, InfluxDB
- [ ] Backpressure na ingestão — o que fazer quando os produtores são mais rápidos que os consumidores

## D.3 Sharding a sério
- [ ] Escolha da **chave de partição**: cardinalidade alta, distribuição uniforme, alinhada com o padrão de consulta
- [ ] Estratégias: por range, por hash, por lista, por diretório de lookup
- [ ] **Consistent hashing** e virtual nodes — rebalancear sem remapear tudo
- [ ] **Hot partition / hotspot** — o problema nº1 do sharding (ex: chave = data, e todo mundo escreve "hoje")
- [ ] Resharding e migração de dados sem downtime
- [ ] O custo escondido: queries cross-shard, joins distribuídos, transações cross-shard, contagem global
- [ ] Ferramentas: Vitess (MySQL), Citus (Postgres)

## D.4 CQRS e Event Sourcing na prática
- [ ] Quando CQRS realmente compensa (e quando é complexidade gratuita)
- [ ] Modelo de escrita normalizado × modelo de leitura desnormalizado
- [ ] **Event Sourcing**: estado como log imutável de eventos; replay; snapshot para não reprocessar tudo
- [ ] Projeções e sincronização eventual entre write model e read model
- [ ] Versionamento e evolução de esquema de eventos
- [ ] Os problemas reais: GDPR/LGPD (direito ao esquecimento vs log imutável), debug, crescimento infinito

## D.5 Streaming e CDC
- [ ] **Change Data Capture (CDC)** — ler o WAL do banco e transformar mudanças em eventos (**Debezium**)
- [ ] Log como fonte da verdade (a "unificação" do Kleppmann/Kreps)
- [ ] Processamento em stream: **Kafka Streams**, **Flink**, Spark Structured Streaming
- [ ] Windowing (tumbling, sliding, session), watermark, **event time vs processing time**, dados atrasados
- [ ] Arquitetura **Lambda** vs **Kappa**
- [ ] Stream-table duality
- [ ] Exactly-once no Kafka: transações, idempotent producer

## D.6 Escolha de banco para alta escrita
- [ ] **Cassandra / ScyllaDB** — escrita massiva, leaderless, quórum ajustável
- [ ] **DynamoDB** — serverless, chave de partição é tudo
- [ ] **ClickHouse** — colunar, analytics e ingestão gigante
- [ ] **NewSQL**: CockroachDB, TiDB, YugabyteDB, Google Spanner — SQL + ACID distribuído (usam Raft por baixo)
- [ ] Vitess / Citus — escalar horizontalmente MySQL/Postgres existentes
- [ ] Como decidir: padrão de acesso primeiro, banco depois (**nunca o contrário**)

---

# MÓDULO E — Backends de Alta Leitura
*(entra na Fase 14)*

## E.1 Réplicas e distribuição de leitura
- [ ] Read replicas e roteamento leitura/escrita na aplicação
- [ ] O problema do **lag**: usuário escreve e não vê a própria alteração — soluções (ler do primário após escrita, sticky por sessão, timestamp de causalidade)
- [ ] Réplicas geográficas e roteamento por latência
- [ ] Réplica dedicada para relatório/analytics (isolar carga pesada)

## E.2 Cache multi-camada (o que faltava na sua lista)
- [ ] **As camadas, do mais perto ao mais longe**: browser → CDN → proxy/gateway → **cache local em processo (near cache: Caffeine, Guava)** → **cache distribuído (Redis/Memcached)** → banco
- [ ] Near cache: latência de nanossegundos, mas **coerência entre instâncias** é o desafio (invalidação via pub/sub)
- [ ] Estratégias: **Cache-Aside** (lazy), **Read-Through**, **Write-Through**, **Write-Behind** (write-back), **Refresh-Ahead**
- [ ] Políticas de evicção: LRU, LFU, **W-TinyLFU** (a do Caffeine, melhor taxa de acerto), FIFO, ARC
- [ ] Dimensionar TTL: curto demais = pouco ganho; longo demais = dado velho
- [ ] **Cache Stampede / Thundering Herd** — mitigar com:
  - [ ] **Lock/single-flight** (só uma requisição recalcula)
  - [ ] **Expiração probabilística antecipada** (XFetch)
  - [ ] Refresh em background antes de expirar
  - [ ] Jitter no TTL (não deixar 1 milhão de chaves expirarem juntas)
- [ ] **Cache penetration** (consultas para chaves inexistentes) — mitigar com null caching e Bloom filter
- [ ] **Cache avalanche** (o cache inteiro cai e a carga vai toda ao banco)
- [ ] Invalidação: por TTL, por evento, por versão de chave, por tag
- [ ] Hit ratio como métrica de primeira classe — e por que cache com hit ratio baixo é só latência extra

## E.3 Modelagem para leitura
- [ ] **Desnormalização consciente** e o custo de manter cópias sincronizadas
- [ ] **Materialized views** e refresh incremental
- [ ] Tabelas de agregação pré-computadas
- [ ] **Fan-out on write vs fan-out on read** (o problema do feed de rede social — e a solução híbrida para usuários com milhões de seguidores)
- [ ] Índices especializados: índice invertido (Elasticsearch), índice geoespacial, índice vetorial
- [ ] Precomputação em background vs cálculo sob demanda

## E.4 Entrega
- [ ] **CDN**: pull vs push, edge caching, `Cache-Control` na origem, invalidação e purge
- [ ] Edge computing / edge functions (lógica perto do usuário)
- [ ] Compressão e otimização de payload (só devolver os campos necessários — evita "extraneous fetching")
- [ ] HTTP caching correto (`ETag`, `304`) — leitura que não custa banda nem CPU

---

# 🔬 Metodologia — Provar que é Rápido e Disponível

> Módulo G (Vol. 2): USE/RED, teste de carga, coordinated omission, back-of-the-envelope.

---

# MÓDULO G — Metodologia: como você prova que é rápido e disponível
*(faça junto com o Módulo B)*

## G.1 Método de investigação de performance
- [ ] **Método USE** (Brendan Gregg): para cada recurso — **U**tilização, **S**aturação, **E**rros
- [ ] **Método RED** (para serviços): **R**ate, **E**rrors, **D**uration
- [ ] Os quatro sinais de ouro do Google SRE: latência, tráfego, erros, **saturação**
- [ ] Profiling: CPU profiler, **flame graphs**, async-profiler (Java), `perf`, eBPF
- [ ] Encontrar o gargalo antes de otimizar (**otimizar o lugar errado é desperdício puro**)
- [ ] Análise de causa raiz com dados; não confiar em intuição

## G.2 Teste de carga feito certo
- [ ] Tipos: **load** (carga esperada), **stress** (até quebrar), **soak/endurance** (24h+, revela memory leak), **spike** (pico súbito), **breakpoint**
- [ ] ⚠️ **Coordinated Omission** — o erro que invalida a maioria dos benchmarks: se o gerador de carga espera a resposta antes de enviar a próxima, ele **deixa de medir justamente os momentos ruins** e seu p99 fica lindo e falso. Ferramentas que corrigem isso: **wrk2**, k6 (com configuração correta), Gatling
- [ ] Testar em ambiente equivalente ao de produção (dados realistas, não tabela vazia)
- [ ] Modelar carga realista (distribuição de endpoints, think time, tamanho de payload real)
- [ ] Ferramentas: **k6** (recomendado — script em JS), Gatling, JMeter, Locust, wrk2
- [ ] Estabelecer **baseline** e detectar regressão de performance no CI
- [ ] Capacity planning: extrapolar da curva medida, não da esperança

## G.3 Estimativa de capacidade (back-of-the-envelope)
- [ ] Números que todo engenheiro deve ter na cabeça (*"Latency Numbers Every Programmer Should Know"* — Jeff Dean): cache L1 ~1ns · RAM ~100ns · SSD ~100µs · disco ~10ms · rede no mesmo DC ~0,5ms · rede intercontinental ~150ms
- [ ] Calcular QPS, storage, banda, número de servidores
- [ ] Relação pico/média (regra prática: pico ≈ 2 a 10× a média)
- [ ] Dimensionar pool de conexões, threads e memória com base em Little's Law

---

# ☁️ Cloud a Sério

> Módulo H.3 (Vol. 3): IAM, VPC, Terraform, 6 R's de migração.

---

## H.3 Cloud a sério (não só "noção")
- [ ] Modelos: IaaS · PaaS · CaaS · FaaS · SaaS — e o que você deixa de controlar em cada um
- [ ] Regiões, **zonas de disponibilidade**, edge locations
- [ ] **IAM** — o serviço mais importante e o mais mal usado: princípio do menor privilégio, roles vs users, policies, credenciais temporárias
- [ ] Computação: VM (EC2), container gerenciado (ECS/Fargate, Cloud Run), Kubernetes gerenciado (EKS/AKS/GKE), serverless (Lambda)
- [ ] Armazenamento: object storage (**S3**), block storage (EBS), file storage (EFS); classes de armazenamento e ciclo de vida
- [ ] Banco gerenciado: RDS/Aurora, DynamoDB, ElastiCache
- [ ] Rede: **VPC**, subnet pública/privada, security group, NAT gateway, load balancer (ALB/NLB), API Gateway
- [ ] Mensageria gerenciada: SQS, SNS, EventBridge, MSK (Kafka gerenciado)
- [ ] Observabilidade: CloudWatch, X-Ray
- [ ] Segredos: Secrets Manager, Parameter Store, KMS
- [ ] **Infraestrutura como Código**: **Terraform** (multi-cloud, o padrão de mercado), CloudFormation, Pulumi, CDK
- [ ] **Cold start** em serverless e por que isso destrói p99
- [ ] **Migração para cloud — os 6 R's**: Rehost (lift-and-shift), Replatform, Repurchase, **Refactor**, Retire, Retain
- [ ] Estratégia de migração incremental (**Strangler Fig** na prática) e o risco do big bang
- [ ] Vendor lock-in — quando aceitar conscientemente e quando evitar
- [ ] Certificação (opcional mas ajuda no filtro de RH): **AWS Solutions Architect Associate** é a de melhor custo-benefício

---

# 👥 Code Review, Mentoria e Liderança Técnica

> Módulo I.2 (Vol. 3).

---

## I.2 Code review, mentoria e liderança técnica
- [ ] **Como revisar código**: focar em design e correção, não em estilo (isso é trabalho do linter)
- [ ] Comentário de review construtivo: perguntar em vez de acusar; separar "bloqueante" de "sugestão"
- [ ] Como **receber** review sem defensividade — separar o código de você mesmo
- [ ] Pair programming e mob programming
- [ ] **Mentoria**: ensinar o processo de pensar, não a resposta pronta
- [ ] Delegar com contexto (dar o *porquê*, não só o *o quê*)
- [ ] Definir padrões de time sem virar burocracia
- [ ] Liderança sem autoridade formal — influência técnica
- [ ] Conduzir discussão técnica sem que vire briga de ego
- [ ] **Ensinar é a melhor forma de descobrir os próprios gaps.** Escreva, apresente ao time, responda dúvidas — é atalho de aprendizado.
