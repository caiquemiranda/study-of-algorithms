# [0643] Maximum Average Subarray I

> 🔗 [LeetCode 643](https://leetcode.com/problems/maximum-average-subarray-i/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Array` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums` com `n` elementos e um inteiro `k`, encontre um subarray contíguo de comprimento **exatamente** `k` com a maior média possível e retorne essa média. Qualquer resposta com erro de cálculo menor que `10^-5` é aceita.

**Exemplos:**
```
Input:  nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explicação: a maior média é (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Input:  nums = [5], k = 1
Output: 5.00000
```

**Restrições (e o que elas denunciam):**
- `n == nums.length` e `1 <= k <= n <= 10^5` → recalcular a soma de cada janela do zero pode chegar a O(n·k) ≈ O(n²); precisa de O(n)
- `-10^4 <= nums[i] <= 10^4` → a soma de até `10^5` elementos cabe folgadamente em `long`, sem risco de overflow

## 🧭 Como reconhecer o padrão

"Subarray contíguo de tamanho **fixo** `k` otimizando uma soma/média" é o exemplo mais clássico de janela deslizante de tamanho fixo: soma-se a primeira janela uma vez e, a cada passo seguinte, ajusta-se a soma removendo o elemento que sai à esquerda e somando o que entra à direita — sem nunca recontar o meio da janela.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada início `i` de `0` a `n-k`, somar do zero os `k` elementos de `nums[i..i+k-1]` e comparar a média resultante com a melhor vista até então.

- Tempo: O(n·k) · Espaço: O(1)
- **Por que não basta:** recalcula a soma inteira a cada nova janela, mesmo que `k-1` dos `k` elementos sejam exatamente os mesmos da janela anterior.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule a soma da primeira janela (os `k` primeiros elementos) uma única vez. A cada passo seguinte, `soma_nova = soma_atual - nums[i] + nums[i+k]` — remove o elemento que sai à esquerda, soma o que entra à direita. Guarde a maior soma vista; no final, divida pela `k` para obter a média.

## 🎬 Exemplo passo a passo

`nums = [1,12,-5,-6,50,3]`, `k = 4`

| Passo | Janela (índices) | Remove | Adiciona | Soma | Melhor soma |
|---|---|---|---|---|---|
| inicial | [0..3] | — | — | 1+12-5-6=2 | 2 |
| 1 | [1..4] | nums[0]=1 | nums[4]=50 | 2-1+50=51 | 51 |
| 2 | [2..5] | nums[1]=12 | nums[5]=3 | 51-12+3=42 | 51 |

Melhor soma: `51` → média = `51/4 = 12.75` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — soma inicial O(k) mais `n-k` deslizamentos O(1) cada
- **Espaço:** O(1) — só a soma corrente e o melhor valor

## 💻 Implementações

### Java (referência completa e comentada)
```java
public double findMaxAverage(int[] nums, int k) {
    long windowSum = 0;
    for (int i = 0; i < k; i++) {
        windowSum += nums[i];
    }

    long best = windowSum;
    for (int i = k; i < nums.length; i++) {
        windowSum += nums[i] - nums[i - k]; // desliza: entra nums[i], sai nums[i-k]
        best = Math.max(best, windowSum);
    }

    return (double) best / k;
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

- Recalcular a soma do zero a cada janela em vez de deslizar — funciona, mas vira O(n·k) e pode estourar o tempo limite com `n = 10^5`.
- Comparar médias em ponto flutuante a cada passo em vez de comparar somas inteiras (ou `long`) — acumula erro de arredondamento; divida só no final.
- Esquecer que o subarray deve ter tamanho **exatamente** `k`, não "até `k`" — não existe escolha de tamanho variável neste problema.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k igual a n | `nums=[5]`, `k=1` | 5.0 | única janela possível é o array inteiro |
| Todos negativos | `nums=[-1,-2,-3]`, `k=2` | -1.5 | a "melhor" janela ainda é a de soma menos negativa |
| Melhor janela logo no início | `nums=[10,10,-100,-100]`, `k=2` | 10.0 | primeira janela já é ótima, deslizar só piora |
| k=n (array inteiro) | `nums=[1,2,3,4]`, `k=4` | 2.5 | não há outra janela para comparar |

## 🔗 Conexões

- Problemas irmãos: [0209] Minimum Size Subarray Sum (mesma família de soma de subarray, mas com janela de tamanho **variável** em vez de fixo), [1876] Substrings of Size Three with Distinct Characters (mesmo padrão de janela fixa, aplicado a strings)
- No backend: calcular médias móveis de métricas — por exemplo, latência média das últimas `k` requisições — sem reprocessar a janela inteira a cada nova amostra; a base de qualquer dashboard de monitoramento em tempo real.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
