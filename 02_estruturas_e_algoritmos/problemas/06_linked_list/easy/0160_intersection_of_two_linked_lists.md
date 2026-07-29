# [0160] Intersection of Two Linked Lists

> 🔗 [LeetCode 160](https://leetcode.com/problems/intersection-of-two-linked-lists/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#DoisPonteiros` `#Easy`

## 📜 O Problema

Dadas as cabeças de duas linked lists `headA` e `headB`, retorne **o nó** onde as duas listas se intersectam (o mesmo nó em memória, referenciado por ambas a partir de algum ponto). Se não houver interseção, retorne `null`. As listas não têm ciclos, e devem manter a estrutura original depois da função rodar.

**Exemplos:**
```
Input:  listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: nó de valor 8 (a partir dali, as duas listas compartilham os mesmos nós)

Input:  listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: nó de valor 2

Input:  listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null (sem interseção)
```

**Restrições (e o que elas denunciam):**
- `1 <= m, n <= 3 * 10^4` → O(n) é o esperado; nada de O(m·n) comparando cada nó de A com cada nó de B
- `1 <= Node.val <= 10^5` → valores podem se repetir entre as duas listas, então a resposta **não pode** ser decidida comparando `val` — precisa ser o mesmo nó em memória (mesma referência)
- Follow-up "O(m+n) tempo e O(1) espaço" → descarta guardar nós de uma lista num `HashSet` como solução final; empurra para o truque dos dois ponteiros que trocam de lista

## 🧭 Como reconhecer o padrão

Duas listas de tamanhos possivelmente diferentes que "se juntam" em algum ponto é um caso de **dois ponteiros com truque de alinhamento** — variação do padrão de ponteiros da categoria (ver [fundamentos](../../../fundamentos/06_linked_list.md)). A comparação precisa ser sempre por **identidade de nó**, nunca por valor.

## 🐢 Solução 1 — Força bruta (hash set de nós de uma das listas)

Percorre `listA` guardando cada nó (referência) num `HashSet`. Depois percorre `listB`; o primeiro nó de `listB` que já está no set é a interseção.

- Tempo: O(m + n) · Espaço: O(m)
- **Por que não basta:** o tempo já é ótimo, mas o espaço não — o follow-up pede explicitamente O(1) de memória, e existe uma forma de fazer isso sem estrutura auxiliar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se as listas se intersectam, a partir do ponto de interseção elas compartilham exatamente os mesmos nós até o fim — só a parte "antes" da interseção pode ter tamanhos diferentes (`skipA` vs `skipB`).

O truque: usa dois ponteiros, `pA` começando em `headA` e `pB` começando em `headB`. Cada um anda 1 passo por vez; quando um chega ao fim (`null`), ele é redirecionado para a **cabeça da outra lista**. Como `pA` percorre `A + B` nós no total (até o encontro) e `pB` percorre `B + A`, os dois percorrem exatamente a mesma distância total — isso automaticamente **compensa a diferença de tamanho** entre as listas, e eles chegam juntos ao ponto de interseção (ou a `null` ao mesmo tempo, se não houver interseção).

## 🎬 Exemplo passo a passo

`listA = [4,1,8,4,5]` (skipA=2), `listB = [5,6,1,8,4,5]` (skipB=3) — interseção a partir do nó de valor 8

| Passo | pA | pB | pA == pB? |
|---|---|---|---|
| início | 4 (A) | 5 (B) | não |
| 1 | 1 (A) | 6 (B) | não |
| 2 | 8 (A) ← interseção | 1 (B) | não |
| 3 | 4 (A) | 8 (B) ← interseção | não |
| 4 | 5 (A) | 4 (B) | não |
| 5 | null → pula p/ headB | 5 (B) | não |
| 6 | 5 (B) | null → pula p/ headA | não |
| 7 | 6 (B) | 4 (A) | não |
| 8 | 1 (B) | 1 (A) | não |
| 9 | 8 (B) | 8 (A) | **sim** → interseção em nó de valor 8 |

Resultado final: nó de valor `8` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(m + n) — no pior caso cada ponteiro percorre as duas listas inteiras uma vez
- **Espaço:** O(1) — apenas dois ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    if (headA == null || headB == null) return null;

    ListNode pA = headA, pB = headB;

    // Quando um ponteiro chega ao fim, ele "pula" para a cabeça da OUTRA lista.
    // Isso faz os dois percorrerem a mesma distância total (m+n), compensando
    // a diferença de tamanho entre as listas automaticamente.
    while (pA != pB) {
        pA = (pA == null) ? headB : pA.next;
        pB = (pB == null) ? headA : pB.next;
    }

    // Se há interseção, pA == pB é o nó de encontro.
    // Se não há, os dois viram null ao mesmo tempo (percorreram m+n cada) e o loop
    // termina com pA == pB == null, que é exatamente o retorno esperado.
    return pA;
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

- **Comparar por valor em vez de identidade**: valores podem se repetir entre as listas (`1 <= Node.val <= 10^5` não garante unicidade); a resposta certa é sobre qual nó **em memória**, não qual valor.
- **Esquecer de redirecionar para a cabeça da outra lista ao chegar em `null`**: sem isso, o algoritmo vira uma simples corrida em paralelo que nunca converge quando os tamanhos são diferentes.
- **Não tratar o caso sem interseção**: quando não há interseção, os dois ponteiros precisam se tornar `null` **exatamente no mesmo passo** — o truque do "pula para a outra cabeça" garante isso, mas só se a troca acontecer só uma vez por ponteiro (não entrar em loop infinito trocando de novo).
- **Calcular os tamanhos das listas manualmente e "adiantar" o ponteiro mais longo**: essa é outra solução válida (também O(m+n) tempo, O(1) espaço), mas exige duas passadas extras para medir os tamanhos — o truque de trocar de lista resolve com uma lógica mais enxuta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem interseção | `listA=[2,6,4], listB=[1,5]` | `null` | os dois ponteiros viram `null` juntos após percorrer `m+n` |
| Interseção logo na cabeça (listas idênticas) | `listA=headB=[1,2,3]` | nó de valor 1 | testa o encontro no 1º passo, sem precisar trocar de lista |
| Listas de tamanhos bem diferentes | `listA` com 3× o tamanho de `listB`, interseção perto do fim | nó correto | valida que a troca de ponteiros compensa a diferença de tamanho |
| Uma lista é sublista da outra desde o início | `listA=[1,2,4], listB=[1,2,4]` (mesmos nós) | nó de valor 1 | garante comparação por identidade, não por posição |
| Interseção no meio | exemplo do enunciado | nó de valor 8 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0141] Linked List Cycle** (mesma família de dois ponteiros por identidade de nó), **[0021] Merge Two Sorted Lists** (também dois ponteiros percorrendo listas em paralelo, mas combinando em vez de comparando)
- No backend: encontrar onde dois caminhos convergem aparece em análise de **árvores de herança/dependência** (dois módulos que compartilham uma dependência comum a partir de certo ponto) e em estruturas de **grafo compartilhado** como copy-on-write, onde dois ponteiros de versões diferentes passam a apontar para o mesmo bloco de dados a partir de onde não houve modificação.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
