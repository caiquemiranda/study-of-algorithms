# [1456] Maximum Number of Vowels in a Substring of Given Length

> 🔗 [LeetCode 1456](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dada uma string `s` e um inteiro `k`, retorne o número máximo de vogais em qualquer substring de `s` com comprimento `k`. As vogais em inglês são `'a'`, `'e'`, `'i'`, `'o'`, `'u'`.

**Exemplos:**
```
Input:  s = "abciiidef", k = 3
Output: 3
Explicação: a substring "iii" contém 3 vogais.

Input:  s = "aeiou", k = 2
Output: 2

Input:  s = "leetcode", k = 3
Output: 2
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n·k) recalculando cada janela é arriscado; O(n) é o esperado
- `1 <= k <= s.length` → `k` sempre cabe dentro do tamanho da string

## 🧭 Como reconhecer o padrão

"Maior contagem de uma característica dentro de uma janela de tamanho **fixo**" é o caso mais direto de janela deslizante de tamanho fixo: mantém-se uma contagem corrente de vogais, ajustada ao deslizar.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada início `i`, contar as vogais dos `k` caracteres do zero.

- Tempo: O(n·k) · Espaço: O(1)
- **Por que não basta:** recalcula a contagem inteira a cada janela, mesmo que `k-1` dos `k` caracteres sejam os mesmos da janela anterior.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte as vogais da primeira janela. Ao deslizar, incremente a contagem se o caractere que entra é vogal, decremente se o que sai era vogal. Mantenha o maior valor visto.

## 🎬 Exemplo passo a passo

`s = "abciiidef"`, `k = 3` (índices: a0 b1 c2 i3 i4 i5 d6 e7 f8)

| Janela (índices) | Remove | Adiciona | Vogais na janela | Melhor |
|---|---|---|---|---|
| [0..2] inicial | — | — | 1 (a) | 1 |
| [1..3] | a (vogal) | i (vogal) | 1 | 1 |
| [2..4] | b (não) | i (vogal) | 2 | 2 |
| [3..5] | c (não) | i (vogal) | 3 | 3 |
| [4..6] | i (vogal) | d (não) | 2 | 3 |
| [5..7] | i (vogal) | e (vogal) | 2 | 3 |
| [6..8] | i (vogal) | f (não) | 1 | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxVowels(String s, int k) {
    Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');
    int count = 0;
    for (int i = 0; i < k; i++) {
        if (vowels.contains(s.charAt(i))) {
            count++;
        }
    }

    int best = count;
    for (int i = k; i < s.length(); i++) {
        if (vowels.contains(s.charAt(i))) {
            count++;
        }
        if (vowels.contains(s.charAt(i - k))) {
            count--;
        }
        best = Math.max(best, count);
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

- Checar se um caractere é vogal com `Set.contains` a cada passo é O(1) (conjunto de 5 elementos fixos); um array booleano de 26 posições é ainda mais rápido na prática, mas ambos são O(1) assintoticamente.
- Janela de tamanho FIXO `k` — não há encolhimento, só o deslizamento clássico de subtrair o que sai e somar o que entra.
- Confundir "conta as vogais" com "conta os caracteres distintos" — a métrica é uma contagem simples, não um conjunto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Todas vogais | `s="aeiou"`, `k=2` | 2 | qualquer janela de 2 é só vogais |
| Nenhuma vogal | `s="xyz"`, `k=2` | 0 | nenhum caractere é vogal |
| k igual ao tamanho da string | `s="leetcode"`, `k=8` | 3 | única janela possível, conta todas as vogais da string |
| Exemplo do enunciado | `s="abciiidef"`, `k=3` | 3 | a janela "iii" tem 3 vogais |

## 🔗 Conexões

- Problemas irmãos: [2379] Minimum Recolors to Get K Consecutive Black Blocks (mesma técnica de janela fixa contando uma característica binária), [1876] Substrings of Size Three with Distinct Characters (mesma família de janela fixa aplicada a strings)
- No backend: calcular a densidade máxima de um tipo de evento (ex.: erros) dentro de uma janela de tamanho fixo de um log, para detectar o pior trecho de um período monitorado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
