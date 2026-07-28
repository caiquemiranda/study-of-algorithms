# [1031] Maximum Sum of Two Non-Overlapping Subarrays

> 🔗 [LeetCode 1031](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#DynamicProgramming` `#Medium`

## 📜 O Problema

Dado um array de inteiros `nums` e dois inteiros `firstLen` e `secondLen`, retorne a soma máxima de elementos em duas subarrays **não sobrepostas** com comprimentos `firstLen` e `secondLen`. A subarray de comprimento `firstLen` pode vir antes ou depois da de comprimento `secondLen`, mas elas não podem se sobrepor.

**Exemplos:**
```
Input:  nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explicação: [9] (comprimento 1) e [6,5] (comprimento 2).

Input:  nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
```

**Restrições (e o que elas denunciam):**
- `1 <= firstLen, secondLen <= 1000`, `firstLen + secondLen <= nums.length <= 1000` → O(n²) testando todo par de posições é aceitável nesse tamanho, mas O(n) é alcançável
- As janelas podem aparecer em qualquer ordem → é preciso testar as duas orientações (`firstLen` antes de `secondLen`, e vice-versa)

## 🧭 Como reconhecer o padrão

"Duas janelas de tamanho **fixo** não sobrepostas, maximizando a soma" é resolvido combinando prefix sums com uma janela deslizante que mantém o melhor valor de UMA das janelas já visto até a posição atual — enquanto a outra janela desliza para a direita, sempre à frente da primeira, garantindo que nunca se sobreponham.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição da janela `M`, procurar do zero a melhor posição da janela `L` inteiramente à esquerda dela, recalculando cada soma de janela `L` a partir do array original.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula a soma de cada candidata a janela `L` repetidamente para cada posição de `M`, quando o melhor valor de `L` já visto poderia ser mantido incrementalmente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pré-compute prefix sums. Deslize a janela `M` da esquerda para a direita; a cada posição, atualize `Lmax` (a maior soma de uma janela `L` terminando em qualquer ponto até o início de `M`) e combine com a soma atual de `M`. Como o array de tamanhos pode aparecer nas duas ordens, chame essa lógica duas vezes — uma com `(L, M) = (firstLen, secondLen)`, outra com `(secondLen, firstLen)` — e retorne o maior resultado.

## 🎬 Exemplo passo a passo

`nums = [0,6,5,2,2,5,1,9,4]`, `firstLen = 1`, `secondLen = 2` — mostrando a orientação vencedora (`L=2` antes de `M=1`):

| i (posição da janela M) | Lmax (melhor janela L até aqui) | Msum (janela M em i) | Lmax+Msum | melhor |
|---|---|---|---|---|
| inicial (i=2) | 6 ([0,6]) | 5 (nums[2]) | 11 | 11 |
| 3 | 11 ([6,5]) | 2 (nums[3]) | 13 | 13 |
| 4 | 11 | 2 (nums[4]) | 13 | 13 |
| 5 | 11 | 5 (nums[5]) | 16 | 16 |
| 6 | 11 | 1 (nums[6]) | 12 | 16 |
| 7 | 11 | 9 (nums[7]) | 20 | 20 |
| 8 | 11 | 4 (nums[8]) | 15 | 20 |

Resultado desta orientação (L=2 antes de M=1): `20`. A orientação oposta (L=1 antes de M=2) produz no máximo `19`.

Resultado final: `max(20, 19) = 20` ✔ (janela [6,5] de tamanho 2 nos índices 1-2, mais [9] de tamanho 1 no índice 7)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) para cada orientação (prefix sums + uma passada), O(n) no total
- **Espaço:** O(n) para o array de prefix sums

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
    return Math.max(
        bestSum(nums, firstLen, secondLen),
        bestSum(nums, secondLen, firstLen)
    );
}

// L antes de M: acha a melhor combinação com a janela L à esquerda da janela M
private int bestSum(int[] nums, int L, int M) {
    int n = nums.length;
    int[] prefix = new int[n + 1];
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    int lMax = prefix[L]; // soma da primeira janela L possível, [0, L)
    int result = lMax + (prefix[L + M] - prefix[L]);

    for (int i = L + 1; i + M <= n; i++) {
        lMax = Math.max(lMax, prefix[i] - prefix[i - L]); // janela L terminando exatamente em i
        int mSum = prefix[i + M] - prefix[i];
        result = Math.max(result, lMax + mSum);
    }

    return result;
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

- As duas janelas podem aparecer em QUALQUER ordem — testar só uma orientação perde metade dos casos válidos; por isso a função auxiliar é chamada duas vezes, com os tamanhos trocados.
- `lMax` é o maior valor de janela `L` encontrado ATÉ a posição atual (nunca depois) — isso garante que a janela `L` e a janela `M` nunca se sobrepõem, já que `L` sempre termina antes (ou exatamente onde) `M` começa.
- Recalcular a soma da janela `L` do zero a cada posição, em vez de usar prefix sums, tornaria o algoritmo O(n²) — o ponto central da otimização é consultar qualquer soma de subarray em O(1).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Janelas ocupam o array inteiro | `nums=[1,2,1,3]`, `firstLen=2`, `secondLen=2` | 7 | única divisão possível: [1,2] e [1,3] |
| Tamanhos iguais | `nums=[1,1,1,1]`, `firstLen=2`, `secondLen=2` | 4 | duas janelas de tamanho 2 somando 2 cada |
| Uma orientação supera a outra | `nums=[3,8,1,3,2,1,8,9,0]`, `firstLen=3`, `secondLen=2` | 29 | [3,8,1] (tamanho 3) + [8,9] (tamanho 2) |
| Exemplo do enunciado | `nums=[0,6,5,2,2,5,1,9,4]`, `firstLen=1`, `secondLen=2` | 20 | [9] (tamanho 1) + [6,5] (tamanho 2) |

## 🔗 Conexões

- Problemas irmãos: [0643] Maximum Average Subarray I (mesma técnica-base de soma de janela fixa, aqui combinando DUAS janelas), [3364] Minimum Positive Sum Subarray (mesma técnica de prefix sums para consultar somas de subarray em O(1))
- No backend: escolher os dois melhores blocos de tempo não sobrepostos para agendar tarefas de tamanhos fixos diferentes (ex.: um bloco de manutenção curto e um longo) maximizando alguma métrica de valor ao longo de um período.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
