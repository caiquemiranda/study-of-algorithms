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
