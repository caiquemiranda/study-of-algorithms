# [0290] Word Pattern

> 🔗 [LeetCode 290](https://leetcode.com/problems/word-pattern/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Dado um `pattern` (letras) e uma string `s` (palavras separadas por espaço), determine se `s` **segue** o mesmo padrão: deve existir uma **bijeção** entre cada letra do pattern e cada palavra de `s` — cada letra mapeia para exatamente uma palavra, e cada palavra mapeia para exatamente uma letra.

**Exemplos:**
```
Input:  pattern = "abba", s = "dog cat cat dog"   Output: true  ('a'->dog, 'b'->cat)
Input:  pattern = "abba", s = "dog cat cat fish"  Output: false (a última palavra quebra o padrão)
Input:  pattern = "aaaa", s = "dog cat cat dog"   Output: false ('a' mapearia para 2 palavras diferentes)
```

**Restrições (e o que elas denunciam):**
- `1 <= pattern.length <= 300` e `1 <= s.length <= 3000` → tamanhos pequenos, qualquer solução O(n) ou até O(n²) passaria — o desafio é a **corretude da bijeção**, não a performance
- "palavras separadas por um único espaço, sem espaços extras" → você pode confiar no `split(" ")` sem se preocupar com strings vazias
- Se o **número de palavras** em `s` for diferente do **tamanho do pattern**, já é impossível bater — verificação óbvia mas fácil de esquecer

## 🧭 Como reconhecer o padrão

É a mesma estrutura de **[0205] Isomorphic Strings**, só que mapeando **caractere → palavra** em vez de caractere → caractere. Sempre que o enunciado usa a palavra "bijeção" (ou descreve as duas regras "cada X mapeia pra um Y" e "cada Y mapeia pra um X"), são necessários **dois mapas**, um em cada direção.

## 🐢 Solução 1 — Força bruta

Para cada letra distinta do pattern, coletar todas as posições onde ela aparece e verificar, com um laço aninhado, se a palavra correspondente em `s` é sempre a mesma nessas posições — repetir a checagem simétrica para cada palavra distinta de `s`.

- Tempo: O(n²) no pior caso (revisitar posições repetidamente) · Espaço: O(n)
- **Por que não é a ideal:** o mesmo resultado sai em uma única passada com dois hash maps — não há motivo para reprocessar posições já vistas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, quebre `s` em palavras. Se a quantidade de palavras não bater com o tamanho do pattern, já é `false`. Depois, percorra os dois em paralelo com **dois mapas** (`letra -> palavra` e `palavra -> letra`), igual ao problema de Isomorphic Strings — cada consulta confirma que a correspondência é consistente nas duas direções.

## 🎬 Exemplo passo a passo

`pattern = "abba"`, `s = "dog cat cat dog"` → palavras: `["dog", "cat", "cat", "dog"]` (4 palavras, pattern tem 4 letras — ok)

| i | letra | palavra | letra→palavra antes | palavra→letra antes | Verificação | Ação |
|---|---|---|---|---|---|---|
| 0 | a | dog | {} | {} | nenhum mapeado | registra a→dog, dog→a |
| 1 | b | cat | {a:dog} | {dog:a} | nenhum mapeado | registra b→cat, cat→b |
| 2 | b | cat | {a:dog,b:cat} | {dog:a,cat:b} | b→cat bate; cat→b bate | ok |
| 3 | a | dog | {a:dog,b:cat} | {dog:a,cat:b} | a→dog bate; dog→a bate | ok |

Resultado final: **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — n = tamanho do pattern, m = tamanho de `s` (dividir em palavras é O(m); a varredura com os mapas é O(n))
- **Espaço:** O(n) — os dois mapas guardam no máximo uma entrada por letra/palavra distinta

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean wordPattern(String pattern, String s) {
    String[] palavras = s.split(" ");

    // se as quantidades não batem, é IMPOSSÍVEL existir bijeção — descarta sem processar nada
    if (palavras.length != pattern.length()) {
        return false;
    }

    Map<Character, String> letraParaPalavra = new HashMap<>();
    Map<String, Character> palavraParaLetra = new HashMap<>();

    for (int i = 0; i < pattern.length(); i++) {
        char letra = pattern.charAt(i);
        String palavra = palavras[i];

        // checa a direção letra -> palavra
        if (letraParaPalavra.containsKey(letra) && !letraParaPalavra.get(letra).equals(palavra)) {
            return false;
        }
        // checa a direção palavra -> letra (SEM ISSO, duas letras poderiam mapear pra mesma palavra)
        if (palavraParaLetra.containsKey(palavra) && palavraParaLetra.get(palavra) != letra) {
            return false;
        }

        letraParaPalavra.put(letra, palavra);
        palavraParaLetra.put(palavra, letra);
    }
    return true;
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

- Esquecer de comparar `palavras.length != pattern.length()` antes de tudo — sem isso, o loop pode acessar índice fora do array de palavras.
- **Java**: comparar `String` com `!=` (referência) em vez de `.equals()` (valor) — `letraParaPalavra.get(letra) != palavra` daria resultado errado na maioria das vezes; strings vindas de `split()` não são interned.
- Usar **só um mapa** (letra→palavra) — passa em `"abba"`/`"dog cat cat dog"` mas falha em detectar duas letras diferentes mapeando para a mesma palavra (ex.: `pattern="ab"`, `s="dog dog"` deveria ser `false`).
- Assumir que `s` pode ter espaços extras — o enunciado garante palavras separadas por espaço único, sem espaços nas pontas.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Bijeção válida | `pattern="abba", s="dog cat cat dog"` | true | caso do enunciado |
| Quantidades diferentes | `pattern="abc", s="dog cat"` | false | pega no primeiro check |
| Duas letras, uma palavra (só 1 mapa não pegaria) | `pattern="ab", s="dog dog"` | false | testa a direção palavra→letra |
| Uma letra, várias palavras | `pattern="aaa", s="dog dog cat"` | false | 'a' mapearia para 2 palavras diferentes |

## 🔗 Conexões

- Problemas irmãos: **[0205] Isomorphic Strings** (o mesmo problema, mas caractere↔caractere em vez de caractere↔palavra), **[0291] Word Pattern II** (variante hard sem espaços separando as palavras — exige backtracking)
- No backend: validação de esquemas de nomenclatura (ex.: garantir que cada tipo de evento sempre usa o mesmo template de log) e verificação de contratos de API onde cada campo deve mapear para exatamente um tipo usam esta mesma checagem de bijeção.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
