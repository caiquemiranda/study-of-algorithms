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
