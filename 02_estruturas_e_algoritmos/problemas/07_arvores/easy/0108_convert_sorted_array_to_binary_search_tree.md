# [0108] Convert Sorted Array to Binary Search Tree

> 🔗 [LeetCode 108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DivideEConquista` `#Easy`

## 📜 O Problema

Dado um array `nums` ordenado em ordem **estritamente crescente**, converta-o numa **BST balanceada em altura** (height-balanced).

**Exemplos:**
```
Input:  nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]   (ou [0,-10,5,null,-3,null,9] — ambos aceitos)

Input:  nums = [1,3]
Output: [3,1]                 (ou [1,null,3] — ambos aceitos)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → precisa de solução O(n); qualquer coisa quadrática por causa de inserção repetida numa BST desbalanceada é arriscado
- `-10^4 <= nums[i] <= 10^4` → valores cabem em `int`
- `nums` **estritamente crescente** → não há duplicatas, então nunca existe ambiguidade sobre "para qual lado vai um valor igual"
- "height-balanced" é a restrição mais importante do problema: existem **múltiplas** BSTs válidas com o mesmo conjunto de valores, mas só as que mantêm altura O(log n) são aceitas

## 🧭 Como reconhecer o padrão

Array ordenado + "construa uma BST balanceada" é sinal de **divisão e conquista**: se você sempre escolhe o **elemento do meio** como raiz, metade dos elementos menores forma a subárvore esquerda e metade dos maiores forma a direita — recursivamente, cada subchamada também escolhe o meio do seu próprio intervalo. Essa escolha é o que garante o balanceamento, não é um acidente.

## 🐢 Solução 1 — Força bruta (sempre usar o primeiro elemento como raiz)

Pegar `nums[0]` como raiz, e colocar todo o resto como filhos à direita recursivamente (como se fosse construir uma lista ligada disfarçada de árvore) — ou, de forma equivalente, inserir os elementos um a um numa BST vazia usando a inserção clássica de BST, na ordem em que aparecem no array.

- Tempo: O(n) para a primeira abordagem, O(n²) no pior caso para a inserção um a um (cada inserção percorre o caminho até a folha, que cresce a cada inserção) · Espaço: O(n)
- **Por que não basta:** as duas formas produzem uma árvore **degenerada** (uma corrente, praticamente uma lista ligada) quando o array já está ordenado — que é exatamente a entrada garantida aqui. Isso viola diretamente a restrição "height-balanced": a altura fica O(n) em vez de O(log n).

## 💡 Solução 2 — A ideia otimizada (intuição)

Escolha sempre o **elemento do meio** do intervalo `[esquerda, direita]` atual como raiz da subárvore. Chame recursivamente para `[esquerda, meio-1]` (vira a subárvore esquerda) e `[meio+1, direita]` (vira a subárvore direita). Como o array já está ordenado, o meio automaticamente é maior que tudo à esquerda e menor que tudo à direita — a propriedade de BST sai de graça, sem nenhuma comparação extra.

## 🎬 Exemplo passo a passo

`nums = [-10,-3,0,5,9]` (índices 0 a 4)

| Passo | Intervalo [esq,dir] | meio (índice) | Valor da raiz | Subárvores geradas |
|---|---|---|---|---|
| 1 | [0,4] | 2 | 0 | esquerda=[0,1], direita=[3,4] |
| 2 | [0,1] | 0 | -10 | esquerda=[], direita=[1,1] |
| 3 | [1,1] | 1 | -3 | esquerda=[], direita=[] |
| 4 | [3,4] | 3 | 5 | esquerda=[], direita=[4,4] |
| 5 | [4,4] | 4 | 9 | esquerda=[], direita=[] |

Árvore final: raiz `0`, filho esquerdo `-10` (com filho direito `-3`), filho direito `5` (com filho direito `9`) — profundidade máxima 3, balanceada ✔ (equivalente ao `[0,-10,5,null,-3,null,9]` aceito no enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada elemento do array vira exatamente um nó, visitado uma única vez
- **Espaço:** O(log n) de pilha de recursão (árvore balanceada por construção) **+** O(n) da árvore resultante em si

## 💻 Implementações

### Java (referência completa e comentada)
```java
public TreeNode sortedArrayToBST(int[] nums) {
    return constroi(nums, 0, nums.length - 1);
}

private TreeNode constroi(int[] nums, int esquerda, int direita) {
    if (esquerda > direita) return null; // intervalo vazio: sem nó aqui

    // elemento do meio vira a raiz — garante metade dos valores para cada lado
    int meio = esquerda + (direita - esquerda) / 2; // evita overflow de (esquerda+direita)/2 em arrays gigantes
    TreeNode no = new TreeNode(nums[meio]);

    no.left = constroi(nums, esquerda, meio - 1);
    no.right = constroi(nums, meio + 1, direita);

    return no;
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

- Usar `(esquerda + direita) / 2` em vez de `esquerda + (direita - esquerda) / 2` — praticamente inofensivo aqui dado o limite de `10^4`, mas é o hábito certo para evitar overflow de `int` em arrays maiores.
- Escolher sempre o elemento de baixo do meio (`meio = (esq+dir)/2` arredondando para baixo) vs de cima — ambos geram árvores balanceadas válidas, mas formatos **diferentes**; o enunciado aceita qualquer BST balanceada, então não existe "a" resposta certa, só validação por propriedade (altura O(log n) + é BST válida).
- Esquecer o caso base `esquerda > direita` — sem ele, a recursão nunca para e estoura a pilha, ou tenta acessar `nums[meio]` fora dos limites.
- Achar que qualquer BST construída a partir do array (mesmo sem escolher o meio) passa no teste — o validador do LeetCode checa altura balanceada explicitamente, não só se os valores formam uma BST válida.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento | `nums = [5]` | `[5]` | caso base direto, sem recursão adicional |
| Dois elementos | `nums = [1,3]` | `[3,1]` ou `[1,null,3]` | testa a escolha do meio com array par, ambas as respostas são válidas |
| Array com negativos | `nums = [-10,-3,0,5,9]` | árvore balanceada com raiz `0` | cobre o exemplo do enunciado, valores negativos não afetam a lógica de índices |
| Array grande e ordenado | `nums = [1..10^4]` | árvore com altura ≈ log₂(10^4) ≈ 14 | garante que a escolha do meio realmente produz O(log n), não O(n) |

## 🔗 Conexões

- Problemas irmãos: [0109] Convert Sorted List to Binary Search Tree (mesma ideia, mas a entrada é uma linked list em vez de array, o que muda como se acha "o meio"), [0110] Balanced Binary Tree (valida exatamente a propriedade que esta construção garante por design)
- No backend: essa técnica de "sempre dividir pelo meio" é a mesma ideia por trás de árvores de índice balanceadas (B-Trees em bancos de dados) construídas em lote (bulk loading) a partir de dados já ordenados — muito mais rápido que inserir registro por registro numa árvore vazia.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
