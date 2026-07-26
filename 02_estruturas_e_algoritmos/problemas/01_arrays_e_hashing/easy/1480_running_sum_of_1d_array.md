# [1480] Running Sum of 1d Array

> 🔗 [LeetCode 1480](https://leetcode.com/problems/running-sum-of-1d-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#PrefixSum` `#Easy`

## 📜 O Problema

Dado um array `nums`, definimos a soma corrente (running sum) como `runningSum[i] = sum(nums[0]…nums[i])`. Retorne a soma corrente de `nums`.

**Exemplos:**
```
Input:  nums = [1,2,3,4]
Output: [1,3,6,10]
Explicação: a soma corrente é obtida assim: [1, 1+2, 1+2+3, 1+2+3+4].

Input:  nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Input:  nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 1000` → O(n) resolve com folga
- valores podem ser negativos → soma ainda funciona igual, sem tratamento especial

## 🧭 Como reconhecer o padrão

"runningSum[i] = soma de tudo até i" é a definição literal de prefix sum — o exemplo mais direto e didático da técnica, sem nenhuma complicação extra.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i`, somar `nums[0..i]` do zero.

- Tempo: O(n²) · Espaço: O(n) para o resultado
- **Por que não basta:** recalcula a soma inteira a cada posição, quando `runningSum[i] = runningSum[i-1] + nums[i]` já reaproveita o trabalho anterior.

## 💡 Solução 2 — A ideia otimizada (intuição)

Acumule a soma numa única passada, guardando o total corrente em cada posição.

## 🎬 Exemplo passo a passo

`nums = [1,2,3,4]`

| Passo | i | nums[i] | somaAcumulada |
|---|---|---|---|
| 1 | 0 | 1 | 1 |
| 2 | 1 | 2 | 3 |
| 3 | 2 | 3 | 6 |
| 4 | 3 | 4 | 10 |

Resultado final: `[1,3,6,10]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) extra (fora o array de saída)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] runningSum(int[] nums) {
    int[] resultado = new int[nums.length];
    int somaAcumulada = 0;
    for (int i = 0; i < nums.length; i++) {
        somaAcumulada += nums[i];
        resultado[i] = somaAcumulada;
    }
    return resultado;
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

- Recalcular a soma do zero a cada posição em vez de acumular — funciona, mas é O(n²) desnecessário.
- Modificar o array `nums` original em vez de criar um novo `resultado` — funciona também (prefix sum in-place é uma técnica válida), mas altera os dados de entrada, o que pode surpreender quem chama a função esperando `nums` intacto.
- Esquecer que o primeiro elemento do resultado é simplesmente `nums[0]` — não há nada de especial a fazer nele, a lógica geral já cobre esse caso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | [1,2,3,4] | [1,3,6,10] | soma cumulativa simples |
| Todos iguais | [1,1,1,1,1] | [1,2,3,4,5] | soma cresce de 1 em 1 |
| Um único elemento | [5] | [5] | menor entrada possível |
| Valores mistos | [3,1,2,10,1] | [3,4,6,16,17] | soma acumula normalmente com valores variados |

## 🔗 Conexões

- Problemas irmãos: [0724] Find Pivot Index (mesma técnica base), [1413] Minimum Value to Get Positive Step by Step Sum (mesma soma passo a passo, mas com objetivo diferente)
- No backend: cálculo de saldo acumulado em extratos financeiros (ex.: saldo após cada transação numa lista de movimentações).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
