# [1984] Minimum Difference Between Highest and Lowest of K Scores

> 🔗 [LeetCode 1984](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array `nums` (0-indexado) onde `nums[i]` é a nota do `i`-ésimo aluno, e um inteiro `k`, escolha as notas de `k` alunos quaisquer de forma que a diferença entre a maior e a menor nota escolhida seja **mínima**. Retorne essa diferença mínima possível.

**Exemplos:**
```
Input:  nums = [90], k = 1
Output: 0
Explicação: só uma nota escolhida, diferença sempre 0.

Input:  nums = [9,4,1,7], k = 2
Output: 2
Explicação: a melhor escolha é [9,7] (ou [7,9]), diferença 9-7=2.
```

**Restrições (e o que elas denunciam):**
- `1 <= k <= nums.length <= 1000` → testar todos os `C(n,k)` subconjuntos é combinatoriamente inviável; O(n log n) é o esperado
- `0 <= nums[i] <= 10^5` → valores cabem em `int` sem risco de overflow na subtração

## 🧭 Como reconhecer o padrão

"Escolher `k` elementos minimizando a diferença entre o maior e o menor" tem uma propriedade-chave: depois de **ordenar** o array, a melhor escolha de `k` elementos é sempre um **bloco contíguo** no array ordenado — qualquer conjunto não contíguo pode ser trocado por um bloco contíguo de mesmo tamanho com diferença igual ou menor. Isso transforma o problema em deslizar uma janela de tamanho **fixo** `k` sobre o array ordenado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todos os `C(n, k)` subconjuntos de tamanho `k` possíveis, calculando a diferença máximo-mínimo de cada um.

- Tempo: O(C(n,k) · k), combinatoriamente explosivo · Espaço: O(k) por subconjunto
- **Por que não basta:** não aproveita que a ordem dos valores escolhidos não importa nem que a resposta ótima está sempre entre elementos vizinhos depois de ordenados — sem ordenar, não há como restringir a busca a blocos contíguos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums`. Depois, para cada início `i` de `0` a `n-k`, calcule `nums[i+k-1] - nums[i]` — a diferença entre o maior e o menor elemento de uma janela de tamanho `k` no array **ordenado** — e mantenha o menor valor encontrado.

## 🎬 Exemplo passo a passo

`nums = [9,4,1,7]`, `k = 2` → ordenado: `[1,4,7,9]`

| i | Janela ordenada | nums[i+k-1] | nums[i] | Diferença | Melhor |
|---|---|---|---|---|---|
| 0 | [1,4] | 4 | 1 | 3 | 3 |
| 1 | [4,7] | 7 | 4 | 3 | 3 |
| 2 | [7,9] | 9 | 7 | 2 | 2 |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura da janela depois é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort usado internamente

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumDifference(int[] nums, int k) {
    Arrays.sort(nums);
    int best = Integer.MAX_VALUE;

    for (int i = 0; i + k - 1 < nums.length; i++) {
        int diff = nums[i + k - 1] - nums[i];
        best = Math.min(best, diff);
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

- Esquecer de **ordenar** antes de deslizar a janela — sem ordenação, uma janela contígua no array original não representa o melhor conjunto de `k` valores.
- `k = 1` é um caso válido (`1 <= k <= nums.length`): a diferença é sempre `0`, pois um único score tem `max == min`. O algoritmo já trata isso naturalmente (`nums[i] - nums[i] = 0`).
- Tentar resolver com busca combinatória de todos os subconjuntos de tamanho `k` — ignora a propriedade-chave de que a resposta ótima está sempre entre elementos **adjacentes** no array ordenado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=1 | `nums=[90]`, `k=1` | 0 | único score escolhido, diferença sempre 0 |
| k igual ao tamanho do array | `nums=[9,4,1,7]`, `k=4` | 8 | obrigado a pegar todos, diferença é max-min do array inteiro |
| Todos os valores iguais | `nums=[5,5,5]`, `k=2` | 0 | qualquer par tem diferença 0 |
| Exemplo do enunciado | `nums=[9,4,1,7]`, `k=2` | 2 | janela [7,9] no array ordenado é a mais "apertada" |

## 🔗 Conexões

- Problemas irmãos: [0220] Contains Duplicate III (mesma ideia de olhar diferenças dentro de uma janela, mas sobre índices em vez de valores ordenados), [0643] Maximum Average Subarray I (mesma técnica de janela de tamanho fixo deslizando, aqui aplicada depois de ordenar)
- No backend: agrupar recursos em faixas mais homogêneas possíveis — por exemplo, escolher `k` servidores com capacidades mais próximas entre si para formar um cluster balanceado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
