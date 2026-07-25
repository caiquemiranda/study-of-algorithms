# 14 — Programação Dinâmica 2D

> Estados com duas dimensões: duas sequências, grades e mochilas. Soluções em [`../problemas/14_programacao_dinamica_2d/`](../problemas/14_programacao_dinamica_2d/).

## 1. Conceito Central e Analogia Didática

- Mesmo método do [13 — DP 1D](13_programacao_dinamica_1d.md), mas o estado carrega **dois índices**: `dp[i][j]` = resposta para os prefixos `s1[:i]` e `s2[:j]` (ou célula da grade, ou item × capacidade).
- Três famílias dominam: **duas sequências** (LCS, Edit Distance), **grade** (caminhos), **knapsack** (subconjunto que atinge capacidade).
- Truque de compressão: se a transição só olha a **linha anterior**, uma linha basta — e no knapsack 0/1, a **direção do loop** de capacidade decide se o item pode repetir.

**Analogia (LCS):** comparar duas trilhas de música numa mesa de mixagem: você avança dois cursores; quando os trechos casam, ganha 1 e avança os dois; quando não casam, testa avançar cada cursor separadamente e fica com o melhor. A tabela é a memória de todas as combinações de posições já comparadas.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se compara **duas strings/arrays** ("transformar A em B", "subsequência comum") → tabela (n+1)×(m+1).
- Se pede caminhos/custos **numa grade** andando para direita/baixo → DP de grade.
- Se pede "**subconjunto que soma X**" / "dividir em duas partes iguais" → knapsack (Partition, Target Sum).
- Se pede "número de **combinações** que somam X" com reuso → unbounded, itens no loop de FORA.
- Se a decisão divide o problema em esquerda+direita (Burst Balloons) → DP de intervalo, O(n³).

## 3. Templates de Código

### LCS (duas sequências)

```java
// Java — dp[i][j] = LCS dos prefixos a[0..i) e b[0..j); índice da tabela = TAMANHO do prefixo
public int longestCommonSubsequence(String a, String b) {
    int n = a.length(), m = b.length();
    int[][] dp = new int[n + 1][m + 1];          // linha/coluna 0 = prefixo vazio (base já em 0)
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a.charAt(i - 1) == b.charAt(j - 1)) {   // i-1/j-1: tabela é 1-based, string 0-based
                dp[i][j] = 1 + dp[i - 1][j - 1]; // casou: estende a diagonal (os dois avançam)
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); // não casou: melhor de pular um lado
            }
        }
    }
    return dp[n][m];
}
```

```python
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]        # diagonal: casamento consome os dois chars
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]
```

### Knapsack 0/1 comprimido (Partition / Target Sum)

```java
// Java — 1 dimensão; capacidade DECRESCENTE garante que cada item entra no máximo 1 vez
public boolean canPartition(int[] nums) {
    int soma = Arrays.stream(nums).sum();
    if (soma % 2 != 0) return false;
    int alvo = soma / 2;
    boolean[] dp = new boolean[alvo + 1];
    dp[0] = true;                                  // soma 0 sempre alcançável (conjunto vazio)
    for (int n : nums) {
        for (int c = alvo; c >= n; c--) {          // DECRESCENTE: dp[c-n] ainda é da rodada anterior
            dp[c] = dp[c] || dp[c - n];            // com o item (dp[c-n]) ou sem (dp[c])
        }
    }
    return dp[alvo];
}
```

```python
def can_partition(nums):
    soma = sum(nums)
    if soma % 2:
        return False
    alvo = soma // 2
    dp = [True] + [False] * alvo
    for n in nums:
        for c in range(alvo, n - 1, -1):   # decrescente = 0/1; crescente viraria reuso infinito
            dp[c] = dp[c] or dp[c - n]
    return dp[alvo]
```

### Coin Change II (contagem de COMBINAÇÕES)

```python
def change(amount, coins):
    dp = [1] + [0] * amount            # 1 forma de somar 0: não usar nada
    for moeda in coins:                # moedas por FORA: fixa a ordem => conta combinações
        for v in range(moeda, amount + 1):
            dp[v] += dp[v - moeda]     # loops invertidos contariam PERMUTAÇÕES (1+2 e 2+1 dobrados)
    return dp[amount]
```

## 4. Walkthrough Visual (Teste de Mesa)

`lcs("ace", "abe")` — tabela `dp` (linhas = "ace", colunas = "abe"):

|  | "" | a | b | e |
|---|---|---|---|---|
| **""** | 0 | 0 | 0 | 0 |
| **a** | 0 | **1**↖ | 1 | 1 |
| **c** | 0 | 1 | 1 | 1 |
| **e** | 0 | 1 | 1 | **2**↖ |

- `a==a` → diagonal+1; `c` não casa com nada → herda o max dos vizinhos; `e==e` → 1+dp[2][2] = **2**.
- LCS = "ae", tamanho **2** ✔ — a seta ↖ marca onde houve casamento.

## 5. Complexidade (Tempo e Espaço)

| Família | Tempo | Espaço |
|---|---|---|
| Duas sequências | O(n·m) | O(n·m) → O(min(n,m)) com 1 linha |
| Grade | O(R·C) | O(C) comprimido |
| Knapsack | O(n·capacidade) | O(capacidade) |
| DP de intervalo | O(n³) | O(n²) |

- Knapsack é "pseudo-polinomial": cresce com o **valor** da capacidade, não com o tamanho do input — capacidade de 10⁹ inviabiliza.

## 6. Pegadinhas e Erros Comuns

- **Off-by-one**: `dp[i]` = prefixo de TAMANHO i → o char correspondente é `s[i-1]`. Padronize e nunca mais erre.
- Knapsack 0/1 com capacidade **crescente** na versão comprimida → item reutilizado silenciosamente (vira unbounded).
- Contagem: **itens fora, capacidade dentro = combinações**; invertido = permutações — decore com o exemplo 1+2 vs 2+1.
- Esquecer a linha/coluna 0 (caso base do vazio) → tabela inteira errada.
- **Java**: `new int[n][m]` já vem zerado; `Boolean[][]` (wrapper) vem `null` — NPE ao ler sem inicializar.
- **Python**: `[[0]*m]*n` cria n REFERÊNCIAS à mesma linha — mutação em uma muda todas; use list comprehension.
- Otimizar espaço **antes** de ter a versão 2D correta e testada — depure na tabela cheia.

## 7. Aplicações no Mundo Real (Backend)

- **Edit distance move o mundo**: `git diff`, correção ortográfica, deduplicação fuzzy de cadastros de clientes, bioinformática.
- **LCS**: motores de merge de 3 vias e ferramentas de comparação de versões de documentos.
- **Knapsack**: alocação com orçamento — bin packing de pods no Kubernetes, seleção de features por custo/benefício, otimização de carga.
- **PostgreSQL**: `levenshtein()` do módulo `fuzzystrmatch` é o Edit Distance rodando no banco.
- Diff de configuração/estado (Terraform plan, reconciliação do K8s) é a família de duas sequências.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | 🟡 Medium |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 🟡 Medium |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 🟡 Medium |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | 🟡 Medium |
| 518 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | 🟡 Medium |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🟡 Medium |
| 312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | 🔴 Hard |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard |
