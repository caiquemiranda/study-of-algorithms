# [0111] Minimum Depth of Binary Tree

> 🔗 [LeetCode 111](https://leetcode.com/problems/minimum-depth-of-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#BFS` `#Easy`

## 📜 O Problema

Dado um `root` de árvore binária, encontre a **profundidade mínima**: o número de nós ao longo do caminho mais curto da raiz até a **folha** mais próxima. Uma folha é um nó sem filhos.

**Exemplos:**
```
Input:  root = [3,9,20,null,null,15,7]
Output: 2

Input:  root = [2,null,3,null,4,null,5,null,6]
Output: 5
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^5]` → precisa de O(n), e a versão com early-exit da BFS pode terminar bem antes de visitar todos os nós em árvores assimétricas
- `-1000 <= Node.val <= 1000` → valores não importam para este problema, só a estrutura
- O exemplo 2 é a pegadinha do problema: é uma árvore só com filhos à direita, então a "profundidade mínima" não pode ser 1 (a raiz não é folha, ela tem um filho) — a resposta é o caminho inteiro até a única folha que existe

## 🧭 Como reconhecer o padrão

Parece o gêmeo de [0104] Maximum Depth, mas **não é** só trocar `max` por `min` — a definição exige que o caminho termine numa **folha real** (sem filhos), não em qualquer nó nulo. Essa restrição de "tem que ser folha" é o sinal de que BFS com parada antecipada é mais natural aqui: assim que a primeira folha aparece (varrendo nível a nível), essa é garantidamente a resposta, sem precisar visitar o resto da árvore.

## 🐢 Solução 1 — Força bruta (DFS completo até todas as folhas)

Percorrer a árvore inteira via DFS, calculando a profundidade de **cada** folha encontrada, e no final retornar o menor valor entre todas elas.

- Tempo: O(n) · Espaço: O(h)
- **Por que não basta:** não está errado nem é lento no sentido de complexidade assintótica — mas visita nós desnecessariamente. Numa árvore onde a folha mais próxima está a 2 níveis da raiz mas a árvore inteira tem 10^5 nós espalhados por outros ramos profundos, o DFS completo processa tudo antes de "perceber" que já tinha achado a resposta lá no início.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça BFS nível a nível a partir da raiz. Assim que encontrar o **primeiro** nó que é folha (sem `left` e sem `right`), pare imediatamente — como BFS visita em ordem de distância crescente da raiz, essa é garantidamente a folha mais próxima, e não há necessidade de continuar explorando níveis mais fundos.

## 🎬 Exemplo passo a passo

`root = [2,null,3,null,4,null,5,null,6]` (só filhos à direita, uma corrente)

```
2
 \
  3
   \
    4
     \
      5
       \
        6
```

| Nível | Fila processada | Nó é folha? | Ação |
|---|---|---|---|
| 1 | [2] | não (tem filho direito 3) | empilha 3 para o próximo nível |
| 2 | [3] | não (tem filho direito 4) | empilha 4 |
| 3 | [4] | não (tem filho direito 5) | empilha 5 |
| 4 | [5] | não (tem filho direito 6) | empilha 6 |
| 5 | [6] | **sim**, sem filhos | retorna nível atual = 5 |

Resultado final: `5` ✔ (bate com o enunciado — a "trapaça" de olhar só o filho mais próximo da raiz erraria achando que é 1)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no pior caso (árvore onde a folha mais próxima está no último nível, ex.: árvore perfeitamente balanceada), mas **melhor que O(n)** em árvores assimétricas onde a folha mais próxima aparece cedo
- **Espaço:** O(largura da árvore) para a fila do BFS

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minDepth(TreeNode root) {
    if (root == null) return 0; // árvore vazia: profundidade 0

    Queue<TreeNode> fila = new ArrayDeque<>();
    fila.offer(root);
    int profundidade = 1; // a raiz já conta como o primeiro nível

    while (!fila.isEmpty()) {
        int tamanhoNivel = fila.size(); // congela: só os nós DESTE nível

        for (int i = 0; i < tamanhoNivel; i++) {
            TreeNode no = fila.poll();

            // folha real (sem filho nenhum): achamos o caminho mais curto possível
            if (no.left == null && no.right == null) {
                return profundidade;
            }

            if (no.left != null) fila.offer(no.left);
            if (no.right != null) fila.offer(no.right);
        }

        profundidade++; // terminou o nível inteiro sem achar folha, desce mais um
    }

    return profundidade; // inatingível na prática, mas mantém o método total
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

- Copiar a solução de [0104] Maximum Depth e trocar `max` por `min` cegamente — `1 + Math.min(altura(left), altura(right))` quebra quando um dos lados é `null`: `altura(null)` retorna 0, e o `min` escolheria erroneamente o lado vazio como "o caminho mais curto", quando na verdade um nó com só um filho **não é** folha e não conta.
- Esquecer que um nó com **apenas um filho** não é folha — precisa continuar descendo pelo lado que existe, não pode parar ali achando que "não tem os dois filhos, então é folha o suficiente".
- Usar DFS pós-ordem ingênuo sem tratar o caso de filho único corretamente (mesma pegadinha acima, só que na versão recursiva): a versão DFS correta precisa de um `if` explícito para "só tem um filho → desça por ele, não use o outro lado como 0".
- Achar que BFS é sempre "mais lento" que DFS por usar fila — aqui é o contrário: o early-exit da BFS pode terminar muito antes de visitar a árvore inteira, algo que o DFS completo não aproveita.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `0` | caso base sem nós |
| Um nó só | `root = [1]` | `1` | a própria raiz já é folha |
| Só filhos de um lado (skew) | `root = [2,null,3,null,4,null,5,null,6]` | `5` | cobre o exemplo 2; testa a pegadinha "nó com um filho não é folha" |
| Árvore balanceada | `root = [3,9,20,null,null,15,7]` | `2` | a folha mais próxima (9) está no segundo nível, BFS para cedo |

## 🔗 Conexões

- Problemas irmãos: [0104] Maximum Depth of Binary Tree (o "oposto" superficial, mas sem a pegadinha de exigir folha real), [0102] Binary Tree Level Order Traversal (mesmo esqueleto de BFS por nível, sem o early-exit)
- No backend: BFS com parada antecipada é o mesmo princípio de busca do "vizinho mais próximo que satisfaz uma condição" em grafos de roteamento (ex.: achar o servidor disponível mais próximo numa topologia hierárquica) — parar assim que a primeira solução válida aparece, sem varrer o grafo inteiro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
