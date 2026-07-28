# [2760] Longest Even Odd Subarray With Threshold

> 🔗 [LeetCode 2760](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums` (0-indexado) e um inteiro `threshold`, encontre o comprimento do maior subarray começando em `l` e terminando em `r` que satisfaz: `nums[l] % 2 == 0`; para todo índice `i` em `[l, r-1]`, `nums[i] % 2 != nums[i+1] % 2` (paridade alterna); e para todo índice `i` em `[l, r]`, `nums[i] <= threshold`.

**Exemplos:**
```
Input:  nums = [3,2,5,4], threshold = 5
Output: 3
Explicação: o subarray [2,5,4] (índices 1 a 3) satisfaz todas as condições.

Input:  nums = [1,2], threshold = 2
Output: 1
Explicação: só [2] (índice 1) satisfaz.

Input:  nums = [2,3,4,5], threshold = 4
Output: 3
Explicação: o subarray [2,3,4] (índices 0 a 2) satisfaz.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`, `1 <= threshold <= 100` → entrada pequena, mas o padrão de janela sem retrocesso já resolve em O(n) mesmo para entradas maiores
- A condição de início (`nums[l]` par) e a condição de todo o intervalo (`<= threshold`) juntas descartam qualquer índice como início "genérico" — só índices pares e dentro do limite podem abrir um subarray válido

## 🧭 Como reconhecer o padrão

"Maior subarray contíguo satisfazendo uma condição local entre vizinhos (paridade alterna) e uma condição global (limite de valor)" é resolvido com uma janela deslizante que **nunca retrocede**: ao encontrar um início válido, expande-se o quanto for possível; quando a expansão para, o próximo início candidato só pode estar a partir de onde a expansão parou — nunca dentro do trecho já explorado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(l, r)` com `l <= r`, verificar diretamente as três condições percorrendo o intervalo inteiro.

- Tempo: O(n³) (O(n²) subarrays, O(n) para validar cada um) · Espaço: O(1)
- **Por que não basta:** revalida do zero a alternância de paridade e o limite de valor para cada subarray candidato, mesmo quando ele é apenas um subarray anterior estendido em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `nums` com um índice `i`. Se `nums[i]` não é par ou excede o `threshold`, `i` não pode iniciar um subarray válido — avance `i` em 1. Caso contrário, expanda `r` a partir de `i+1` enquanto `nums[r] <= threshold` e a paridade alterna em relação ao elemento anterior. Ao parar, registre o comprimento e pule `i` direto para `r` — qualquer início par dentro do trecho já percorrido gera, no máximo, um sufixo do subarray já encontrado, nunca um resultado maior.

## 🎬 Exemplo passo a passo

`nums = [3,2,5,4]`, `threshold = 5` (índices: 3₀ 2₁ 5₂ 4₃)

| i (início) | nums[i] par & ≤ threshold? | Expansão de r | Motivo da parada | Comprimento | Melhor |
|---|---|---|---|---|---|
| 0 | não (ímpar) | — | início inválido, i++ | — | 0 |
| 1 | sim | r=2 (5, ok, ímpar após par) → r=3 (4, ok, par após ímpar) → r=4 fora dos limites | fim do array | 3 (índices 1–3) | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — mesmo com o loop aninhado, cada índice é visitado no máximo uma vez ao todo (por `i` ou por `r`, nunca ambos reprocessando a mesma posição)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int longestAlternatingSubarray(int[] nums, int threshold) {
    int n = nums.length;
    int best = 0;
    int i = 0;

    while (i < n) {
        if (nums[i] % 2 != 0 || nums[i] > threshold) {
            i++; // não é um início válido, avança um passo
            continue;
        }

        int r = i + 1;
        while (r < n && nums[r] <= threshold && nums[r] % 2 != nums[r - 1] % 2) {
            r++;
        }

        best = Math.max(best, r - i);
        i = r; // pula direto pro ponto onde a extensão parou, sem retroceder
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

- Depois de expandir até `r`, reiniciar a busca em `i+1` em vez de `i = r` funciona mas é redundante — qualquer início par dentro do intervalo já explorado gera um subarray no máximo do mesmo tamanho ou menor.
- Esquecer de checar `nums[l] % 2 == 0` como condição do **primeiro** elemento — a alternância entre vizinhos não basta sozinha; o subarray só é válido se começar com um número par.
- Confundir "threshold" com limite de tamanho — é um limite de **valor** (`nums[i] <= threshold`) aplicado a todos os elementos do subarray, não um limite de quantidade de elementos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só um elemento válido | `nums=[1,2]`, `threshold=2` | 1 | apenas [2] (índice 1) satisfaz início par ≤ threshold |
| Início logo no índice 0 | `nums=[2,3,4,5]`, `threshold=4` | 3 | [2,3,4] alterna e respeita o threshold |
| Nenhum elemento par ≤ threshold | `nums=[1,3,5]`, `threshold=10` | 0 | nenhum índice pode iniciar um subarray válido |
| Threshold barra a extensão | `nums=[2,7]`, `threshold=5` | 1 | só [2] serve; 7 excede o threshold |

## 🔗 Conexões

- Problemas irmãos: [0485] Max Consecutive Ones (mesma família de "expandir enquanto uma condição local se mantém, sem retroceder"), [3090] Maximum Length Substring With Two Occurrences (mesma ideia de expandir uma janela variável validando uma condição a cada passo)
- No backend: identificar a maior sequência válida de leituras de sensores alternando entre dois estados (ex.: liga/desliga) dentro de um limite de valor aceitável, útil para detectar padrões de oscilação saudável versus saturação.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
