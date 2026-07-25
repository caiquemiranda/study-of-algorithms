# 🟦 Roadmap Vol. 1 — JÚNIOR

> Fundamentos: ferramentas, computação, SQL, APIs, Java/Spring, testes, debugging — mais a teoria da trilha de Estruturas de Dados e Algoritmos.
>
> Documento consolidado, gerado das pastas `01_junior`, `02_estruturas_e_algoritmos/` em 2026-07-24. **Edite as pastas, não este arquivo** — regenere com `python roadmap/gerar_volumes.py`. Método de estudo e marcação 🔴🟡🟢: ver `METODO.md`.

## Índice deste volume

1. 🟦 Guia do Nível — JÚNIOR
2. 🧰 Ferramentas Base — Linux, Terminal e Git
3. 💻 Computação, Memória, SO e Redes
4. 🗄️ SQL e Bancos de Dados — parte Júnior
5. 🔌 Design de APIs — parte Júnior
6. ☕ Java e Spring Boot — parte Júnior
7. ✅ Testes — parte Júnior
8. 🐞 Debugging
9. 🧠 Trilha de Estruturas de Dados e Algoritmos
10. 📊 Análise de Complexidade
11. 🧱 Estruturas de Dados — implementar do zero
12. 🎯 Algoritmos e Padrões de Resolução

---

# 🟦 Guia do Nível — JÚNIOR

> Escopo mínimo, estimativa e sinal de aprovação. Fonte: Volume 3.

---

## 🟦 Nível 1 — JÚNIOR (foco: base sólida)

**Objetivo:** conseguir a primeira vaga de desenvolvedor.

| Fase | Escopo mínimo |
|---|---|
| **Fase 0** | Linux básico + Git completo |
| **Fase 1** | Toda — é o que te diferencia de outros juniores |
| **Fase 2** | Complexidade + estruturas lineares + hash + árvores + BFS/DFS + ordenação + os padrões de two pointers/sliding window |
| **Fase 5** | 5.1 a 5.4 (SQL, índices, transações) |
| **Fase 6** | 6.1 a 6.5 (fundamentos + REST + design + CRUD + erros) |
| **Fase 7** | 7.1, 7.3, 7.4, 7.5, 7.6, 7.7 (Java + Spring Boot + JPA) |
| **Fase 11** | 11.1 e 11.2 (pirâmide + JUnit + Mockito) |
| **Novo** | Módulo H.1 (Debug) — não pule, é diferencial imediato |
| **Projeto** | Projeto 2 da Fase 17 (API CRUD Spring Boot completa) |

**⏱️ Estimativa realista:** 8 a 14 meses a 1–1,5h/dia. Você já tem parte disso.

**🚩 Sinal de que passou de nível:** você constrói uma API REST completa do zero — com autenticação, banco, validação, tratamento de erro e testes — sem seguir tutorial.

---

# 🧰 Ferramentas Base — Linux, Terminal e Git

> Fase 0 do roadmap (Vol. 1).

---

# FASE 0 — Ferramentas Base [NÚCLEO]

> Não estava na v1 do roadmap e é um buraco clássico. Ninguém ensina, todo mundo cobra.

## 0.1 Linux e terminal
- [ ] Estrutura de diretórios do Linux (`/etc`, `/var`, `/usr`, `/home`, `/proc`)
- [ ] Navegação e manipulação: `cd`, `ls`, `cp`, `mv`, `rm`, `find`
- [ ] Permissões: `chmod`, `chown`, o que significa `755` e `644` (e por que isso derruba deploy)
- [ ] Pipes e redirecionamento: `|`, `>`, `>>`, `2>&1`
- [ ] Ferramentas de texto: `grep`, `sed`, `awk`, `cat`, `less`, `tail -f`
- [ ] Processos: `ps`, `top`/`htop`, `kill`, `&`, `nohup`
- [ ] Rede pelo terminal: `curl`, `netstat`/`ss`, `ping`, `dig`, `telnet`, `nc` (netcat)
- [ ] Variáveis de ambiente e `PATH`
- [ ] Shell script básico (variáveis, `if`, loop, argumentos)
- [ ] SSH: chaves pública/privada, `ssh-keygen`, acesso a servidor remoto

## 0.2 Git e GitHub
- [ ] Modelo mental do Git: working directory → staging → commit → remote
- [ ] `init`, `clone`, `add`, `commit`, `push`, `pull`, `fetch`
- [ ] Branches: criar, trocar, `merge` vs `rebase` (e quando cada um)
- [ ] Resolver conflitos de merge na mão
- [ ] `log`, `diff`, `blame`, `stash`
- [ ] Desfazer coisas: `reset` (soft/mixed/hard), `revert`, `checkout` de arquivo
- [ ] `.gitignore` e o que **nunca** commitar (segredos, `.env`, `node_modules`, `target/`)
- [ ] Pull Request / Code Review: como abrir, como revisar
- [ ] Estratégias de branching: Git Flow, GitHub Flow, Trunk-Based
- [ ] Conventional Commits (padrão de mensagem)
- [ ] Tags e versionamento semântico (SemVer: MAJOR.MINOR.PATCH)

**✅ Checkpoint:** você resolve um conflito de merge sem pânico e sabe recuperar um commit "perdido" com `reflog`.

**📚 Livros:**
- *Pro Git* — Scott Chacon & Ben Straub (**gratuito** em git-scm.com/book/pt-br) — a referência oficial
- *The Linux Command Line* — William Shotts (**gratuito** em linuxcommand.org)

---

# 💻 Computação, Memória, SO e Redes

> Fase 1 do roadmap (Vol. 1). Aprofundamento de redes no Sênior (`04_senior/06`).

---

# FASE 1 — Computação, Memória, SO e Redes [NÚCLEO]

## 1.1 Como o computador executa um programa
- [ ] Sistemas numéricos: binário, hexadecimal, conversões
- [ ] Representação de dados: inteiros com sinal (complemento de dois), ponto flutuante IEEE 754 (**e por que `0.1 + 0.2 != 0.3`**)
- [ ] Codificação de texto: ASCII, UTF-8, Unicode (e por que acento quebra em API mal configurada)
- [ ] CPU: registradores, ULA, ciclo *fetch-decode-execute*
- [ ] Hierarquia de memória: registrador → cache L1/L2/L3 → RAM → SSD/HD → rede (e a diferença de latência entre eles, em ordens de grandeza)
- [ ] Localidade de referência (temporal e espacial) — por que percorrer um array é mais rápido que uma linked list
- [ ] Compilado vs interpretado vs máquina virtual: o que acontece com um `.c`, um `.java` e um `.py` até virar instrução na CPU

## 1.2 Memória em nível de processo
- [ ] Layout de memória de um processo: text, data, BSS, heap, stack
- [ ] **Stack**: frames de função, variáveis locais, por que é rápida, por que é limitada (*stack overflow*)
- [ ] **Heap**: alocação dinâmica, fragmentação, por que precisa ser gerenciada
- [ ] Ponteiros, endereços e referências (conceito)
- [ ] Memory leak: o que é e por que só aparece em processo de longa duração
- [ ] Garbage Collection: contagem de referência vs mark-and-sweep vs generational (visão geral — aprofunda na Fase 7 com a JVM)
- [ ] Memória virtual, paginação e *swap*

## 1.3 Sistema Operacional
- [ ] Processo vs Thread: o que o SO enxerga, custo de criação de cada um
- [ ] *Context switching* — por que ter 10.000 threads é ruim
- [ ] Escalonamento de processos (visão geral: preemptivo, quantum)
- [ ] File Descriptor e a filosofia Unix "tudo é arquivo" — **por que um socket de rede é tratado como arquivo**
- [ ] Syscalls: a fronteira user space / kernel space
- [ ] Sinais POSIX: `SIGINT`, `SIGTERM`, `SIGKILL` — como desligar um servidor sem corromper dados
- [ ] `fork` e `exec` — criação de processos
- [ ] IPC (comunicação entre processos): pipes, sockets, memória compartilhada
- [ ] Concorrência: *race condition*, seção crítica, mutex, semáforo, *deadlock* (as 4 condições de Coffman)

## 1.4 Redes
- [ ] Modelo em camadas: TCP/IP (4 camadas) e sua relação com o OSI (7 camadas)
- [ ] Endereçamento IP, máscara de sub-rede, CIDR, IP público vs privado, NAT
- [ ] Portas e o conceito de socket (IP + porta)
- [ ] **TCP**: orientado a conexão, confiável, ordenado
  - [ ] *3-way handshake* (`SYN` → `SYN-ACK` → `ACK`)
  - [ ] Encerramento (`FIN`/`ACK`) e o estado `TIME_WAIT`
  - [ ] Controle de fluxo (janela deslizante) e controle de congestionamento
  - [ ] **TCP é um fluxo contínuo de bytes** — não existe "pacote = mensagem". Por isso você lê em buffers.
- [ ] **UDP**: sem conexão, sem garantia — quando isso é *melhor* (streaming, DNS, jogos)
- [ ] `127.0.0.1` (loopback) vs `0.0.0.0` (todas as interfaces) — decide quem consegue acessar sua aplicação
- [ ] DNS: hierarquia (root → TLD → autoritativo), tipos de registro (A, AAAA, CNAME, MX, TXT), TTL e cache
- [ ] Como funciona a internet, ponta a ponta: o que acontece entre digitar a URL e a página aparecer
- [ ] Firewall e regras básicas de porta

**✅ Checkpoint da Fase 1:** você narra, do teclado ao pixel, todo o caminho de uma requisição — sem dizer "framework" nenhuma vez — e sabe apontar em qual camada cada coisa acontece.

**📚 Livros:**
- *Computer Networking: A Top-Down Approach* — **Kurose & Ross** (redes; a referência de graduação, tem edição em PT-BR: "Redes de Computadores e a Internet")
- *Operating Systems: Three Easy Pieces* — Remzi & Andrea Arpaci-Dusseau (**gratuito** em pages.cs.wisc.edu/~remzi/OSTEP/) — o melhor livro de SO disponível hoje, e é grátis
- *Sistemas Operacionais Modernos* — Andrew Tanenbaum (alternativa clássica, em PT-BR)
- *Code: The Hidden Language of Computer Hardware and Software* — Charles Petzold (para o "como o computador funciona" do zero absoluto; leitura leve e excelente)
- *Computer Systems: A Programmer's Perspective* (CS:APP) — Bryant & O'Hallaron (a ponte definitiva entre hardware e código; denso, mas transformador)
- *TCP/IP Illustrated, Vol. 1* — W. Richard Stevens (consulta, quando quiser o detalhe do protocolo)

---

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

---

# 🔌 Design de APIs — parte Júnior

> Fase 6.1–6.5 (Vol. 1). Continua no Pleno: auth, segurança, docs e performance (`03_pleno/03`).

---

# FASE 6 — Design de APIs [NÚCLEO]

> Consolida o roadmap "Building APIs" do roadmap.sh. Você já tem os fundamentos da Fase 4 — agora é sobre **projetar bem**.

## 6.1 Fundamentos
- [ ] O que é uma API, contrato, e por que ele é a "interface pública" do seu sistema
- [ ] URL, path parameters, query parameters, matrix parameters, fragmentos
- [ ] **Content Negotiation**: `Accept`, `Content-Type`, `Accept-Language`, `Accept-Encoding`
- [ ] **CORS** por dentro: preflight `OPTIONS`, `Access-Control-Allow-Origin`, credenciais, e por que o erro aparece só no navegador
- [ ] HTTP Caching aplicado a API (`ETag`, `Cache-Control`)

## 6.2 Estilos de API
- [ ] **REST** — os 6 constraints de Fielding, níveis do Modelo de Maturidade de Richardson
- [ ] Simple JSON APIs (o que 90% do mercado chama de "REST" e não é)
- [ ] **gRPC** — Protobuf, HTTP/2, streaming bidirecional; ideal para comunicação interna entre serviços
- [ ] **GraphQL** — schema, query, mutation, subscription, resolvers; o problema N+1 e o DataLoader
- [ ] **SOAP / XML** — saber ler (legado, ainda vivo em ERPs e integrações bancárias)
- [ ] **Webhooks** — API ao contrário; assinatura HMAC do payload, retry, idempotência
- [ ] Quando escolher cada um

## 6.3 Design First — projetar antes de codar
- [ ] **Princípios REST**: recursos, representações, stateless, interface uniforme
- [ ] **Design de URI**: substantivos no plural, hierarquia (`/clientes/{id}/pedidos`), sem verbos
- [ ] Modelagem de recursos e convenções de nomenclatura (camelCase vs snake_case — escolha uma e mantenha)
- [ ] **Versionamento**: na URL (`/v1/`), no header, por content-type — prós e contras
- [ ] **HATEOAS** — o nível 3 de REST (saber o que é, e por que quase ninguém usa)
- [ ] Design de DTOs: separar modelo de domínio do contrato de API

## 6.4 Manipulação de dados e requisições
- [ ] CRUD mapeado corretamente em métodos HTTP e status codes
- [ ] **Filtragem, ordenação e busca** — padrões de query string
- [ ] **Paginação**: offset/limit, page/size, **cursor-based** (e quando cada uma quebra)
- [ ] **Idempotência**: quais métodos são idempotentes por definição, e como implementar `Idempotency-Key` em POST (crítico para pagamento)
- [ ] Bulk operations e partial update (`PATCH` com JSON Merge Patch ou JSON Patch)
- [ ] Validação de entrada e mensagens de erro úteis

## 6.5 Controle de tráfego e erros
- [ ] **Rate Limiting**: algoritmos — Token Bucket, Leaky Bucket, Fixed Window, **Sliding Window**
- [ ] Headers de rate limit (`X-RateLimit-*`, `Retry-After`) e o status `429`
- [ ] Throttling vs rate limiting vs quota
- [ ] **RFC 7807 / RFC 9457 — Problem Details for HTTP APIs**: o formato padronizado de erro (`type`, `title`, `status`, `detail`, `instance`) — implemente isso, poucos fazem
- [ ] Tratamento de erro consistente: nunca vazar stack trace, sempre correlacionar com um trace ID

---

# ☕ Java e Spring Boot — parte Júnior

> Fase 7.1, 7.3–7.7 (Vol. 1). Continua no Pleno: JVM, Spring Security e testes (`03_pleno/04`).

---

# FASE 7 — Java e Spring Boot em Profundidade [NÚCLEO]

## 7.1 Java — a linguagem
- [ ] Sintaxe, tipos primitivos vs wrappers, autoboxing (e a armadilha do `==` vs `.equals()`)
- [ ] **OOP de verdade**: encapsulamento, herança, polimorfismo, abstração
- [ ] Interface vs classe abstrata; `default methods`
- [ ] **Composição sobre herança** — e por quê
- [ ] `equals()` e `hashCode()` — o contrato entre eles e o que quebra no HashMap se você errar
- [ ] Imutabilidade, `final`, e `record` (Java 16+)
- [ ] **Collections Framework**: `List` (ArrayList vs LinkedList), `Set` (HashSet vs TreeSet vs LinkedHashSet), `Map` (HashMap vs TreeMap vs LinkedHashMap vs ConcurrentHashMap) — **quando usar cada um** (conecta com a Fase 2)
- [ ] Generics, wildcards (`? extends`, `? super`), type erasure
- [ ] **Exceptions**: checked vs unchecked, `try-with-resources`, quando criar exception customizada, por que nunca engolir exception
- [ ] **Streams API** e programação funcional: `map`, `filter`, `reduce`, `collect`, lazy evaluation
- [ ] `Optional` — usar certo (não como substituto de `null` em todo lugar)
- [ ] `Comparable` vs `Comparator`
- [ ] I/O e NIO
- [ ] **Concorrência**: `Thread`, `Runnable`, `ExecutorService`, `CompletableFuture`, `synchronized`, `volatile`, `AtomicInteger`, `ConcurrentHashMap`
- [ ] **Virtual Threads** (Java 21+) — a mudança de paradigma do Loom
- [ ] Novidades modernas: `var`, switch expressions, text blocks, sealed classes, pattern matching

---

## 7.3 Ecossistema e build
- [ ] **Maven** — `pom.xml`, ciclo de vida, dependências, escopos, plugins, multi-módulo
- [ ] **Gradle** — noção (muitos projetos modernos usam)
- [ ] Gerenciamento de dependências transitivas e conflito de versão

## 7.4 Spring — os fundamentos que ninguém explica
- [ ] **IoC (Inversão de Controle)** e o **Container** Spring
- [ ] **Injeção de Dependência**: por construtor (**preferida**), setter, campo — e por que `@Autowired` em campo é ruim
- [ ] **Beans**: ciclo de vida, `@Component`/`@Service`/`@Repository`/`@Configuration`
- [ ] **Escopos de bean**: singleton (padrão), prototype, request, session
- [ ] **AOP** (Programação Orientada a Aspectos): proxy dinâmico, `@Aspect`, e como `@Transactional` e `@Cacheable` funcionam por baixo (**é AOP, não mágica**)
- [ ] A armadilha do self-invocation (chamar método `@Transactional` de dentro da mesma classe não funciona — e você vai saber por quê)
- [ ] Configuração: `application.yml`/`.properties`, `@Value`, `@ConfigurationProperties`, **Profiles** (dev/staging/prod)
- [ ] Anotações essenciais e o que cada uma realmente faz

## 7.5 Spring Boot
- [ ] **Starters** — o que são e o que trazem
- [ ] **Autoconfiguration** — `@ConditionalOn...`, e como ler o relatório de autoconfiguração para entender o que o Boot ligou sozinho
- [ ] **Embedded Server** — Tomcat/Jetty/Undertow embutido; por que o JAR "roda sozinho"
- [ ] **Actuator** — health, metrics, info, env; e como proteger esses endpoints
- [ ] DevTools, hot reload

## 7.6 Spring MVC / Web
- [ ] Arquitetura: **DispatcherServlet** → HandlerMapping → Controller → ViewResolver (e como isso é a Fase 4.4 e 4.8 na prática)
- [ ] `@RestController`, `@RequestMapping`, `@GetMapping` e família
- [ ] `@RequestBody`, `@ResponseBody`, `@PathVariable`, `@RequestParam`, `@RequestHeader`
- [ ] `ResponseEntity` e controle fino de status/headers
- [ ] **Bean Validation** (`@Valid`, `@NotNull`, `@Size`, validador customizado)
- [ ] **`@ControllerAdvice` / `@ExceptionHandler`** — tratamento global de erro (implemente com RFC 7807)
- [ ] Filtros vs Interceptors — e onde cada um entra na cadeia
- [ ] Configuração de CORS
- [ ] **Spring WebFlux** e programação reativa (Mono/Flux) — saber que existe e quando faz sentido

## 7.7 Persistência
- [ ] **JDBC** puro primeiro (para ver o que o JPA esconde) e `JdbcTemplate`
- [ ] **JPA / Hibernate**: `@Entity`, `@Id`, estratégias de geração de ID
- [ ] **Relacionamentos**: `@OneToOne`, `@OneToMany`, `@ManyToOne`, `@ManyToMany`; `mappedBy` e lado dono
- [ ] **Fetch types**: LAZY vs EAGER — e por que EAGER é quase sempre um erro
- [ ] **`LazyInitializationException`** — por que acontece e como resolver certo
- [ ] **Ciclo de vida da entidade**: transient → managed → detached → removed
- [ ] **Persistence Context / 1st level cache**, `flush`, `dirty checking`
- [ ] **Problema N+1 no Hibernate** — detectar com log de SQL e resolver com `JOIN FETCH`, `@EntityGraph`, `@BatchSize`
- [ ] **Spring Data JPA**: repositórios, query methods derivados, `@Query` (JPQL e nativa), `Specification`, `Pageable`
- [ ] **`@Transactional`**: propagação (REQUIRED, REQUIRES_NEW, ...), isolamento, `readOnly`, rollback rules
- [ ] Spring Data JDBC e Spring Data MongoDB (noção)
- [ ] Migrations com **Flyway** ou Liquibase
- [ ] Connection pool **HikariCP** — tuning de pool size

---

**✅ Checkpoint da Fase 7:** você constrói uma API Spring Boot completa (auth JWT, JPA com relacionamentos, validação, tratamento global de erro, testes, migrations) e explica o que o framework faz em cada ponto — porque você já construiu aquilo na mão na Fase 4.

**📚 Livros:**
- *Effective Java* — **Joshua Bloch** — obrigatório. Leia depois de saber Java básico; é o livro que faz você escrever Java como profissional.
- *Java: Como Programar* — Deitel (base, em PT-BR) ou *Head First Java* (mais leve)
- *Spring in Action* — Craig Walls (a referência de Spring)
- *Spring Boot: Up and Running* — Mark Heckler
- *Java Concurrency in Practice* — Brian Goetz (denso, mas é *a* referência de concorrência em Java)
- *Java Persistence with Hibernate* — Bauer & King (para JPA a fundo)
- *Optimizing Java* — Benjamin Evans (JVM, GC e performance)

---

# ✅ Testes — parte Júnior

> Fase 11.1–11.2 (Vol. 1): pirâmide, AAA, mocks. Itens avançados (Testcontainers, TDD, carga, mutação) completam-se no Pleno (`03_pleno/06`).

---

# FASE 11 — Testes e Qualidade [NÚCLEO]

> **Estava faltando por completo na v1.** É o que mais separa júnior de pleno em entrevista técnica.

## 11.1 Pirâmide de testes
- [ ] Unitário (muitos, rápidos, isolados)
- [ ] Integração (menos, testam a junção com banco/fila/API externa)
- [ ] End-to-End (poucos, lentos, frágeis, mas valiosos)
- [ ] O antipadrão "cone de sorvete" (muitos E2E, poucos unitários)

## 11.2 Prática
- [ ] AAA: Arrange, Act, Assert
- [ ] Test doubles: **dummy, stub, spy, mock, fake** — saber a diferença de verdade
- [ ] Mockito (Java) / `unittest.mock` e `pytest-mock` (Python)
- [ ] **Testcontainers** — banco/Kafka reais em container para teste de integração
- [ ] Testes funcionais e de contrato (**Pact**)
- [ ] Testes de carga: **k6**, JMeter, Gatling, Locust — e como interpretar p95/p99
- [ ] Mocking de API externa: WireMock, MockServer
- [ ] Cobertura de código (JaCoCo) — **e por que 100% de cobertura não significa qualidade**
- [ ] **TDD** — red/green/refactor; pelo menos experimentar de verdade num projeto
- [ ] Testes de mutação (PIT) — a métrica que realmente mede a qualidade dos testes

---

# 🐞 Debugging

> Módulo H.1 (Vol. 3) — nível júnior, impacto de sênior.

---

## H.1 Debugging (nível júnior, impacto de sênior)
> Estava faltando e é constrangedor o quanto isso é subestimado. Desenvolvedor que não sabe debugar depende dos outros para sempre.

- [ ] Breakpoints: simples, **condicional**, por exceção, por campo (watchpoint)
- [ ] Step over / step into / step out / run to cursor
- [ ] Inspeção de variáveis, watch expressions, **avaliar expressão em runtime**
- [ ] Ler e interpretar **stack trace** — encontrar a causa raiz, não a última linha
- [ ] `Caused by:` e exceções encadeadas
- [ ] **Remote debugging** (JDWP) — anexar o debugger a uma aplicação rodando em container/servidor
- [ ] Debug de teste, debug de código assíncrono/multithread (o mais difícil)
- [ ] Debug sem debugger: logging estratégico, bisect no Git, minimal reproducible example
- [ ] **Thread dump** (`jstack`) — diagnosticar deadlock e thread travada
- [ ] **Heap dump** (`jmap`) + análise no Eclipse MAT — encontrar memory leak
- [ ] Java Flight Recorder e async-profiler em produção
- [ ] Ferramentas de linha: `strace`, `tcpdump`, `curl -v`
- [ ] **Método**: hipótese → teste → eliminar. Nunca "mudar coisas até funcionar"

---

# 🧠 Trilha de Estruturas de Dados e Algoritmos

> Trilha **transversal**: começa no Júnior e acompanha todos os níveis. Corresponde à Fase 2 do roadmap (Vol. 1).

## Como esta trilha se organiza

| Pasta / arquivo | O que é |
|---|---|
| [01_complexidade.md](01_complexidade.md) | Big-O, análise amortizada, Teorema Mestre |
| [02_estruturas_de_dados.md](02_estruturas_de_dados.md) | Checklist de estruturas para implementar **do zero** |
| [03_algoritmos_e_padroes.md](03_algoritmos_e_padroes.md) | Ordenação, busca, padrões de entrevista, DP, grafos |
| `fundamentos/` | Uma anotação por padrão (18 categorias, alinhadas ao NeetCode 150) |
| `problemas/` | Soluções LeetCode organizadas por categoria × dificuldade |
| `implementacoes/` | Estruturas implementadas do zero em Java, Python, C++ e Go |
| [INDICE.md](INDICE.md) | Índice gerado automaticamente por `gerador_de_indice.py` |

## Escopo por nível

- **Júnior:** complexidade + estruturas lineares + hash + árvores + BFS/DFS + ordenação + two pointers / sliding window
- **Pleno:** completar DP, grafos avançados, backtracking
- **Sênior:** reimplementar as estruturas em C++ (gerência manual de memória) e Go

## Regras de prática deliberada (Fase 2.4)

- **NeetCode 150** — a lista mais eficiente hoje (organizada exatamente pelas categorias de `problemas/`)
- LeetCode: *Blind 75* ou *Grind 75* como meta mínima
- Codewars ou Exercism para prática diária leve
- Regra: **sem consultar solução por 30 minutos**. Depois de 30min, leia a solução, entenda, feche tudo e reimplemente do zero no dia seguinte.
- Refazer todas as estruturas do zero, sem consultar, em pelo menos uma linguagem

## Convenção de nome dos arquivos de solução

```
problemas/<categoria>/<dificuldade>/<numero-leetcode>_<nome-do-problema>.md
Ex.: problemas/01_arrays_e_hashing/easy/0001_two_sum.md
```

Cada solução deve registrar: enunciado resumido, abordagem, complexidade tempo/espaço, código e o que aprendeu.
Depois de resolver, rode `python gerador_de_indice.py` para atualizar o [INDICE.md](INDICE.md).

**✅ Checkpoint da trilha (nível Júnior):** implementar Hash Table, BST e Grafo com BFS/DFS do zero, sem consulta, e justificar a complexidade de cada operação.

---

# 📊 Análise de Complexidade

> Fase 2.1 (Vol. 1).

---

## 2.1 Análise de complexidade
- [ ] Notação assintótica: Big-O (limite superior), Big-Ω (inferior), Big-Θ (justo)
- [ ] Complexidade de **tempo** vs **espaço**
- [ ] Análise de melhor / médio / pior caso
- [ ] Análise amortizada (por que `ArrayList.add()` é O(1) amortizado mesmo redimensionando)
- [ ] Reconhecer visualmente as classes:
  - [ ] O(1) — constante
  - [ ] O(log n) — logarítmica (divide o problema pela metade)
  - [ ] O(n) — linear
  - [ ] O(n log n) — linearítmica (o teto prático de ordenação por comparação)
  - [ ] O(n²) — quadrática (loops aninhados)
  - [ ] O(2ⁿ) e O(n!) — exponencial e fatorial (força bruta, backtracking sem poda)
- [ ] Complexidade de recursão: árvore de recursão e Teorema Mestre (noção)

---

# 🧱 Estruturas de Dados — implementar do zero

> Fase 2.2 (Vol. 1). Implementações em `implementacoes/{java,python,cpp,go}/`.

---

## 2.2 Estruturas de Dados — implementar **cada uma do zero**, sem usar a lib da linguagem

### Lineares
- [ ] **Array estático** — acesso O(1), inserção/remoção O(n), memória contígua
- [ ] **Array dinâmico / Vector / ArrayList** — estratégia de crescimento (dobrar capacidade), custo amortizado
- [ ] **String** — imutabilidade, por que concatenar em loop é O(n²), StringBuilder/Rope
- [ ] **Linked List simples** — inserção O(1) na cabeça, busca O(n), custo de cache miss
- [ ] **Linked List duplamente encadeada** — navegação bidirecional, remoção O(1) com referência
- [ ] **Linked List circular**
- [ ] **Stack (Pilha)** — LIFO; `push`/`pop`/`peek`; aplicações: chamada de função, undo, parsing de expressão, DFS iterativo
- [ ] **Queue (Fila)** — FIFO; `enqueue`/`dequeue`; aplicações: BFS, escalonamento, buffer de mensagens
- [ ] **Deque** — fila de duas pontas
- [ ] **Circular Buffer / Ring Buffer** — a estrutura por trás de buffers de rede e log de alta performance

### Hashing
- [ ] **Hash Table / HashMap** — função de hash, fator de carga, *rehashing*
- [ ] Tratamento de colisão: encadeamento (chaining) vs endereçamento aberto (linear/quadratic probing, double hashing)
- [ ] Por que é O(1) "em média" e O(n) no pior caso — e como isso já virou vetor de ataque (Hash DoS)
- [ ] **Set** implementado sobre hash
- [ ] **Bloom Filter** — probabilístico, falso positivo sim / falso negativo não; usado em cache e banco de dados

### Árvores
- [ ] **Árvore binária** — terminologia: raiz, folha, altura, profundidade, grau
- [ ] Travessias: **pré-ordem, em-ordem, pós-ordem** (recursiva e iterativa) e **por nível (BFS)**
- [ ] **BST (Binary Search Tree)** — busca/inserção/remoção O(log n) *se balanceada*, O(n) se degenerada
- [ ] **Árvores balanceadas**: AVL (rotações) e Red-Black Tree (a que está por trás do `TreeMap` do Java)
- [ ] **B-Tree e B+Tree** — **estrutura dos índices de banco de dados**; por que otimiza leitura em disco (conecta direto com a Fase 5)
- [ ] **Heap (Min-Heap / Max-Heap)** e **Priority Queue** — inserção/remoção O(log n), acesso ao mínimo/máximo O(1)
- [ ] **Trie (árvore de prefixos)** — autocompletar, dicionário
- [ ] **Radix Tree / Patricia Trie** — **é o roteador de URL dos frameworks modernos** (FastAPI/Starlette). Conecta com a Fase 4.8.
- [ ] **Segment Tree / Fenwick Tree (BIT)** — consultas de intervalo (nível competitivo, opcional)
- [ ] **Union-Find / Disjoint Set** — com *path compression* e *union by rank*; usado em Kruskal e detecção de ciclo

### Grafos
- [ ] Terminologia: dirigido/não-dirigido, ponderado, cíclico/acíclico, DAG, conexo
- [ ] Representações: **matriz de adjacência** (O(V²) espaço, O(1) checagem de aresta) vs **lista de adjacência** (O(V+E) espaço)
- [ ] Quando usar cada representação (grafo denso vs esparso)

---

# 🎯 Algoritmos e Padrões de Resolução

> Fase 2.3–2.4 (Vol. 1): ordenação, busca, padrões de entrevista, DP, grafos, strings, concorrência.

---

## 2.3 Algoritmos — os tipos mais comuns, detalhados

### Ordenação
| Algoritmo | Tempo (médio) | Espaço | Estável? | Quando importa |
|---|---|---|---|---|
| Bubble Sort | O(n²) | O(1) | Sim | Só didático |
| Selection Sort | O(n²) | O(1) | Não | Só didático |
| Insertion Sort | O(n²) | O(1) | Sim | Ótimo para n pequeno ou quase ordenado |
| Merge Sort | O(n log n) | O(n) | Sim | Ordenação externa, listas ligadas |
| Quick Sort | O(n log n) | O(log n) | Não | O padrão prático; pior caso O(n²) |
| Heap Sort | O(n log n) | O(1) | Não | Quando espaço é crítico |
| Counting / Radix / Bucket | O(n + k) | O(k) | Sim | Quando o domínio é limitado (não comparativo) |

- [ ] Implementar Insertion, Merge, Quick e Heap Sort do zero
- [ ] Entender **estabilidade** e por que importa (ordenar por 2 critérios)
- [ ] Saber que `Timsort` (Python/Java) é um híbrido Merge + Insertion — e por quê

### Busca
- [ ] Busca linear O(n)
- [ ] **Busca binária** O(log n) — implementar iterativa e recursiva
- [ ] Variações críticas de busca binária: *lower bound*, *upper bound*, busca em array rotacionado, **busca binária na resposta** (padrão avançado muito cobrado)
- [ ] Busca em árvore (BST) e em hash

### Padrões de resolução de problemas (**o que realmente cai em entrevista**)
- [ ] **Two Pointers** — par com soma alvo, remover duplicatas, container with most water
- [ ] **Sliding Window** — fixa e variável; maior substring sem repetição, soma máxima de subarray de tamanho k
- [ ] **Fast & Slow Pointers (Tortoise and Hare)** — detectar ciclo em lista ligada, encontrar o meio
- [ ] **Prefix Sum / Soma de Prefixos** — consultas de soma de intervalo em O(1)
- [ ] **Merge Intervals** — sobreposição de intervalos, agendamento de salas
- [ ] **Cyclic Sort** — encontrar número faltante/duplicado em array de 1..n
- [ ] **Top-K elements** (com Heap) — k maiores, k mais frequentes
- [ ] **Monotonic Stack** — próximo maior elemento, histograma de maior retângulo
- [ ] **Backtracking** — permutações, combinações, subconjuntos, N-Rainhas, Sudoku
- [ ] **Bit Manipulation** — XOR para achar único, contar bits, máscaras

### Recursão e Programação Dinâmica
- [ ] Recursão: caso base, passo recursivo, pilha de chamadas, recursão de cauda
- [ ] Dividir e conquistar (o padrão do Merge Sort e da busca binária)
- [ ] **Memoization (top-down)** vs **Tabulação (bottom-up)**
- [ ] Clássicos de DP a implementar:
  - [ ] Fibonacci (o "hello world" da DP)
  - [ ] Climbing Stairs / Coin Change
  - [ ] Knapsack (mochila 0/1 e fracionária)
  - [ ] Longest Common Subsequence (LCS)
  - [ ] Longest Increasing Subsequence (LIS)
  - [ ] Edit Distance (distância de Levenshtein)
  - [ ] Subset Sum / Partition
  - [ ] DP em matriz (caminhos únicos, soma mínima de caminho)

### Algoritmos gulosos (Greedy)
- [ ] Quando o guloso funciona (propriedade de escolha gulosa + subestrutura ótima) e quando falha
- [ ] Clássicos: seleção de atividades, troco de moedas (guloso vs DP), Huffman coding

### Grafos — algoritmos
- [ ] **BFS** — menor caminho em grafo não ponderado, nível por nível
- [ ] **DFS** — recursiva e iterativa; detecção de ciclo; componentes conexos
- [ ] **Ordenação topológica** (Kahn e via DFS) — resolução de dependências, build systems
- [ ] **Dijkstra** — menor caminho com pesos positivos (usa Priority Queue)
- [ ] **Bellman-Ford** — aceita pesos negativos, detecta ciclo negativo
- [ ] **Floyd-Warshall** — todos os pares, O(V³)
- [ ] **A\*** — Dijkstra com heurística (noção)
- [ ] **MST**: Kruskal (com Union-Find) e Prim
- [ ] Detecção de ciclo em grafo dirigido vs não-dirigido

### Strings
- [ ] Manipulação básica, palíndromo, anagrama
- [ ] **KMP** — busca de padrão em O(n+m)
- [ ] Rabin-Karp (hash rolante)
- [ ] Trie aplicada a autocompletar

### Concorrência (algoritmos e problemas clássicos)
- [ ] Produtor-Consumidor
- [ ] Leitores-Escritores
- [ ] Jantar dos Filósofos (deadlock)
- [ ] Padrões de sincronização: mutex, semáforo, barreira, latch

## 2.4 Prática deliberada
- [ ] **NeetCode 150** — a lista mais eficiente hoje (organizada exatamente pelos padrões acima)
- [ ] LeetCode: fazer os *Blind 75* ou o *Grind 75* como meta mínima
- [ ] Codewars ou Exercism para prática diária leve
- [ ] Regra: **sem consultar solução por 30 minutos**. Depois de 30min, leia a solução, entenda, feche tudo e reimplemente do zero no dia seguinte.
- [ ] Refazer todas as estruturas do 2.2 do zero, sem consultar, em pelo menos uma linguagem

**✅ Checkpoint da Fase 2:** você implementa Hash Table, BST e Grafo com BFS/DFS do zero, sem consulta, e justifica a complexidade de cada operação.

**📚 Livros:**
- *Grokking Algorithms* (**"Entendendo Algoritmos"**, tem em PT-BR) — Aditya Bhargava — **comece por aqui**, é visual e destrava o assunto
- *Algorithms* — Robert Sedgewick & Kevin Wayne (o meio-termo perfeito: rigoroso mas prático; tem curso gratuito no Coursera)
- *Introduction to Algorithms* (CLRS) — Cormen et al. — a bíblia. **Use como referência/consulta, não como leitura linear**
- *Cracking the Coding Interview* — Gayle Laakmann McDowell (foco em entrevista)
- *The Algorithm Design Manual* — Steven Skiena (excelente na parte de "qual algoritmo usar para qual problema")
