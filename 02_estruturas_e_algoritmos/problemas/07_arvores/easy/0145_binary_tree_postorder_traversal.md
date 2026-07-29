# [0145] Binary Tree Postorder Traversal

> 🔗 [LeetCode 145](https://leetcode.com/problems/binary-tree-postorder-traversal/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne a **travessia pós-ordem** (postorder) dos valores dos seus nós: visita a subárvore esquerda, depois a subárvore direita, depois o nó atual.

**Exemplos:**
```
Input:  root = [1,null,2,3]
Output: [3,2,1]

Input:  root = []
Output: []

Input:  root = [1]
Output: [1]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 100]` → entrada pequena, o desafio é o follow-up (fazer sem recursão), não a performance
- `-100 <= Node.val <= 100` → valores cabem em `int`
- Follow-up "faça iterativamente" → pós-ordem é a **mais difícil** das três travessias de fazer iterativa, porque o nó é registrado por último, depois de já ter "voltado" dos dois filhos

## 🧭 Como reconhecer o padrão

"Pós-ordem" processa o nó **depois** dos dois filhos: esquerda → direita → nó. É a ordem natural para "o pai precisa do resultado dos filhos antes de decidir algo" — soma de subárvore, altura, exclusão segura de nós (deletar filhos antes do pai).

## 🐢 Solução 1 — Força bruta (recursão direta)

Função recursiva: visita `left`, visita `right`, adiciona `node.val` à lista. Caso base: nó nulo não faz nada.

- Tempo: O(n) · Espaço: O(h) de pilha de chamadas
- **Por que não basta:** mesmo raciocínio de [0094] e [0144] — correta, mas depende da pilha de chamadas do runtime, que o follow-up pede para não usar.

## 💡 Solução 2 — A ideia otimizada (intuição)

O truque mais simples: faça uma travessia iterativa "nó → direita → esquerda" (o espelho invertido da pré-ordem — empilhando **esquerda** antes de **direita**, e registrando o valor ao desempilhar) e depois **inverta o resultado**. `nó, direita, esquerda` invertido é exatamente `esquerda, direita, nó` — que é a definição de pós-ordem. É a mesma pilha explícita de [0144], só muda a ordem de empilhar os filhos e um passo final de reversão.

## 🎬 Exemplo passo a passo

`root = [1,null,2,3]` → `1` tem filho direito `2`; `2` tem filho esquerdo `3`.

```
1
 \
  2
 /
3
```

| Passo | Ação | Pilha (topo à direita) | Saída (nó-direita-esquerda) |
|---|---|---|---|
| 1 | empilha raiz | `[1]` | `[]` |
| 2 | desempilha 1, registra, empilha esquerdo(nenhum) depois direito(2) | `[2]` | `[1]` |
| 3 | desempilha 2, registra, empilha esquerdo(3) depois direito(nenhum) | `[3]` | `[1,2]` |
| 4 | desempilha 3, registra, sem filhos | `[]` | `[1,2,3]` |
| 5 | pilha vazia → inverte a saída | — | `[3,2,1]` |

Resultado final: `[3,2,1]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é empilhado e desempilhado uma vez, mais O(n) para inverter a lista no final
- **Espaço:** O(h) para a pilha, mais O(n) para a lista de resultado (que seria necessária de qualquer forma para a resposta)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> postorderTraversal(TreeNode root) {
    LinkedList<Integer> resultado = new LinkedList<>(); // LinkedList permite addFirst em O(1)
    if (root == null) return resultado;

    Deque<TreeNode> pilha = new ArrayDeque<>();
    pilha.push(root);

    while (!pilha.isEmpty()) {
        TreeNode no = pilha.pop();
        resultado.addFirst(no.val); // insere no INÍCIO: monta a lista já invertida, sem precisar de reverse() no final

        // empilha esquerdo primeiro para que o direito saia no topo (LIFO) na próxima iteração
        // (é o espelho exato da pré-ordem, que empilhava direito antes de esquerdo)
        if (no.left != null) pilha.push(no.left);
        if (no.right != null) pilha.push(no.right);
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

- Esquecer de inverter o resultado (ou de usar `addFirst`) — sem isso, a saída fica na ordem "nó, direita, esquerda", que não é pós-ordem.
- Empilhar `right` antes de `left` (copiando [0144] sem ajustar) — isso produz a ordem errada quando combinado com a inversão; a ordem de empilhar aqui é o espelho da pré-ordem, não a mesma.
- Achar que "usar `addFirst` numa `ArrayList`" é equivalente a usar `LinkedList` — `ArrayList.add(0, x)` é O(n) por chamada (desloca todos os elementos), o que faria a solução inteira virar O(n²); `LinkedList.addFirst` é O(1).
- Tentar generalizar direto do template de em-ordem ([0094], que "desce até o fim antes de registrar") — pós-ordem iterativa **não** usa esse padrão de descida; é mais fácil pensar nela como pré-ordem invertida do que como uma variação da em-ordem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | retorno antecipado, pilha nunca é usada |
| Um nó só | `root = [1]` | `[1]` | caso base, sem filhos |
| Só filhos à direita (skew) | `root = [1,null,2,null,3]` | `[3,2,1]` | testa a inversão numa corrente simples |
| Árvore com ambos os lados | `root = [1,2,3,4,5]` | `[4,5,2,3,1]` | garante que a ordem esquerda-direita-nó se mantém após a inversão, mesmo com ramos em ambos os lados |

## 🔗 Conexões

- Problemas irmãos: [0144] Binary Tree Preorder Traversal (o espelho exato desta solução, antes da inversão), [0094] Binary Tree Inorder Traversal (a terceira travessia clássica, com técnica iterativa diferente), [0543] Diameter of Binary Tree (usa a mesma ideia de "processar o nó só depois de saber a resposta dos filhos")
- No backend: pós-ordem é a ordem certa para **liberar recursos hierárquicos com segurança** — deletar um diretório só depois de deletar todo o conteúdo dele, ou desalocar nós de uma árvore de dependências só depois que todos os dependentes já foram processados (ordem de destruição/cleanup em sistemas de build).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
