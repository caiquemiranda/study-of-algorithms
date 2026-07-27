# [1768] Merge Strings Alternately

> 🔗 [LeetCode 1768](https://leetcode.com/problems/merge-strings-alternately/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dadas duas strings `word1` e `word2`, mescle-as alternando letras, começando por `word1`. Se uma for mais longa que a outra, anexe as letras restantes no final da string mesclada.

**Exemplos:**
```
Input:  word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input:  word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explicação: word2 é mais longa, "rs" é anexado no final.

Input:  word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explicação: word1 é mais longa, "cd" é anexado no final.
```

**Restrições (e o que elas denunciam):**
- `1 <= word1.length, word2.length <= 100` → O(n+m) esperado, entrada pequena
- Tamanhos podem ser **diferentes** → o critério de parada não pode assumir que as duas strings acabam juntas; é preciso continuar com a mais longa depois que a mais curta esgotar

## 🧭 Como reconhecer o padrão

"Intercalar dois conjuntos de dados, continuando com o que sobra quando um deles acaba" é dois ponteiros andando na mesma direção, cada um na sua própria string, avançando de forma independente — sem nunca precisar comparar valores entre eles (diferente de [0088] Merge Sorted Array, aqui a ordem de intercalação é fixa, não decidida por comparação).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Construir a string resultado concatenando caractere a caractere com o operador `+=` dentro de um loop.

- Tempo: O((n+m)²) · Espaço: O(n+m) para o resultado final
- **Por que não basta:** em Java (e em várias outras linguagens), strings são imutáveis — cada `+=` cria uma **nova** string, copiando tudo que já foi montado até ali. Repetir isso a cada caractere transforma um trabalho linear em quadrático.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um `StringBuilder` (mutável, evita as cópias repetidas) e dois ponteiros `i` (em `word1`) e `j` (em `word2`), ambos começando em 0. A cada passo, anexe `word1[i]` se `i` ainda for válido, depois `word2[j]` se `j` ainda for válido, avançando cada um independentemente. Continue enquanto **qualquer um** dos dois ainda tiver caracteres — isso naturalmente anexa o restante da string mais longa depois que a mais curta se esgota.

## 🎬 Exemplo passo a passo

`word1 = "ab"`, `word2 = "pqrs"`

| Passo | i | j | Ação | Resultado parcial |
|---|---|---|---|---|
| 1 | 0 | 0 | anexa `word1[0]='a'` (i=1); anexa `word2[0]='p'` (j=1) | `"ap"` |
| 2 | 1 | 1 | anexa `word1[1]='b'` (i=2); anexa `word2[1]='q'` (j=2) | `"apbq"` |
| 3 | 2 (esgotado) | 2 | `word1` esgotado, pula; anexa `word2[2]='r'` (j=3) | `"apbqr"` |
| 4 | 2 | 3 | `word1` esgotado, pula; anexa `word2[3]='s'` (j=4) | `"apbqrs"` |

Resultado final: `"apbqrs"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — cada caractere das duas strings é anexado exatamente uma vez
- **Espaço:** O(n + m) para o resultado (exigido pelo problema); o `StringBuilder` evita cópias intermediárias

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String mergeAlternately(String word1, String word2) {
    StringBuilder sb = new StringBuilder();
    int i = 0;
    int j = 0;
    int n1 = word1.length();
    int n2 = word2.length();

    while (i < n1 || j < n2) { // continua enquanto QUALQUER uma ainda tiver caracteres
        if (i < n1) {
            sb.append(word1.charAt(i));
            i++;
        }
        if (j < n2) {
            sb.append(word2.charAt(j));
            j++;
        }
    }

    return sb.toString();
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

- Usar `+=` numa String dentro do loop em vez de `StringBuilder` — cada `+=` recopia tudo que já foi montado, virando O(n²); `StringBuilder.append` é O(1) amortizado.
- Assumir que as duas strings têm o mesmo tamanho e usar um loop com um único contador compartilhado — quando os tamanhos diferem, é preciso continuar com a string mais longa depois que a mais curta esgota; por isso a condição é `i < n1 || j < n2` (OU, não E).
- Esquecer de checar `i < n1` e `j < n2` individualmente antes de cada `charAt` — sem essa checagem, ler um índice além do fim de uma das strings já esgotadas lança exceção.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Mesmo tamanho | `word1="abc"`, `word2="pqr"` | `"apbqcr"` | intercalação perfeita, sem sobra |
| word2 mais longa | `word1="ab"`, `word2="pqrs"` | `"apbqrs"` | sobra `"rs"` de word2 anexada no final |
| word1 mais longa | `word1="abcd"`, `word2="pq"` | `"apbqcd"` | sobra `"cd"` de word1 anexada no final |
| Um único caractere cada | `word1="a"`, `word2="b"` | `"ab"` | caso mínimo, intercalação de 1 caractere cada |

## 🔗 Conexões

- Problemas irmãos: [0088] Merge Sorted Array (mesma ideia de mesclar duas sequências com dois ponteiros, mas por ORDEM em vez de alternância fixa), [0006] Zigzag Conversion (também reorganiza caracteres num padrão intercalado)
- No backend: intercalar dois streams/canais de dados na ordem de chegada — por exemplo, combinar mensagens de dois canais alternando round-robin, continuando com o canal restante quando um deles esgota primeiro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
