# [0590] N-ary Tree Postorder Traversal

> 🔗 [LeetCode 590](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreNaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore n-ária, retorne a **travessia pós-ordem** dos valores dos seus nós: visita cada filho, da esquerda para a direita, recursivamente, e só depois o próprio nó.

**Exemplos:**
```
Input:  root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Input:  root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → precisa de solução O(n)
- `0 <= Node.val <= 10^4` → valores não-negativos, cabem em `int`
- Follow-up "faça iterativamente" → mesmo espírito de [0145] Binary Tree Postorder Traversal, generalizado para N filhos por nó

## 🧭 Como reconhecer o padrão

É a versão n-ária de [0145] Binary Tree Postorder Traversal: filhos (todos, da esquerda para a direita) antes do nó. A técnica iterativa mais simples continua sendo "gerar a ordem inversa e depois inverter o resultado", só que agora "os filhos" é uma lista de tamanho variável, não dois campos fixos.

## 🐢 Solução 1 — Força bruta (recursão direta)

Função recursiva: para cada filho em `node.children`, visita recursivamente; depois de todos os filhos visitados, adiciona `node.val` à lista.

- Tempo: O(n) · Espaço: O(h) de pilha de chamadas
- **Por que não basta:** mesmo raciocínio de [0589] e [0145] — correta, mas depende da pilha de chamadas do runtime, que o follow-up pede para não usar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use uma pilha explícita: empilhe a raiz; em cada iteração, desempilhe um nó, registre o valor **imediatamente** no início do resultado (`addFirst`, construindo a lista já invertida), e empilhe os filhos dele em ordem **original** (esquerda para direita) — como a pilha é LIFO, o último filho empilhado (o mais à direita) é o próximo a ser desempilhado, produzindo uma ordem de visita "nó, último filho, penúltimo filho, ..., primeiro filho" que, ao ser montada com `addFirst`, sai como "primeiro filho, ..., último filho, nó" — exatamente pós-ordem.

## 🎬 Exemplo passo a passo

`root = [1,null,3,2,4,null,5,6]` → nó `1` tem filhos `[3,2,4]`; nó `3` tem filhos `[5,6]`.

```
        1
     /  |  \
    3   2   4
   / \
  5   6
```

| Passo | Ação | Pilha (topo à direita) | Saída (addFirst a cada passo) |
|---|---|---|---|
| 1 | empilha raiz | `[1]` | `[]` |
| 2 | desempilha 1, addFirst, empilha filhos [3,2,4] em ordem original | `[3,2,4]` | `[1]` |
| 3 | desempilha 4, addFirst, sem filhos | `[3,2]` | `[4,1]` |
| 4 | desempilha 2, addFirst, sem filhos | `[3]` | `[2,4,1]` |
| 5 | desempilha 3, addFirst, empilha filhos [5,6] | `[5,6]` | `[3,2,4,1]` |
| 6 | desempilha 6, addFirst, sem filhos | `[5]` | `[6,3,2,4,1]` |
| 7 | desempilha 5, addFirst, sem filhos | `[]` | `[5,6,3,2,4,1]` |

Resultado final: `[5,6,3,2,4,1]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é empilhado e desempilhado exatamente uma vez
- **Espaço:** O(n) no pior caso — a pilha pode conter simultaneamente os irmãos de vários níveis numa árvore larga e rasa

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> postorder(Node root) {
    LinkedList<Integer> resultado = new LinkedList<>(); // addFirst em O(1)
    if (root == null) return resultado;

    Deque<Node> pilha = new ArrayDeque<>();
    pilha.push(root);

    while (!pilha.isEmpty()) {
        Node no = pilha.pop();
        resultado.addFirst(no.val); // monta a lista já invertida, sem precisar de reverse() no final

        // empilha em ordem ORIGINAL: o último filho fica no topo, é desempilhado primeiro
        for (Node filho : no.children) {
            pilha.push(filho);
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

- Empilhar os filhos em ordem **reversa** (copiando a lógica de [0589] Preorder) por engano — aqui a ordem certa de empilhar é a **original**, porque a inversão final já corrige a ordem de saída.
- Esquecer de usar `addFirst` (ou não inverter o resultado no final) — sem isso, a saída fica na ordem "nó, últimos filhos primeiro", que não é pós-ordem.
- Usar `ArrayList.add(0, x)` em vez de `LinkedList.addFirst(x)` — a primeira é O(n) por chamada (desloca todos os elementos), transformando a solução inteira em O(n²).
- Assumir que `children` é sempre não-vazia sem checagem — um nó folha tem `children` como lista vazia; o `for` sobre lista vazia já funciona sem tratamento especial, então nem é preciso um `if` extra.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | retorno antecipado, pilha nunca é usada |
| Um nó só, sem filhos | `root = [1]` | `[1]` | caso base, `children` vazia |
| Nó com múltiplos filhos diretos | `root = [1,null,2,3,4]` | `[2,3,4,1]` | valida a ordem correta entre irmãos sem netos |
| Árvore larga e profunda | primeiro exemplo do enunciado | `[5,6,3,2,4,1]` | cobre o caso combinando largura (3 filhos diretos) e profundidade (netos) |

## 🔗 Conexões

- Problemas irmãos: [0145] Binary Tree Postorder Traversal (a versão binária deste mesmo problema), [0589] N-ary Tree Preorder Traversal (mesma estrutura de nó, técnica de pilha "espelhada")
- No backend: pós-ordem em árvore n-ária é a ordem certa para deletar recursivamente uma estrutura de diretórios (apagar todo o conteúdo antes da pasta) ou para calcular agregações bottom-up numa árvore de componentes (cada nó só pode ser processado depois de todos os seus filhos).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
