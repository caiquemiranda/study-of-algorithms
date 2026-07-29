# [0109] Convert Sorted List to Binary Search Tree

> 🔗 [LeetCode 109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Arvores` `#BST` `#DivideAndConquer` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list simples com elementos em ordem **crescente**, converta-a numa **BST height-balanced** (árvore de busca binária balanceada em altura). Se houver mais de uma resposta válida, qualquer uma é aceita.

**Exemplos:**
```
Input:  head = [-10,-3,0,5,9]
Output: uma árvore como [0,-3,9,-10,null,5]
Explicação: essa é uma das respostas válidas — uma BST balanceada com esses valores.

Input:  head = []
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 2 * 10^4]` → O(n) é o esperado; O(n log n) também passa confortavelmente, mas O(n²) provavelmente não
- `-10^5 <= Node.val <= 10^5` → sem risco de overflow
- "**height-balanced**" → não é qualquer BST válida: a diferença de altura entre as subárvores de qualquer nó não pode passar de 1. Isso é a peça-chave: para garantir balanceamento, a raiz de cada subárvore precisa ser sempre o elemento do **meio** do intervalo — é o mesmo princípio de **busca binária** aplicado à construção da árvore

## 🧭 Como reconhecer o padrão

O input é uma `ListNode`, mas o objetivo é **construir uma árvore** (`TreeNode`) — pela regra de ouro da categorização ("classifique pela técnica da solução ótima, não pelo tipo do input"), isso é um problema de **árvores**: divisão recursiva de um intervalo ordenado, sempre escolhendo o meio como raiz, exatamente como descrito nos [fundamentos de árvores](../../../fundamentos/07_arvores.md) para construção a partir de uma sequência ordenada. A única particularidade de linked list aqui é *como* achar esse "meio" sem acesso por índice — usando o padrão **fast & slow** emprestado da categoria de listas encadeadas.

## 🐢 Solução 1 — Força bruta (copiar para um array, depois construir por índice)

Percorre a lista uma vez copiando os valores para um array (O(n) espaço extra). Com o array em mãos, constrói a árvore recursivamente: para cada intervalo `[lo, hi]`, o elemento do meio (`mid = (lo+hi)/2`, por índice O(1)) vira a raiz, e os intervalos `[lo, mid-1]` e `[mid+1, hi]` viram as subárvores esquerda e direita.

- Tempo: O(n) · Espaço: O(n) para o array
- **Por que não basta:** o tempo já é ótimo, mas gasta memória extra proporcional ao tamanho da lista só para ganhar acesso por índice — o enunciado já entrega os dados numa lista encadeada, então existe uma forma de achar o "meio" de cada sublista diretamente com os próprios nós, sem replicar os valores.

## 💡 Solução 2 — A ideia otimizada (intuição)

A mesma ideia de "sempre a raiz é o elemento do meio" (para garantir balanceamento), mas achando o meio de cada sublista com o padrão **fast & slow** direto nos nós, em vez de indexar um array. Cada chamada recursiva recebe um par `(head, tail)`, onde `tail` marca o fim da sublista (exclusivo, `null` na primeira chamada). Dentro dela: `slow` e `fast` andam a partir de `head` até `fast` alcançar `tail` (ou passar perto); `slow` para exatamente no nó do meio, que vira a raiz. A sublista à esquerda de `slow` vira a recursão da esquerda; a sublista de `slow.next` até `tail` vira a recursão da direita.

## 🎬 Exemplo passo a passo

`head = [-10,-3,0,5,9]` (nós: A=-10, B=-3, C=0, D=5, E=9)

| Chamada | Sublista (head..tail exclusivo) | Meio (fast & slow) → raiz | Sublista esquerda | Sublista direita |
|---|---|---|---|---|
| nível 0 | [A,B,C,D,E] | C (valor 0) | [A,B] | [D,E] |
| nível 1 (esq.) | [A,B] | B (valor -3) | [A] | [] |
| nível 1 (dir.) | [D,E] | E (valor 9) | [D] | [] |
| nível 2 | [A] | A (valor -10) | [] | [] |
| nível 2 | [D] | D (valor 5) | [] | [] |

Árvore final: raiz `0`, filho esquerdo `-3` (que tem filho esquerdo `-10`), filho direito `9` (que tem filho esquerdo `5`) ✔ — height-balanced, e bate com a resposta de exemplo do enunciado (`[0,-3,9,-10,null,5]`).

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — achar o meio de uma sublista de tamanho `k` custa O(k); somando o custo em cada um dos O(log n) níveis da recursão (cada nível processa o total de `n` nós, espalhados entre as chamadas daquele nível), o total é O(n log n)
- **Espaço:** O(log n) — só a pilha de recursão (proporcional à altura da árvore balanceada), sem array auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public TreeNode sortedListToBST(ListNode head) {
    return build(head, null); // tail=null representa "até o fim da lista"
}

private TreeNode build(ListNode head, ListNode tail) {
    if (head == tail) return null; // sublista vazia: caso base da recursão

    // fast & slow limitados por 'tail' (exclusivo): slow para no nó do MEIO da sublista,
    // garantindo que a raiz escolhida deixa as duas metades com tamanhos parecidos (balanceamento).
    ListNode slow = head, fast = head;
    while (fast != tail && fast.next != tail) {
        slow = slow.next;
        fast = fast.next.next;
    }

    TreeNode root = new TreeNode(slow.val);
    root.left = build(head, slow);        // tudo ANTES do meio
    root.right = build(slow.next, tail);  // tudo DEPOIS do meio, até o limite original
    return root;
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

- **Escolher sempre o primeiro ou o último elemento como raiz em vez do meio**: gera uma BST válida (a ordenação está certa), mas completamente degenerada (uma lista disfarçada de árvore) — quebra a exigência de "height-balanced".
- **Errar o limite `tail` como inclusivo em vez de exclusivo**: a condição `fast != tail` (não `fast.next != null`) é o que permite delimitar sublistas menores que a lista inteira sem precisar cortar fisicamente os ponteiros `next` originais.
- **Cortar a lista original (`slow.next = null`) para "separar" as metades**: funciona, mas destrói informação necessária para a recursão da direita descobrir onde ela termina — usar o parâmetro `tail` evita essa mutação desnecessária.
- **Recalcular o tamanho da sublista a cada chamada para achar o meio por índice**: reintroduz o custo de uma passada extra por nível: o fast & slow já encontra o meio numa única passada, sem precisar saber o tamanho de antemão.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `null` (árvore vazia) | `head == tail` (ambos `null`) já na 1ª chamada |
| Um nó | `head = [5]` | árvore com só a raiz `5` | fast & slow para imediatamente em `head`, sem filhos |
| Dois nós | `head = [1,2]` | raiz `2`, filho esquerdo `1` (ou raiz `1`, filho direito `2` — ambas balanceadas) | testa o caso onde `fast.next` já bate em `tail` cedo |
| Lista maior, exemplo do enunciado | `head = [-10,-3,0,5,9]` | árvore balanceada equivalente a `[0,-3,9,-10,null,5]` | trace acima |
| Valores negativos e positivos misturados | `head = [-3,-1,0,2,4]` | qualquer BST balanceada válida com esses valores | garante que sinais negativos não afetam a lógica de comparação por posição |

## 🔗 Conexões

- Problemas irmãos: **[0108] Convert Sorted Array to Binary Search Tree** (mesmo problema, mas com acesso O(1) por índice desde o início — dispensa o fast & slow), **[0876] Middle of the Linked List** (a mesma sub-rotina de achar o meio usada aqui, sem a parte de construção de árvore), **[0098] Validate Binary Search Tree** (verifica a propriedade que este problema constrói)
- No backend: construir uma estrutura balanceada a partir de dados já ordenados (sem reordenar do zero) é o mesmo princípio por trás da criação de **índices B-Tree em lote** (bulk loading) em bancos de dados — quando os dados já chegam ordenados (ex.: de um dump ou de um `ORDER BY`), o banco constrói o índice de baixo para cima escolhendo pontos médios, muito mais rápido que inserir registro por registro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
