# 06 — Linked List

> Nós encadeados por ponteiros: inserção O(1), acesso O(n). Soluções em [`../problemas/06_linked_list/`](../problemas/06_linked_list/).

## 1. Conceito Central e Analogia Didática

- Cada nó = valor + referência ao próximo (e ao anterior, na duplamente encadeada). Sem índice: chegar ao k-ésimo custa O(k).
- Em troca, inserir/remover **com a referência em mãos** é O(1) — nenhum elemento é deslocado.
- Técnicas centrais: **nó sentinela (dummy)**, **reversão de ponteiros**, **fast & slow** (Floyd) e **gap fixo** entre dois ponteiros.

**Analogia:** caça ao tesouro: cada pista diz apenas onde está a **próxima** pista. Para chegar à 10ª, passe pelas 9 anteriores; mas para inserir uma pista nova entre duas, basta reescrever um bilhete — ninguém mais precisa saber.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se o input é `ListNode` → a questão é *qual técnica*, não *se* é lista.
- Se pede "**detecte ciclo**" / "**encontre o meio**" / "ache a duplicata sem espaço extra" → fast & slow.
- Se pede "**reverta / reordene** (in-place, O(1) espaço)" → reversão de ponteiros.
- Se pede "**remova o N-ésimo do fim** em uma passada" → dois ponteiros com gap de N.
- Se combina lista + acesso O(1) por chave (LRU) → lista dupla + hash map.

## 3. Templates de Código

### Reversão de ponteiros

```java
// Java — três referências andando juntas; o exercício mais fundamental da categoria
public ListNode reverseList(ListNode head) {
    ListNode prev = null;                // atrás de tudo: será a nova cabeça no fim
    while (head != null) {
        ListNode nxt = head.next;        // guarda o resto ANTES de sobrescrever — senão a lista se perde
        head.next = prev;                // a seta vira para trás: é a reversão em si
        prev = head;                     // prev avança
        head = nxt;                      // head avança pelo caminho salvo
    }
    return prev;                         // head virou null; prev parou no último nó (nova cabeça)
}
```

```python
def reverse_list(head):
    prev = None
    while head:
        nxt = head.next        # salva o resto antes de virar a seta
        head.next = prev       # inverte o ponteiro
        prev, head = head, nxt # avança o par
    return prev
```

### Fast & Slow (meio da lista / ciclo)

```java
// Java — fast anda 2, slow anda 1: quando fast acaba, slow está no meio
public ListNode middleNode(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {  // as DUAS checagens: fast pula de 2 em 2
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;                                  // lista par: retorna o 2º nó do meio
}

public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;  // em ciclo, fast alcança slow (aproxima 1 nó por volta)
    }
    return false;                        // fast achou o fim: sem ciclo
}
```

```python
def middle_node(head):
    slow = fast = head
    while fast and fast.next:      # a dupla condição protege o salto duplo
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:           # identidade (is), não valor: nós distintos podem ter o mesmo val
            return True
    return False
```

### Merge com sentinela

```java
// Java — o dummy elimina o caso especial "inserir na cabeça vazia"
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0), cur = dummy;
    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) { cur.next = l1; l1 = l1.next; }
        else                  { cur.next = l2; l2 = l2.next; }
        cur = cur.next;
    }
    cur.next = (l1 != null) ? l1 : l2;   // emenda o resto da lista que sobrou
    return dummy.next;                   // a resposta começa DEPOIS do sentinela
}
```

```python
def merge_two_lists(l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2      # 'or' devolve a lista não vazia (ou None)
    return dummy.next
```

## 4. Walkthrough Visual (Teste de Mesa)

`reverseList(1 → 2 → 3 → null)`

| Iteração | prev | head | nxt | ação |
|---|---|---|---|---|
| início | null | 1 | — | — |
| 1 | 1 | 2 | 2 | `1.next = null` (1 vira cauda) |
| 2 | 2 | 3 | 3 | `2.next = 1` |
| 3 | 3 | null | null | `3.next = 2` — loop encerra |

- Retorna `prev = 3` → lista final: `3 → 2 → 1 → null` ✔

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade |
|---|---|
| Acesso ao k-ésimo | O(k) |
| Inserção/remoção com referência | O(1) |
| Reversão / merge / fast&slow | O(n) tempo, O(1) espaço |
| Versões recursivas | O(n) tempo, **O(n) pilha** |

- Fast & slow acha o meio em **uma passada** — sem contar o tamanho antes.

## 6. Pegadinhas e Erros Comuns

- Sobrescrever `head.next` **antes** de salvar `nxt` → o resto da lista vira lixo inalcançável.
- `fast.next.next` sem checar `fast != null && fast.next != null` → `NullPointerException`/`AttributeError`.
- Dispensar o **sentinela** e espalhar `if (head == null)` pelo código — dummy elimina todos.
- **Java**: comparar nós com `.equals()` sobrescrito por valor quando o problema exige **identidade** (`==` de referência é o correto para detectar ciclo).
- **Python**: usar `==` (valor) onde deve ser `is` (identidade) na detecção de ciclo.
- Esquecer de fechar o `next` do último nó em reorder/split → lista "vaza" para os nós antigos (ciclo acidental).
- Em entrevista Java: saber defender por que `ArrayList` vence `LinkedList` na prática (cache locality — Fase 1.1).

## 7. Aplicações no Mundo Real (Backend)

- **LRU Cache** (LC 146) é a implementação real de caches: `LinkedHashMap` do Java, Caffeine, política LRU do Redis — hash map (O(1) por chave) + lista dupla (ordem de uso).
- **MVCC no PostgreSQL**: versões de uma linha formam cadeia encadeada que as transações percorrem.
- **Filas de mensageria em memória**: `ConcurrentLinkedQueue` (Java) encadeia nós com CAS.
- **Undo logs / WAL**: registros apontando para o anterior — a travessia reversa é uma linked list.
- Free lists de alocadores de memória (JVM, malloc) encadeiam blocos livres.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟢 Easy |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | 🟢 Easy |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 🟢 Easy |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | 🟡 Medium |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | 🟡 Medium |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | 🟡 Medium |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard |
