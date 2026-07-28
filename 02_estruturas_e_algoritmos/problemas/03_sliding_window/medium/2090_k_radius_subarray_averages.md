# [2090] K Radius Subarray Averages

> 🔗 [LeetCode 2090](https://leetcode.com/problems/k-radius-subarray-averages/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dado um array `nums` de `n` inteiros (0-indexado) e um inteiro `k`, a **k-radius average** de um subarray centrado no índice `i` é a média de todos os elementos entre os índices `i-k` e `i+k` (inclusive). Se houver menos de `k` elementos antes OU depois de `i`, a k-radius average é `-1`. Construa e retorne um array `avgs` de comprimento `n` onde `avgs[i]` é a k-radius average centrada em `i`. A média usa divisão **inteira** (trunca em direção a zero).

**Exemplos:**
```
Input:  nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]

Input:  nums = [100000], k = 0
Output: [100000]

Input:  nums = [8], k = 100000
Output: [-1]
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^5` → O(n·k) recalculando cada janela do zero é arriscado; O(n) é o esperado
- `0 <= nums[i], k <= 10^5` → `k` pode ser maior que o array inteiro, tornando todo índice `-1`

## 🧭 Como reconhecer o padrão

"Janela **centrada** de raio fixo `k` (tamanho `2k+1`)" é janela deslizante de tamanho fixo — a única diferença de [0643] Maximum Average Subarray I é que aqui o índice de saída (`avgs[i]`) corresponde ao CENTRO da janela, não ao seu início ou fim.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i`, somar os `2k+1` elementos ao redor dele (se existirem) do zero.

- Tempo: O(n·k) · Espaço: O(n) para a saída
- **Por que não basta:** recalcula a soma inteira a cada centro, mesmo que a janela vizinha compartilhe quase todos os elementos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule a soma da primeira janela válida (tamanho `2k+1`, centrada em `k`). Deslize subtraindo o elemento que sai e somando o que entra; o centro correspondente à janela `[i-k, i+k]` é `i`, mas ao deslizar por índice de janela (`right`), o centro é `right - k`.

## 🎬 Exemplo passo a passo

`nums = [7,4,3,9,1,8,5,2,6]`, `k = 3` (tamanho da janela: 7)

| Centro i | Janela (índices) | Soma | Média (divisão inteira) |
|---|---|---|---|
| 0,1,2 | (menos de k elementos antes) | — | -1 |
| 3 | [0..6] | 37 | 37/7=5 |
| 4 | [1..7] | 32 | 32/7=4 |
| 5 | [2..8] | 34 | 34/7=4 |
| 6,7,8 | (menos de k elementos depois) | — | -1 |

Resultado final: `[-1,-1,-1,5,4,4,-1,-1,-1]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n) para o array de saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] getAverages(int[] nums, int k) {
    int n = nums.length;
    int[] avgs = new int[n];
    Arrays.fill(avgs, -1);

    int windowSize = 2 * k + 1;
    if (windowSize > n) {
        return avgs; // nenhum centro tem k elementos de cada lado
    }

    long windowSum = 0;
    for (int i = 0; i < windowSize; i++) {
        windowSum += nums[i];
    }
    avgs[k] = (int) (windowSum / windowSize);

    for (int i = windowSize; i < n; i++) {
        windowSum += nums[i] - nums[i - windowSize];
        avgs[i - k] = (int) (windowSum / windowSize); // centro da janela atual
    }

    return avgs;
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

- O CENTRO da janela `[i-k, i+k]` é o índice `i`, mas ao deslizar a janela de tamanho fixo `2k+1`, o centro correspondente à posição final da janela é `right - k`, não `right` — fácil de errar esse deslocamento.
- Divisão INTEIRA (truncando, não arredondando) é explicitamente exigida pelo enunciado — `37/7` em Java já trunca naturalmente para inteiros, mas em outras linguagens vale conferir.
- Quando `2k+1 > n`, nenhum índice tem `k` elementos de cada lado — o array inteiro de saída é `-1`, sem sequer entrar no loop principal.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 (janela de 1 elemento) | `nums=[100000]`, `k=0` | [100000] | a "média" de um único elemento é ele mesmo |
| k maior que o array permite | `nums=[8]`, `k=100000` | [-1] | nenhum centro tem k elementos de cada lado |
| Divisão inteira trunca | soma não múltipla do tamanho da janela | trunca pra baixo | regra explícita do enunciado |
| Exemplo do enunciado | `nums=[7,4,3,9,1,8,5,2,6]`, `k=3` | [-1,-1,-1,5,4,4,-1,-1,-1] | só os índices 3,4,5 têm k elementos completos dos dois lados |

## 🔗 Conexões

- Problemas irmãos: [0643] Maximum Average Subarray I (mesma técnica-base de janela fixa com soma incremental), [2379] Minimum Recolors to Get K Consecutive Black Blocks (mesma família de janela fixa deslizando)
- No backend: calcular médias móveis centradas de uma métrica de série temporal (suavização de um gráfico), preenchendo com um sentinela nos extremos onde não há dados suficientes.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
