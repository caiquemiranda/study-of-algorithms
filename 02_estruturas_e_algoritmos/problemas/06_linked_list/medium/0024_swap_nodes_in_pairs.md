# [0024] Swap Nodes in Pairs

> 🔗 [LeetCode 24](https://leetcode.com/problems/swap-nodes-in-pairs/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Sentinela` `#Medium`

## 📜 O Problema

Dada uma linked list, troque cada dois nós adjacentes e retorne a nova cabeça. A troca deve ser feita **sem alterar os valores** dos nós — só os próprios nós podem ser reorganizados (só reatribuir ponteiros `next`).

**Exemplos:**
```
Input:  head = [1,2,3,4]
Output: [2,1,4,3]

Input:  head = []
Output: []

Input:  head = [1]
Output: [1]

Input:  head = [1,2,3]
Output: [2,1,3]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 100]` → O(n) é o esperado, uma única passada
- `0 <= Node.val <= 100` → sem risco de overflow
- "sem alterar os valores, só os nós" → proíbe a solução preguiçosa de só trocar `node1.val` com `node2.val` — é preciso religar os ponteiros `next` de verdade, que é o ponto didático do problema

## 🧭 Como reconhecer o padrão

"Reorganize a lista em blocos fixos (aqui, pares), preservando a ordem entre blocos, in-place" é uma variação da **reversão de ponteiros** — em vez de inverter a lista inteira, inverte-se **cada par** isoladamente, um de cada vez, precisando sempre manter uma referência ao nó **antes** do par para religar o bloco anterior ao novo início do par trocado (ver [fundamentos](../../../fundamentos/06_linked_list.md)).

## 🐢 Solução 1 — Força bruta (copiar valores para um array, trocar em pares, reconstruir)

Percorre a lista guardando os valores num array, troca os valores em pares (`array[i]` com `array[i+1]`), e reconstrói uma lista nova a partir do array trocado.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** o tempo já é ótimo, mas usa memória extra e — mais importante — o enunciado proíbe explicitamente resolver só trocando valores; o objetivo didático é praticar a reorganização de ponteiros, não contornar o problema copiando dados.

## 💡 Solução 2 — A ideia otimizada (intuição)

Usa um sentinela (`dummy`) antes de `head`, com um ponteiro `prev` que sempre aponta para o nó **antes** do próximo par a trocar. A cada iteração: identifica os dois nós do par (`primeiro` e `segundo`), reatribui os ponteiros para inverter a ordem deles (`primeiro.next = segundo.next`, `segundo.next = primeiro`), religa `prev.next = segundo` (o par trocado começa agora pelo antigo segundo nó), e avança `prev` para `primeiro` (que agora é o **último** do par já trocado, pronto para religar o próximo par).

## 🎬 Exemplo passo a passo

`head = [1,2,3,4]`

| Iteração | prev (antes) | primeiro | segundo | Ação | Lista após a iteração |
|---|---|---|---|---|---|
| início | — | — | — | — | dummy→1→2→3→4 |
| 1 | dummy | 1 | 2 | `1.next=3`; `2.next=1`; `dummy.next=2`; `prev` vira 1 | dummy→2→1→3→4 |
| 2 | 1 | 3 | 4 | `3.next=null`; `4.next=3`; `1.next=4`; `prev` vira 3 | dummy→2→1→4→3 |
| checagem | 3 | — | — | `prev.next.next` é `null` → não sobra par, loop encerra | dummy→2→1→4→3 |

Resultado final: `2 → 1 → 4 → 3` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado uma única vez, em blocos de 2
- **Espaço:** O(1) na versão iterativa — só ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode swapPairs(ListNode head) {
    ListNode dummy = new ListNode(0, head); // sentinela: cobre a troca do 1º par sem caso especial
    ListNode prev = dummy;

    // Só troca se existir um PAR completo à frente (2 nós); lista ímpar deixa o último nó intocado.
    while (prev.next != null && prev.next.next != null) {
        ListNode primeiro = prev.next;
        ListNode segundo = primeiro.next;

        // A ordem destas 3 linhas importa: salva o resto ANTES de reatribuir,
        // senão a cauda da lista (depois do par) se perde.
        primeiro.next = segundo.next; // primeiro passa a apontar para o que vem DEPOIS do par
        segundo.next = primeiro;      // segundo passa a apontar para primeiro — a troca em si
        prev.next = segundo;          // o bloco anterior agora aponta para o novo início do par

        prev = primeiro; // primeiro é agora o ÚLTIMO do par trocado: vira o "prev" do próximo par
    }

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

- **Só trocar `node.val`**: resolve visualmente o problema, mas viola a restrição explícita "não altere os valores, só os nós" — em entrevista, essa solução é rejeitada mesmo passando nos testes automatizados que só checam a saída.
- **Ordem errada ao reatribuir os ponteiros**: se `segundo.next = primeiro` acontecer antes de salvar `segundo.next` original (`primeiro.next = segundo.next`), a referência ao resto da lista se perde — sempre "salvar o resto antes de sobrescrever" é a regra de ouro da categoria.
- **Esquecer de avançar `prev` para `primeiro` (não para `segundo`)**: depois da troca, `primeiro` é o nó que fica por último no par já processado — é ele que precisa virar o novo `prev`, não `segundo` (que já é a nova cabeça do par).
- **Lista de tamanho ímpar**: a condição `prev.next.next != null` já garante que o último nó sozinho (sem par) é deixado como está, sem tentar trocar algo que não existe.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `[]` | `prev.next` já é `null`, loop nem roda |
| Um nó (ímpar, sem par) | `head = [1]` | `[1]` | `prev.next.next` é `null`, loop nem roda |
| Um par exato | `head = [1,2]` | `[2,1]` | menor caso onde a troca realmente acontece |
| Tamanho ímpar, exemplo do enunciado | `head = [1,2,3]` | `[2,1,3]` | valida que o nó sobrando no fim fica intocado |
| Tamanho par, exemplo do enunciado | `head = [1,2,3,4]` | `[2,1,4,3]` | trace acima, dois pares completos |

## 🔗 Conexões

- Problemas irmãos: **[0025] Reverse Nodes in k-Group** (generaliza este problema para blocos de tamanho `k` em vez de sempre 2), **[0206] Reverse Linked List** (mesma técnica de reatribuição de ponteiros, mas invertendo a lista inteira de uma vez em vez de em pares)
- No backend: reorganizar elementos em blocos fixos preservando a ordem entre blocos aparece em **paginação com reordenação parcial** (trocar pares de itens numa fila de exibição, ex.: A/B testing de posições) e em **processamento de batches** onde pares de registros adjacentes precisam ser reordenados sem realocar a estrutura inteira.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
