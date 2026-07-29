# [0559] Maximum Depth of N-ary Tree

> 🔗 [LeetCode 559](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreNaria` `#DFS` `#Easy`

## 📜 O Problema

Dada uma árvore **n-ária** (cada nó pode ter **qualquer número** de filhos, não só 0, 1 ou 2), encontre sua **profundidade máxima**: o número de nós ao longo do caminho mais longo da raiz até a folha mais distante.

**Exemplos:**
```
Input:  root = [1,null,3,2,4,null,5,6]
Output: 3

Input:  root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
```

**Restrições (e o que elas denunciam):**
- Número total de nós em `[0, 10^4]` → precisa de solução O(n), mesmo com número variável de filhos por nó
- "A profundidade da árvore n-ária é ≤ 1000" → dá uma cota para a altura, mas não muda a técnica; é mais uma garantia de que a entrada não é patologicamente profunda
- O nó agora tem uma **lista de filhos** (`children: List<Node>`), não `left`/`right` fixos → a lógica de "olhar os dois lados" vira "olhar todos os filhos numa lista"

## 🧭 Como reconhecer o padrão

É exatamente a mesma pergunta de [0104] Maximum Depth of Binary Tree, só que a árvore não tem um número fixo de "lados" para comparar. Em vez de `1 + max(altura(left), altura(right))`, a resposta vira `1 + max(altura(filho) para cada filho na lista)` — o `max` de dois valores fixos vira o `max` de uma lista de tamanho variável.

## 🐢 Solução 1 — Força bruta (BFS contando níveis)

Percorrer a árvore nível a nível com uma fila, empilhando **todos** os filhos de cada nó (não só dois) e incrementando um contador de profundidade a cada nível completo processado.

- Tempo: O(n) · Espaço: O(largura da árvore)
- **Por que não basta:** mesmo raciocínio de [0104] — não está errado nem mais lento assintoticamente, mas precisa gerenciar fila, tamanho de nível e contador à parte para responder algo que a recursão resolve de forma mais direta, sem estruturas auxiliares.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pergunte a cada subárvore "qual é a sua altura?" recursivamente, como em [0104]. A diferença é que agora, em vez de comparar dois valores fixos (`left`, `right`), você percorre a **lista** `children` e pega o maior valor de altura entre todos eles. Um nó sem filhos (lista vazia) tem altura 1 (ele mesmo); um nó com filhos tem `1 + max(altura de cada filho)`.

## 🎬 Exemplo passo a passo

`root = [1,null,3,2,4,null,5,6]` → nó `1` tem filhos `[3,2,4]`; nó `3` tem filhos `[5,6]`; `2` e `4` não têm filhos.

```
        1
     /  |  \
    3   2   4
   / \
  5   6
```

| Chamada | Filhos | Alturas dos filhos | retorna |
|---|---|---|---|
| altura(5) | [] | — | 1 |
| altura(6) | [] | — | 1 |
| altura(2) | [] | — | 1 |
| altura(4) | [] | — | 1 |
| altura(3) | [5,6] | [1,1] | 1 + max(1,1) = 2 |
| altura(1) | [3,2,4] | [2,1,1] | 1 + max(2,1,1) = **3** |

Resultado final: `3` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez, independente de quantos filhos tenha
- **Espaço:** O(h) — pilha de recursão proporcional à altura da árvore, não ao número de filhos por nó

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxDepth(Node root) {
    if (root == null) return 0; // caso base: subárvore vazia não contribui em altura

    int maiorAlturaFilho = 0;
    for (Node filho : root.children) {
        // percorre TODOS os filhos, não só dois fixos como na árvore binária
        maiorAlturaFilho = Math.max(maiorAlturaFilho, maxDepth(filho));
    }

    return 1 + maiorAlturaFilho; // +1 conta o próprio nó
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

- Assumir que `children` nunca é vazio ou nulo — um nó folha numa árvore n-ária tem `children` como lista **vazia** (não `null`, na maioria das implementações do LeetCode), então o loop `for` sobre uma lista vazia já retorna `1 + 0 = 1` corretamente, sem precisar de tratamento especial.
- Tentar reaproveitar a lógica de `left`/`right` da árvore binária sem adaptar — o nó n-ário não tem esses campos, só `children`; copiar a assinatura de [0104] sem trocar por um loop quebra a compilação.
- Esquecer o caso base `root == null` — sem ele, uma árvore vazia (`root = []`) quebra ao tentar acessar `.children` de `null`.
- Confundir o **formato de serialização** do enunciado (lista com `null` separando grupos de irmãos) com a estrutura real do nó em memória — o `null` no array de entrada é só uma convenção de codificação da entrada de teste, o objeto `Node` de verdade usa uma `List<Node> children` normal, sem nulos internos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `0` | caso base sem nenhum nó |
| Um nó só, sem filhos | `root = [1]` | `1` | lista `children` vazia, `1 + max(vazio) = 1` |
| Nó com muitos filhos diretos | `root = [1,null,2,3,4,5,6]` (1 tem 5 filhos) | `2` | valida que o `max` funciona com mais de 2 filhos, não só binário |
| Árvore profunda e larga | segundo exemplo do enunciado | `5` | cobre o caso real do LeetCode, mistura largura e profundidade |

## 🔗 Conexões

- Problemas irmãos: [0104] Maximum Depth of Binary Tree (a versão binária deste mesmo problema), [0589] N-ary Tree Preorder Traversal (mesma estrutura de nó com lista de filhos, técnica de travessia diferente)
- No backend: árvores com número variável de filhos por nó modelam diretamente hierarquias de sistema de arquivos (uma pasta pode ter N arquivos/subpastas) e árvores de componentes de UI (um elemento DOM pode ter N filhos) — calcular profundidade máxima é o mesmo problema de medir o nível de aninhamento mais fundo de uma estrutura de diretórios ou de um DOM.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
