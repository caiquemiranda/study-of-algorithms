# [0413] Arithmetic Slices

> 🔗 [LeetCode 413](https://leetcode.com/problems/arithmetic-slices/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#DynamicProgramming` `#Medium`

## 📜 O Problema

Um array de inteiros é chamado **arithmetic** (aritmético) se tem pelo menos 3 elementos e a diferença entre quaisquer dois elementos consecutivos é a mesma. Dado um array `nums`, retorne o número de **subarrays** arithmetic de `nums`.

**Exemplos:**
```
Input:  nums = [1,2,3,4]
Output: 3
Explicação: temos 3 slices arithmetic: [1,2,3], [2,3,4] e [1,2,3,4].

Input:  nums = [1]
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 5000` → O(n³) enumerando todo subarray e checando a diferença estoura; O(n) é o esperado
- `-1000 <= nums[i] <= 1000` → valores pequenos, sem risco de overflow ao calcular diferenças

## 🧭 Como reconhecer o padrão

"Contar TODOS os subarrays contíguos que satisfazem uma condição de diferença constante" é resolvido mantendo um **run** (sequência corrente) de diferenças iguais: enquanto a condição se mantém, o run cresce e cada crescimento adiciona um número previsível de NOVAS slices terminando na posição atual; quando a condição quebra, o run reseta. Esse é o mesmo espírito de "expandir enquanto válido, resetar ao quebrar" das janelas deslizantes.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)` com `right - left >= 2`, checar se todas as diferenças consecutivas dentro do subarray são iguais.

- Tempo: O(n³) (O(n²) subarrays, O(n) para validar cada um) · Espaço: O(1)
- **Por que não basta:** revalida a diferença constante do zero a cada subarray candidato, mesmo quando ele é apenas o anterior estendido em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array comparando cada diferença consecutiva com a anterior. Mantenha um contador `cur` representando quantas NOVAS slices arithmetic terminam exatamente na posição atual: toda vez que a diferença bate com a anterior, `cur` incrementa (e soma-se ao total); quando quebra, `cur` volta a `0`.

## 🎬 Exemplo passo a passo

`nums = [1,2,3,4]`

| i | nums[i]-nums[i-1] | nums[i-1]-nums[i-2] | Iguais? | cur | total |
|---|---|---|---|---|---|
| 2 | 3-2=1 | 2-1=1 | sim | 1 | 1 |
| 3 | 4-3=1 | 3-2=1 | sim | 2 | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numberOfArithmeticSlices(int[] nums) {
    int cur = 0;
    int total = 0;

    for (int i = 2; i < nums.length; i++) {
        if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
            cur++; // mais uma slice arithmetic termina aqui: estende todas as anteriores em 1
            total += cur;
        } else {
            cur = 0; // a sequência de diferença constante quebrou, reinicia
        }
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

- `cur` representa quantas NOVAS slices arithmetic terminam exatamente no índice atual — somar `cur` (não `1`) ao total a cada passo é o que conta corretamente TODAS as subslices, não só a mais longa.
- Resetar `cur` para `0` (não `1`) quando a diferença quebra — a próxima possível slice só pode começar a ser contada a partir de 3 elementos novos consecutivos com diferença igual.
- Array com menos de 3 elementos nunca tem nenhuma slice arithmetic — o loop começando em `i=2` já lida com isso naturalmente, retornando 0 sem executar nenhuma iteração se `n<3`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Menos de 3 elementos | `[1]` | 0 | nenhuma slice possível, mínimo é 3 elementos |
| Sem nenhuma diferença constante | `[1,3,7,15]` | 0 | diferenças (2,4,8) nunca se repetem consecutivamente |
| Todos iguais (diferença 0 constante) | `[7,7,7,7]` | 3 | diferença constante 0 forma slices: [7,7,7],[7,7,7],[7,7,7,7] |
| Exemplo do enunciado | `[1,2,3,4]` | 3 | [1,2,3], [2,3,4], [1,2,3,4] |

## 🔗 Conexões

- Problemas irmãos: [3411] Maximum Subarray With Equal Products (mesma técnica de "run" que se estende ou reseta conforme uma condição local entre elementos consecutivos), [0978] Longest Turbulent Subarray (mesma família de acompanhar um contador que cresce ou reseta a cada comparação de vizinhos)
- No backend: contar quantos trechos de uma série temporal têm crescimento/decrescimento linear constante — por exemplo, detectar padrões de tendência estável em métricas de sistema, útil para identificar comportamento previsível versus anômalo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
