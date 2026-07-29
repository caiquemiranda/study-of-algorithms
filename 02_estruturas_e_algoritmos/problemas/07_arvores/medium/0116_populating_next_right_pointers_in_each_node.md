# [0116] Populating Next Right Pointers in Each Node

> 🔗 [LeetCode 116](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Arvores` `#BFS` `#Medium`

## 📜 O Problema

Você recebe uma árvore binária **perfeita** (todas as folhas no mesmo nível, todo pai tem dois filhos), cujo `Node` tem um campo extra `next`. Preencha cada `next` para apontar para o próximo nó **à direita no mesmo nível**. Se não houver, `next` deve ser `null`. Inicialmente, todos os `next` são `null`.

**Exemplos:**
```
Input:  root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explicação: cada nível fica conectado da esquerda para a direita, '#' marca o fim de cada nível.

Input:  root = []
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 2^12 - 1]` → confirma que a árvore é **perfeita** (número de nós de uma árvore perfeita completa até certa altura), o que garante que todo nó não-folha tem exatamente 2 filhos — sem esse fato, a técnica otimizada não funcionaria
- `-1000 <= Node.val <= 1000` → sem risco de overflow
- Follow-up "use apenas espaço constante; a pilha implícita da recursão não conta" → sugere que existe uma solução O(1) de espaço **de verdade** iterativa, sem fila nem pilha explícitas, aproveitando os próprios ponteiros `next` já preenchidos de um nível para "atravessar" esse nível sem estrutura auxiliar

## 🧭 Como reconhecer o padrão

"Conecte nós do mesmo nível" é a assinatura mais direta de **BFS por nível** — ver [fundamentos](../../../fundamentos/07_arvores.md), seção "Como Reconhecer". A particularidade aqui é que, como a árvore é **perfeita**, dá para evitar a fila explícita do BFS tradicional: uma vez que um nível está conectado via `next`, esses próprios ponteiros servem de "trilho" para percorrer o nível sem fila.

## 🐢 Solução 1 — Força bruta (BFS com fila, nível por nível)

Usa uma fila (`Queue<Node>`). Para cada nível, fixa o tamanho da fila naquele instante (para saber onde o nível termina), tira os nós um a um ligando `atual.next = próximo do mesmo nível` (ou `null` no último), e empurra os filhos de cada nó para a fila.

- Tempo: O(n) · Espaço: O(n) — no pior caso, a fila chega a guardar o nível mais largo, que numa árvore perfeita tem até `n/2` nós
- **Por que não basta:** o tempo já é ótimo, mas o follow-up pede espaço O(1) de verdade — a fila guarda um nível inteiro de cada vez, e como a árvore é perfeita, existe uma forma de dispensar essa fila completamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Como a árvore é **perfeita**, todo nó do nível atual tem exatamente 2 filhos. A ideia: depois que o nível atual já está conectado por `next` (o nível da raiz "já está conectado" trivialmente, com um único nó), usa-se essa própria cadeia de `next` para visitar cada nó do nível e conectar os filhos dele ao **próximo nível**, sem nenhuma fila. Para cada nó `node` do nível atual: `node.left.next = node.right` (os dois filhos do mesmo pai são vizinhos diretos); e, se `node.next` existir, `node.right.next = node.next.left` (o filho direito de um nó se conecta ao filho esquerdo do próximo nó do mesmo nível — a "ponte" entre famílias diferentes). Repete isso nível a nível, descendo por `leftmost = leftmost.left`.

## 🎬 Exemplo passo a passo

`root = [1,2,3,4,5,6,7]` (árvore perfeita de 3 níveis)

| Nível processado | Nó (`node`) | `node.left.next = node.right` | `node.right.next = node.next.left`? | Nível seguinte já conectado |
|---|---|---|---|---|
| 0 (raiz) | 1 | `2.next = 3` | `node.next` é `null` → pula | 2 → 3 |
| 1 | 2 | `4.next = 5` | `2.next=3` existe → `5.next = 3.left = 6` | 4 → 5 → 6 |
| 1 | 3 | `6.next = 7` | `3.next` é `null` → pula | 4 → 5 → 6 → 7 |
| 2 | 4, 5, 6, 7 | (são folhas, `node.left` é `null`) | — | — (loop externo encerra: `leftmost.left` é `null`) |

Resultado final: nível 0 → `1,#`; nível 1 → `2,3,#`; nível 2 → `4,5,6,7,#` ✔ — bate com `[1,#,2,3,#,4,5,6,7,#]` do enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez como `node` (percorrendo seu nível) e uma vez como filho conectado
- **Espaço:** O(1) — nenhuma fila nem pilha; apenas os ponteiros `leftmost` e `node`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public Node connect(Node root) {
    Node leftmost = root; // primeiro nó de cada nível, usado para "descer" um nível de cada vez

    // Continua enquanto o nível atual tiver filhos (ou seja, não é o último nível/folhas).
    while (leftmost != null && leftmost.left != null) {
        Node node = leftmost;

        // Percorre o nível atual usando os next JÁ CONECTADOS (nenhuma fila necessária)
        // e vai conectando os filhos — o próximo nível.
        while (node != null) {
            node.left.next = node.right; // filhos do MESMO pai: vizinhos diretos

            if (node.next != null) {
                // Filho direito deste nó se conecta ao filho esquerdo do PRÓXIMO nó do
                // mesmo nível — a ponte entre duas famílias diferentes.
                node.right.next = node.next.left;
            }
            // se node.next == null, node.right.next já é null por padrão (fim do nível)

            node = node.next; // avança pelo nível atual usando o trilho já pronto
        }

        leftmost = leftmost.left; // desce para o primeiro nó do próximo nível
    }

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

- **Esquecer de checar `node.next != null` antes de `node.right.next = node.next.left`**: sem essa checagem, acessar `.left` de um `next` nulo lança `NullPointerException` — o último nó de cada nível não tem próximo.
- **Assumir que a técnica funciona em árvores não-perfeitas**: se algum nó tiver só 1 filho ou 0, `node.left.next = node.right` quebra (acesso a `null.next`) — essa é exatamente a diferença para o irmão LC 117, que exige uma lógica mais cuidadosa.
- **Tentar usar recursão pura contando como "O(1) espaço"**: o enunciado permite isso explicitamente no follow-up ("a pilha implícita não conta"), mas vale saber que, rigorosamente, uma versão recursiva ainda gasta O(log n) de pilha — só a versão iterativa é O(1) de verdade.
- **Conectar os filhos antes de ter certeza de que o pai já está com seu próprio `next` correto**: a ordem de processamento (nível por nível, usando os `next` já prontos do nível anterior) é o que garante que `node.next.left` sempre aponta para o lugar certo quando é lido.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | `leftmost` já é `null`, loop nem roda |
| Um único nó | `root = [1]` | `[1,#]` | `leftmost.left` é `null`, loop externo nem roda; `1.next` continua `null` |
| Dois níveis | `root = [1,2,3]` | `[1,#,2,3,#]` | menor caso onde a conexão "mesmo pai" é testada |
| Três níveis, exemplo do enunciado | `root = [1,2,3,4,5,6,7]` | `[1,#,2,3,#,4,5,6,7,#]` | trace acima, testa também a conexão "entre famílias" (`5.next=6`) |
| Valores negativos | `root = [-1,-2,-3]` | `[-1,#,-2,-3,#]` | garante que a lógica de ponteiros não depende do sinal do valor |

## 🔗 Conexões

- Problemas irmãos: **[0117] Populating Next Right Pointers in Each Node II** (mesma ideia, mas para árvore binária qualquer — não pode assumir 2 filhos por nó), **[0102] Binary Tree Level Order Traversal** (o BFS clássico com fila que esta solução otimizada evita)
- No backend: conectar nós do mesmo "nível" sem estrutura auxiliar aparece em **travessia de árvores de UI/DOM** (encontrar o próximo elemento irmão sem manter uma fila separada) e no conceito de **link horizontal em B+Trees** usado por alguns bancos de dados, onde folhas do mesmo nível são conectadas para permitir range scans sequenciais sem voltar à raiz.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
