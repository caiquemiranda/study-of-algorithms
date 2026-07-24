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
