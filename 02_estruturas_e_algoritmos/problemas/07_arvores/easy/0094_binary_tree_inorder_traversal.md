# [0094] Binary Tree Inorder Traversal

> 🔗 [LeetCode 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne a **travessia em-ordem** (in-order) dos valores dos seus nós: visita a subárvore esquerda, depois o nó atual, depois a subárvore direita.

**Exemplos:**
```
Input:  root = [1,null,2,3]
Output: [1,3,2]

Input:  root = []
Output: []

Input:  root = [1]
Output: [1]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 100]` → entrada pequena; qualquer solução O(n) passa tranquilamente — o desafio real é o **follow-up** (fazer sem recursão), não a performance
- `-100 <= Node.val <= 100` → valores cabem em `int` sem risco de overflow
- Follow-up "faça iterativamente" → sinaliza que a versão recursiva é considerada trivial demais; o valor didático está em simular a pilha de chamadas manualmente

## 🧭 Como reconhecer o padrão

"Travessia em-ordem" é vocabulário direto de árvore: **esquerda → nó → direita**. Se a árvore fosse uma BST, esse percurso sairia em ordem crescente — é de onde vem o nome. Aqui a árvore não é necessariamente uma BST, então o resultado só precisa respeitar a ordem de visita, não vir ordenado.

## 🐢 Solução 1 — Força bruta (recursão direta)

Função recursiva: visita `left`, adiciona `node.val` à lista, visita `right`. Caso base: nó nulo não faz nada.

- Tempo: O(n) · Espaço: O(h) de pilha de chamadas (h = altura da árvore)
- **Por que não basta:** resolve corretamente, mas usa a pilha de chamadas do próprio runtime, que o enunciado pede explicitamente para não depender no follow-up — numa árvore muito desbalanceada e profunda (fora do range de 100 nós deste problema, mas comum em produção), a recursão pode estourar o limite de profundidade da pilha.

## 💡 Solução 2 — A ideia otimizada (intuição)

Simule a pilha de chamadas manualmente com uma `Deque` explícita: desça sempre pela esquerda empilhando cada nó visitado; quando não houver mais esquerda, desempilhe (esse é o próximo nó "em-ordem"), registre o valor, e passe a descer pela direita dele. É literalmente o mesmo algoritmo da recursão, só que a pilha é uma estrutura de dados controlada por você, não a do interpretador.

## 🎬 Exemplo passo a passo

`root = [1,null,2,3]` → `1` tem filho direito `2`; `2` tem filho esquerdo `3`.

```
1
 \
  2
 /
3
```

| Passo | Ação | Pilha (topo à direita) | atual | Saída |
|---|---|---|---|---|
| 1 | empilha 1, desce esquerda (não tem) | `[1]` | null | `[]` |
| 2 | desempilha 1, visita, desce direita (2) | `[]` | 2 | `[1]` |
| 3 | empilha 2, desce esquerda (3) | `[2]` | 3 | `[1]` |
| 4 | empilha 3, desce esquerda (não tem) | `[2,3]` | null | `[1]` |
| 5 | desempilha 3, visita, desce direita (não tem) | `[2]` | null | `[1,3]` |
| 6 | desempilha 2, visita, desce direita (não tem) | `[]` | null | `[1,3,2]` |
| 7 | pilha vazia e atual null → termina | `[]` | — | `[1,3,2]` |

Resultado final: `[1,3,2]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é empilhado e desempilhado exatamente uma vez
- **Espaço:** O(h) — a pilha guarda no máximo o caminho da raiz até o nó mais fundo sendo processado; no pior caso (árvore degenerada), h = n

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> resultado = new ArrayList<>();
    Deque<TreeNode> pilha = new ArrayDeque<>();
    TreeNode atual = root;

    while (atual != null || !pilha.isEmpty()) {
        // desce o máximo possível pela esquerda, empilhando o caminho percorrido
        while (atual != null) {
            pilha.push(atual);
            atual = atual.left;
        }
        // não há mais esquerda: este é o próximo nó em ordem
        atual = pilha.pop();
        resultado.add(atual.val);
        // agora a "descida pela esquerda" recomeça a partir da subárvore direita
        atual = atual.right;
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

- Esquecer a condição `atual != null` no while externo — checar só `!pilha.isEmpty()` faz perder ramos direitos ainda não empilhados.
- Adicionar o valor à lista **antes** de terminar de descer pela esquerda — isso produz pré-ordem, não em-ordem.
- Esquecer de reatribuir `atual = atual.right` depois do `pop()` — sem isso, o loop reprocessa a mesma subárvore esquerda indefinidamente.
- Achar que a versão iterativa "não usa memória" — ela continua O(h); só troca a pilha implícita da recursão por uma pilha explícita do seu controle.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | pilha nunca recebe nada, loop nem roda |
| Um nó | `root = [1]` | `[1]` | caso base, sem filhos |
| Só filhos à direita (skew) | `root = [1,null,2,null,3]` | `[1,2,3]` | pilha nunca acumula mais de 1 elemento, mas testa a travessia sem ramos esquerdos |
| Só filhos à esquerda (skew) | `root = [3,2,1]` (2 é filho esquerdo de 3; 1 é filho esquerdo de 2) | `[1,2,3]` | pilha acumula toda a cadeia antes do primeiro pop |

## 🔗 Conexões

- Problemas irmãos: [0144] Binary Tree Preorder Traversal (mesma técnica de pilha, ordem de visita diferente), [0145] Binary Tree Postorder Traversal (a mais difícil de iterar das três), [0230] Kth Smallest Element in a BST (usa em-ordem parcial, parando assim que encontra o k-ésimo)
- No backend: em-ordem é a forma canônica de "ler uma BST como se fosse uma lista ordenada" — é o que estruturas como `TreeMap`/`TreeSet` em Java fazem internamente (são Red-Black Trees) para entregar `.entrySet()` já em ordem crescente sem precisar ordenar nada explicitamente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
