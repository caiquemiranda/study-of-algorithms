# [0674] Longest Continuous Increasing Subsequence

> 🔗 [LeetCode 674](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array desordenado de inteiros `nums`, retorne **o comprimento da maior subsequência contínua crescente** (ou seja, subarray). A subsequência deve ser **estritamente** crescente.

Uma **subsequência contínua crescente** é definida por dois índices `l` e `r` (`l < r`) tal que `nums[i] < nums[i+1]` para todo `l <= i < r`.

**Exemplos:**
```
Input:  nums = [1,3,5,4,7]
Output: 3
Explicação: a maior subsequência contínua crescente é [1,3,5], com tamanho 3.
Mesmo [1,3,5,7] sendo crescente, ela não é contínua (5 e 7 estão separados pelo elemento 4).

Input:  nums = [2,2,2,2,2]
Output: 1
Explicação: a maior subsequência contínua crescente é [2], tamanho 1. Precisa ser estritamente crescente.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → precisa O(n)
- `-10^9 <= nums[i] <= 10^9` → valores grandes, mas a operação é só comparação, sem risco de overflow
- "estritamente crescente" → elementos iguais QUEBRAM a sequência, não a continuam

## 🧭 Como reconhecer o padrão

Mesma assinatura de "maior sequência CONTÍGUA que satisfaz uma condição local entre vizinhos" (`nums[i] < nums[i+1]`): um contador que cresce enquanto a condição se mantém entre elementos adjacentes, e reseta a 1 assim que quebra.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição inicial `i`, expanda enquanto `nums[j] < nums[j+1]`, contando o tamanho, guardando o máximo.

- Tempo: O(n²) — repete a expansão a partir de cada índice, mesmo que já tenha sido "visitado" numa expansão anterior · Espaço: O(1)
- **Por que não basta:** se `nums[0..5]` já é uma sequência crescente, começar de novo em `i=1`, `i=2` etc. refaz um trabalho que a passada a partir de `i=0` já cobriu.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única passada comparando `nums[i]` com `nums[i-1]`. Se `nums[i] > nums[i-1]`, estende o contador atual; senão, reseta o contador para 1 (o próprio elemento atual já é uma sequência de tamanho 1). Atualiza o máximo a cada passo.

## 🎬 Exemplo passo a passo

`nums = [1,3,5,4,7]`

| Passo | i | nums[i] | nums[i-1] | condição | atual | maximo |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | — | (início) | 1 | 1 |
| 2 | 1 | 3 | 1 | 3>1, estende | 2 | 2 |
| 3 | 2 | 5 | 3 | 5>3, estende | 3 | 3 |
| 4 | 3 | 4 | 5 | 4<5, quebra | 1 | 3 |
| 5 | 4 | 7 | 4 | 7>4, estende | 2 | 3 |

Resultado final: `3` ✔ (`[1,3,5]`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) — dois contadores inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findLengthOfLCIS(int[] nums) {
    int atual = 1;
    int maximo = 1;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            atual++;                       // continua a sequência estritamente crescente
        } else {
            atual = 1;                     // quebrou (igual ou menor): reinicia contando o elemento atual
        }
        maximo = Math.max(maximo, atual);
    }
    return maximo;
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

- Usar `>=` em vez de `>` — o problema exige estritamente crescente; elementos iguais (`nums = [2,2,2]`) devem resetar o contador, não estendê-lo.
- Inicializar `atual` e `maximo` como `0` em vez de `1` — um array de um único elemento sempre tem sequência de tamanho pelo menos 1, mesmo sem nenhuma comparação acontecer.
- Resetar `atual` para `0` em vez de `1` ao quebrar a sequência — o próprio elemento que quebrou a sequência anterior já conta como o início de uma nova sequência de tamanho 1.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Quebra no meio | `[1,3,5,4,7]` | 3 | maior trecho é `[1,3,5]`, não o array inteiro |
| Todos iguais | `[2,2,2,2,2]` | 1 | "estritamente" crescente exclui repetições |
| Já decrescente | `[5,4,3,2,1]` | 1 | nenhum par consecutivo satisfaz a condição |
| Um elemento | `[7]` | 1 | menor entrada possível, sem comparação a fazer |

## 🔗 Conexões

- Problemas irmãos: [0485] Max Consecutive Ones (mesmo padrão de contador que reseta), [0128] Longest Consecutive Sequence (parecido no nome, mas resolve valores consecutivos SEM exigir contiguidade no array — técnica bem diferente, usa hash set)
- No backend: análise de séries temporais (ex.: maior período de crescimento contínuo de uma métrica, como vendas ou uso de CPU, antes de uma queda) — o mesmo contador de streak aparece em dashboards de monitoramento.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
