# [3090] Maximum Length Substring With Two Occurrences

> 🔗 [LeetCode 3090](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Easy`

## 📜 O Problema

Dada uma string `s`, retorne o comprimento **máximo** de uma substring que contém **no máximo duas ocorrências** de cada caractere.

**Exemplos:**
```
Input:  s = "bcbbbcba"
Output: 4
Explicação: a substring "bcba" (índices 4 a 7) tem comprimento 4 e no máximo 2 ocorrências de cada caractere.

Input:  s = "aaaa"
Output: 2
Explicação: a substring "aa" tem comprimento 2 e no máximo 2 ocorrências de 'a'.
```

**Restrições (e o que elas denunciam):**
- `2 <= s.length <= 100` → entrada pequena, mas o padrão de janela deslizante já resolve em O(n) mesmo para entradas maiores
- `s` consiste só em letras minúsculas → no máximo 26 caracteres distintos, cabendo num array de contagem de tamanho fixo

## 🧭 Como reconhecer o padrão

"Maior substring com no máximo `k` ocorrências de cada caractere" é a variação direta do padrão "expandir e encolher": expande-se a janela pela direita; quando um caractere excede o limite permitido (aqui, `k=2`), encolhe-se pela esquerda até a janela voltar a ser válida.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, extrair a substring e contar as ocorrências de cada caractere com um mapa, checando se todas são `<= 2`.

- Tempo: O(n³) (O(n²) substrings, O(n) para contar cada uma) · Espaço: O(26) por substring
- **Por que não basta:** revalida a contagem de caracteres do zero a cada substring candidata, mesmo quando ela difere da anterior por apenas um caractere a mais.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use dois ponteiros `left` e `right` e um array de contagem de 26 posições. Expanda `right`, incrementando a contagem do caractere incluído. Se a contagem desse caractere passar de 2, encolha `left` (decrementando as contagens dos caracteres removidos) até a janela voltar a ter no máximo 2 ocorrências de cada letra. A cada passo válido, atualize o maior comprimento visto.

## 🎬 Exemplo passo a passo

`s = "bcbbbcba"` (índices: b0 c1 b2 b3 b4 c5 b6 a7)

| right | char | freq[char] após incluir | shrinks necessários | left final | comprimento | melhor |
|---|---|---|---|---|---|---|
| 0 | b | 1 | 0 | 0 | 1 | 1 |
| 1 | c | 1 | 0 | 0 | 2 | 2 |
| 2 | b | 2 | 0 | 0 | 3 | 3 |
| 3 | b | 3 | 1 (remove s[0]=b) | 1 | 3 | 3 |
| 4 | b | 3 | 2 (remove s[1]=c, s[2]=b) | 3 | 2 | 3 |
| 5 | c | 1 | 0 | 3 | 3 | 3 |
| 6 | b | 3 | 1 (remove s[3]=b) | 4 | 3 | 3 |
| 7 | a | 1 | 0 | 4 | 4 | 4 |

Resultado final: `4` ✔ (substring `"bcba"`, índices 4 a 7)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada índice entra e sai da janela no máximo uma vez
- **Espaço:** O(26) = O(1) — array de contagem de letras minúsculas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maximumLengthSubstring(String s) {
    int[] freq = new int[26];
    int left = 0;
    int best = 0;

    for (int right = 0; right < s.length(); right++) {
        int c = s.charAt(right) - 'a';
        freq[c]++;

        while (freq[c] > 2) {
            freq[s.charAt(left) - 'a']--; // encolhe pela esquerda até a janela voltar a ser válida
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

- Encolher a janela apenas **uma vez** em vez de usar um `while` — quando o caractere que sai não é o que causou o excesso, pode ser necessário remover mais de um elemento pela esquerda até a janela voltar a ser válida.
- Resetar `left` para `right` em vez de avançar gradualmente — perde candidatos válidos que ainda poderiam formar a maior janela.
- Comparar `freq[c] > 2` (mais de duas ocorrências) — a condição permite **exatamente** 2 ocorrências; usar `>= 2` invalidaria janelas perfeitamente válidas.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Todos os caracteres iguais | `"aaaa"` | 2 | no máximo 2 ocorrências de 'a' cabem na janela |
| Sem repetição nenhuma | `"ab"` | 2 | string inteira já é válida |
| Tamanho mínimo, exatamente 2 ocorrências | `"aa"` | 2 | ainda dentro do limite permitido |
| Exemplo do enunciado | `"bcbbbcba"` | 4 | a melhor janela é "bcba" (índices 4-7) |

## 🔗 Conexões

- Problemas irmãos: [0003] Longest Substring Without Repeating Characters (mesma técnica, mas limite de 1 ocorrência em vez de 2), [0159] Longest Substring with At Most Two Distinct Characters (mesma família, mas limitando o número de caracteres DISTINTOS, não de ocorrências de cada um)
- No backend: limitar a repetição de eventos do mesmo tipo dentro de uma janela de processamento — por exemplo, aceitar no máximo 2 requisições idênticas consecutivas antes de acionar um filtro de deduplicação.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
