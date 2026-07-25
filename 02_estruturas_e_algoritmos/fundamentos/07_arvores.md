# 07 — Árvores

> Estrutura hierárquica; a maioria dos problemas é recursão bem formulada. Problemas em [`../problemas/07_arvores/`](../problemas/07_arvores/).

## Conceito

**Árvore binária**: cada nó tem até 2 filhos. Termos: raiz, folha, altura (maior caminho até folha), profundidade (distância da raiz).

**BST (Binary Search Tree)**: esquerda < nó < direita, para **toda** a subárvore. Busca/inserção/remoção O(h) — O(log n) balanceada, O(n) degenerada em lista. Percurso **em-ordem devolve os valores ordenados** (a propriedade mais explorada em problemas).

**Travessias:**
- **DFS pré-ordem** (nó, esq, dir): copiar/serializar árvore
- **DFS em-ordem** (esq, nó, dir): BST em ordem crescente
- **DFS pós-ordem** (esq, dir, nó): quando o pai precisa do resultado dos filhos (altura, diâmetro, deletar)
- **BFS por nível** (fila): level order, visão por camadas

**O molde mental**: quase todo problema de árvore é *"o que eu pergunto para cada subárvore, e como combino as respostas no nó?"* — recursão com contrato claro.

## Como reconhecer no enunciado

- "profundidade / diâmetro / balanceada / simétrica" → DFS pós-ordem devolvendo métricas
- "por nível / da esquerda para a direita / zigzag / visão lateral" → BFS
- "k-ésimo menor / validar / sucessor" em BST → em-ordem ou descida guiada pela propriedade
- "ancestral comum (LCA)" → recursão que devolve quem foi encontrado em cada lado

## Templates

```python
# DFS pós-ordem — altura e diâmetro juntos
def diameter(root):
    melhor = 0
    def altura(no):
        nonlocal melhor
        if not no:
            return 0
        e, d = altura(no.left), altura(no.right)
        melhor = max(melhor, e + d)      # caminho que passa por este nó
        return 1 + max(e, d)
    altura(root)
    return melhor

# BFS por nível
from collections import deque
def level_order(root):
    if not root:
        return []
    res, fila = [], deque([root])
    while fila:
        nivel = []
        for _ in range(len(fila)):        # processa exatamente um nível
            no = fila.popleft()
            nivel.append(no.val)
            if no.left:  fila.append(no.left)
            if no.right: fila.append(no.right)
        res.append(nivel)
    return res

# Validar BST — passe limites para baixo (não compare só com o pai!)
def is_valid_bst(root, lo=float("-inf"), hi=float("inf")):
    if not root:
        return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left, lo, root.val)
            and is_valid_bst(root.right, root.val, hi))

# LCA em árvore binária
def lca(root, p, q):
    if not root or root is p or root is q:
        return root
    e = lca(root.left, p, q)
    d = lca(root.right, p, q)
    if e and d:
        return root                       # um de cada lado: este é o LCA
    return e or d
```

## Complexidade típica

Travessias: O(n) tempo, O(h) espaço (pilha de recursão) ou O(largura) no BFS. Operações de BST: O(h).

## Erros comuns

- Validar BST comparando só com o pai (o clássico) — a restrição é da **subárvore inteira**, passe limites
- Confundir altura com profundidade, ou nós com arestas no diâmetro
- Esquecer o caso base `if not no` (o mais comum de todos)
- No BFS por nível, não fixar `len(fila)` antes do loop interno
- Recursão sem contrato claro: escreva em uma frase o que sua função devolve antes de codar

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 226. Invert Binary Tree | 🟢 easy |
| 104. Maximum Depth | 🟢 easy |
| 543. Diameter of Binary Tree | 🟢 easy |
| 110. Balanced Binary Tree | 🟢 easy |
| 100. Same Tree / 572. Subtree of Another Tree | 🟢 easy |
| 235. LCA of a BST | 🟡 medium |
| 102. Level Order Traversal | 🟡 medium |
| 199. Right Side View | 🟡 medium |
| 98. Validate BST | 🟡 medium |
| 230. Kth Smallest in BST | 🟡 medium |
| 105. Construct from Preorder and Inorder | 🟡 medium |
| 124. Binary Tree Maximum Path Sum | 🔴 hard |
| 297. Serialize and Deserialize | 🔴 hard |

## Conexão com backend

Índices de banco são **B-Trees/B+Trees** (BSTs generalizadas para disco — Fase 5.3); `TreeMap` do Java é uma Red-Black Tree; o DOM, ASTs de compiladores e a hierarquia de processos do SO são árvores. Serialização de árvore (LC 297) é o mesmo problema de serialização da Fase 4.11.
