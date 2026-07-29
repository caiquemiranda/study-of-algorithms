# [0430] Flatten a Multilevel Doubly Linked List

> 🔗 [LeetCode 430](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#DFS` `#DoublyLinkedList` `#Medium`

## 📜 O Problema

Você recebe uma linked list duplamente encadeada onde, além de `next` e `prev`, cada nó tem um ponteiro `child` que pode apontar para outra lista duplamente encadeada (que também pode ter filhos, formando uma estrutura **multinível**). Achate a lista para um único nível: se `curr` tem uma lista filha, ela deve aparecer **depois** de `curr` e **antes** de `curr.next` no resultado. Todos os ponteiros `child` devem ficar `null` no final.

**Exemplos:**
```
Input:  head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Input:  head = [1,2,null,3]
Output: [1,3,2]
Explicação: o nó de valor 1 tem uma lista filha [3]; ela é inserida entre 1 e o antigo próximo dele (2).
```

**Restrições (e o que elas denunciam):**
- Número de nós até 1000 → O(n) é o esperado, tanto em tempo quanto em espaço razoável
- `1 <= Node.val <= 10^5` → sem risco de overflow
- "a lista filha aparece entre `curr` e `curr.next`" → é literalmente a definição de uma travessia em **pré-ordem**: visita `curr`, depois mergulha na lista filha inteira (recursivamente, pois ela também pode ter filhos), e só depois continua para `curr.next`

## 🧭 Como reconhecer o padrão

Apesar do nome "linked list", a estrutura com um ponteiro `child` que aponta para outra sublista é, na prática, uma **árvore n-ária disfarçada** (cada nó pode ter um "filho" e um "próximo irmão"). "Achatar em pré-ordem" é a mesma técnica de DFS usada para serializar árvores (ver [fundamentos](../../../fundamentos/07_arvores.md) para o paralelo com [0114] Flatten Binary Tree to Linked List) — a diferença aqui é que a estrutura já chega como lista (com `prev`/`next`) em vez de `TreeNode`, então a categorização correta continua sendo linked list, mas a técnica de travessia é herdada de árvores.

## 🐢 Solução 1 — Força bruta (DFS coletando os nós numa lista auxiliar, depois religando tudo)

Faz uma travessia (pré-ordem: visita `curr`, depois `curr.child` recursivamente, depois `curr.next`) coletando os nós, na ordem visitada, numa `List<Node>` auxiliar. Depois, percorre essa lista religando `next`/`prev` entre posições consecutivas e zerando todo `child`.

- Tempo: O(n) · Espaço: O(n) para a lista auxiliar (+ O(d) de pilha de recursão, `d` = profundidade de aninhamento)
- **Por que não basta:** o tempo já é ótimo, mas materializar todos os nós numa lista à parte gasta O(n) de espaço extra — como a estrutura já é encadeada, dá para religar os ponteiros **durante** a própria travessia, sem essa lista intermediária, reduzindo o espaço extra para O(d) (proporcional à profundidade de aninhamento, não ao total de nós).

## 💡 Solução 2 — A ideia otimizada (intuição)

Usa uma **pilha explícita** para simular a travessia em pré-ordem sem recursão. Começa empilhando `head`. A cada passo: tira o nó do topo (`cur`), religa `prev.next = cur` e `cur.prev = prev` (onde `prev` é o último nó já colocado na lista achatada); se `cur` tem `next`, empilha (para ser processado **depois** de tudo que vier do `child`); se `cur` tem `child`, empilha **por último** (para ser processado **primeiro**, já que pilha é LIFO) e zera `cur.child`. Como o `child` é empilhado por cima do `next`, ele é desempilhado primeiro — exatamente a ordem pré-ordem exigida.

## 🎬 Exemplo passo a passo

`head = [1,2,null,3]`: nó 1 (`next`→2, `child`→3), nó 2 (sem `next`, sem `child`), nó 3 (sem `next`, sem `child`)

| Passo | Pilha (topo à direita) | `cur` retirado | Ação | Lista achatada até aqui |
|---|---|---|---|---|
| início | `[1]` | — | — | (vazia) |
| 1 | `[]` → empilha `2` depois `3` → `[2,3]` | 1 | religa `prev(dummy).next=1`; `1.child=3` existe → empilha `3` por cima; `1.next=2` existe → já tinha sido empilhado antes do child | `1` |
| 2 | `[2]` | 3 (topo, veio do child) | religa `1.next=3`, `3.prev=1`; sem `next`/`child` | `1 → 3` |
| 3 | `[]` | 2 | religa `3.next=2`, `2.prev=3`; sem `next`/`child` | `1 → 3 → 2` |

Resultado final: `1 → 3 → 2` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é empilhado e desempilhado exatamente uma vez
- **Espaço:** O(d) — a pilha guarda, no máximo, um nó "pendente" por nível de aninhamento ainda não fechado (bem menor que O(n) em estruturas pouco aninhadas)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public Node flatten(Node head) {
    if (head == null) return head;

    Node pseudoHead = new Node(0, null, head, null); // sentinela: simplifica a 1ª religação
    Node prev = pseudoHead;

    Deque<Node> pilha = new ArrayDeque<>();
    pilha.push(head);

    while (!pilha.isEmpty()) {
        Node cur = pilha.pop();

        prev.next = cur;
        cur.prev = prev;

        // Empilha 'next' ANTES de 'child': como pilha é LIFO, 'child' sai primeiro —
        // é isso que garante a ordem pré-ordem (child inteiro antes de continuar no next).
        if (cur.next != null) {
            pilha.push(cur.next);
        }
        if (cur.child != null) {
            pilha.push(cur.child);
            cur.child = null; // obrigatório: o enunciado exige todo child == null no resultado
        }

        prev = cur;
    }

    pseudoHead.next.prev = null; // desfaz a ligação com o sentinela descartável
    return pseudoHead.next;
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

- **Empilhar `child` antes de `next`**: inverte a ordem — o `next` sairia da pilha primeiro, e a sublista filha apareceria **depois** do resto do nível atual, violando a regra "filho aparece antes do próximo".
- **Esquecer de zerar `cur.child` depois de processá-lo**: o enunciado exige explicitamente que todo `child` termine `null` — deixar o ponteiro antigo pendurado (mesmo que não seja mais "alcançado" pela travessia principal) reprova a validação.
- **Esquecer de religar `prev`, só `next`**: como a estrutura é **duplamente** encadeada, um `next` religado sem o `prev` correspondente deixa a lista inconsistente para quem tentar percorrer de trás para frente.
- **Tentar resolver com BFS (fila) em vez de DFS (pilha/recursão)**: BFS processaria todos os nós de um "nível" antes de mergulhar nos filhos, produzindo uma ordem completamente diferente da pré-ordem exigida.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `[]` (`null`) | retorna cedo, `head == null` |
| Lista sem nenhum `child` | `head = [1,2,3]` | `[1,2,3]` | a pilha nunca ganha um nó "extra" via child, comportamento igual a uma lista simples |
| Filho no meio da lista, exemplo do enunciado | `head = [1,2,null,3]` | `[1,3,2]` | trace acima |
| Filho na cauda (sem `next` depois) | lista `1→2`, onde `2.child→3` | `[1,2,3]` | valida o caso onde não há nó "depois" do child para desempilhar por último |
| Aninhamento em múltiplos níveis (child do child) | `1 → 2`, `2.child → 3`, `3.child → 4` | `[1,2,3,4]` | valida que a pilha lida corretamente com child-de-child, não só um nível |

## 🔗 Conexões

- Problemas irmãos: **[0114] Flatten Binary Tree to Linked List** (mesma ideia de achatamento em pré-ordem, mas de uma árvore binária em vez de uma estrutura lista+child), **[0138] Copy List with Random Pointer** (também lida com uma linked list com um ponteiro extra além de `next`)
- No backend: achatar uma estrutura aninhada numa sequência linear preservando a hierarquia em pré-ordem é o padrão usado em **serialização de árvores de comentários aninhados** (threads de fórum, onde respostas a respostas viram uma lista linear para exibição) e em **parsers de estruturas de arquivo/diretório** que precisam listar arquivos e subpastas numa ordem de exibição específica sem materializar a árvore inteira em memória antes de começar a imprimir.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
