# 🗄️ SQL Avançado, NoSQL e Escala de Banco

> Fase 5.5–5.7 (Vol. 1). Parte Júnior em `01_junior/03` (livros lá).

---

## 5.5 Operação
- [ ] **Migrations**: Flyway ou Liquibase (Java), Alembic (Python) — versionar schema como se versiona código
- [ ] Migration *reversível* e migration em produção sem downtime (expand/contract)
- [ ] Backup e restore, PITR (point-in-time recovery)
- [ ] **SQL Injection**: como acontece e por que **prepared statement** resolve (e concatenar string nunca resolve)

## 5.6 NoSQL — saber o que é e quando usar
- [ ] Teorema **CAP** (Consistência, Disponibilidade, Tolerância a Partição) e PACELC
- [ ] Modelos de consistência: forte, eventual, fraca
- [ ] **Key-Value**: Redis, DynamoDB, Memcached — cache, sessão, rate limit, lock distribuído
- [ ] **Documento**: MongoDB, CouchDB — schema flexível
- [ ] **Colunar**: Cassandra, ClickHouse, ScyllaDB — escrita massiva e analytics
- [ ] **Grafo**: Neo4j, DGraph — relacionamentos como cidadão de primeira classe
- [ ] **Time Series**: InfluxDB, TimescaleDB — métricas, IoT (**muito relevante para o seu contexto de automação predial**)
- [ ] **Search**: Elasticsearch, OpenSearch, Solr — índice invertido, busca textual
- [ ] Redis a fundo: estruturas (String, List, Set, Sorted Set, Hash, Stream), TTL, persistência (RDB/AOF), pub/sub

## 5.7 Escala de banco
- [ ] **Replicação**: master-slave (leitura/escrita) e master-master; lag de replicação
- [ ] **Sharding** e escolha da chave de shard; hot partition
- [ ] Federação / particionamento funcional
- [ ] Particionamento de tabela (por range, por lista, por hash)
- [ ] Read replicas para separar carga de leitura
