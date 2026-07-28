# [3364] Minimum Positive Sum Subarray

> 🔗 [LeetCode 3364](https://leetcode.com/problems/minimum-positive-sum-subarray/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#PrefixSum` `#Easy`

## 📜 O Problema

Dado um array `nums` e dois inteiros `l` e `r`, encontre a **menor** soma de um **subarray** cujo tamanho esteja entre `l` e `r` (inclusive) e cuja soma seja maior que 0. Retorne essa soma mínima; se não existir tal subarray, retorne `-1`.

**Exemplos:**
```
Input:  nums = [3,-2,1,4], l = 2, r = 3
Output: 1
Explicação: o subarray [3,-2] tem soma 1, a menor soma positiva entre os tamanhos 2 e 3.

Input:  nums = [-2,2,-3,1], l = 2, r = 3
Output: -1
Explicação: nenhum subarray de tamanho 2 ou 3 tem soma > 0.

Input:  nums = [1,2,3,4], l = 2, r = 4
Output: 3
Explicação: o subarray [1,2] tem soma 3, a menor soma positiva possível.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 100` → entrada pequena; até O(n²) com prefix sums é folgado
- `1 <= l <= r <= nums.length` → sempre existe pelo menos um tamanho de janela válido dentro dos limites do array
- `-1000 <= nums[i] <= 1000` → valores negativos presentes, então a soma de uma janela **não** cresce monotonicamente com o tamanho — não dá pra usar "encolher pela esquerda enquanto a soma for grande demais" como em problemas só com positivos

## 🧭 Como reconhecer o padrão

"Soma de subarrays de **tamanho variável dentro de um intervalo [l, r]**" é resolvido tratando cada tamanho de janela separadamente: para cada tamanho fixo `w` entre `l` e `r`, deslizar uma janela de tamanho `w` sobre o array usando **prefix sums**, que transformam a soma de qualquer subarray numa subtração O(1).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada tamanho `w` de `l` a `r` e cada posição inicial `i`, somar o subarray `nums[i..i+w-1]` do zero.

- Tempo: O(n · (r-l+1) · n) no pior caso, podendo chegar a O(n³) · Espaço: O(1)
- **Por que não basta:** recalcula a soma do subarray inteiro toda vez, quando um pré-processamento de prefix sums permite obter qualquer soma de subarray em O(1).

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule o array de prefix sums `prefix[i] = nums[0] + ... + nums[i-1]` (com `prefix[0] = 0`). Para cada tamanho de janela `w` de `l` a `r`, e cada posição inicial `i` de `0` a `n-w`, a soma do subarray é `prefix[i+w] - prefix[i]` — O(1) por consulta. Percorra todos esses valores, mantendo o menor que for maior que zero.

## 🎬 Exemplo passo a passo

`nums = [3,-2,1,4]`, `l = 2`, `r = 3` → `prefix = [0,3,1,2,6]`

| w (tamanho) | i (início) | Soma (prefix[i+w]-prefix[i]) | >0? | Melhor até agora |
|---|---|---|---|---|
| 2 | 0 | 1-0=1 | sim | 1 |
| 2 | 1 | 2-3=-1 | não | 1 |
| 2 | 2 | 6-1=5 | sim | 1 |
| 3 | 0 | 2-0=2 | sim | 1 |
| 3 | 1 | 6-3=3 | sim | 1 |

Resultado final: `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) para o prefix sum, mais O(n · (r-l+1)) para varrer todos os tamanhos e posições — no pior caso (`r-l+1 = n`), O(n²)
- **Espaço:** O(n) para o array de prefix sums

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumSumSubarray(int[] nums, int l, int r) {
    int n = nums.length;
    long[] prefix = new long[n + 1];
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    long best = Long.MAX_VALUE;
    for (int w = l; w <= r; w++) {
        for (int i = 0; i + w <= n; i++) {
            long sum = prefix[i + w] - prefix[i];
            if (sum > 0 && sum < best) {
                best = sum;
            }
        }
    }

    return best == Long.MAX_VALUE ? -1 : (int) best;
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

- Esquecer que o tamanho do subarray deve estar entre `l` e `r` **inclusive** — testar só um tamanho fixo ou só os extremos perde candidatos válidos.
- Confundir "soma mínima positiva" com "soma mínima" — subarrays de soma negativa ou zero devem ser ignorados, mesmo que sejam numericamente menores.
- Assumir que dá pra usar a técnica clássica de "encolher a janela enquanto a soma for grande demais" — com valores negativos presentes, a soma não é monotônica em relação ao tamanho da janela, então essa técnica não se aplica aqui.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhum subarray positivo | `nums=[-2,2,-3,1]`, `l=2`, `r=3` | -1 | toda combinação de tamanho 2 ou 3 soma ≤ 0 |
| Melhor soma num tamanho intermediário | `nums=[1,2,3,4]`, `l=2`, `r=4` | 3 | subarray [1,2] tem a menor soma positiva entre os tamanhos permitidos |
| l igual a r (tamanho fixo) | `nums=[5,-1,5]`, `l=1`, `r=1` | 5 | com tamanho fixo 1, a resposta é o menor valor positivo isolado |
| Exemplo do enunciado | `nums=[3,-2,1,4]`, `l=2`, `r=3` | 1 | subarray [3,-2] soma 1, a menor soma positiva possível |

## 🔗 Conexões

- Problemas irmãos: [0209] Minimum Size Subarray Sum (mesma família de soma de subarray com prefix sums, mas minimizando o TAMANHO em vez da SOMA), [0560] Subarray Sum Equals K (mesma técnica-base de prefix sums para consultar somas de subarray em O(1))
- No backend: encontrar o menor lote de transações (dentro de um intervalo de tamanhos permitido) cujo saldo líquido seja positivo — útil em conciliação financeira ou detecção de ciclos de caixa mínimos viáveis.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
