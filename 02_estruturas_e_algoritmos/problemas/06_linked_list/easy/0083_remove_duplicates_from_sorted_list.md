# [0083] Remove Duplicates from Sorted List

> 🔗 [LeetCode 83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#DoisPonteiros` `#Easy`

## 📜 O Problema

Dado o `head` de uma linked list **ordenada**, remova os nós duplicados de forma que cada valor apareça só uma vez. Retorne a lista, que continua ordenada.

**Exemplos:**
```
Input:  head = [1,1,2]
Output: [1,2]

Input:  head = [1,1,2,3,3]
Output: [1,2,3]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 300]` → entrada pequena, mas a solução esperada continua sendo O(n): não há motivo para ser mais lento, já que a lista está ordenada
- `-100 <= Node.val <= 100` → valores cabem em `int` sem risco de overflow
- "a lista está garantidamente ordenada" → **essa é a informação-chave**: duplicatas de um mesmo valor ficam sempre **lado a lado**, então basta comparar cada nó com o seguinte, nunca é preciso um `Set` para lembrar valores distantes

## 🧭 Como reconhecer o padrão

Lista **ordenada** + "remova duplicatas" é diferente de "remova duplicatas" num array qualquer: como os iguais são sempre vizinhos, um único ponteiro andando e comparando `atual.val` com `atual.next.val` resolve. Não é fast & slow nem reversão — é o padrão mais simples da categoria: **um ponteiro decide se pula ou avança**.

## 🐢 Solução 1 — Força bruta (hash set de valores vistos)

Percorre a lista guardando cada valor num `HashSet`. Para cada nó, se o valor já apareceu antes, remove o nó da lista (religando o `next` do anterior); senão, avança normalmente.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** funciona, mas gasta memória extra para resolver algo que a ordenação da lista já entrega de graça — como duplicatas são sempre adjacentes, não é preciso lembrar valores "de longe".

## 💡 Solução 2 — A ideia otimizada (intuição)

Como a lista está ordenada, todo valor repetido aparece em nós **consecutivos**. Basta manter um ponteiro `cur` e, enquanto `cur.next` tiver o mesmo valor que `cur`, "pular" esse próximo nó ligando `cur.next` direto ao nó seguinte a ele. Só avança `cur` quando o valor à frente for diferente.

## 🎬 Exemplo passo a passo

`head = [1,1,2,3,3]`

| Passo | cur | cur.next.val == cur.val? | Ação | Lista após o passo |
|---|---|---|---|---|
| 1 | 1 (1º) | 1 == 1 → sim | pula o 2º nó (`cur.next = cur.next.next`) | 1 → 2 → 3 → 3 |
| 2 | 1 (1º) | 2 == 1 → não | avança `cur` | 1 → 2 → 3 → 3 |
| 3 | 2 | 3 == 2 → não | avança `cur` | 1 → 2 → 3 → 3 |
| 4 | 3 (1º) | 3 == 3 → sim | pula o 2º nó de valor 3 | 1 → 2 → 3 |
| 5 | 3 | `cur.next == null` | loop termina | 1 → 2 → 3 |

Resultado final: `1 → 2 → 3` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada; cada nó é visitado (e possivelmente pulado) uma vez
- **Espaço:** O(1) — só um ponteiro extra, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode deleteDuplicates(ListNode head) {
    ListNode cur = head;

    while (cur != null && cur.next != null) {
        if (cur.val == cur.next.val) {
            // Mesmo valor à frente: "pula" o próximo nó religando o ponteiro.
            // Não precisa avançar cur aqui — pode haver uma 3ª, 4ª repetição do mesmo valor.
            cur.next = cur.next.next;
        } else {
            // Valor diferente: só agora é seguro avançar, o bloco de repetidos acabou.
            cur = cur.next;
        }
    }

    return head; // a cabeça nunca muda neste problema (o 1º nó nunca é removido)
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

- **Avançar `cur` mesmo quando encontra uma duplicata**: se `cur = cur.next` acontecer também no ramo de "pular", uma sequência com 3+ repetições do mesmo valor (ex.: `[1,1,1,2]`) deixa uma cópia extra passar despercebida.
- **Esquecer a checagem `cur.next != null`**: sem ela, `cur.next.val` explode com `NullPointerException` quando `cur` é o último nó da lista.
- **Confundir com o irmão LC 82**: aqui a regra é "cada valor aparece uma vez" (mantém um representante); no 82 a regra é "remova TODOS os nós que tiveram duplicata" (não sobra nenhum representante) — soluções parecidas, resultados diferentes.
- **Tentar usar `head.val` como referência fixa**: a comparação certa é sempre `cur` com `cur.next`, não com o valor do nó anterior guardado à parte — isso complica sem necessidade.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `[]` | `cur` já é `null`, loop nem roda |
| Um nó | `head = [1]` | `[1]` | `cur.next` é `null` de cara, sem duplicata possível |
| Sem duplicatas | `head = [1,2,3]` | `[1,2,3]` | nenhuma condição de pular é acionada |
| Todos iguais | `head = [7,7,7,7]` | `[7]` | testa múltiplas repetições seguidas do mesmo valor |
| Duplicata só na cauda | `head = [1,2,3,3]` | `[1,2,3]` | garante que o pulo funciona até o fim da lista |

## 🔗 Conexões

- Problemas irmãos: **[0082] Remove Duplicates from Sorted List II** (remove os representantes também, não só os extras), **[0026] Remove Duplicates from Sorted Array** (mesma ideia, mas em array com dois ponteiros in-place)
- No backend: deduplicação de registros já ordenados (por chave de índice, por timestamp) é exatamente este padrão — usado em merges de logs ordenados e em passes de compactação de séries temporais onde só o valor mais recente por chave interessa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
