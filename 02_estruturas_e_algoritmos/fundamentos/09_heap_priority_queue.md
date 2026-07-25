# 09 — Heap / Priority Queue

> O extremo (menor/maior) sempre no topo em O(1); inserção/remoção O(log n). Soluções em [`../problemas/09_heap_priority_queue/`](../problemas/09_heap_priority_queue/).

## 1. Conceito Central e Analogia Didática

- **Heap binário**: árvore completa guardada num array (`filhos de i` = `2i+1`, `2i+2`); invariante: pai ≤ filhos (min-heap). NÃO é ordenado — só o topo é garantido.
- **Padrão Top-K**: para os K maiores, mantenha um **min-heap de tamanho K** — o topo é o "pior dos melhores"; chegou alguém melhor, troca. O(n log k).
- **Two Heaps**: max-heap (metade menor) + min-heap (metade maior) balanceados → mediana de stream em O(log n) por inserção.

**Analogia:** triagem de pronto-socorro: não importa a ordem completa da fila — só quem é o **mais urgente agora**. Quando um paciente entra, ele "borbulha" até sua posição de urgência; atender o próximo é sempre pegar o topo.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "**os K maiores/menores/mais frequentes/mais próximos**" → heap de tamanho K.
- Se pede "processe sempre o menor/mais urgente primeiro" → simulação com priority queue.
- Se pede "**mediana de um stream**" → two heaps.
- Se pede "**mescle N listas/fontes ordenadas**" → heap com um cursor por fonte.
- Se aparecer "agendador / intervalo mínimo entre tarefas iguais" (Task Scheduler) → heap por frequência.

## 3. Templates de Código

### Top-K maiores (min-heap de tamanho k)

```java
// Java — PriorityQueue é MIN-heap por padrão: perfeito, o topo é o k-ésimo maior
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> heap = new PriorityQueue<>();  // min-heap
    for (int n : nums) {
        heap.offer(n);
        if (heap.size() > k) {
            heap.poll();          // expulsa o menor: sobram sempre os k melhores vistos até aqui
        }
    }
    return heap.peek();           // topo = o menor entre os k maiores = k-ésimo maior
}
```

```python
import heapq

def find_kth_largest(nums, k):
    heap = []                        # heapq é SEMPRE min-heap
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)      # descarta o menor; o heap nunca passa de k elementos
    return heap[0]                   # topo do min-heap de tamanho k = k-ésimo maior
```

### Two Heaps (mediana de stream)

```java
// Java — max-heap guarda a metade MENOR; min-heap a metade MAIOR
class MedianFinder {
    private final PriorityQueue<Integer> baixo = new PriorityQueue<>(Comparator.reverseOrder()); // max-heap
    private final PriorityQueue<Integer> alto = new PriorityQueue<>();                            // min-heap

    public void addNum(int num) {
        baixo.offer(num);                 // entra sempre pelo lado menor...
        alto.offer(baixo.poll());         // ...e o maior do lado menor migra: garante baixo <= alto
        if (alto.size() > baixo.size()) { // rebalanceia: baixo pode ter no máx. 1 a mais
            baixo.offer(alto.poll());
        }
    }

    public double findMedian() {
        if (baixo.size() > alto.size()) return baixo.peek();       // ímpar: topo do lado cheio
        return (baixo.peek() + alto.peek()) / 2.0;                  // par: média das fronteiras
    }
}
```

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.baixo = []   # max-heap SIMULADO com valores negados
        self.alto = []    # min-heap normal

    def addNum(self, num):
        heapq.heappush(self.baixo, -num)                      # nega ao entrar no max-heap
        heapq.heappush(self.alto, -heapq.heappop(self.baixo)) # migra o maior do lado baixo
        if len(self.alto) > len(self.baixo):
            heapq.heappush(self.baixo, -heapq.heappop(self.alto))

    def findMedian(self):
        if len(self.baixo) > len(self.alto):
            return -self.baixo[0]                             # desfaz a negação ao ler!
        return (-self.baixo[0] + self.alto[0]) / 2
```

## 4. Walkthrough Visual (Teste de Mesa)

`findKthLargest(nums=[3, 2, 8, 5, 1], k=2)`

| n | heap após push | size > 2? | heap após poll |
|---|---|---|---|
| 3 | `[3]` | não | `[3]` |
| 2 | `[2, 3]` | não | `[2, 3]` |
| 8 | `[2, 3, 8]` | sim → sai 2 | `[3, 8]` |
| 5 | `[3, 5, 8]` | sim → sai 3 | `[5, 8]` |
| 1 | `[1, 5, 8]` | sim → sai 1 | `[5, 8]` |

- Topo final: **5** = 2º maior ✔ — o heap nunca cresceu além de k, e o array nunca foi ordenado.

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade | Motivo |
|---|---|---|
| push / poll | O(log n) | o elemento borbulha pela altura da árvore |
| peek (topo) | O(1) | invariante do heap |
| heapify de array inteiro | **O(n)** | pegadinha de entrevista: não é O(n log n) |
| Top-K | O(n log k) | heap limitado a k elementos |

## 6. Pegadinhas e Erros Comuns

- **Python**: `heapq` é só min-heap — negue os valores para max-heap e **desfaça a negação ao ler** (o esquecimento clássico).
- **Java**: `PriorityQueue` também é min-heap por padrão; para max, `Comparator.reverseOrder()`.
- **Java**: o **iterador** da PriorityQueue NÃO percorre em ordem — só `poll()` garante ordem.
- Ordenar o array inteiro para pegar K elementos: O(n log n) desnecessário quando k ≪ n.
- Tuplas com desempate: `(prioridade, objeto)` quebra se dois objetos não forem comparáveis → adicione contador incremental no meio.
- "Atualizar" prioridade dentro do heap não existe nas libs padrão → insira de novo e **descarte entradas obsoletas ao remover** (lazy deletion, como no Dijkstra).

## 7. Aplicações no Mundo Real (Backend)

- **Escalonadores**: CFS do Linux, thread pools com prioridade, retry com prioridade em filas de mensageria.
- **Timers de event loop**: Netty/Node mantêm o próximo timeout no topo de um heap.
- **RabbitMQ**: priority queues nativas — mensagens de prioridade alta furam a fila.
- **Observabilidade**: "top K endpoints mais lentos" em dashboards = Top-K com heap sobre stream de métricas.
- **Dijkstra** (roteamento OSPF, mapas) tem a priority queue como coração — ver [12_grafos_avancados](12_grafos_avancados.md).

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | 🟢 Easy |
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | 🟢 Easy |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | 🟡 Medium |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | 🟡 Medium |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | 🔴 Hard |
