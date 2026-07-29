# [0019] Remove Nth Node From End of List

> 🔗 [LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#DoisPonteiros` `#Sentinela` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list, remova o `n`-ésimo nó **contado a partir do fim** e retorne a nova cabeça.

**Exemplos:**
```
Input:  head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input:  head = [1], n = 1
Output: []

Input:  head = [1,2], n = 1
Output: [1]
```

**Restrições (e o que elas denunciam):**
- Número de nós = `sz`, `1 <= sz <= 30` → array pequeno, mas o follow-up já entrega a meta real
- `1 <= n <= sz` → `n` é sempre válido; não é preciso tratar `n` maior que o tamanho da lista
- Follow-up "resolva em uma passada" → descarta a solução óbvia de duas passadas (contar o tamanho, depois andar); empurra para dois ponteiros com um **gap fixo** de `n`

## 🧭 Como reconhecer o padrão

"Remova o N-ésimo do fim, em uma passada" é a assinatura exata de **dois ponteiros com gap fixo** — ver [fundamentos](../../../fundamentos/06_linked_list.md), seção "Como Reconhecer". Contar "a partir do fim" sem poder andar para trás (linked list simples não tem ponteiro anterior) é o que força esse truque de manter uma distância constante entre dois ponteiros.

## 🐢 Solução 1 — Força bruta (duas passadas: contar, depois remover)

Primeira passada: percorre a lista inteira para contar o tamanho `sz`. Segunda passada: anda `sz - n` passos a partir de `head` para chegar ao nó **anterior** ao que será removido, e religa o ponteiro para pular esse nó.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o tempo assintótico já é O(n) (linear), mas exige **duas passadas completas** pela lista — o follow-up pede explicitamente uma solução em uma única passada, o que é possível e mais elegante com o truque do gap fixo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Usa um sentinela (`dummy`) antes de `head`, para cobrir o caso de remover a própria cabeça sem tratamento especial. Dois ponteiros, `fast` e `slow`, começam em `dummy`. Primeiro, `fast` anda `n + 1` passos sozinho — isso cria um **gap fixo** de `n + 1` nós entre `fast` e `slow`. Depois, os dois andam juntos, 1 passo por vez, até `fast` chegar em `null`. Nesse momento, `slow` está exatamente no nó **anterior** ao que precisa ser removido — porque a distância constante de `n + 1` garante que, quando `fast` "sai" da lista, `slow` ficou `n + 1` posições atrás do fim, ou seja, uma posição antes do n-ésimo nó a partir do fim.

## 🎬 Exemplo passo a passo

`head = [1,2,3,4,5]`, `n = 2` (remover o 2º nó a partir do fim → o nó de valor 4)

**Fase 1 — `fast` anda `n+1 = 3` passos sozinho a partir de `dummy`:**

| Passo | fast |
|---|---|
| início | dummy |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

**Fase 2 — `fast` e `slow` andam juntos até `fast` chegar em `null`:**

| Passo | slow | fast |
|---|---|---|
| início | dummy | 3 |
| 1 | 1 | 4 |
| 2 | 2 | 5 |
| 3 | 3 | null → loop encerra |

`slow` parou no nó de valor `3`, que é o nó **anterior** ao alvo (valor 4). Religa: `slow.next = slow.next.next` → pula o nó de valor 4.

Resultado final: `1 → 2 → 3 → 5` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada; `fast` percorre no máximo o tamanho da lista mais `n+1`
- **Espaço:** O(1) — só dois ponteiros e o sentinela

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0, head); // sentinela: cobre a remoção da própria head
    ListNode fast = dummy, slow = dummy;

    // fast anda n+1 passos sozinho: cria o gap fixo que faz slow parar
    // exatamente no nó ANTERIOR ao alvo quando fast chegar ao fim.
    for (int i = 0; i < n + 1; i++) {
        fast = fast.next;
    }

    // Anda os dois juntos até fast sair da lista — a distância constante
    // de n+1 é o que garante que slow para no lugar certo.
    while (fast != null) {
        fast = fast.next;
        slow = slow.next;
    }

    slow.next = slow.next.next; // pula o n-ésimo nó a partir do fim

    return dummy.next;
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

- **Andar `fast` só `n` passos em vez de `n + 1`**: sem o `+1`, `slow` para **no** nó alvo em vez de no nó **anterior** a ele — e sem uma referência ao anterior não dá para religar o ponteiro e remover.
- **Não usar sentinela**: quando o nó a remover é a própria `head` (ex.: `head=[1], n=1`), sem o `dummy` seria preciso um `if` especial antes do loop para esse caso.
- **Fazer duas passadas quando o follow-up pede uma só**: não é um erro de corretude, mas é a limitação que este problema existe para ensinar a evitar.
- **Esquecer que `n` sempre é válido pela restrição**: não é preciso validar `n > sz` ou `n <= 0` — a restrição `1 <= n <= sz` já garante que o gap sempre cabe dentro da lista.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Remover o único nó | `head=[1], n=1` | `[]` | testa a remoção da própria head via sentinela |
| Remover a cabeça de uma lista maior | `head=[1,2], n=2` | `[2]` | `fast` sai da lista rápido, `slow` fica no dummy |
| Remover a cauda | `head=[1,2,3], n=1` | `[1,2]` | gap mínimo, `slow` para no penúltimo nó |
| Remover do meio, exemplo do enunciado | `head=[1,2,3,4,5], n=2` | `[1,2,3,5]` | trace acima |
| Lista de um nó | `head=[1], n=1` | `[]` | menor caso possível, mesmo que o 1º já cubra isso, vale reforçar |

## 🔗 Conexões

- Problemas irmãos: **[0876] Middle of the Linked List** (outra aplicação de dois ponteiros com distância controlada, mas fast anda 2x mais rápido em vez de manter gap fixo), **[0061] Rotate List** (também precisa localizar uma posição relativa ao fim da lista)
- No backend: manter dois cursores com distância fixa entre si é o mesmo padrão usado em **janelas deslizantes sobre streams** (processar o elemento que está a `k` posições atrás do cursor atual, sem materializar tudo em memória) e em **buffers circulares** de sistemas de log, onde se precisa saber "o que aconteceu N eventos atrás" sem contar o stream inteiro de novo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
