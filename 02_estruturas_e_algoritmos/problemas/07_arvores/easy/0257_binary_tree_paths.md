# [0257] Binary Tree Paths

> 🔗 [LeetCode 257](https://leetcode.com/problems/binary-tree-paths/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#Backtracking` `#DFS`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne **todos os caminhos raiz-até-folha**, em qualquer ordem, formatados como strings no padrão `"1->2->5"`.

**Exemplos:**
```
Input:  root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input:  root = [1]
Output: ["1"]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 100]` → entrada pequena, o custo de manipulação de string não é o gargalo aqui, mas o hábito importa para árvores maiores
- `-100 <= Node.val <= 100` → valores cabem em `int`, mas viram texto no resultado (formato `"->"` entre eles)
- A árvore sempre tem **pelo menos 1 nó** (`[1, 100]`, não `[0, 100]`) → não existe caso de árvore vazia para tratar aqui, diferente de outros problemas de árvore

## 🧭 Como reconhecer o padrão

"Retorne todos os caminhos raiz-folha" é **backtracking** disfarçado de árvore: descer construindo o caminho atual, e quando chegar numa folha, "salvar uma foto" desse caminho na lista de respostas. A palavra-chave é "todos os caminhos", não "existe um caminho" (que seria só DFS booleano, como em [0112] Path Sum).

## 🐢 Solução 1 — Força bruta (concatenar strings a cada nível)

DFS que, em vez de carregar uma lista de valores, vai **concatenando** a string do caminho a cada nível (`caminhoAtual + "->" + node.val`) e passando a nova string para as chamadas recursivas dos filhos.

- Tempo: O(n²) no pior caso · Espaço: O(n²) no pior caso
- **Por que não basta:** `String` é imutável em Java — cada concatenação `caminhoAtual + "->" + valor` cria um objeto novo, copiando todo o conteúdo anterior. Numa árvore degenerada de profundidade n, o último caminho tem comprimento O(n), e ele foi reconstruído por cópia a cada um dos n níveis — o custo total de todas as concatenações soma O(n²) em tempo e memória, mesmo que a resposta final "pareça" O(n).

## 💡 Solução 2 — A ideia otimizada (intuição)

Use uma estrutura mutável (uma `List<String>` ou `StringBuilder`) para acumular o caminho enquanto desce, e **desfaça** a última adição ao subir da recursão (o "back" do backtracking) — em vez de criar uma string nova a cada nível, o mesmo buffer é reaproveitado para todos os ramos da árvore, adicionando e removendo peças conforme a DFS avança e retrocede.

## 🎬 Exemplo passo a passo

`root = [1,2,3,null,5]` (2 é filho esquerdo de 1, com filho direito 5; 3 é filho direito de 1)

```
    1
   / \
  2   3
   \
    5
```

| Passo | Nó | Caminho (lista mutável) | É folha? | Ação |
|---|---|---|---|---|
| 1 | 1 | `[1]` | não | desce para 2 |
| 2 | 2 | `[1,2]` | não | desce para 5 |
| 3 | 5 | `[1,2,5]` | sim | salva `"1->2->5"`, depois **remove** o 5 ao retroceder |
| 4 | volta a 2, sem mais filhos | `[1,2]` → remove 2 | — | retrocede até 1 |
| 5 | 1 | `[1]` | não | desce para 3 |
| 6 | 3 | `[1,3]` | sim | salva `"1->3"`, depois remove o 3 |

Resultado final: `["1->2->5", "1->3"]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) no pior caso — mesmo com backtracking, formatar cada um dos até O(n) caminhos em string ainda custa O(comprimento do caminho); a diferença real está no espaço, não no tempo assintótico total
- **Espaço:** O(n) para a estrutura mutável do caminho atual (compartilhada entre todos os ramos, não recriada), mais O(n) para a lista de resultados

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<String> binaryTreePaths(TreeNode root) {
    List<String> resultado = new ArrayList<>();
    dfs(root, new ArrayList<>(), resultado);
    return resultado;
}

private void dfs(TreeNode no, List<Integer> caminho, List<String> resultado) {
    if (no == null) return;

    caminho.add(no.val); // adiciona ANTES de decidir se é folha

    if (no.left == null && no.right == null) {
        // folha: "tira uma foto" do caminho atual formatando como string
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < caminho.size(); i++) {
            if (i > 0) sb.append("->");
            sb.append(caminho.get(i));
        }
        resultado.add(sb.toString());
    } else {
        dfs(no.left, caminho, resultado);
        dfs(no.right, caminho, resultado);
    }

    caminho.remove(caminho.size() - 1); // BACKTRACK: desfaz este nó antes de subir para o pai
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

- Esquecer o `caminho.remove(caminho.size() - 1)` no final — sem desfazer, o mesmo buffer mutável vaza valores de um ramo para os ramos irmãos seguintes, misturando ancestrais que não têm relação.
- Concatenar strings ingenuamente a cada nível (a força bruta) — funciona para árvores de 100 nós como aqui, mas é o hábito errado a carregar para problemas maiores.
- Formatar a string **antes** de saber se o nó é folha — o formato `"1->2->5"` não tem separador à direita do último elemento, então formatar cedo demais complica a lógica de "quando colocar o `->`".
- Passar a **mesma instância** de `List<Integer>` sem cuidado entre chamadas irmãs, mas esquecendo o backtrack — resultaria em todos os caminhos salvos apontando para a mesma lista final (mutada), corrompendo respostas já salvas. (Note que o problema aqui não ocorre porque só formatamos a string, que é imutável, no momento da folha — mas seria um bug real se a lista fosse salva por referência.)

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1]` | `["1"]` | a própria raiz já é folha, caminho de tamanho 1 |
| Só filhos de um lado (skew) | `root = [1,2,null,3]` | `["1->2->3"]` | um único caminho, mas testa a formatação com 3 níveis |
| Duas folhas em ramos diferentes | `root = [1,2,3,null,5]` | `["1->2->5","1->3"]` | cobre o exemplo do enunciado, valida o backtrack entre ramos irmãos |
| Árvore balanceada com 4 folhas | `root = [1,2,3,4,5,6,7]` | 4 caminhos de tamanho 3 cada | garante que o backtrack limpa corretamente entre múltiplos ramos consecutivos |

## 🔗 Conexões

- Problemas irmãos: [0112] Path Sum (mesma estrutura de descida raiz-folha, mas responde só `true`/`false` em vez de coletar todos os caminhos), [0113] Path Sum II (praticamente este problema combinado com [0112]: coleta os caminhos que também batem com uma soma-alvo)
- No backend: enumerar todos os caminhos raiz-folha é o mesmo padrão usado para listar todas as rotas possíveis de navegação num menu hierárquico, ou para gerar todos os "breadcrumbs" possíveis de uma árvore de categorias de um catálogo de produtos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
