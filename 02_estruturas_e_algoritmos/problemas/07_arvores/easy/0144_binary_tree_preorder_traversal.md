# [0144] Binary Tree Preorder Traversal

> 🔗 [LeetCode 144](https://leetcode.com/problems/binary-tree-preorder-traversal/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne a **travessia pré-ordem** (preorder) dos valores dos seus nós: visita o nó atual, depois a subárvore esquerda, depois a subárvore direita.

**Exemplos:**
```
Input:  root = [1,null,2,3]
Output: [1,2,3]

Input:  root = []
Output: []

Input:  root = [1]
Output: [1]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 100]` → entrada pequena, o desafio é o follow-up (fazer sem recursão), não a performance
- `-100 <= Node.val <= 100` → valores cabem em `int`
- Follow-up "faça iterativamente" → mesmo espírito de [0094] Inorder Traversal, mas pré-ordem é a **mais simples** das três de fazer iterativa (não precisa "descer até o fim" antes de registrar o valor)

## 🧭 Como reconhecer o padrão

"Pré-ordem" processa o nó **antes** de olhar os filhos: nó → esquerda → direita. É a ordem natural para "copiar"/"serializar" uma árvore, porque ao reconstruí-la a partir da sequência, o primeiro valor sempre é a raiz.

## 🐢 Solução 1 — Força bruta (recursão direta)

Função recursiva: adiciona `node.val` à lista, visita `left`, visita `right`. Caso base: nó nulo não faz nada.

- Tempo: O(n) · Espaço: O(h) de pilha de chamadas
- **Por que não basta:** mesmo raciocínio de [0094] Inorder — funciona, mas depende da pilha de chamadas do runtime, que o follow-up pede para não usar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use uma pilha explícita: empilhe a raiz; em cada iteração, desempilhe um nó, **registre o valor imediatamente** (diferente da em-ordem, aqui não é preciso "descer" antes de registrar), e empilhe primeiro o filho **direito**, depois o **esquerdo** — assim, quando a pilha desempilhar de novo, o esquerdo sai primeiro (LIFO), preservando a ordem nó→esquerda→direita.

## 🎬 Exemplo passo a passo

`root = [1,null,2,3]` → `1` tem filho direito `2`; `2` tem filho esquerdo `3`.

```
1
 \
  2
 /
3
```

| Passo | Ação | Pilha (topo à direita) | Saída |
|---|---|---|---|
| 1 | empilha raiz | `[1]` | `[]` |
| 2 | desempilha 1, registra, empilha direito(2) depois esquerdo(nenhum) | `[2]` | `[1]` |
| 3 | desempilha 2, registra, empilha direito(nenhum) depois esquerdo(3) | `[3]` | `[1,2]` |
| 4 | desempilha 3, registra, sem filhos | `[]` | `[1,2,3]` |
| 5 | pilha vazia → termina | `[]` | `[1,2,3]` |

Resultado final: `[1,2,3]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é empilhado e desempilhado exatamente uma vez
- **Espaço:** O(h) — pilha guarda no máximo o caminho até o nó mais fundo em processamento

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> resultado = new ArrayList<>();
    if (root == null) return resultado;

    Deque<TreeNode> pilha = new ArrayDeque<>();
    pilha.push(root);

    while (!pilha.isEmpty()) {
        TreeNode no = pilha.pop();
        resultado.add(no.val); // registra ANTES de olhar os filhos: é isso que faz ser pré-ordem

        // empilha direito primeiro para que o esquerdo saia no topo (LIFO) na próxima iteração
        if (no.right != null) pilha.push(no.right);
        if (no.left != null) pilha.push(no.left);
    }

    return resultado;
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

- Empilhar `left` antes de `right` — inverte a ordem de saída, porque a pilha é LIFO: o último empilhado é o primeiro a sair. Para o esquerdo sair primeiro, ele precisa ser empilhado **depois** do direito.
- Registrar o valor **depois** de desempilhar os filhos, em vez de imediatamente ao desempilhar o próprio nó — produz uma ordem diferente da pré-ordem.
- Confundir com a versão iterativa de em-ordem ([0094]) e tentar "descer pela esquerda" antes de registrar — em pré-ordem isso é desnecessário, o valor já pode ser registrado assim que o nó é desempilhado.
- Esquecer de checar `no.right != null` / `no.left != null` antes de empilhar — empilhar `null` sem querer faz o `pop()` seguinte quebrar com `NullPointerException`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | retorno antecipado, pilha nunca é usada |
| Um nó só | `root = [1]` | `[1]` | caso base, sem filhos |
| Só filhos à esquerda (skew) | `root = [3,2,1]` (2 é left de 3, 1 é left de 2) | `[3,2,1]` | testa que a ordem nó→esquerda se mantém numa corrente |
| Árvore com ambos os lados | `root = [1,2,3,4,5]` | `[1,2,4,5,3]` | garante que a pilha alterna corretamente entre ramos esquerdo e direito |

## 🔗 Conexões

- Problemas irmãos: [0094] Binary Tree Inorder Traversal (mesma técnica de pilha, mas precisa "descer" antes de registrar), [0145] Binary Tree Postorder Traversal (a mais complexa das três de fazer iterativa), [0105] Construct Binary Tree from Preorder and Inorder Traversal (usa a propriedade "pré-ordem sempre começa pela raiz" para reconstruir a árvore)
- No backend: pré-ordem é a ordem usada para **serializar** uma árvore de forma que ela possa ser reconstruída de forma unívoca (junto com marcadores de nulo) — é a base de formatos de serialização de AST em compiladores e de estruturas de diretórios (a raiz sempre aparece antes de seu conteúdo).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
