# [1248] Count Number of Nice Subarrays

> 🔗 [LeetCode 1248](https://leetcode.com/problems/count-number-of-nice-subarrays/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#PrefixSum` `#Medium`

## 📜 O Problema

Dado um array de inteiros `nums` e um inteiro `k`, um subarray contínuo é chamado **nice** (bonito) se contém `k` números ímpares. Retorne o número de subarrays nice.

**Exemplos:**
```
Input:  nums = [1,1,2,1,1], k = 3
Output: 2
Explicação: os únicos subarrays com 3 números ímpares são [1,1,2,1] e [1,2,1,1].

Input:  nums = [2,4,6], k = 1
Output: 0

Input:  nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 50000` → O(n²) força bruta é arriscado; O(n) é o esperado
- `1 <= k <= nums.length` → `k` sempre cabe dentro do tamanho do array

## 🧭 Como reconhecer o padrão

Se cada número ímpar virar `1` e cada par virar `0`, "contar subarrays com exatamente `k` números ímpares" é literalmente o mesmo problema de [0930] Binary Subarrays With Sum: contar subarrays com soma exatamente `k`. A técnica é a mesma diferença de duas contagens acumuladas: `atMost(k) - atMost(k-1)`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, contar quantos números ímpares existem no subarray e checar se são exatamente `k`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula a contagem de ímpares do zero a cada par, quando uma contagem corrente atualizada incrementalmente resolveria em O(1) por passo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Implemente `atMost(nums, g)`: conta subarrays com no máximo `g` números ímpares, usando dois ponteiros (encolhendo pela esquerda enquanto a contagem de ímpares exceder `g`, somando `right-left+1` a cada passo válido). A resposta final é `atMost(k) - atMost(k-1)`.

## 🎬 Exemplo passo a passo

`nums = [1,1,2,1,1]`, `k = 3` → paridade: `[1,1,0,1,1]` (1=ímpar, 0=par)

**atMost(3):**
| right | ímpar? | soma de ímpares | Encolhe? | left | válidas | total |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | não | 0 | 1 | 1 |
| 1 | 1 | 2 | não | 0 | 2 | 3 |
| 2 | 0 | 2 | não | 0 | 3 | 6 |
| 3 | 1 | 3 | não | 0 | 4 | 10 |
| 4 | 1 | 4 | sim: remove nums[0] (ímpar) → 3 | 1 | 4 | 14 |

`atMost(3) = 14`

**atMost(2):**
| right | ímpar? | soma de ímpares | Encolhe? | left | válidas | total |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | não | 0 | 1 | 1 |
| 1 | 1 | 2 | não | 0 | 2 | 3 |
| 2 | 0 | 2 | não | 0 | 3 | 6 |
| 3 | 1 | 3 | sim: remove nums[0] (ímpar) → 2 | 1 | 3 | 9 |
| 4 | 1 | 3 | sim: remove nums[1] (ímpar) → 2 | 2 | 3 | 12 |

`atMost(2) = 12`

Resultado final: `atMost(3) - atMost(2) = 14 - 12 = 2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numberOfSubarrays(int[] nums, int k) {
    return atMost(nums, k) - atMost(nums, k - 1);
}

private int atMost(int[] nums, int k) {
    if (k < 0) {
        return 0;
    }

    int left = 0;
    int oddCount = 0;
    int count = 0;

    for (int right = 0; right < nums.length; right++) {
        if (nums[right] % 2 != 0) {
            oddCount++;
        }

        while (oddCount > k) {
            if (nums[left] % 2 != 0) {
                oddCount--;
            }
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

- Contar subarrays com EXATAMENTE `k` ímpares diretamente com janela deslizante não funciona de forma direta — a saída é `atMost(k) - atMost(k-1)`, isolando exatamente os subarrays com `k` ímpares.
- `atMost` precisa tratar `k < 0` (retornando `0`), já que `k - 1` pode ficar negativo quando `k = 0` — embora as restrições garantam `k >= 1`, é um hábito de defesa correto.
- Confundir "contagem de ímpares" com "soma dos elementos" — o valor do número não importa, só sua paridade.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem números ímpares | `nums=[2,4,6]`, `k=1` | 0 | nenhum ímpar no array |
| Todos ímpares | `nums=[1,1,1]`, `k=2` | 2 | subarrays [1,1] (índices 0-1) e [1,1] (índices 1-2) |
| k igual ao total de ímpares | `nums=[1,1,2,1,1]`, `k=4` | 1 | só o array inteiro tem 4 ímpares |
| Exemplo do enunciado | `nums=[1,1,2,1,1]`, `k=3` | 2 | [1,1,2,1] e [1,2,1,1] |

## 🔗 Conexões

- Problemas irmãos: [0930] Binary Subarrays With Sum (mesmíssima técnica, reformulada apenas trocando "soma" por "contagem de ímpares"), [3258] Count Substrings That Satisfy K-Constraint I (mesma técnica de somar `right-left+1` para contar todas as janelas válidas)
- No backend: contar quantas janelas de eventos num fluxo contêm um número exato de ocorrências de um tipo específico (ex.: exatamente k tentativas de login falhas), útil em detecção de padrões de comportamento.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
