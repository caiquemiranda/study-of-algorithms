# [0142] Linked List Cycle II

> 🔗 [LeetCode 142](https://leetcode.com/problems/linked-list-cycle-ii/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#LinkedList` `#FastSlow` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list, retorne o **nó onde o ciclo começa**. Se não houver ciclo, retorne `null`. Você **não pode modificar a lista** (nem marcar nós visitados alterando algum campo).

**Exemplos:**
```
Input:  head = [3,2,0,-4], pos = 1    Output: nó de índice 1 (valor 2)
Explicação: a cauda (-4) aponta de volta para o 2º nó — o ciclo começa ali.

Input:  head = [1,2], pos = 0         Output: nó de índice 0 (valor 1)
Explicação: o ciclo começa logo na cabeça.

Input:  head = [1], pos = -1         Output: null (sem ciclo)
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → O(n) é tranquilo; não é sobre tempo, é sobre **espaço**
- `-10^5 <= Node.val <= 10^5` → valores **podem se repetir**, então não dá para usar o `val` para saber "já visitei este nó"; é preciso comparar **identidade de nó** (referência), não valor
- `pos` é `-1` ou um índice válido → se existir ciclo, ele sempre volta para um nó **real** da lista (nunca "flutua" fora dela)
- "não modifique a lista" → descarta o truque de marcar nós visitados (ex.: setar um campo sentinel); empurra para duas soluções legítimas: hash set (gasta memória) ou o algoritmo de Floyd (não gasta)

## 🧭 Como reconhecer o padrão

"Detecte ciclo" no enunciado já é a assinatura clássica de **fast & slow (Floyd)** — ver [fundamentos](../../../fundamentos/06_linked_list.md), seção "fast & slow". A diferença para o irmão mais simples (LC 141, que só pergunta *se existe* ciclo) é que aqui é preciso **localizar o nó** onde o ciclo começa — isso exige uma segunda fase depois de detectar o encontro dos ponteiros.

## 🐢 Solução 1 — Força bruta (hash set de nós visitados)

Percorre a lista guardando cada nó visitado num `HashSet` (por **referência**, não por valor). No primeiro nó que já está no set, esse é o início do ciclo. Se chegar em `null`, não há ciclo.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** o resultado está correto, mas gasta memória proporcional ao tamanho da lista. Como o problema é sobre listas encadeadas — categoria em que O(1) de espaço é quase sempre alcançável com dois ponteiros —, guardar todos os nós num set é desperdiçar a estrutura mais barata disponível (é o follow-up clássico deste problema: "resolva com memória O(1)").

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, detecta o ciclo do jeito de sempre: `slow` anda 1, `fast` anda 2. Se existe ciclo, eles se encontram em algum nó **dentro** do ciclo (fast "dá a volta" e alcança slow por trás).

A parte não óbvia é achar o **início** do ciclo a partir desse ponto de encontro. A matemática por trás:
- Seja `a` = distância da cabeça até o início do ciclo, `b` = distância do início do ciclo até o ponto de encontro, `c` = distância do ponto de encontro de volta até o início do ciclo (então o ciclo tem tamanho `L = b + c`).
- Quando se encontram: `slow` andou `a + b`; `fast` andou o dobro, `2(a+b)`, e também andou `a + b + n·L` (deu `n` voltas extras no ciclo). Igualando: `a + b = n·L`, ou seja, `a = n·L - b = (n-1)·L + c`.
- Isso significa: andar `a` passos a partir da **cabeça** é a mesma distância (módulo o tamanho do ciclo) que andar `c` passos a partir do **ponto de encontro**.

Na prática: depois de achar o encontro, resete um ponteiro para `head` e mantenha o outro no ponto de encontro. Ande **1 passo de cada vez** com os dois. Onde eles se encontrarem de novo é o início do ciclo — garantido pela conta acima, sem precisar saber `a`, `b` ou `c` de verdade.

## 🎬 Exemplo passo a passo

`head = [3,2,0,-4]`, `pos = 1` (nós: A=3, B=2, C=0, D=-4, e `D.next = B`)

**Fase 1 — achar o ponto de encontro:**

| Passo | slow | fast | slow == fast? |
|---|---|---|---|
| 1 | B | C | não |
| 2 | C | B | não |
| 3 | D | D | **sim** → encontro em D |

**Fase 2 — achar o início do ciclo (1 passo de cada vez, um a partir de `head`):**

| Passo | ptr (desde head) | encontro (desde D) | iguais? |
|---|---|---|---|
| 0 | A | D | não |
| 1 | B | B | **sim** → início do ciclo é **B** |

Resultado final: nó de valor `2` (índice 1) ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada fase é, no pior caso, uma passada proporcional ao número de nós (a fase 2 nunca anda mais que `a + c ≤ n` passos)
- **Espaço:** O(1) — apenas três ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode detectCycle(ListNode head) {
    ListNode slow = head, fast = head;

    // Fase 1: fast anda 2x mais rápido que slow. Se existe ciclo, eles
    // necessariamente se encontram dentro dele (fast "dá a volta" por trás).
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;

        if (slow == fast) {                 // identidade de nó, não valor!
            // Fase 2: a prova matemática de Floyd garante que andar 1 passo
            // por vez a partir da CABEÇA e a partir do PONTO DE ENCONTRO
            // faz os dois ponteiros se encontrarem exatamente no início do ciclo.
            ListNode ptr = head;
            while (ptr != slow) {
                ptr = ptr.next;
                slow = slow.next;
            }
            return ptr;
        }
    }

    // fast chegou ao fim da lista (null): não existe ciclo.
    return null;
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

- **Comparar por valor (`slow.val == fast.val`) em vez de identidade (`slow == fast`)**: como `Node.val` pode se repetir (`-10^5 <= val <= 10^5` não garante unicidade), comparar por valor gera falso positivo em listas sem ciclo mas com valores duplicados.
- **Esquecer a checagem dupla `fast != null && fast.next != null`**: sem ela, `fast.next.next` explode com `NullPointerException` assim que `fast` chega perto do fim de uma lista sem ciclo.
- **Fase 2 começando do lugar errado**: o ponteiro resetado precisa partir de `head`, não do ponto de encontro. É fácil, sob pressão, mover os dois a partir do encontro — isso não converge no início do ciclo (a prova matemática depende de um dos dois começar em `head`).
- **Tentar marcar nós visitados alterando algo neles** (ex.: setar `val` para um sentinel): além de violar "não modifique a lista", não há valor seguro para usar como sentinel, já que `val` pode ser qualquer número entre `-10^5` e `10^5`.
- **Confundir com o LC 141**: aquele só pede `true`/`false`; aqui é preciso retornar o **nó**, o que exige a fase 2 — só rodar a fase 1 resolve o problema errado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `null` | `fast` já é `null` de cara, loop nem roda |
| Um nó, sem ciclo | `[1], pos=-1` | `null` | `fast.next` vira `null` na 1ª checagem |
| Um nó, ciclo nele mesmo | `[1], pos=0` | nó de valor 1 | menor ciclo possível: o nó aponta para si mesmo |
| Ciclo começa na cabeça | `[1,2], pos=0` | nó de valor 1 | testa a fase 2 quando `a = 0` (ptr não precisa andar) |
| Ciclo no meio | `[3,2,0,-4], pos=1` | nó de valor 2 | exemplo do enunciado, trace acima |
| Lista maior sem ciclo | `[1,2,3,4,5], pos=-1` | `null` | `fast` percorre até o fim normalmente, sem encontro |

## 🔗 Conexões

- Problemas irmãos: **[0141] Linked List Cycle** (mesma fase 1, mas só pede `true`/`false`), **[0202] Happy Number** (o mesmo algoritmo de Floyd aplicado a uma sequência numérica em vez de nós encadeados), **[0287] Find the Duplicate Number** (aplica Floyd's num array tratado como lista encadeada implícita via índices)
- No backend: detectar ciclo sem gastar memória extra é o mesmo raciocínio usado para achar referência circular em grafos de dependência (import cycles, containers de injeção de dependência) ou para garantir que uma cadeia de ponteiros `next`/`parent` (ex.: lista de blocos livres de um alocador, cadeia de redirecionamentos de URL) não entra em loop infinito.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
