# [0438] Find All Anagrams in a String

> 🔗 [LeetCode 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dadas duas strings `s` e `p`, retorne um array com todos os índices iniciais dos anagramas de `p` em `s`. A resposta pode ser retornada em qualquer ordem.

**Exemplos:**
```
Input:  s = "cbaebabacd", p = "abc"
Output: [0,6]
Explicação: a substring no índice 0 é "cba" (anagrama de "abc"); no índice 6 é "bac" (anagrama de "abc").

Input:  s = "abab", p = "ab"
Output: [0,1,2]
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length, p.length <= 3 * 10^4` → O(n·m) comparando caractere a caractere para cada janela é arriscado; O(n) é o esperado
- `s` e `p` consistem só em letras minúsculas → no máximo 26 caracteres distintos, cabendo num array de contagem fixo

## 🧭 Como reconhecer o padrão

"Todas as posições onde uma janela de tamanho **fixo** tem a mesma composição de caracteres que um padrão" é janela deslizante de tamanho fixo: mantém-se um array de frequência da janela atual em `s`, atualizado incrementalmente, e compara-se com o array de frequência de `p` a cada passo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, extrair `s.substring(i, i+m)` e checar se é anagrama de `p` ordenando ambas as strings e comparando.

- Tempo: O(n · m log m) · Espaço: O(m) por comparação
- **Por que não basta:** ordena uma substring nova a cada janela, quando um array de frequência atualizado incrementalmente evita todo esse trabalho repetido.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa o array de frequência de `p` (`needed`). Deslize uma janela de tamanho `m = p.length()` sobre `s`, mantendo seu próprio array de frequência (`window`), incrementando o caractere que entra e decrementando o que sai. Sempre que `window` for igual a `needed`, o índice inicial da janela entra no resultado.

## 🎬 Exemplo passo a passo

`s = "cbaebabacd"`, `p = "abc"` (m=3, needed: a1,b1,c1)

| i | char entra | char sai | a | b | c | Anagrama de p? | Índice adicionado |
|---|---|---|---|---|---|---|---|
| 0 | c | — | 0 | 0 | 1 | (janela incompleta) | — |
| 1 | b | — | 0 | 1 | 1 | (janela incompleta) | — |
| 2 | a | — | 1 | 1 | 1 | sim | 0 |
| 3 | e | c | 1 | 1 | 0 | não | — |
| 4 | b | b | 1 | 1 | 0 | não | — |
| 5 | a | a | 1 | 1 | 0 | não | — |
| 6 | b | e | 1 | 2 | 0 | não | — |
| 7 | a | b | 2 | 1 | 0 | não | — |
| 8 | c | a | 1 | 1 | 1 | sim | 6 |
| 9 | d | b | 1 | 0 | 1 | não | — |

Resultado final: `[0,6]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(26n) = O(n) — comparação de arrays de 26 posições a cada passo
- **Espaço:** O(26) = O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();
    int n = s.length();
    int m = p.length();
    if (n < m) {
        return result;
    }

    int[] needed = new int[26];
    for (char c : p.toCharArray()) {
        needed[c - 'a']++;
    }

    int[] window = new int[26];
    for (int i = 0; i < n; i++) {
        window[s.charAt(i) - 'a']++;
        if (i >= m) {
            window[s.charAt(i - m) - 'a']--; // remove o caractere que saiu da janela
        }
        if (i >= m - 1 && Arrays.equals(window, needed)) {
            result.add(i - m + 1);
        }
    }

    return result;
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

- Comparar os arrays de frequência com `Arrays.equals` a cada passo é O(26) — como 26 é constante, o algoritmo continua O(n) no total; uma otimização com contador de "diferenças" reduz a constante, mas não muda a complexidade assintótica.
- Esquecer de remover o caractere que sai da janela quando `i >= m` — sem isso, a janela cresce indefinidamente em vez de manter tamanho fixo `m`.
- `s.length() < p.length()` deve retornar lista vazia imediatamente — nenhuma janela de tamanho `p.length()` cabe em `s`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| p maior que s | `s="a"`, `p="ab"` | [] | nenhuma janela de tamanho 2 cabe numa string de tamanho 1 |
| s inteiro é anagrama de p | `s="ab"`, `p="ab"` | [0] | única janela possível já é anagrama |
| Anagramas sobrepostos | `s="abab"`, `p="ab"` | [0,1,2] | toda janela de tamanho 2 é "ab" ou "ba" |
| Exemplo do enunciado | `s="cbaebabacd"`, `p="abc"` | [0,6] | duas janelas com a mesma composição de caracteres que "abc" |

## 🔗 Conexões

- Problemas irmãos: [0567] Permutation in String (mesmíssima técnica, mas retornando só `true`/`false` em vez de todos os índices), [0076] Minimum Window Substring (mesma família de comparar composição de caracteres numa janela, mas com tamanho variável em vez de fixo)
- No backend: detectar todas as ocorrências de uma "assinatura" de caracteres dentro de um fluxo de dados maior, útil em parsing de protocolos com campos de tamanho fixo mas ordem variável.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
