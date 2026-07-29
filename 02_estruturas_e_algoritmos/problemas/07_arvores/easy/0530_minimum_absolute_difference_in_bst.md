# [0530] Minimum Absolute Difference in BST

> 🔗 [LeetCode 530](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#TravessiaEmOrdem`

## 📜 O Problema

Dado o `root` de uma BST, retorne a **menor diferença absoluta** entre os valores de quaisquer dois nós diferentes da árvore.

**Exemplos:**
```
Input:  root = [4,2,6,1,3]
Output: 1

Input:  root = [1,0,48,null,null,12,49]
Output: 1
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[2, 10^4]` → sempre há pelo menos 2 nós (o problema faz sentido; não existe caso de árvore com 0 ou 1 nó a tratar), e precisa de solução O(n)
- `0 <= Node.val <= 10^5` → valores não-negativos cabem em `int` sem problema
- É a **mesma questão** que a [0783] Minimum Distance Between BST Nodes, conforme a nota do próprio enunciado — dois números de problema, uma solução idêntica

## 🧭 Como reconhecer o padrão

"BST + menor diferença entre dois valores quaisquer" parece pedir comparar todos os pares (O(n²)), mas a propriedade de BST entrega a resposta de graça: numa travessia **em-ordem**, os valores saem em ordem crescente, e a menor diferença entre **quaisquer** dois nós da árvore sempre aparece entre dois **vizinhos consecutivos** dessa sequência ordenada — nunca entre dois valores distantes. Comparar só pares adjacentes na travessia já é suficiente e necessário.

## 🐢 Solução 1 — Força bruta (coletar tudo, ordenar, comparar)

Percorrer a árvore com qualquer travessia (nem precisa ser em-ordem) coletando todos os valores numa lista, ordenar essa lista, e depois percorrer comparando cada elemento com o seguinte para achar a menor diferença.

- Tempo: O(n log n) por causa do sort · Espaço: O(n) para a lista
- **Por que não basta:** o sort é trabalho redundante — a travessia em-ordem de uma BST **já entrega os valores ordenados**, sem precisar de nenhum algoritmo de ordenação separado. Pagar O(n log n) para reordenar algo que a estrutura já garante ordenado é desperdiçar a propriedade central de uma BST.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça a travessia em-ordem e, em vez de guardar todos os valores numa lista, mantenha só o **valor do nó anterior** visitado. A cada novo nó, calcule `no.val - valorAnterior` (sempre não-negativo, já que em-ordem visita em ordem crescente) e atualize o mínimo se for menor que o recorde atual. Como os vizinhos na travessia em-ordem são os candidatos mais próximos possíveis em valor, comparar só consecutivos basta.

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

public int getMinimumDifference(TreeNode root) {
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

- Comparar cada nó com **todos** os outros (força bruta O(n²)) achando que é necessário — a propriedade de BST + em-ordem já garante que o par mais próximo está sempre entre vizinhos consecutivos na travessia.
- Usar `Math.abs(no.val - valorAnterior)` sem necessidade — como a em-ordem visita em ordem crescente, `no.val` é sempre ≥ `valorAnterior`, então a diferença já sai não-negativa; usar `abs` não é errado, só redundante (mas não é bug).
- Esquecer de checar `valorAnterior != null` antes da primeira comparação — no primeiro nó visitado não existe "anterior" ainda, e comparar contra um sentinela mal escolhido (como `0`) daria uma diferença falsa.
- Ordenar uma lista coletada via travessia que **não** é em-ordem, achando que economiza o sort — só a travessia em-ordem garante saída já ordenada; pré-ordem ou pós-ordem não têm essa propriedade.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Dois nós (mínimo possível) | `root = [2,1]` | `1` | caso mínimo garantido pela restrição `[2, 10^4]` |
| Valores bem espaçados | `root = [1,0,48,null,null,12,49]` | `1` | cobre o exemplo 2 do enunciado, testa com valores grandes e pequenos misturados |
| Menor diferença longe da raiz | `root = [90,69,null,49,89,null,null,null,52]` (hipotético) | diferença entre 89 e 90 ou 49 e 52 | garante que o mínimo não depende de estar perto da raiz, e sim da posição na ordem em-ordem |
| Árvore com valor 0 | `root = [1,0,2]` | `1` | valida que `0` (extremo inferior permitido) funciona normalmente na comparação |

## 🔗 Conexões

- Problemas irmãos: [0783] Minimum Distance Between BST Nodes (literalmente o mesmo problema, número diferente), [0501] Find Mode in Binary Search Tree (mesma travessia em-ordem comparando com o valor anterior, mas contando repetições em vez de diferença)
- No backend: comparar apenas vizinhos numa sequência ordenada em vez de todos os pares é o mesmo princípio de detecção de anomalias em séries temporais ordenadas por tempo, e de deduplicação/merge de intervalos onde só bordas adjacentes precisam ser checadas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
