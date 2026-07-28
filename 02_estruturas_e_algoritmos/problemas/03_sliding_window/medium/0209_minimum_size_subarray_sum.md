# [0209] Minimum Size Subarray Sum

> 🔗 [LeetCode 209](https://leetcode.com/problems/minimum-size-subarray-sum/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#PrefixSum` `#Medium`

## 📜 O Problema

Dado um array de inteiros **positivos** `nums` e um inteiro positivo `target`, retorne o **comprimento mínimo** de um subarray contíguo cuja soma seja maior ou igual a `target`. Se não existir tal subarray, retorne `0`.

**Exemplos:**
```
Input:  target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explicação: o subarray [4,3] tem o menor comprimento sob a restrição do problema.

Input:  target = 4, nums = [1,4,4]
Output: 1

Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= target <= 10^9`, `1 <= nums.length <= 10^5` → O(n²) força bruta é arriscado nesse tamanho; O(n) é o esperado
- `1 <= nums[i] <= 10^4` → **todos os valores são positivos** — essa é a chave que permite a técnica de janela deslizante: somar mais elementos só aumenta a soma, removê-los só diminui, uma propriedade monotônica indispensável aqui

## 🧭 Como reconhecer o padrão

"Menor subarray cuja soma atinge um alvo, com todos os valores positivos" é o padrão canônico de janela deslizante variável que **encolhe**: como cada elemento é positivo, expandir a janela pela direita só aumenta a soma, e encolher pela esquerda só diminui — essa monotonicidade garante que dá pra encolher com segurança sempre que a condição ainda estiver satisfeita.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, somar o subarray do zero e checar se atinge o alvo, atualizando o menor tamanho encontrado.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula a soma inteira a cada par, ignorando que valores positivos permitem manter uma soma corrente que só cresce ao expandir e só diminui ao encolher.

## 💡 Solução 2 — A ideia otimizada (intuição)

Expanda `right`, somando `nums[right]` a uma soma corrente. Enquanto a soma corrente for `>= target`, registre `right - left + 1` como candidato e encolha `left` (subtraindo `nums[left]`, avançando `left`) — tentando um subarray ainda menor.

## 🎬 Exemplo passo a passo

`target = 7`, `nums = [2,3,1,2,4,3]`

| right | sum após incluir | ≥ target? | Encolhimentos (sum, left) | Melhor comprimento |
|---|---|---|---|---|
| 0 | 2 | não | — | ∞ |
| 1 | 5 | não | — | ∞ |
| 2 | 6 | não | — | ∞ |
| 3 | 8 | sim | remove nums[0]=2 → sum=6, left=1 (para) | 4 |
| 4 | 10 | sim | remove nums[1]=3 → sum=7 (ainda ≥7!) → remove nums[2]=1 → sum=6, left=3 (para) | 3 |
| 5 | 9 | sim | remove nums[3]=2 → sum=7 (ainda ≥7!) → remove nums[4]=4 → sum=3, left=5 (para) | 2 |

Resultado final: `2` ✔ (subarray [4,3])

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `right` percorre a string uma vez; `left` só avança, nunca retrocede, então no total anda no máximo `n` passos
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minSubArrayLen(int target, int[] nums) {
    int left = 0;
    long sum = 0;
    int best = Integer.MAX_VALUE;

    for (int right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum >= target) {
            best = Math.min(best, right - left + 1);
            sum -= nums[left]; // encolhe pela esquerda em busca de um subarray ainda menor
            left++;
        }
    }

    return best == Integer.MAX_VALUE ? 0 : best;
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

- Essa técnica de encolher a janela SÓ funciona porque todos os valores são positivos (`1 <= nums[i]`) — com valores negativos presentes, a soma não seria monotônica e o encolhimento poderia pular a resposta correta (como em [3364] Minimum Positive Sum Subarray).
- Usar `if` em vez de `while` ao encolher a janela perde oportunidades de encolher MAIS de uma vez quando a soma ainda está acima do alvo depois da primeira remoção.
- Esquecer o caso em que nenhum subarray atinge o alvo — retornar `0` (não `-1` nem o tamanho do array inteiro) quando `best` nunca foi atualizado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhum subarray atinge o alvo | `target=11`, `nums=[1,1,1,1,1,1,1,1]` | 0 | soma total (8) já é menor que o alvo |
| Um único elemento já basta | `target=4`, `nums=[1,4,4]` | 1 | `nums[1]=4` sozinho atinge o alvo |
| Array inteiro necessário | `target=15`, `nums=[1,2,3,4,5]` | 5 | só a soma de todos os elementos (15) atinge o alvo |
| Exemplo do enunciado | `target=7`, `nums=[2,3,1,2,4,3]` | 2 | subarray [4,3] soma 7 com o menor tamanho possível |

## 🔗 Conexões

- Problemas irmãos: [3364] Minimum Positive Sum Subarray (mesma família de soma de subarray, mas com valores negativos permitidos, o que impede a técnica de encolher janela e exige prefix sums em vez disso), [0003] Longest Substring Without Repeating Characters (mesma técnica de dois ponteiros com janela variável, buscando o extremo oposto — o MAIOR subarray válido, em vez do MENOR)
- No backend: encontrar o menor lote de eventos consecutivos cuja soma de "peso" (bytes, custo, tempo de processamento) atinge um limite mínimo — útil para agrupar itens de uma fila até acumular um valor mínimo de processamento em lote.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
