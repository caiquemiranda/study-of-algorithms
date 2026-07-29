# [0707] Design Linked List

> 🔗 [LeetCode 707](https://leetcode.com/problems/design-linked-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Design` `#Sentinela` `#Medium`

## 📜 O Problema

Projete sua própria implementação de linked list, do zero (singular ou duplamente encadeada). Implemente `MyLinkedList`:
- `get(index)`: valor do nó no índice (0-indexado), ou `-1` se inválido.
- `addAtHead(val)` / `addAtTail(val)`: adiciona no início/fim.
- `addAtIndex(index, val)`: adiciona antes do nó naquele índice (se `index == tamanho`, adiciona no fim; se `index > tamanho`, não insere).
- `deleteAtIndex(index)`: remove o nó naquele índice, se válido.

**Exemplos:**
```
Input:
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1,2], [1], [1], [1]]
Output:
[null, null, null, null, 2, null, 3]

Explicação:
addAtHead(1) → lista [1]; addAtTail(3) → lista [1,3];
addAtIndex(1,2) → lista [1,2,3]; get(1) → 2;
deleteAtIndex(1) → lista [1,3]; get(1) → 3
```

**Restrições (e o que elas denunciam):**
- `0 <= index, val <= 1000`, até `2000` chamadas → volume pequeno, o foco não é performance extrema, é a **implementação correta** da estrutura
- "não use a biblioteca de LinkedList pronta" → o exercício é literalmente construir nós com `val` e `next` (e opcionalmente `prev`) manualmente, praticando a manipulação de ponteiros que os problemas anteriores da categoria só consomem

## 🧭 Como reconhecer o padrão

Este é o problema "meta" da categoria: em vez de resolver algo **usando** uma linked list, o exercício é **construir** a estrutura em si — `Node` com `val`/`next`, e as operações básicas (`get`, inserir, remover) reimplementadas com os mesmos padrões vistos nos outros problemas: **nó sentinela** para eliminar o caso especial "operação no índice 0" (ver [fundamentos](../../../fundamentos/06_linked_list.md)).

## 🐢 Solução 1 — Força bruta (usar um array/lista dinâmica por baixo dos panos)

Guarda os valores num `ArrayList<Integer>` interno. `get(index)` vira `list.get(index)` (O(1)); `addAtIndex`/`deleteAtIndex` viram `list.add(index, val)`/`list.remove(index)` (O(n), por causa do deslocamento de elementos).

- Tempo: O(1) para `get`, O(n) para inserção/remoção · Espaço: O(n)
- **Por que não basta:** tecnicamente essa abordagem até **vence** a linked list real em `get` (O(1) contra O(n) de percorrer nó a nó) — mas ela terceiriza exatamente o que o problema pede para praticar: manipular `next` manualmente. O objetivo deste exercício não é "qual estrutura é mais rápida", é entender por dentro como uma linked list gerencia inserção/remoção sem deslocar elementos, ao custo de não ter acesso O(1) por índice.

## 💡 Solução 2 — A ideia otimizada (intuição — a linked list de verdade)

Uma classe `Node` com `val` e `next`. Um **nó sentinela** (`dummy`) fixo antes do primeiro nó real, e um contador `size` para validar índices em O(1) sem precisar percorrer a lista. Toda operação (`get`, `addAtIndex`, `deleteAtIndex`) segue o mesmo padrão: anda `index` passos a partir de `dummy` para achar o nó **anterior** à posição de interesse, e a partir dali lê ou religa ponteiros — exatamente como em [0203] Remove Linked List Elements ou [0021] Merge Two Sorted Lists, só que agora generalizado para qualquer posição.

## 🎬 Exemplo passo a passo

Sequência do enunciado, com sentinela `dummy` fixo antes do índice 0:

| Operação | Ação | Lista resultante (a partir de `dummy.next`) |
|---|---|---|
| `addAtHead(1)` | insere no índice 0: `novo.next = dummy.next`; `dummy.next = novo` | `1` |
| `addAtTail(3)` | insere no índice `size=1` (equivalente a "no fim"): anda 1 passo, insere depois | `1 → 3` |
| `addAtIndex(1,2)` | anda 1 passo (chega no nó `1`), insere `2` logo depois | `1 → 2 → 3` |
| `get(1)` | anda 1 passo a partir de `dummy.next`, lê o valor | retorna `2` |
| `deleteAtIndex(1)` | anda 1 passo (chega no nó `1`), religa `prev.next = prev.next.next` (pula o `2`) | `1 → 3` |
| `get(1)` | anda 1 passo a partir de `dummy.next`, lê o valor | retorna `3` |

Resultado final: `[null, null, null, null, 2, null, 3]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(index) por operação — cada uma anda até a posição de interesse a partir da cabeça; `size` é mantido à parte, então validar um índice é O(1)
- **Espaço:** O(n) total para armazenar os `n` nós; O(1) extra por chamada

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MyLinkedList {
    private class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
    }

    private final Node dummy = new Node(0); // sentinela: get/add/delete no índice 0 não é caso especial
    private int size = 0;

    public int get(int index) {
        if (index < 0 || index >= size) return -1;
        Node cur = dummy.next;
        for (int i = 0; i < index; i++) cur = cur.next;
        return cur.val;
    }

    public void addAtHead(int val) {
        addAtIndex(0, val);
    }

    public void addAtTail(int val) {
        addAtIndex(size, val);
    }

    public void addAtIndex(int index, int val) {
        if (index > size) return; // índice além do fim: não insere, por contrato do enunciado
        if (index < 0) index = 0; // índice negativo: trata como inserir na cabeça

        Node prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;

        Node novo = new Node(val);
        novo.next = prev.next;
        prev.next = novo;
        size++;
    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;

        Node prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;

        prev.next = prev.next.next; // pula o nó do índice, desconectando-o
        size--;
    }
}
```

### Python (pratique você — reimplemente sem olhar o Java)
```python
# TODO: sua vez. Regra da trilha: implemente do zero no dia seguinte.
```

### C++ (pratique você)
```cpp
// TODO: sua vez.
```

## ⚠️ Pegadinhas e erros comuns

- **Esquecer de validar `index >= size` (ou `index < 0`) antes de `get`/`deleteAtIndex`**: sem essa checagem, o loop tentaria andar além do fim da lista, acabando em `NullPointerException` ao tentar `cur.next` num nó `null`.
- **Confundir a regra de `addAtIndex` para `index == size`**: o enunciado trata esse caso como "inserir no fim" (válido), não como erro — só `index > size` deve ser recusado.
- **Não manter `size` sincronizado**: esquecer de incrementar/decrementar `size` em `addAtIndex`/`deleteAtIndex` corrompe todas as validações de índice das chamadas seguintes.
- **Não usar sentinela**: sem `dummy`, inserir/remover no índice `0` (a cabeça real) exige tratamento especial separado do resto do código — o sentinela unifica tudo num único caminho de código.

## 🧪 Casos de teste para validar

| Caso | Sequência | Esperado | Por quê |
|---|---|---|---|
| Get em lista vazia | `get(0)` sem nenhuma inserção | `-1` | `size == 0`, qualquer índice é inválido |
| addAtIndex além do tamanho | `addAtHead(1); addAtIndex(5, 9)` | a inserção não acontece (lista continua `[1]`) | `index(5) > size(1)` |
| addAtIndex igual ao tamanho (equivalente a addAtTail) | `addAtHead(1); addAtIndex(1, 2)` | lista vira `[1,2]` | valida que `index == size` é tratado como inserção no fim, não erro |
| Deletar a cabeça | `addAtHead(1); addAtTail(2); deleteAtIndex(0); get(0)` | `2` | valida remoção no índice 0 via sentinela, sem caso especial |
| Sequência completa do enunciado | sequência acima | `[null,null,null,null,2,null,3]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0146] LRU Cache** (reaproveita a mesma ideia de nó + ponteiros, mas com uma lista **dupla** combinada a um hash map), **[0203] Remove Linked List Elements** e **[0021] Merge Two Sorted Lists** (os padrões de sentinela e travessia que este problema generaliza)
- No backend: implementar a estrutura de dados do zero (em vez de usar a `LinkedList`/`ArrayList` da linguagem) é exatamente o exercício que aparece ao construir bibliotecas de baixo nível — drivers de sistema, alocadores de memória customizados, ou estruturas de dados otimizadas para um caso de uso específico onde as garantias das coleções genéricas da linguagem (thread-safety, overhead de boxing, etc.) não servem.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
