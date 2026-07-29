# [0101] Symmetric Tree

> 🔗 [LeetCode 101](https://leetcode.com/problems/symmetric-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, verifique se ela é um **espelho de si mesma** em torno do centro (simétrica).

**Exemplos:**
```
Input:  root = [1,2,2,3,4,4,3]
Output: true

Input:  root = [1,2,2,null,3,null,3]
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 1000]` → entrada pequena, O(n) é mais que suficiente
- `-100 <= Node.val <= 100` → valores cabem em `int`
- Follow-up "resolva recursivamente e iterativamente" → sinaliza que ambas as abordagens têm o mesmo valor didático aqui; o Java de referência usa a recursiva por ser mais direta de justificar

## 🧭 Como reconhecer o padrão

"Espelho de si mesma" é uma comparação entre **duas metades da mesma árvore**: a subárvore esquerda da raiz precisa ser o espelho exato da subárvore direita. Isso reduz o problema a "isSameTree, mas comparando left com o mirror de right" — uma variação de [0100] Same Tree em que, em vez de comparar `left` com `left` e `right` com `right`, você compara `left` com `right` **trocado**.

## 🐢 Solução 1 — Força bruta (construir a árvore espelhada e comparar)

Criar uma cópia completa da árvore com `left` e `right` trocados em cada nó (uma árvore nova, alocando nós), depois comparar essa cópia com a árvore original usando a lógica de "mesma árvore".

- Tempo: O(n) · Espaço: O(n) — tanto para a árvore espelhada nova quanto para a pilha de recursão da construção
- **Por que não basta:** funciona, mas aloca uma árvore inteira só para descartá-la logo em seguida — n nós novos de memória para responder uma pergunta que não precisa de nenhuma estrutura extra, só de comparar os nós certos na ordem certa.

## 💡 Solução 2 — A ideia otimizada (intuição)

Não construa nada: compare `root.left` com `root.right` usando uma função que recebe **dois** nós e verifica se um é o espelho do outro — dois nós são espelho quando têm o mesmo valor, o `left` de um é espelho do `right` do outro, **e** o `right` de um é espelho do `left` do outro (comparação cruzada, não posição a posição).

## 🎬 Exemplo passo a passo

`root = [1,2,2,3,4,4,3]`

```
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

| Passo | Chamada | Comparação cruzada | Resultado parcial |
|---|---|---|---|
| 1 | ehEspelho(2, 2) [nós do nível 1] | val 2==2; compara (2.left,2.right) cruzado | aguardando |
| 2 | ehEspelho(3, 3) [2.left com 2.right] | val 3==3; ambos sem filhos → `true` | ✔ |
| 3 | ehEspelho(4, 4) [2.right com 2.left] | val 4==4; ambos sem filhos → `true` | ✔ |
| 4 | volta ao passo 1 | ✔ e ✔ → `true` | `true` |

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado uma vez, cada comparação é O(1)
- **Espaço:** O(h) — pilha de recursão limitada pela altura da árvore; pior caso O(n) numa árvore degenerada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isSymmetric(TreeNode root) {
    if (root == null) return true; // árvore vazia é trivialmente simétrica
    return ehEspelho(root.left, root.right);
}

private boolean ehEspelho(TreeNode a, TreeNode b) {
    if (a == null && b == null) return true;  // ambos ausentes: simétrico até aqui
    if (a == null || b == null) return false; // só um ausente: quebrou a simetria
    if (a.val != b.val) return false;         // valores diferentes na posição espelhada

    // comparação CRUZADA: esquerda de "a" precisa espelhar direita de "b", e vice-versa
    return ehEspelho(a.left, b.right) && ehEspelho(a.right, b.left);
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

- Comparar `a.left` com `b.left` (posição a posição, como em "mesma árvore") em vez da comparação **cruzada** `a.left` com `b.right` — isso testa se as duas metades são idênticas, não se são espelho uma da outra.
- Esquecer que a chamada inicial já começa comparando `root.left` com `root.right`, não `root` com ele mesmo — comparar a raiz consigo mesma sempre daria `true` trivialmente e nunca checaria nada.
- Confundir "espelho" com "igual": `[1,2,2]` é simétrico, mas `[1,2,3]` (mesmos filhos, valores diferentes) não é — o valor nos dois lados precisa bater, não só a forma.
- Achar que basta comparar as travessias em-ordem da esquerda e da direita invertida — funciona por coincidência em alguns casos, mas não captura estrutura corretamente em árvores com nulos assimétricos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1]` | `true` | sem filhos, `ehEspelho(null, null)` |
| Assimetria por posição de nulo | `root = [1,2,2,null,3,null,3]` | `false` | mesmos valores, mas um `3` está à direita da esquerda e o outro à direita da direita — cobre o exemplo 2 do enunciado |
| Dois níveis simétricos | `root = [1,2,2]` | `true` | caso simples sem netos |
| Valores iguais, forma diferente | `root = [1,2,2,3,null,null,3]` vs conceito | `false` | garante que a comparação cruzada pega nulo faltando de um lado só |

## 🔗 Conexões

- Problemas irmãos: [0100] Same Tree (a base: comparação de dois nós, mas posição a posição em vez de cruzada), [0226] Invert Binary Tree (inverter e depois comparar com o original é outra forma válida, porém mais cara, de pensar sobre simetria)
- No backend: checagem de simetria estrutural aparece em validação de layouts de UI responsivos espelhados (RTL/LTR) e em comparação de árvores de decisão ou regras de negócio que precisam ser balanceadas/simétricas por design.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
