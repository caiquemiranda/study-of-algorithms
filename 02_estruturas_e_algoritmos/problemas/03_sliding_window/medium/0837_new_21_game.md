# [0837] New 21 Game

> 🔗 [LeetCode 837](https://leetcode.com/problems/new-21-game/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#DynamicProgramming` `#Medium`

## 📜 O Problema

Alice joga um jogo baseado no "21": começa com `0` pontos e sorteia números enquanto tiver menos que `k` pontos. A cada sorteio, ganha um número inteiro de pontos aleatório e uniforme no intervalo `[1, maxPts]`. Ela para de sortear ao atingir `k` **ou mais** pontos. Retorne a probabilidade de Alice terminar com `n` pontos ou menos.

**Exemplos:**
```
Input:  n = 10, k = 1, maxPts = 10
Output: 1.00000
Explicação: Alice sorteia uma única carta e para.

Input:  n = 6, k = 1, maxPts = 10
Output: 0.60000
Explicação: com um único sorteio, 6 dos 10 valores possíveis ficam ≤ 6.

Input:  n = 21, k = 17, maxPts = 10
Output: 0.73278
```

**Restrições (e o que elas denunciam):**
- `0 <= k <= n <= 10^4`, `1 <= maxPts <= 10^4` → O(n · maxPts) força bruta (recalcular a soma de `maxPts` estados anteriores para cada `dp[i]`) pode chegar a `10^8`; O(n) é o esperado
- `n` pode ser bem maior que `k` → o corte de segurança (quando qualquer pontuação final possível já é `<= n`) evita processamento desnecessário

## 🧭 Como reconhecer o padrão

Esse não é um problema de janela sobre um array de ENTRADA, mas sobre o próprio array `dp` que está sendo CONSTRUÍDO: `dp[i]` depende da soma de `dp[i-maxPts .. i-1]`. Recalcular essa soma do zero a cada `i` é O(maxPts) por passo; mantê-la como uma **soma de janela deslizante** (somando o que entra, subtraindo o que sai do alcance de `maxPts`) reduz cada passo a O(1).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `i` de `1` a `n`, somar diretamente `dp[max(0,i-maxPts) .. min(i-1,k-1)]` do zero para calcular `dp[i]`.

- Tempo: O(n · maxPts) · Espaço: O(n)
- **Por que não basta:** recalcula a mesma soma de até `maxPts` termos repetidamente, quando apenas um termo entra e um sai da janela a cada incremento de `i`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha uma soma de janela (`windowSum`) representando a soma de `dp[i-maxPts .. i-1]`, mas só considerando estados com índice `< k` (só eles "geram" novos sorteios). A cada `i`: `dp[i] = windowSum / maxPts`; se `i < k`, esse novo estado entra na janela (soma-se a `windowSum`, pois Alice pode continuar sorteando a partir dele); senão, é um estado final e vai direto para o resultado. Por fim, remova da janela o estado que saiu do alcance de `maxPts` posições.

## 🎬 Exemplo passo a passo

`n = 6`, `k = 1`, `maxPts = 10` (com `k=1`, cada sorteio único decide o resultado; `maxPts=10 > n`, então a remoção da janela nunca é exercitada neste exemplo)

| i | dp[i] = windowSum/maxPts | i<k? | Ação | windowSum após | resultado acumulado |
|---|---|---|---|---|---|
| 1 | 1/10=0.1 | não (1<1 falso) | resultado += 0.1 | 1 (sem alteração) | 0.1 |
| 2 | 1/10=0.1 | não | resultado += 0.1 | 1 | 0.2 |
| 3 | 1/10=0.1 | não | resultado += 0.1 | 1 | 0.3 |
| 4 | 1/10=0.1 | não | resultado += 0.1 | 1 | 0.4 |
| 5 | 1/10=0.1 | não | resultado += 0.1 | 1 | 0.5 |
| 6 | 1/10=0.1 | não | resultado += 0.1 | 1 | 0.6 |

Resultado final: `0.6` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada, cada posição faz trabalho O(1) para atualizar a soma da janela
- **Espaço:** O(n) para o array `dp`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public double new21Game(int n, int k, int maxPts) {
    if (k == 0 || n >= k + maxPts - 1) {
        return 1.0; // qualquer pontuação final possível já é <= n
    }

    double[] dp = new double[n + 1];
    dp[0] = 1.0;
    double windowSum = 1.0; // soma de dp[i] para os índices i < k dentro do alcance de maxPts
    double result = 0.0;

    for (int i = 1; i <= n; i++) {
        dp[i] = windowSum / maxPts;

        if (i < k) {
            windowSum += dp[i]; // esse estado ainda pode gerar novos sorteios
        } else {
            result += dp[i]; // estado final (Alice já parou aqui)
        }

        if (i - maxPts >= 0) {
            windowSum -= dp[i - maxPts]; // esse estado saiu do alcance de um sorteio (> maxPts de distância)
        }
    }

    return result;
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

- A janela deslizante aqui não é sobre um array de entrada, mas sobre o próprio array `dp` que está sendo construído — a cada novo `dp[i]`, a soma da janela dos `maxPts` estados anteriores é o que permite computá-lo em O(1) em vez de somar `maxPts` valores do zero.
- Só estados com índice `< k` continuam alimentando a janela (`windowSum`) — uma vez que a pontuação atinge `k` ou mais, Alice PARA de sortear, então esse estado não gera "filhos" e deve ir direto para o resultado.
- O caso `k == 0` é especial: Alice nunca sorteia (ela só sorteia enquanto tem MENOS que `k` pontos, e já começa com `0 >= k = 0`), então fica com 0 pontos e a resposta é sempre `1.0`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 (nunca sorteia) | `n=10`, `k=0`, `maxPts=10` | 1.0 | Alice já começa com 0 pontos, que satisfaz `0 >= k` |
| n grande o bastante pra garantir sucesso | `n=10`, `k=1`, `maxPts=10` | 1.0 | qualquer pontuação final possível (no máximo k-1+maxPts=10) já é ≤ n |
| Exemplo intermediário do enunciado | `n=6`, `k=1`, `maxPts=10` | 0.6 | com k=1, um único sorteio de 1 a 10 determina o resultado; 6 dos 10 valores são ≤6 |
| Exemplo mais restritivo do enunciado | `n=21`, `k=17`, `maxPts=10` | 0.73278 | caso geral, exercitando plenamente a soma de janela deslizante sobre o dp |

## 🔗 Conexões

- Problemas irmãos: [0070] Climbing Stairs (mesma ideia-base de dp[i] depender de uma janela de estados anteriores, aqui generalizada para probabilidade em vez de contagem), [0209] Minimum Size Subarray Sum (mesma técnica de manter uma soma corrente atualizada incrementalmente, aplicada a um array de entrada em vez de um array de DP)
- No backend: simular acumuladores probabilísticos com limite de corte — por exemplo, estimar a chance de um sistema de rate-limiting "estourar" um limite acumulado dado um padrão de chegada de eventos com valores aleatórios limitados.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
