# 14 — Programação Dinâmica 2D

> Estados com duas dimensões: duas sequências, grade, ou item × capacidade. Problemas em [`../problemas/14_programacao_dinamica_2d/`](../problemas/14_programacao_dinamica_2d/).

## Conceito

Mesmo método do [13 — DP 1D](13_programacao_dinamica_1d.md) (estado → transição → base → resposta), mas o estado precisa de **dois índices**. As três famílias:

**1. Duas sequências** — `dp[i][j]` = resposta para os prefixos `s1[:i]` e `s2[:j]`:
- **LCS**: se os caracteres casam, `1 + dp[i-1][j-1]`; senão, `max(dp[i-1][j], dp[i][j-1])`
- **Edit Distance**: min entre inserir, remover, substituir — cada um é uma das 3 células vizinhas
- Este molde resolve: diff de arquivos, alinhamento, autocorreção

**2. Grade** — `dp[r][c]` = melhor forma de chegar à célula: `dp[r][c] = grid[r][c] + min/soma(dp[r-1][c], dp[r][c-1])`. Unique Paths, Minimum Path Sum.

**3. Knapsack (mochila)** — `dp[i][cap]` = melhor usando os i primeiros itens com capacidade cap:
- **0/1** (cada item uma vez): itera capacidade **decrescente** na versão 1D comprimida
- **Unbounded** (reuso ilimitado): capacidade crescente
- **Contagem de combinações** (Coin Change II): loop de **itens por fora** (senão conta permutações)

## Como reconhecer no enunciado

- Duas strings/arrays comparados ("transformar A em B", "subsequência comum")
- Caminhos em grade com custo/contagem
- "subconjunto que soma X" / "dividir em duas partes iguais" → knapsack (Partition, Target Sum)
- Intervalos onde a decisão divide o problema em esquerda+direita (Burst Balloons) → DP de intervalo, `dp[i][j]`

## Templates

```python
# LCS — O(n·m)
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

# Edit Distance — O(n·m)
def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): dp[i][0] = i        # apagar tudo
    for j in range(m + 1): dp[0][j] = j        # inserir tudo
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],     # remover
                                   dp[i][j-1],     # inserir
                                   dp[i-1][j-1])   # substituir
    return dp[n][m]

# Knapsack 0/1 comprimido — capacidade DECRESCENTE
def knapsack_01(pesos, valores, cap):
    dp = [0] * (cap + 1)
    for p, v in zip(pesos, valores):
        for c in range(cap, p - 1, -1):        # decrescente: item usado 1x
            dp[c] = max(dp[c], dp[c - p] + v)
    return dp[cap]

# Coin Change II — combinações: moedas POR FORA, capacidade crescente
def change(amount, coins):
    dp = [1] + [0] * amount
    for moeda in coins:
        for v in range(moeda, amount + 1):
            dp[v] += dp[v - moeda]
    return dp[amount]
```

## Complexidade típica

O(n·m) tempo e espaço; espaço reduzível a O(min(n, m)) guardando só a linha anterior. DP de intervalo: O(n³).

## Erros comuns

- Off-by-one entre índice da string (`i-1`) e índice da tabela (`i`) — padronize `dp[i]` = "prefixo de tamanho i"
- Knapsack 0/1 com capacidade crescente na versão 1D (reusa o item — vira unbounded silenciosamente)
- Contagem: inverter a ordem dos loops e contar permutações em vez de combinações
- Esquecer de inicializar linha 0 e coluna 0 (casos base do vazio)
- Tentar otimizar espaço antes de ter a versão 2D correta

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 62. Unique Paths | 🟡 medium |
| 64. Minimum Path Sum | 🟡 medium |
| 1143. Longest Common Subsequence | 🟡 medium |
| 518. Coin Change II | 🟡 medium |
| 416. Partition Equal Subset Sum | 🟡 medium |
| 494. Target Sum | 🟡 medium |
| 97. Interleaving String | 🟡 medium |
| 72. Edit Distance | 🟡 medium |
| 312. Burst Balloons (DP de intervalo) | 🔴 hard |
| 10. Regular Expression Matching | 🔴 hard |

## Conexão com backend

Edit distance move o mundo real: `git diff`, correção ortográfica, deduplicação fuzzy de cadastros, comparação de DNA. LCS é o coração de ferramentas de merge. Knapsack é alocação de recursos com orçamento — inclusive bin packing de containers em schedulers tipo Kubernetes.
