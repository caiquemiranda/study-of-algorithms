# [0567] Permutation in String

> 🔗 [LeetCode 567](https://leetcode.com/problems/permutation-in-string/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dadas duas strings `s1` e `s2`, retorne `true` se `s2` contém uma permutação de `s1`, ou `false` caso contrário. Em outras palavras, retorne `true` se alguma permutação de `s1` é substring de `s2`.

**Exemplos:**
```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true
Explicação: s2 contém uma permutação de s1 ("ba").

Input:  s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= s1.length, s2.length <= 10^4` → O(n·m log m) ordenando cada janela é arriscado; O(n) é o esperado
- `s1` e `s2` consistem só em letras minúsculas → no máximo 26 caracteres distintos, cabendo num array de contagem fixo

## 🧭 Como reconhecer o padrão

"Existe uma janela de tamanho **fixo** em `s2` com a mesma composição de caracteres que `s1`" é janela deslizante de tamanho fixo: mantém-se um array de frequência da janela atual, atualizado incrementalmente, e compara-se com o array de frequência de `s1` a cada passo — assim que baterem, encontrou-se uma permutação.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, extrair `s2.substring(i, i+m)` (onde `m = s1.length()`) e checar se é permutação de `s1` ordenando ambas e comparando.

- Tempo: O(n · m log m) · Espaço: O(m) por comparação
- **Por que não basta:** ordena uma substring nova a cada janela, quando um array de frequência atualizado incrementalmente evita todo esse trabalho repetido.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa o array de frequência de `s1` (`needed`). Deslize uma janela de tamanho `m` sobre `s2`, mantendo seu próprio array de frequência (`window`). "Permutação" significa mesma composição de caracteres, independente da ordem — assim que `window` igualar `needed`, retorna `true` imediatamente.

## 🎬 Exemplo passo a passo

`s1 = "ab"`, `s2 = "eidbaooo"` (m=2, needed: a1,b1)

| i | char entra | char sai | janela relevante (letras não-zero) | Permutação de s1? |
|---|---|---|---|---|
| 0 | e | — | e:1 | (janela incompleta) |
| 1 | i | — | e:1,i:1 | não |
| 2 | d | e | i:1,d:1 | não |
| 3 | b | i | d:1,b:1 | não |
| 4 | a | d | b:1,a:1 | sim |

Resultado final: `true` ✔ (janela "ba", índices 3-4)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(26n) = O(n)
- **Espaço:** O(26) = O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean checkInclusion(String s1, String s2) {
    int m = s1.length();
    int n = s2.length();
    if (n < m) {
        return false;
    }

    int[] needed = new int[26];
    for (char c : s1.toCharArray()) {
        needed[c - 'a']++;
    }

    int[] window = new int[26];
    for (int i = 0; i < n; i++) {
        window[s2.charAt(i) - 'a']++;
        if (i >= m) {
            window[s2.charAt(i - m) - 'a']--;
        }
        if (i >= m - 1 && Arrays.equals(window, needed)) {
            return true;
        }
    }

    return false;
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

- "Permutação" aqui significa mesma composição de caracteres, independente da ordem — comparar arrays de frequência (não strings ordenadas) é o jeito certo e mais eficiente.
- `s2.length() < s1.length()` deve retornar `false` imediatamente — nenhuma janela do tamanho de `s1` cabe em `s2`.
- Esquecer de remover o caractere que sai da janela (`i >= m`) faz a janela crescer sem limite, comparando cada vez mais caracteres com `s1` em vez de manter tamanho fixo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| s2 menor que s1 | `s1="abc"`, `s2="ab"` | false | nenhuma janela de tamanho 3 cabe em "ab" |
| s1 igual a s2 | `s1="ab"`, `s2="ab"` | true | a única janela já é idêntica |
| Nenhuma permutação presente | `s1="ab"`, `s2="eidboaoo"` | false | nenhuma janela de tamanho 2 tem a mesma composição de "ab" |
| Exemplo do enunciado | `s1="ab"`, `s2="eidbaooo"` | true | a janela "ba" (índices 3-4) é permutação de "ab" |

## 🔗 Conexões

- Problemas irmãos: [0438] Find All Anagrams in a String (mesmíssima técnica, mas retornando TODOS os índices em vez de parar no primeiro), [0076] Minimum Window Substring (mesma família de comparar composição de caracteres numa janela)
- No backend: validar se um fluxo de bytes contém, em algum ponto, exatamente o mesmo conjunto de flags ou códigos de um padrão esperado, independente da ordem de chegada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
