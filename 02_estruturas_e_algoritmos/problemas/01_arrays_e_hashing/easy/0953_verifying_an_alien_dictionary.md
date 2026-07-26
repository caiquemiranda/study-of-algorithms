# [0953] Verifying an Alien Dictionary

> 🔗 [LeetCode 953](https://leetcode.com/problems/verifying-an-alien-dictionary/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Numa língua alienígena, surpreendentemente, também se usam as letras minúsculas do inglês, mas possivelmente numa `order` (ordem) diferente. A `order` do alfabeto é alguma permutação das letras minúsculas.

Dada uma sequência de `words` escritas nessa língua alienígena, e a `order` do alfabeto, retorne `true` se e somente se as `words` dadas estão ordenadas lexicograficamente nessa língua.

**Exemplos:**
```
Input:  words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explicação: como 'h' vem antes de 'l' nesta língua, a sequência está ordenada.

Input:  words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explicação: como 'd' vem depois de 'l' nesta língua, words[0] > words[1], logo a sequência não está ordenada.

Input:  words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explicação: os primeiros três caracteres "app" coincidem, e a segunda string é mais curta. Por regra
lexicográfica, "apple" > "app", porque 'l' > vazio, e vazio é definido como menor que qualquer caractere.
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 100`, `1 <= words[i].length <= 20` → pequeno, O(n×L) resolve com folga
- `order.length == 26` → é uma permutação completa do alfabeto, cada letra tem uma posição única
- caso de prefixo (ex.: "app" vs "apple") segue a regra padrão de string vazia sendo "menor que qualquer caractere"

## 🧭 Como reconhecer o padrão

"Comparar ordem lexicográfica segundo um alfabeto customizado" é resolvido mapeando cada letra para sua posição no alfabeto alienígena (array de 26 posições), e depois comparando pares de palavras adjacentes usando essas posições no lugar da ordem ASCII padrão.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de palavras adjacentes, comparar caractere por caractere usando `order.indexOf(char)` toda vez que precisar saber a posição de uma letra.

- Tempo: O(n × L × 26) — cada `indexOf` percorre a string `order` inteira (até 26 caracteres) · Espaço: O(1) extra
- **Por que não basta:** repete a busca "qual a posição desta letra no alfabeto alienígena" toda vez que uma letra é comparada, quando um mapa pré-computado (uma única vez) responde isso em O(1).

## 💡 Solução 2 — A ideia otimizada (intuição)

Pré-compute um array `posicao[26]` onde `posicao[letra - 'a']` é o índice dessa letra em `order`. Para cada par de palavras adjacentes, compare caractere por caractere usando `posicao` em vez da ordem ASCII; a primeira posição em que as letras diferem decide qual palavra vem primeiro. Se uma palavra é prefixo da outra, a mais curta deve vir primeiro.

## 🎬 Exemplo passo a passo

`words = ["word","world","row"]`, `order = "worldabcefghijkmnpqstuvxyz"` — `posicao`: w=0, o=1, r=2, l=3, d=4, a=5...

Comparando "word" com "world":

| Passo | i | char em "word" | char em "world" | posicao(word[i]) | posicao(world[i]) | decisão |
|---|---|---|---|---|---|---|
| 1 | 0 | w | w | 0 | 0 | iguais, continua |
| 2 | 1 | o | o | 1 | 1 | iguais, continua |
| 3 | 2 | r | r | 2 | 2 | iguais, continua |
| 4 | 3 | d | l | 4 | 3 | **4 > 3**: "word" > "world" |

`"word" > "world"` na ordem alienígena → a sequência NÃO está ordenada → **false** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(soma dos tamanhos das palavras) — pré-computação O(26) + comparações
- **Espaço:** O(1) extra (array fixo de 26 posições)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isAlienSorted(String[] words, String order) {
    int[] posicao = new int[26];
    for (int i = 0; i < order.length(); i++) {
        posicao[order.charAt(i) - 'a'] = i; // pré-computa a posição de cada letra no alfabeto alienígena
    }

    for (int i = 1; i < words.length; i++) {
        if (!estaOrdenado(words[i - 1], words[i], posicao)) {
            return false; // já achou um par fora de ordem, corta cedo
        }
    }
    return true;
}

private boolean estaOrdenado(String a, String b, int[] posicao) {
    int tamanhoMinimo = Math.min(a.length(), b.length());
    for (int i = 0; i < tamanhoMinimo; i++) {
        int posA = posicao[a.charAt(i) - 'a'];
        int posB = posicao[b.charAt(i) - 'a'];
        if (posA != posB) {
            return posA < posB; // a primeira diferença decide a ordem
        }
    }
    // todos os caracteres em comum são iguais: a mais curta deve vir primeiro
    return a.length() <= b.length();
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

- Comparar as strings com o operador padrão (`compareTo`) — ele usa a ordem ASCII normal, não a ordem alienígena definida por `order`; é preciso "traduzir" cada letra pela sua posição antes de comparar.
- Esquecer o caso de prefixo (ex.: `"apple"` vs `"app"`) — se uma palavra é prefixo exato da outra, a mais curta precisa vir primeiro; do contrário, a ordem está errada mesmo sem nenhuma letra "fora de ordem".
- Recalcular `order.indexOf(char)` a cada comparação em vez de pré-computar o array `posicao` uma única vez — funciona, mas é O(26) por consulta em vez de O(1).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ordenado corretamente | `words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"` | true | 'h' vem antes de 'l' no alfabeto alienígena |
| Fora de ordem | `words=["word","world","row"], order="worldabcefghijkmnpqstuvxyz"` | false | 'd' vem depois de 'l' na ordem alienígena |
| Caso de prefixo inválido | `words=["apple","app"], order="abcdefghijklmnopqrstuvwxyz"` | false | "app" é prefixo de "apple", mas vem depois dela |
| Lista de uma palavra | `words=["hello"], order="abcdefghijklmnopqrstuvwxyz"` | true | nada para comparar, trivialmente ordenado |

## 🔗 Conexões

- Problemas irmãos: [0791] Custom Sort String (mesma ideia de mapa de ordem customizada), [0014] Longest Common Prefix (mesma técnica de comparar strings posição a posição)
- No backend: validação de ordenação segundo regras de negócio customizadas (ex.: ordenar categorias de produto por uma prioridade específica da empresa, não alfabética) — o mapa "elemento → prioridade" é a mesma técnica usada em comparadores customizados de qualquer linguagem.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
