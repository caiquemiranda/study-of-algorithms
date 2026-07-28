# [1754] Largest Merge of Two Strings

> 🔗 [LeetCode 1754](https://leetcode.com/problems/largest-merge-of-two-strings/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Greedy` `#Medium`

## 📜 O Problema

Dadas `word1` e `word2`, construa `merge` escolhendo repetidamente: tirar o primeiro caractere de `word1` (se não vazia) OU de `word2` (se não vazia) e anexá-lo a `merge`. Retorne o `merge` lexicograficamente **maior** possível.

**Exemplos:**
```
Input:  word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"

Input:  word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"
```

**Restrições (e o que elas denunciam):**
- `1 <= word1.length, word2.length <= 3000` → uma solução O(n×m) (ex.: comparar sufixos a cada passo) ainda cabe (~9×10^6), mesmo sem ser O(n+m) puro
- Só letras minúsculas → sem normalização de case
- "Lexicograficamente maior" depende de olhar além do primeiro caractere em caso de empate → sinaliza que comparar só `word1[i]` com `word2[j]` isoladamente não basta

## 🧭 Como reconhecer o padrão

"Escolher, a cada passo, de qual das duas fontes tirar o próximo elemento pra maximizar o resultado" é dois ponteiros consumindo `word1` e `word2` simultaneamente — a diferença para um merge comum é que a decisão de qual ponteiro avançar depende de comparar o **restante** de cada string, não só o caractere na posição atual (empates no primeiro caractere só se resolvem olhando adiante).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todas as `2^(n+m)` sequências possíveis de escolhas (tirar de `word1` ou de `word2` em cada passo) e escolher a que gera a maior string resultante.

- Tempo: O(2^(n+m)) — exponencial no tamanho combinado das strings
- **Por que não basta:** claramente inviável até para entradas pequenas. A decisão em cada passo pode ser tomada localmente, comparando os sufixos restantes de `word1` e `word2` — e um algoritmo guloso baseado nessa comparação já é comprovadamente ótimo, sem precisar explorar combinações.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `i` em `word1` e `j` em `word2`. A cada passo, compare o que **sobra** de `word1` a partir de `i` com o que sobra de `word2` a partir de `j` (comparação lexicográfica de string, não só do caractere atual). Tire o caractere da string cujo restante for maior — isso garante que, mesmo em empates no início, a escolha certa considera o que vem depois. Quando uma das strings esgotar, anexe o restante da outra diretamente (não sobra mais escolha a fazer).

## 🎬 Exemplo passo a passo

`word1 = "cabaa"`, `word2 = "bcaaa"`

| Passo | word1 restante | word2 restante | Comparação | Escolha | merge parcial |
|---|---|---|---|---|---|
| 1 | `cabaa` | `bcaaa` | `'c' > 'b'` | word1: `'c'` | `"c"` |
| 2 | `abaa` | `bcaaa` | `'a' < 'b'` | word2: `'b'` | `"cb"` |
| 3 | `abaa` | `caaa` | `'a' < 'c'` | word2: `'c'` | `"cbc"` |
| 4 | `abaa` | `aaa` | `'a'=='a'`, depois `'b'>'a'` | word1: `'a'` | `"cbca"` |
| 5 | `baa` | `aaa` | `'b' > 'a'` | word1: `'b'` | `"cbcab"` |
| 6 | `aa` | `aaa` | `"aa"` é prefixo de `"aaa"` (menor) | word2: `'a'` | `"cbcaba"` |
| 7 | `aa` | `aa` | iguais (empate) → prefere word1 | word1: `'a'` | `"cbcabaa"` |
| 8 | `a` | `aa` | `"a"` é prefixo de `"aa"` (menor) | word2: `'a'` | `"cbcabaaa"` |
| 9 | `a` | `a` | iguais (empate) → prefere word1 | word1: `'a'` (esgota) | `"cbcabaaaa"` |

`word1` esgotado → anexa o resto de `word2` (`"a"`) → resultado final: `"cbcabaaaaa"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n × m) no pior caso — cada uma das até `n+m` decisões pode comparar sufixos de até `O(max(n,m))` caracteres
- **Espaço:** O(n + m) para o `merge` resultante

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String largestMerge(String word1, String word2) {
    StringBuilder merge = new StringBuilder();
    int i = 0;
    int j = 0;

    while (i < word1.length() && j < word2.length()) {
        // compara os SUFIXOS restantes, não só o caractere atual (evita decidir errado em empates)
        if (word1.substring(i).compareTo(word2.substring(j)) > 0) {
            merge.append(word1.charAt(i));
            i++;
        } else {
            merge.append(word2.charAt(j));
            j++;
        }
    }
    // anexa o que sobrou de qualquer um dos dois (o outro já esgotou)
    merge.append(word1.substring(i));
    merge.append(word2.substring(j));

    return merge.toString();
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

- Comparar só o caractere ATUAL (`word1.charAt(i)` vs `word2.charAt(j)`) em vez do SUFIXO inteiro — em caso de empate no primeiro caractere, a decisão certa depende do que vem depois; ex.: `word1="cab"`, `word2="caa"` empatam em `'c'`, mas o sufixo de `word1` (`"ab"` vs `"aa"`) é maior, então `word1` deveria "vencer" ali.
- Inverter o critério de desempate (usar `<` em vez de `<=`, ou vice-versa) de forma inconsistente entre as comparações — qualquer critério de desempate funciona matematicamente por simetria, mas precisa ser aplicado sempre da mesma forma.
- Esquecer de anexar o restante de uma das strings quando a outra esgota — o loop principal só roda enquanto as DUAS têm caracteres; o que sobra da mais longa precisa ser copiado direto, sem mais comparação.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo do enunciado | `word1="cabaa"`, `word2="bcaaa"` | `"cbcabaaaaa"` | mistura de escolhas com empates de sufixo |
| Sem empates | `word1="ab"`, `word2="ba"` | `"baab"` | comparação direta decide toda vez sem ambiguidade |
| Um mais longo | `word1="a"`, `word2="aa"` | `"aaa"` | empate constante, mas comprimento decide (prefixo é "menor") |
| Strings idênticas | `word1="ab"`, `word2="ab"` | `"aabb"` | empate total em cada passo, escolha consistente intercala igual |

## 🔗 Conexões

- Problemas irmãos: [1768] Merge Strings Alternately (mesma ideia de consumir duas strings com dois ponteiros, mas alternando fixo em vez de decidir greedily), [0088] Merge Sorted Array (mesma família de merge guiado por comparação a cada passo)
- No backend: mesclar dois streams de eventos escolhendo, a cada passo, a fonte que produz a sequência "mais relevante" segundo algum critério de prioridade — que pode empatar no início e precisar olhar adiante para desempatar.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
