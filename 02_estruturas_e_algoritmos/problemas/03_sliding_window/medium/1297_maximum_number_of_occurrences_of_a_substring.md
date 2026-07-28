# [1297] Maximum Number of Occurrences of a Substring

> 🔗 [LeetCode 1297](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dada uma string `s`, retorne o número máximo de ocorrências de **qualquer** substring que satisfaça: o número de caracteres únicos deve ser `<= maxLetters`; o tamanho da substring deve estar entre `minSize` e `maxSize` (inclusive).

**Exemplos:**
```
Input:  s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explicação: "aab" ocorre 2 vezes, satisfazendo as condições (2 letras únicas, tamanho 3).

Input:  s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explicação: "aaa" ocorre 2 vezes na string (pode se sobrepor).
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n · (maxSize-minSize)) testando todos os tamanhos é arriscado; um insight reduz o trabalho a apenas O(n)
- `1 <= minSize <= maxSize <= min(26, s.length)` → os tamanhos de janela são pequenos (no máximo 26), então operações O(tamanho) por janela são baratas

## 🧭 Como reconhecer o padrão

A pista central: qualquer substring MAIOR que `minSize` nunca pode ter frequência maior que a de seu **prefixo** de tamanho `minSize` (toda ocorrência da maior implica uma ocorrência do prefixo no mesmo lugar), e se a maior satisfaz `maxLetters`, o prefixo (com o mesmo conjunto de caracteres ou menos) também satisfaz. Isso significa que a resposta ótima está sempre entre janelas de tamanho **fixo** `minSize` — dispensando completamente `maxSize`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada tamanho de `minSize` a `maxSize`, para cada janela desse tamanho, checar `maxLetters` e contar ocorrências num mapa.

- Tempo: O(n · (maxSize-minSize)) · Espaço: O(n)
- **Por que não basta:** testa todos os tamanhos de janela quando o argumento de dominância já garante que o tamanho `minSize` nunca é superado por um tamanho maior.

## 💡 Solução 2 — A ideia otimizada (intuição)

Deslize só janelas de tamanho `minSize`. Para cada uma, conte os caracteres distintos; se `<= maxLetters`, registre-a num `HashMap<String,Integer>` de contagem. A resposta é a maior contagem no mapa ao final.

## 🎬 Exemplo passo a passo

`s = "aababcaab"`, `maxLetters = 2`, `minSize = 3` (índices: a0 a1 b2 a3 b4 c5 a6 a7 b8)

| i (início) | Janela (tam minSize=3) | Caracteres distintos | ≤ maxLetters(2)? | Freq após contar |
|---|---|---|---|---|
| 0 | "aab" | 2 | sim | aab:1 |
| 1 | "aba" | 2 | sim | aba:1 |
| 2 | "bab" | 2 | sim | bab:1 |
| 3 | "abc" | 3 | não | (ignorado) |
| 4 | "bca" | 3 | não | (ignorado) |
| 5 | "caa" | 2 | sim | caa:1 |
| 6 | "aab" | 2 | sim | aab:2 |

Resultado final (maior frequência no mapa): `2` ✔ ("aab")

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `n-minSize+1` janelas, cada checagem O(minSize) (no máximo 26)
- **Espaço:** O(n) para o mapa

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
    Map<String, Integer> freq = new HashMap<>();
    int best = 0;

    for (int i = 0; i + minSize <= s.length(); i++) {
        String window = s.substring(i, i + minSize);
        if (distinctChars(window) <= maxLetters) {
            int count = freq.merge(window, 1, Integer::sum);
            best = Math.max(best, count);
        }
    }

    return best;
}

private int distinctChars(String window) {
    Set<Character> chars = new HashSet<>();
    for (char c : window.toCharArray()) {
        chars.add(c);
    }
    return chars.size();
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

- A ideia central é que só é preciso testar janelas de tamanho `minSize` — `maxSize` nunca precisa ser usado na solução ótima, dado o argumento de dominância.
- Usar `String` como chave do `HashMap` funciona bem aqui porque `minSize <= 26` (garantido pelas restrições), mantendo o custo de hash da chave pequeno.
- Confundir "caracteres únicos" com "tamanho da substring" — são duas condições independentes que precisam ser checadas separadamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| minSize igual a maxSize | `s="aaaa"`, `maxLetters=1`, `minSize=3`, `maxSize=3` | 2 | "aaa" ocorre 2 vezes, sobrepondo |
| Nenhuma janela satisfaz maxLetters | `s="abcabc"`, `maxLetters=1`, `minSize=2`, `maxSize=2` | 0 | toda janela de 2 chars tem 2 letras distintas |
| Só uma ocorrência possível | `s="abc"`, `maxLetters=3`, `minSize=3`, `maxSize=3` | 1 | única janela do tamanho pedido |
| Exemplo do enunciado | `s="aababcaab"`, `maxLetters=2`, `minSize=3`, `maxSize=4` | 2 | "aab" ocorre 2 vezes e satisfaz o limite de letras |

## 🔗 Conexões

- Problemas irmãos: [0438] Find All Anagrams in a String (mesma técnica de janela fixa com HashMap de contagem, aqui contando substrings inteiras em vez de comparar frequências de caracteres), [0003] Longest Substring Without Repeating Characters (mesma família de limitar caracteres distintos numa janela)
- No backend: identificar o padrão de texto mais frequente dentro de um limite de "vocabulário" (poucos caracteres distintos), útil em compressão ou detecção de repetição em logs.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
