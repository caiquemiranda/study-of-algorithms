# [0713] Subarray Product Less Than K

> 🔗 [LeetCode 713](https://leetcode.com/problems/subarray-product-less-than-k/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dado um array de inteiros `nums` e um inteiro `k`, retorne o número de subarrays contíguos onde o produto de todos os elementos é **estritamente menor** que `k`.

**Exemplos:**
```
Input:  nums = [10,5,2,6], k = 100
Output: 8
Explicação: os 8 subarrays são [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6].
Note que [10,5,2] não conta, pois seu produto (100) não é estritamente menor que k.

Input:  nums = [1,2,3], k = 0
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 3 * 10^4` → O(n²) força bruta é arriscado; O(n) é o esperado
- `1 <= nums[i] <= 1000` → **todos os valores são positivos**, garantindo que o produto só cresce ao expandir a janela e só diminui ao encolher (monotonicidade essencial pra técnica)
- `0 <= k <= 10^6` → `k` pode ser `0` ou `1`, casos em que nenhum subarray de positivos pode ter produto menor

## 🧭 Como reconhecer o padrão

"Contar subarrays cujo produto satisfaz uma condição, com valores todos positivos" é dois ponteiros clássico: como o produto só cresce ao adicionar elementos positivos, encolher pela esquerda enquanto o produto for `>= k` é seguro, e a cada `right` válido, TODA substring `[l', right]` com `l' >= left` também é válida — basta somar `right-left+1`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, calcular o produto do subarray do zero e checar se é menor que `k`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula o produto inteiro a cada par, ignorando que valores positivos permitem manter um produto corrente que só cresce ao expandir e só diminui ao encolher.

## 💡 Solução 2 — A ideia otimizada (intuição)

Expanda `right`, multiplicando `nums[right]` a um produto corrente. Enquanto o produto for `>= k`, encolha `left` (dividindo pelo elemento que sai). A cada passo válido, some `right - left + 1` ao total — o número de novos subarrays terminando em `right` que satisfazem a condição.

## 🎬 Exemplo passo a passo

`nums = [10,5,2,6]`, `k = 100`

| right | nums[right] | product após incluir | <k? | Encolhe | left final | válidas (right-left+1) | total |
|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | sim | não | 0 | 1 | 1 |
| 1 | 5 | 50 | sim | não | 0 | 2 | 3 |
| 2 | 2 | 100 | não | remove nums[0]=10 → 10 | 1 | 2 | 5 |
| 3 | 6 | 60 | sim | não | 1 | 3 | 8 |

Resultado final: `8` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numSubarrayProductLessThanK(int[] nums, int k) {
    if (k <= 1) {
        return 0; // produto de inteiros positivos nunca é < 1 (ou <=0)
    }

    int left = 0;
    long product = 1;
    int count = 0;

    for (int right = 0; right < nums.length; right++) {
        product *= nums[right];

        while (product >= k) {
            product /= nums[left];
            left++;
        }

        count += right - left + 1; // toda substring [l', right] com l' >= left também vale
    }

    return count;
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

- `k <= 1` é um caso especial: como todos os `nums[i] >= 1`, nenhum produto de subarray não-vazio pode ser menor que 1 — retornar `0` direto evita até dividir por valores inválidos.
- A condição é produto **estritamente menor** que `k` — usar `<=` em vez de `<` conta subarrays a mais.
- Esquecer que, uma vez que `[left, right]` é válido, TODA substring `[l', right]` com `l' >= left` também é — basta somar `right - left + 1` de uma vez, sem enumerar cada subarray individualmente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 | `nums=[1,2,3]`, `k=0` | 0 | nenhum produto de positivos é menor que 0 |
| k=1 | `nums=[1,1,1]`, `k=1` | 0 | produto sempre igual a 1, nunca menor que 1 |
| Todo o array serve | `nums=[1,2,3]`, `k=100` | 6 | todo subarray tem produto menor que 100 |
| Exemplo do enunciado | `nums=[10,5,2,6]`, `k=100` | 8 | 8 subarrays contíguos têm produto estritamente menor que 100 |

## 🔗 Conexões

- Problemas irmãos: [0209] Minimum Size Subarray Sum (mesma técnica de dois ponteiros com condição monotônica, soma em vez de produto), [3258] Count Substrings That Satisfy K-Constraint I (mesma ideia de "contar todas as substrings válidas somando right-left+1")
- No backend: contar quantas janelas de configuração (fatores multiplicativos aplicados em sequência) mantêm um valor acumulado abaixo de um limite de segurança, sem recalcular o produto do zero a cada janela.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
