# [0543] Diameter of Binary Tree

> 🔗 [LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne o **diâmetro** da árvore: o comprimento do caminho mais longo entre quaisquer dois nós, medido em número de **arestas** (não de nós). O caminho pode ou não passar pela raiz.

**Exemplos:**
```
Input:  root = [1,2,3,4,5]
Output: 3
Explicação: 3 é o comprimento do caminho [4,2,1,3] ou [5,2,1,3]

Input:  root = [1,2]
Output: 1
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^4]` → precisa de solução O(n); recalcular altura por nó (O(n²)) fica arriscado no limite superior
- `-100 <= Node.val <= 100` → valores não importam para este problema, só a estrutura
- "pode ou não passar pela raiz" é a pegadinha central: o caminho mais longo pode estar **inteiramente dentro de uma subárvore**, longe da raiz — não basta olhar só `altura(esquerda) + altura(direita)` da raiz

## 🧭 Como reconhecer o padrão

"Caminho mais longo entre dois nós quaisquer" é a assinatura de combinar **duas perguntas numa mesma passada pós-ordem**: cada nó calcula sua própria altura (pergunta "de baixo para cima" que o pai precisa), e ao mesmo tempo, no momento em que os dois lados (esquerda e direita) já responderam, verifica se o caminho que **passa por ele** (`altura(esquerda) + altura(direita)`) é o maior visto até agora — mesmo que esse nó não seja a raiz.

## 🐢 Solução 1 — Força bruta (altura recalculada por nó)

Para cada nó da árvore, chamar uma função `altura()` separada para a subárvore esquerda e para a direita, somar os dois valores, e comparar com o maior diâmetro encontrado até agora — repetindo esse processo recursivamente para todos os nós.

- Tempo: O(n²) no pior caso · Espaço: O(h)
- **Por que não basta:** a altura de cada subárvore é recalculada do zero múltiplas vezes — uma vez ao processar o próprio nó, outra vez ao processar o pai dele, e assim sucessivamente subindo pela árvore. Numa árvore degenerada, isso é O(n) chamadas de altura, cada uma O(n) — O(n²) total, o mesmo problema de recomputação de [0110] Balanced Binary Tree.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única função recursiva que **retorna a altura** da subárvore (o contrato que o pai precisa), mas que **também** atualiza uma variável externa `melhor` com `altura(esquerda) + altura(direita)` toda vez que processa um nó — capturando o diâmetro de qualquer "ponto de junção" da árvore, não só da raiz, sem nunca recalcular a mesma altura duas vezes.

## 🎬 Exemplo passo a passo

`root = [1,2,3,4,5]`

```
      1
     / \
    2   3
   / \
  4   5
```

| Chamada | e (altura esq) | d (altura dir) | melhor após | retorna (altura) |
|---|---|---|---|---|
| altura(4) | 0 | 0 | 0 | 1 |
| altura(5) | 0 | 0 | 0 | 1 |
| altura(2) | 1 | 1 | **2** (caminho 4→2→5) | 2 |
| altura(3) | 0 | 0 | 2 | 1 |
| altura(1) | 2 | 1 | max(2, 2+1) = **3** | 3 |

Resultado final: `3` ✔ (bate com o enunciado — o diâmetro veio de um nó interno, `2`, combinado com o outro lado da raiz, não só da raiz sozinha)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez
- **Espaço:** O(h) — pilha de recursão proporcional à altura da árvore

## 💻 Implementações

### Java (referência completa e comentada)
```java
private int melhor = 0; // diâmetro em ARESTAS, atualizado como efeito colateral

public int diameterOfBinaryTree(TreeNode root) {
    altura(root);
    return melhor;
}

private int altura(TreeNode no) {
    if (no == null) return 0; // subárvore vazia: contribui 0 de altura

    int e = altura(no.left);
    int d = altura(no.right);

    // caminho que PASSA por este nó: perna esquerda + perna direita, em arestas
    melhor = Math.max(melhor, e + d);

    // contrato: devolve a altura desta subárvore para o pai usar no cálculo dele
    return 1 + Math.max(e, d);
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

- Calcular só `altura(root.left) + altura(root.right)` na raiz, achando que o diâmetro sempre passa por ela — o próprio enunciado avisa "pode ou não passar pela raiz"; o diâmetro real pode estar inteiramente dentro de uma subárvore distante.
- Confundir **arestas** com **nós** no caminho — o diâmetro é medido em arestas (conexões), não na contagem de nós visitados; um caminho com 4 nós tem 3 arestas.
- Retornar `melhor` (o diâmetro) da função `altura()` por engano, misturando os dois contratos — a função precisa devolver **altura** para o pai continuar o cálculo corretamente; o diâmetro é só um efeito colateral guardado à parte.
- Recalcular altura por nó separadamente (a força bruta) — funciona, mas é a diferença entre O(n) e O(n²) que a restrição de 10^4 nós está testando.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1]` | `0` | sem arestas possíveis, árvore trivial |
| Dois nós | `root = [1,2]` | `1` | um único caminho possível, uma aresta |
| Diâmetro passando pela raiz | `root = [1,2,3,4,5]` | `3` | cobre o exemplo do enunciado |
| Diâmetro fora da raiz (numa subárvore) | `root = [1,2,null,3,null,4]` (corrente à esquerda) | `3` | garante que o `melhor` captura o caminho mesmo sem envolver a raiz diretamente |

## 🔗 Conexões

- Problemas irmãos: [0104] Maximum Depth of Binary Tree (o cálculo de altura reaproveitado aqui), [0110] Balanced Binary Tree (mesma técnica de "combinar duas perguntas numa passada pós-ordem só", já documentada nos fundamentos da categoria)
- No backend: essa técnica de "atualizar um recorde global como efeito colateral de uma recursão que retorna outra coisa" aparece em cálculo de latência máxima ponta-a-ponta em grafos de dependência de microsserviços, e em análise de caminho crítico (critical path) em grafos de tarefas de um pipeline de build.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
