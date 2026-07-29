# [0096] Unique Binary Search Trees

> 🔗 [LeetCode 96](https://leetcode.com/problems/unique-binary-search-trees/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#ProgramacaoDinamica` `#NumerosDeCatalan`

## 📜 O Problema

Dado um inteiro `n`, retorne o **número** de BSTs estruturalmente diferentes que têm exatamente `n` nós com valores únicos de `1` a `n`.

**Exemplos:**
```
Input:  n = 3
Output: 5

Input:  n = 1
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 19` → o range é maior que em [0095] (que só ia até 8), porque aqui não é preciso **construir** nenhuma árvore, só contar — contar é muito mais barato que gerar; `n = 19` já se aproxima do limite de `int` para o número de Catalan correspondente
- Valores de `1` a `n` → a contagem depende só de **quantos** valores existem, não de quais são (a estrutura de possibilidades é a mesma para qualquer intervalo contíguo de `n` valores)

## 🧭 Como reconhecer o padrão

"Quantas estruturas diferentes existem" (sem precisar listá-las) é o sinal clássico de trocar "gerar tudo" por **programação dinâmica**: se você já sabe quantas BSTs existem para intervalos menores, pode combinar essas contagens (multiplicando, não enumerando) para achar a contagem do intervalo maior — é a mesma ideia de [0095], mas contando combinações em vez de construir cada uma.

## 🐢 Solução 1 — Força bruta (gerar todas as árvores e contar)

Reaproveitar a lógica de [0095] Unique Binary Search Trees II para gerar de fato **todas** as árvores possíveis, e retornar o tamanho da lista resultante.

- Tempo: O(Catalan(n) · n) — o mesmo custo de gerar todas as árvores · Espaço: O(Catalan(n) · n) para guardar árvores completas que serão descartadas logo em seguida
- **Por que não basta:** desperdiça memória e tempo alocando `TreeNode`s inteiros só para, no final, jogar tudo fora e ficar só com um número. A pergunta é "quantas", não "quais" — não é preciso materializar nenhuma árvore para responder isso.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada valor `i` de `1` a `n`, escolhido como raiz: o número de BSTs possíveis com raiz `i` é `(número de formas de organizar a esquerda) × (número de formas de organizar a direita)` — e a esquerda tem `i-1` valores, a direita tem `n-i` valores. Como a contagem de "quantas BSTs existem para k valores" só depende de **quantos** valores há (não de quais), você pode guardar isso num array `dp[]` e reaproveitar: `dp[n] = soma, para i de 1 a n, de dp[i-1] * dp[n-i]`. Essa é a definição dos **números de Catalan**.

## 🎬 Exemplo passo a passo

`n = 3` — construindo `dp[]` de baixo para cima

| k | Cálculo de dp[k] | dp[k] |
|---|---|---|
| 0 | caso base: intervalo vazio tem 1 forma (nenhuma árvore) | 1 |
| 1 | dp[0]\*dp[0] (só um valor, só uma forma) | 1 |
| 2 | i=1: dp[0]\*dp[1] + i=2: dp[1]\*dp[0] = 1+1 | 2 |
| 3 | i=1: dp[0]\*dp[2] + i=2: dp[1]\*dp[1] + i=3: dp[2]\*dp[0] = 2+1+2 | **5** |

Resultado final: `5` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) — para cada um dos n valores de `dp[]`, soma-se até n termos
- **Espaço:** O(n) — o array `dp[]` de tamanho `n+1`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numTrees(int n) {
    int[] dp = new int[n + 1];
    dp[0] = 1; // intervalo vazio: exatamente 1 forma (a "árvore nula")

    for (int total = 1; total <= n; total++) {
        // i é o valor escolhido como raiz dentro de um intervalo de "total" valores
        for (int i = 1; i <= total; i++) {
            int tamanhoEsquerda = i - 1;
            int tamanhoDireita = total - i;
            // combinações independentes: formas da esquerda VEZES formas da direita
            dp[total] += dp[tamanhoEsquerda] * dp[tamanhoDireita];
        }
    }

    return dp[n];
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

- Esquecer `dp[0] = 1` — o caso base parece contraintuitivo ("zero valores tem UMA forma?"), mas é essencial: representa "não ter subárvore" como uma opção válida e única, necessária para o produto funcionar corretamente quando `i` é o primeiro ou o último valor do intervalo.
- Confundir `tamanhoEsquerda`/`tamanhoDireita` com os **valores** reais do intervalo — o `dp[]` é indexado pela **quantidade** de valores, não por quais valores são; por isso a mesma tabela serve para qualquer intervalo contíguo, não só `1..n`.
- Gerar todas as árvores (a força bruta, reaproveitando [0095]) quando só a contagem interessa — funciona para `n` pequeno, mas não escala até `n = 19` como a versão DP escala.
- Usar recursão ingênua sem memoização para calcular `dp[total]` — sem guardar resultados já calculados, a mesma subcontagem (ex.: `dp[2]`) seria recalculada do zero múltiplas vezes, perdendo o ganho da programação dinâmica.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| n = 1 | `n = 1` | `1` | caso base, um nó só tem uma única forma |
| n = 2 | `n = 2` | `2` | menor caso com mais de uma estrutura possível |
| n = 3 | `n = 3` | `5` | cobre o exemplo do enunciado |
| n = 19 (limite superior) | `n = 19` | `1767263190` | valida que `dp[]` com `int` ainda comporta o maior número de Catalan dentro do range garantido, sem overflow |

## 🔗 Conexões

- Problemas irmãos: [0095] Unique Binary Search Trees II (a versão que constrói e retorna todas as árvores, em vez de só contar), [0022] Generate Parentheses (também é contado/gerado pelos números de Catalan, mesma estrutura combinatória por trás)
- No backend: os números de Catalan aparecem em qualquer contagem de estruturas balanceadas recursivamente decompostas — número de formas de triangular um polígono, número de caminhos válidos em treliças, e em otimizadores de banco de dados ao contar quantas ordens de junção (join order) distintas são possíveis para `n` tabelas antes de escolher a mais barata.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
