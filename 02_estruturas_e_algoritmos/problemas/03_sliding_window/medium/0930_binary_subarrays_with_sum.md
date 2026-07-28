# [0930] Binary Subarrays With Sum

> 🔗 [LeetCode 930](https://leetcode.com/problems/binary-subarrays-with-sum/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#PrefixSum` `#Medium`

## 📜 O Problema

Dado um array binário `nums` e um inteiro `goal`, retorne o número de **subarrays** não vazios com soma exatamente `goal`.

**Exemplos:**
```
Input:  nums = [1,0,1,0,1], goal = 2
Output: 4

Input:  nums = [0,0,0,0,0], goal = 0
Output: 15
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 3 * 10^4` → O(n²) força bruta é arriscado; O(n) é o esperado
- `nums[i]` é `0` ou `1` → binário, permitindo a técnica de dois ponteiros (soma monotônica)
- `0 <= goal <= nums.length` → `goal` pode ser `0`, um caso que exige tratamento cuidadoso

## 🧭 Como reconhecer o padrão

"Contar subarrays com soma **exatamente** igual a um alvo" não dá pra resolver diretamente encolhendo uma janela (a soma não "aponta" para uma única resposta ao encolher). A saída é a técnica de **diferença de duas contagens acumuladas**: `atMost(goal) - atMost(goal-1)`, onde `atMost(g)` conta subarrays com soma `<= g` usando janela deslizante clássica (válida aqui porque todos os valores são não-negativos).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, somar o subarray do zero e checar se a soma é exatamente `goal`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula a soma inteira a cada par, quando uma soma corrente atualizada incrementalmente resolveria isso em O(1) por passo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Implemente `atMost(nums, g)`: conta subarrays com soma `<= g` usando dois ponteiros (encolhendo pela esquerda enquanto a soma exceder `g`, somando `right-left+1` a cada passo válido). A resposta final é `atMost(goal) - atMost(goal-1)` — isolando exatamente os subarrays cuja soma é `goal`.

## 🎬 Exemplo passo a passo

`nums = [1,0,1,0,1]`, `goal = 2`

**Trace de `atMost(2)`:**
| right | nums[right] | sum após incluir | Encolhe? | left final | subarrays válidos (right-left+1) | total |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | não | 0 | 1 | 1 |
| 1 | 0 | 1 | não | 0 | 2 | 3 |
| 2 | 1 | 2 | não | 0 | 3 | 6 |
| 3 | 0 | 2 | não | 0 | 4 | 10 |
| 4 | 1 | 3 | sim: remove nums[0]=1 → sum=2 | 1 | 4 | 14 |

`atMost(2) = 14`

**Trace de `atMost(1)` (mesma mecânica, alvo menor):**
| right | nums[right] | sum após incluir | Encolhe? | left final | subarrays válidos | total |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | não | 0 | 1 | 1 |
| 1 | 0 | 1 | não | 0 | 2 | 3 |
| 2 | 1 | 2 | sim: remove nums[0]=1 → sum=1 | 1 | 2 | 5 |
| 3 | 0 | 1 | não | 1 | 3 | 8 |
| 4 | 1 | 2 | sim: remove nums[1]=0 → sum=2 (ainda>1!) → remove nums[2]=1 → sum=1 | 3 | 2 | 10 |

`atMost(1) = 10`

Resultado final: `atMost(2) - atMost(1) = 14 - 10 = 4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas O(n) cada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numSubarraysWithSum(int[] nums, int goal) {
    return atMost(nums, goal) - atMost(nums, goal - 1);
}

private int atMost(int[] nums, int goal) {
    if (goal < 0) {
        return 0; // nenhum subarray tem soma <= a um alvo negativo (soma mínima é 0)
    }

    int left = 0;
    int sum = 0;
    int count = 0;

    for (int right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum > goal) {
            sum -= nums[left];
            left++;
        }

        count += right - left + 1;
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

- Contar subarrays com soma **exatamente** `goal` diretamente com janela deslizante não funciona de forma direta — a saída é contar `atMost(goal) - atMost(goal-1)`.
- `atMost` precisa tratar `goal < 0` como caso especial (retornando `0`), já que `goal - 1` pode ficar negativo quando o `goal` original é `0`.
- Confundir "quantos subarrays com soma <= goal" com "qual o subarray com soma <= goal" — a técnica de somar `right-left+1` a cada passo conta TODOS os subarrays terminando em `right` que são válidos, não só um.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| goal=0 (só zeros) | `nums=[0,0,0,0,0]`, `goal=0` | 15 | todo subarray de puros zeros soma 0; C(5+1,2)=15 |
| Nenhum subarray soma o alvo | `nums=[0,0,0]`, `goal=1` | 0 | não há nenhum 1 no array |
| Array de um elemento | `nums=[1]`, `goal=1` | 1 | único subarray, soma exatamente 1 |
| Exemplo do enunciado | `nums=[1,0,1,0,1]`, `goal=2` | 4 | 4 subarrays somam exatamente 2 |

## 🔗 Conexões

- Problemas irmãos: [0560] Subarray Sum Equals K (mesma técnica geral de "diferença de duas contagens acumuladas", mas usando prefix sums em vez de janela deslizante, pois os valores podem ser negativos), [3258] Count Substrings That Satisfy K-Constraint I (mesma técnica de somar `right-left+1` para contar todas as janelas válidas)
- No backend: contar quantas janelas de eventos binários (sucesso/falha) têm exatamente um número-alvo de ocorrências de sucesso, útil em auditoria de logs de sistemas binários.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
