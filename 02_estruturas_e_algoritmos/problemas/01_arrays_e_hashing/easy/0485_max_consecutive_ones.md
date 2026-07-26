# [0485] Max Consecutive Ones

> 🔗 [LeetCode 485](https://leetcode.com/problems/max-consecutive-ones/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#SlidingWindow` `#Easy`

## 📜 O Problema

Dado um array binário `nums`, retorne **o número máximo de 1's consecutivos no array**.

**Exemplos:**
```
Input:  nums = [1,1,0,1,1,1]
Output: 3
Explicação: os dois primeiros dígitos ou os três últimos são consecutivos. O máximo é 3.

Input:  nums = [1,0,1,1,0,1]
Output: 2
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → precisa de O(n)
- `nums[i]` é `0` ou `1` → só dois valores possíveis, sem necessidade de validação extra

## 🧭 Como reconhecer o padrão

"Maior sequência contígua de X" é sempre resolvido com um contador que cresce enquanto a condição se mantém e reseta assim que quebra — é a versão mais simples de janela deslizante: uma janela que só expande, nunca precisa encolher com dois ponteiros.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, expanda para a direita contando quantos 1s consecutivos existem a partir dali, guardando o máximo.

- Tempo: O(n²) — para cada início possível, percorre até o fim da sequência de 1s · Espaço: O(1)
- **Por que não basta:** recalcula do zero um trabalho que já foi feito ao processar posições anteriores dentro da mesma sequência de 1s.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única passada com um contador `atual` que incrementa a cada 1 e zera a cada 0, atualizando um `maximo` sempre que `atual` cresce.

## 🎬 Exemplo passo a passo

`nums = [1,1,0,1,1,1]`

| Passo | i | nums[i] | atual | maximo |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | 1 |
| 2 | 1 | 1 | 2 | 2 |
| 3 | 2 | 0 | 0 | 2 |
| 4 | 3 | 1 | 1 | 2 |
| 5 | 4 | 1 | 2 | 2 |
| 6 | 5 | 1 | 3 | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelo array
- **Espaço:** O(1) — só dois contadores inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findMaxConsecutiveOnes(int[] nums) {
    int atual = 0;
    int maximo = 0;
    for (int num : nums) {
        if (num == 1) {
            atual++;                      // estende a sequência corrente
            maximo = Math.max(maximo, atual);
        } else {
            atual = 0;                    // sequência quebrou, reinicia do zero
        }
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

- Esquecer de atualizar `maximo` a cada incremento (só atualizar quando encontra 0) — perde o caso em que a sequência mais longa é o próprio sufixo do array (nunca "quebra" para disparar a atualização).
- Resetar `atual` para `1` em vez de `0` ao encontrar um zero — erro comum de off-by-one que infla a contagem em 1.
- Não testar array de um único elemento — funciona naturalmente com o algoritmo, mas vale conferir no teste.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sequência no final | `[1,0,1,1,1]` | 3 | maior sequência é o sufixo, sem "quebra" final para disparar update |
| Só zeros | `[0,0,0]` | 0 | nunca incrementa `atual` |
| Só uns | `[1,1,1]` | 3 | array inteiro é uma única sequência |
| Elemento único | `[1]` | 1 | menor entrada possível |

## 🔗 Conexões

- Problemas irmãos: [0674] Longest Continuous Increasing Subsequence (mesmo padrão de contador que reseta), [1004] Max Consecutive Ones III (versão com sliding window de verdade, permitindo até k trocas de 0 para 1)
- No backend: monitoramento de uptime (maior sequência de checks "OK" consecutivos), detecção de streaks em métricas de qualidade (ex.: maior sequência de requisições bem-sucedidas antes de uma falha).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
