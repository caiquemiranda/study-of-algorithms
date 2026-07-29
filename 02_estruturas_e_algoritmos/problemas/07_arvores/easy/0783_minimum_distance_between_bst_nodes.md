# [0783] Minimum Distance Between BST Nodes

> 🔗 [LeetCode 783](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#TravessiaEmOrdem`

## 📜 O Problema

Dado o `root` de uma BST, retorne a **menor diferença** entre os valores de quaisquer dois nós diferentes da árvore.

**Exemplos:**
```
Input:  root = [4,2,6,1,3]
Output: 1

Input:  root = [1,0,48,null,null,12,49]
Output: 1
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[2, 100]` → sempre há pelo menos 2 nós, entrada pequena, qualquer O(n) resolve com folga
- `0 <= Node.val <= 10^5` → valores não-negativos, cabem em `int`
- **É o mesmo problema que [0530] Minimum Absolute Difference in BST** — o próprio enunciado do LeetCode aponta essa duplicata; a solução é idêntica, só muda o número do problema no catálogo

## 🧭 Como reconhecer o padrão

"BST + menor diferença entre dois valores quaisquer" é o mesmo raciocínio de [0530]: numa travessia **em-ordem**, os valores saem em ordem crescente, e a menor diferença entre quaisquer dois nós da árvore sempre aparece entre dois **vizinhos consecutivos** dessa sequência ordenada — nunca entre dois valores distantes.

## 🐢 Solução 1 — Força bruta (coletar tudo, ordenar, comparar)

Percorrer a árvore com qualquer travessia coletando todos os valores numa lista, ordenar essa lista, e comparar cada elemento com o seguinte para achar a menor diferença.

- Tempo: O(n log n) por causa do sort · Espaço: O(n) para a lista
- **Por que não basta:** o sort é trabalho redundante — a travessia em-ordem de uma BST já entrega os valores ordenados de graça, sem precisar de nenhum algoritmo de ordenação separado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça a travessia em-ordem e mantenha só o **valor do nó anterior** visitado. A cada novo nó, calcule `no.val - valorAnterior` (sempre não-negativo, já que em-ordem visita em ordem crescente) e atualize o mínimo se for menor que o recorde atual.

## 🎬 Exemplo passo a passo

`root = [4,2,6,1,3]`

```
      4
     / \
    2   6
   / \
  1   3
```

Travessia em-ordem: `1, 2, 3, 4, 6`

| Passo | Valor visitado | valorAnterior | Diferença | mínimo após |
|---|---|---|---|---|
| 1 | 1 | — | (nenhuma, primeiro valor) | ∞ |
| 2 | 2 | 1 | 2 - 1 = 1 | **1** |
| 3 | 3 | 2 | 3 - 2 = 1 | 1 |
| 4 | 4 | 3 | 4 - 3 = 1 | 1 |
| 5 | 6 | 4 | 6 - 4 = 2 | 1 |

Resultado final: `1` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — travessia em-ordem visita cada nó exatamente uma vez, sem sort
- **Espaço:** O(h) de pilha de recursão — não precisa de lista auxiliar guardando todos os valores

## 💻 Implementações

### Java (referência completa e comentada)
```java
private Integer valorAnterior = null;
private int menorDiferenca = Integer.MAX_VALUE;

public int minDiffInBST(TreeNode root) {
    emOrdem(root);
    return menorDiferenca;
}

private void emOrdem(TreeNode no) {
    if (no == null) return;

    emOrdem(no.left);

    // em-ordem de BST visita em ordem CRESCENTE: comparar só com o anterior já é suficiente
    if (valorAnterior != null) {
        menorDiferenca = Math.min(menorDiferenca, no.val - valorAnterior);
    }
    valorAnterior = no.val;

    emOrdem(no.right);
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

- Comparar cada nó com **todos** os outros (força bruta O(n²) ou O(n log n) com sort) achando que é necessário — a propriedade de BST + em-ordem já garante que o par mais próximo está sempre entre vizinhos consecutivos na travessia.
- Esquecer de checar `valorAnterior != null` antes da primeira comparação — no primeiro nó visitado não existe "anterior" ainda.
- Tratar este problema como diferente de [0530] e tentar uma abordagem nova do zero — reconhecer duplicatas entre problemas de catálogos como o LeetCode economiza tempo de estudo; a mesma solução resolve os dois.
- Ordenar uma lista coletada via travessia que **não** é em-ordem — só a travessia em-ordem garante saída já ordenada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Dois nós (mínimo possível) | `root = [2,1]` | `1` | caso mínimo garantido pela restrição `[2, 100]` |
| Valores bem espaçados | `root = [1,0,48,null,null,12,49]` | `1` | cobre o exemplo 2 do enunciado |
| Árvore balanceada | `root = [4,2,6,1,3]` | `1` | cobre o exemplo 1 do enunciado |
| Valores consecutivos | `root = [3,2,4]` | `1` | menor diferença possível entre inteiros distintos |

## 🔗 Conexões

- Problemas irmãos: [0530] Minimum Absolute Difference in BST (literalmente o mesmo problema, número diferente no catálogo), [0501] Find Mode in Binary Search Tree (mesma travessia em-ordem comparando com o valor anterior, mas contando repetições em vez de diferença)
- No backend: comparar apenas vizinhos numa sequência ordenada em vez de todos os pares é o mesmo princípio de detecção de anomalias em séries temporais ordenadas por tempo, e de deduplicação/merge de intervalos onde só bordas adjacentes precisam ser checadas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
