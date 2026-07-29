# [0897] Increasing Order Search Tree

> 🔗 [LeetCode 897](https://leetcode.com/problems/increasing-order-search-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#TravessiaEmOrdem`

## 📜 O Problema

Dado o `root` de uma BST, rearranje a árvore **em-ordem** de forma que o nó mais à esquerda vire a nova raiz, e todo nó não tenha filho esquerdo, só um filho direito — formando uma corrente que segue a ordem crescente.

**Exemplos:**
```
Input:  root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Input:  root = [5,1,7]
Output: [1,null,5,null,7]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 100]` → entrada pequena, qualquer O(n) resolve com folga
- `0 <= Node.val <= 1000` → valores não-negativos, cabem em `int`
- "todo nó não tem filho esquerdo, só um filho direito" → a árvore resultante é essencialmente uma **lista ligada** disfarçada de árvore, ordenada em ordem crescente

## 🧭 Como reconhecer o padrão

"Rearranjar uma BST em-ordem" é exatamente a travessia em-ordem de [0094] Inorder Traversal, mas em vez de coletar os valores numa lista de saída, você **religa os próprios nós** conforme a travessia avança, formando a corrente diretamente.

## 🐢 Solução 1 — Força bruta (coletar valores, construir árvore nova)

Fazer uma travessia em-ordem coletando todos os valores numa lista. Depois, construir uma árvore **totalmente nova**, alocando um `TreeNode` para cada valor da lista e ligando cada um como filho direito do anterior.

- Tempo: O(n) · Espaço: O(n) para a lista intermediária **mais** O(n) para os nós novos alocados
- **Por que não basta:** os nós originais já existem e só precisam ser **religados** na ordem certa — alocar uma árvore inteira nova quando os nós de origem já têm tudo que é preciso (o valor) é desperdiçar memória à toa.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça a travessia em-ordem, mas em vez de só ler `node.val`, **desconecte** o `left` do nó atual (`no.left = null`) e **plugue-o** como o `right` do último nó processado (mantendo um ponteiro `anterior`). Como a travessia em-ordem já visita em ordem crescente, cada nó visitado se torna naturalmente o próximo elo da corrente — sem lista intermediária, sem nós novos.

## 🎬 Exemplo passo a passo

`root = [5,1,7]`

```
    5
   / \
  1   7
```

| Passo | Nó visitado (em-ordem) | Ação | anterior.right após | anterior após |
|---|---|---|---|---|
| 1 | 1 | `1.left = null`; vira a nova raiz (`anterior` ainda não existe) | — | 1 |
| 2 | 5 | `5.left = null`; `anterior.right = 5` (1 aponta para 5) | `1 → 5` | 5 |
| 3 | 7 | `7.left = null`; `anterior.right = 7` (5 aponta para 7) | `5 → 7` | 7 |

Resultado final: `1 → 5 → 7` (só filhos direitos) → `[1,null,5,null,7]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado e religado exatamente uma vez
- **Espaço:** O(h) de pilha de recursão — nenhuma lista intermediária, nenhum nó novo alocado; a saída reaproveita os nós de entrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
private TreeNode anterior; // último nó já religado na corrente

public TreeNode increasingBST(TreeNode root) {
    TreeNode dummy = new TreeNode(0); // nó auxiliar: seu .right vai virar a resposta real
    anterior = dummy;
    emOrdem(root);
    return dummy.right;
}

private void emOrdem(TreeNode no) {
    if (no == null) return;

    emOrdem(no.left);

    // desconecta a esquerda e pluga este nó como o PRÓXIMO da corrente
    no.left = null;
    anterior.right = no;
    anterior = no;

    emOrdem(no.right); // ainda precisa visitar a direita ORIGINAL antes de ela ser sobrescrita
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

- Chamar `emOrdem(no.right)` **depois** de já ter sobrescrito `no.right` (religando para o próximo nó da corrente) — a ordem certa é: desconectar `left`, religar `anterior.right = no`, **e só então** recursar para `no.right`, porque nesse ponto `no.right` ainda aponta para a subárvore direita original (a religação ainda não aconteceu para esse campo).
- Esquecer de zerar `no.left = null` — sem isso, o nó final ainda tem uma referência (agora "fantasma") para sua antiga subárvore esquerda, violando a exigência de "nenhum nó tem filho esquerdo".
- Não usar um nó `dummy` (auxiliar) no início — sem ele, é preciso tratar o primeiro nó da corrente (a nova raiz) como um caso especial separado, porque não existe "anterior" ainda no início da travessia.
- Construir uma árvore nova (a força bruta) quando os nós originais já podem ser reaproveitados — funciona, mas desperdiça memória.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1]` | `[1]` | caso base, corrente de tamanho 1 |
| Só filho esquerdo (skew) | `root = [3,2,null,1]` | `[1,null,2,null,3]` | testa a religação numa árvore já bem desbalanceada à esquerda |
| Árvore balanceada | `root = [5,1,7]` | `[1,null,5,null,7]` | cobre o exemplo 2 do enunciado |
| Árvore maior com múltiplos níveis | exemplo 1 do enunciado | corrente completa em ordem crescente | garante que a religação funciona corretamente em profundidade maior |

## 🔗 Conexões

- Problemas irmãos: [0094] Binary Tree Inorder Traversal (a mesma travessia, mas religando nós em vez de coletar valores), [0114] Flatten Binary Tree to Linked List (mesma ideia de "achatar" uma árvore numa corrente, mas usando pré-ordem em vez de em-ordem)
- No backend: transformar uma estrutura em árvore numa lista ligada ordenada, reaproveitando os nós existentes, é o mesmo princípio usado em serialização de árvores de índice para exportação sequencial (ex.: exportar uma B-Tree de banco de dados como um stream ordenado sem duplicar os dados em memória).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
