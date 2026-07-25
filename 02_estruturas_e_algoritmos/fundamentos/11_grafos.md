# 11 — Grafos (BFS, DFS, fundamentos)

> Nós e arestas: o modelo de tudo que se conecta. Problemas em [`../problemas/11_grafos/`](../problemas/11_grafos/).

## Conceito

**Representações:**
- **Lista de adjacência** (`dict[no] -> [vizinhos]`): O(V+E) espaço — o padrão para grafos esparsos (quase sempre)
- **Matriz de adjacência**: O(V²) espaço, checagem de aresta O(1) — só para grafos densos ou pequenos
- **Grade (matriz 2D)**: um grafo implícito — cada célula é nó, vizinhos são as 4 direções

**Os dois motores:**
- **BFS** (fila): explora por camadas → **menor caminho em grafo NÃO ponderado**, propagação simultânea (multi-source)
- **DFS** (recursão/pilha): explora até o fundo → componentes conexos, detecção de ciclo, flood fill

**Extensões fundamentais:**
- **Ordenação topológica** (grafo dirigido acíclico): ordem que respeita dependências. Kahn = BFS por grau de entrada; ou DFS com pós-ordem invertida. Se sobrar nó não processado → **há ciclo**
- **Union-Find (DSU)**: conjuntos disjuntos com `find` (com path compression) e `union` (por rank) — quase O(1) amortizado; responde "estão no mesmo componente?" sem travessia

## Como reconhecer no enunciado

- "ilhas / regiões / áreas conectadas" em grade → DFS/BFS flood fill
- "menor número de passos/movimentos" → BFS
- "propagação a partir de várias fontes ao mesmo tempo" (podridão, portões) → BFS multi-source
- "pré-requisitos / ordem de compilação / dependências" → topological sort
- "conectar componentes / detectar redundância" → Union-Find

## Templates

```python
from collections import deque

# BFS — menor caminho em grade (número de passos)
def bfs_grade(grid, inicio, fim):
    R, C = len(grid), len(grid[0])
    fila = deque([(*inicio, 0)])
    visitado = {inicio}
    while fila:
        r, c, dist = fila.popleft()
        if (r, c) == fim:
            return dist
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visitado \
               and grid[nr][nc] != "#":
                visitado.add((nr, nc))            # marca AO ENFILEIRAR
                fila.append((nr, nc, dist + 1))
    return -1

# DFS — contar ilhas
def num_islands(grid):
    R, C = len(grid), len(grid[0])
    def afunda(r, c):
        if not (0 <= r < R and 0 <= c < C) or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            afunda(r + dr, c + dc)
    return sum(afunda(r, c) or 1
               for r in range(R) for c in range(C) if grid[r][c] == "1")

# Topological sort (Kahn) — detecta ciclo de quebra
def topo_sort(n, arestas):
    adj = [[] for _ in range(n)]
    grau = [0] * n
    for a, b in arestas:                 # a -> b
        adj[a].append(b); grau[b] += 1
    fila = deque(i for i in range(n) if grau[i] == 0)
    ordem = []
    while fila:
        u = fila.popleft(); ordem.append(u)
        for v in adj[u]:
            grau[v] -= 1
            if grau[v] == 0:
                fila.append(v)
    return ordem if len(ordem) == n else None    # None = ciclo

# Union-Find
class DSU:
    def __init__(self, n):
        self.pai = list(range(n))
    def find(self, x):
        while self.pai[x] != x:
            self.pai[x] = self.pai[self.pai[x]]   # path compression
            x = self.pai[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                           # já conectados (ciclo!)
        self.pai[ra] = rb
        return True
```

## Complexidade típica

BFS/DFS: O(V + E) · Topological: O(V + E) · Union-Find: ~O(α(n)) por operação (inverso de Ackermann, constante na prática).

## Erros comuns

- Marcar visitado **ao desenfileirar** em vez de ao enfileirar (nós duplicados na fila — TLE)
- Esquecer `visitado` e entrar em loop infinito em grafo com ciclo
- Em grafo **dirigido**, detectar ciclo exige 3 estados (branco/cinza/preto) — o `visitado` booleano do não-dirigido não basta
- DFS recursivo em grade gigante → RecursionError (Python limita ~1000; use iterativo ou aumente o limite)
- Não tratar grafo desconexo (loop externo sobre todos os nós)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 200. Number of Islands | 🟡 medium |
| 133. Clone Graph | 🟡 medium |
| 695. Max Area of Island | 🟡 medium |
| 994. Rotting Oranges (BFS multi-source) | 🟡 medium |
| 417. Pacific Atlantic Water Flow | 🟡 medium |
| 130. Surrounded Regions | 🟡 medium |
| 207/210. Course Schedule I e II (topo sort) | 🟡 medium |
| 684. Redundant Connection (Union-Find) | 🟡 medium |
| 261. Graph Valid Tree | 🟡 medium |

## Conexão com backend

Topological sort é o algoritmo de **build systems** (Maven/Gradle), resolução de migrations e DAGs de pipeline (Airflow). BFS é descoberta de rede; Union-Find aparece em detecção de partição de cluster. Grafos de dependência entre microsserviços são analisados exatamente assim (Fase 13.4).
