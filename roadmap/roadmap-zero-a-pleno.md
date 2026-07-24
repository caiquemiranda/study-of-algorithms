# 🗺️ Roadmap Zero → Pleno/Senior — Backend-first, sem lacunas

> Objetivo: eliminar os buracos de conhecimento, entender **como as coisas funcionam por dentro** antes de usar frameworks, e chegar a um nível pleno/senior sólido em Java, C++, Go e SQL (com Python para IA/APIs e TypeScript para o frontend).

## Como usar isso

Cada item tem uma marcação. Você decide o status agora, na primeira passada:

- 🔴 **Não sei / nunca estudei** → estudar do zero, com calma, com prática.
- 🟡 **Já ouvi falar / usei mas não entendo por dentro** → é aqui que estão seus buracos. Não pule — é exatamente o que você descreveu sentir.
- 🟢 **Domino de verdade (já expliquei/usei com profundidade)** → pule na 1ª passada, mas mantenha marcado para a **2ª passada de revisão geral**, que você faz depois de terminar tudo.

Regra de ouro: **nunca avance de fase enquanto tiver 🔴 na fase atual**. É exatamente essa impaciência (pular fundamento porque o curso "genérico" já assumia que você sabia) que criou os buracos.

---

## Visão geral das fases

| Fase | Tema | Por quê vem aqui |
|---|---|---|
| 1 | Fundamentos de computação, memória, SO, redes | Base de tudo. Sem isso, frameworks são "magia" |
| 2 | Lógica, complexidade, estruturas de dados, algoritmos | Vocabulário e ferramentas de raciocínio |
| 3 | C++ (baixa abstração) | Ver com as próprias mãos o que Java/Python escondem |
| 4 | A Web sem frameworks (16 pilares) | Entender o que Spring/FastAPI fazem por debaixo |
| 5 | SQL e bancos relacionais | Toda API pleno/senior depende disso |
| 6 | Go (concorrência) | Linguagem moderna, simples, ótima para revisar tudo da Fase 4 |
| 7 | Java + Spring em profundidade | Seu foco de mercado (BR) |
| 8 | Python aplicado (APIs + IA) | Seu uso real: IA e automações |
| 9 | TypeScript (comunicação com frontend) | Você já trabalha com frontend |
| 10 | Mensageria, Docker, arquitetura, SOLID | Pleno → Senior |
| 11 | Projetos-âncora progressivos | Onde tudo se junta na prática |

---

## FASE 1 — Fundamentos de Computação, Memória, SO e Redes

### 1.1 Como o computador executa um programa
- [ ] Binário, bytes, representação de números e texto (ASCII/UTF-8)
- [ ] CPU, registradores, ciclo fetch-decode-execute (visão geral, não precisa virar engenheiro de hardware)
- [ ] Hierarquia de memória: registrador → cache (L1/L2/L3) → RAM → disco, e por que isso importa para performance
- [ ] Compilação vs interpretação vs máquina virtual (o que acontece com um `.java`, um `.py`, um `.c` até rodar)

### 1.2 Memória em nível de processo
- [ ] Stack vs Heap: o que vai em cada um, por que a Stack é rápida e limitada, por que o Heap precisa de gerenciamento
- [ ] Ponteiros e endereços de memória (conceito, mesmo antes de C++)
- [ ] Vazamento de memória (memory leak) e por que processos de longa duração (um servidor rodando 48h) sofrem com isso
- [ ] Garbage Collection: ideia geral (você vai aprofundar isso de novo na Fase 3 e na Fase 7 com a JVM)

### 1.3 Sistema Operacional
- [ ] Processo vs Thread (o que o SO enxerga, custo de criar cada um, *context switching*)
- [ ] File Descriptor — "tudo é um arquivo" (filosofia Unix) — e por que um socket de rede é tratado como arquivo
- [ ] Syscalls (o programa "pedindo" algo ao SO — ler arquivo, abrir socket, alocar memória)
- [ ] Sinais (`SIGINT`, `SIGTERM`) — como um processo é avisado para desligar sem corromper dados
- [ ] `fork` — criar processo filho, e por que isso foi um gargalo histórico (ver CGI na Fase 4)

### 1.4 Redes — do cabo ao pacote
- [ ] Modelo TCP/IP em camadas (não precisa decorar o OSI completo, mas entender a ideia de camadas)
- [ ] Sockets: `bind`, `listen`, `accept`, `connect` — o vocabulário básico
- [ ] 3-way handshake (`SYN` → `SYN-ACK` → `ACK`)
- [ ] `127.0.0.1` (localhost) vs `0.0.0.0` — por que isso decide quem pode acessar sua aplicação
- [ ] TCP como fluxo contínuo de bytes (*stream*) — por que você precisa ler em buffers (ex: 1024 bytes por vez) e não existe "pacote = mensagem"
- [ ] DNS (visão geral: nome → IP), portas, e a diferença entre TCP e UDP

**✅ Checkpoint da Fase 1:** você consegue explicar em voz alta, sem gaguejar, o caminho completo de "digitei um endereço no navegador" até "o servidor recebeu bytes" — sem usar a palavra "framework" nenhuma vez.

**Recursos:** *Computer Networking: A Top-Down Approach* (Kurose & Ross) para redes; qualquer material introdutório de "Sistemas Operacionais" (ex: livro do Tanenbaum, capítulos de processos/memória) para o resto.

---

## FASE 2 — Lógica, Complexidade, Estruturas de Dados e Algoritmos

### 2.1 Análise de complexidade (Big-O)
- [ ] O que é Big-O e por que ele importa mais que "o código funciona"
- [ ] Complexidade de tempo vs espaço
- [ ] Reconhecer O(1), O(log n), O(n), O(n log n), O(n²) só de olhar o código (loops aninhados, recursão, etc.)

### 2.2 Estruturas de dados fundamentais (implementar do zero, sem usar a biblioteca da linguagem na primeira vez)
- [ ] Array e String (e por que strings são imutáveis em várias linguagens)
- [ ] Linked List (simples e duplamente encadeada)
- [ ] Stack e Queue
- [ ] Hash Table — como funciona o hashing, colisões, por que é O(1) "quase sempre"
- [ ] Árvores: árvore binária, BST (árvore de busca binária)
- [ ] Trie / Radix Tree — **este é o que aparece de novo na Fase 4** quando você for entender como frameworks tipo FastAPI/Starlette resolvem `/clientes/{id}` sem 500 `if`s
- [ ] Heap / Priority Queue
- [ ] Grafos: representação (lista de adjacência vs matriz), BFS, DFS

### 2.3 Algoritmos essenciais
- [ ] Ordenação: bubble/insertion (para entender), depois merge sort e quick sort (para usar de verdade)
- [ ] Busca binária
- [ ] Recursão (e recursão vs iteração, quando cada uma é melhor)
- [ ] Programação dinâmica (memoization, tabulação) — pelo menos os clássicos (fibonacci, mochila, subsequência)
- [ ] Algoritmos em grafos: Dijkstra (visão geral), detecção de ciclo

### 2.4 Prática deliberada
- [ ] Resolver problemas em uma plataforma de desafios (NeetCode 150, LeetCode ou Codewars) — meta: não é "resolver 500 problemas", é resolver o suficiente até parar de travar nos padrões básicos (two pointers, sliding window, BFS/DFS, DP)
- [ ] Refazer cada estrutura de dados do 2.2 sem consultar nada, do zero, em pelo menos uma linguagem

**✅ Checkpoint da Fase 2:** você consegue implementar uma Hash Table e uma BST do zero, sem olhar referência, e explicar a complexidade de cada operação.

---

## FASE 3 — C++ como linguagem de fundamentos (baixa abstração)

> Objetivo aqui não é "ser expert em C++ enterprise", é usar o C++ como lente de aumento para ver o que Java/Python escondem de você.

- [ ] Processo de compilação: pré-processador → compilador → *linker* → binário executável (diferença entre compilação e execução, que em Java/Python é escondida)
- [ ] Gerenciamento manual de memória: `new`/`delete`, `malloc`/`free`, e por que "esquecer" causa leak
- [ ] Ponteiros e referências na prática (não só o conceito da Fase 1 — agora usando)
- [ ] Stack allocation vs Heap allocation no código real (uma variável local vs um objeto criado com `new`)
- [ ] Smart pointers (visão geral — como C++ moderno evita o pesadelo do gerenciamento manual)
- [ ] Structs/classes, e como um objeto realmente existe na memória (layout de campos)
- [ ] **Projeto prático:** reimplementar em C++ pelo menos 2 estruturas da Fase 2 (ex: Linked List e Hash Table) gerenciando a memória manualmente — sentir na pele a diferença de não ter Garbage Collector

**✅ Checkpoint da Fase 3:** você consegue explicar, usando exemplos de C++, por que Java "não precisa" que você libere memória manualmente — e o que isso custa em performance (GC pausa a aplicação).

---

## FASE 4 — Desconstruindo a Web sem Frameworks (os 16 pilares)

> Esta é a fase que resolve diretamente o problema que você descreveu: usar Java/Spring, Python/FastAPI, etc. sem entender o que existe "por debaixo do `@app.get`". Faça isso em **Python puro** primeiro (biblioteca padrão, sem framework) — é a linguagem mais direta para isso — e depois **replique em Go** na Fase 6 para fixar de outro ângulo.

### 4.1 Sockets TCP/IP na prática
- [ ] Abrir um socket, dar `bind`, `listen`, `accept` usando só a biblioteca padrão (`socket` em Python)
- [ ] Ler bytes com `recv()` em loop até montar a mensagem completa

### 4.2 HTTP cru (parsing manual)
- [ ] Ler a *Request Line* (`GET /api/clientes HTTP/1.1`)
- [ ] Parsear Headers (formato `Chave: Valor`), entender `Host` e `Content-Length`
- [ ] Identificar o `\r\n\r\n` que separa headers do corpo (Body/Payload)
- [ ] Montar manualmente uma resposta HTTP válida (*Status Line* + Headers + corpo)

### 4.3 CGI (o ancestral — entender por que existiu)
- [ ] Como o Apache antigo executava um script por requisição via variáveis de ambiente (`REQUEST_METHOD`, `QUERY_STRING`)
- [ ] Por que o `fork` por requisição foi o gargalo que matou essa abordagem em escala

### 4.4 WSGI e ASGI
- [ ] WSGI: uma função só, recebendo `environ` (dict) e `start_response` — é isso que Django/Flask escondem de você
- [ ] ASGI: a versão assíncrona (`async`/`await`) — é a base do Uvicorn/FastAPI
- [ ] **Exercício:** escrever uma "aplicação" WSGI mínima de 10 linhas sem nenhum framework

### 4.5 Concorrência e I/O de baixo nível
- [ ] Thread-per-request (modelo clássico, forte em Java "puro") — custo de memória e context switching
- [ ] Event Loop + multiplexação de I/O (`epoll` no Linux) — como Node.js/FastAPI seguram tráfego alto com poucos recursos
- [ ] CPU-bound vs I/O-bound — por que isso decide a arquitetura certa

### 4.6 Gerenciamento de estado (HTTP é amnésico)
- [ ] Ciclo `Set-Cookie` / `Cookie`
- [ ] Sessão server-side vs client-side
- [ ] JWT: por que ele resolve o problema de escalar sem guardar sessão em memória do servidor

### 4.7 Comunicação com banco de dados (wire protocol)
- [ ] Banco de dados é só outro servidor TCP em uma porta (Postgres na 5432)
- [ ] Protocolo binário próprio (o driver empacota SQL em bytes, não manda string solta)
- [ ] Connection Pooling — por que abrir/fechar conexão a cada clique mata o sistema

### 4.8 Roteamento inteligente (URL Dispatching)
- [ ] Abordagem antiga: Regex compilada por rota
- [ ] Abordagem moderna: Radix Tree / Trie (conecta direto com o que você estudou na Fase 2.2)

### 4.9 Segurança de baixo nível
- [ ] Handshake TLS (ideia geral: troca de chaves antes do primeiro byte de HTTP)
- [ ] Hashing unidirecional + Salting (`bcrypt`/`Argon2`) — nunca criptografia de mão dupla para senha

### 4.10 Processamento em background
- [ ] Sinais POSIX (`SIGINT`, `SIGTERM`) para não corromper dados ao desligar durante um processamento longo
- [ ] Daemon / processo filho lendo de uma fila em memória — a base do que Celery/Spring Batch fazem

### 4.11 Serialização / Marshalling
- [ ] Como um objeto na memória (RAM) se transforma em JSON via Reflection (Java) / `inspect` (Python)
- [ ] Upload de arquivo grande via `multipart/form-data` sem explodir a RAM (leitura em *chunks*, delimitadores/*boundaries*)

### 4.12 Arquivos estáticos e cache
- [ ] `sendfile` (Zero-Copy) — disco direto pra rede sem passar pela CPU
- [ ] `ETag` / `Cache-Control` / `304 Not Modified`

### 4.13 Event loop próprio
- [ ] Implementar um loop `while True` rudimentar usando `select`/`selectors` (Python) monitorando múltiplos sockets

### 4.14 WebSockets e Server-Sent Events
- [ ] O `101 Switching Protocols` — como a conexão deixa de ser request-response e vira um túnel bidirecional

### 4.15 Proxy reverso
- [ ] Implementar um "porteiro" simples: aceita conexão na porta 80, lê o header `Host`, abre novo socket com a app interna (ex: porta 8000) e repassa bytes — a base do Nginx

### 4.16 Gerenciamento de memória em processos longos
- [ ] Por que um servidor que roda 48h precisa de Garbage Collection ativo (diferente do CGI, que "zerava" a cada clique)

**🏗️ Projeto prático central da Fase 4:** usar o repositório **`danistefanovic/build-your-own-x`** (seções "Build your own Web Server" e "Build your own Database") e implementar, em Python puro:
1. Um servidor HTTP do zero (sockets → parsing → resposta) atendendo pelo menos 2 rotas via *Radix Tree*.
2. Autenticação com sessão via cookie **e** via JWT (as duas, para comparar).
3. Upload de arquivo via multipart, salvando em chunks.

**Leituras de apoio:** *Foundations of Python Network Programming* (Rhodes & Goerzen), *High Performance Browser Networking* (Ilya Grigorik, grátis online), *Computer Networking: A Top-Down Approach* (Kurose & Ross).

**✅ Checkpoint da Fase 4:** você sobe seu próprio "mini-Flask" sem nenhuma lib de terceiros e ele responde HTTP de verdade no navegador.

---

## FASE 5 — SQL e Bancos de Dados Relacionais

- [ ] Modelo relacional: tabelas, chaves primária/estrangeira, normalização (1FN, 2FN, 3FN — pelo menos entender por que existem)
- [ ] SQL na prática: `SELECT`, `JOIN` (inner/left/right), `GROUP BY`, subqueries
- [ ] Índices: como aceleram busca (conecta com BST/B-Tree da Fase 2) e o custo em escrita
- [ ] Transações e ACID (Atomicidade, Consistência, Isolamento, Durabilidade)
- [ ] `EXPLAIN` / plano de execução (pelo menos ler um, mesmo que básico)
- [ ] **Projeto:** modelar um schema real (ex: o backend do seu projeto-âncora) e escrever as queries à mão antes de usar qualquer ORM

**✅ Checkpoint da Fase 5:** você explica por que um índice em uma coluna acelera `WHERE` mas pode piorar `INSERT`.

---

## FASE 6 — Go (concorrência e sistemas simples)

- [ ] Sintaxe e idiomas de Go (tipagem, structs, interfaces — sem "classes")
- [ ] Goroutines e Channels — o modelo de concorrência que resolve, de outro jeito, o que você viu na Fase 4.5
- [ ] `net/http` da standard lib (ver como Go já entrega um roteador básico embutido)
- [ ] **Projeto:** recriar o servidor HTTP da Fase 4 em Go puro (sem framework), comparando a concorrência de Go (goroutines) com o event loop que você implementou em Python

**✅ Checkpoint da Fase 6:** você sabe dizer, com exemplos, a diferença prática entre goroutines e threads do SO.

---

## FASE 7 — Java em profundidade (foco de mercado BR)

- [ ] JVM: bytecode, classloading, visão geral do Garbage Collector (agora com contexto da Fase 1 e 3)
- [ ] Memória da JVM: Heap, Stack, Metaspace
- [ ] OOP sólido: herança vs composição, interfaces, princípios SOLID (aprofundar na Fase 10)
- [ ] Coleções (List, Map, Set) e quando usar cada uma (conecta direto com Fase 2)
- [ ] Spring Boot: Injeção de Dependência, Spring MVC, Spring Data JPA/Hibernate, Spring Security
- [ ] **Projeto:** API CRUD completa com autenticação JWT, agora usando Spring — e você vai reconhecer cada peça porque já a construiu na mão na Fase 4

**✅ Checkpoint da Fase 7:** você consegue apontar, dentro de uma aplicação Spring Boot, qual peça faz o papel de cada um dos 16 pilares da Fase 4.

---

## FASE 8 — Python aplicado (APIs + IA)

- [ ] Python além do básico: generators, context managers, decorators, tipagem com `typing`
- [ ] `asyncio` e `async`/`await` na prática (conecta com ASGI da Fase 4.4)
- [ ] FastAPI: rotas, Pydantic, dependências, middlewares
- [ ] Integração com APIs de LLM (chamadas, streaming de resposta, tratamento de erro)
- [ ] **Projeto:** servir uma funcionalidade de IA (ex: RAG, chatbot) via API própria em FastAPI

---

## FASE 9 — TypeScript (comunicação com o frontend)

- [ ] Sistema de tipos: interfaces, generics, union types
- [ ] Tipagem de contratos de API (DTOs compartilhados entre front e back)
- [ ] Consumo de API (fetch/axios), tratamento de erro e loading state
- [ ] **Projeto:** conectar um frontend real aos backends das fases anteriores (Java e/ou Python)

---

## FASE 10 — Sistemas Distribuídos e Arquitetura (Pleno → Senior)

- [ ] Mensageria: Kafka (tópicos, partições, consumer groups) e RabbitMQ (filas, exchanges) — quando usar cada um
- [ ] Docker: containers, imagens, `docker-compose` para orquestrar sua API + banco + fila localmente
- [ ] Clean Architecture e SOLID aplicados de verdade (não só de nome)
- [ ] Observabilidade básica: logs estruturados, métricas, tracing (visão geral)

---

## FASE 11 — Projetos-Âncora Progressivos

Isso retoma o roadmap de projetos que você já tinha definido, agora com todo o fundamento por baixo:

1. **CRUD API** simples (Java/Spring ou Python/FastAPI) — mas agora você sabe o que o framework faz por você.
2. **Fluxo SDD** (spec-driven development) aplicado a um projeto real.
3. **Full-stack com Docker** — backend + frontend (TypeScript) + banco, tudo containerizado.
4. **Servidor MCP** — conectando com seu interesse em IA/automação.
5. **Capstone integrado com IA** — projeto final que junta linguagens, banco, mensageria e IA.

---

## Segunda passada (revisão geral)

Depois de terminar a Fase 11, volte ao topo e refaça **cada item marcado 🟢** — agora não para aprender, mas para confirmar. É comum, na segunda passada, descobrir que um 🟢 antigo na verdade era um 🟡 disfarçado. É esperado, e é exatamente esse tipo de buraco que este roadmap existe para fechar.

## Recursos centrais

- **Repositório:** `danistefanovic/build-your-own-x` (GitHub) — guias práticos de construir servidor web, banco de dados, etc. do zero, em várias linguagens
- **Livros:** *Computer Networking: A Top-Down Approach* (Kurose & Ross); *Foundations of Python Network Programming* (Rhodes & Goerzen); *High Performance Browser Networking* (Ilya Grigorik, gratuito)
- **Prática de algoritmos:** NeetCode 150 / LeetCode / Codewars
- **Comunidades:** Hacker News (arquitetura e papers), Dev.to (tags `#tcp`, `#networking`, "from scratch")
- **roadmap.sh/backend** — use como checklist complementar de tópicos de mercado (framework, deploy, testing), já que ele é mais focado no "o que o mercado pede" do que no "como funciona por dentro"
