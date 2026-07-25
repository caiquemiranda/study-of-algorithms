# 12 — Grafos Avançados (Dijkstra, Bellman-Ford, MST)

> Menor caminho com pesos e árvore geradora mínima. Soluções em [`../problemas/12_grafos_avancados/`](../problemas/12_grafos_avancados/).

## 1. Conceito Central e Analogia Didática

- **Dijkstra**: menor caminho de uma origem com **pesos positivos**; guloso com min-heap — o nó de menor distância no topo já tem distância final.
- **Bellman-Ford**: relaxa todas as arestas V−1 vezes (O(V·E)); aceita **pesos negativos** e detecta ciclo negativo; a variante limitada a K rodadas resolve "no máximo K paradas".
- **MST** (conectar tudo com custo mínimo): **Kruskal** = arestas ordenadas + Union-Find; **Prim** = cresce a árvore com heap de fronteira.

**Analogia (Dijkstra):** GPS calculando rota: das cidades com tempo estimado, ele **confirma** primeiro a de menor tempo — ninguém chega lá mais rápido por outro caminho, pois qualquer desvio passaria por algo já mais caro (só vale com "pedágios" positivos!).

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "menor caminho/custo/tempo" **com pesos** → Dijkstra (positivos) / Bellman-Ford (negativos ou limite de passos).
- Se pede "conectar **todos** os pontos com custo total mínimo" → MST.
- Se pede "minimize o **máximo** do caminho" (Swim in Rising Water) → Dijkstra trocando soma por `max`, ou busca binária + BFS.
- Se limita "**no máximo K paradas**" (voos) → Bellman-Ford com K rodadas e snapshot.
- Se as arestas têm peso 0/1 → BFS com deque (0-1 BFS); todos os pares em grafo pequeno → Floyd-Warshall O(V³).

## 3. Templates de Código

### Dijkstra com lazy deletion

```java
// Java — heap guarda {distância, nó}; entradas velhas são descartadas ao sair
public int[] dijkstra(int n, List<int[]>[] adj, int origem) {   // adj[u] = lista de {v, peso}
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[origem] = 0;
    PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
    heap.offer(new int[]{0, origem});
    while (!heap.isEmpty()) {
        int[] topo = heap.poll();
        int d = topo[0], u = topo[1];
        if (d > dist[u]) continue;            // entrada obsoleta: já confirmamos u por caminho melhor
        for (int[] viz : adj[u]) {
            int v = viz[0], nd = d + viz[1];
            if (nd < dist[v]) {               // relaxamento: achou caminho melhor até v
                dist[v] = nd;
                heap.offer(new int[]{nd, v}); // insere de novo; a versão velha morre no continue acima
            }
        }
    }
    return dist;
}
```

```python
import heapq
from collections import defaultdict

def dijkstra(n, arestas, origem):
    adj = defaultdict(list)
    for u, v, w in arestas:
        adj[u].append((v, w))
    dist = {origem: 0}
    heap = [(0, origem)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue                          # lazy deletion: ignora versão desatualizada
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist
```

### Bellman-Ford limitado (Cheapest Flights, K paradas)

```python
def cheapest_flights(n, voos, src, dst, k):
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):                  # k paradas = k+1 arestas no máximo
        novo = dist[:]                      # SNAPSHOT: limita a 1 aresta nova por rodada
        for u, v, w in voos:
            if dist[u] + w < novo[v]:       # relaxa lendo do estado ANTERIOR
                novo[v] = dist[u] + w
        dist = novo
    return dist[dst] if dist[dst] != INF else -1
```

### Kruskal (MST com Union-Find)

```python
def kruskal(n, arestas):                    # arestas: (peso, u, v)
    dsu = DSU(n)                            # DSU do arquivo 11_grafos.md
    custo = usadas = 0
    for w, u, v in sorted(arestas):         # gulosa: sempre a aresta mais barata disponível
        if dsu.union(u, v):                 # False = formaria ciclo → descarta
            custo += w
            usadas += 1
            if usadas == n - 1:             # árvore completa: n-1 arestas
                break
    return custo if usadas == n - 1 else -1 # -1 = grafo desconexo
```

## 4. Walkthrough Visual (Teste de Mesa)

Dijkstra, origem A: `A→B (peso 1), A→C (4), B→C (2)`

| Passo | heap (dist, nó) | pop | dist após relaxamentos |
|---|---|---|---|
| início | `[(0,A)]` | — | `{A:0}` |
| 1 | `[(1,B), (4,C)]` | (0,A) | `{A:0, B:1, C:4}` |
| 2 | `[(3,C), (4,C)]` | (1,B) | `{A:0, B:1, C:3}` (1+2 < 4) |
| 3 | `[(4,C)]` | (3,C) | C confirmado em 3 |
| 4 | `[]` | (4,C) | **descartada**: `4 > dist[C]=3` (lazy deletion) |

- Resultado: `{A:0, B:1, C:3}` ✔ — a entrada obsoleta `(4,C)` morreu no `continue`.

## 5. Complexidade (Tempo e Espaço)

| Algoritmo | Tempo | Restrição |
|---|---|---|
| Dijkstra (heap) | O((V+E) log V) | pesos ≥ 0 |
| Bellman-Ford | O(V·E) | detecta ciclo negativo |
| Kruskal | O(E log E) | ordenação domina |
| Prim | O(E log V) | denso: prefira |
| Floyd-Warshall | O(V³) | todos os pares, V pequeno |

## 6. Pegadinhas e Erros Comuns

- **Dijkstra com peso negativo**: resultado silenciosamente errado — a prova gulosa exige pesos ≥ 0.
- Esquecer o `if d > dist[u]: continue` → reprocessa nós e degrada a complexidade.
- Bellman-Ford limitado **sem snapshot** do array → usa 2+ arestas na mesma rodada e viola o limite de paradas.
- Confundir **MST com menor caminho**: MST minimiza a soma das arestas da árvore, não a distância entre dois nós.
- Marcar nó como "fechado" cedo demais quando o estado tem dimensão extra (K paradas): o mesmo nó pode valer com menos paradas.
- **Java**: `PriorityQueue<int[]>` sem `Comparator` explode com `ClassCastException` — arrays não são comparáveis.
- **Python**: tuplas `(dist, no)` funcionam direto no heapq; se `no` não for comparável, insira um contador de desempate no meio.

## 7. Aplicações no Mundo Real (Backend)

- **Roteamento de rede**: OSPF roda Dijkstra dentro de cada roteador; RIP é Bellman-Ford distribuído (Fase 1.4).
- **Logística/mapas**: rota mais barata com pedágios/tempo — Dijkstra e A* (Dijkstra + heurística).
- **Infraestrutura**: MST desenha a topologia física de custo mínimo (cabeamento entre prédios — seu domínio!).
- **Sistemas distribuídos**: escolher a réplica de menor latência = menor caminho ponderado (Vol. 2, Módulo E.1).
- Grafos de chamadas entre microsserviços com latência como peso → o "caminho crítico" do p99 é o mais pesado.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium |
| 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 🟡 Medium |
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium |
| 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | 🟡 Medium |
| 778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | 🔴 Hard |
| 269 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | 🔴 Hard |
