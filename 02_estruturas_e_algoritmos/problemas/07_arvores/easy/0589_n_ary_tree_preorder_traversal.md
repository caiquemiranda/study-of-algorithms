# [0589] N-ary Tree Preorder Traversal

> 🔗 [LeetCode 589](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreNaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore **n-ária** (cada nó tem uma lista `children` com qualquer número de filhos), retorne a **travessia pré-ordem** dos valores dos seus nós: visita o nó atual, depois cada filho, da esquerda para a direita, recursivamente.

**Exemplos:**
```
Input:  root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Input:  root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → precisa de solução O(n)
- `0 <= Node.val <= 10^4` → valores não-negativos, cabem em `int`
- Altura da árvore ≤ 1000 → cota razoável para não estourar pilha de recursão facilmente
- Follow-up "faça iterativamente" → mesmo espírito de [0144] Binary Tree Preorder Traversal, mas agora com **múltiplos** filhos por nó em vez de só dois

## 🧭 Como reconhecer o padrão

É a mesma ideia de [0144] Binary Tree Preorder Traversal — nó, depois filhos, da esquerda para a direita — só que "os filhos" agora é uma lista de tamanho variável (`children`) em vez de dois campos fixos `left`/`right`.

## 🐢 Solução 1 — Força bruta (recursão direta)

Função recursiva: adiciona `node.val` à lista, depois percorre `node.children` em ordem, chamando a recursão para cada um. Caso base: nó nulo (ou lista de filhos vazia) não faz mais nada.

- Tempo: O(n) · Espaço: O(h) de pilha de chamadas
- **Por que não basta:** mesmo raciocínio de [0144] — correta, mas depende da pilha de chamadas do runtime, que o follow-up pede para não usar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use uma pilha explícita, como em [0144]: empilhe a raiz; em cada iteração, desempilhe um nó, registre seu valor imediatamente, e empilhe **todos os filhos dele em ordem reversa** (do último para o primeiro). Como a pilha é LIFO, empilhar em ordem reversa garante que o **primeiro** filho da lista original seja o **próximo** a ser desempilhado — preservando a ordem "esquerda para direita" mesmo com N filhos.

## 🎬 Exemplo passo a passo

`root = [1,null,3,2,4,null,5,6]` → nó `1` tem filhos `[3,2,4]`; nó `3` tem filhos `[5,6]`.

```
        1
     /  |  \
    3   2   4
   / \
  5   6
```

| Passo | Ação | Pilha (topo à direita) | Saída |
|---|---|---|---|
| 1 | empilha raiz | `[1]` | `[]` |
| 2 | desempilha 1, registra, empilha filhos [3,2,4] **invertidos**: 4,2,3 | `[4,2,3]` | `[1]` |
| 3 | desempilha 3, registra, empilha filhos [5,6] invertidos: 6,5 | `[4,2,6,5]` | `[1,3]` |
| 4 | desempilha 5, registra, sem filhos | `[4,2,6]` | `[1,3,5]` |
| 5 | desempilha 6, registra, sem filhos | `[4,2]` | `[1,3,5,6]` |
| 6 | desempilha 2, registra, sem filhos | `[4]` | `[1,3,5,6,2]` |
| 7 | desempilha 4, registra, sem filhos | `[]` | `[1,3,5,6,2,4]` |

Resultado final: `[1,3,5,6,2,4]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é empilhado e desempilhado exatamente uma vez
- **Espaço:** O(n) no pior caso — a pilha pode conter simultaneamente todos os irmãos de vários níveis numa árvore larga e rasa, diferente da árvore binária onde o pior caso costuma ser O(h)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> preorder(Node root) {
    List<Integer> resultado = new ArrayList<>();
    if (root == null) return resultado;

    Deque<Node> pilha = new ArrayDeque<>();
    pilha.push(root);

    while (!pilha.isEmpty()) {
        Node no = pilha.pop();
        resultado.add(no.val); // registra ANTES de olhar os filhos: pré-ordem

        // empilha os filhos em ordem REVERSA para que o primeiro filho saia primeiro (LIFO)
        for (int i = no.children.size() - 1; i >= 0; i--) {
            pilha.push(no.children.get(i));
        }
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

- Empilhar os filhos na ordem original (sem inverter) — como a pilha é LIFO, o **último** filho empilhado seria o primeiro a sair, invertendo a ordem esperada de visita entre irmãos.
- Copiar a lógica de [0144] Binary Tree Preorder Traversal sem adaptar o `if (no.right != null) / if (no.left != null)` para um loop sobre `children` — a árvore n-ária não tem campos fixos `left`/`right`.
- Assumir que `children` é sempre não-nula — na maioria das implementações do LeetCode, um nó folha tem `children` como lista **vazia**, não `null`; iterar sobre uma lista vazia já funciona sem tratamento especial, mas assumir `null` sem checar quebraria com `NullPointerException`.
- Confundir o formato de **entrada serializada** do enunciado (valores e `null` como separadores de grupos de irmãos) com a estrutura do `Node` em memória — na hora de implementar, você recebe o `root` já montado como objeto, não precisa parsear esse formato.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | retorno antecipado, pilha nunca é usada |
| Um nó só, sem filhos | `root = [1]` | `[1]` | caso base, `children` vazia |
| Nó com muitos filhos diretos | `root = [1,null,2,3,4]` (1 tem filhos 2,3,4) | `[1,2,3,4]` | valida a ordem correta entre múltiplos irmãos, não só 2 |
| Árvore larga e profunda | primeiro exemplo do enunciado | `[1,3,5,6,2,4]` | cobre o caso combinando largura (3 filhos diretos) e profundidade (netos) |

## 🔗 Conexões

- Problemas irmãos: [0144] Binary Tree Preorder Traversal (a versão binária deste mesmo problema), [0590] N-ary Tree Postorder Traversal (mesma estrutura de nó, ordem de visita diferente), [0559] Maximum Depth of N-ary Tree (mesma estrutura de `children`, pergunta diferente)
- No backend: pré-ordem em árvore n-ária é exatamente como se percorre uma árvore de diretórios (DFS listando pasta antes do conteúdo) ou uma árvore DOM (visitar um elemento antes de seus filhos, na ordem em que aparecem) para gerar uma representação linear navegável.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
