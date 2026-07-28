# [1838] Frequency of the Most Frequent Element

> 🔗 [LeetCode 1838](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Sorting` `#Medium`

## 📜 O Problema

A **frequência** de um elemento é o número de vezes que ele ocorre num array. Dado um array de inteiros `nums` e um inteiro `k`, em uma operação você pode escolher um índice de `nums` e incrementar o elemento nele em `1`. Retorne a **frequência máxima possível** de um elemento depois de no máximo `k` operações.

**Exemplos:**
```
Input:  nums = [1,2,4], k = 5
Output: 3
Explicação: incremente o primeiro elemento 3 vezes e o segundo 2 vezes para obter [4,4,4].

Input:  nums = [1,4,8,13], k = 5
Output: 2

Input:  nums = [3,9,6], k = 2
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) força bruta é arriscado; O(n log n) é o esperado (dominado pela ordenação)
- `1 <= nums[i] <= 10^5`, `1 <= k <= 10^5` → o custo de igualar uma janela pode ficar grande, exigindo `long` na multiplicação

## 🧭 Como reconhecer o padrão

"Maximizar a frequência de um valor usando um orçamento de incrementos" fica muito mais simples depois de ORDENAR: dentro de uma janela ordenada, o alvo mais barato de igualar é sempre o MAIOR valor já presente na janela (`nums[right]`) — incrementar até um valor menor nunca compensa. O custo de igualar a janela inteira a `nums[right]` é `nums[right] * comprimento - soma`; encolhe-se a janela enquanto esse custo exceder `k`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada valor-alvo candidato, calcular quantos elementos dá pra elevar até ele dentro do orçamento `k`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** testa cada valor-alvo isoladamente, recalculando o custo do zero, quando uma janela deslizante sobre o array ordenado resolve isso incrementalmente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums`. Expanda `right`, somando à soma corrente. O custo de igualar a janela `[left, right]` ao valor `nums[right]` é `nums[right] * (right-left+1) - soma`. Enquanto esse custo exceder `k`, encolha `left`. A cada passo válido, atualize o maior comprimento de janela visto — essa é a maior frequência alcançável.

## 🎬 Exemplo passo a passo

`nums = [1,2,4]`, `k = 5` (já ordenado)

| right | nums[right] | sum | custo = nums[right]*len - sum | <=k? | comprimento | melhor |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1·1-1=0 | sim | 1 | 1 |
| 1 | 2 | 3 | 2·2-3=1 | sim | 2 | 2 |
| 2 | 4 | 7 | 4·3-7=5 | sim | 3 | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura da janela depois é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxFrequency(int[] nums, int k) {
    Arrays.sort(nums);
    int left = 0;
    long sum = 0;
    int best = 1;

    for (int right = 0; right < nums.length; right++) {
        sum += nums[right];

        // custo para igualar toda a janela ao maior valor (nums[right])
        while ((long) nums[right] * (right - left + 1) - sum > k) {
            sum -= nums[left];
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
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

- Depois de ordenar, o "alvo" de cada janela é sempre `nums[right]` (o maior valor dela) — nunca compensa tentar igualar a um valor menor dentro da janela, porque subir até o maior já presente é sempre mais barato.
- O custo `nums[right] * comprimento - soma` pode ficar grande — usar `long` na multiplicação evita overflow quando `nums[right]` e o comprimento da janela são ambos grandes.
- Ordenar destrói os índices originais, mas como só a FREQUÊNCIA (não a posição) importa na resposta, isso não é um problema aqui.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 (sem operações) | `nums=[1,2,4]`, `k=0` | 1 | sem poder incrementar, cada valor já é seu próprio grupo |
| Todos os valores já iguais | `nums=[3,3,3]`, `k=5` | 3 | nenhuma operação necessária |
| k grande o bastante pro array inteiro | `nums=[3,9,6]`, `k=100` | 3 | orçamento generoso alcança igualar todo mundo |
| Exemplo do enunciado | `nums=[1,2,4]`, `k=5` | 3 | incrementa 1→4 (3 ops) e 2→4 (2 ops), total 5 |

## 🔗 Conexões

- Problemas irmãos: [1423] Maximum Points You Can Obtain from Cards (mesma técnica-base de janela deslizante sobre array ordenado/prefix sum), [1984] Minimum Difference Between Highest and Lowest of K Scores (mesma ideia de janela sobre array ordenado, aqui com orçamento de operações em vez de tamanho fixo)
- No backend: calcular quantos registros podem ser normalizados para um mesmo valor-alvo dentro de um orçamento limitado de ajustes, útil em reconciliação de preços ou cotas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
