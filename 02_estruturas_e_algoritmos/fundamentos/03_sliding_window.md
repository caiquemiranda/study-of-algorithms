# 03 — Sliding Window

> Janela `[esq, dir]` que desliza reaproveitando cálculo. Soluções em [`../problemas/03_sliding_window/`](../problemas/03_sliding_window/).

## 1. Conceito Central e Analogia Didática

- Mantém uma janela sobre o array/string e um **estado incremental** (soma, mapa de frequência): o que entra soma ao estado, o que sai subtrai — nada é recalculado.
- **Janela fixa**: tamanho k constante, desliza 1 posição por vez. **Janela variável**: `dir` expande sempre; `esq` encolhe conforme a regra do invariante.
- Cada elemento entra e sai **no máximo uma vez** → O(n) em vez de O(n²).

**Analogia:** caixa de supermercado somando um carrinho em esteira rolante: quando um produto novo entra na área da balança, soma; quando um sai pela frente, subtrai. Ninguém pesa a esteira inteira de novo a cada movimento.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "**maior/menor subarray/substring CONTÍGUA** que satisfaz X" → janela variável.
- Se pede "soma/média/máximo de **todas as janelas de tamanho k**" → janela fixa.
- Se limita "**no máximo K distintos / K trocas / K zeros**" → janela variável com contador.
- Palavras-gatilho: *longest*, *shortest*, *substring*, *subarray*, *at most K*.
- ⚠️ Se pede **subsequência** (não contígua) → NÃO é sliding window; provavelmente é DP.

## 3. Templates de Código

### Janela variável (maior substring sem repetição)

```java
// Java — o invariante "sem repetidos" é restaurado encolhendo a esquerda
public int lengthOfLongestSubstring(String s) {
    Set<Character> janela = new HashSet<>();
    int esq = 0, melhor = 0;
    for (int dir = 0; dir < s.length(); dir++) {
        char c = s.charAt(dir);
        while (janela.contains(c)) {        // violou o invariante: encolhe até expulsar a duplicata
            janela.remove(s.charAt(esq++));
        }
        janela.add(c);                      // agora é seguro incluir o novo caractere
        melhor = Math.max(melhor, dir - esq + 1); // janela atual é válida: candidata a recorde
    }
    return melhor;
}
```

```python
def length_of_longest_substring(s):
    janela = set()
    esq = melhor = 0
    for dir in range(len(s)):
        while s[dir] in janela:          # encolhe SÓ o necessário para readmitir s[dir]
            janela.remove(s[esq])
            esq += 1
        janela.add(s[dir])
        melhor = max(melhor, dir - esq + 1)
    return melhor
```

### Janela fixa (maior soma de k elementos)

```java
// Java — desliza em O(1): soma o que entra, subtrai o que sai
public int maxSomaK(int[] nums, int k) {
    int soma = 0;
    for (int i = 0; i < k; i++) soma += nums[i];  // janela inicial
    int melhor = soma;
    for (int dir = k; dir < nums.length; dir++) {
        soma += nums[dir] - nums[dir - k];        // entra 1, sai 1: custo constante
        melhor = Math.max(melhor, soma);
    }
    return melhor;
}
```

```python
def max_soma_k(nums, k):
    soma = sum(nums[:k])
    melhor = soma
    for dir in range(k, len(nums)):
        soma += nums[dir] - nums[dir - k]   # atualização incremental, nunca re-soma a janela
        melhor = max(melhor, soma)
    return melhor
```

## 4. Walkthrough Visual (Teste de Mesa)

`length_of_longest_substring("abcabb")`

| dir | s[dir] | ação do while | janela após | esq | melhor |
|---|---|---|---|---|---|
| 0 | a | — | `{a}` | 0 | 1 |
| 1 | b | — | `{a,b}` | 0 | 2 |
| 2 | c | — | `{a,b,c}` | 0 | 3 |
| 3 | a | remove `a` (esq→1) | `{b,c,a}` | 1 | 3 |
| 4 | b | remove `b` (esq→2) | `{c,a,b}` | 2 | 3 |
| 5 | b | remove `c`,`a`,`b` (esq→5) | `{b}` | 5 | 3 |

- Resultado: **3** (`"abc"`) ✔ — `esq` nunca recua; cada char entra/sai do set uma única vez.

## 5. Complexidade (Tempo e Espaço)

| Forma | Tempo | Espaço |
|---|---|---|
| Janela fixa | O(n) | O(1) |
| Janela variável | O(n) | O(k) ou O(alfabeto) |

- O(n) porque `esq` e `dir` só andam para frente — o `while` interno é pago pelo total de saídas, não por iteração (análise amortizada).

## 6. Pegadinhas e Erros Comuns

- Recalcular a janela inteira a cada passo → O(n·k), perde o propósito do padrão.
- Direção do encolhimento invertida: **maximização** encolhe enquanto *inválida*; **minimização** encolhe enquanto *válida*.
- Esquecer de remover `s[esq]` do estado ao encolher → janela "fantasma".
- **Java**: `s.charAt(i)` em loop é ok, mas concatenar `String` para guardar a janela é O(n²) — use `Set`/índices.
- **Python**: fatiar `s[esq:dir]` para checar conteúdo é O(k) escondido dentro do loop.
- Números **negativos** quebram a monotonicidade em "soma ≥ alvo" → aí é prefix sum + deque, não janela.

## 7. Aplicações no Mundo Real (Backend)

- **Rate limiting Sliding Window** (API Gateway, Resilience4j): a janela é sobre timestamps de requisições — o algoritmo é este.
- **Kafka Streams / Flink**: tumbling e sliding windows de agregação são a versão distribuída do padrão.
- **Observabilidade**: métricas móveis (p99 dos últimos 5 min, média móvel de CPU) mantêm estado incremental idêntico.
- **TCP**: a janela deslizante de controle de fluxo (`rwnd`) usa o mesmo conceito de fronteiras que avançam.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 🟢 Easy |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 🟡 Medium |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | 🟡 Medium |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🔴 Hard |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🔴 Hard |
