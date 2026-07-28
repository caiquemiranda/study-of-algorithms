# [1493] Longest Subarray of 1's After Deleting One Element

> 🔗 [LeetCode 1493](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dado um array binário `nums`, você deve deletar exatamente um elemento dele. Retorne o tamanho do maior subarray não vazio contendo só `1`s no array resultante. Retorne `0` se não existir tal subarray.

**Exemplos:**
```
Input:  nums = [1,1,0,1]
Output: 3
Explicação: deletando a posição 2, [1,1,1] tem 3 números com valor 1.

Input:  nums = [0,1,1,1,0,1,1,0,1]
Output: 5

Input:  nums = [1,1,1]
Output: 2
Explicação: você é obrigado a deletar um elemento.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `nums[i]` é `0` ou `1` → o mesmo padrão "no máximo k zeros" de [1004] Max Consecutive Ones III, com `k=1`, mas com uma pegadinha extra: a deleção é OBRIGATÓRIA

## 🧭 Como reconhecer o padrão

"Maior janela de 1s permitindo no máximo 1 zero" é o mesmo padrão de [1004] Max Consecutive Ones III com `k=1` — a diferença é que aqui a deleção é OBRIGATÓRIA, mesmo quando não há zero para remover. Isso significa que a resposta final é sempre `melhorJanela - 1`, nunca a janela bruta.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada elemento a deletar, simular a remoção e procurar a maior sequência de 1s consecutivos no array resultante.

- Tempo: O(n²) · Espaço: O(n) por simulação
- **Por que não basta:** simula fisicamente cada deleção possível e reprocessa o array inteiro, quando a janela deslizante resolve isso numa única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Encontre a maior janela com no máximo 1 zero (a técnica clássica de [1004]). O zero "restante" dentro dessa janela é justamente o que será deletado; se a janela não tiver zero nenhum, ainda assim um elemento (um `1`) precisa ser removido. Em ambos os casos, a resposta é `melhorJanela - 1`.

## 🎬 Exemplo passo a passo

`nums = [0,1,1,1,0,1,1,0,1]`

| right | nums[right] | zeros | Encolhe? | left final | comprimento (at most 1 zero) | melhor |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | não | 0 | 1 | 1 |
| 1 | 1 | 1 | não | 0 | 2 | 2 |
| 2 | 1 | 1 | não | 0 | 3 | 3 |
| 3 | 1 | 1 | não | 0 | 4 | 4 |
| 4 | 0 | 2 | sim: remove nums[0]=0 → left=1, zeros=1 | 1 | 4 | 4 |
| 5 | 1 | 1 | não | 1 | 5 | 5 |
| 6 | 1 | 1 | não | 1 | 6 | 6 |
| 7 | 0 | 2 | sim: avança left até o zero de nums[4] sair → left=5, zeros=1 | 5 | 3 | 6 |
| 8 | 1 | 1 | não | 5 | 4 | 6 |

Melhor janela "com no máximo 1 zero": `6`. Resultado final: `6 - 1 = 5` ✔ (obrigatório deletar exatamente um elemento)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int longestSubarray(int[] nums) {
    int left = 0;
    int zeros = 0;
    int best = 0;

    for (int right = 0; right < nums.length; right++) {
        if (nums[right] == 0) {
            zeros++;
        }

        while (zeros > 1) {
            if (nums[left] == 0) {
                zeros--;
            }
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best - 1; // é obrigatório deletar exatamente um elemento, mesmo que seja um 1
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

- É preciso deletar EXATAMENTE um elemento, mesmo que o array seja todo de 1s (ex.: `[1,1,1]` → resposta `2`, não `3`) — por isso a resposta final é sempre `melhorJanela - 1`, nunca a janela bruta.
- A janela "com no máximo 1 zero" já modela a deleção: o zero "restante" na janela é justamente o que será deletado; se a janela não tem zero nenhum, ainda assim um elemento precisa ser removido, e é isso que o `-1` final garante.
- Esse é o mesmo padrão de [1004] Max Consecutive Ones III com `k=1`, mas com a obrigatoriedade adicional de deletar mesmo quando não há zero para remover.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só 1s (obrigado a deletar um 1) | `[1,1,1]` | 2 | mesmo sem zero, precisa deletar exatamente um elemento |
| Um único zero | `[1,1,0,1]` | 3 | deletar o zero une os dois blocos de 1s |
| Só zeros | `[0,0]` | 0 | depois de deletar um zero, sobra só outro zero (nenhum 1) |
| Exemplo maior do enunciado | `[0,1,1,1,0,1,1,0,1]` | 5 | melhor resultado deletando o zero da posição 4 |

## 🔗 Conexões

- Problemas irmãos: [1004] Max Consecutive Ones III (mesmíssima técnica, mas permitindo `k` flips em vez de uma deleção obrigatória), [2760] Longest Even Odd Subarray With Threshold (mesma família de janela variável com uma condição de contagem)
- No backend: calcular a maior sequência de operações bem-sucedidas tolerando exatamente uma falha obrigatoriamente descartada do lote, útil em métricas de "quase perfeição" de pipelines.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
