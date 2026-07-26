# [1002] Find Common Characters

> 🔗 [LeetCode 1002](https://leetcode.com/problems/find-common-characters/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#String` `#Easy`

## 📜 O Problema

Dado um array de strings `words`, retorne **um array com todos os caracteres que aparecem em todas as strings de `words`** (incluindo duplicatas). Você pode retornar a resposta em qualquer ordem.

**Exemplos:**
```
Input:  words = ["bella","label","roller"]
Output: ["e","l","l"]

Input:  words = ["cool","lock","cook"]
Output: ["c","o"]
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 100`, `1 <= words[i].length <= 100` → pequeno, O(n×26) ou O(n×L) resolve com folga
- "incluindo duplicatas" → precisa manter a contagem MÍNIMA de cada letra entre todas as palavras, não só presença/ausência
- letras minúsculas apenas → array fixo de 26 posições

## 🧭 Como reconhecer o padrão

"Caracteres que aparecem em TODAS as strings, respeitando quantidade" é resolvido mantendo um array de contagem "mínimo" — comece com a contagem da primeira palavra, e para cada palavra seguinte, atualize cada posição para o MENOR valor entre o que já tinha e a contagem dessa nova palavra (interseção de multiconjuntos).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada caractere possível (a-z), contar quantas vezes ele aparece em CADA palavra individualmente (percorrendo a palavra inteira a cada checagem), e pegar o mínimo entre todas as palavras; repetir isso para as 26 letras.

- Tempo: O(26 × palavras × tamanho_palavra) — recalcula a contagem de cada letra em cada palavra do zero, letra por letra · Espaço: O(1) extra
- **Por que não basta:** recalcula a contagem de uma letra específica varrendo a palavra inteira, quando dá pra contar TODAS as 26 letras de uma palavra numa única passada por ela.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa o array de contagem (26 posições) da primeira palavra. Para cada palavra seguinte, construa o array de contagem dela e atualize o array acumulado fazendo `minimo[letra] = Math.min(minimo[letra], contagemAtual[letra])`. No final, para cada letra com contagem mínima > 0, adicione essa letra ao resultado repetida `minimo[letra]` vezes.

## 🎬 Exemplo passo a passo

`words = ["bella","label","roller"]`

contagem("bella") = {b:1, e:1, l:2, a:1}
contagem("label") = {l:2, a:1, b:1, e:1}
contagem("roller") = {r:2, o:1, l:2, e:1}

| Passo | palavra | contagem da palavra | minimo acumulado (letras relevantes) |
|---|---|---|---|
| 1 | bella | b:1,e:1,l:2,a:1 | b:1,e:1,l:2,a:1 |
| 2 | label | l:2,a:1,b:1,e:1 | sem mudança (contagens iguais) |
| 3 | roller | r:2,o:1,l:2,e:1 | b:0(sumiu),e:1,l:2,a:0(sumiu) |

Resultado final (letras com mínimo > 0, repetidas conforme a contagem): `["e","l","l"]` ✔ (ordem pode variar)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(soma dos tamanhos das palavras)
- **Espaço:** O(1) extra (arrays fixos de 26 posições)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<String> commonChars(String[] words) {
    int[] minimo = contarLetras(words[0]);

    for (int i = 1; i < words.length; i++) {
        int[] atual = contarLetras(words[i]);
        for (int c = 0; c < 26; c++) {
            minimo[c] = Math.min(minimo[c], atual[c]); // interseção: mantém só o que sobrevive em TODAS as palavras
        }
    }

    List<String> resultado = new ArrayList<>();
    for (int c = 0; c < 26; c++) {
        for (int vezes = 0; vezes < minimo[c]; vezes++) {
            resultado.add(String.valueOf((char) ('a' + c)));
        }
    }
    return resultado;
}

private int[] contarLetras(String palavra) {
    int[] contagem = new int[26];
    for (char ch : palavra.toCharArray()) {
        contagem[ch - 'a']++;
    }
    return contagem;
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

- Usar um `HashSet` (presença/ausência) em vez de contagem — perde a informação de "quantas vezes", e o enunciado exige incluir duplicatas (ex.: "ll" contribui com 2 'l's, não 1).
- Inicializar o array `minimo` como todo zero em vez de com a contagem da primeira palavra — sem a inicialização correta, o `Math.min` sempre resultaria em zero.
- Esquecer que o resultado precisa REPETIR a letra `minimo[c]` vezes, não só incluí-la uma vez — "incluindo duplicatas" é literal no enunciado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Letra repetida no resultado | `["bella","label","roller"]` | ["e","l","l"] (ordem qualquer) | 'l' aparece com contagem mínima 2 entre as três palavras |
| Sem repetição no resultado | `["cool","lock","cook"]` | ["c","o"] | cada letra comum aparece só 1 vez no mínimo |
| Uma única palavra | `["abc"]` | ["a","b","c"] | com uma palavra só, o "comum" é ela mesma |
| Sem letras em comum | `["abc","def"]` | [] | nenhuma letra aparece nas duas |

## 🔗 Conexões

- Problemas irmãos: [0350] Intersection of Two Arrays II (exatamente a mesma técnica de "interseção com contagem mínima", mas aplicada a arrays de números em vez de letras), [0242] Valid Anagram (mesma base de contagem de 26 letras)
- No backend: cálculo de "estoque mínimo garantido" entre múltiplos fornecedores/lotes (ex.: quantas unidades de cada componente estão disponíveis em TODOS os depósitos simultaneamente) — a mesma lógica de interseção com mínimo aparece em consolidação de inventário.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
