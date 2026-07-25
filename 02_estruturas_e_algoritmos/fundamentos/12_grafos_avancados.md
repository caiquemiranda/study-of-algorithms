# 12 — Grafos Avançados (Dijkstra, MST, Bellman-Ford)

> Menor caminho com pesos, árvore geradora mínima e variações. Problemas em [`../problemas/12_grafos_avancados/`](../problemas/12_grafos_avancados/).

## Conceito

**Dijkstra** — menor caminho de uma origem, **pesos positivos**. Guloso com min-heap: sempre expande o nó de menor distância conhecida (essa distância já é final). Com pesos negativos, a premissa quebra — use Bellman-Ford.

**Bellman-Ford** — relaxa todas as arestas V−1 vezes: O(V·E). Aceita pesos negativos e **detecta ciclo negativo** (se a V-ésima rodada ainda melhora algo). Variante com limite de K passos: Cheapest Flights.

**Floyd-Warshall** — todos os pares, O(V³), DP sobre "posso passar pelo nó k?". Só para grafos pequenos.

**MST (Minimum Spanning Tree)** — conectar todos os nós com custo total mínimo:
- **Kruskal**: ordena arestas por peso + Union-Find para pular as que formam ciclo — O(E log E)
- **Prim**: cresce a árvore a partir de um nó com min-heap de arestas de fronteira — O(E log V)

**A* **: Dijkstra + heurística admissível (nunca superestima) — prioriza `dist + estimativa(destino)`.

## Como reconhecer no enunciado

- "menor caminho/custo/tempo" **com pesos** → Dijkstra (positivos) ou Bellman-Ford (negativos/limite de paradas)
- "conectar todos os pontos com custo mínimo" → MST
- "minimize o máximo do caminho" (Swim in Rising Water) → Dijkstra trocando soma por `max`, ou busca binária + BFS
- "no máximo K paradas/passos" → Bellman-Ford limitado ou BFS por camadas com estado

## Templates

```python
import heapq
from collections import defaultdict

# Dijkstra — O((V+E) log V)
def dijkstra(n, arestas, origem):
    adj = defaultdict(list)
    for u, v, w in arestas:
        adj[u].append((v, w))
    dist = {origem: 0}
    heap = [(0, origem)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue                     # entrada obsoleta (lazy deletion)
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

# Bellman-Ford com limite de K paradas (Cheapest Flights)
def cheapest_flights(n, voos, src, dst, k):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(k + 1):
        novo = dist[:]                   # snapshot: no máx 1 aresta por rodada
        for u, v, w in voos:
            if dist[u] + w < novo[v]:
                novo[v] = dist[u] + w
        dist = novo
    return dist[dst] if dist[dst] != float("inf") else -1

# Kruskal (MST) — usa a DSU do arquivo 11
def kruskal(n, arestas):                 # arestas: (peso, u, v)
    dsu = DSU(n)
    custo = usadas = 0
    for w, u, v in sorted(arestas):
        if dsu.union(u, v):
            custo += w; usadas += 1
            if usadas == n - 1:
                break
    return custo if usadas == n - 1 else -1   # -1 = grafo desconexo
```

## Complexidade típica

| Algoritmo | Tempo | Restrição |
|---|---|---|
| Dijkstra (heap) | O((V+E) log V) | pesos ≥ 0 |
| Bellman-Ford | O(V·E) | detecta ciclo negativo |
| Floyd-Warshall | O(V³) | todos os pares, grafo pequeno |
| Kruskal | O(E log E) | MST |
| Prim | O(E log V) | MST |

## Erros comuns

- Dijkstra com peso negativo (resultado silenciosamente errado)
- Esquecer o descarte de entradas obsoletas do heap (`if d > dist[u]: continue`)
- Bellman-Ford limitado **sem o snapshot** do array (permite usar 2+ arestas na mesma rodada)
- Confundir MST com menor caminho — MST minimiza a **soma total das arestas da árvore**, não o caminho entre dois nós
- Marcar visitado antes da hora no Dijkstra com estado extra (ex.: K paradas — o mesmo nó pode valer a pena com menos paradas)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 743. Network Delay Time (Dijkstra) | 🟡 medium |
| 1584. Min Cost to Connect All Points (MST) | 🟡 medium |
| 787. Cheapest Flights Within K Stops | 🟡 medium |
| 778. Swim in Rising Water | 🔴 hard |
| 269. Alien Dictionary (topo sort) | 🔴 hard |
| 332. Reconstruct Itinerary | 🔴 hard |

## Conexão com backend

Dijkstra roda em protocolos de roteamento (OSPF) e em qualquer "rota mais barata" (logística, latência entre datacenters). MST é o desenho de rede física de custo mínimo. Bellman-Ford distribuído é a base histórica do RIP. Em sistemas: menor caminho ponderado = escolher réplica de menor latência (Vol. 2, Módulo E.1).
