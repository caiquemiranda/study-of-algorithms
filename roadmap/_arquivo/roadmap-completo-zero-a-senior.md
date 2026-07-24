# 🗺️ Roadmap Definitivo: Zero → Pleno/Sênior (Backend-first)

> **Versão 2 — completa.** Consolida: seus documentos sobre "a web sem frameworks" (16 pilares), os roadmaps do roadmap.sh (Backend, Building APIs, System Design, Spring Boot) e uma bibliografia de referência por tema.
>
> Foco de mercado: **Java + Spring Boot**. Apoio: **Python** (IA/APIs), **TypeScript** (frontend), **SQL** (dados), **Go** (concorrência), **C++** (fundamentos de baixa abstração).

---

## 📋 Como usar este roadmap

### Sistema de marcação
Passe por **todos** os itens uma vez marcando o status. Não estude ainda — só classifique:

- 🔴 **Zero** — nunca estudei. Estudar do início, com prática.
- 🟡 **Superficial** — já usei/ouvi falar, mas não sei explicar como funciona por dentro. **Esses são seus buracos.** É o item mais importante da lista.
- 🟢 **Domino** — já expliquei para alguém, já usei com profundidade. Pula na 1ª passada.

### As 3 regras que resolvem seu problema

1. **Nunca avance de fase com 🔴 pendente na fase atual.** Foi pular fundamento que criou os buracos.
2. **🟡 é mais perigoso que 🔴.** O 🔴 você sabe que não sabe. O 🟡 te dá falsa confiança e te derruba lá na frente.
3. **Segunda passada obrigatória.** Terminou tudo? Volte e refaça os 🟢. Você vai descobrir que alguns eram 🟡 disfarçados.

### Teste de domínio real (aplique em cada item antes de marcar 🟢)
> Consigo explicar isso em voz alta, sem consultar nada, para alguém que não sabe — incluindo **por que existe** e **o que aconteceria se não existisse**?

Se não: é 🟡.

### Ordem de prioridade se o tempo apertar
As fases marcadas **[NÚCLEO]** são inegociáveis para o seu objetivo. As **[APOIO]** podem ser feitas em paralelo, mais devagar, ou depois. As **[AMPLIAÇÃO]** são para consolidar sênior.

---

## 🧭 Mapa geral

| # | Fase | Peso | Por que aqui |
|---|---|---|---|
| 0 | Ferramentas base (Linux, terminal, Git) | [NÚCLEO] | Sem isso nada mais funciona |
| 1 | Computação, memória, SO, redes | [NÚCLEO] | Base de todos os buracos |
| 2 | Algoritmos e Estruturas de Dados | [NÚCLEO] | Vocabulário de raciocínio |
| 3 | C++ — baixa abstração | [APOIO] | Ver o que Java/Python escondem |
| 4 | A Web sem frameworks (16 pilares) | [NÚCLEO] | Desmistifica Spring/FastAPI |
| 5 | SQL e Bancos Relacionais | [NÚCLEO] | Toda API depende disso |
| 6 | Design de APIs (REST e além) | [NÚCLEO] | Seu produto final |
| 7 | Java + Spring Boot em profundidade | [NÚCLEO] | Foco de mercado |
| 8 | Go — concorrência | [APOIO] | Revisar a Fase 4 por outro ângulo |
| 9 | Python aplicado (APIs + IA) | [NÚCLEO] | Seu uso real |
| 10 | TypeScript e integração com frontend | [APOIO] | Você já trabalha com isso |
| 11 | Testes e Qualidade | [NÚCLEO] | Separa júnior de pleno |
| 12 | Docker, CI/CD e Operação | [NÚCLEO] | Requisito de vaga pleno |
| 13 | Arquitetura de Software e Design Patterns | [NÚCLEO] | Pleno → Sênior |
| 14 | System Design e Escala | [AMPLIAÇÃO] | Sênior |
| 15 | Observabilidade e Confiabilidade | [AMPLIAÇÃO] | Sênior |
| 16 | IA aplicada a backend | [APOIO] | Seu interesse + diferencial |
| 17 | Projetos-âncora | [NÚCLEO] | Onde tudo se junta |

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

# FASE 2 — Algoritmos e Estruturas de Dados [NÚCLEO]

> Você pediu os tipos mais comuns **detalhados**. Esta fase é a mais granular do roadmap por isso.

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

**✅ Checkpoint da Fase 5:** você lê um `EXPLAIN ANALYZE`, identifica um N+1 num projeto real e explica qual nível de isolamento resolve um lost update.

**📚 Livros:**
- ⭐ *Designing Data-Intensive Applications* — **Martin Kleppmann** — se você só puder ler **um** livro técnico na vida, é este. Cobre bancos, replicação, consistência, sistemas distribuídos e mensageria com uma clareza rara. Tem edição em PT-BR.
- *SQL Antipatterns* — Bill Karwin (excelente e curto; mostra os erros que todo mundo comete)
- *Use a Cabeça! SQL* (Head First SQL) — para começar leve, em PT-BR
- *High Performance MySQL* — Baron Schwartz (mesmo usando Postgres, os conceitos valem)
- *The Art of PostgreSQL* — Dimitri Fontaine (se for focar em Postgres)
- *Database Internals* — Alex Petrov (como o banco funciona por dentro: B-Trees, LSM, consenso)

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

## 7.2 JVM
- [ ] Compilação: `.java` → bytecode `.class` → JVM → JIT → código nativo
- [ ] **Áreas de memória**: Heap (young/old generation), Stack por thread, Metaspace, Code Cache
- [ ] **Garbage Collectors**: Serial, Parallel, CMS, **G1** (padrão), **ZGC** e Shenandoah (baixa pausa)
- [ ] Stop-the-world e tuning básico (`-Xms`, `-Xmx`)
- [ ] Classloading e o modelo de delegação
- [ ] Ferramentas: `jstack`, `jmap`, `jstat`, **VisualVM**, JProfiler, Java Flight Recorder
- [ ] Diagnóstico de memory leak com heap dump

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

## 7.10 Microsserviços com Spring Cloud
- [ ] Quando **não** usar microsserviços (comece monolito modular — sério)
- [ ] **Spring Cloud Gateway** — API Gateway
- [ ] **Config Server** — configuração centralizada
- [ ] **Eureka / Service Discovery**
- [ ] **OpenFeign** — cliente HTTP declarativo
- [ ] **Resilience4j** — Circuit Breaker, Retry, Bulkhead, Rate Limiter
- [ ] **Micrometer** — métricas e tracing distribuído

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

# FASE 13 — Arquitetura de Software e Design Patterns [NÚCLEO]

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

---

# FASE 17 — Projetos-Âncora [NÚCLEO]

> Cada projeto força a integração das fases anteriores. **Um projeto real vale mais que dez cursos assistidos.**

1. **Mini-framework web** (Fase 4) — servidor HTTP do zero, sem dependências
2. **API CRUD com Spring Boot** — auth JWT, JPA, validação, tratamento global de erro, testes, migrations, Docker Compose
3. **API equivalente em FastAPI** — para comparar os dois ecossistemas com o mesmo domínio
4. **Sistema com mensageria** — dois serviços conversando via Kafka ou RabbitMQ, com outbox pattern e consumidor idempotente
5. **Full-stack completo** — backend Java + frontend TypeScript com tipos gerados do OpenAPI + Postgres + Redis, tudo em Docker Compose, com CI no GitHub Actions
6. **Servidor MCP** — conectando IA a uma ferramenta real
7. **Capstone — o projeto do seu diferencial:** plataforma de monitoramento predial/industrial. Ingestão de telemetria de dispositivos, banco time-series, alertas em tempo real via WebSocket/SSE, histórico, dashboard, e um módulo de diagnóstico com RAG sobre manuais técnicos.
   > Este último é o que te diferencia de todo mundo que fez o mesmo tutorial de "API de tarefas". Ele cruza os seus 10+ anos de automação com o seu novo perfil de engenheiro de software — e essa combinação é rara no mercado.

---

# 📚 Biblioteca essencial — a ordem de leitura

Se você comprasse **apenas 8 livros** para os próximos anos, nesta ordem:

| # | Livro | Quando ler |
|---|---|---|
| 1 | *Entendendo Algoritmos* (Grokking Algorithms) — Bhargava | Fase 2, agora |
| 2 | *Operating Systems: Three Easy Pieces* (grátis) | Fase 1 |
| 3 | *Redes de Computadores e a Internet* — Kurose & Ross | Fase 1/4 |
| 4 | *Effective Java* — Joshua Bloch | Fase 7 |
| 5 | *Refactoring* — Martin Fowler | Fase 11 |
| 6 | ⭐ *Designing Data-Intensive Applications* — Kleppmann | Fase 5/14 |
| 7 | *Clean Architecture* — Robert C. Martin | Fase 13 |
| 8 | *Release It!* — Michael Nygard | Fase 14/15 |

**Gratuitos que valem tanto quanto pagos:**
- *Operating Systems: Three Easy Pieces* — pages.cs.wisc.edu/~remzi/OSTEP/
- *High Performance Browser Networking* — hpbn.co
- *Pro Git* (PT-BR) — git-scm.com/book/pt-br
- *The System Design Primer* — github.com/donnemartin/system-design-primer
- *Google SRE Book* — sre.google/books
- *Architecture Patterns with Python* — cosmicpython.com
- *build-your-own-x* — github.com/codecrafters-io/build-your-own-x
- Refactoring.Guru (design patterns, em português)

---

# 🔁 A segunda passada

Terminou a Fase 17? Volte ao topo e refaça **cada item marcado 🟢**.

Você vai encontrar 🟡 disfarçados de 🟢 — isso é normal e é exatamente o ponto. O conhecimento que você tinha antes de construir um servidor HTTP do zero não é o mesmo conhecimento depois. A segunda passada é onde os buracos que você nem sabia que existiam ficam visíveis.

---

# ⚠️ Cinco avisos honestos

1. **Isto é um mapa de anos, não de meses.** Fases 0–7 já te colocam em vaga júnior/pleno. As fases 13–15 são consolidação de sênior. Não tente atropelar.
2. **Não estude nas 17 fases ao mesmo tempo.** Uma fase principal + no máximo uma de apoio em paralelo. A sobrecarga que você descreveu vem justamente de tentar tudo de uma vez.
3. **Constância vence intensidade.** 1h por dia todo dia bate 8h no sábado. Seu tempo é limitado — proteja o ritmo, não o volume.
4. **Você não precisa de 100% de tudo para se candidatar.** Depois da Fase 7 + Fase 11 + Fase 12, você já é candidato viável a pleno. Continue estudando *empregado*.
5. **Seu maior ativo não está neste roadmap.** São os 10+ anos de automação industrial. Backend + IoT industrial é um nicho com pouca gente qualificada e muita demanda. Direcione seus projetos para lá.
