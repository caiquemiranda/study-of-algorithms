# [0637] Average of Levels in Binary Tree

> 🔗 [LeetCode 637](https://leetcode.com/problems/average-of-levels-in-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#BFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne um array com a **média dos valores de cada nível**, na ordem da raiz para baixo.

**Exemplos:**
```
Input:  root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]

Input:  root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^4]` → precisa de solução O(n); a árvore nunca é vazia, então não existe caso de lista de resultado vazia
- `-2^31 <= Node.val <= 2^31 - 1` → valores cabem no limite de `int`, mas a **soma** de muitos nós de um nível pode facilmente estourar `int` (2^31 - 1 é o próprio limite de um único valor) — a soma acumulada precisa de `long`
- "resposta aceita com erro de até 10^-5" → sinaliza que o cálculo é feito com ponto flutuante (`double`), não precisa de precisão exata de fração

## 🧭 Como reconhecer o padrão

"Um valor por nível" é a assinatura mais direta de **BFS por nível**: processar a árvore camada por camada, agregando alguma coisa (aqui, soma e contagem) dentro de cada camada antes de passar para a próxima.

## 🐢 Solução 1 — Força bruta (DFS coletando todos os valores por nível)

DFS que, para cada nó visitado, adiciona o valor numa `List<Integer>` correspondente ao seu nível (criando a lista daquele nível na primeira vez que ele é alcançado). No final, percorre a lista de listas calculando a média de cada uma.

- Tempo: O(n) · Espaço: O(n) para guardar **todos** os valores individuais, agrupados por nível
- **Por que não basta:** guarda cada valor individualmente numa lista por nível, quando só a **soma** e a **contagem** de cada nível são necessárias para calcular a média — não é preciso lembrar cada valor depois de já tê-lo somado.

## 💡 Solução 2 — A ideia otimizada (intuição)

BFS com fila: processe a árvore nível a nível (usando o truque de "congelar `fila.size()`" antes do loop interno). Para cada nível, acumule só dois números — `soma` e `contagem` — e ao final do nível, calcule a média (`soma / contagem`) e descarte os valores individuais, sem nunca precisar de uma lista guardando cada um deles.

## 🎬 Exemplo passo a passo

`root = [3,9,20,null,null,15,7]`

```
      3
     / \
    9  20
      /  \
    15    7
```

| Nível | Nós processados | soma | contagem | média |
|---|---|---|---|---|
| 0 | [3] | 3 | 1 | 3.0 |
| 1 | [9, 20] | 29 | 2 | 14.5 |
| 2 | [15, 7] | 22 | 2 | 11.0 |

Resultado final: `[3.0, 14.5, 11.0]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez
- **Espaço:** O(largura da árvore) para a fila do BFS — não guarda nenhuma lista de valores por nível

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Double> averageOfLevels(TreeNode root) {
    List<Double> resultado = new ArrayList<>();
    Queue<TreeNode> fila = new ArrayDeque<>();
    fila.offer(root);

    while (!fila.isEmpty()) {
        int tamanhoNivel = fila.size(); // congela: só os nós DESTE nível
        long soma = 0; // long: soma de até 10^4 valores próximos de 2^31 estouraria int

        for (int i = 0; i < tamanhoNivel; i++) {
            TreeNode no = fila.poll();
            soma += no.val;

            if (no.left != null) fila.offer(no.left);
            if (no.right != null) fila.offer(no.right);
        }

        resultado.add((double) soma / tamanhoNivel); // média do nível, valores individuais já descartados
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

- Usar `int` para acumular `soma` em vez de `long` — com `Node.val` podendo chegar a `2^31 - 1` e até `10^4` nós por nível, a soma pode facilmente ultrapassar o limite de `int` e dar overflow silencioso (resultado errado sem erro nenhum).
- Fazer a divisão inteira (`soma / tamanhoNivel` com ambos `int`/`long`) antes de converter para `double` — perde a parte fracionária; é preciso converter **antes** de dividir, não depois.
- Esquecer de congelar `fila.size()` antes do loop interno — sem isso, os filhos recém-adicionados ao próximo nível se misturam com o processamento do nível atual, quebrando a separação entre níveis.
- Guardar todos os valores numa lista por nível (a força bruta) quando só soma e contagem interessam — funciona, mas gasta memória proporcional ao tamanho de cada nível à toa.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1]` | `[1.0]` | caso mínimo, um único nível |
| Árvore com valores extremos | `root = [2147483647,2147483647]` | `[2147483647.0, 2147483647.0]` | valida que `long` evita overflow mesmo em nível com valores no limite de `int` |
| Árvore assimétrica | `root = [3,9,20,null,null,15,7]` | `[3.0,14.5,11.0]` | cobre o exemplo do enunciado, testa contagem diferente por nível |
| Valores negativos | `root = [-5,-3,-7]` | `[-5.0,-5.0]` | garante que a soma e a média funcionam corretamente com negativos |

## 🔗 Conexões

- Problemas irmãos: [0102] Binary Tree Level Order Traversal (o mesmo esqueleto de BFS, mas retornando os valores em vez de agregá-los), [0111] Minimum Depth of Binary Tree (mesma técnica de BFS por nível, agregando uma condição de parada em vez de uma média)
- No backend: agregações por nível de uma hierarquia (soma, média, contagem) aparecem em relatórios organizacionais consolidados por nível hierárquico (ex.: custo médio por nível de gestão) e em métricas de árvores de decisão/roteamento onde cada "camada" de decisão precisa de uma estatística agregada antes de seguir para a próxima.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
