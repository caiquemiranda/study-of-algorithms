# 11 — Grafos (BFS, DFS, Topological Sort, Union-Find)

> O modelo de tudo que se conecta. Soluções em [`../problemas/11_grafos/`](../problemas/11_grafos/).

## 1. Conceito Central e Analogia Didática

- **Representação padrão**: lista de adjacência (`no → vizinhos`), O(V+E) de espaço; grades 2D são grafos implícitos (célula = nó, 4 direções = arestas).
- **BFS** (fila) explora por camadas → **menor caminho sem pesos**; **DFS** (recursão/pilha) mergulha fundo → componentes, ciclos, flood fill.
- Extensões: **Topological Sort** (ordem de dependências em DAG; sobrou nó → há ciclo) e **Union-Find** ("estão no mesmo grupo?" quase O(1)).

**Analogia:** boato se espalhando: BFS é o boato por proximidade — primeiro os vizinhos, depois os vizinhos dos vizinhos (ondas). DFS é o fofoqueiro obsessivo que segue UMA cadeia de amigos até o fim antes de voltar e tentar outra.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "**ilhas / regiões / áreas conectadas**" em grade → flood fill (DFS/BFS).
- Se pede "**menor número de passos/movimentos**" sem pesos → BFS, sempre.
- Se a propagação parte de **várias fontes ao mesmo tempo** (laranjas podres, portões) → BFS multi-source (todas as fontes entram na fila juntas).
- Se envolve "**pré-requisitos / ordem de build / dependências**" → topological sort.
- Se pergunta "conectados? / aresta redundante? / quantos componentes?" sem precisar do caminho → Union-Find.

## 3. Templates de Código

### BFS em grade (menor caminho / multi-source)

```java
// Java — visitado marcado AO ENFILEIRAR: garante que cada célula entra na fila UMA vez
public int bfsGrade(char[][] grid, int[] inicio, int[] fim) {
    int R = grid.length, C = grid[0].length;
    int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
    boolean[][] visitado = new boolean[R][C];
    Queue<int[]> fila = new ArrayDeque<>();
    fila.offer(new int[]{inicio[0], inicio[1], 0});      // {linha, coluna, distância}
    visitado[inicio[0]][inicio[1]] = true;
    while (!fila.isEmpty()) {
        int[] atual = fila.poll();
        if (atual[0] == fim[0] && atual[1] == fim[1]) return atual[2]; // BFS: 1ª chegada = menor caminho
        for (int[] d : dirs) {
            int nr = atual[0] + d[0], nc = atual[1] + d[1];
            if (nr >= 0 && nr < R && nc >= 0 && nc < C
                    && !visitado[nr][nc] && grid[nr][nc] != '#') {
                visitado[nr][nc] = true;                 // marca AQUI, não ao desenfileirar
                fila.offer(new int[]{nr, nc, atual[2] + 1});
            }
        }
    }
    return -1;
}
```

```python
from collections import deque

def bfs_grade(grid, inicio, fim):
    R, C = len(grid), len(grid[0])
    fila = deque([(*inicio, 0)])
    visitado = {inicio}
    while fila:
        r, c, dist = fila.popleft()
        if (r, c) == fim:
            return dist                          # camadas garantem: primeira chegada é a mais curta
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visitado and grid[nr][nc] != "#":
                visitado.add((nr, nc))           # ao enfileirar: evita duplicatas na fila
                fila.append((nr, nc, dist + 1))
    return -1
```

### Topological Sort (Kahn) + detecção de ciclo

```python
from collections import deque

def topo_sort(n, arestas):                # arestas: (a, b) significa a -> b (a antes de b)
    adj = [[] for _ in range(n)]
    grau = [0] * n                        # grau de entrada: quantos pré-requisitos faltam
    for a, b in arestas:
        adj[a].append(b)
        grau[b] += 1
    fila = deque(i for i in range(n) if grau[i] == 0)   # começa por quem não depende de ninguém
    ordem = []
    while fila:
        u = fila.popleft()
        ordem.append(u)
        for v in adj[u]:
            grau[v] -= 1                  # u foi "cursado": libera uma dependência de v
            if grau[v] == 0:
                fila.append(v)
    return ordem if len(ordem) == n else None   # sobrou nó preso => ciclo de dependências
```

### Union-Find (DSU)

```java
// Java — find com path compression: a árvore achata a cada consulta
class DSU {
    private final int[] pai;
    DSU(int n) { pai = new int[n]; for (int i = 0; i < n; i++) pai[i] = i; }

    int find(int x) {
        while (pai[x] != x) {
            pai[x] = pai[pai[x]];   // pula uma geração: achatamento barato e eficaz
            x = pai[x];
        }
        return x;
    }

    boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false; // mesma raiz: uni-los criaria CICLO — informação valiosa
        pai[ra] = rb;
        return true;
    }
}
```

## 4. Walkthrough Visual (Teste de Mesa)

`topo_sort(4, [(0,1), (0,2), (1,3), (2,3)])` — 0 libera 1 e 2; ambos liberam 3:

| Passo | fila | u | grau após decrementos | ordem |
|---|---|---|---|---|
| início | `[0]` | — | `[0,1,1,2]` | `[]` |
| 1 | `[1,2]` | 0 | `[0,0,0,2]` | `[0]` |
| 2 | `[2]` | 1 | grau[3]: 2→1 | `[0,1]` |
| 3 | `[3]` | 2 | grau[3]: 1→0 → entra | `[0,1,2]` |
| 4 | `[]` | 3 | — | `[0,1,2,3]` ✔ |

- `len(ordem) == 4 == n` → sem ciclo; a ordem respeita todas as dependências.

## 5. Complexidade (Tempo e Espaço)

| Algoritmo | Tempo | Motivo |
|---|---|---|
| BFS / DFS | O(V + E) | cada nó e aresta visitados uma vez |
| Topological (Kahn) | O(V + E) | idem, com fila de grau zero |
| Union-Find | ~O(α(n)) por op | inverso de Ackermann ≈ constante |
| Espaço | O(V) | visitados + fila/pilha |

## 6. Pegadinhas e Erros Comuns

- Marcar visitado **ao desenfileirar** em vez de ao enfileirar → o mesmo nó entra várias vezes na fila (TLE clássico).
- Sem `visitado` em grafo com ciclo → loop infinito.
- Ciclo em grafo **dirigido** exige 3 estados (branco/cinza/preto) — o booleano do não-dirigido não detecta corretamente.
- Grafo **desconexo**: esquecer o loop externo sobre todos os nós (contagem de componentes sai errada).
- **Python**: DFS recursivo em grade grande estoura o limite de ~1000 frames → versão iterativa com pilha.
- **Java**: `LinkedList` como fila funciona, mas `ArrayDeque` é o idiomático e mais rápido.
- Union-Find sem path compression degrada para O(n) por operação em cadeias longas.

## 7. Aplicações no Mundo Real (Backend)

- **Topological sort é onipresente**: ordem de build (Maven/Gradle), execução de migrations, DAGs de pipeline (Airflow), resolução de dependências do Spring na subida do contexto.
- **PostgreSQL**: detecção de **deadlock** é busca de ciclo no grafo de espera de locks.
- **Kubernetes/service mesh**: grafo de dependências entre serviços; análise de raio de impacto de uma falha.
- **Union-Find**: detecção de partição de cluster e agrupamento de eventos correlacionados.
- BFS multi-source = propagação de invalidação de cache a partir de várias origens.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium |
| 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 🟡 Medium |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟡 Medium |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium |
| 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium |
| 684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟡 Medium |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🔴 Hard |
