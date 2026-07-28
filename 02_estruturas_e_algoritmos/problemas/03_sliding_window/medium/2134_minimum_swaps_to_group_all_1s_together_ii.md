# [2134] Minimum Swaps to Group All 1's Together II

> 🔗 [LeetCode 2134](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Um **swap** troca os valores de duas posições distintas de um array. Um array **circular** considera o primeiro e o último elemento como adjacentes. Dado um array binário **circular** `nums`, retorne o número mínimo de swaps necessários para agrupar todos os `1`s juntos em qualquer localização.

**Exemplos:**
```
Input:  nums = [0,1,0,1,1,0,0]
Output: 1

Input:  nums = [0,1,1,1,0,0,1,1,0]
Output: 2

Input:  nums = [1,1,0,0,1]
Output: 0
Explicação: os 1's já estão agrupados devido à propriedade circular.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `nums[i]` é `0` ou `1`, array **circular** → o bloco final onde os 1's ficam agrupados tem sempre o mesmo tamanho: `totalOnes`

## 🧭 Como reconhecer o padrão

"Agrupar todos os 1's num bloco contíguo, minimizando trocas" é resolvido reconhecendo que o bloco final deve ter tamanho exatamente `totalOnes` (a quantidade de 1's no array) — deslize uma janela **circular** de tamanho fixo `totalOnes`, contando quantos `0`s ela tem em cada posição; o menor número de zeros encontrado é o número mínimo de swaps (cada zero dentro do bloco precisa ser trocado por um 1 de fora).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição inicial do bloco de tamanho `totalOnes`, contar os zeros dentro dele do zero, tratando a circularidade com módulo.

- Tempo: O(n·totalOnes) · Espaço: O(1)
- **Por que não basta:** recalcula a contagem de zeros do zero a cada posição do bloco, quando apenas um elemento sai e um entra entre posições vizinhas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte `totalOnes`. Deslize uma janela circular de tamanho `totalOnes` (usando índices módulo `n`), mantendo a contagem de `1`s dentro dela incrementalmente. O número de swaps para aquela janela é `totalOnes - (uns na janela)` (os zeros restantes). Minimize essa quantidade sobre todas as posições.

## 🎬 Exemplo passo a passo

`nums = [0,1,0,1,1,0,0]` (n=7, totalOnes=3)

| Janela (índices, circular) | Valores | Zeros na janela |
|---|---|---|
| [0,1,2] | 0,1,0 | 2 |
| [1,2,3] | 1,0,1 | 1 |
| [2,3,4] | 0,1,1 | 1 |
| [3,4,5] | 1,1,0 | 1 |
| [4,5,6] | 1,0,0 | 2 |
| [5,6,0] | 0,0,0 | 3 |
| [6,0,1] | 0,0,1 | 2 |

Resultado final (mínimo de zeros entre todas as janelas): `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minSwaps(int[] nums) {
    int n = nums.length;
    int totalOnes = 0;
    for (int num : nums) {
        totalOnes += num;
    }
    if (totalOnes == 0 || totalOnes == n) {
        return 0; // nada pra agrupar, ou já é tudo 1
    }

    int windowOnes = 0;
    for (int i = 0; i < totalOnes; i++) {
        windowOnes += nums[i];
    }

    int maxOnes = windowOnes;
    for (int i = totalOnes; i < n + totalOnes - 1; i++) {
        int inIndex = i % n; // índice circular do elemento que entra
        int outIndex = (i - totalOnes) % n; // índice circular do elemento que sai
        windowOnes += nums[inIndex] - nums[outIndex];
        maxOnes = Math.max(maxOnes, windowOnes);
    }

    return totalOnes - maxOnes; // zeros na melhor janela = trocas necessárias
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

- O tamanho da janela é sempre `totalOnes` (a quantidade de 1's no array), não um valor arbitrário — é o único tamanho de "bloco compacto" que poderia conter todos os 1's juntos.
- O array é CIRCULAR — a última janela pode "dar a volta" ao início, exigindo índices módulo `n` no deslizamento, igual a [1652] Defuse the Bomb.
- Minimizar zeros na janela é equivalente a MAXIMIZAR uns na janela (já que o tamanho é fixo) — a implementação acima maximiza uns e subtrai de `totalOnes` no final, mas ambas as formulações levam à mesma resposta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já agrupados (usando circularidade) | `[1,1,0,0,1]` | 0 | os 1's já formam um bloco contíguo circular |
| Sem nenhum 1 | `[0,0,0]` | 0 | nada para agrupar |
| Todos 1 | `[1,1,1]` | 0 | já é um único bloco (o array inteiro) |
| Exemplo do enunciado | `[0,1,0,1,1,0,0]` | 1 | melhor janela de tamanho 3 tem só 1 zero |

## 🔗 Conexões

- Problemas irmãos: [1652] Defuse the Bomb (mesma técnica de janela fixa circular com índices módulo n), [2379] Minimum Recolors to Get K Consecutive Black Blocks (mesma ideia de contar elementos "errados" numa janela de tamanho fixo, aqui generalizada pra array circular)
- No backend: calcular o menor número de realocações para agrupar recursos de um mesmo tipo (réplicas de um serviço) num bloco contíguo de um anel de servidores (topologia circular).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
