# [0061] Rotate List

> 🔗 [LeetCode 61](https://leetcode.com/problems/rotate-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#ListaCircular` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list, rotacione a lista para a **direita** em `k` posições.

**Exemplos:**
```
Input:  head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input:  head = [0,1,2], k = 4
Output: [2,0,1]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 500]` → O(n) é o esperado
- `0 <= k <= 2 * 10^9` → **essa é a pegadinha central**: `k` pode ser muito maior que o tamanho da lista (o 2º exemplo já mostra `k=4` numa lista de 3 nós). Rotacionar `k` vezes de fato, uma posição por vez, seria catastroficamente lento (e `k` nem cabe com folga num laço ingênuo) — o valor **efetivo** de rotação é sempre `k % n`, porque rotacionar `n` vezes devolve a lista ao estado original

## 🧭 Como reconhecer o padrão

"Mova os últimos `k` elementos para o início" é resolvido de forma elegante transformando a lista **temporariamente numa lista circular**: fechar o ciclo (`tail.next = head`), andar até o ponto de corte certo, e abrir o ciclo de novo no lugar novo. É uma variação do padrão de dois ponteiros/contagem de posição da categoria (ver [fundamentos](../../../fundamentos/06_linked_list.md)), combinada com o insight de que rotação é periódica módulo `n`.

## 🐢 Solução 1 — Força bruta (rotacionar uma posição por vez, k vezes)

Para cada uma das `k` rotações: acha o último nó, desconecta ele do resto, e o reconecta como nova cabeça (rotação de 1 posição). Repete isso `k` vezes.

- Tempo: O(n · k) · Espaço: O(1)
- **Por que não basta:** com `k` até `2 × 10^9`, rodar o processo `k` vezes é inviável — mesmo que cada rotação individual seja O(n), multiplicar por `k` estoura qualquer limite de tempo. Além disso, é redundante: rotacionar uma lista de `n` nós por `n` posições devolve exatamente a lista original, então a maior parte das `k` iterações não faz nada de novo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, reduz `k` ao seu **valor efetivo**: como rotacionar `n` vezes é o mesmo que não rotacionar, o deslocamento real é `k % n` (e se der 0, a lista não muda). Depois, a rotação de `k % n` posições para a direita é equivalente a: a nova cabeça é o nó que está `k % n` posições **antes do fim**, e a nova cauda é o nó logo antes dela.

O truque de implementação: fecha a lista num **ciclo** (`tail.next = head`), anda `n - (k % n) - 1` passos a partir de `head` para achar a nova cauda, pega `newTail.next` como a nova cabeça, e **quebra o ciclo** (`newTail.next = null`).

## 🎬 Exemplo passo a passo

`head = [1,2,3,4,5]`, `k = 2`, `n = 5`

| Etapa | Cálculo | Valor |
|---|---|---|
| `k` efetivo | `k % n` = `2 % 5` | 2 |
| Passos até a nova cauda | `n - k%n - 1` = `5 - 2 - 1` | 2 |
| Andar 2 passos a partir de `head` (1→2→3) | novo tail | nó de valor **3** |
| `newTail.next` | nova cabeça | nó de valor **4** |

Fecha o ciclo, anda 2 passos (`1 → 2 → 3`), pega `3.next = 4` como nova cabeça, quebra o ciclo em `3.next = null`.

Resultado final: `4 → 5 → 1 → 2 → 3` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para medir o tamanho, uma passada (parcial) para achar a nova cauda
- **Espaço:** O(1) — só ponteiros, a lista é reorganizada in-place

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode rotateRight(ListNode head, int k) {
    if (head == null || head.next == null) return head; // 0 ou 1 nó: rotação não muda nada

    // Mede o tamanho e já deixa 'tail' apontando para o último nó.
    int n = 1;
    ListNode tail = head;
    while (tail.next != null) {
        tail = tail.next;
        n++;
    }

    k %= n; // reduz ao deslocamento EFETIVO: rotacionar n vezes = não rotacionar
    if (k == 0) return head; // nada a fazer

    tail.next = head; // fecha o ciclo temporariamente

    // A nova cauda fica (n - k - 1) passos à frente de head — a matemática que
    // localiza "k posições antes do fim" sem precisar andar para trás.
    int passos = n - k - 1;
    ListNode newTail = head;
    for (int i = 0; i < passos; i++) {
        newTail = newTail.next;
    }

    ListNode newHead = newTail.next;
    newTail.next = null; // quebra o ciclo no lugar certo

    return newHead;
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

- **Não aplicar `k % n` antes de processar**: com `k` até `2 × 10^9`, ignorar essa redução faz qualquer abordagem baseada em "andar k vezes" ficar inviável — é a restrição mais importante deste problema.
- **Esquecer o caso `k % n == 0`**: quando `k` é múltiplo exato do tamanho da lista, a rotação não muda nada — sem esse checkpoint, o código tentaria calcular `passos = n - 0 - 1 = n - 1` e devolveria a mesma lista de qualquer forma, mas por um caminho desnecessário (ainda funciona, mas vale a pena tratar explicitamente por clareza).
- **Não tratar lista vazia ou de 1 nó**: fechar o ciclo (`tail.next = head`) numa lista de 1 nó cria um ciclo que aponta pra si mesmo — funciona matematicamente, mas é mais seguro sair cedo nesses casos triviais.
- **Confundir "posições a partir do fim" com "posições a partir do início"**: a fórmula `n - k - 1` (e não `k - 1` ou `k`) é o que converte "os últimos k nós" em "andar a partir da cabeça" — errar esse sinal inverte a direção da rotação.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head=[], k=5` | `[]` | retorna cedo, `head == null` |
| Um nó | `head=[1], k=100` | `[1]` | rotação de qualquer valor não muda uma lista de 1 elemento |
| `k` múltiplo do tamanho | `head=[1,2,3], k=3` | `[1,2,3]` | `k % n == 0`, lista inalterada |
| `k` maior que o tamanho, exemplo do enunciado | `head=[0,1,2], k=4` | `[2,0,1]` | valida que `k % n` reduz corretamente antes de processar |
| `k = 0` | `head=[1,2,3], k=0` | `[1,2,3]` | menor caso de "sem rotação" |

## 🔗 Conexões

- Problemas irmãos: **[0019] Remove Nth Node From End of List** (mesma ideia de "posição contada a partir do fim", resolvida com dois ponteiros com gap em vez de ciclo temporário), **[0708] Insert into a Sorted Circular Linked List** (trabalha diretamente com listas circulares, sem precisar criar o ciclo manualmente)
- No backend: transformar uma estrutura linear num ciclo temporário para reposicionar um "ponto de corte" é o mesmo raciocínio de **buffers circulares** (ring buffers) usados em filas de mensageria e streaming, onde o "início lógico" dos dados se move sem precisar copiar ou deslocar elementos fisicamente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
