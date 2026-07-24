# 🔬 Roadmap — Volume 2: Redes, Protocolos, Distribuição e Performance de Cauda

> **Complemento ao Roadmap Principal (v2).** Este volume não substitui o anterior — ele **preenche as lacunas** que a sua última lista revelou e aprofunda os temas até o nível necessário para construir backends robustos, escaláveis, com **p99 previsível** e **alta disponibilidade**.
>
> Cada módulo indica em que fase do roadmap principal ele se encaixa.

---

## 📊 Análise de cobertura: o que já tínhamos vs. o que faltava

| Tema da sua lista | Estava no roadmap? | Onde |
|---|---|---|
| HTTP/HTTPS, métodos, status | ✅ Completo | Fase 4.2, 6.1 |
| TCP vs UDP | ✅ Básico | Fase 1.4 |
| WebSockets | ✅ Completo | Fase 4.14 |
| REST / SOAP / GraphQL / gRPC | ✅ Completo | Fase 6.2 |
| Webhooks | ✅ Completo | Fase 6.2 |
| **WebRTC** | ❌ **Ausente** | → Módulo A.6 |
| p99 / latência de cauda | ⚠️ Só mencionado | → **Módulo B (novo, inteiro)** |
| Non-blocking I/O | ✅ Completo | Fase 4.5 |
| Pool de conexões | ✅ Completo | Fase 4.7 |
| Tuning de GC para baixa latência | ⚠️ Superficial | → Módulo B.4 |
| Load Balancing L4 vs L7 | ✅ Básico | Fase 14.2 |
| **Anti-entropia / coerência eventual** | ❌ **Ausente** | → Módulo C.5 |
| **Auto-scaling por métrica de saturação** | ❌ **Ausente** | → Módulo F.3 |
| **Cache multi-camada / near cache** | ❌ **Ausente** | → Módulo E.2 |
| Cache stampede | ✅ Mencionado | → aprofundado em E.2 |
| Circuit Breaker / Rate Limit / Degradação | ✅ Completo | Fase 14.3 |
| CQRS / Read Replicas / Sharding | ✅ Básico | Fase 5.7, 13.3 |
| **NewSQL** | ❌ **Ausente** | → Módulo D.6 |
| **Consenso (Raft/Paxos)** | ❌ **Ausente** | → Módulo C.3 |
| **Relógios lógicos / ordenação de eventos** | ❌ **Ausente** | → Módulo C.2 |
| **Quórum (R+W>N)** | ❌ **Ausente** | → Módulo C.4 |
| **LSM Tree vs B-Tree / WAL** | ❌ **Ausente** | → Módulo D.1 |
| **Teoria de filas (Little, USL, Amdahl)** | ❌ **Ausente** | → Módulo B.2 |
| **Coordinated Omission em benchmark** | ❌ **Ausente** | → Módulo G.2 |
| **MQTT / CoAP / protocolos industriais** | ❌ **Ausente** | → Módulo A.5 |
| **CDC / Stream processing** | ❌ **Ausente** | → Módulo D.5 |
| **Multi-região / RTO / RPO** | ❌ **Ausente** | → Módulo F |

**Veredito:** o roadmap principal estava sólido até "pleno". Faltava a camada que separa **pleno de sênior/especialista**: teoria de sistemas distribuídos, engenharia de latência e internals de armazenamento. É exatamente isso que este volume cobre.

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

# 💡 O ponto que amarra tudo

Você escreveu: *"preciso ser capaz de resolver qualquer problema e que com bons fundamentos, poderei usar qualquer linguagem"*.

Isso está exatamente certo, e vale reforçar **por quê**:

- Sockets, TCP, buffers, event loop → **iguais em toda linguagem**. Você aprende uma vez.
- Complexidade, estruturas de dados, teoria de filas → **matemática**, não sintaxe.
- CAP, quórum, consenso, relógios lógicos → **propriedades da realidade física** (a luz tem velocidade finita), não de um framework.
- Latência de cauda, contenção, saturação → **física de sistemas**, valem para Java, Go, Rust ou o que vier em 2035.

O que muda entre linguagens é: sintaxe, biblioteca padrão, modelo de concorrência e modelo de memória. Isso são **semanas** de adaptação, não anos — *desde que* a base esteja sólida.

E é por isso que o seu diagnóstico original estava correto: o problema nunca foi falta de curso. Era falta de fundamento embaixo dos cursos.

---

# 📚 A bibliografia final deste volume

**Os 5 essenciais para este nível:**
1. ⭐ *Designing Data-Intensive Applications* — Kleppmann *(cobre os Módulos C, D e E quase inteiros)*
2. *Systems Performance* (2ª ed.) — Brendan Gregg *(Módulos B e G)*
3. *Database Internals* — Alex Petrov *(Módulo D.1)*
4. *Release It!* (2ª ed.) — Michael Nygard *(Módulos B.4 e F)*
5. *Understanding Distributed Systems* — Roberto Vitillo *(Módulo C, a porta de entrada mais amigável)*

**Papers e leituras curtas de alto impacto:**
- "The Tail at Scale" — Dean & Barroso
- "Notes on Distributed Systems for Young Bloods" — Jeff Hodges
- "Latency Numbers Every Programmer Should Know" — Jeff Dean
- Paper do Raft — Ongaro & Ousterhout
- Paper do Dynamo — Amazon
- "Time, Clocks, and the Ordering of Events" — Lamport
- Blog do Martin Kleppmann (especialmente a crítica ao Redlock)
- Blog do Brendan Gregg
- *Google SRE Book* + *SRE Workbook* (ambos **grátis**)

**Gratuitos:**
- MIT 6.5840 Distributed Systems (aulas no YouTube)
- *High Performance Browser Networking* — hpbn.co
- *The System Design Primer* — GitHub
- Jepsen.io — análises reais de bancos distribuídos **quebrando** sob partição de rede (leitura fascinante e educativa)
