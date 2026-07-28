# [1839] Longest Substring Of All Vowels in Order

> 🔗 [LeetCode 1839](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Uma string é considerada **beautiful** se: cada uma das 5 vogais (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) aparece pelo menos uma vez; e as letras estão em ordem alfabética não-decrescente (todos os `'a'` antes dos `'e'`, todos os `'e'` antes dos `'i'`, etc.). Dada uma string `word` de vogais, retorne o comprimento da maior substring beautiful. Se não existir nenhuma, retorne `0`.

**Exemplos:**
```
Input:  word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explicação: a maior substring beautiful é "aaaaeiiiiouuu".

Input:  word = "aeeeiiiioooauuuaeiou"
Output: 5
Explicação: a maior substring beautiful é "aeiou".

Input:  word = "a"
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= word.length <= 5 * 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `word` consiste só em vogais → simplifica: nunca há consoantes a filtrar, só ordem e presença a verificar

## 🧭 Como reconhecer o padrão

"Maior substring onde uma sequência de caracteres precisa aparecer em ordem, todos presentes" é resolvido acompanhando um **run** que se estende enquanto a ordem se mantém (`word[i] >= word[i-1]`) e reseta quando quebra — dentro de cada run, um conjunto de vogais vistas rastreia se as 5 já apareceram.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, checar se a substring tem as 5 vogais e está em ordem.

- Tempo: O(n²) ou O(n³) · Espaço: O(1)
- **Por que não basta:** revalida ordem e presença do zero a cada substring candidata, mesmo quando ela é apenas a anterior estendida em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `word` mantendo o índice de início do run atual (`start`) e um conjunto de vogais vistas nele. Quando `word[i] < word[i-1]`, a ordem quebrou: reinicie `start = i` e limpe o conjunto. Adicione `word[i]` ao conjunto; quando o conjunto tiver as 5 vogais, o comprimento `i - start + 1` é um candidato válido.

## 🎬 Exemplo passo a passo

`word = "aeeeiiiioooauuuaeiou"` (índices: ...a11,u12,u13,u14,a15,e16,i17,o18,u19)

| Evento | start do run atual | Conjunto de vogais no run | Comprimento válido? |
|---|---|---|---|
| i=0..10: run "aeeeiiiiooo" | 0 | {a,e,i,o} (nunca chega a 5, falta 'u') | não (falta u) |
| i=11: 'a' < 'o' → reset | 11 | {a} | — |
| i=12..14: run "auuu" | 11 | {a,u} (falta e,i,o) | não |
| i=15: 'a' < 'u' → reset | 15 | {a} | — |
| i=16..19: run "aeiou" | 15 | {a,e,i,o,u} → 5 vogais! | sim, comprimento 19-15+1=5 |

Resultado final: `5` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1) — set de no máximo 5 vogais

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int longestBeautifulSubstring(String word) {
    int start = 0;
    int best = 0;
    Set<Character> seen = new HashSet<>();

    for (int i = 0; i < word.length(); i++) {
        if (i > 0 && word.charAt(i) < word.charAt(i - 1)) {
            start = i; // ordem quebrou, reinicia o run aqui
            seen.clear();
        }
        seen.add(word.charAt(i));

        if (seen.size() == 5) {
            best = Math.max(best, i - start + 1);
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

- "Ordem alfabética" aqui significa NÃO-decrescente (`'a' <= 'a'` é permitido, repetir a mesma vogal não quebra o run) — só uma vogal "voltando" para uma anterior (`word[i] < word[i-1]`) reinicia o run.
- Ter as 5 vogais presentes NÃO basta sozinho — elas precisam estar na ordem certa dentro do MESMO run; por isso o reset do `start` e do `seen` acontece ANTES de adicionar o caractere atual ao conjunto.
- `word` consiste só em vogais (garantido pelas restrições) — não é preciso checar se um caractere é consoante.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem nenhuma substring bonita | `"a"` | 0 | um único caractere nunca tem as 5 vogais |
| Caso mínimo exato | `"aeiou"` | 5 | a string inteira já é bonita |
| Ordem quebrada, todas presentes mas fora de ordem | `"uaeio"` | 0 | nenhum trecho contíguo mantém a ordem com as 5 vogais |
| Exemplo do enunciado | `"aeeeiiiioooauuuaeiou"` | 5 | o run final "aeiou" é o único que reúne as 5 vogais em ordem |

## 🔗 Conexões

- Problemas irmãos: [1248] Count Number of Nice Subarrays (mesma família de raciocinar sobre runs que resetam quando uma condição quebra), [3090] Maximum Length Substring With Two Occurrences (mesma técnica-base de manter um conjunto de caracteres vistos numa janela)
- No backend: validar se uma sequência de estados de um pipeline (created→processing→shipped→delivered) aparece na ordem correta dentro de um trecho de log, sem retrocessos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
