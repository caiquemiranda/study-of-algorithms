# 🟧 Roadmap Vol. 2 — PLENO

> A web sem frameworks (16 pilares), SQL avançado, segurança de APIs, JVM, Docker/CI/CD, mensageria, SOLID, FastAPI, TypeScript e IA aplicada.
>
> Documento consolidado, gerado das pastas `03_pleno/` em 2026-08-05. **Edite as pastas, não este arquivo** — regenere com `python roadmap/gerar_volumes.py`. Método de estudo e marcação 🔴🟡🟢: ver `METODO.md`.

## Índice deste volume

1. 🟧 Guia do Nível — PLENO
2. 🕸️ A Web sem Frameworks — os 16 Pilares
3. 🗄️ SQL Avançado, NoSQL e Escala de Banco
4. 🔐 APIs — Auth, Segurança, Docs e Performance
5. ☕ Java Avançado — JVM, Spring Security e Testes no Spring
6. 🐍 Python Aplicado — FastAPI e asyncio
7. 🧹 Qualidade de Código
8. 🐳 Docker, CI/CD, Mensageria e Cloud (noção)
9. 🧩 SOLID e Design Patterns
10. 🔄 Versões do Java, Consumo de APIs Externas e Ecossistema
11. 🟦 TypeScript e Integração com Frontend [APOIO]
12. 🤖 IA Aplicada a Backend [APOIO]

---

# 🟧 Guia do Nível — PLENO

> Escopo, estimativa e sinal de aprovação. Fonte: Volume 3.

---

## 🟧 Nível 2 — PLENO (foco: aplicações completas)

**Objetivo:** ser autônomo. Recebe um problema, entrega a solução inteira.

| Fase | Escopo |
|---|---|
| **Fase 4** | ⭐ **Toda.** Os 16 pilares. *Este é o seu maior diferencial e o que resolve os seus gaps.* |
| **Fase 2** | Completar: DP, grafos avançados, backtracking |
| **Fase 5** | 5.5 a 5.7 (migrations, NoSQL, Redis, replicação) |
| **Fase 6** | 6.6 a 6.12 (auth completa, segurança, docs, performance, integração) |
| **Fase 7** | 7.2, 7.8, 7.9 (JVM, Spring Security, testes) |
| **Fase 9** | Python + FastAPI (seu uso de IA) |
| **Fase 11** | Toda, incluindo Testcontainers e TDD |
| **Fase 12** | Toda (Docker, CI/CD, Kafka, RabbitMQ) |
| **Fase 13** | 13.1 e 13.2 (SOLID + Design Patterns) |
| **Novo** | Módulo H.2 (Java LTS) e H.4 (consumo de APIs externas) |
| **Projeto** | Projetos 3, 4 e 5 da Fase 17 |

**⏱️ Estimativa:** +12 a 18 meses.

**🚩 Sinal de que passou:** você olha para um projeto Spring Boot e sabe apontar o que o framework faz em cada linha — porque construiu aquilo na mão. E consegue debugar um problema em produção sem depender de ninguém.

---

# 🕸️ A Web sem Frameworks — os 16 Pilares

> Fase 4 (Vol. 1). ⭐ A fase mais importante do roadmap.

---

# FASE 4 — A Web sem Frameworks: os 16 Pilares [NÚCLEO]

> **A fase mais importante do seu roadmap.** É ela que transforma Spring Boot e FastAPI de "magia" em "eu sei exatamente o que isso está fazendo".
>
> Faça em **Python puro** (biblioteca padrão, zero dependências) e depois **replique em Go** na Fase 8.

## 4.1 Sockets TCP/IP
- [ ] `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `close()`
- [ ] `SO_REUSEADDR` e por que a porta fica "presa" ao reiniciar o servidor
- [ ] Ler bytes com `recv()` em loop até montar a mensagem inteira; gerenciar o tamanho do buffer
- [ ] Escrever com `send()` e por que ele pode enviar **menos bytes do que você pediu**
- [ ] Sockets bloqueantes vs não-bloqueantes

## 4.2 HTTP cru — parsing manual
- [ ] **Request Line**: `GET /api/clientes?ativo=true HTTP/1.1`
- [ ] Parsear method, path, query string e versão
- [ ] **Headers** no formato `Chave: Valor`; os críticos: `Host`, `Content-Length`, `Content-Type`, `Accept`, `Authorization`, `User-Agent`
- [ ] O delimitador **CRLF duplo (`\r\n\r\n`)** que separa headers do body
- [ ] `Transfer-Encoding: chunked` — quando não se sabe o tamanho de antemão
- [ ] Montar a resposta: **Status Line** (`HTTP/1.1 200 OK`) + headers + `\r\n\r\n` + body
- [ ] Métodos HTTP: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS — e suas semânticas (seguro? idempotente?)
- [ ] Status codes por família: 1xx, 2xx (200, 201, 204), 3xx (301, 302, 304), 4xx (400, 401, 403, 404, 409, 422, 429), 5xx (500, 502, 503, 504)
- [ ] Versões: HTTP/1.0 vs 1.1 (keep-alive, pipelining) vs **HTTP/2** (multiplexação, binário, server push) vs **HTTP/3** (QUIC sobre UDP)
- [ ] Teste manual: abrir `telnet`/`nc` numa porta 80 e digitar HTTP na mão

## 4.3 CGI — o ancestral
- [ ] Variáveis de ambiente (`REQUEST_METHOD`, `QUERY_STRING`, `CONTENT_LENGTH`)
- [ ] Comunicação via `stdin`/`stdout`
- [ ] O gargalo do `fork` por requisição — por que 1.000 usuários derrubavam o servidor

## 4.4 WSGI e ASGI
- [ ] **WSGI**: uma função recebendo `environ` (dict) e `start_response` — é literalmente isso que Flask/Django são por baixo
- [ ] Escrever uma aplicação WSGI de 10 linhas, sem framework, e servi-la com Gunicorn
- [ ] **ASGI**: a versão assíncrona (`scope`, `receive`, `send`) — base do FastAPI/Uvicorn
- [ ] Equivalente no mundo Java: **Servlet API** e o container (Tomcat) — e por que `@RestController` do Spring acaba virando um Servlet

## 4.5 Concorrência e I/O de baixo nível
- [ ] **Thread-per-request** (modelo clássico do Java/Tomcat): custo de memória por thread, context switching
- [ ] Thread Pool — por que reusar threads em vez de criar por requisição
- [ ] **Multiplexação de I/O**: `select` → `poll` → `epoll` (Linux) / `kqueue` (BSD/macOS)
- [ ] **Event Loop**: uma thread monitorando milhares de sockets; a base de Node.js, Uvicorn, Nginx
- [ ] O problema **C10K** (e hoje C10M) — o contexto histórico disso tudo
- [ ] **CPU-bound vs I/O-bound** — a decisão arquitetural mais importante
- [ ] Java moderno: **Virtual Threads (Project Loom)** — como o Java resolveu isso a partir do Java 21

## 4.6 Gerenciamento de estado
- [ ] HTTP é **stateless** — cada requisição é a primeira
- [ ] Ciclo `Set-Cookie` (resposta) → `Cookie` (requisições seguintes)
- [ ] Atributos de cookie: `HttpOnly`, `Secure`, `SameSite`, `Domain`, `Path`, `Max-Age` (cada um bloqueia um ataque específico)
- [ ] Sessão **server-side** (memória/Redis/banco) vs **client-side** (JWT)
- [ ] Por que sessão em memória quebra ao escalar horizontalmente (*sticky sessions* como remendo)
- [ ] **JWT** por dentro: header.payload.signature em Base64URL, assinatura HMAC vs RSA, `exp`, `iat`
- [ ] O calcanhar de Aquiles do JWT: **não dá para revogar** — e as soluções (refresh token, blacklist, expiração curta)

## 4.7 Comunicação com banco de dados (wire protocol)
- [ ] Banco é só outro servidor TCP numa porta (PostgreSQL 5432, MySQL 3306)
- [ ] **Wire protocol binário** — o driver empacota o SQL em bytes num formato específico (PostgreSQL Message Flow)
- [ ] Prepared statements no protocolo — e como isso previne SQL Injection de verdade
- [ ] **Connection Pooling**: por que abrir conexão é caro, min/max pool, timeout, leak de conexão
- [ ] Hierarquia de abstração: socket → driver (JDBC/psycopg) → pool (HikariCP) → ORM (Hibernate/SQLAlchemy)

## 4.8 Roteamento (URL Dispatching)
- [ ] Abordagem ingênua: cadeia de `if` (O(n) por requisição)
- [ ] Regex compilada por rota
- [ ] **Radix Tree / Trie** — a solução moderna; cada `/` desce um nó (conecta com a Fase 2.2)
- [ ] Parâmetros de path (`/users/{id}`) vs query (`?page=2`) vs wildcards
- [ ] Precedência de rotas e conflitos (`/users/me` vs `/users/{id}`)
- [ ] **Implementar um roteador com Radix Tree** — é o exercício que mais eleva seu nível em estrutura de dados aplicada

## 4.9 Segurança de baixo nível
- [ ] Criptografia **simétrica** vs **assimétrica** (chave pública/privada)
- [ ] **Handshake TLS** passo a passo: ClientHello → ServerHello → certificado → troca de chaves → chave de sessão simétrica
- [ ] Certificados X.509, cadeia de confiança, Autoridade Certificadora, Let's Encrypt
- [ ] Diferença SSL vs TLS (e por que "SSL" é só um nome que ficou)
- [ ] **Hashing unidirecional** — nunca criptografia reversível para senha
- [ ] Algoritmos: MD5 e SHA-1 (**quebrados**), SHA-256 (bom para integridade, ruim para senha por ser rápido), **bcrypt / scrypt / Argon2** (lentos de propósito)
- [ ] **Salt** (contra Rainbow Tables) e **pepper**
- [ ] *Fator de custo* / work factor — por que ele deve subir com o tempo

## 4.10 Processamento em background
- [ ] Por que tarefa longa no fluxo HTTP causa timeout
- [ ] Interceptar `SIGTERM` para *graceful shutdown* (terminar o que está processando antes de morrer)
- [ ] Daemon: processo filho desvinculado do terminal
- [ ] Fila em memória (`queue` do Python, `BlockingQueue` do Java) e estruturas thread-safe
- [ ] O que Celery / Spring Batch / Sidekiq fazem por cima disso
- [ ] Padrão: HTTP `202 Accepted` + endpoint de status/polling para tarefa assíncrona

## 4.11 Serialização e Marshalling
- [ ] Objeto na RAM → stream de bytes na rede
- [ ] **Reflection** (Java) / `inspect` (Python) — como o framework descobre os campos do seu objeto em runtime
- [ ] Formatos: JSON, XML, **Protocol Buffers**, MessagePack, Avro — texto vs binário, tamanho vs legibilidade
- [ ] Escrever um serializador JSON simples do zero (objeto → string)
- [ ] **`multipart/form-data`**: boundaries, e como processar upload de 50MB lendo em *chunks* sem estourar a RAM
- [ ] Riscos de desserialização insegura (uma das OWASP Top 10)

## 4.12 Arquivos estáticos e caching
- [ ] Syscall **`sendfile`** e Zero-Copy — disco direto para a placa de rede, sem passar pela CPU/user space
- [ ] **`ETag`** (hash do conteúdo) e o fluxo `If-None-Match` → `304 Not Modified`
- [ ] `Last-Modified` / `If-Modified-Since`
- [ ] `Cache-Control`: `max-age`, `no-cache`, `no-store`, `public`/`private`, `must-revalidate`
- [ ] Cache no navegador vs CDN vs proxy — e invalidação de cache

## 4.13 Event Loop próprio
- [ ] Implementar um `while True` com `selectors` (Python) monitorando N sockets
- [ ] Registrar callbacks para eventos de leitura/escrita
- [ ] Entender o que é uma *coroutine* e como `async`/`await` vira máquina de estados

## 4.14 Protocol Upgrades — WebSockets e SSE
- [ ] Handshake de upgrade: `Connection: Upgrade` + `Upgrade: websocket` → **`101 Switching Protocols`**
- [ ] Frames do WebSocket (opcode, mask, payload length), ping/pong (keep-alive)
- [ ] **Server-Sent Events (SSE)**: unidirecional, sobre HTTP normal, reconexão automática
- [ ] **Long polling** e **short polling** — as alternativas antigas
- [ ] Quando usar cada um: SSE para notificação/streaming de LLM; WebSocket para chat/colaboração bidirecional

## 4.15 Proxy Reverso
- [ ] Implementar um "porteiro": aceita TCP na 80, lê o header `Host`, abre socket com a app interna (8000) e repassa bytes
- [ ] Diferença **proxy** (cliente) vs **proxy reverso** (servidor)
- [ ] **Load Balancer vs Proxy Reverso** (sobreposição e diferença)
- [ ] Headers de proxy: `X-Forwarded-For`, `X-Forwarded-Proto`, `X-Real-IP`
- [ ] **Terminação TLS** no proxy
- [ ] Nginx, Apache, Caddy, Traefik — configuração básica de cada (pelo menos Nginx de verdade)

## 4.16 Memória em processos longos
- [ ] Por que servidor moderno não "zera" a memória a cada requisição (diferente do CGI/PHP antigo)
- [ ] Como um memory leak derruba um servidor depois de 48h no ar
- [ ] Diagnóstico: heap dump, profiler, monitoramento de memória ao longo do tempo

## 🏗️ Projeto central da Fase 4
Usando o repositório **`codecrafters-io/build-your-own-x`** (ex-`danistefanovic/build-your-own-x`), seções *"Build your own Web Server"* e *"Build your own Database"*:

1. Servidor HTTP do zero em Python puro: sockets → parsing → resposta, com roteador em **Radix Tree**
2. Suporte a **thread pool** e depois a **event loop** — medir a diferença sob carga
3. Autenticação com sessão via cookie **e** via JWT (implementar as duas para comparar)
4. Upload multipart salvando em chunks no disco
5. Servir estáticos com `ETag` e `304`
6. Um proxy reverso simples na frente disso tudo

**✅ Checkpoint da Fase 4:** seu "mini-framework" responde HTTP de verdade no navegador, sem uma linha de dependência externa — e você consegue apontar, num projeto Spring Boot, qual classe faz o papel de cada um destes 16 pilares.

**📚 Livros:**
- *HTTP: The Definitive Guide* — David Gourley & Brian Totty (a referência de HTTP)
- *High Performance Browser Networking* — Ilya Grigorik (**gratuito** em hpbn.co) — leitura obrigatória
- *Foundations of Python Network Programming* — Brandon Rhodes & John Goerzen (sockets, TLS e protocolos em Python puro, ignorando frameworks)
- *Unix Network Programming, Vol. 1* — W. Richard Stevens (a bíblia de sockets; consulta)
- *Web Scalability for Startup Engineers* — Artur Ejsmont (ótima ponte entre esta fase e System Design)

---

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

---

# 🔐 APIs — Auth, Segurança, Docs e Performance

> Fase 6.6–6.12 (Vol. 1). Parte Júnior em `01_junior/04`.

---

## 6.6 Autenticação
- [ ] **Basic Auth** — Base64, e por que só serve sobre HTTPS
- [ ] **Token-based Auth** (Bearer)
- [ ] **JWT** — estrutura, assinatura, `exp`, refresh token, revogação (retomando a Fase 4.6)
- [ ] **Session-based Auth** — cookie + store server-side
- [ ] **OAuth 2.0** — os fluxos: Authorization Code (+ **PKCE**), Client Credentials, Device Code; e por que Implicit e Password Grant foram **descontinuados**
- [ ] **OIDC (OpenID Connect)** — a camada de *identidade* sobre OAuth2; `id_token`
- [ ] **SAML** — legado corporativo, mas vivo em SSO empresarial
- [ ] mTLS (autenticação mútua por certificado) — comum entre serviços internos
- [ ] API Keys: geração, **rotação**, escopos, armazenamento (hash, nunca em texto puro)

## 6.7 Autorização
- [ ] **RBAC** (Role-Based) — o mais comum; papéis e permissões
- [ ] **ABAC** (Attribute-Based) — decisão baseada em atributos do usuário/recurso/contexto
- [ ] **ReBAC** (Relationship-Based) — modelo do Google Zanzibar
- [ ] PBAC (Policy-Based), DAC (Discretionary), MAC (Mandatory)
- [ ] Escopos e permissões granulares
- [ ] Onde autorizar: gateway, filtro, service layer, ou banco (row-level security)

## 6.8 Segurança de API
- [ ] **OWASP Top 10** e **OWASP API Security Top 10** (são listas diferentes — estude as duas)
- [ ] Injection: SQL, NoSQL, Command, LDAP
- [ ] Broken Object Level Authorization (**BOLA/IDOR**) — a vulnerabilidade nº1 de APIs
- [ ] Mass Assignment / Excessive Data Exposure
- [ ] XSS, CSRF (e por que API stateless com Bearer token é menos vulnerável a CSRF)
- [ ] SSRF, XXE, Insecure Deserialization
- [ ] **CSP** (Content Security Policy), HSTS, security headers
- [ ] Gestão de segredos: variáveis de ambiente, Vault, AWS Secrets Manager — **nunca no Git**
- [ ] Sanitização de log (não logar senha, token, PII)

## 6.9 Documentação
- [ ] **OpenAPI / Swagger** — escrever a spec, gerar doc, gerar client
- [ ] Code-first vs Spec-first (Design First)
- [ ] **Postman / Insomnia / Bruno** — coleções, environments, testes automatizados
- [ ] Stoplight, Readme.com, Redoc
- [ ] Boa documentação: exemplos de request/response reais, erros documentados, changelog

## 6.10 Performance de API
- [ ] Métricas que importam: **latência p50/p95/p99** (não use média!), throughput, taxa de erro
- [ ] Estratégias de cache em cada camada (cliente, CDN, gateway, aplicação, banco)
- [ ] Load balancing (aprofunda na Fase 14)
- [ ] Compressão (`gzip`, `brotli`)
- [ ] Profiling e monitoramento
- [ ] **Retry com backoff exponencial + jitter** — e por que retry ingênuo causa *retry storm*
- [ ] Timeouts em todas as camadas (nunca deixar sem timeout)

## 6.11 Padrões de integração
- [ ] APIs síncronas vs assíncronas
- [ ] **API Gateway** — roteamento, auth centralizada, rate limit, agregação
- [ ] **BFF (Backend for Frontend)** — uma API por tipo de cliente
- [ ] **Event-Driven Architecture** — publish/subscribe, event sourcing (noção)
- [ ] Webhooks vs Polling — trade-offs
- [ ] Batch processing
- [ ] Filas de mensagem como integração (aprofunda na Fase 12)

## 6.12 Ciclo de vida, padrões e conformidade
- [ ] API Lifecycle: design → desenvolvimento → publicação → versionamento → **depreciação** (com `Sunset` header e prazo)
- [ ] Contract testing (Pact) — garantir que provider e consumer não quebrem um ao outro
- [ ] **LGPD** (é a lei que se aplica a você no Brasil) e **GDPR** (equivalente europeu)
- [ ] Conceito de **PII** (dados pessoais identificáveis) e minimização de dados
- [ ] PCI DSS (cartão), HIPAA (saúde, EUA) — saber que existem e quando se aplicam

**✅ Checkpoint da Fase 6:** você projeta uma API do zero em OpenAPI, com versionamento, paginação por cursor, rate limit, erros em RFC 7807 e OAuth2 — e defende cada decisão.

**📚 Livros:**
- *RESTful Web APIs* — Leonard Richardson & Mike Amundsen (a referência de REST)
- *API Design Patterns* — JJ Geewax (Google) — excelente e moderno
- *Designing Web APIs* — Brenda Jin et al. (prático, curto)
- *The Web Application Hacker's Handbook* — Stuttard & Pinto (segurança ofensiva; ler para saber se defender)

---

# ☕ Java Avançado — JVM, Spring Security e Testes no Spring

> Fase 7.2, 7.8, 7.9 (Vol. 1). Parte Júnior em `01_junior/05` (livros lá). Spring Cloud/microsserviços no Sênior (`04_senior/03`).

---

## 7.2 JVM
- [ ] Compilação: `.java` → bytecode `.class` → JVM → JIT → código nativo
- [ ] **Áreas de memória**: Heap (young/old generation), Stack por thread, Metaspace, Code Cache
- [ ] **Garbage Collectors**: Serial, Parallel, CMS, **G1** (padrão), **ZGC** e Shenandoah (baixa pausa)
- [ ] Stop-the-world e tuning básico (`-Xms`, `-Xmx`)
- [ ] Classloading e o modelo de delegação
- [ ] Ferramentas: `jstack`, `jmap`, `jstat`, **VisualVM**, JProfiler, Java Flight Recorder
- [ ] Diagnóstico de memory leak com heap dump

---

## 7.8 Spring Security
- [ ] A **cadeia de filtros** (SecurityFilterChain) — o coração do Spring Security
- [ ] `AuthenticationManager`, `UserDetailsService`, `PasswordEncoder` (BCrypt)
- [ ] Autenticação stateless com **JWT** (implementar o filtro na mão pelo menos uma vez)
- [ ] Autorização: `@PreAuthorize`, `@Secured`, configuração por rota, `hasRole` vs `hasAuthority`
- [ ] **OAuth2 Resource Server** e OAuth2 Client
- [ ] CSRF: quando desabilitar (API stateless) e quando **não** (app com sessão/cookie)
- [ ] Method security e segurança em nível de objeto

## 7.9 Testes no Spring
- [ ] `@SpringBootTest` (integração) vs teste unitário puro
- [ ] `@WebMvcTest` + **MockMvc** — testar controller isolado
- [ ] `@DataJpaTest` — testar repositório
- [ ] `@MockBean` / `@MockitoBean`
- [ ] **Testcontainers** — testes de integração com banco real em container (padrão de mercado hoje)
- [ ] RestAssured para testes de API

---

# 🐍 Python Aplicado — FastAPI e asyncio

> Fase 9 (Vol. 1).

---

# FASE 9 — Python Aplicado [NÚCLEO]

## 9.1 Python além do básico
- [ ] Modelo de dados: tudo é objeto, `__dunder__` methods
- [ ] Mutabilidade e a armadilha do argumento default mutável
- [ ] List/dict/set comprehensions
- [ ] **Generators** e `yield` — lazy evaluation e economia de memória
- [ ] **Decorators** — e como isso é o mecanismo do `@app.get` do FastAPI
- [ ] **Context managers** e `with` (`__enter__`/`__exit__`)
- [ ] Type hints e `typing` (`Optional`, `Union`, `Generic`, `Protocol`); `mypy`
- [ ] **GIL (Global Interpreter Lock)** — por que threading em Python não paraleliza CPU, e o que fazer (multiprocessing)
- [ ] `asyncio`: event loop, coroutines, `async`/`await`, `gather`, `TaskGroup` (retoma a Fase 4.13)
- [ ] Ambientes: `venv`, `poetry`/`uv`, `requirements.txt` vs `pyproject.toml`
- [ ] Testes: `pytest`, fixtures, parametrize, mocks

## 9.2 FastAPI
- [ ] Rotas, path/query params, request body
- [ ] **Pydantic** — validação e serialização por tipo; v1 vs v2
- [ ] Sistema de **Dependency Injection** (`Depends`)
- [ ] Middlewares e exception handlers
- [ ] Docs automáticas (OpenAPI gerado do código)
- [ ] Autenticação OAuth2/JWT
- [ ] Background tasks
- [ ] Rodar com **Uvicorn** (ASGI — retoma a Fase 4.4)
- [ ] SQLAlchemy 2.0 (ORM) + Alembic (migrations)

**📚 Livros:**
- *Fluent Python* — **Luciano Ramalho** (brasileiro; é *o* livro de Python intermediário/avançado. Tem em PT-BR: "Python Fluente")
- *Effective Python* — Brett Slatkin
- *Architecture Patterns with Python* — Percival & Gregory (**gratuito** em cosmicpython.com) — DDD, repositório, unit of work em Python
- *Python Testing with pytest* — Brian Okken

---

# 🧹 Qualidade de Código

> Fase 11.3 (Vol. 1) + completar os itens avançados da 11.2 (`01_junior/06`): Testcontainers, TDD, testes de carga e mutação.

---

## 11.3 Qualidade de código
- [ ] Análise estática: SonarQube, SpotBugs, Checkstyle, `ruff`/`black` (Python), ESLint
- [ ] **Code smells** e refatoração sistemática
- [ ] Code Review: como revisar e como receber revisão
- [ ] Debt técnico: identificar, registrar e negociar

**📚 Livros:**
- ⭐ *Clean Code* — **Robert C. Martin** — leia com senso crítico (algumas opiniões são datadas), mas os capítulos de nomes, funções e testes são formadores
- *Refactoring* — **Martin Fowler** (2ª ed.) — o catálogo de refatorações
- *Working Effectively with Legacy Code* — Michael Feathers (como testar código que não foi feito para ser testado — realidade de 90% dos empregos)
- *Test-Driven Development: By Example* — Kent Beck
- *Growing Object-Oriented Software, Guided by Tests* — Freeman & Pryce
- *The Pragmatic Programmer* — Hunt & Thomas — não é sobre testes, é sobre ser desenvolvedor. Leia em algum momento.

---

# 🐳 Docker, CI/CD, Mensageria e Cloud (noção)

> Fase 12 (Vol. 1).

---

# FASE 12 — Docker, CI/CD e Operação [NÚCLEO]

## 12.1 Containers
- [ ] O que é um container por baixo: **namespaces + cgroups** (não é VM!)
- [ ] Imagem vs container vs layer
- [ ] **Dockerfile**: `FROM`, `RUN`, `COPY`, `WORKDIR`, `ENV`, `EXPOSE`, `CMD` vs `ENTRYPOINT`
- [ ] **Multi-stage build** — imagem final pequena (essencial em Java)
- [ ] Cache de layers e ordem das instruções
- [ ] Volumes (persistência) e bind mounts
- [ ] Redes Docker: bridge, host, custom network
- [ ] **Docker Compose** — subir API + Postgres + Redis + Kafka localmente com um comando
- [ ] Boas práticas: usuário não-root, imagem base slim/alpine/distroless, `.dockerignore`, health check
- [ ] Registry: Docker Hub, ECR, GHCR
- [ ] **Kubernetes** (noção): Pod, Deployment, Service, Ingress, ConfigMap, Secret, HPA

## 12.2 CI/CD
- [ ] Integração Contínua: build + testes + análise estática a cada push
- [ ] **GitHub Actions** — workflow, jobs, steps, matrix, secrets, cache
- [ ] Pipeline típico: lint → test → build → scan de segurança → build da imagem → push → deploy
- [ ] Ambientes: dev → staging → produção
- [ ] Estratégias de deploy: **rolling, blue-green, canary**, feature flags
- [ ] Rollback e versionamento de artefato
- [ ] Segredos no pipeline (nunca em texto puro no repositório)

## 12.3 Mensageria
- [ ] Por que filas existem: desacoplamento, absorção de pico, resiliência
- [ ] **RabbitMQ**: exchange (direct, topic, fanout, headers), queue, binding, ack/nack, DLQ (Dead Letter Queue), prefetch
- [ ] **Kafka**: tópico, **partição**, offset, consumer group, replicação, retenção, compactação
- [ ] Quando RabbitMQ e quando Kafka (fila de tarefas vs log de eventos)
- [ ] Garantias de entrega: at-most-once, at-least-once, exactly-once (e por que "exactly-once" é mais complicado do que parece)
- [ ] **Idempotência no consumidor** — obrigatório quando a entrega é at-least-once
- [ ] Ordenação de mensagens e a relação com partições
- [ ] **Outbox Pattern** — como publicar evento e gravar no banco atomicamente
- [ ] Saga Pattern — transação distribuída (coreografia vs orquestração)

## 12.4 Cloud (noção suficiente)
- [ ] Modelos: IaaS, PaaS, SaaS, Serverless
- [ ] Serviços básicos (AWS como referência): EC2, S3, RDS, SQS/SNS, Lambda, ECS/EKS, CloudWatch, IAM
- [ ] Twelve-Factor App — os 12 princípios (config no ambiente, logs como stream, processos stateless, etc.)

**📚 Livros:**
- *Docker Deep Dive* — Nigel Poulton
- *The Phoenix Project* e *The DevOps Handbook* — Gene Kim et al. (cultura e por que DevOps existe)
- *Continuous Delivery* — Jez Humble & David Farley
- *Kafka: The Definitive Guide* — Narkhede, Shapira & Palino (**gratuito** pela Confluent)
- *Enterprise Integration Patterns* — Hohpe & Woolf (o catálogo clássico de mensageria)

---

# 🧩 SOLID e Design Patterns

> Fase 13.1–13.2 (Vol. 1). Arquiteturas (13.3+) no Sênior (`04_senior/03` — livros lá).

---

## 13.1 Princípios
- [ ] **SOLID**, um por um, com exemplo de violação e correção:
  - [ ] **S**ingle Responsibility
  - [ ] **O**pen/Closed
  - [ ] **L**iskov Substitution (o mais mal compreendido)
  - [ ] **I**nterface Segregation
  - [ ] **D**ependency Inversion (**e a diferença entre isso e Injeção de Dependência**)
- [ ] DRY, KISS, YAGNI — e quando o DRY vira acoplamento ruim
- [ ] Coesão alta, acoplamento baixo
- [ ] Lei de Deméter
- [ ] Composição sobre herança
- [ ] Separação de responsabilidades por camada

### Object Calisthenics — as 9 regras (exercício, não lei)
> Criadas por Jeff Bay (*The ThoughtWorks Anthology*) como um kata: aplique as 9 ao pé da letra num exercício pequeno para sentir a dor dos extremos — não como padrão de produção. O ganho é o **hábito** que sobra depois de tirar o pé do acelerador.
- [ ] **Um nível de indentação por método** — força extrair método em vez de aninhar `if`/`for`
- [ ] **Não use `ELSE`** — *early return* ou polimorfismo no lugar do `if/else` (raiz do "sem `else`" está na Fase 13.1: Open/Closed)
- [ ] **Encapsule todos os primitivos e Strings** — `CPF`, `Email`, `Dinheiro` como Value Object em vez de `String`/`double` soltos (evita "obsessão primitiva" — bug clássico de trocar dois parâmetros do mesmo tipo)
- [ ] **Coleções de primeira classe** — uma classe que só existe para envelopar uma coleção (`PedidoItens` em vez de `List<Item>` passando de mão em mão)
- [ ] **Um ponto por linha** — Lei de Deméter levada ao limite: `a.b().c().d()` é proibido; fale só com quem você conhece diretamente
- [ ] **Não abrevie** — nomes completos, sem `qtd`, `tmp`, `mgr` (o custo de digitar é menor que o custo de decifrar depois)
- [ ] **Mantenha as entidades pequenas** — classes ≤ 50 linhas, pacotes ≤ 10 arquivos (limite artificial que expõe quando uma classe faz coisa demais)
- [ ] **No máximo 2 variáveis de instância por classe** — a regra mais controversa; o ponto real é forçar composição em vez de uma classe "Deus" com 15 campos
- [ ] **Sem getters/setters/properties públicos** — "Tell, Don't Ask": peça para o objeto fazer, não puxe o dado dele para decidir por fora (choca de propósito com o Java Bean tradicional — é o ponto principal do exercício)

## 13.2 Design Patterns (GoF) — os que realmente aparecem
**Criacionais**
- [ ] Singleton (e por que costuma ser antipadrão fora do container de DI)
- [ ] Factory Method e Abstract Factory
- [ ] **Builder** (muito usado em Java)
- [ ] Prototype

**Estruturais**
- [ ] **Adapter** — integrar sistema legado
- [ ] **Decorator** — adicionar comportamento sem herança
- [ ] **Proxy** — é o mecanismo do `@Transactional` do Spring
- [ ] Facade — simplificar subsistema complexo
- [ ] Composite, Bridge, Flyweight

**Comportamentais**
- [ ] **Strategy** — o mais útil no dia a dia
- [ ] **Observer** — base de eventos
- [ ] **Template Method**
- [ ] **Chain of Responsibility** — é a cadeia de filtros do Spring Security
- [ ] Command, State, Iterator, Mediator, Visitor, Memento

---

# 🔄 Versões do Java, Consumo de APIs Externas e Ecossistema

> Módulos H.2, H.4 e H.7 (Vol. 3).

---

## H.2 Versões do Java e migração
- [ ] O modelo de release: 6 meses por versão, **LTS a cada 2 anos** (8 → 11 → 17 → **21** → 25)
- [ ] Java 8: lambdas, streams, `Optional`, nova API de data/hora (`java.time`)
- [ ] Java 9–11: módulos (JPMS), `var`, HTTP Client nativo, `String` methods
- [ ] Java 12–17: **records**, sealed classes, switch expressions, text blocks, pattern matching for `instanceof`
- [ ] Java 18–21: **Virtual Threads**, pattern matching for `switch`, sequenced collections, structured concurrency (preview)
- [ ] Java 22–25: novidades recentes (consulte, pois muda rápido)
- [ ] **Migração de versão**: o que quebra (JPMS, remoção de módulos Java EE, mudanças de GC padrão), ferramenta `jdeprscan`, `jdeps`
- [ ] Distribuições da JDK: Oracle, **Temurin/Adoptium**, Corretto, Zulu, GraalVM — e as diferenças de licença
- [ ] **Realidade de mercado:** muita vaga ainda é Java 8/11. Saiba trabalhar nelas e saiba argumentar a migração.

---

## H.4 Consumo de APIs externas (disciplina própria)
> Você vai integrar com ERP, gateway de pagamento, API de LLM, SCADA. Consumir API bem é diferente de expor API bem.

- [ ] Cliente HTTP: `RestClient`/`WebClient` (Spring 6+), **OpenFeign**, `HttpClient` nativo
- [ ] **Timeout sempre** — de conexão e de leitura. API externa sem timeout é bomba-relógio.
- [ ] Retry com backoff + jitter, e **só em erro transitório** (5xx, timeout — nunca em 4xx)
- [ ] **Circuit breaker** em toda dependência externa (Resilience4j)
- [ ] Fallback e degradação quando o terceiro cai
- [ ] Cache de resposta de terceiro (e respeitar o `Cache-Control` deles)
- [ ] **Idempotência na sua ponta** — assumir que a chamada pode duplicar
- [ ] Rate limit do fornecedor: respeitar `429` e `Retry-After`
- [ ] Gestão de credenciais e rotação de token (refresh automático de OAuth2)
- [ ] **Anti-Corruption Layer** — nunca deixar o modelo do terceiro vazar para o seu domínio
- [ ] Versionamento e depreciação do fornecedor — como se proteger de quebra
- [ ] Testes: **WireMock/MockServer** para simular o terceiro; **contract testing**
- [ ] Sandbox vs produção; observabilidade específica (latência e taxa de erro **por fornecedor**)
- [ ] Webhook de entrada: validar assinatura HMAC, responder rápido e processar assíncrono, tratar reentrega

---

## H.7 Java fora do backend (saber que existe, priorizar por objetivo)
- [ ] **JavaFX / Swing** — desktop. ⚠️ Só estude se surgir demanda real. Para automação industrial pode aparecer (HMI, ferramenta interna), mas **não é prioridade** no seu objetivo de backend.
- [ ] **Android (Kotlin)** — se um dia quiser app móvel. Fora do seu foco atual.
- [ ] **Kotlin** — vale mais a pena que JavaFX: roda na JVM, interopera com Java, é usado com Spring Boot em várias empresas. Depois do Nível Pleno, é um bom investimento.
- [ ] **Decisão consciente:** deixar itens de fora não é lacuna, é priorização. A imagem lista tudo que existe no ecossistema; **o seu roadmap lista o que serve ao seu objetivo.**

---

# 🟦 TypeScript e Integração com Frontend [APOIO]

> Fase 10 (Vol. 1).

---

# FASE 10 — TypeScript e Integração com Frontend [APOIO]

- [ ] Tipos básicos, inferência, `type` vs `interface`
- [ ] Union, intersection, literal types, **narrowing** e type guards
- [ ] Generics
- [ ] Utility types: `Partial`, `Pick`, `Omit`, `Record`, `Readonly`
- [ ] `unknown` vs `any` vs `never`
- [ ] `strict` mode e `tsconfig.json`
- [ ] Async/await, Promises, tratamento de erro
- [ ] Módulos ESM vs CommonJS
- [ ] **Tipar o contrato da API** — gerar tipos a partir do OpenAPI (`openapi-typescript`) para o front nunca sair do contrato do back
- [ ] Consumo de API: `fetch`, axios, TanStack Query (cache, loading, retry)
- [ ] Node.js: event loop (retoma Fase 4.5), streams, `npm`/`pnpm`
- [ ] **Projeto:** conectar um frontend real aos backends Java e Python das fases anteriores, com tipos compartilhados

**📚 Livros:**
- *Programming TypeScript* — Boris Cherny
- *Effective TypeScript* — Dan Vanderkam
- *TypeScript Handbook* (**gratuito**, documentação oficial — é excelente)

---

# 🤖 IA Aplicada a Backend [APOIO]

> Fase 16 (Vol. 1). RAG, embeddings, MCP, streaming.

---

# FASE 16 — IA Aplicada a Backend [APOIO]

> Diferencial forte no seu perfil, especialmente cruzando com automação industrial.

- [ ] Como um **LLM** funciona por cima: tokens, contexto, temperatura, sampling
- [ ] **Embeddings** e espaço vetorial; similaridade de cosseno
- [ ] **Bancos vetoriais**: pgvector, Qdrant, Chroma, Pinecone
- [ ] **RAG (Retrieval-Augmented Generation)**: chunking, estratégias de recuperação, reranking, avaliação
- [ ] Prompt engineering: few-shot, chain-of-thought, system prompt
- [ ] **Structured outputs** — forçar JSON válido de saída
- [ ] **Function calling / Tool use** — o LLM chamando sua API
- [ ] **Streaming de resposta** (SSE) — retoma a Fase 4.14
- [ ] **Agentes** e o **MCP (Model Context Protocol)** — construir um servidor MCP próprio
- [ ] Padrões de integração e resiliência com provedores de LLM (timeout, retry, fallback, custo por token, cache semântico)
- [ ] Avaliação e guardrails; alucinação e como mitigar
- [ ] Ferramentas de codificação assistida (Claude Code, Copilot, Cursor) — usar como acelerador **sem** terceirizar o entendimento

**📚 Livros:**
- *Building LLM Apps* / *AI Engineering* — Chip Huyen (**AI Engineering**, 2025, é a melhor referência atual)
- *Designing Machine Learning Systems* — Chip Huyen
- Documentação oficial dos provedores + o repositório de cookbooks da Anthropic/OpenAI (mais atualizado que qualquer livro nesta área)
