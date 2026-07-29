# [0938] Range Sum of BST

> 🔗 [LeetCode 938](https://leetcode.com/problems/range-sum-of-bst/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma BST e dois inteiros `low` e `high`, retorne a **soma dos valores** de todos os nós cujo valor está no intervalo `[low, high]` (inclusive).

**Exemplos:**
```
Input:  root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Input:  root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 2 * 10^4]` → precisa de solução eficiente; O(n) resolve, mas O(n) sempre visitando tudo é o "teto", não o ideal
- `1 <= Node.val <= 10^5`, `1 <= low <= high <= 10^5` → valores cabem em `int`
- `Node.val` **únicos** → não há ambiguidade sobre "qual nó de valor X" ao usar a propriedade de BST para decidir por onde descer

## 🧭 Como reconhecer o padrão

"Somar valores num intervalo, numa BST" é sinal de aproveitar a propriedade de ordenação para **podar** ramos que não podem conter nada dentro do intervalo: se o valor do nó atual já é menor que `low`, toda a subárvore esquerda dele é ainda menor — pode ser ignorada inteira; se é maior que `high`, a subárvore direita pode ser ignorada.

## 🐢 Solução 1 — Força bruta (visitar todos os nós, ignorando a ordem)

Percorrer a árvore inteira com DFS ou BFS genérico, somando `no.val` sempre que ele estiver dentro de `[low, high]`, sem usar a comparação para decidir se vale a pena descer para um lado ou outro.

- Tempo: O(n) sempre, mesmo quando o intervalo é pequeno · Espaço: O(h) (ou O(largura) no BFS)
- **Por que não basta:** não está errado, mas desperdiça a garantia de BST. Se o intervalo `[low, high]` cobre só uma pequena parte da árvore, essa abordagem ainda visita **todos** os n nós, incluindo ramos inteiros que a propriedade de ordenação já deixa claro que estão fora do intervalo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em cada nó: se `no.val < low`, não desça pela esquerda (lá só existem valores ainda menores, fora do intervalo); se `no.val > high`, não desça pela direita (só valores ainda maiores). Se `no.val` está dentro do intervalo, some-o e desça para **ambos** os lados (pode haver mais valores válidos nos dois).

## 🎬 Exemplo passo a passo

`root = [10,5,15,3,7,null,18]`, `low = 7, high = 15`

```
        10
       /  \
      5    15
     / \     \
    3   7     18
```

| Passo | Nó | Dentro de [7,15]? | Ação |
|---|---|---|---|
| 1 | 10 | sim | soma 10; desce para ambos os lados |
| 2 | 5 | não (5 < 7) | **poda** a esquerda de 5 (o `3`); ainda desce à direita (o `7` pode estar no intervalo) |
| 3 | 7 | sim | soma 7 (total: 17); sem filhos, nada mais a fazer |
| 4 | 15 | sim | soma 15 (total: 32); desce para a direita |
| 5 | 18 | não (18 > 15) | **poda** a direita de 18 (não existe, mas o princípio vale); nó descartado |

Resultado final: `10 + 7 + 15 = 32` ✔ (bate com o enunciado — o `3` e o `18` nunca contribuíram, e o `3` sequer precisou ser comparado individualmente, pois toda a subárvore de `5` à esquerda foi podada de uma vez)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no pior caso (intervalo cobre a árvore inteira), mas potencialmente muito menor quando o intervalo é estreito, graças à poda
- **Espaço:** O(h) de pilha de recursão

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int rangeSumBST(TreeNode root, int low, int high) {
    if (root == null) return 0;

    // fora do intervalo por baixo: só a subárvore DIREITA pode ter valores válidos
    if (root.val < low) return rangeSumBST(root.right, low, high);

    // fora do intervalo por cima: só a subárvore ESQUERDA pode ter valores válidos
    if (root.val > high) return rangeSumBST(root.left, low, high);

    // dentro do intervalo: soma este nó e explora AMBOS os lados
    return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high);
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

- Descer para os dois lados sempre, mesmo quando `no.val` já está fora do intervalo — desperdiça a poda que a propriedade de BST permite, degradando para O(n) mesmo em casos onde o intervalo é pequeno.
- Usar `<=`/`>=` errado nos limites — o intervalo é **inclusivo** (`[low, high]`), então um nó com `no.val == low` ou `no.val == high` deve ser somado, não excluído.
- Esquecer o caso base `root == null` — sem ele, a recursão que desce para um filho ausente quebra com `NullPointerException`.
- Tratar como árvore binária genérica (a força bruta), visitando sempre os dois lados — funciona, mas ignora a informação que a garantia de BST oferece de graça.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só, dentro do intervalo | `root = [10], low = 5, high = 15` | `10` | caso base, soma trivial |
| Um nó só, fora do intervalo | `root = [10], low = 15, high = 20` | `0` | testa que um único nó fora do intervalo não é somado |
| Intervalo cobrindo a árvore inteira | `root = [10,5,15,3,7,null,18], low = 1, high = 100` | soma de todos os nós | garante que sem poda a solução ainda soma corretamente tudo |
| Intervalo estreito no meio da árvore | `root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10` | `23` | cobre o exemplo 2 do enunciado, testa poda dos dois lados |

## 🔗 Conexões

- Problemas irmãos: [0700] Search in a Binary Search Tree (mesma ideia de usar a comparação para decidir o lado, mas buscando um valor único em vez de somar um intervalo), [0230] Kth Smallest Element in a BST (também aproveita a ordenação da BST, mas via travessia em-ordem)
- No backend: somar/agregar valores dentro de um intervalo usando um índice ordenado (poda de ramos fora do range) é exatamente como consultas `WHERE valor BETWEEN low AND high` são otimizadas por índices B-Tree em bancos de dados — o índice evita varrer a tabela inteira, descendo só pelos ramos que podem conter linhas no intervalo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
