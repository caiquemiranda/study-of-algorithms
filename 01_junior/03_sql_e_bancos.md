# 🗄️ SQL e Bancos de Dados — parte Júnior

> Fase 5.1–5.4 (Vol. 1). Continua no Pleno: operação, NoSQL e escala (`03_pleno/02`).

---

# FASE 5 — SQL e Bancos de Dados [NÚCLEO]

## 5.1 Modelo relacional e modelagem
- [ ] Tabela, linha, coluna, domínio, chave primária, chave estrangeira, chave composta, chave candidata
- [ ] Cardinalidade: 1:1, 1:N, N:N (e a tabela de junção)
- [ ] Modelo Entidade-Relacionamento (MER) e diagrama (DER)
- [ ] **Normalização**: 1FN, 2FN, 3FN, BCNF — e **quando desnormalizar de propósito** (performance de leitura)
- [ ] Tipos de dados e por que escolher errado custa caro (`VARCHAR(255)` vs `TEXT`, `FLOAT` vs `DECIMAL` para dinheiro, timestamp **com** timezone)

## 5.2 SQL na prática
- [ ] DDL: `CREATE`, `ALTER`, `DROP`, constraints (`NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`)
- [ ] DML: `INSERT`, `UPDATE`, `DELETE`, `UPSERT` (`ON CONFLICT` / `MERGE`)
- [ ] `SELECT`: `WHERE`, `ORDER BY`, `LIMIT`/`OFFSET`, `DISTINCT`
- [ ] **JOINs**: INNER, LEFT, RIGHT, FULL, CROSS, SELF JOIN — desenhar o diagrama de cada um
- [ ] Agregação: `GROUP BY`, `HAVING`, `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- [ ] Subqueries: escalar, correlacionada, `IN`/`EXISTS`
- [ ] **CTEs** (`WITH`) e CTE recursiva (hierarquia, árvore de categorias)
- [ ] **Window Functions**: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `PARTITION BY` — **o divisor de águas entre SQL júnior e pleno**
- [ ] `CASE WHEN`, `COALESCE`, `NULLIF`
- [ ] Tratamento de `NULL` (e por que `NULL = NULL` é falso)
- [ ] Views e Materialized Views
- [ ] Stored procedures, functions e triggers (saber que existem e quando *não* usar)

## 5.3 Performance
- [ ] **Índices**: B-Tree (o padrão), Hash, GIN/GiST (Postgres), full-text
- [ ] Índice composto e a **regra do prefixo mais à esquerda**
- [ ] Índice coberto (*covering index*)
- [ ] O trade-off: índice acelera `SELECT` e **desacelera** `INSERT`/`UPDATE`/`DELETE`
- [ ] **`EXPLAIN` / `EXPLAIN ANALYZE`** — ler um plano de execução: seq scan vs index scan, nested loop vs hash join
- [ ] **Problema N+1** — o bug de performance nº1 de quem usa ORM. Como detectar e resolver (`JOIN FETCH`, `@EntityGraph`, batch size)
- [ ] Paginação: `OFFSET` (degrada em tabelas grandes) vs **keyset/cursor pagination**
- [ ] SQL Tuning: reescrever query, evitar função em coluna indexada, evitar `SELECT *`

## 5.4 Transações e concorrência
- [ ] **ACID**: Atomicidade, Consistência, Isolamento, Durabilidade — explicar cada um com exemplo
- [ ] `BEGIN`, `COMMIT`, `ROLLBACK`, savepoints
- [ ] **Níveis de isolamento**: Read Uncommitted, Read Committed, Repeatable Read, Serializable
- [ ] Os problemas que cada nível evita: **dirty read, non-repeatable read, phantom read, lost update**
- [ ] Locks: otimista (versão/`@Version`) vs pessimista (`SELECT ... FOR UPDATE`)
- [ ] Deadlock no banco: como acontece e como o SGBD resolve
- [ ] MVCC (Multi-Version Concurrency Control) — como o Postgres evita bloquear leitura

---

**✅ Checkpoint da Fase 5:** você lê um `EXPLAIN ANALYZE`, identifica um N+1 num projeto real e explica qual nível de isolamento resolve um lost update.

**📚 Livros:**
- ⭐ *Designing Data-Intensive Applications* — **Martin Kleppmann** — se você só puder ler **um** livro técnico na vida, é este. Cobre bancos, replicação, consistência, sistemas distribuídos e mensageria com uma clareza rara. Tem edição em PT-BR.
- *SQL Antipatterns* — Bill Karwin (excelente e curto; mostra os erros que todo mundo comete)
- *Use a Cabeça! SQL* (Head First SQL) — para começar leve, em PT-BR
- *High Performance MySQL* — Baron Schwartz (mesmo usando Postgres, os conceitos valem)
- *The Art of PostgreSQL* — Dimitri Fontaine (se for focar em Postgres)
- *Database Internals* — Alex Petrov (como o banco funciona por dentro: B-Trees, LSM, consenso)
