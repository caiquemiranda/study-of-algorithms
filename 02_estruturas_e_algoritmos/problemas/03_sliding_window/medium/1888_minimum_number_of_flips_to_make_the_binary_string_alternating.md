# [1888] Minimum Number of Flips to Make the Binary String Alternating

> 🔗 [LeetCode 1888](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dada uma string binária `s`, você pode realizar dois tipos de operação em qualquer sequência: **tipo-1** remove o caractere do início e o anexa ao fim; **tipo-2** escolhe qualquer caractere e inverte seu valor. Retorne o número **mínimo** de operações tipo-2 necessárias para que `s` fique **alternada** (nenhum par de caracteres adjacentes iguais).

**Exemplos:**
```
Input:  s = "111000"
Output: 2
Explicação: rotacionar duas vezes e trocar 2 caracteres.

Input:  s = "010"
Output: 0

Input:  s = "1110"
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n²) força bruta simulando cada rotação é arriscado; O(n) é o esperado
- Rotações (tipo-1) são ilimitadas e "grátis" → o custo real está só nas operações tipo-2, e o número dessas independe de QUAL rotação é escolhida antes

## 🧭 Como reconhecer o padrão

Como as rotações são ilimitadas e grátis, modele-as concatenando `s` com ela mesma (`s+s`): qualquer janela de tamanho `n` dentro dessa string dobrada representa uma rotação possível de `s`. O problema vira "achar a janela de tamanho fixo `n` que exige menos flips para virar um dos dois padrões alternados possíveis (`0101...` ou `1010...`)".

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular cada uma das `n` rotações possíveis, e para cada uma, contar os flips necessários contra os dois padrões alternados, comparando caractere a caractere.

- Tempo: O(n²) · Espaço: O(n) por rotação simulada
- **Por que não basta:** recria a string rotacionada e recalcula os flips do zero para cada uma das `n` rotações, quando uma janela deslizante sobre `s+s` resolve isso incrementalmente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s+s` mantendo `diff`: quantas posições da janela atual de tamanho `n` não batem com o padrão "começa com 0" (`0101...`). Como toda posição que não bate com esse padrão bate com o padrão oposto (`1010...`), o custo do padrão oposto é sempre `n - diff` — não precisa recontar. A cada janela completa, o melhor candidato é `min(diff, n-diff)`.

## 🎬 Exemplo passo a passo

`s = "111000"` (n=6) → `s+s = "111000111000"`

| i (posição em s+s) | doubled[i] | esperado ("0101...") | diff | Se i≥n: remove efeito de doubled[i-n] | Se janela completa: melhor candidato |
|---|---|---|---|---|---|
| 0..4 | 1,1,1,0,0 | 0,1,0,1,0 | cresce até 3 | — | — |
| 5 | 0 | 1 | 4 | — | min(4, 6-4)=2 → melhor=2 |
| 6 | 1 | 0 | 5→4 (após remover doubled[0]) | remove doubled[0]='1' (era mismatch) | min(4,2)=2 → melhor continua 2 |
| ... | ... | ... | oscila entre 4 e 5 | ... | melhor permanece 2 |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — a string dobrada tem 2n caracteres, uma passada
- **Espaço:** O(n) para a string dobrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minFlips(String s) {
    int n = s.length();
    String doubled = s + s;
    int diff = 0;
    int best = Integer.MAX_VALUE;

    for (int i = 0; i < doubled.length(); i++) {
        char expected = (i % 2 == 0) ? '0' : '1';
        if (doubled.charAt(i) != expected) {
            diff++;
        }

        if (i >= n) {
            int outIndex = i - n;
            char expectedOut = (outIndex % 2 == 0) ? '0' : '1';
            if (doubled.charAt(outIndex) != expectedOut) {
                diff--;
            }
        }

        if (i >= n - 1) {
            best = Math.min(best, Math.min(diff, n - diff));
        }
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

- As rotações (tipo-1) são "grátis" e ilimitadas — modelar isso concatenando `s` com ela mesma permite testar TODAS as rotações possíveis como janelas de tamanho `n`, sem simular nenhuma rotação de verdade.
- Duas rotações alternadas existem (começando com '0' ou com '1'); como qualquer posição que não bate com um padrão bate com o outro, `n - diff` dá o custo do padrão oposto sem recontar nada.
- `diff` é atualizado de forma incremental (soma o que entra, subtrai o que sai), evitando recontar as `n` posições da janela do zero a cada deslizamento.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já alternada | `"010"` | 0 | nenhuma operação necessária |
| Uma única troca resolve | `"1110"` | 1 | rotacionar e trocar 1 caractere já alterna |
| String de tamanho ímpar | `"111"` | 1 | melhor rotação ainda precisa de 1 flip |
| Exemplo do enunciado | `"111000"` | 2 | melhor combinação de rotação + flips custa 2 |

## 🔗 Conexões

- Problemas irmãos: [1234] Replace the Substring for Balanced String (mesma família de janela deslizante sobre uma condição de composição, embora sem a rotação), [0424] Longest Repeating Character Replacement (mesma técnica-base de comparar contra um padrão-alvo dentro de uma janela)
- No backend: calcular o menor custo de correção de uma sequência cíclica (um buffer circular de estados) para satisfazer uma regra de alternância, considerando que o ponto de início do ciclo pode ser redefinido livremente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
