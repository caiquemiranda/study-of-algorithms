# [0104] Maximum Depth of Binary Tree

> 🔗 [LeetCode 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne sua **profundidade máxima**: o número de nós ao longo do caminho mais longo da raiz até a folha mais distante.

**Exemplos:**
```
Input:  root = [3,9,20,null,null,15,7]
Output: 3

Input:  root = [1,null,2]
Output: 2
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → precisa de solução O(n); qualquer coisa que recompute trabalho por nó (O(n²)) fica arriscado no limite superior
- `-100 <= Node.val <= 100` → os valores em si não importam para este problema, só a estrutura (posições de nós e nulos)
- Árvore vazia é caso válido (`root = []`, profundidade 0) → precisa de caso base explícito, não assumir que sempre existe pelo menos um nó

## 🧭 Como reconhecer o padrão

"Profundidade máxima / altura" é a pergunta pós-ordem mais direta que existe: a altura de uma árvore é `1 + max(altura da esquerda, altura da direita)`. Cada nó só precisa saber a altura dos dois filhos para responder a própria — é o "contrato" clássico da recursão em árvore descrito nos fundamentos da categoria.

## 🐢 Solução 1 — Força bruta (BFS contando níveis)

Percorrer a árvore nível a nível com uma fila, incrementando um contador de profundidade a cada nível completo processado (usando o truque de "congelar o tamanho da fila" antes do loop interno).

- Tempo: O(n) · Espaço: O(largura da árvore), pior caso O(n) numa árvore completa
- **Por que não basta:** não é que esteja errado ou lento — dá a resposta certa em O(n) igual à solução ótima. O problema é o **custo de código e estado**: precisa gerenciar fila, tamanho de nível e contador à parte, para responder uma pergunta que a recursão pós-ordem resolve em 3 linhas sem estrutura auxiliar nenhuma.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pergunte a cada subárvore "qual é a sua altura?" recursivamente. Um nó nulo tem altura 0 (caso base). Um nó real tem altura `1 + max(altura(esquerda), altura(direita))` — o "+1" conta o próprio nó, e o `max` escolhe o galho mais profundo entre os dois lados.

## 🎬 Exemplo passo a passo

`root = [3,9,20,null,null,15,7]`

```
      3
     / \
    9  20
      /  \
    15    7
```

| Chamada | altura(esq) | altura(dir) | retorna |
|---|---|---|---|
| altura(9) | 0 | 0 | 1 |
| altura(15) | 0 | 0 | 1 |
| altura(7) | 0 | 0 | 1 |
| altura(20) | 1 | 1 | 2 |
| altura(3) | 1 | 2 | **3** |

Resultado final: `3` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez
- **Espaço:** O(h) — pilha de recursão proporcional à altura; pior caso O(n) numa árvore degenerada (todos os nós numa linha)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxDepth(TreeNode root) {
    if (root == null) return 0; // caso base: subárvore vazia não contribui em altura

    int esquerda = maxDepth(root.left);
    int direita = maxDepth(root.right);

    // +1 conta o próprio nó; max escolhe o galho mais profundo entre os dois lados
    return 1 + Math.max(esquerda, direita);
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

- Retornar `0` em vez de `1` para um nó folha sem filhos — o nó folha em si conta como profundidade 1, o `+1` da recursão já cuida disso automaticamente ao chamar com `left`/`right` nulos.
- Confundir **profundidade** (raiz → nó) com o que este problema pede, que na prática é a **altura** da árvore inteira (maior profundidade entre todas as folhas) — os dois conceitos se equivalem aqui só porque a pergunta é sobre a folha mais distante.
- Em árvore degenerada (uma linha de 10^4 nós), a recursão pode estourar a pilha de chamadas em algumas linguagens/configurações — se isso acontecer na prática, a versão BFS (força bruta) vira a alternativa segura, apesar de mais verbosa.
- Esquecer o caso base `root == null` retornando `0` — sem ele, uma árvore vazia (`root = []`) quebra com `NullPointerException` em vez de retornar `0`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `0` | testa o caso base isolado, sem nenhum nó |
| Um nó só | `root = [1]` | `1` | folha única, `1 + max(0,0)` |
| Só filhos à direita (skew) | `root = [1,null,2]` | `2` | cobre o exemplo 2 do enunciado, garante que ausência de filho esquerdo não quebra o `max` |
| Árvore perfeitamente balanceada | `root = [1,2,3,4,5,6,7]` | `3` | ambos os lados contribuem igualmente, valida o `max` em caso simétrico |

## 🔗 Conexões

- Problemas irmãos: [0111] Minimum Depth of Binary Tree (a mesma pergunta, mas com a pegadinha de exigir folha real, não só o mínimo entre os dois lados), [0543] Diameter of Binary Tree (reaproveita este mesmo cálculo de altura para achar o caminho mais longo entre duas folhas quaisquer, não só raiz-folha)
- No backend: calcular a "profundidade" de uma hierarquia aparece em validação de árvores de categorias de e-commerce (evitar aninhamento excessivo), em análise de profundidade de call stacks de tracing distribuído, e em detecção de árvores de decisão desbalanceadas em sistemas de regras.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
