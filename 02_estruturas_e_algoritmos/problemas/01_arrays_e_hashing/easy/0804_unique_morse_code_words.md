# [0804] Unique Morse Code Words

> 🔗 [LeetCode 804](https://leetcode.com/problems/unique-morse-code-words/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#String` `#Easy`

## 📜 O Problema

O Código Morse Internacional define uma codificação padrão onde cada letra é mapeada para uma série de pontos e traços, por exemplo `'a'` mapeia para `".-"`, `'b'` mapeia para `"-..."`, `'c'` mapeia para `"-.-."`, e assim por diante.

Dado um array de strings `words`, onde cada palavra pode ser escrita como a concatenação do código Morse de cada letra — chamamos essa concatenação de **transformação** da palavra — retorne **o número de transformações diferentes entre todas as palavras**.

**Exemplos:**
```
Input:  words = ["gin","zen","gig","msg"]
Output: 2
Explicação: as transformações são:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
Existem 2 transformações diferentes: "--...-." e "--...--.".

Input:  words = ["a"]
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 100`, `1 <= words[i].length <= 12` → entrada pequena, qualquer O(n) resolve com folga
- letras minúsculas apenas → a tabela morse fixa de 26 posições cobre todas as entradas possíveis
- código morse é um mapeamento fixo por letra → cada palavra vira uma string determinística, perfeita para comparar via hash set

## 🧭 Como reconhecer o padrão

"Quantas transformações distintas existem" é sempre resolvido aplicando a transformação em cada elemento e contando quantos resultados únicos aparecem, via hash set — não precisa comparar par a par.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra, construir sua transformação morse; comparar a nova transformação com todas as transformações já vistas anteriormente.

- Tempo: O(n² × L) onde L é o tamanho médio da transformação — comparação par a par de todas as transformações · Espaço: O(n×L)
- **Por que não basta:** recompara cada nova transformação contra todas as anteriores, quando um hash set decide "já vi essa" em O(1) amortizado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pré-compute a tabela morse fixa (26 posições). Para cada palavra, construa sua transformação concatenando o código de cada letra, e adicione ao hash set. A resposta é o tamanho do set.

## 🎬 Exemplo passo a passo

`words = ["gin","zen","gig","msg"]`

| Passo | palavra | transformação | já no set? | set depois |
|---|---|---|---|---|
| 1 | gin | --...-. | não | {--...-.} |
| 2 | zen | --...-. | sim (igual à anterior) | {--...-.} |
| 3 | gig | --...--. | não | {--...-., --...--.} |
| 4 | msg | --...--. | sim (igual à anterior) | {--...-., --...--.} |

Resultado final: tamanho do set = `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n × L) — n palavras, L letras médias por palavra, cada uma O(1) para achar o código morse
- **Espaço:** O(n × L) — para o hash set de transformações

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int uniqueMorseRepresentations(String[] words) {
    String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                       ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                       ".--","-..-","-.--","--.."};
    Set<String> transformacoes = new HashSet<>();
    for (String word : words) {
        StringBuilder sb = new StringBuilder();
        for (char c : word.toCharArray()) {
            sb.append(morse[c - 'a']); // concatena o código morse de cada letra
        }
        transformacoes.add(sb.toString());
    }
    return transformacoes.size();
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

- Usar `String +=` dentro do loop de letras em vez de `StringBuilder` — funciona, mas é um hábito ruim que fica quadrático em problemas com strings maiores.
- Esquecer que o índice do código morse é `c - 'a'`, não o caractere em si.
- Comparar as transformações com `equals` par a par em vez de um `HashSet` — funciona, mas volta para O(n²).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Transformações repetidas | `["gin","zen","gig","msg"]` | 2 | duas transformações distintas apesar de 4 palavras |
| Palavra única | `["a"]` | 1 | trivial |
| Todas diferentes | `["a","b","c"]` | 3 | cada letra tem código morse único |
| Todas iguais | `["abc","abc"]` | 1 | mesma palavra gera mesma transformação |

## 🔗 Conexões

- Problemas irmãos: [0242] Valid Anagram (mesma ideia de canonicalizar e comparar), [0049] Group Anagrams (mesmo padrão de "transformar e agrupar/contar com hash")
- No backend: deduplicação de registros após uma transformação normalizadora (ex.: contar quantos hashes/checksums distintos existem depois de aplicar uma função de codificação a um conjunto de dados).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
