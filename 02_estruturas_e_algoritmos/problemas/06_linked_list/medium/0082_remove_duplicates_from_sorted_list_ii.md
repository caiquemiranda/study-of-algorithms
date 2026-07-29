# [0082] Remove Duplicates from Sorted List II

> 🔗 [LeetCode 82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Sentinela` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list **ordenada**, remova **todos os nós que têm valor duplicado**, deixando na lista apenas os números que aparecem exatamente uma vez no original. Retorne a lista, que continua ordenada.

**Exemplos:**
```
Input:  head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Input:  head = [1,1,1,2,3]
Output: [2,3]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 300]` → O(n) é o esperado, uma única passada
- `-100 <= Node.val <= 100` → sem risco de overflow
- "a lista está garantidamente ordenada" → duplicatas ficam sempre adjacentes; e diferente do LC 83 (que mantém 1 representante), aqui **nenhum** representante de um valor duplicado sobrevive — é preciso reconhecer o **bloco inteiro** de repetições antes de decidir removê-lo

## 🧭 Como reconhecer o padrão

Como no LC 83, a ordenação garante que duplicatas são vizinhas. A diferença que muda tudo: aqui a decisão "remover ou manter" só pode ser tomada depois de **olhar o bloco inteiro** de valores iguais — não dá para decidir nó a nó. Isso exige um sentinela (a própria `head` pode ser removida, como no 2º exemplo) e um ponteiro `prev` que só avança quando um nó sobrevive intacto (ver [fundamentos](../../../fundamentos/06_linked_list.md), padrão do nó sentinela).

## 🐢 Solução 1 — Força bruta (contar ocorrências, depois filtrar)

Primeira passada: percorre a lista guardando num `HashMap` a contagem de cada valor. Segunda passada: reconstrói a lista incluindo só os nós cujo valor aparece exatamente uma vez no mapa.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** o tempo já é ótimo, mas gasta memória proporcional ao número de valores distintos — como a lista está ordenada, dá para decidir "esse valor é duplicado?" olhando só os vizinhos imediatos, numa única passada, sem precisar de um mapa de contagem global.

## 💡 Solução 2 — A ideia otimizada (intuição)

Sentinela (`dummy`) antes de `head`, com `prev` apontando sempre para o último nó **confirmado como sobrevivente**, e `cur` percorrendo a lista. Para cada `cur`: se `cur.val == cur.next.val`, existe um bloco de duplicatas — anda `cur` até o **último** nó desse valor (consumindo o bloco inteiro), depois religa `prev.next = cur.next`, pulando o bloco todo de uma vez. Se `cur.val != cur.next.val` (ou `cur` é o último nó), esse nó é único no seu valor — `prev` avança para `cur`, confirmando-o como sobrevivente.

## 🎬 Exemplo passo a passo

`head = [1,2,3,3,4,4,5]`

| Passo | prev | cur | Situação | Ação |
|---|---|---|---|---|
| início | dummy | 1 | `cur.next=2`, diferente | `prev` avança para 1 |
| 1 | 1 | 2 | `cur.next=3`, diferente | `prev` avança para 2 |
| 2 | 2 | 3 (1º) | `cur.val == cur.next.val` (3==3) | anda `cur` até o último 3; `prev.next = 4` (pula os dois 3) |
| 3 | 2 | 4 (1º) | `cur.val == cur.next.val` (4==4) | anda `cur` até o último 4; `prev.next = 5` (pula os dois 4) |
| 4 | 2 | 5 | `cur.next = null`, sem duplicata | `prev` avança para 5 |
| fim | 5 | null | — | loop encerra |

Resultado final: `1 → 2 → 5` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado uma única vez (seja para confirmar como sobrevivente, seja para ser consumido dentro de um bloco de duplicatas)
- **Espaço:** O(1) — sentinela e dois ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode deleteDuplicates(ListNode head) {
    ListNode dummy = new ListNode(0, head); // sentinela: a própria head pode ser removida (2º exemplo)
    ListNode prev = dummy, cur = head;

    while (cur != null) {
        if (cur.next != null && cur.val == cur.next.val) {
            int valorRepetido = cur.val;
            // Consome o BLOCO inteiro de duplicatas — não decide nada até saber onde ele termina.
            while (cur.next != null && cur.next.val == valorRepetido) {
                cur = cur.next;
            }
            prev.next = cur.next; // pula o bloco inteiro de uma vez; prev NÃO avança (não sobreviveu)
            cur = cur.next;
        } else {
            prev = cur;   // cur é único no seu valor: confirma como sobrevivente
            cur = cur.next;
        }
    }

    return dummy.next; // a nova cabeça pode ser diferente da original
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

- **Avançar `prev` para dentro do bloco de duplicatas**: se `prev` for atualizado para qualquer nó do bloco removido, o ponteiro final fica apontando para um nó desconectado da lista — `prev` só pode avançar para nós que **sobrevivem** intactos.
- **Confundir com o LC 83**: lá mantém-se 1 representante por valor; aqui **nenhum** sobrevive se houve duplicata — reaproveitar a lógica do 83 sem ajustar remove só os "extras" e deixa representantes indevidos na lista.
- **Não usar sentinela**: a própria `head` pode fazer parte de um bloco de duplicatas removido (ex.: `[1,1,1,2,3]` → a nova cabeça é `2`) — sem `dummy`, decidir a nova cabeça exige tratamento especial.
- **Esquecer a checagem `cur.next != null` antes de comparar valores**: sem ela, `cur.next.val` explode com `NullPointerException` quando `cur` é o último nó da lista.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `[]` | `cur` já é `null`, loop nem roda |
| Sem duplicatas | `head = [1,2,3]` | `[1,2,3]` | nenhum bloco de duplicata é encontrado |
| Todos duplicados | `head = [1,1,1,1]` | `[]` | o bloco inteiro é removido, inclusive a head |
| Duplicata na cabeça, exemplo do enunciado | `head = [1,1,1,2,3]` | `[2,3]` | valida que o sentinela cobre a remoção da própria head |
| Duplicata no meio, exemplo do enunciado | `head = [1,2,3,3,4,4,5]` | `[1,2,5]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0083] Remove Duplicates from Sorted List** (mantém 1 representante por valor, em vez de remover o bloco inteiro), **[0026] Remove Duplicates from Sorted Array** (mesma ideia de "duplicata sempre adjacente", mas em array com dois ponteiros in-place)
- No backend: remover **todos** os registros que colidem por chave (em vez de manter um) é o padrão usado em **deduplicação estrita de eventos** (ex.: descartar completamente qualquer grupo de eventos que chegou duplicado, por suspeita de reprocessamento indevido) e em **detecção de conflitos** em sistemas de sincronização, onde uma chave que aparece mais de uma vez é tratada como inválida em vez de resolvida automaticamente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
