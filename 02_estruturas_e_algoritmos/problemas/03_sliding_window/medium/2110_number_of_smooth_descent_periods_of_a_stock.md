# [2110] Number of Smooth Descent Periods of a Stock

> 🔗 [LeetCode 2110](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#TwoPointers` `#Medium`

## 📜 O Problema

Dado um array de inteiros `prices` representando o histórico diário de preços de uma ação, um **período de queda suave** consiste em um ou mais dias contíguos onde o preço de cada dia é **menor** que o do dia anterior por **exatamente** `1` (o primeiro dia do período é isento dessa regra). Retorne o número de períodos de queda suave.

**Exemplos:**
```
Input:  prices = [3,2,1,4]
Output: 7
Explicação: [3],[2],[1],[4],[3,2],[2,1],[3,2,1]

Input:  prices = [8,6,7,7]
Output: 4
Explicação: [8],[6],[7],[7]. Note que [8,6] não é um período suave (8-6≠1).

Input:  prices = [1]
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= prices.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `1 <= prices[i] <= 10^5` → valores pequenos, sem risco de overflow

## 🧭 Como reconhecer o padrão

"Contar TODOS os períodos contíguos que satisfazem uma condição de queda constante" é resolvido mantendo um **run**: enquanto a queda de exatamente `1` se mantém, o run cresce e cada crescimento adiciona um número previsível de NOVOS períodos terminando na posição atual — o mesmo espírito de [0413] Arithmetic Slices.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, checar se todas as quedas consecutivas dentro do período são exatamente `1`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** revalida a condição de queda constante do zero a cada período candidato, mesmo quando ele é apenas o anterior estendido em um dia.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `prices` comparando cada dia com o anterior. Mantenha um contador `run`: se `prices[i] == prices[i-1] - 1`, o run se estende (`run++`); senão, reseta para `1` (todo dia isolado já é um período trivial de tamanho 1). Some `run` ao total a cada passo — cada extensão adiciona exatamente `run` novos sub-períodos terminando ali.

## 🎬 Exemplo passo a passo

`prices = [3,2,1,4]`

| i | prices[i] | prices[i]==prices[i-1]-1? | run | total |
|---|---|---|---|---|
| 0 | 3 | — (início) | 1 | 1 |
| 1 | 2 | sim (2=3-1) | 2 | 3 |
| 2 | 1 | sim (1=2-1) | 3 | 6 |
| 3 | 4 | não (4≠1-1=0) | 1 | 7 |

Resultado final: `7` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public long getDescentPeriods(int[] prices) {
    long total = 0;
    int run = 1;

    for (int i = 0; i < prices.length; i++) {
        if (i > 0 && prices[i] == prices[i - 1] - 1) {
            run++; // continua o período de queda suave
        } else {
            run = 1; // quebrou (ou é o primeiro dia): reinicia com o próprio dia
        }
        total += run; // toda sub-sequência terminando aqui, de tamanho 1 até run, é válida
    }

    return total;
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

- Cada dia isolado já é um "período de queda suave" trivial (comprimento 1) — por isso `run` nunca reseta para `0`, sempre para `1`, e `total` sempre soma pelo menos `1` a cada dia.
- Somar `run` (não `1`) a cada passo é o que conta corretamente TODAS as sub-sequências terminando naquele dia — o mesmo padrão de [0413] Arithmetic Slices.
- A queda precisa ser de EXATAMENTE `1`, não "qualquer queda" — `prices[i] == prices[i-1] - 1`, não `prices[i] < prices[i-1]`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único dia | `[1]` | 1 | só o próprio dia conta |
| Sem nenhuma queda de 1 | `[8,6,7,7]` | 4 | cada dia isolado conta, mas nenhum encadeamento (8-6=2≠1) |
| Queda constante o array inteiro | `[5,4,3,2,1]` | 15 | período de 5 dias gera 5+4+3+2+1=15 sub-períodos |
| Exemplo do enunciado | `[3,2,1,4]` | 7 | [3],[2],[1],[4],[3,2],[2,1],[3,2,1] |

## 🔗 Conexões

- Problemas irmãos: [0413] Arithmetic Slices (mesmíssima técnica de "run" que se estende ou reseta, aqui com a condição de queda de 1 em vez de diferença arbitrária constante), [3411] Maximum Subarray With Equal Products (mesma família de acompanhar um estado incremental que se resolve por completo a cada passo)
- No backend: contar quantos sub-períodos de uma série de preços representam uma tendência de queda perfeitamente linear, útil para detectar padrões de correção previsível em séries financeiras.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
