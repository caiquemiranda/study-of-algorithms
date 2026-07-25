# 13 — Programação Dinâmica 1D

> Dividir em subproblemas sobrepostos e nunca resolver o mesmo duas vezes. Problemas em [`../problemas/13_programacao_dinamica_1d/`](../problemas/13_programacao_dinamica_1d/).

## Conceito

DP se aplica quando o problema tem: **(1) subestrutura ótima** — a resposta se compõe de respostas de subproblemas — e **(2) subproblemas sobrepostos** — a recursão ingênua recalcula os mesmos estados.

**Os dois estilos (domine ambos):**
- **Top-down (memoization)**: recursão + cache. Mais fácil de derivar — escreva a força bruta e adicione `@lru_cache`
- **Bottom-up (tabulação)**: preenche a tabela na ordem das dependências. Mais rápido e permite otimizar espaço (ex.: guardar só os 2 últimos valores)

**O método em 4 passos (use sempre):**
1. **Estado**: o que define um subproblema? (`dp[i]` = melhor resposta considerando até i)
2. **Transição**: como `dp[i]` deriva de estados menores?
3. **Caso base**
4. **Resposta**: qual célula (ou combinação) responde o problema?

**Famílias 1D clássicas:**
- **Fibonacci-like**: `dp[i] = f(dp[i-1], dp[i-2])` — Climbing Stairs, House Robber
- **Unbounded knapsack**: Coin Change (`dp[valor] = min sobre moedas`)
- **Subsequência**: LIS — `dp[i]` = maior subsequência crescente terminando em i
- **Partição de string**: Word Break — `dp[i]` = "prefixo até i é segmentável?"

## Como reconhecer no enunciado

- "número de maneiras de..." → contagem por DP
- "mínimo/máximo custo para chegar a..." → otimização por DP
- "é possível...?" com escolhas sequenciais → DP booleana
- **Subsequência** (não contígua) → quase sempre DP
- Decisões em cadeia onde a escolha atual restringe as futuras — e n grande demais para backtracking

## Templates

```python
from functools import lru_cache

# Top-down — Coin Change (mínimo de moedas)
def coin_change(coins, amount):
    @lru_cache(None)
    def dp(resto):
        if resto == 0: return 0
        if resto < 0:  return float("inf")
        return 1 + min(dp(resto - c) for c in coins)
    r = dp(amount)
    return r if r != float("inf") else -1

# Bottom-up com espaço O(1) — House Robber
def rob(nums):
    ant2 = ant1 = 0                  # dp[i-2], dp[i-1]
    for n in nums:
        ant2, ant1 = ant1, max(ant1, ant2 + n)   # rouba ou pula
    return ant1

# LIS O(n log n) — pilhas de "menor cauda por comprimento"
import bisect
def length_of_lis(nums):
    caudas = []                      # caudas[k] = menor fim de LIS de tam k+1
    for n in nums:
        i = bisect.bisect_left(caudas, n)
        if i == len(caudas):
            caudas.append(n)
        else:
            caudas[i] = n
    return len(caudas)

# Word Break — partição de string
def word_break(s, palavras):
    dic = set(palavras)
    dp = [True] + [False] * len(s)   # dp[i]: s[:i] é segmentável
    for i in range(1, len(s) + 1):
        dp[i] = any(dp[j] and s[j:i] in dic for j in range(i))
    return dp[-1]
```

## Complexidade típica

O(n) a O(n²) tempo (nº de estados × custo da transição); espaço O(n), frequentemente reduzível a O(1) quando a transição só olha poucos estados anteriores.

## Erros comuns

- Definir o estado vago demais (se você não consegue escrever a transição, o estado está errado — refine-o)
- Ordem de preenchimento errada no bottom-up (usar célula ainda não calculada)
- Confundir subsequência (DP) com subarray (sliding window/Kadane)
- Coin Change: confundir "mínimo de moedas" (min) com "número de combinações" (soma — e a ordem dos loops muda! ver [14](14_programacao_dinamica_2d.md))
- Esquecer `@lru_cache` e achar que "recursão é lenta" (era a memoization que faltava)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 70. Climbing Stairs | 🟢 easy |
| 746. Min Cost Climbing Stairs | 🟢 easy |
| 198 / 213. House Robber I e II | 🟡 medium |
| 322. Coin Change | 🟡 medium |
| 300. Longest Increasing Subsequence | 🟡 medium |
| 139. Word Break | 🟡 medium |
| 152. Maximum Product Subarray | 🟡 medium |
| 91. Decode Ways | 🟡 medium |
| 647. Palindromic Substrings | 🟡 medium |

## Conexão com backend

Memoization É caching aplicado a função pura — o mesmo raciocínio de cache-aside (Vol. 2, E.2), só que em memória de processo. Retry com backoff, cálculo de janelas de agregação e otimizadores de plano de query usam DP de verdade por baixo.
