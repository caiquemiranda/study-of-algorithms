# [1408] String Matching in an Array

> 🔗 [LeetCode 1408](https://leetcode.com/problems/string-matching-in-an-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#String` `#StringMatching` `#Easy`

## 📜 O Problema

Dado um array de strings `words`, retorne todas as strings em `words` que são substring de outra palavra. Você pode retornar a resposta em qualquer ordem.

**Exemplos:**
```
Input:  words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explicação: "as" é substring de "mass" e "hero" é substring de "superhero".
["hero","as"] também é uma resposta válida.

Input:  words = ["leetcode","et","code"]
Output: ["et","code"]
Explicação: "et" e "code" são substrings de "leetcode".

Input:  words = ["blue","green","bu"]
Output: []
Explicação: nenhuma string de words é substring de outra.
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 100`, `1 <= words[i].length <= 30` → pequeno, O(n² × L) resolve com folga
- strings únicas em `words` → não precisa se preocupar com duplicatas exatas (mas uma palavra pode ainda ser substring de outra diferente)

## 🧭 Como reconhecer o padrão

"Encontre todas as strings que são substring de OUTRA string na mesma coleção" é resolvido comparando cada palavra contra todas as outras (excluindo ela mesma), usando um método de busca de substring pronto da linguagem.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra `words[i]`, comparar contra todas as outras palavras `words[j]` (`j != i`), verificando se `words[i]` é substring de `words[j]` — na prática, já é essencialmente a única abordagem razoável para este tamanho de entrada.

- Tempo: O(n² × L) — n² pares, cada checagem de substring custa O(L) (comprimento médio das palavras) · Espaço: O(1) extra
- **Por que vale nomear mesmo assim:** com n ≤ 100 e L ≤ 30, o pior caso é 100×100×30 = 300.000 operações — plenamente aceitável; não há necessidade de uma estrutura mais sofisticada (como um Trie) para este tamanho de entrada.

## 💡 Solução 2 — A ideia otimizada (mesma ideia, evitando comparações redundantes)

Para cada palavra `words[i]`, percorra as outras palavras `words[j]` (`j != i`); assim que encontrar QUALQUER `words[j]` que contenha `words[i]` como substring, adicione `words[i]` ao resultado e pare de procurar para essa palavra.

## 🎬 Exemplo passo a passo

`words = ["mass","as","hero","superhero"]`

| Passo | palavra (i) | comparando com | é substring? | Ação |
|---|---|---|---|---|
| 1 | mass | as, hero, superhero | não é substring de nenhuma | não adiciona |
| 2 | as | mass, hero, superhero | "as" está em "mass"? sim | adiciona "as" |
| 3 | hero | mass, as, superhero | "hero" está em "superhero"? sim | adiciona "hero" |
| 4 | superhero | mass, as, hero | não é substring de nenhuma (é a maior) | não adiciona |

Resultado final: `["as","hero"]` ✔ (ordem pode variar)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n² × L)
- **Espaço:** O(1) extra (fora o resultado)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<String> stringMatching(String[] words) {
    List<String> resultado = new ArrayList<>();

    for (int i = 0; i < words.length; i++) {
        for (int j = 0; j < words.length; j++) {
            if (i != j && words[j].contains(words[i])) {
                resultado.add(words[i]); // achou words[i] dentro de outra palavra, já basta
                break; // não precisa continuar procurando para esta palavra
            }
        }
    }
    return resultado;
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

- Esquecer de pular a comparação de uma palavra com ela mesma (`i != j`) — toda string é trivialmente substring de si mesma, o que faria TODAS as palavras entrarem no resultado incorretamente.
- Não usar `break` ao encontrar a primeira correspondência — sem ele, a mesma palavra poderia ser adicionada múltiplas vezes ao resultado se fosse substring de mais de uma outra palavra.
- Achar que precisa comparar tamanhos antes de checar substring — não precisa; `contains()` já lida corretamente com o caso em que `words[i]` é maior que `words[j]` (simplesmente retorna `false`).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Duas substrings encontradas | `["mass","as","hero","superhero"]` | ["as","hero"] | caso padrão do enunciado |
| Substrings encadeadas | `["leetcode","et","code"]` | ["et","code"] | ambas são substrings de "leetcode" |
| Nenhuma é substring de outra | `["blue","green","bu"]` | [] | "bu" não é substring de "blue" (ordem das letras não bate) |
| Palavras de tamanhos crescentes | `["a","ab","abc"]` | ["a","ab"] | cada uma é substring da próxima maior |

## 🔗 Conexões

- Problemas irmãos: [0459] Repeated Substring Pattern (mesma operação básica de busca de substring), [0028] Find the Index of the First Occurrence in a String (mesma operação fundamental usada internamente)
- No backend: deduplicação de tags ou palavras-chave onde uma é redundante por já estar contida em outra mais específica (ex.: filtrar "java" quando "javascript" já está na lista, dependendo da regra de negócio).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
