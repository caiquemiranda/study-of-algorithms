# [0654] Maximum Binary Tree

> 🔗 [LeetCode 654](https://leetcode.com/problems/maximum-binary-tree/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Tree`

## 📜 O Problema

Dado um array de inteiros `nums` sem duplicatas, uma **árvore binária máxima** é construída recursivamente assim: o nó raiz tem o valor máximo de `nums`; a subárvore esquerda é construída recursivamente sobre o **prefixo** à esquerda do máximo; a subárvore direita é construída recursivamente sobre o **sufixo** à direita do máximo. Retorne a árvore binária máxima construída a partir de `nums`.

**Exemplos:**
```
Input:  nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explicação:
- O maior valor é 6. Prefixo [3,2,1], sufixo [0,5].
  - Maior de [3,2,1] é 3. Prefixo [], sufixo [2,1].
    - Maior de [2,1] é 2. Prefixo [], sufixo [1].
  - Maior de [0,5] é 5. Prefixo [0], sufixo [].

Input:  nums = [3,2,1]
Output: [3,null,2,null,1]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 1000` → mesmo O(n²) da abordagem recursiva óbvia passaria, mas existe uma solução O(n) mais elegante via monotonic stack
- `nums[i]` únicos → não há ambiguidade sobre "qual" é o máximo em cada subarray

## 🧭 Como reconhecer o padrão

"Construir uma estrutura onde cada elemento se torna pai de tudo que é menor e mais próximo à sua esquerda/direita" é a assinatura de **monotonic stack**: ao processar o array da esquerda para a direita mantendo uma pilha **decrescente**, cada novo elemento maior que o topo "engole" (vira pai de) todos os elementos menores que acabaram de ser desempilhados — exatamente a relação de parentesco que a árvore máxima exige.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Recursão direta seguindo a definição: encontrar o índice do máximo no subarray atual (varrendo-o), criar o nó, e chamar recursivamente para o prefixo e o sufixo.

- Tempo: O(n²) pior caso (quando o array já está ordenado, cada chamada recursiva faz uma busca linear sobre um subarray que só diminui em 1) · Espaço: O(n) pela recursão
- **Por que não basta:** para arrays já ordenados (crescente ou decrescente), cada nível de recursão busca o máximo num subarray quase do mesmo tamanho do anterior, degradando para O(n²). Com uma pilha monotônica, o array é processado numa única passada O(n), sem re-varrer nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `nums` da esquerda para a direita mantendo uma pilha de **nós** com valores decrescentes de baixo para cima. Para cada novo valor: crie um nó. Enquanto o valor do topo da pilha for **menor** que o valor atual, desempilhe-o — ele se torna o **filho esquerdo** do nó atual (o último desempilhado, que é o maior entre os removidos, vira o filho esquerdo; os demais já foram encadeados nas iterações anteriores). Depois, se ainda sobrar algo na pilha, o nó atual se torna o **filho direito** do novo topo (o valor que "contém" o atual à sua direita). Empilhe o nó atual. No final, a base da pilha é a raiz da árvore.

## 🎬 Exemplo passo a passo

`nums = [3,2,1,6,0,5]`

| Passo | Valor | Ação do while (desempilha menores, guarda o último como filho esquerdo) | Filho direito de quem sobrou no topo | Pilha após (valores, base→topo) |
|---|---|---|---|---|
| 1 | 3 | pilha vazia | — | `[3]` |
| 2 | 2 | 3 não < 2, não desempilha | nó(2) vira filho direito de 3 | `[3, 2]` |
| 3 | 1 | 2 não < 1, não desempilha | nó(1) vira filho direito de 2 | `[3, 2, 1]` |
| 4 | 6 | 1<6→pop(esq=1); 2<6→pop(esq=2, sobrescreve); 3<6→pop(esq=3, sobrescreve) | pilha vazia, sem pai | `[6]` (filho esquerdo de 6 = nó 3, que já tem 2 como seu filho direito, que já tem 1 como filho direito) |
| 5 | 0 | 6 não < 0, não desempilha | nó(0) vira filho direito de 6 | `[6, 0]` |
| 6 | 5 | 0<5→pop(esq=0) | pilha tem `[6]` → nó(5) vira filho direito de 6 | `[6, 5]` (filho esquerdo de 5 = nó 0) |

Base da pilha = raiz = nó `6`, com filho esquerdo `3` (que tem filho direito `2`, que tem filho direito `1`) e filho direito `5` (que tem filho esquerdo `0`).

Resultado final: `[6,3,5,null,2,0,null,null,1]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada elemento é empilhado e desempilhado no máximo uma vez
- **Espaço:** O(n) — a pilha guarda no máximo todos os nós (array estritamente crescente, nunca desempilha nada até o fim)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public TreeNode constructMaximumBinaryTree(int[] nums) {
    Deque<TreeNode> pilha = new ArrayDeque<>(); // valores decrescentes da base para o topo

    for (int num : nums) {
        TreeNode atual = new TreeNode(num);
        TreeNode ultimoDesempilhado = null;

        // desempilha tudo que é menor: o atual "engole" esses nós à sua esquerda
        while (!pilha.isEmpty() && pilha.peek().val < num) {
            ultimoDesempilhado = pilha.pop();
        }
        atual.left = ultimoDesempilhado; // o último (maior entre os removidos) vira filho esquerdo

        if (!pilha.isEmpty()) {
            pilha.peek().right = atual; // quem sobrou no topo "adota" o atual como filho direito
        }

        pilha.push(atual);
    }

    // a base da pilha é a raiz: o primeiro elemento nunca é desempilhado até sobrar só ele
    TreeNode raiz = null;
    while (!pilha.isEmpty()) {
        raiz = pilha.pop();
    }
    return raiz;
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

- Usar o **primeiro** desempilhado como filho esquerdo em vez do **último** — dentro do while, cada elemento desempilhado sobrescreve o filho esquerdo do próximo maior automaticamente durante as iterações anteriores; o que sobra ao final do while (o último a sair) é o que realmente deve virar filho esquerdo do nó atual, pois é o maior entre os que "perderam" para o valor atual.
- Esquecer de checar se a pilha ainda tem algo antes de setar `right` do topo — se a pilha ficou vazia depois do while, não há pai para o nó atual (ele mesmo é temporariamente uma nova "raiz candidata").
- Confundir a direção: valores desempilhados (menores, à esquerda na entrada) tornam-se filhos **esquerdos**; o nó atual torna-se filho **direito** de quem sobra no topo (que está à esquerda dele na entrada, mas ainda não foi "superado"). Trocar `left`/`right` produz uma árvore com estrutura espelhada errada.
- Extrair a raiz incorretamente ao final — a raiz é o elemento que nunca foi desempilhado por ninguém maior, ou seja, o que sobra na **base** da pilha depois de todo o processamento.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Array decrescente | `[3,2,1]` | `[3,null,2,null,1]` | cada elemento vira filho direito do anterior, nunca desempilha nada |
| Array crescente | `[1,2,3]` | `[3,2,null,1]` (raiz 3, filho esquerdo 2, que tem filho esquerdo 1) | cada elemento desempilha tudo antes dele, formando uma cadeia à esquerda |
| Um único elemento | `[5]` | `[5]` | nó único, sem filhos |
| Máximo no meio | `[3,2,1,6,0,5]` | `[6,3,5,null,2,0,null,null,1]` | caso do enunciado, testa filhos dos dois lados |

## 🔗 Conexões

- Problemas irmãos: [0496] Next Greater Element I (mesma técnica de monotonic stack, mas retornando um valor em vez de construir relações de parentesco), [0105] Construct Binary Tree from Preorder and Inorder Traversal (outra construção de árvore a partir de array, mas com técnica de divisão diferente)
- No backend: essa técnica de "cada elemento adota os menores desempilhados como filhos" aparece em construção de treaps e cartesian trees (estruturas usadas em índices de banco de dados e em algoritmos de range query), onde a prioridade de cada nó determina sua posição na hierarquia de forma similar a este problema.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
