# [0086] Partition List

> 🔗 [LeetCode 86](https://leetcode.com/problems/partition-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Sentinela` `#DuasListas` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list e um valor `x`, particione a lista de forma que todos os nós com valor **menor que** `x` venham antes dos nós com valor **maior ou igual a** `x`. A ordem relativa original dentro de cada partição deve ser **preservada**.

**Exemplos:**
```
Input:  head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input:  head = [2,1], x = 2
Output: [1,2]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 200]` → O(n) é o esperado, uma única passada
- `-100 <= Node.val <= 100` e `-200 <= x <= 200` → sem risco de overflow
- "preserve a ordem relativa original" → é a restrição mais importante: descarta qualquer abordagem que ordene ou reordene dentro de cada grupo (ex.: um algoritmo de partição estilo quicksort que troca posições) — só é permitido **filtrar preservando ordem**

## 🧭 Como reconhecer o padrão

"Separe em dois grupos preservando a ordem relativa" é resolvido de forma direta construindo **duas listas novas simultaneamente** — uma para "menores que x", outra para "maiores ou iguais" — reaproveitando os nós existentes, e depois **emendando** as duas ao final. É uma combinação de nó sentinela (dois sentinelas, um por lista) com a técnica de "só reorganizar ponteiros" (ver [fundamentos](../../../fundamentos/06_linked_list.md)).

## 🐢 Solução 1 — Força bruta (copiar valores para dois arrays, reconstruir)

Percorre a lista original duas vezes: primeiro guarda os valores `< x` num array (na ordem em que aparecem), depois guarda os valores `>= x` noutro array. Constrói uma lista nova concatenando os dois arrays.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** o tempo já é ótimo, mas cria nós novos do zero quando dá para resolver só reorganizando os ponteiros dos nós já existentes — sem alocar nada além de dois sentinelas descartáveis.

## 💡 Solução 2 — A ideia otimizada (intuição)

Cria dois sentinelas, `lessDummy` (cabeça da lista dos "menores que x") e `geDummy` (cabeça da lista dos "maiores ou iguais"), cada um com um ponteiro de cauda que vai sendo estendido. Percorre a lista original **uma única vez**: cada nó é "anexado" (via ponteiro `next`, sem copiar) na cauda da lista correta, dependendo se `val < x` ou `val >= x`. Como cada nó só é movido, nunca copiado, a ordem relativa dentro de cada grupo é automaticamente preservada (a ordem de chegada é a ordem original). No final, emenda a cauda da lista "menores" ao início da lista "maiores/iguais".

## 🎬 Exemplo passo a passo

`head = [1,4,3,2,5,2]`, `x = 3`

| Nó visitado | val < 3? | Vai para | Lista "menores" (less) | Lista "maiores/iguais" (ge) |
|---|---|---|---|---|
| 1 | sim | less | 1 | — |
| 4 | não | ge | 1 | 4 |
| 3 | não (3 não é `< 3`) | ge | 1 | 4 → 3 |
| 2 | sim | less | 1 → 2 | 4 → 3 |
| 5 | não | ge | 1 → 2 | 4 → 3 → 5 |
| 2 | sim | less | 1 → 2 → 2 | 4 → 3 → 5 |

Emenda: `less` termina em `2`, aponta para o início de `ge` (`4`); `ge` termina em `5`, aponta para `null`.

Resultado final: `1 → 2 → 2 → 4 → 3 → 5` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela lista original
- **Espaço:** O(1) extra — só os dois sentinelas e ponteiros de cauda; os nós são reaproveitados, não copiados

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode partition(ListNode head, int x) {
    ListNode lessDummy = new ListNode(0); // cabeça descartável da lista "< x"
    ListNode geDummy = new ListNode(0);   // cabeça descartável da lista ">= x"
    ListNode less = lessDummy, ge = geDummy;

    while (head != null) {
        if (head.val < x) {
            less.next = head; // anexa (não copia) o nó atual na cauda da lista correta
            less = less.next;
        } else {
            ge.next = head;
            ge = ge.next;
        }
        head = head.next;
    }

    // Crucial: fecha a cauda de "ge" com null. Sem isso, o último nó de "ge" ainda
    // carrega o ponteiro .next do encadeamento ORIGINAL, o que pode criar um ciclo
    // acidental se esse nó também tiver ido parar em "less" mais cedo na travessia.
    ge.next = null;

    less.next = geDummy.next; // emenda: fim de "menores" aponta para o início de "maiores/iguais"
    return lessDummy.next;
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

- **Esquecer `ge.next = null` no final**: o último nó da lista "maiores/iguais" ainda carrega o ponteiro `.next` da lista original — se esse ponteiro apontava para um nó que já foi movido para a lista "menores", a lista final fica com um **ciclo acidental**.
- **Usar `<=` em vez de `<` na comparação**: o problema define a partição como "menor que x" vs. "maior ou igual a x" — usar `<=` move valores iguais a `x` para o grupo errado.
- **Tentar reordenar dentro de cada grupo (ex.: ordenar por valor)**: o enunciado exige preservar a **ordem relativa original**, não ordenar — só filtrar mantendo a sequência de chegada.
- **Comparar `head.val` depois de já ter avançado `head`**: a leitura do valor e a decisão de qual lista usar precisam acontecer **antes** de mover `head` para o próximo nó, senão a lógica perde a referência do nó que está sendo classificado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head=[], x=1` | `[]` | os dois sentinelas ficam vazios, `less.next` é `null` |
| Todos menores que x | `head=[1,2], x=5` | `[1,2]` | a lista "ge" fica vazia; emenda não muda nada |
| Todos maiores ou iguais a x | `head=[5,6], x=1` | `[5,6]` | a lista "less" fica vazia; `lessDummy.next` aponta direto para "ge" |
| x igual a um valor da lista | `head=[2,1], x=2` | `[1,2]` | valida que `2 >= x` vai para o grupo certo (exemplo do enunciado) |
| Exemplo maior do enunciado | `head=[1,4,3,2,5,2], x=3` | `[1,2,2,4,3,5]` | trace acima, valida preservação de ordem em ambos os grupos |

## 🔗 Conexões

- Problemas irmãos: **[0075] Sort Colors** (partição em 3 grupos, mas em array com três ponteiros in-place, sem a exigência de preservar ordem), **[0143] Reorder List** (também constrói/religa listas auxiliares antes de emendar o resultado final)
- No backend: separar registros em dois grupos preservando ordem, numa única passada, é o padrão usado em **filtros de stream** (separar eventos "válidos" de "inválidos" mantendo a ordem cronológica de cada grupo) e no passo de **partição estável** de algoritmos de ordenação (ex.: radix sort, que depende de partições estáveis para funcionar corretamente).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
