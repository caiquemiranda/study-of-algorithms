# 09 — Heap / Priority Queue

> Acesso O(1) ao menor (ou maior) elemento; inserção e remoção O(log n). Problemas em [`../problemas/09_heap_priority_queue/`](../problemas/09_heap_priority_queue/).

## Conceito

**Heap binário**: árvore completa guardada num array (`filhos de i = 2i+1, 2i+2`), com a propriedade: pai ≤ filhos (min-heap) ou pai ≥ filhos (max-heap). Não é ordenado — só garante o extremo no topo. `heapify` de um array inteiro é O(n) (não O(n log n) — pegadinha de entrevista).

**Padrão Top-K** (o mais cobrado): para os K maiores, mantenha um **min-heap de tamanho K** — o topo é o "pior dos melhores"; se chegar algo maior, troque. O(n log k), muito melhor que ordenar tudo quando k ≪ n.

**Two Heaps**: um max-heap (metade menor) + um min-heap (metade maior), balanceados → mediana de stream em O(log n) por inserção.

⚠️ `heapq` do Python é **min-heap**; para max-heap, insira o valor negado.

## Como reconhecer no enunciado

- "os K maiores/menores/mais frequentes/mais próximos"
- "processar sempre o mais urgente/menor primeiro" → simulação com PQ
- "mediana de um stream" → two heaps
- "mesclar N fontes ordenadas" → heap com um cursor por fonte
- Dijkstra e A* usam PQ por definição (ver [12_grafos_avancados](12_grafos_avancados.md))

## Templates

```python
import heapq

# Top-K maiores — min-heap de tamanho k, O(n log k)
def k_maiores(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)       # descarta o menor do heap
    return heap                        # os k maiores (topo = k-ésimo maior)

# K mais frequentes — frequência + heap de tamanho k
from collections import Counter
def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda p: p[1])]

# Mediana de stream — two heaps
class MedianFinder:
    def __init__(self):
        self.baixo = []                # max-heap (negado): metade menor
        self.alto = []                 # min-heap: metade maior

    def addNum(self, num):
        heapq.heappush(self.baixo, -num)
        heapq.heappush(self.alto, -heapq.heappop(self.baixo))
        if len(self.alto) > len(self.baixo):        # rebalanceia
            heapq.heappush(self.baixo, -heapq.heappop(self.alto))

    def findMedian(self):
        if len(self.baixo) > len(self.alto):
            return -self.baixo[0]
        return (-self.baixo[0] + self.alto[0]) / 2
```

## Complexidade típica

push/pop: O(log n) · topo: O(1) · heapify: O(n) · Top-K: O(n log k).

## Erros comuns

- Esquecer que `heapq` é min-heap (e negar só na inserção, esquecendo de negar na leitura)
- Ordenar o array inteiro para pegar K elementos (O(n log n) desnecessário)
- Empatar tuplas não comparáveis no heap (em `(prioridade, objeto)`, adicione um contador de desempate)
- Tentar "atualizar" prioridade de um item dentro do heap — o idiomático é inserir de novo e **descartar entradas obsoletas ao remover** (lazy deletion, como no Dijkstra)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 703. Kth Largest Element in a Stream | 🟢 easy |
| 1046. Last Stone Weight | 🟢 easy |
| 973. K Closest Points to Origin | 🟡 medium |
| 215. Kth Largest Element in an Array | 🟡 medium |
| 621. Task Scheduler | 🟡 medium |
| 355. Design Twitter | 🟡 medium |
| 295. Find Median from Data Stream | 🔴 hard |

## Conexão com backend

Filas de prioridade sustentam: escalonadores do SO (Fase 1.3), timers de event loop (o próximo timeout fica no topo), retry com prioridade em filas de mensagens, Dijkstra em roteamento. O padrão Top-K é como se calculam "os K endpoints mais lentos" em observabilidade (Fase 15).
