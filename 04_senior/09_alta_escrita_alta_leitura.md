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
