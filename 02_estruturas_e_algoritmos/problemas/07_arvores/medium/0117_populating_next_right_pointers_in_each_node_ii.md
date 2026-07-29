# [0117] Populating Next Right Pointers in Each Node II

> 🔗 [LeetCode 117](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Arvores` `#BFS` `#Medium`

## 📜 O Problema

Igual ao LC 116, mas agora para uma árvore binária **qualquer** (não necessariamente perfeita — nós podem ter 0, 1 ou 2 filhos). Preencha cada `next` para apontar para o próximo nó à direita no mesmo nível, ou `null` se não houver.

**Exemplos:**
```
Input:  root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Input:  root = []
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 6000]` → O(n) é o esperado
- `-100 <= Node.val <= 100` → sem risco de overflow
- **Sem a garantia de árvore perfeita** (diferente do LC 116) → a técnica de "todo nó tem exatamente 2 filhos" quebra aqui; é preciso uma forma de **pular buracos** (filhos ausentes) ao construir a conexão do próximo nível
- Follow-up "espaço O(1), pilha implícita não conta" → a mesma meta do irmão: uma solução iterativa que usa só os próprios ponteiros da árvore como estrutura auxiliar

## 🧭 Como reconhecer o padrão

Mesma assinatura do LC 116 — "conecte nós do mesmo nível" é **BFS por nível** (ver [fundamentos](../../../fundamentos/07_arvores.md)) — mas sem a garantia de árvore perfeita, o truque de "sempre existem os dois filhos" não serve. A solução precisa construir explicitamente a lista de filhos do próximo nível, pulando os que forem `null`, usando um **nó sentinela** para simplificar a montagem dessa lista (o mesmo padrão de sentinela usado em linked lists).

## 🐢 Solução 1 — Força bruta (BFS com fila, nível por nível)

Igual à força bruta do LC 116: usa uma fila, processa um nível por vez (com o tamanho do nível fixado no início da iteração), religando `next` entre nós consecutivos da fila e empurrando os filhos existentes (pulando os `null`) para a próxima rodada.

- Tempo: O(n) · Espaço: O(n) — a fila pode guardar o nível mais largo da árvore
- **Por que não basta:** funciona para qualquer árvore (não depende de ser perfeita), mas o follow-up pede O(1) de espaço extra — a fila cresce proporcionalmente à largura da árvore, o que dá para evitar reaproveitando os próprios ponteiros `next` do nível atual para montar o próximo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Igual em espírito ao LC 116 (usa o nível atual, já conectado por `next`, para montar o próximo nível sem fila), mas com um ajuste: como nem todo nó tem os dois filhos, não dá para simplesmente ligar `node.left.next = node.right` (um dos dois pode ser `null`). Em vez disso, mantém-se um **sentinela** (`dummy`) e uma **cauda** (`tail`) para o próximo nível: percorre-se o nível atual via `next`, e para cada filho **existente** (esquerda, depois direita) de cada nó, anexa-se esse filho na cauda da lista do próximo nível — pulando silenciosamente os que forem `null`. No fim de cada nível, `dummy.next` é o primeiro nó do próximo nível, e o processo repete.

## 🎬 Exemplo passo a passo

`root = [1,2,3,4,5,null,7]` — árvore:
```
        1
      /   \
     2     3
    / \      \
   4   5      7
```

**Nível 0** (`node = 1`): `dummy0`, `tail = dummy0`. `1.left=2` existe → anexa 2. `1.right=3` existe → anexa 3. `node = 1.next = null`, fim do nível.
→ próximo nível: `2 → 3` (via `next`)

**Nível 1** (`node` percorre `2 → 3`):
| node | filho esquerdo | filho direito | Anexado na cauda |
|---|---|---|---|
| 2 | 4 (existe) | 5 (existe) | 4, depois 5 |
| 3 | null (pula) | 7 (existe) | 7 |

→ próximo nível: `4 → 5 → 7` (via `next`, montado nesta ordem)

**Nível 2** (`node` percorre `4 → 5 → 7`): nenhum tem filhos → nada é anexado → `dummy2.next` continua `null` → loop externo encerra.

Resultado final: nível 0 → `1,#`; nível 1 → `2,3,#`; nível 2 → `4,5,7,#` ✔ — bate com `[1,#,2,3,#,4,5,7,#]` do enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado uma vez para ler seus filhos e, depois, uma vez como membro do nível seguinte
- **Espaço:** O(1) — só `dummy`/`tail` por nível (constante, não proporcional à largura da árvore) e os ponteiros de percurso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public Node connect(Node root) {
    Node leftmost = root;

    while (leftmost != null) {
        // Sentinela: monta a lista do PRÓXIMO nível sem precisar tratar "o 1º filho
        // encontrado" como caso especial — o mesmo padrão de dummy usado em linked lists.
        Node dummy = new Node(0);
        Node tail = dummy;
        Node node = leftmost;

        // Percorre o nível ATUAL usando os next já prontos (nenhuma fila necessária).
        while (node != null) {
            if (node.left != null) {
                tail.next = node.left;
                tail = tail.next;
            }
            if (node.right != null) {
                tail.next = node.right;
                tail = tail.next;
            }
            node = node.next;
        }

        leftmost = dummy.next; // 1º nó do próximo nível (ou null, se não houver mais níveis)
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

- **Aplicar a lógica do LC 116 direto (`node.left.next = node.right`)**: quebra assim que um nó tem só 1 filho ou nenhum — `node.left` ou `node.right` pode ser `null`, e não existe garantia de que ambos existam juntos.
- **Esquecer de checar `node.left != null` e `node.right != null` separadamente**: sem essas checagens, tentar anexar um filho `null` na cauda corrompe a lista do próximo nível.
- **Não usar sentinela para a cauda do próximo nível**: sem `dummy`, é preciso tratar "qual é o primeiro filho encontrado neste nível" como caso especial antes do loop.
- **Reaproveitar a variável `tail` entre níveis sem resetar**: cada nível precisa do seu próprio `dummy`/`tail` novos — misturar caudas de níveis diferentes junta nós de níveis diferentes na mesma cadeia `next`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | `leftmost` já é `null`, loop externo nem roda |
| Um único nó | `root = [1]` | `[1,#]` | nenhum filho existe, `dummy.next` continua `null` após o nível 0 |
| Nó com um único filho | `root = [1,2]` (só filho esquerdo) | `[1,#,2,#]` | valida que pular o filho `null` (direito) não quebra a cadeia |
| Árvore não-perfeita, exemplo do enunciado | `root = [1,2,3,4,5,null,7]` | `[1,#,2,3,#,4,5,7,#]` | trace acima — testa o "buraco" no filho esquerdo de 3 |
| Árvore assimétrica em profundidade | `root = [1,2,3,4,null,null,5]` | `[1,#,2,3,#,4,5,#]` | `4` (filho de 2) e `5` (filho de 3) vêm de ramos diferentes, mas precisam ficar conectados no último nível |

## 🔗 Conexões

- Problemas irmãos: **[0116] Populating Next Right Pointers in Each Node** (mesmo problema, mas com a garantia de árvore perfeita, permitindo uma versão sem sentinela), **[0102] Binary Tree Level Order Traversal** (o BFS clássico com fila que esta versão otimizada evita)
- No backend: montar a "próxima camada" de processamento a partir da atual, pulando itens ausentes, sem estrutura auxiliar proporcional ao tamanho da camada, é o mesmo padrão usado em **pipelines de processamento em ondas** (wavefront processing) de sistemas distribuídos, onde cada "onda" de tarefas gera a próxima sem precisar materializar todas as tarefas pendentes de uma vez.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
