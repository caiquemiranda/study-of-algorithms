# 13 — Programação Dinâmica 1D

> Subproblemas sobrepostos: resolva cada um UMA vez. Soluções em [`../problemas/13_programacao_dinamica_1d/`](../problemas/13_programacao_dinamica_1d/).

## 1. Conceito Central e Analogia Didática

- DP exige duas propriedades: **subestrutura ótima** (a resposta se monta com respostas menores) + **subproblemas sobrepostos** (a recursão ingênua recalcula os mesmos estados).
- Dois estilos: **top-down** (recursão + cache; derive da força bruta) e **bottom-up** (tabela preenchida na ordem das dependências; permite otimizar espaço).
- Método de 4 passos, sempre: **1) estado** → **2) transição** → **3) caso base** → **4) onde está a resposta**.

**Analogia:** subir uma escada contando de quantas formas se chega a cada degrau: o degrau 10 não recalcula nada — só **soma o que já foi contado** nos degraus 9 e 8. Anotar o resultado de cada degrau na parede é a memoization.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "**número de maneiras** de..." → DP de contagem.
- Se pede "**custo mínimo / lucro máximo** para chegar a..." → DP de otimização.
- Se pede "**é possível...?**" com decisões em sequência → DP booleana.
- Se fala em **subsequência** (não contígua) → quase sempre DP.
- Se o backtracking estoura (n até 10³–10⁵) e há estados repetidos → memoize: virou DP.

## 3. Templates de Código

### Top-down (Coin Change — mínimo de moedas)

```java
// Java — força bruta + cache: o memo transforma exponencial em O(valor × moedas)
public int coinChange(int[] coins, int amount) {
    int[] memo = new int[amount + 1];
    Arrays.fill(memo, -2);                        // -2 = "nunca calculado" (evita recomputar)
    return dp(coins, amount, memo);
}

private int dp(int[] coins, int resto, int[] memo) {
    if (resto == 0) return 0;                     // caso base: nada a pagar, zero moedas
    if (resto < 0) return -1;                     // caminho inválido: estourou o valor
    if (memo[resto] != -2) return memo[resto];    // subproblema já resolvido: reaproveita
    int melhor = Integer.MAX_VALUE;
    for (int c : coins) {
        int sub = dp(coins, resto - c, memo);
        if (sub >= 0) melhor = Math.min(melhor, sub + 1); // +1 = a moeda usada agora
    }
    memo[resto] = (melhor == Integer.MAX_VALUE) ? -1 : melhor;
    return memo[resto];
}
```

```python
from functools import lru_cache

def coin_change(coins, amount):
    @lru_cache(None)                       # o cache É a diferença entre TLE e aceito
    def dp(resto):
        if resto == 0: return 0
        if resto < 0:  return float("inf") # inválido: infinito para perder no min()
        return 1 + min(dp(resto - c) for c in coins)
    r = dp(amount)
    return r if r != float("inf") else -1
```

### Bottom-up com espaço O(1) (House Robber)

```java
// Java — a transição só olha 2 estados atrás: a tabela inteira é desnecessária
public int rob(int[] nums) {
    int ant2 = 0, ant1 = 0;                 // dp[i-2] e dp[i-1] comprimidos em 2 variáveis
    for (int n : nums) {
        int atual = Math.max(ant1, ant2 + n); // decide: pula esta casa OU rouba (casa + dp[i-2])
        ant2 = ant1;                          // desliza a janela de estados
        ant1 = atual;
    }
    return ant1;
}
```

```python
def rob(nums):
    ant2 = ant1 = 0
    for n in nums:
        ant2, ant1 = ant1, max(ant1, ant2 + n)  # rouba (ant2+n) ou pula (ant1)
    return ant1
```

### LIS em O(n log n) (bônus: DP + busca binária)

```python
import bisect

def length_of_lis(nums):
    caudas = []                                  # caudas[k] = MENOR fim possível de LIS de tamanho k+1
    for n in nums:
        i = bisect.bisect_left(caudas, n)        # onde n substituiria mantendo caudas ordenado
        if i == len(caudas):
            caudas.append(n)                     # n estende a maior sequência conhecida
        else:
            caudas[i] = n                        # n melhora (abaixa) a cauda de uma LIS existente
    return len(caudas)
```

## 4. Walkthrough Visual (Teste de Mesa)

`rob(nums=[2, 7, 9, 3])`

| n | ant2 (antes) | ant1 (antes) | atual = max(ant1, ant2+n) | decisão |
|---|---|---|---|---|
| 2 | 0 | 0 | max(0, 0+2) = 2 | rouba a casa 2 |
| 7 | 0 | 2 | max(2, 0+7) = 7 | rouba 7, pula 2 |
| 9 | 2 | 7 | max(7, 2+9) = 11 | rouba 2 e 9 |
| 3 | 7 | 11 | max(11, 7+3) = 11 | pula 3 |

- Resposta: **11** (casas 2 + 9) ✔ — duas variáveis carregaram toda a "tabela".

## 5. Complexidade (Tempo e Espaço)

| Padrão | Tempo | Espaço |
|---|---|---|
| Fibonacci-like (stairs, robber) | O(n) | O(1) comprimido |
| Coin Change | O(valor × moedas) | O(valor) |
| LIS | O(n log n) com bisect | O(n) |
| Regra geral | nº de estados × custo da transição | nº de estados |

- A conta mágica de DP: **tempo = estados × transição** — se souber contar estados, sabe a complexidade.

## 6. Pegadinhas e Erros Comuns

- Estado **vago demais**: se você não consegue escrever a transição, o estado está mal definido — refine-o.
- Bottom-up preenchendo em **ordem errada** → lê célula ainda não calculada (lixo/zero).
- Confundir **subsequência** (DP) com **subarray** (Kadane/sliding window).
- Coin Change: "mínimo de moedas" (min) ≠ "número de combinações" (soma — e a ordem dos loops muda! ver [14](14_programacao_dinamica_2d.md)).
- **Python**: `@lru_cache` em método de classe segura `self` no cache (leak); prefira função interna.
- **Python**: default mutável como acumulador de memo (`def f(memo={})`) compartilha estado entre chamadas de teste.
- **Java**: `Integer.MAX_VALUE + 1` estoura para negativo — proteja a soma antes do `min` (por isso o `sub >= 0` no template).

## 7. Aplicações no Mundo Real (Backend)

- **Memoization É cache de função pura**: `@Cacheable` do Spring e o cache-aside do Redis aplicam o mesmo raciocínio (Vol. 2, E.2).
- **PostgreSQL**: o otimizador de joins usa DP (algoritmo de Selinger) para escolher a ordem de menor custo.
- **Diff/versionamento**: distância de edição incremental em editores e sistemas de merge.
- **Rate limiting/pricing**: "menor custo para compor um recurso" é Coin Change com outra roupa.
- Backoff e janelas de retry calculadas por recorrência = transições de DP em série temporal.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 Easy |
| 746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | 🟢 Easy |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | 🟡 Medium |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 Medium |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | 🟡 Medium |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟡 Medium |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 🟡 Medium |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | 🟡 Medium |
