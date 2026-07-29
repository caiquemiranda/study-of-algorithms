# [0114] Flatten Binary Tree to Linked List

> 🔗 [LeetCode 114](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Arvores` `#DFS` `#PreOrdem` `#Medium`

## 📜 O Problema

Dado o `root` de uma árvore binária, "achate" a árvore numa "linked list": use a própria classe `TreeNode`, onde o ponteiro `right` aponta para o próximo nó da lista e `left` é sempre `null`. A ordem da lista resultante deve ser a mesma de uma travessia **pré-ordem** da árvore original.

**Exemplos:**
```
Input:  root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Input:  root = []
Output: []

Input:  root = [0]
Output: [0]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 2000]` → O(n) é o esperado, uma única passada pela árvore
- `-100 <= Node.val <= 100` → sem risco de overflow
- Follow-up "resolva in-place com O(1) de espaço extra" → descarta guardar os nós numa lista auxiliar antes de religar os ponteiros; empurra para uma técnica de **threading** que reaproveita a própria estrutura da árvore como "memória" durante o processo

## 🧭 Como reconhecer o padrão

Apesar do resultado final "parecer" uma linked list, o input é uma `TreeNode` e a ordem exigida é literalmente uma **travessia pré-ordem** — a técnica central é de árvores: um DFS que decide, para cada nó, como religar suas subárvores (ver [fundamentos](../../../fundamentos/07_arvores.md)). É primo direto dos problemas de "serialize/threading" de árvore, não um problema de linked list — o `ListNode` nunca aparece no enunciado, só `TreeNode` com uma reinterpretação dos papéis de `left`/`right`.

## 🐢 Solução 1 — Força bruta (pré-ordem para uma lista auxiliar, depois religar)

Faz uma travessia pré-ordem completa (recursiva ou com pilha) coletando os nós numa `List<TreeNode>`, na ordem visitada. Depois, percorre a lista religando `nó[i].right = nó[i+1]` e `nó[i].left = null` para cada posição.

- Tempo: O(n) · Espaço: O(n) para a lista auxiliar (+ O(h) de pilha de recursão)
- **Por que não basta:** o tempo já é ótimo, mas o follow-up pede O(1) de espaço extra — guardar todos os nós numa lista à parte é exatamente o que dá para evitar, já que a árvore em si tem espaço de sobra (ponteiros `left` que vão virar `null` de qualquer forma) para servir de "rascunho" durante o processo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada nó (a partir da raiz, andando sempre por `current.right` depois de processado): se `current` tem subárvore esquerda, essa subárvore precisa ser "encaixada" entre `current` e o que hoje é `current.right` (porque pré-ordem visita a subárvore esquerda inteira antes de voltar para a direita). O truque: acha o nó **mais à direita** da subárvore esquerda (o último nó dela em pré-ordem) e pendura ali o antigo `current.right`. Depois, move a subárvore esquerda inteira para `current.right` e zera `current.left`. Isso é feito nó a nó, sem nunca sair da árvore original — o mesmo espírito da **threading de Morris**, mas para achatamento em vez de travessia sem pilha.

## 🎬 Exemplo passo a passo

`root = [1,2,5,3,4,null,6]` — árvore original:
```
        1
      /   \
     2     5
    / \      \
   3   4      6
```

| current | current.left | Nó mais à direita da subárvore esquerda | Ação | current.right vira |
|---|---|---|---|---|
| 1 | 2 | 4 (2→4, sem mais à direita) | `4.right = 1.right (5)`; `1.right = 2`; `1.left = null` | 2 |
| 2 | 3 | 3 (sem filho à direita) | `3.right = 2.right (4)`; `2.right = 3`; `2.left = null` | 3 |
| 3 | null | — | nada a fazer, só avança | 4 |
| 4 | null | — | nada a fazer, só avança | 5 *(herdado do passo em `1`)* |
| 5 | null | — | nada a fazer, só avança | 6 |
| 6 | null | — | nada a fazer, `current.right = null`, loop encerra | — |

Resultado final (cadeia via `right`, todos os `left = null`): `1 → 2 → 3 → 4 → 5 → 6` ✔ — é exatamente a pré-ordem da árvore original, batendo com `[1,null,2,null,3,null,4,null,5,null,6]`.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado uma vez como `current`, e o "achar o nó mais à direita" no total soma O(n) ao longo de toda a execução (cada aresta é percorrida no máximo uma vez nesse papel)
- **Espaço:** O(1) — nenhuma estrutura auxiliar; a solução é iterativa e reaproveita os próprios ponteiros da árvore

## 💻 Implementações

### Java (referência completa e comentada)
```java
public void flatten(TreeNode root) {
    TreeNode current = root;

    while (current != null) {
        if (current.left != null) {
            // Acha o último nó em pré-ordem da subárvore esquerda: o mais à direita dela.
            TreeNode rightmost = current.left;
            while (rightmost.right != null) {
                rightmost = rightmost.right;
            }

            // Pendura a antiga subárvore direita no fim da esquerda — é ali que ela
            // precisa aparecer em pré-ordem: DEPOIS de toda a subárvore esquerda.
            rightmost.right = current.right;

            // A subárvore esquerda assume o lugar da direita; esquerda vira null,
            // porque a "linked list" resultante só usa o ponteiro right.
            current.right = current.left;
            current.left = null;
        }
        current = current.right; // avança na cadeia já achatada até aqui
    }
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

- **Esquecer de "pendurar" a antiga subárvore direita no nó mais à direita da esquerda**: sem isso, a subárvore direita inteira é perdida quando `current.right = current.left` sobrescreve o ponteiro.
- **Mover `current` para `current.left` em vez de `current.right`**: depois do rearranjo, a cadeia inteira (esquerda + antiga direita) está pendurada em `current.right` — `current.left` já foi zerado.
- **Confundir a ordem da subárvore direita antiga com a nova**: a antiga direita deve aparecer **depois** da subárvore esquerda inteira (regra da pré-ordem: raiz, esquerda, direita) — pendurá-la direto em `current.right` sem passar pela esquerda primeiro inverteria a ordem.
- **Usar recursão sem perceber o custo de pilha**: uma versão recursiva (baseada em "achata a esquerda, achata a direita, religa") é didaticamente mais simples, mas gasta O(h) de pilha — o follow-up de O(1) espaço extra só é atendido pela versão iterativa com threading.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | `current` já é `null`, loop nem roda |
| Um único nó | `root = [0]` | `[0]` | não há subárvore esquerda, `current` só avança e o loop encerra |
| Só filhos à esquerda (lista degenerada) | `root = [1,2,null,3]` (2 é filho esquerdo de 1, 3 é filho esquerdo de 2) | `[1,null,2,null,3]` | testa quando toda subárvore é "esquerda-only", sem nunca precisar pendurar uma direita antiga |
| Só filhos à direita (já quase uma lista) | `root = [1,null,2,null,3]` | `[1,null,2,null,3]` | garante que a função não quebra uma árvore que já está no formato certo |
| Exemplo do enunciado | `root = [1,2,5,3,4,null,6]` | `[1,null,2,null,3,null,4,null,5,null,6]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0144] Binary Tree Preorder Traversal** (a travessia que este problema materializa como estrutura), **[0143] Reorder List** (também rearranja ponteiros de uma estrutura encadeada em uma ordem específica, mas já começando de uma linked list em vez de uma árvore)
- No backend: "achatar" uma estrutura hierárquica numa sequência linear, sem espaço extra, é o mesmo padrão usado em **serialização in-place de árvores de configuração** (converter uma árvore de nós JSON aninhados numa lista de eventos, como faz um parser SAX) e no **layout de memória de estruturas em árvore** de alguns bancos de dados orientados a documento, onde a árvore é percorrida em pré-ordem para gravação sequencial em disco.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
