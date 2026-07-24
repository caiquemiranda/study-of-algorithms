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
