# [0700] Search in a Binary Search Tree

> 🔗 [LeetCode 700](https://leetcode.com/problems/search-in-a-binary-search-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#Easy`

## 📜 O Problema

Dado o `root` de uma BST e um inteiro `val`, encontre o nó cujo valor é `val` e retorne a **subárvore** enraizada nele. Se não existir, retorne `null`.

**Exemplos:**
```
Input:  root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input:  root = [4,2,7,1,3], val = 5
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 5000]` → precisa de solução eficiente; O(n) já resolve, mas O(h) é possível e mais barato
- `1 <= Node.val, val <= 10^7` → valores cabem em `int`
- "`root` é garantidamente uma BST" → é a permissão explícita para usar a propriedade de ordenação em vez de tratar como árvore binária genérica

## 🧭 Como reconhecer o padrão

"Buscar um valor numa BST" é a operação mais fundamental da estrutura: como toda subárvore respeita "esquerda < nó < direita", cada comparação elimina **metade** da árvore restante (numa árvore balanceada), exatamente como busca binária num array ordenado — só que "o array" aqui é a própria forma da árvore.

## 🐢 Solução 1 — Força bruta (DFS/BFS genérico ignorando a ordem)

Percorrer a árvore inteira com qualquer travessia (pré-ordem, BFS, tanto faz), comparando `no.val == val` em cada nó, sem usar a comparação para decidir para qual lado ir.

- Tempo: O(n) · Espaço: O(h) (ou O(largura) se for BFS)
- **Por que não basta:** funciona, mas ignora a informação mais valiosa que a garantia de BST oferece de graça: **em qual lado procurar**. Numa árvore balanceada de 5000 nós, isso é a diferença entre visitar todos os 5000 nós (pior caso) e visitar só ~13 (log₂ 5000 ≈ 12.3).

## 💡 Solução 2 — A ideia otimizada (intuição)

Compare `val` com `no.val`: se forem iguais, achou — retorna esse nó (e toda a subárvore dele, que já é a resposta). Se `val` for menor, a resposta só pode estar à **esquerda** (a propriedade de BST garante isso); se for maior, só pode estar à **direita**. Nunca é preciso olhar o lado errado.

## 🎬 Exemplo passo a passo

`root = [4,2,7,1,3]`, `val = 2`

```
      4
     / \
    2   7
   / \
  1   3
```

| Passo | Nó atual | Comparação | Decisão |
|---|---|---|---|
| 1 | 4 | 2 < 4 | desce para a esquerda |
| 2 | 2 | 2 == 2 | achou! retorna a subárvore `[2,1,3]` |

Resultado final: `[2,1,3]` ✔ (bate com o enunciado — o lado direito da raiz, com o `7`, nunca foi visitado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(h) — balanceada, O(log n); no pior caso (árvore degenerada), O(n)
- **Espaço:** O(1) na versão iterativa (sem pilha de recursão) ou O(h) na versão recursiva

## 💻 Implementações

### Java (referência completa e comentada)
```java
public TreeNode searchBST(TreeNode root, int val) {
    TreeNode atual = root;

    while (atual != null && atual.val != val) {
        // a propriedade de BST decide o lado: nunca é preciso checar os dois
        atual = (val < atual.val) ? atual.left : atual.right;
    }

    return atual; // já é o nó certo, ou null se saiu da árvore sem achar
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

- Comparar os dois filhos (esquerda e direita) em vez de decidir por comparação — isso joga fora a garantia de BST e faz a busca degenerar para O(n), igual à força bruta.
- Esquecer de checar `atual != null` no loop — sem essa condição, buscar um valor que não existe (ex.: `val = 5` no exemplo 2) acaba tentando acessar `.val` de um nó nulo.
- Confundir "retornar o **valor**" com "retornar a **subárvore**" — o problema pede o nó (com toda a subárvore pendurada nele), não um booleano ou o valor isolado.
- Assumir que a árvore está balanceada — a restrição só garante que é uma BST **válida**, não que tem altura O(log n); no pior caso (inserções sempre crescentes, virando uma corrente), a busca é O(n) mesmo sendo BST.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Valor na raiz | `root = [4,2,7], val = 4` | `[4,2,7]` | caso trivial, achou na primeira comparação |
| Valor inexistente | `root = [4,2,7,1,3], val = 5` | `[]` (`null`) | testa o caminho que sai da árvore sem encontrar |
| Valor numa folha | `root = [4,2,7,1,3], val = 1` | `[1]` | subárvore de resultado é só o próprio nó, sem filhos |
| Árvore degenerada (skew) | `root = [1,null,2,null,3,null,4], val = 4` | `[4]` | garante que a busca segue corretamente numa corrente só à direita |

## 🔗 Conexões

- Problemas irmãos: [0701] Insert into a Binary Search Tree (mesma lógica de navegação por comparação, mas insere em vez de buscar), [0450] Delete Node in a BST (a operação mais complexa do trio busca/inserção/remoção)
- No backend: buscar um valor descendo por comparação é exatamente como índices B-Tree de bancos de dados localizam uma chave em O(log n) sem varrer a tabela inteira — a mesma ideia de "eliminar metade do espaço de busca a cada passo" escalada para milhões de registros em disco.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
