# [0110] Balanced Binary Tree

> 🔗 [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado um `root` de árvore binária, determine se ela é **balanceada em altura**: para **todo** nó da árvore, a diferença de altura entre as subárvores esquerda e direita não pode ser maior que 1.

**Exemplos:**
```
Input:  root = [3,9,20,null,null,15,7]
Output: true

Input:  root = [1,2,2,3,3,null,null,4,4]
Output: false

Input:  root = []
Output: true
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 5000]` → O(n²) (5000² = 25 milhões) ainda passaria no tempo, mas é o tipo de restrição que existe justamente para separar quem entendeu a otimização de quem não entendeu
- `-10^4 <= Node.val <= 10^4` → valores não importam para este problema, só a forma da árvore
- "para **todo** nó" é a palavra-chave: não basta checar a raiz, cada subárvore precisa satisfazer a condição recursivamente

## 🧭 Como reconhecer o padrão

"Balanceada" é sempre uma pergunta sobre **altura de subárvores**, então o instinto certo é reaproveitar o cálculo de altura (como em [0104] Maximum Depth) e, no caminho de volta da recursão (pós-ordem), comparar a altura da esquerda com a da direita em cada nó — não só na raiz.

## 🐢 Solução 1 — Força bruta (recalcular altura a cada nó)

Para cada nó da árvore, chamar uma função `altura()` separada para a subárvore esquerda e outra para a direita, comparar as duas, e recursivamente repetir essa checagem para todos os nós da árvore.

- Tempo: O(n²) no pior caso · Espaço: O(h)
- **Por que não basta:** o mesmo nó tem sua altura recalculada do zero múltiplas vezes — uma vez como parte da checagem do seu pai, outra vez como parte da checagem do avô, e assim por diante. Numa árvore degenerada (praticamente uma lista), isso vira O(n) chamadas de altura, cada uma O(n) — O(n²) total, o clássico "trabalho refeito à toa" que a restrição de 5000 nós já deixa perigoso.

## 💡 Solução 2 — A ideia otimizada (intuição)

Combine as duas perguntas ("qual a altura?" e "está balanceada?") numa única passada pós-ordem: a função retorna a altura da subárvore, mas se em qualquer ponto detectar desbalanceamento, propaga um valor sentinela (`-1`) para cima em vez da altura real — assim que um `-1` aparece, toda a cadeia de chamadas acima só precisa checar "recebi -1?" e repassar, sem nunca mais recalcular nada.

## 🎬 Exemplo passo a passo

`root = [3,9,20,null,null,15,7]`

```
      3
     / \
    9  20
      /  \
    15    7
```

| Chamada | altura(esq) | altura(dir) | \|dif\| ≤ 1? | retorna |
|---|---|---|---|---|
| verifica(9) | 0 | 0 | sim | 1 |
| verifica(15) | 0 | 0 | sim | 1 |
| verifica(7) | 0 | 0 | sim | 1 |
| verifica(20) | 1 | 1 | sim | 2 |
| verifica(3) | 1 | 2 | sim (\|1-2\|=1) | 3 |

Nenhum `-1` propagado → árvore balanceada.

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez, a altura e a checagem de balanceamento são calculadas juntas
- **Espaço:** O(h) — pilha de recursão proporcional à altura da árvore

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isBalanced(TreeNode root) {
    return altura(root) != -1; // -1 é o sentinela: "já achei desbalanceamento em algum lugar"
}

private int altura(TreeNode no) {
    if (no == null) return 0; // subárvore vazia: altura 0, trivialmente balanceada

    int esquerda = altura(no.left);
    if (esquerda == -1) return -1; // já desbalanceado mais embaixo: propaga sem checar mais nada

    int direita = altura(no.right);
    if (direita == -1) return -1; // idem para o lado direito

    if (Math.abs(esquerda - direita) > 1) return -1; // desbalanceou AQUI, neste nó

    return 1 + Math.max(esquerda, direita); // ainda balanceado: devolve a altura real
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

- Checar o balanceamento só na raiz (`abs(altura(root.left) - altura(root.right)) <= 1`) sem verificar recursivamente cada subárvore — o exemplo 2 do enunciado (`[1,2,2,3,3,null,null,4,4]`) tem a raiz aparentemente equilibrada, mas um nó mais embaixo (`2`) não está.
- Usar `0` como sentinela de erro em vez de `-1` — `0` é uma altura válida (nó nulo), então confundiria "vazio" com "desbalanceado".
- Recalcular a altura da esquerda e da direita em funções separadas por nó (a força bruta) — funciona, mas é a diferença entre O(n) e O(n²) que a restrição de 5000 nós está testando.
- Esquecer de propagar o `-1` assim que ele aparece de um lado, calculando o outro lado mesmo assim — não quebra a corretude, mas desperdiça trabalho que o early-return evitaria.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `true` | caso base, altura 0 é trivialmente balanceada |
| Um nó só | `root = [1]` | `true` | sem filhos, nada para desbalancear |
| Desbalanceamento na raiz | `root = [1,2,null,3]` | `false` | esquerda tem altura 2, direita tem altura 0 |
| Desbalanceamento longe da raiz | `root = [1,2,2,3,3,null,null,4,4]` | `false` | a raiz parece balanceada, mas um nó filho não está — cobre o exemplo 2 do enunciado |

## 🔗 Conexões

- Problemas irmãos: [0104] Maximum Depth of Binary Tree (o cálculo de altura reaproveitado aqui), [0543] Diameter of Binary Tree (mesma técnica de "combinar duas perguntas numa passada pós-ordem só")
- No backend: a ideia de "propagar um sentinela para abortar cedo em vez de recalcular tudo" aparece em validações de árvores de índice (garantir que uma B-Tree se mantém balanceada após inserções/remoções) e em pipelines de validação que precisam falhar rápido (fail-fast) sem processar o restante da estrutura.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
