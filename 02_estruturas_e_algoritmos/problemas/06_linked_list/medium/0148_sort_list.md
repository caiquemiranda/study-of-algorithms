# [0148] Sort List

> 🔗 [LeetCode 148](https://leetcode.com/problems/sort-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#FastSlow` `#DivideAndConquer` `#MergeSort` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list, retorne-a ordenada em ordem **crescente**.

**Exemplos:**
```
Input:  head = [4,2,1,3]
Output: [1,2,3,4]

Input:  head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Input:  head = []
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 5 * 10^4]` → com até 50 mil nós, O(n²) (como o insertion sort do LC 147) é claramente lento demais; o próprio limite já empurra para O(n log n)
- `-10^5 <= Node.val <= 10^5` → sem risco de overflow
- Follow-up "O(n log n) tempo **e** O(1) memória (espaço constante)" → é a meta mais ambiciosa: entre os algoritmos O(n log n) clássicos, quicksort não garante O(n log n) no pior caso e heapsort não se adapta bem a listas encadeadas — **merge sort** é o que sobra, e numa linked list ele pode ser feito sem o array auxiliar O(n) que precisaria num array comum

## 🧭 Como reconhecer o padrão

"Ordene uma linked list em O(n log n)" é a assinatura de **merge sort aplicado a listas encadeadas**: divide a lista ao meio (fast & slow, o mesmo padrão do LC 876), ordena cada metade recursivamente, e junta as duas metades ordenadas (o mesmo merge do LC 21). É a combinação de três técnicas já vistas na categoria (ver [fundamentos](../../../fundamentos/06_linked_list.md)), aplicadas em conjunto para um objetivo de ordenação.

## 🐢 Solução 1 — Força bruta (copiar para um array, ordenar, reconstruir)

Percorre a lista copiando os valores para um array, ordena o array com o algoritmo de ordenação padrão da linguagem (ex.: `Collections.sort`, O(n log n)), e reconstrói a lista a partir do array ordenado.

- Tempo: O(n log n) · Espaço: O(n) para o array
- **Por que não basta:** o tempo já bate a meta do follow-up, mas o espaço não — copiar todos os valores para um array gasta O(n) de memória extra, quando o follow-up pede O(1). A alternativa é fazer o merge sort **diretamente sobre os nós da lista**, sem nunca materializar um array.

## 💡 Solução 2 — A ideia otimizada (intuição)

**Merge sort recursivo sobre a lista**: 
1. **Caso base**: lista vazia ou de 1 nó já está ordenada.
2. **Divide**: acha o meio com fast & slow (guardando o nó **anterior** ao meio, `prev`, para poder cortar a lista ali com `prev.next = null`) — produz duas sublistas independentes.
3. **Conquista**: chama a mesma função recursivamente em cada metade.
4. **Combina**: junta as duas metades já ordenadas com o merge clássico de duas listas ordenadas (LC 21).

## 🎬 Exemplo passo a passo

`head = [4,2,1,3]`

**Fase de divisão (top-down):**

| Nível | Sublista | Ponto de corte | Metade esquerda | Metade direita |
|---|---|---|---|---|
| 0 | 4 → 2 → 1 → 3 | após o 2º nó | 4 → 2 | 1 → 3 |
| 1 (esq.) | 4 → 2 | após o 1º nó | 4 | 2 |
| 1 (dir.) | 1 → 3 | após o 1º nó | 1 | 3 |

**Fase de combinação (bottom-up):**

| Merge | Entradas | Resultado |
|---|---|---|
| nível 1 (esq.) | `4` e `2` | `2 → 4` |
| nível 1 (dir.) | `1` e `3` | `1 → 3` |
| nível 0 | `2 → 4` e `1 → 3` | `1 → 2 → 3 → 4` |

Resultado final: `1 → 2 → 3 → 4` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — O(log n) níveis de divisão, e cada nível processa o total de `n` nós no merge, igual ao merge sort tradicional
- **Espaço:** O(log n) — pilha de recursão (proporcional ao número de níveis); a versão totalmente O(1) exige uma variante **iterativa bottom-up** (mais complexa, ver Pegadinhas), que evita a pilha de recursão por completo

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode sortList(ListNode head) {
    if (head == null || head.next == null) return head; // caso base: 0 ou 1 nó já está ordenado

    // Divide: acha o meio com fast & slow, guardando 'prev' (o nó ANTES do meio)
    // para poder cortar a lista em duas sublistas independentes.
    ListNode prev = null, slow = head, fast = head;
    while (fast != null && fast.next != null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    prev.next = null; // corta: 'head' agora é só a 1ª metade; 'slow' é o início da 2ª

    // Conquista: ordena cada metade recursivamente.
    ListNode left = sortList(head);
    ListNode right = sortList(slow);

    // Combina: merge de duas listas já ordenadas — mesma lógica do LC 21.
    return merge(left, right);
}

private ListNode merge(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0);
    ListNode cur = dummy;
    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) { cur.next = l1; l1 = l1.next; }
        else                  { cur.next = l2; l2 = l2.next; }
        cur = cur.next;
    }
    cur.next = (l1 != null) ? l1 : l2; // emenda o restante da lista mais longa
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

- **Esquecer de cortar a lista (`prev.next = null`)**: sem isso, as duas "metades" continuam fisicamente ligadas, e a recursão da esquerda acaba processando a lista inteira de novo (loop infinito de divisão ou resultado incorreto).
- **Usar o `slow` do padrão "meio para LC 876" sem rastrear `prev`**: aquele padrão devolve o nó do meio, mas não o nó **anterior** a ele — sem `prev`, não há como cortar a lista em duas partes sem uma passada extra.
- **Confundir com o LC 147 (Insertion Sort List)**: aqui a meta é O(n log n); usar insertion sort resolve corretamente, mas é O(n²) e não atende ao follow-up deste problema.
- **Achar que a versão recursiva já é O(1) de espaço**: ela é O(log n) por causa da pilha de recursão — a versão verdadeiramente O(1) precisa ser **iterativa bottom-up** (mescla sublistas de tamanho 1, depois 2, depois 4, dobrando a cada rodada, sem nunca recursar), uma técnica bem mais elaborada, geralmente reservada para quando o espaço é uma restrição real de produção.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `[]` | caso base, retorna direto |
| Um nó | `head = [1]` | `[1]` | caso base, já ordenado |
| Já ordenada | `head = [1,2,3]` | `[1,2,3]` | valida que o merge sort não corrompe uma entrada já ordenada |
| Ordem decrescente | `head = [3,2,1]` | `[1,2,3]` | pior caso relativo, mas ainda O(n log n) (merge sort não degrada como insertion sort) |
| Exemplo maior do enunciado | `head = [-1,5,3,4,0]` | `[-1,0,3,4,5]` | valida negativos e um caso com 5 nós (divisão desigual) |

## 🔗 Conexões

- Problemas irmãos: **[0021] Merge Two Sorted Lists** (a sub-rotina de merge usada aqui), **[0876] Middle of the Linked List** (a sub-rotina de achar o meio, adaptada para também rastrear o nó anterior), **[0147] Insertion Sort List** (mesmo objetivo de ordenar, mas O(n²) — a diferença de abordagem quando o volume de dados exige uma complexidade melhor)
- No backend: merge sort sobre estruturas encadeadas é a base do **external sort** — ordenar arquivos maiores que a memória disponível, dividindo em blocos que cabem em memória, ordenando cada um e fazendo merge sequencial dos resultados em disco. É também o algoritmo por trás de operações de `ORDER BY` em bancos de dados quando o conjunto de dados não cabe inteiro em memória.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
