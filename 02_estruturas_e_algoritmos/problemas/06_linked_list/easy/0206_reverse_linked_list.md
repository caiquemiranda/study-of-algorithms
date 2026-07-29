# [0206] Reverse Linked List

> 🔗 [LeetCode 206](https://leetcode.com/problems/reverse-linked-list/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#ReversaoDePonteiros` `#Easy`

## 📜 O Problema

Dado o `head` de uma linked list simples, inverta a lista e retorne a nova cabeça (o antigo último nó).

**Exemplos:**
```
Input:  head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input:  head = [1,2]
Output: [2,1]

Input:  head = []
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 5000]` → O(n) é o esperado, uma passada resolve
- `-5000 <= Node.val <= 5000` → valores cabem em `int`, sem risco de overflow
- Follow-up "implemente tanto iterativo quanto recursivo" → sinaliza que ambas as formas são didaticamente relevantes, mas que a recursiva paga um custo de pilha O(n) que a iterativa não paga

## 🧭 Como reconhecer o padrão

"Inverta a lista" é a assinatura mais direta de **reversão de ponteiros**, a técnica mais fundamental da categoria (ver [fundamentos](../../../fundamentos/06_linked_list.md)). Praticamente todo problema de "reordene/inverta parte de uma lista, in-place, O(1) espaço" usa esta ideia como bloco de construção — inclusive o próprio walkthrough dos fundamentos usa exatamente este problema como exemplo.

## 🐢 Solução 1 — Força bruta (copiar valores para um array, reconstruir invertido)

Percorre a lista original guardando os valores num array, depois cria uma lista nova lendo o array de trás para frente.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** o tempo já é ótimo, mas gasta memória proporcional ao tamanho da lista para algo que dá para fazer só reorganizando os ponteiros já existentes, sem alocar nada novo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Cada nó tem um único ponteiro `next`; inverter a lista é literalmente inverter a direção de cada seta. Para isso sem perder o resto da lista, precisamos de três referências andando juntas: `prev` (o que já foi invertido), `head` (o nó atual) e `nxt` (o que falta processar, salvo **antes** de sobrescrever `head.next`). A cada passo: guarda o resto (`nxt = head.next`), inverte a seta do nó atual (`head.next = prev`), e avança os dois ponteiros (`prev = head`, `head = nxt`).

## 🎬 Exemplo passo a passo

`head = [1,2,3]`

| Iteração | prev | head | nxt | Ação |
|---|---|---|---|---|
| início | null | 1 | — | — |
| 1 | 1 | 2 | 2 | `1.next = null` (1 vira cauda) |
| 2 | 2 | 3 | 3 | `2.next = 1` |
| 3 | 3 | null | null | `3.next = 2` — loop encerra |

Resultado final: `prev = 3` → lista `3 → 2 → 1 → null` ✔ — bate com o esperado (padrão análogo ao do enunciado, que usa `[1,2,3,4,5] → [5,4,3,2,1]`).

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado e tem seu ponteiro invertido exatamente uma vez
- **Espaço:** O(1) na versão iterativa (só três referências) · **O(n) de pilha** na versão recursiva

## 💻 Implementações

### Java (referência completa e comentada)
```java
// Versão iterativa — a preferida em produção: O(1) de espaço, sem risco de estouro de pilha.
public ListNode reverseList(ListNode head) {
    ListNode prev = null;               // atrás de tudo: será a nova cabeça no fim
    while (head != null) {
        ListNode nxt = head.next;       // guarda o resto ANTES de sobrescrever — senão a lista se perde
        head.next = prev;               // a seta vira para trás: é a reversão em si
        prev = head;                    // prev avança
        head = nxt;                     // head avança pelo caminho salvo
    }
    return prev;                        // head virou null; prev parou no último nó (nova cabeça)
}

// Versão recursiva — didaticamente elegante, mas gasta O(n) de pilha (ver Pegadinhas).
public ListNode reverseListRecursive(ListNode head) {
    if (head == null || head.next == null) {
        return head; // caso base: lista vazia ou de 1 nó já está "invertida"
    }
    ListNode novaCabeca = reverseListRecursive(head.next); // inverte o resto primeiro
    head.next.next = head;  // o nó seguinte passa a apontar de volta para este
    head.next = null;       // este nó vira a nova cauda
    return novaCabeca;      // a cabeça encontrada lá no fundo da recursão sobe intacta
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

- **Sobrescrever `head.next` antes de salvar `nxt`**: sem guardar o resto da lista primeiro, o restante vira lixo inalcançável — é o erro nº 1 deste problema.
- **Esquecer de setar `head.next = null` na primeira iteração**: o antigo primeiro nó precisa virar a nova cauda; se `prev` não começar em `null`, o "fim" da lista invertida nunca é marcado.
- **Na versão recursiva, esquecer `head.next = null`**: sem essa linha, a lista fica com um ciclo (o antigo próximo nó aponta de volta para este, mas este ainda aponta para a frente também).
- **Usar a versão recursiva sem medir o custo**: para `n` até 5000 (o limite deste problema) a pilha aguenta, mas em listas de dezenas de milhares de nós a recursão estoura — prefira sempre a iterativa quando espaço importa.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `[]` | `head` já é `null`, o `while`/`if` base retorna direto |
| Um nó | `head = [1]` | `[1]` | não há nada para inverter; `prev` vira o próprio nó na 1ª iteração |
| Dois nós | `head = [1,2]` | `[2,1]` | menor caso onde a reversão realmente rearranja algo |
| Lista maior, exemplo do enunciado | `head = [1,2,3,4,5]` | `[5,4,3,2,1]` | trace acima, generalizado |
| Valores negativos | `head = [-1,-2,-3]` | `[-3,-2,-1]` | garante que a lógica não depende do sinal do valor |

## 🔗 Conexões

- Problemas irmãos: **[0092] Reverse Linked List II** (inverte só um trecho `[left, right]` da lista, mesma técnica com dois pontos de emenda extras), **[0025] Reverse Nodes in k-Group** (inverte em blocos de tamanho k), **[0143] Reorder List** (usa reversão de metade da lista como uma das três etapas)
- No backend: reversão de ponteiros aparece em **undo logs / WAL** (percorrer o histórico de trás para frente), em **pilhas de chamadas de replay de eventos**, e é a base conceitual para inverter a ordem de exibição de uma **timeline** (feed de eventos mais recentes primeiro) quando os dados chegam encadeados em ordem cronológica.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
