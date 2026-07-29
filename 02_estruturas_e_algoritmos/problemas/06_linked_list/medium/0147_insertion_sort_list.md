# [0147] Insertion Sort List

> 🔗 [LeetCode 147](https://leetcode.com/problems/insertion-sort-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Sentinela` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list, ordene-a usando o algoritmo de **insertion sort** e retorne a lista ordenada. A ideia do insertion sort: mantém-se uma porção já ordenada (inicialmente só o 1º elemento); a cada passo, remove-se um elemento não processado e insere-se no **lugar certo** dentro da porção ordenada.

**Exemplos:**
```
Input:  head = [4,2,1,3]
Output: [1,2,3,4]

Input:  head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 5000]` → o insertion sort é O(n²) no pior caso; com `n` até 5000, isso significa até ~25 milhões de comparações — aceitável, mas confirma que este problema é sobre **praticar a técnica**, não sobre performance máxima (para isso existe o LC 148, Sort List, que pede O(n log n))
- `-5000 <= Node.val <= 5000` → sem risco de overflow
- "ordene usando insertion sort" → é uma restrição de **técnica**, não só de resultado: o enunciado quer especificamente a adaptação do algoritmo clássico de insertion sort para ponteiros, não qualquer ordenação que produza a saída certa

## 🧭 Como reconhecer o padrão

"Construa uma porção ordenada, inserindo um elemento de cada vez no lugar certo" é o insertion sort clássico — a parte de linked list é **como encontrar e inserir no lugar certo usando ponteiros**, em vez de deslocar elementos de um array. É outra aplicação do **nó sentinela** (ver [fundamentos](../../../fundamentos/06_linked_list.md)): a porção ordenada é construída a partir de um `dummy`, o que evita tratar "inserir na cabeça da porção ordenada" como caso especial.

## 🐢 Solução 1 — Força bruta (ordenar com outro algoritmo, fora do escopo do exercício)

Copia os valores para um array, ordena com o algoritmo de ordenação genérico da linguagem (ex.: `Arrays.sort`, que usa Timsort, O(n log n)), e reconstrói a lista a partir do array ordenado.

- Tempo: O(n log n) · Espaço: O(n)
- **Por que não basta:** tecnicamente essa abordagem é até **mais rápida** em Big-O do que o insertion sort pedido — mas foge completamente do que o enunciado pede para praticar. O exercício aqui é especificamente adaptar o **insertion sort** (um algoritmo O(n²) por natureza) para trabalhar com ponteiros de uma linked list, não apenas produzir a saída ordenada por qualquer meio.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantém um sentinela (`dummy`) apontando para o início da **porção já ordenada** (que começa vazia). Para cada nó `cur` da lista original (na ordem em que aparecem, guardando `cur.next` **antes** de desconectá-lo): percorre a porção ordenada a partir de `dummy` até achar a posição certa (o primeiro nó cuja `val` não é menor que `cur.val`), e insere `cur` ali, religando os ponteiros. Repete até processar todos os nós originais.

## 🎬 Exemplo passo a passo

`head = [4,2,1,3]`

| `cur` processado | Porção ordenada ANTES | Posição de inserção | Porção ordenada DEPOIS |
|---|---|---|---|
| 4 | (vazia) | início (só elemento) | `4` |
| 2 | `4` | antes de `4` (2 < 4) | `2 → 4` |
| 1 | `2 → 4` | antes de `2` (1 < 2) | `1 → 2 → 4` |
| 3 | `1 → 2 → 4` | entre `2` e `4` (2 < 3 < 4) | `1 → 2 → 3 → 4` |

Resultado final: `1 → 2 → 3 → 4` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) no pior caso (lista em ordem decrescente: cada inserção percorre a porção ordenada inteira) · O(n) no melhor caso (lista já ordenada: cada inserção para na 1ª comparação)
- **Espaço:** O(1) — sentinela e ponteiros; nenhuma estrutura auxiliar, os nós são reaproveitados

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode insertionSortList(ListNode head) {
    ListNode dummy = new ListNode(0); // cabeça da porção ordenada, começa vazia
    ListNode cur = head;

    while (cur != null) {
        ListNode next = cur.next; // salva ANTES de desconectar cur do resto da lista original

        // Percorre a porção ordenada procurando onde cur se encaixa: o primeiro ponto
        // em que o próximo nó já não é menor que cur (ou o fim da porção ordenada).
        ListNode prev = dummy;
        while (prev.next != null && prev.next.val < cur.val) {
            prev = prev.next;
        }

        cur.next = prev.next; // insere cur no lugar certo
        prev.next = cur;

        cur = next; // avança para o próximo nó da lista ORIGINAL (não da ordenada)
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

- **Esquecer de salvar `cur.next` antes de desconectar `cur`**: assim que `cur.next = prev.next` é executado, o ponteiro para o resto da lista **original** se perde — sem guardar `next` antes, o loop externo não sabe qual é o próximo nó a processar.
- **Reiniciar a busca da posição de inserção sempre a partir de `dummy`**: é exatamente o que o insertion sort exige (percorrer a porção ordenada do início), mas é fácil, por engano, tentar "otimizar" continuando de onde a busca anterior parou — isso quebra a corretude, porque a posição de inserção não tem relação com a anterior.
- **Usar `<=` em vez de `<` na comparação**: com `<=`, elementos de valor igual mudam de posição relativa (o novo elemento pula na frente do igual já inserido) — não quebra a ordenação, mas altera a estabilidade da ordenação, o que pode importar em variações do problema.
- **Confundir "porção ordenada" com "lista original restante"**: `cur` sempre avança pela lista **original** (via `next` salvo antes), nunca pela porção ordenada que está sendo construída — são duas travessias independentes.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó | `head = [1]` | `[1]` | porção ordenada recebe o único nó direto, sem comparação |
| Já ordenada (melhor caso) | `head = [1,2,3]` | `[1,2,3]` | cada inserção para na 1ª comparação, O(n) total |
| Ordem decrescente (pior caso) | `head = [3,2,1]` | `[1,2,3]` | cada inserção percorre a porção ordenada inteira, O(n²) |
| Valores duplicados | `head = [2,1,2]` | `[1,2,2]` | valida que `<` (não `<=`) mantém a corretude com empates |
| Exemplo do enunciado com negativos | `head = [-1,5,3,4,0]` | `[-1,0,3,4,5]` | garante que sinais negativos não afetam a lógica de comparação |

## 🔗 Conexões

- Problemas irmãos: **[0148] Sort List** (o mesmo objetivo de ordenar uma linked list, mas exigindo O(n log n) — força uma técnica diferente, merge sort), **[0021] Merge Two Sorted Lists** (a sub-rotina de "inserir mantendo ordem" usada aqui em miniatura, um nó de cada vez)
- No backend: manter uma coleção pequena sempre ordenada, inserindo um item de cada vez no lugar certo, é o padrão usado em **listas de prioridade simples** (quando `n` é pequeno o suficiente para o custo O(n) por inserção não importar) e em algoritmos híbridos de ordenação (como o Timsort, que usa insertion sort para sub-listas pequenas antes de fazer merge, exatamente porque insertion sort é rápido na prática para entradas quase ordenadas ou minúsculas).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
