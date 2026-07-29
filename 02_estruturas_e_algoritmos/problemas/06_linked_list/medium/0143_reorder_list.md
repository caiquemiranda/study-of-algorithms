# [0143] Reorder List

> 🔗 [LeetCode 143](https://leetcode.com/problems/reorder-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#FastSlow` `#ReversaoDePonteiros` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list `L0 → L1 → … → Ln`, reordene-a **in-place** para a forma `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`. Só os nós podem ser reorganizados — os valores não podem ser alterados.

**Exemplos:**
```
Input:  head = [1,2,3,4]
Output: [1,4,2,3]

Input:  head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 5 * 10^4]` → O(n) é o esperado
- `1 <= Node.val <= 1000` → sem risco de overflow
- "só nós podem ser mudados, não valores" → proíbe a solução preguiçosa de copiar valores para um array e reescrever `node.val` na ordem certa; é preciso religar ponteiros de verdade
- O padrão de saída (`L0, Ln, L1, Ln-1, ...`) → é literalmente "intercalar a primeira metade com a segunda metade **invertida**" — a restrição em si já denuncia a estrutura da solução

## 🧭 Como reconhecer o padrão

"Alterne entre o início e o fim da lista" combina, em sequência, **três técnicas já vistas** da categoria (ver [fundamentos](../../../fundamentos/06_linked_list.md)): fast & slow para achar o meio, reversão de ponteiros para inverter a segunda metade, e um merge intercalado (como em Merge Two Sorted Lists, mas alternando de fonte a cada nó em vez de comparar valores).

## 🐢 Solução 1 — Força bruta (copiar nós para um array, reconstruir por índices)

Percorre a lista guardando os **nós** (não os valores) num array, na ordem original. Depois, percorre o array com dois índices — `i=0` e `j=n-1` — religando `next` alternadamente: `array[0].next = array[n-1]`, `array[n-1].next = array[1]`, `array[1].next = array[n-2]`, e assim por diante, até os índices se cruzarem.

- Tempo: O(n) · Espaço: O(n) para o array de nós
- **Por que não basta:** o tempo já é ótimo, mas guardar todos os nós num array gasta memória proporcional a `n` — a lista já tem tudo que é preciso para achar "o meio" e "o fim" sem essa cópia, usando fast & slow e reversão em vez de indexação.

## 💡 Solução 2 — A ideia otimizada (intuição)

Três fases, cada uma reaproveitando uma técnica já conhecida da categoria:
1. **Achar o meio** com fast & slow — o mesmo padrão do LC 876.
2. **Cortar** a lista em duas metades ali, e **inverter** a segunda metade — o mesmo padrão do LC 206.
3. **Intercalar** as duas metades nó a nó (1º da primeira, 1º da segunda-invertida, 2º da primeira, 2º da segunda-invertida, ...) — como o "1º da segunda-invertida" é sempre o **último nó original** da lista, essa intercalação produz exatamente `L0, Ln, L1, Ln-1, ...`.

## 🎬 Exemplo passo a passo

`head = [1,2,3,4]`

**Fase 1 — achar o meio:** fast & slow param em `slow = 3` (nó de valor 3).

**Fase 2 — cortar e inverter a segunda metade:**

| Etapa | Primeira metade | Segunda metade (antes de inverter) | Segunda metade (invertida) |
|---|---|---|---|
| resultado | `1 → 2 → 3 → null` | `4 → null` | `4 → null` (1 nó só, inversão não muda nada) |

**Fase 3 — intercalar** (`first` anda em `1→2→3`, `second` anda em `4`):

| Passo | first (antes) | second (antes) | Ação | Lista construída até aqui |
|---|---|---|---|---|
| 1 | 1 | 4 | `1.next = 4`; `4.next = 2` (o antigo `first.next`) | 1 → 4 → 2 → 3 |
| fim | 2 | null | `second` esgotou, loop encerra; `2.next = 3` permanece intocado (era o resto da 1ª metade) | 1 → 4 → 2 → 3 |

Resultado final: `1 → 4 → 2 → 3` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — as três fases são, cada uma, no máximo uma passada completa pela lista
- **Espaço:** O(1) — só ponteiros; nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public void reorderList(ListNode head) {
    if (head == null || head.next == null) return;

    // Fase 1: acha o fim da 1ª metade (fast & slow) — o mesmo padrão do LC 876.
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Fase 2: corta ali e inverte a 2ª metade — o mesmo padrão do LC 206.
    ListNode second = slow.next;
    slow.next = null; // a 1ª metade agora termina oficialmente aqui
    ListNode prev = null;
    while (second != null) {
        ListNode nxt = second.next;
        second.next = prev;
        prev = second;
        second = nxt;
    }
    second = prev; // cabeça da 2ª metade, já invertida

    // Fase 3: intercala as duas metades. A 1ª metade pode ter 1 nó a mais que a 2ª
    // (lista de tamanho ímpar) — quando 'second' esgota, o que sobra da 1ª metade
    // já está corretamente ligado (não precisa de tratamento extra).
    ListNode first = head;
    while (second != null) {
        ListNode firstNext = first.next;
        ListNode secondNext = second.next;

        first.next = second;
        if (firstNext != null) {
            second.next = firstNext;
        }

        first = firstNext;
        second = secondNext;
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

- **Esquecer `slow.next = null` ao cortar**: sem isso, a "primeira metade" continua fisicamente ligada à segunda, e a fase de reversão acaba invertendo a lista inteira em vez de só a segunda metade.
- **Não checar `firstNext != null` na fase 3**: quando a primeira metade tem 1 nó a mais (lista de tamanho par vs. ímpar dependendo de onde `slow` parou), o último `first` pode não ter próximo — sem a checagem, `second.next = firstNext` sobrescreve com `null` incorretamente ou o acesso falha.
- **Inverter a metade errada**: é a **segunda** metade que precisa ser invertida (para que seus nós apareçam do fim para o meio, na ordem `Ln, Ln-1, ...`) — inverter a primeira produz a ordem errada.
- **Confundir com "palíndromo" (LC 234)**: aqui as duas metades são **religadas** numa lista só, alternando; lá elas são apenas **comparadas**, sem alterar a estrutura — a fase 1 e 2 são idênticas, só a fase 3 muda.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó | `head = [1]` | `[1]` | `head.next == null`, retorna cedo |
| Dois nós | `head = [1,2]` | `[1,2]` | menor caso onde a intercalação não muda nada visualmente (L0, L1 já é a ordem) |
| Tamanho par, exemplo do enunciado | `head = [1,2,3,4]` | `[1,4,2,3]` | trace acima |
| Tamanho ímpar, exemplo do enunciado | `head = [1,2,3,4,5]` | `[1,5,2,4,3]` | valida o caso onde a 1ª metade tem 1 nó a mais que a 2ª |
| Três nós | `head = [1,2,3]` | `[1,3,2]` | menor caso ímpar não trivial |

## 🔗 Conexões

- Problemas irmãos: **[0876] Middle of the Linked List** (a fase 1 isolada), **[0206] Reverse Linked List** (a fase 2 isolada), **[0021] Merge Two Sorted Lists** (mesma estrutura de "intercalar duas listas nó a nó", mas comparando valores em vez de alternar por posição)
- No backend: combinar três sub-rotinas simples (achar posição, inverter trecho, intercalar) para produzir um rearranjo específico é o mesmo raciocínio usado em **algoritmos de embaralhamento estruturado** (ex.: riffle shuffle de baralhos, que intercala duas metades) e em **layout de dados para acesso alternado** (round-robin entre duas fontes de dados já particionadas).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
