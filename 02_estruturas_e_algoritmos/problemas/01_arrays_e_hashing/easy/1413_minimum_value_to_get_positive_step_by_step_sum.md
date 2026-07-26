# [1413] Minimum Value to Get Positive Step by Step Sum

> 🔗 [LeetCode 1413](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#PrefixSum` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums`, você começa com um valor inicial **positivo** `startValue`. Em cada iteração, você calcula a soma passo a passo de `startValue` mais os elementos de `nums` (da esquerda para a direita).

Retorne o menor valor **positivo** de `startValue` tal que a soma passo a passo nunca fique menor que 1.

**Exemplos:**
```
Input:  nums = [-3,2,-3,4,2]
Output: 5
Explicação: com startValue=4, na terceira iteração a soma fica abaixo de 1. Com startValue=5, a soma
nunca cai abaixo de 1 em nenhum ponto.

Input:  nums = [1,2]
Output: 1
Explicação: o valor inicial mínimo precisa ser positivo.

Input:  nums = [1,-2,-3]
Output: 5
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 100` → pequeno, O(n) resolve com folga
- `-100 <= nums[i] <= 100` → valores pequenos, soma cabe em `int` sem overflow
- `startValue` deve ser POSITIVO → a resposta mínima é sempre pelo menos 1

## 🧭 Como reconhecer o padrão

"Menor valor inicial para que uma soma acumulada nunca fique abaixo de um limiar" é resolvido calculando o PIOR PONTO da soma acumulada (o menor prefixo parcial) — o valor inicial precisa compensar exatamente esse pior ponto para que a soma nunca fique negativa.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar valores de `startValue` a partir de 1, incrementando, e para cada um simular a soma passo a passo verificando se ela nunca fica abaixo de 1; parar no primeiro `startValue` que funcionar.

- Tempo: O(n × maiorStartValueTestado) — repete a simulação completa da soma para cada candidato · Espaço: O(1)
- **Por que não basta:** recalcula a soma acumulada inteira para cada tentativa de `startValue`, quando o `startValue` mínimo pode ser derivado diretamente do MENOR valor que a soma de prefixo (sem o `startValue`) atinge.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule a soma de prefixo do array `nums` (sem incluir `startValue`), rastreando o MENOR valor que essa soma atinge em qualquer ponto (`menorPrefixo`). O `startValue` mínimo precisa satisfazer `startValue + menorPrefixo >= 1`, ou seja, `startValue = max(1, 1 - menorPrefixo)`.

## 🎬 Exemplo passo a passo

`nums = [-3,2,-3,4,2]`

| Passo | i | nums[i] | soma de prefixo acumulada | menorPrefixo até agora |
|---|---|---|---|---|
| 1 | 0 | -3 | -3 | -3 |
| 2 | 1 | 2 | -1 | -3 |
| 3 | 2 | -3 | -4 | -4 |
| 4 | 3 | 4 | 0 | -4 |
| 5 | 4 | 2 | 2 | -4 |

`menorPrefixo = -4`. `startValue = max(1, 1 - (-4)) = max(1, 5) = 5`

Resultado final: `5` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada calculando a soma de prefixo e o mínimo
- **Espaço:** O(1) extra

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minStartValue(int[] nums) {
    int somaAcumulada = 0;
    int menorPrefixo = 0; // considera o "prefixo vazio" (antes de somar qualquer elemento) como 0

    for (int num : nums) {
        somaAcumulada += num;
        menorPrefixo = Math.min(menorPrefixo, somaAcumulada);
    }

    return Math.max(1, 1 - menorPrefixo); // startValue precisa compensar o pior ponto da soma
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

- Esquecer que `startValue` precisa ser POSITIVO mesmo quando `menorPrefixo >= 0` (a soma nunca fica negativa mesmo sem ajuda) — nesses casos, a resposta ainda é `1` (o menor positivo possível), não `0` ou negativo.
- Inicializar `menorPrefixo` com o primeiro elemento em vez de `0` — o "prefixo vazio" (antes de somar `nums[0]`) precisa ser considerado como ponto de partida 0, já que a soma acumulada inclui o `startValue` desde o início.
- Confundir "menor valor da soma acumulada" com "menor elemento do array" — não é sobre o menor `nums[i]` individual, é sobre o menor valor que a SOMA ACUMULADA atinge em qualquer ponto do percurso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Soma cai bastante no meio | `[-3,2,-3,4,2]` | 5 | menor prefixo é -4, precisa de startValue=5 |
| Soma sempre positiva | `[1,2]` | 1 | menor prefixo já é >= 0, resposta mínima ainda é 1 (positivo) |
| Soma cai logo no início | `[1,-2,-3]` | 5 | menor prefixo é -4 (em 1-2-3), startValue=5 |
| Um único elemento negativo | `[-5]` | 6 | precisa compensar exatamente o único valor negativo |

## 🔗 Conexões

- Problemas irmãos: [0724] Find Pivot Index (mesma técnica base de soma de prefixo), [0053] Maximum Subarray (mesmo domínio de rastrear extremos de uma soma acumulada, técnica de Kadane)
- No backend: cálculo de saldo mínimo inicial necessário para uma conta nunca ficar negativa dado um histórico de transações (débitos e créditos) — aplicação direta em sistemas financeiros de fluxo de caixa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
