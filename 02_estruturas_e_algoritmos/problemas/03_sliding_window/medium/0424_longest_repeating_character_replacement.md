# [0424] Longest Repeating Character Replacement

> 🔗 [LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dada uma string `s` e um inteiro `k`, você pode escolher qualquer caractere da string e trocá-lo por qualquer outra letra maiúscula do alfabeto inglês, no máximo `k` vezes. Retorne o comprimento da maior substring contendo a mesma letra que você consegue obter depois dessas operações.

**Exemplos:**
```
Input:  s = "ABAB", k = 2
Output: 4
Explicação: troque os dois 'A's por 'B' (ou vice-versa).

Input:  s = "AABABBA", k = 1
Output: 4
Explicação: troque o 'A' do meio por 'B', formando "AABBBBA". A substring "BBBB" tem comprimento 4.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `s` consiste só em letras maiúsculas → no máximo 26 caracteres distintos, cabendo num array de contagem fixo
- `0 <= k <= s.length` → `k` pode cobrir a string inteira, permitindo transformá-la toda numa única letra

## 🧭 Como reconhecer o padrão

"Maior substring de um único caractere repetido, permitindo até `k` trocas" é resolvido com janela deslizante variável: uma janela é válida quando `tamanho_da_janela - frequência_do_caractere_mais_comum <= k` (o número de trocas necessárias para uniformizar a janela). Expande-se pela direita; quando inválida, encolhe pela esquerda.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, contar a frequência de cada letra na janela e checar se `tamanho - maxFreq <= k`.

- Tempo: O(n² · 26) · Espaço: O(26) por janela
- **Por que não basta:** revalida a contagem de frequências do zero a cada substring candidata, mesmo quando ela é apenas a anterior estendida em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um array de frequência de 26 posições e o maior valor de frequência já visto (`maxFreq`) enquanto a janela se expande. Se `tamanho_da_janela - maxFreq > k`, encolha pela esquerda. Note que `maxFreq` NUNCA é recalculado para baixo ao encolher — isso é seguro porque o objetivo é apenas encontrar o maior comprimento de janela válido, e uma janela do mesmo tamanho já foi vista como candidata.

## 🎬 Exemplo passo a passo

`s = "AABABBA"`, `k = 1`

| right | char | freq[char] | maxFreq | tamanho-maxFreq | ação | left final | comprimento | melhor |
|---|---|---|---|---|---|---|---|---|
| 0 | A | 1 | 1 | 0 | ok | 0 | 1 | 1 |
| 1 | A | 2 | 2 | 0 | ok | 0 | 2 | 2 |
| 2 | B | 1 | 2 | 1 | ok | 0 | 3 | 3 |
| 3 | A | 3 | 3 | 1 | ok | 0 | 4 | 4 |
| 4 | B | 2 | 3 | 2 | encolhe | 1 | 4 | 4 |
| 5 | B | 3 | 3 | 2 | encolhe | 2 | 4 | 4 |
| 6 | A | 2 | 3 | 2 | encolhe | 3 | 4 | 4 |

Resultado final: `4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada índice entra e sai da janela no máximo uma vez
- **Espaço:** O(26) = O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int characterReplacement(String s, int k) {
    int[] freq = new int[26];
    int left = 0;
    int maxFreq = 0;
    int best = 0;

    for (int right = 0; right < s.length(); right++) {
        int c = s.charAt(right) - 'A';
        freq[c]++;
        maxFreq = Math.max(maxFreq, freq[c]);

        if (right - left + 1 - maxFreq > k) {
            freq[s.charAt(left) - 'A']--;
            left++;
            // maxFreq NÃO é recalculado aqui de propósito: uma janela desse tamanho já foi vista
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

- Deixar `maxFreq` "desatualizado" (maior do que realmente é na janela atual) é intencional e seguro — o objetivo é só o MAIOR comprimento de janela válido, e o algoritmo nunca reporta um comprimento maior do que o real porque a janela só cresce quando `maxFreq` (mesmo desatualizado) ainda permite.
- Confundir "trocar até k caracteres" com "trocar exatamente k" — a condição é `tamanho - maxFreq <= k`, uma desigualdade, não igualdade.
- Usar `if` em vez de manter a lógica de encolher no máximo uma posição por passo — como o objetivo é só o maior tamanho, encolher em 1 e seguir em frente é suficiente (o tamanho da janela nunca diminui ao longo da varredura).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k cobre a string inteira | `s="ABAB"`, `k=2` | 4 | dá pra uniformizar a string toda |
| k=0 (sem trocas) | `s="ABAB"`, `k=0` | 1 | sem trocas, a maior sequência já repetida tem tamanho 1 |
| Já uniforme | `s="AAAA"`, `k=2` | 4 | nenhuma troca necessária |
| Exemplo do enunciado | `s="AABABBA"`, `k=1` | 4 | troca o 'A' do meio, formando "BBBB" |

## 🔗 Conexões

- Problemas irmãos: [1004] Max Consecutive Ones III (mesmíssima técnica, mas com alfabeto binário e "trocas" implícitas por flips), [1156] Swap For Longest Repeated Character Substring (mesmo objetivo, mas limitado a UMA troca posicional específica em vez de k trocas livres)
- No backend: encontrar o maior trecho de uma sequência de status que pode ser "normalizado" para um único valor dentro de um orçamento limitado de correções, útil em reconciliação de dados com tolerância a poucas divergências.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
