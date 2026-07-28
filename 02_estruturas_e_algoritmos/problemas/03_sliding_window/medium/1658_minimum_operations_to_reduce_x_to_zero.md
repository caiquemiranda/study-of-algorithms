# [1658] Minimum Operations to Reduce X to Zero

> 🔗 [LeetCode 1658](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#PrefixSum` `#Medium`

## 📜 O Problema

Dado um array de inteiros `nums` e um inteiro `x`, em uma operação você pode remover o elemento mais à esquerda ou mais à direita do array e subtrair seu valor de `x`. Retorne o número **mínimo** de operações para reduzir `x` a exatamente `0`, ou `-1` se não for possível.

**Exemplos:**
```
Input:  nums = [1,1,4,2,3], x = 5
Output: 2
Explicação: remover os dois últimos elementos reduz x a zero.

Input:  nums = [5,6,7,8,9], x = 4
Output: -1

Input:  nums = [3,2,20,1,1,3], x = 10
Output: 5
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(2^n) testando todas as combinações de remoção é inviável; O(n) é o esperado
- `1 <= nums[i] <= 10^4` → **todos os valores são positivos**, permitindo a técnica de janela deslizante

## 🧭 Como reconhecer o padrão

A mesma virada de perspectiva de [1423] Maximum Points You Can Obtain from Cards: em vez de "remover elementos das pontas somando `x`", pense em "manter um bloco **contíguo** central cuja soma é `total - x`" — maximizar esse bloco central minimiza as operações necessárias.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todas as combinações de quantos elementos remover de cada ponta (0 a n da esquerda, o resto da direita), somando cada combinação.

- Tempo: O(n²) recalculando cada combinação · Espaço: O(1)
- **Por que não basta:** recalcula a soma removida do zero para cada combinação, quando a técnica do bloco central complementar resolve isso com uma única janela deslizante.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule `total`. Se `total - x < 0`, é impossível. Encontre o maior subarray contíguo cuja soma é exatamente `total - x` usando dois ponteiros (válido porque os valores são positivos). A resposta é `n - maxLen` (o resto do array, fora desse bloco central, é o que foi removido das pontas).

## 🎬 Exemplo passo a passo

`nums = [1,1,4,2,3]`, `x = 5` → total=11, alvo do bloco central = `11-5=6`

| right | nums[right] | sum após shrink | ==target(6)? | comprimento | melhor (maxLen) |
|---|---|---|---|---|---|
| 0 | 1 | 1 | não | — | -1 (nenhum ainda) |
| 1 | 1 | 2 | não | — | -1 |
| 2 | 4 | 6 | sim | 3 | 3 |
| 3 | 2 | 6 (encolheu) | sim | 2 | 3 |
| 4 | 3 | 5 (encolheu) | não | — | 3 |

Resultado final: `n - maxLen = 5 - 3 = 2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minOperations(int[] nums, int x) {
    int total = 0;
    for (int num : nums) {
        total += num;
    }

    int target = total - x;
    if (target < 0) {
        return -1; // nem removendo tudo alcança x
    }
    if (target == 0) {
        return nums.length; // precisa remover o array inteiro
    }

    int left = 0;
    int sum = 0;
    int maxLen = -1;

    for (int right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum > target) {
            sum -= nums[left];
            left++;
        }

        if (sum == target) {
            maxLen = Math.max(maxLen, right - left + 1);
        }
    }

    return maxLen == -1 ? -1 : nums.length - maxLen;
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

- A virada de perspectiva é a mesma de [1423] Maximum Points You Can Obtain from Cards: pense em "manter um bloco CONTÍGUO central" em vez de "remover das pontas".
- `target < 0` (quando `x > total`) significa que nem removendo TODO o array se alcança `x` — retorne `-1` direto.
- `target == 0` é um caso especial: o único bloco central válido é o vazio, então a resposta é remover o array inteiro (`nums.length` operações), não algo derivado de `maxLen`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| x maior que a soma total | `nums=[1,1]`, `x=3` | -1 | soma total é 2, nunca alcança 3 |
| x igual à soma total | `nums=[1,2]`, `x=3` | 2 | precisa remover tudo (target=0) |
| Nenhuma combinação de pontas soma x | `nums=[5,6,7,8,9]`, `x=4` | -1 | nenhuma soma de prefixo/sufixo bate exatamente 4 |
| Exemplo do enunciado | `nums=[1,1,4,2,3]`, `x=5` | 2 | remover os dois últimos elementos (2+3=5) |

## 🔗 Conexões

- Problemas irmãos: [1423] Maximum Points You Can Obtain from Cards (mesmíssima técnica de virar o problema das pontas para um bloco central contíguo), [0209] Minimum Size Subarray Sum (mesma técnica-base de dois ponteiros para somas exatas/mínimas em array de positivos)
- No backend: calcular o menor número de itens a remover das extremidades de uma fila de processamento para atingir exatamente um orçamento de custo/tempo remanescente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
