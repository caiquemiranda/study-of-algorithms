# [0884] Uncommon Words from Two Sentences

> 🔗 [LeetCode 884](https://leetcode.com/problems/uncommon-words-from-two-sentences/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Counting` `#Easy`

## 📜 O Problema

Uma **sentença** é uma string de palavras separadas por um único espaço, onde cada palavra consiste só de letras minúsculas. Uma palavra é **incomum** se aparece exatamente uma vez em uma das sentenças, e **não aparece** na outra.

Dadas duas sentenças `s1` e `s2`, retorne uma lista com todas as palavras incomuns, em qualquer ordem.

**Exemplos:**
```
Input:  s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Explicação: "sweet" só aparece em s1, "sour" só aparece em s2.

Input:  s1 = "apple apple", s2 = "banana"
Output: ["banana"]
```

**Restrições (e o que elas denunciam):**
- `1 <= s1.length, s2.length <= 200` → pequeno, O(n) resolve com folga
- palavras separadas por um único espaço, sem espaços nas bordas → tokenização simples
- "incomum" = aparece exatamente 1 vez NO TOTAL entre as duas frases combinadas

## 🧭 Como reconhecer o padrão

"Conte a frequência combinada de algo em duas fontes, e filtre pelos que aparecem exatamente uma vez no total" é resolvido combinando as duas fontes num único hash map de contagem — a origem (qual frase) não importa depois de combinado, só a contagem total.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra de `s1`, contar quantas vezes ela aparece em `s1` e em `s2` percorrendo as duas frases inteiras de novo; repetir para `s2`.

- Tempo: O(n²) — recontagem repetida da mesma palavra a cada nova palavra processada · Espaço: O(n)
- **Por que não basta:** repete a mesma contagem várias vezes para palavras duplicadas, quando um hash map de frequência calcula tudo em uma única passada por todas as palavras.

## 💡 Solução 2 — A ideia otimizada (intuição)

Tokenize `s1` e `s2` e combine todas as palavras (via `s1 + " " + s2` antes de tokenizar). Conte a frequência de cada palavra num hash map. No final, retorne as palavras cuja contagem total é exatamente 1.

## 🎬 Exemplo passo a passo

`s1 = "this apple is sweet"`, `s2 = "this apple is sour"` — palavras combinadas: this, apple, is, sweet, this, apple, is, sour

| Passo | palavra | frequencia[palavra] |
|---|---|---|
| 1 | this | this:1 |
| 2 | apple | apple:1 |
| 3 | is | is:1 |
| 4 | sweet | sweet:1 |
| 5 | this | this:2 |
| 6 | apple | apple:2 |
| 7 | is | is:2 |
| 8 | sour | sour:1 |

Palavras com frequência exatamente 1: `sweet` e `sour` → resultado `["sweet","sour"]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — n = len(s1), m = len(s2)
- **Espaço:** O(n + m) — para o hash map

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String[] uncommonFromSentences(String s1, String s2) {
    Map<String, Integer> frequencia = new HashMap<>();
    for (String palavra : (s1 + " " + s2).split(" ")) {
        frequencia.merge(palavra, 1, Integer::sum); // conta a ocorrência combinada das duas frases
    }

    List<String> resultado = new ArrayList<>();
    for (Map.Entry<String, Integer> entry : frequencia.entrySet()) {
        if (entry.getValue() == 1) {
            resultado.add(entry.getKey()); // aparece exatamente 1 vez no total -> é incomum
        }
    }
    return resultado.toArray(new String[0]);
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

- Contar `s1` e `s2` em mapas separados e depois tentar cruzar manualmente ("está só em um E tem frequência 1 nele") — funciona, mas é mais lógica do que precisa; combinar num único mapa e filtrar por contagem total `== 1` já captura exatamente a definição do enunciado.
- Esquecer que uma palavra que aparece 2 vezes na MESMA frase (ex.: "apple apple") também não é incomum — a contagem combinada dela já será ≥ 2, então o filtro `== 1` trata isso corretamente sem lógica extra.
- Concatenar `s1 + " " + s2` sem cuidado — funciona bem aqui porque nem `s1` nem `s2` têm espaços nas bordas (garantido pela restrição).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Uma palavra exclusiva em cada frase | `s1="this apple is sweet", s2="this apple is sour"` | ["sweet","sour"] (ordem qualquer) | caso padrão do enunciado |
| Palavra repetida na mesma frase | `s1="apple apple", s2="banana"` | ["banana"] | "apple" tem frequência 2, não é incomum |
| Frases idênticas | `s1="a b c", s2="a b c"` | [] | toda palavra aparece 2 vezes no total |
| Sem sobreposição nenhuma | `s1="a", s2="b"` | ["a","b"] | ambas aparecem só uma vez no total |

## 🔗 Conexões

- Problemas irmãos: [0349] Intersection of Two Arrays (operação "oposta": achar o que é comum, não o incomum), [0387] First Unique Character in a String (mesma ideia de "frequência exatamente 1" aplicada a caracteres em vez de palavras)
- No backend: comparação de dois conjuntos de dados (ex.: tags exclusivas de dois documentos, ou parâmetros que aparecem em só uma de duas versões de uma configuração) — o padrão de "combinar e contar" é a base de diffs simples baseados em frequência.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
