# [1455] Check if a Word Occurs as a Prefix of Any Word in a Sentence

> 🔗 [LeetCode 1455](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma `sentence` com palavras separadas por um único espaço, e um `searchWord`, verifique se `searchWord` é **prefixo** de alguma palavra da sentença. Retorne o índice (**1-indexado**) da primeira palavra onde isso acontece, ou `-1` se nenhuma servir.

**Exemplos:**
```
Input:  sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explicação: "burg" é prefixo de "burger", a 4ª palavra.

Input:  sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explicação: "pro" é prefixo da 2ª e da 6ª palavra, mas retornamos o índice mínimo.

Input:  sentence = "i am tired", searchWord = "you"
Output: -1
```

**Restrições (e o que elas denunciam):**
- `1 <= sentence.length <= 100`, `1 <= searchWord.length <= 10` → entrada pequena, mas O(n) já é natural e suficiente
- Palavras separadas por um único espaço → simplifica a detecção de fronteira de palavra, igual a [0557] Reverse Words in a String III
- Retorna o índice **mínimo** entre as ocorrências → basta parar no primeiro match, sem precisar continuar procurando

## 🧭 Como reconhecer o padrão

"Procurar um prefixo dentro de cada palavra de uma sentença, parando no primeiro match" combina dois padrões já vistos: percorrer palavra por palavra usando um ponteiro que marca onde cada uma começa ([0557]), e comparar caractere a caractere com outro ponteiro, saindo assim que confirma o prefixo ou encontra um mismatch ([0028] Find the Index of the First Occurrence in a String).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Dividir a sentença em palavras com `split(" ")` (alocando um array com todas elas), e para cada palavra chamar `word.startsWith(searchWord)`.

- Tempo: O(n) · Espaço: O(n) — o `split` aloca um array com TODAS as palavras da sentença de uma vez
- **Por que não basta:** monta a lista completa de palavras mesmo que a resposta esteja logo na primeira; dois ponteiros processam palavra por palavra, na ordem, parando assim que encontram o match — sem pré-processar nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um ponteiro `i` marcando o início da palavra atual. Compare `searchWord` com os caracteres a partir de `i`, um a um, com um ponteiro interno `j`. Se `j` alcançar o fim de `searchWord` sem mismatch, essa palavra tem `searchWord` como prefixo — retorne o índice (1-indexado) dela. Se houver mismatch, pule para o início da próxima palavra (avance `i` até o próximo espaço, depois mais um) e tente de novo.

## 🎬 Exemplo passo a passo

`sentence = "this problem is an easy problem"`, `searchWord = "pro"`

| Passo | palavra (índice 1-based) | Comparação | Resultado |
|---|---|---|---|
| 1 | 1 (`"this"`) | `t` ≠ `p` (primeiro caractere já diverge) | não é prefixo, pula pra próxima palavra |
| 2 | 2 (`"problem"`) | `p`, `r`, `o` batem com `"pro"` (3 caracteres) | é prefixo → **retorna 2** |

Resultado final: `2` ✔ (para no primeiro match, nem chega a olhar a segunda ocorrência de `"problem"` no índice 6)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — no pior caso (sem match), cada caractere da sentença é visitado uma vez
- **Espaço:** O(1) — só os índices `i`, `j` e o contador de palavra, sem alocar nenhuma substring

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int isPrefixOfWord(String sentence, String searchWord) {
    int n = sentence.length();
    int i = 0;
    int wordIndex = 1;

    while (i < n) {
        int j = 0;
        // compara searchWord com a palavra que começa em i, caractere a caractere
        while (j < searchWord.length() && i + j < n && sentence.charAt(i + j) == searchWord.charAt(j)) {
            j++;
        }
        if (j == searchWord.length()) {
            return wordIndex; // percorreu searchWord inteiro sem mismatch: é prefixo
        }

        // pula até o fim da palavra atual (próximo espaço ou fim da sentença)
        while (i < n && sentence.charAt(i) != ' ') {
            i++;
        }
        i++; // pula o espaço, começa a próxima palavra
        wordIndex++;
    }

    return -1;
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

- Usar `split(" ")` + `startsWith` — funciona, mas aloca o array com todas as palavras de uma vez; dois ponteiros processam sob demanda, parando no primeiro match.
- Esquecer que "prefixo" não exige que a palavra termine ali — `"burg"` é prefixo de `"burger"` mesmo sem ser a palavra inteira; o critério é `j == searchWord.length()`, não `j == tamanho da palavra`.
- Retornar o índice 0-based em vez de 1-based — o enunciado pede explicitamente índice 1-indexado (a primeira palavra é a palavra 1, não a palavra 0).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Prefixo simples | `sentence="i love eating burger"`, `searchWord="burg"` | 4 | `"burg"` é prefixo de `"burger"`, a 4ª palavra |
| Múltiplas ocorrências | `sentence="this problem is an easy problem"`, `searchWord="pro"` | 2 | retorna o índice mínimo, mesmo com match repetido depois |
| Nenhum match | `sentence="i am tired"`, `searchWord="you"` | -1 | nenhuma palavra começa com `"you"` |
| searchWord igual à palavra inteira | `sentence="i am tired"`, `searchWord="am"` | 2 | prefixo pode ser a palavra inteira, não só um pedaço dela |

## 🔗 Conexões

- Problemas irmãos: [0028] Find the Index of the First Occurrence in a String (mesma técnica de comparação caractere a caractere com dois ponteiros), [0557] Reverse Words in a String III (mesma forma de percorrer palavras delimitadas por espaço com um ponteiro de início/fim)
- No backend: autocompletar ou roteamento por prefixo — por exemplo, encontrar a primeira rota registrada cujo caminho começa com o prefixo requisitado, processando os candidatos em ordem sem pré-carregar todos numa estrutura auxiliar.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
