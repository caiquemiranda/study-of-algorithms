# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree

> 🔗 [LeetCode 1379](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dadas duas árvores binárias `original` e `cloned` (onde `cloned` é uma cópia exata de `original`) e uma referência `target` a um nó de `original`, retorne a **referência ao nó correspondente** em `cloned`.

**Exemplos:**
```
Input:  tree = [7,4,3,null,null,6,19], target = 3
Output: 3

Input:  tree = [7], target = 7
Output: 7

Input:  tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^4]` → precisa de solução O(n)
- Valores dos nós **únicos** (na versão básica do problema) → permite usar o valor como atalho de comparação, mas a solução de referência aqui evita depender disso
- Não pode modificar nenhuma das duas árvores nem o nó `target` → descarta abordagens que alterem a estrutura das árvores para "marcar" o nó procurado
- Follow-up "e se valores repetidos forem permitidos?" → sinaliza que a solução correta **não deve** depender de comparar valores, e sim da **posição estrutural**, que continua válida mesmo com duplicatas

## 🧭 Como reconhecer o padrão

"Duas árvores idênticas + achar o nó correspondente" é DFS **simultâneo** nas duas árvores, igual a [0100] Same Tree e [0617] Merge Two Binary Trees — como as duas árvores têm exatamente a mesma estrutura, andar os dois ponteiros em sincronia garante que, quando um chegar em `target` (por referência, `==`), o outro estará exatamente na posição correspondente.

## 🐢 Solução 1 — Força bruta (duas listas de nós na mesma ordem)

Fazer uma travessia (ex.: pré-ordem) em `original`, coletando todos os nós numa lista. Fazer a **mesma** travessia, na mesma ordem, em `cloned`, coletando numa segunda lista. Achar o índice de `target` na primeira lista (comparando por referência) e retornar o nó de mesmo índice na segunda lista.

- Tempo: O(n) · Espaço: O(n) para as duas listas
- **Por que não basta:** funciona (já que as duas árvores têm estrutura idêntica, a mesma ordem de travessia garante correspondência por índice), mas gasta O(n) de memória guardando **todos** os nós de ambas as árvores, quando a resposta pode ser encontrada percorrendo as duas árvores **ao mesmo tempo**, sem nunca precisar materializar essas listas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `original` e `cloned` **simultaneamente**, nó a nó, com uma única recursão que recebe os dois ponteiros ao mesmo tempo. Assim que o ponteiro de `original` for exatamente o `target` (comparado por referência, `==`, não por valor), retorne o ponteiro correspondente de `cloned` **naquele exato ponto da recursão** — sem precisar de nenhuma lista, sem depender do valor do nó.

## 🎬 Exemplo passo a passo

`tree = [7,4,3,null,null,6,19]`, `target` = o nó de valor `3` em `original`

```
original:      7          cloned:      7
              / \                      / \
             4   3                    4   3
                / \                      / \
               6  19                    6  19
```

| Passo | Chamada | original atual == target? | Ação |
|---|---|---|---|
| 1 | dfs(orig=7, clon=7) | não | desce para ambos os lados |
| 2 | dfs(orig=4, clon=4) [esquerda] | não | sem filhos, retorna `null` (não achou por aqui) |
| 3 | dfs(orig=3, clon=3) [direita] | **sim** | retorna `clon` (o nó `3` de `cloned`) imediatamente |

Resultado final: referência ao nó `3` de `cloned` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no pior caso — visita os nós das duas árvores em paralelo até encontrar `target`, com short-circuit assim que acha
- **Espaço:** O(h) de pilha de recursão — nenhuma lista auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public final TreeNode getTargetCopy(TreeNode original, TreeNode cloned, TreeNode target) {
    if (original == null) return null; // acabou a árvore original sem achar: não existe correspondência aqui

    // comparação por REFERÊNCIA, não por valor — funciona mesmo com valores duplicados na árvore
    if (original == target) return cloned;

    TreeNode encontrado = getTargetCopy(original.left, cloned.left, target);
    if (encontrado != null) return encontrado; // short-circuit: já achou do lado esquerdo

    return getTargetCopy(original.right, cloned.right, target);
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

- Comparar `original.val == target.val` em vez de `original == target` — o follow-up do próprio enunciado (valores repetidos permitidos) existe exatamente para expor essa armadilha: comparar por valor pode retornar o nó **errado** quando há duplicatas na árvore.
- Modificar `original` ou `cloned` para "marcar" o nó já visitado — o enunciado proíbe explicitamente alterar qualquer uma das árvores.
- Esquecer o short-circuit ao checar o resultado da busca à esquerda antes de tentar a direita — sem o `if (encontrado != null) return encontrado`, a chamada recursiva da direita sempre executaria, mesmo depois de já ter achado a resposta.
- Assumir que basta comparar `original.val == target.val` **e** parar de recursar — mesmo em árvores sem duplicatas, comparar por valor funciona por coincidência, mas é uma solução frágil que quebra silenciosamente assim que a garantia de unicidade deixa de valer.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `tree = [7], target = 7` | nó `7` de `cloned` | caso base, a raiz já é o alvo |
| Alvo é uma folha profunda | `tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4` | nó `4` de `cloned` | testa a busca numa árvore bem desbalanceada (corrente) |
| Alvo no meio da árvore | `tree = [7,4,3,null,null,6,19], target = 3` | nó `3` de `cloned` | cobre o exemplo 1 do enunciado |
| Árvore com valores duplicados (follow-up) | `tree = [1,1,1], target` = a segunda ocorrência de `1` | o nó correspondente exato de `cloned`, não qualquer `1` | valida que a comparação por referência (não por valor) resolve o follow-up corretamente |

## 🔗 Conexões

- Problemas irmãos: [0100] Same Tree (o mesmo esqueleto de recursão simultânea em duas árvores), [0617] Merge Two Binary Trees (também percorre duas árvores ao mesmo tempo, mas combinando valores em vez de buscar uma referência)
- No backend: navegar duas estruturas espelhadas em paralelo para localizar um elemento correspondente é o mesmo princípio usado em sincronização de árvores de estado (ex.: encontrar o nó equivalente numa cópia "shadow" de uma árvore de UI usada para diffing, como em Virtual DOM) sem precisar de identificadores externos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
