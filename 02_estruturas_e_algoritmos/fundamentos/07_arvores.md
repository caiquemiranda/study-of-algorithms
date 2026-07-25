# 07 — Árvores

> Hierarquia + recursão bem formulada. Soluções em [`../problemas/07_arvores/`](../problemas/07_arvores/).

## 1. Conceito Central e Analogia Didática

- **Árvore binária**: cada nó tem até 2 filhos; **BST** adiciona a regra "esquerda < nó < direita" para a **subárvore inteira** — e o percurso em-ordem sai ordenado.
- Travessias: **pré-ordem** (copiar/serializar), **em-ordem** (BST ordenada), **pós-ordem** (pai precisa do resultado dos filhos), **BFS por nível** (fila).
- O molde mental de 90% dos problemas: *"o que pergunto a cada subárvore, e como combino as respostas no nó?"* — recursão com contrato claro.

**Analogia:** organograma de empresa: cada gerente (nó) consolida os relatórios das suas equipes (subárvores) e repassa um número só para cima (pós-ordem). O BFS é o comunicado que desce andar por andar.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "profundidade / diâmetro / balanceada / simétrica" → DFS **pós-ordem** devolvendo métricas.
- Se pede "por nível / visão da direita / zigzag / média por nível" → **BFS** com fila.
- Se é BST e pede "k-ésimo menor / validar / piso e teto" → **em-ordem** ou descida guiada pela propriedade.
- Se pede "menor ancestral comum (LCA)" → recursão que reporta quem encontrou em cada lado.
- Se pede "construir árvore a partir de travessias" → pré-ordem dá a raiz; em-ordem divide esquerda/direita.

## 3. Templates de Código

### DFS pós-ordem (altura + diâmetro num só percurso)

```java
// Java — a recursão devolve ALTURA; o diâmetro é efeito colateral no nó que junta as duas pernas
private int melhor = 0;

public int diameterOfBinaryTree(TreeNode root) {
    altura(root);
    return melhor;
}

private int altura(TreeNode no) {
    if (no == null) return 0;               // caso base: subárvore vazia não contribui
    int e = altura(no.left);
    int d = altura(no.right);
    melhor = Math.max(melhor, e + d);       // caminho que PASSA por este nó: perna esq + perna dir
    return 1 + Math.max(e, d);              // contrato: devolve a altura desta subárvore ao pai
}
```

```python
def diameter_of_binary_tree(root):
    melhor = 0
    def altura(no):
        nonlocal melhor
        if not no:
            return 0
        e, d = altura(no.left), altura(no.right)
        melhor = max(melhor, e + d)     # atualiza o recorde no ponto de junção
        return 1 + max(e, d)            # o pai só precisa da altura, não do diâmetro
    altura(root)
    return melhor
```

### BFS por nível

```java
// Java — fixar o tamanho da fila ANTES do loop interno separa os níveis
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> res = new ArrayList<>();
    if (root == null) return res;
    Queue<TreeNode> fila = new ArrayDeque<>();
    fila.offer(root);
    while (!fila.isEmpty()) {
        int tamanhoNivel = fila.size();          // congela: só os nós DESTE nível
        List<Integer> nivel = new ArrayList<>();
        for (int i = 0; i < tamanhoNivel; i++) {
            TreeNode no = fila.poll();
            nivel.add(no.val);
            if (no.left != null) fila.offer(no.left);    // filhos entram, mas são do próximo nível
            if (no.right != null) fila.offer(no.right);
        }
        res.add(nivel);
    }
    return res;
}
```

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res, fila = [], deque([root])
    while fila:
        nivel = []
        for _ in range(len(fila)):        # len congelado no início = fronteira do nível
            no = fila.popleft()
            nivel.append(no.val)
            if no.left:  fila.append(no.left)
            if no.right: fila.append(no.right)
        res.append(nivel)
    return res
```

### Validar BST (limites descendo)

```java
// Java — o erro clássico é comparar só com o pai; a restrição vale para a SUBÁRVORE inteira
public boolean isValidBST(TreeNode root) {
    return valida(root, Long.MIN_VALUE, Long.MAX_VALUE); // long: nós podem valer Integer.MIN/MAX
}

private boolean valida(TreeNode no, long lo, long hi) {
    if (no == null) return true;
    if (no.val <= lo || no.val >= hi) return false;  // fora da faixa herdada dos ancestrais
    return valida(no.left, lo, no.val)               // à esquerda, o teto passa a ser o nó atual
        && valida(no.right, no.val, hi);             // à direita, o piso passa a ser o nó atual
}
```

```python
def is_valid_bst(root, lo=float("-inf"), hi=float("inf")):
    if not root:
        return True
    if not (lo < root.val < hi):        # limites herdados de TODOS os ancestrais
        return False
    return (is_valid_bst(root.left, lo, root.val)
            and is_valid_bst(root.right, root.val, hi))
```

## 4. Walkthrough Visual (Teste de Mesa)

`diameter` na árvore `1(2(4, 5), 3)`:

```
      1
     / \
    2   3
   / \
  4   5
```

| Chamada | e | d | melhor após | retorna (altura) |
|---|---|---|---|---|
| altura(4) | 0 | 0 | 0 | 1 |
| altura(5) | 0 | 0 | 0 | 1 |
| altura(2) | 1 | 1 | **2** (4→2→5) | 2 |
| altura(3) | 0 | 0 | 2 | 1 |
| altura(1) | 2 | 1 | max(2, 2+1)=**3** | 3 |

- Diâmetro final: **3** (caminho 4→2→1→3) ✔ — a resposta apareceu num nó interno, não na raiz.

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade | Motivo |
|---|---|---|
| Travessias (DFS/BFS) | O(n) | cada nó visitado uma vez |
| Espaço DFS | O(h) | pilha de recursão = altura |
| Espaço BFS | O(largura) | fila segura um nível inteiro |
| Busca/inserção BST | O(h) | O(log n) balanceada, O(n) degenerada |

## 6. Pegadinhas e Erros Comuns

- Validar BST comparando **só com o pai** — passa em `[5,4,6,null,null,3,7]` e está errado: passe limites.
- **Java**: usar `int` como limite inicial falha quando um nó vale `Integer.MIN_VALUE`/`MAX_VALUE` → use `long` ou `Integer` nullable.
- Esquecer o caso base `if (no == null)` — o erro nº 1 de recursão.
- Confundir **altura** (nó→folha) com **profundidade** (raiz→nó); e nós com arestas no diâmetro.
- BFS sem congelar `fila.size()` antes do loop interno → níveis se misturam.
- **Python**: recursão em árvore degenerada de 10⁴ nós estoura o limite (~1000) → iterativo ou `sys.setrecursionlimit`.
- Escrever a recursão sem **contrato em uma frase** ("devolve a altura da subárvore") — sem contrato, a combinação no nó sai errada.

## 7. Aplicações no Mundo Real (Backend)

- **PostgreSQL**: todo índice padrão é **B-Tree** (BST generalizada para disco, nós = páginas de 8KB).
- **Java**: `TreeMap`/`TreeSet` são Red-Black Trees — iteração ordenada, `floorKey`/`ceilingKey` em O(log n).
- **Parsing**: AST de compiladores e do parser SQL; o plano de execução (`EXPLAIN`) é uma árvore avaliada em pós-ordem.
- **Sistemas de arquivos e DOM**: hierarquias percorridas por DFS/BFS o tempo todo.
- Serialização de árvore (LC 297) = o problema geral de serialização da Fase 4.11.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 🟢 Easy |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟢 Easy |
| 543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | 🟢 Easy |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟡 Medium |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 Medium |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | 🟡 Medium |
| 105 | [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 🟡 Medium |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | 🔴 Hard |
