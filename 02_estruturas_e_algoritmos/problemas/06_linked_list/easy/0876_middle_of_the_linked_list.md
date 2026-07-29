# [0876] Middle of the Linked List

> 🔗 [LeetCode 876](https://leetcode.com/problems/middle-of-the-linked-list/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#FastSlow` `#Easy`

## 📜 O Problema

Dado o `head` de uma linked list simples, retorne o **nó do meio**. Se houver dois nós do meio (lista de tamanho par), retorne o **segundo** deles.

**Exemplos:**
```
Input:  head = [1,2,3,4,5]
Output: nó de valor 3 (lista [3,4,5] a partir dele)

Input:  head = [1,2,3,4,5,6]
Output: nó de valor 4 (o segundo dos dois nós do meio; lista [4,5,6] a partir dele)
```

**Restrições (e o que elas denunciam):**
- Não há restrição explícita de tamanho no enunciado além de "lista não vazia" implícito nos exemplos, mas o padrão do problema já entrega a assinatura: **achar uma posição relativa sem saber o tamanho de antemão** → pede uma técnica de uma única passada, não duas
- "retorne o **segundo** nó do meio em caso de empate" → é a regra de desempate que decide exatamente onde o `fast` precisa parar de andar; erra-se fácil esse detalhe sem testar o caso par

## 🧭 Como reconhecer o padrão

"Ache o meio da lista" é a assinatura mais direta de **fast & slow (Floyd)** — ver [fundamentos](../../../fundamentos/06_linked_list.md), seção "Fast & Slow". Esta é a forma mais pura da técnica, sem nenhuma outra etapa combinada (diferente de LC 234 ou LC 143, que usam "achar o meio" como um passo dentro de um problema maior).

## 🐢 Solução 1 — Força bruta (duas passadas: contar e depois andar)

Primeira passada: percorre a lista inteira só para contar quantos nós ela tem (`n`). Segunda passada: anda `n / 2` passos a partir de `head` para chegar ao nó do meio.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o tempo assintótico já é O(n), então tecnicamente "basta" em complexidade — mas percorre a lista **duas vezes** quando uma única passada resolve. Em cenários onde a lista é muito grande ou é um stream (não dá para voltar ao início facilmente), isso é uma limitação real, e é exatamente o que o padrão fast & slow evita.

## 💡 Solução 2 — A ideia otimizada (intuição)

Dois ponteiros partem de `head`: `slow` anda 1 passo por vez, `fast` anda 2. Quando `fast` chega ao fim da lista (ou não pode mais andar 2 passos), `slow` terá percorrido exatamente metade da distância — ou seja, estará no meio. Como `fast` anda o dobro, ele "termina" na metade do tempo que `slow` levaria para chegar ao fim sozinho.

A regra de desempate ("segundo nó do meio, em lista par") sai naturalmente da condição de parada `fast != null && fast.next != null`: em lista par, `fast` consegue dar o último passo duplo até `null`, deixando `slow` já avançado um passo a mais do que pararia numa lista ímpar.

## 🎬 Exemplo passo a passo

`head = [1,2,3,4,5,6]` (tamanho par, 6 nós)

| Passo | slow | fast | fast != null && fast.next != null? |
|---|---|---|---|
| início | 1 | 1 | sim |
| 1 | 2 | 3 | sim |
| 2 | 3 | 5 | sim |
| 3 | 4 | null (5.next.next) | não → loop encerra |

Resultado final: `slow` parado no nó de valor `4` ✔ — o **segundo** dos dois nós do meio (3 e 4), como pede o enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada; `fast` percorre no máximo `n` nós
- **Espaço:** O(1) — apenas dois ponteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode middleNode(ListNode head) {
    ListNode slow = head, fast = head;

    // fast anda 2x mais rápido: quando ele não pode mais dar um passo duplo,
    // slow já percorreu exatamente metade do caminho.
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow; // em lista par, essa condição de parada deixa slow no 2º nó do meio
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

- **Esquecer a checagem `fast.next != null`**: checar só `fast != null` permite `fast.next.next` estourar quando `fast` é o último nó de uma lista de tamanho ímpar.
- **Confundir qual dos dois nós do meio retornar em lista par**: o enunciado pede o **segundo**; usar `fast != null` sozinho (sem `&& fast.next != null`) na condição do loop muda o ponto de parada e pode devolver o primeiro por engano — sempre testar com um exemplo par manualmente.
- **Fazer duas passadas quando uma resolve**: não é um erro de corretude, mas é a limitação que este problema existe para ensinar a evitar — em entrevista, vale mencionar por que fast & slow é preferível.
- **Tentar aplicar isso em uma lista circular sem adaptar**: fast & slow para achar o meio assume que a lista **termina** em `null`; numa lista com ciclo, esse loop nunca para (é outro problema — detecção de ciclo, LC 141/142).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó | `head = [1]` | nó de valor 1 | `fast.next` já é `null`, loop nem roda |
| Dois nós | `head = [1,2]` | nó de valor 2 | menor caso par: testa a regra do "segundo nó do meio" |
| Tamanho ímpar | `head = [1,2,3,4,5]` | nó de valor 3 | único nó do meio, sem ambiguidade |
| Tamanho par, exemplo do enunciado | `head = [1,2,3,4,5,6]` | nó de valor 4 | trace acima |
| Lista maior | `head = [1,2,3,4,5,6,7]` | nó de valor 4 | confirma o padrão em tamanho ímpar maior |

## 🔗 Conexões

- Problemas irmãos: **[0234] Palindrome Linked List** (usa "achar o meio" como primeira fase antes de inverter e comparar), **[0143] Reorder List** (mesma primeira fase, seguida de reversão e intercalação), **[0141] Linked List Cycle** (mesmo par de ponteiros fast/slow, mas para detectar ciclo em vez de achar o meio)
- No backend: achar o "ponto médio" de um fluxo de dados sem materializá-lo todo é útil em **particionamento de dados** (dividir uma lista de tarefas ao meio para processamento paralelo) e é a base para o **merge sort de linked list** (LC 148), que precisa quebrar a lista em duas metades repetidamente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
