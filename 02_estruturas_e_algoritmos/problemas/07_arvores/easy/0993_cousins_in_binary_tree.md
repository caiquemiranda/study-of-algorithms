# [0993] Cousins in Binary Tree

> 🔗 [LeetCode 993](https://leetcode.com/problems/cousins-in-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#BFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária com valores únicos e dois valores `x` e `y`, retorne `true` se os nós correspondentes forem **primos**: mesma profundidade, mas pais diferentes.

**Exemplos:**
```
Input:  root = [1,2,3,4], x = 4, y = 3
Output: false

Input:  root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Input:  root = [1,2,3,null,4], x = 2, y = 3
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[2, 100]` → entrada pequena, qualquer O(n) resolve
- `1 <= Node.val <= 100`, valores **únicos** → não há ambiguidade sobre "qual nó" corresponde a `x` ou `y`
- `x != y`, ambos garantidamente existem na árvore → não é preciso tratar o caso de um valor não encontrado

## 🧭 Como reconhecer o padrão

"Mesma profundidade, pais diferentes" exige saber **duas** coisas sobre cada nó ao mesmo tempo: sua profundidade e quem é seu pai — informação que só existe se você a carregar durante a descida (igual a [0404] Sum of Left Leaves, que também precisa de contexto do pai). Como a pergunta é sobre profundidade, BFS por nível é a ferramenta mais natural: processa exatamente os nós de uma profundidade de cada vez.

## 🐢 Solução 1 — Força bruta (duas buscas DFS separadas)

Fazer uma busca DFS completa para achar a profundidade e o pai de `x`, e depois **outra** busca DFS completa, do zero, para achar a profundidade e o pai de `y`.

- Tempo: O(2n) — efetivamente duas passadas completas pela árvore · Espaço: O(h) por busca
- **Por que não basta:** não é assintoticamente pior (ainda é O(n)), mas visita a árvore duas vezes quando uma única passada já pode responder as duas perguntas ao mesmo tempo — desperdício de trabalho redundante.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única BFS por nível: ao processar os nós de um nível (os **pais**), olhe os filhos deles antes de enfileirá-los. Se um filho tiver valor `x`, registre o nó atual como `paiX`; se for `y`, registre como `paiY`. Depois de processar todos os pais daquele nível (ou seja, depois de terminar de examinar os filhos, que formam o próximo nível inteiro), cheque: se **ambos** `paiX` e `paiY` foram encontrados, `x` e `y` estão na mesma profundidade — a resposta é `true` só se os pais forem **diferentes**. Se só um foi encontrado, as profundidades são diferentes e a resposta já é `false`.

## 🎬 Exemplo passo a passo

`root = [1,2,3,null,4,null,5]`, `x = 5, y = 4` (2 é filho esquerdo de 1, com filho direito 4; 3 é filho direito de 1, com filho direito 5)

```
      1
     / \
    2   3
     \   \
      4   5
```

| Iteração do laço | Pais processados neste nível | Filhos examinados | paiX (valor 5) | paiY (valor 4) | Ação |
|---|---|---|---|---|---|
| 1 | [1] | 2, 3 | não achou | não achou | nenhum encontrado, continua |
| 2 | [2, 3] | 4 (filho de 2), 5 (filho de 3) | achou: nó `3` | achou: nó `2` | ambos encontrados neste nível, pais diferentes (3 ≠ 2) → `true` |

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada BFS, cada nó visitado uma vez
- **Espaço:** O(largura da árvore) para a fila do BFS

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isCousins(TreeNode root, int x, int y) {
    Queue<TreeNode> fila = new ArrayDeque<>();
    fila.offer(root);

    while (!fila.isEmpty()) {
        int tamanhoNivel = fila.size(); // congela: só os PAIS deste nível
        TreeNode paiX = null, paiY = null;

        for (int i = 0; i < tamanhoNivel; i++) {
            TreeNode no = fila.poll();

            // examina os FILHOS (o próximo nível) antes de enfileirá-los
            if (no.left != null) {
                if (no.left.val == x) paiX = no;
                if (no.left.val == y) paiY = no;
                fila.offer(no.left);
            }
            if (no.right != null) {
                if (no.right.val == x) paiX = no;
                if (no.right.val == y) paiY = no;
                fila.offer(no.right);
            }
        }

        // ambos apareceram no mesmo nível: só são primos se os pais forem diferentes
        if (paiX != null && paiY != null) return paiX != paiY;

        // só um apareceu: profundidades diferentes, nunca serão primos
        if (paiX != null || paiY != null) return false;
    }

    return false; // inatingível na prática, já que x e y sempre existem na árvore
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

- Checar só a profundidade e esquecer de comparar os pais — dois irmãos (mesmo pai) também têm a mesma profundidade, mas **não** são primos; a condição precisa das duas coisas ao mesmo tempo: mesma profundidade **e** pais diferentes.
- Comparar `x` e `y` como se fossem o próprio nó (`no == x`) em vez de comparar `no.val == x` — `x` e `y` são valores (`int`), não referências de nó.
- Achar que basta checar se um é filho do outro — "primos" é sobre **profundidade compartilhada com pais diferentes**, não sobre relação de ancestralidade direta.
- Declarar `paiX`/`paiY` **fora** do laço `while` (uma única vez, antes de tudo) em vez de dentro dele, a cada iteração — sem reiniciá-los a cada nível, um valor encontrado num nível anterior "vazaria" para a comparação do nível seguinte.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Irmãos diretos (mesmo pai) | `root = [1,2,3,4], x = 4, y = 3` | `false` | cobre o exemplo 1: mesma profundidade não basta se o pai for o mesmo (aqui nem é o caso, mas profundidades diferentes) |
| Primos válidos | `root = [1,2,3,null,4,null,5], x = 5, y = 4` | `true` | cobre o exemplo 2, caso positivo central do problema |
| Pai e filho (profundidades diferentes) | `root = [1,2,3,null,4], x = 2, y = 3` | `false` | cobre o exemplo 3, ambos existem mas em profundidades diferentes |
| Um dos dois na raiz | `root = [1,2,3], x = 1, y = 3` | `false` | a raiz não tem pai (profundidade 0), nunca pode ser prima de ninguém |

## 🔗 Conexões

- Problemas irmãos: [0637] Average of Levels in Binary Tree (mesmo esqueleto de BFS por nível, agregando informação diferente), [0111] Minimum Depth of Binary Tree (mesma técnica de BFS, mas parando na primeira condição satisfeita)
- No backend: verificar se dois registros estão no mesmo "nível" de uma hierarquia mas sob "ramos" diferentes aparece em validação de regras de organograma (dois funcionários no mesmo nível hierárquico, mas em departamentos diferentes) e em detecção de relações estruturais equivalentes em árvores de categorização.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
