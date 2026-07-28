# [2379] Minimum Recolors to Get K Consecutive Black Blocks

> 🔗 [LeetCode 2379](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#String` `#Easy`

## 📜 O Problema

Dada uma string `blocks` (0-indexada) de comprimento `n`, onde cada `blocks[i]` é `'W'` (branco) ou `'B'` (preto), e um inteiro `k` representando o número desejado de blocos pretos **consecutivos**, cada operação recolore um bloco branco para preto. Retorne o **número mínimo** de operações para obter pelo menos uma ocorrência de `k` blocos pretos consecutivos.

**Exemplos:**
```
Input:  blocks = "WBBWWBBWBW", k = 7
Output: 3
Explicação: recolorindo os blocos 0, 3 e 4 obtemos "BBBBBBBWBW".

Input:  blocks = "WBWBBBW", k = 2
Output: 0
Explicação: já existem 2 blocos pretos consecutivos, nenhuma operação necessária.
```

**Restrições (e o que elas denunciam):**
- `n == blocks.length`, `1 <= n <= 100` → entrada pequena, O(n) já é folgado
- `blocks[i]` é `'W'` ou `'B'` → só dois estados, contagem simples de um deles resolve
- `1 <= k <= n` → sempre existe pelo menos uma janela de tamanho `k` para avaliar

## 🧭 Como reconhecer o padrão

"Janela de tamanho **fixo** `k`, minimizando o número de operações" é sliding window de tamanho fixo: o número de operações necessárias para uma janela virar toda preta é exatamente o número de `'W'` dentro dela. Basta deslizar a janela e achar a que tem menos `'W'`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada janela de tamanho `k`, contar quantos `'W'` ela tem percorrendo-a do zero.

- Tempo: O(n·k) · Espaço: O(1)
- **Por que não basta:** recomputa a contagem de `'W'` da janela inteira a cada posição, quando apenas um elemento sai à esquerda e um entra à direita entre janelas consecutivas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte os `'W'` da primeira janela de tamanho `k`. A cada deslizamento, se o elemento que sai (à esquerda) é `'W'`, decremente a contagem; se o que entra (à direita) é `'W'`, incremente. Mantenha o menor valor de contagem visto — essa é a resposta.

## 🎬 Exemplo passo a passo

`blocks = "WBBWWBBWBW"`, `k = 7` (índices: W0 B1 B2 W3 W4 B5 B6 W7 B8 W9)

| i | Janela | Remove | Adiciona | Contagem de W | Mínimo |
|---|---|---|---|---|---|
| 0 (inicial) | [0..6] | — | — | 3 | 3 |
| 1 | [1..7] | blocks[0]=W | blocks[7]=W | 3-1+1=3 | 3 |
| 2 | [2..8] | blocks[1]=B | blocks[8]=B | 3 | 3 |
| 3 | [3..9] | blocks[2]=B | blocks[9]=W | 3+1=4 | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — soma inicial O(k) mais `n-k` deslizamentos O(1) cada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumRecolors(String blocks, int k) {
    int whiteCount = 0;
    for (int i = 0; i < k; i++) {
        if (blocks.charAt(i) == 'W') {
            whiteCount++;
        }
    }

    int best = whiteCount;
    for (int i = k; i < blocks.length(); i++) {
        if (blocks.charAt(i) == 'W') {
            whiteCount++;
        }
        if (blocks.charAt(i - k) == 'W') {
            whiteCount--;
        }
        best = Math.min(best, whiteCount);
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

- Recontar os `'W'` do zero a cada janela em vez de ajustar incrementalmente — funciona para `n <= 100`, mas perde o ponto didático da técnica de janela deslizante (e não escalaria para entradas maiores).
- Confundir "operações necessárias" com "número de `'B'` já presentes" — o que importa é quantos `'W'` precisam virar `'B'`, não o inverso.
- Quando `k == n`, existe só uma janela — o loop de deslizamento nunca executa, e a resposta é simplesmente a contagem de `'W'` do array inteiro.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já satisfeito | `blocks="WBWBBBW"`, `k=2` | 0 | já existem 2 blocos pretos consecutivos |
| k igual a n | `blocks="WWWW"`, `k=4` | 4 | precisa recolorir todos os brancos |
| Só um bloco necessário | `blocks="W"`, `k=1` | 1 | um único W precisa virar B |
| Exemplo do enunciado | `blocks="WBBWWBBWBW"`, `k=7` | 3 | melhor janela de 7 tem só 3 W's |

## 🔗 Conexões

- Problemas irmãos: [0643] Maximum Average Subarray I (mesma técnica de janela fixa com ajuste incremental ao deslizar), [1004] Max Consecutive Ones III (mesma ideia de contar elementos "ruins" numa janela, mas com janela de tamanho variável em vez de fixo)
- No backend: calcular o menor esforço de correção dentro de uma janela de tamanho fixo — por exemplo, quantos registros inválidos precisam ser corrigidos num lote de tamanho fixo de transações processadas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
