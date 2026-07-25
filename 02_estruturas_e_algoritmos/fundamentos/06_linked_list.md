# 06 — Linked List

> Nós encadeados por ponteiros: inserção O(1), acesso O(n), zero localidade de cache. Problemas em [`../problemas/06_linked_list/`](../problemas/06_linked_list/).

## Conceito

Cada nó guarda valor + referência para o próximo (e o anterior, na duplamente encadeada). Não há índice: para chegar ao k-ésimo, percorra. Em compensação, inserir/remover **com a referência em mãos** é O(1) — sem deslocar elementos.

**Técnicas centrais:**
1. **Nó sentinela (dummy)**: um nó falso antes da cabeça elimina os casos especiais de "remover/inserir na cabeça"
2. **Reversão de ponteiros**: `prev, cur, nxt` — o exercício mais fundamental; saiba fazer dormindo
3. **Fast & Slow (Floyd)**: `slow` anda 1, `fast` anda 2 → encontra o meio; se há ciclo, eles se encontram (prova: dentro do ciclo, fast aproxima 1 passo por iteração)
4. **Dois passes ou gap fixo**: para "remover o N-ésimo do fim", avance `fast` N passos e mova os dois juntos

## Como reconhecer no enunciado

- O input já é `ListNode` (óbvio) — a questão é **qual técnica**
- "detecte ciclo / encontre o meio / encontre a duplicata sem espaço extra" → fast & slow
- "reverta / reordene / rearranje" → reversão + (às vezes) achar o meio + merge
- "O(1) de espaço" em lista → manipulação de ponteiros, sem array auxiliar

## Templates

```python
# Reverter lista — O(n), O(1)
def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

# Fast & slow — meio da lista / detecção de ciclo
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow                      # em lista par, retorna o 2º do meio

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False

# Merge de duas listas ordenadas com sentinela — O(n+m)
def merge(l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
```

## Complexidade típica

Percursos O(n), espaço O(1) (iterativo). Recursão gasta O(n) de pilha — em entrevista, prefira iterativo e mencione o trade-off.

## Erros comuns

- Perder a referência do resto da lista antes de religar (`nxt = head.next` **antes** de sobrescrever)
- Esquecer o sentinela e tratar a cabeça como caso especial espalhado pelo código
- `fast.next.next` sem checar `fast and fast.next` → `NoneType` error
- Não religar o `next` do último nó (lista "vazando" para o lixo antigo — em reorder/split)
- Comparar nós por valor quando devia comparar por **identidade** (`is`)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 206. Reverse Linked List | 🟢 easy |
| 21. Merge Two Sorted Lists | 🟢 easy |
| 141. Linked List Cycle | 🟢 easy |
| 143. Reorder List | 🟡 medium |
| 19. Remove Nth Node From End | 🟡 medium |
| 138. Copy List with Random Pointer | 🟡 medium |
| 2. Add Two Numbers | 🟡 medium |
| 287. Find the Duplicate Number (Floyd em array!) | 🟡 medium |
| 146. LRU Cache (lista dupla + hash map) | 🟡 medium |
| 23. Merge k Sorted Lists (com heap) | 🔴 hard |
| 25. Reverse Nodes in k-Group | 🔴 hard |

## Conexão com backend

**LRU Cache (LC 146)** é a estrutura real de caches de aplicação (Caffeine, Redis `maxmemory-policy lru`): hash map para O(1) + lista dupla para ordem de uso. O custo de cache miss da linked list vs array (Fase 1.1) é o motivo de `ArrayList` quase sempre vencer `LinkedList` na prática — saiba defender isso em entrevista Java.
