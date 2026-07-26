# [1160] Find Words That Can Be Formed by Characters

> 🔗 [LeetCode 1160](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#String` `#Counting` `#Easy`

## 📜 O Problema

Você recebe um array de strings `words` e uma string `chars`. Uma string é **boa** se pode ser formada usando caracteres de `chars` (cada caractere só pode ser usado uma vez **por palavra**).

Retorne **a soma dos comprimentos de todas as strings boas em `words`**.

**Exemplos:**
```
Input:  words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explicação: as strings que podem ser formadas são "cat" e "hat", então a resposta é 3 + 3 = 6.

Input:  words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explicação: as strings que podem ser formadas são "hello" e "world", então a resposta é 5 + 5 = 10.
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 1000`, `1 <= words[i].length, chars.length <= 100` → pequeno, O(words × 26) resolve com folga
- "cada caractere só pode ser usado uma vez POR palavra" → cada palavra é testada de forma independente contra o estoque original de `chars`, sem consumir de uma palavra para outra
- letras minúsculas apenas → array fixo de 26 posições

## 🧭 Como reconhecer o padrão

"A palavra só pode ser formada se as letras disponíveis cobrirem a demanda" é a mesma assinatura de Ransom Note ([0383]): construa a contagem do "estoque" (`chars`) e, para cada palavra, verifique se ela não excede esse estoque em nenhuma letra.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra, para cada letra dela, contar quantas vezes essa letra aparece na palavra E em `chars`, recontando `chars` do zero a cada checagem de letra.

- Tempo: O(words × 26 × tamanho_chars) se recontar `chars` para cada letra checada · Espaço: O(1) extra
- **Por que não basta:** repete a contagem de `chars` várias vezes (uma por letra distinta de cada palavra), quando dá pra contar `chars` uma única vez no início e reaproveitar para todas as palavras.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa o array de contagem de `chars` (26 posições) uma única vez. Para cada palavra, construa o array de contagem dela e verifique se, para cada letra, a contagem na palavra não excede a contagem em `chars`. Se a palavra é "boa", some seu comprimento ao total.

## 🎬 Exemplo passo a passo

`words = ["cat","bt","hat","tree"]`, `chars = "atach"` — estoque de chars: `{a:2, t:1, c:1, h:1}`

| Passo | palavra | contagem da palavra | cabe no estoque? | soma |
|---|---|---|---|---|
| 1 | cat | c:1,a:1,t:1 | sim (1≤1, 1≤2, 1≤1) | 3 |
| 2 | bt | b:1,t:1 | não ('b' não existe no estoque) | 3 |
| 3 | hat | h:1,a:1,t:1 | sim | 3+3=6 |
| 4 | tree | t:1,r:1,e:2 | não ('r' e 'e' não existem no estoque) | 6 |

Resultado final: `6` ✔ (3 de "cat" + 3 de "hat")

## ⚡ Complexidade da solução ótima

- **Tempo:** O(soma dos tamanhos das palavras) + O(len(chars))
- **Espaço:** O(1) extra (arrays fixos de 26 posições)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countCharacters(String[] words, String chars) {
    int[] estoque = new int[26];
    for (char c : chars.toCharArray()) {
        estoque[c - 'a']++;
    }

    int somaTotal = 0;
    for (String word : words) {
        int[] necessario = new int[26];
        for (char c : word.toCharArray()) {
            necessario[c - 'a']++;
        }

        if (cabeNoEstoque(necessario, estoque)) {
            somaTotal += word.length();
        }
    }
    return somaTotal;
}

private boolean cabeNoEstoque(int[] necessario, int[] estoque) {
    for (int i = 0; i < 26; i++) {
        if (necessario[i] > estoque[i]) {
            return false; // esta letra precisa de mais unidades do que o estoque tem
        }
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

- Consumir o estoque de `chars` conforme processa cada palavra (em vez de recriar a contagem "necessário" do zero por palavra) — cada palavra é testada de forma INDEPENDENTE contra o estoque original; consumir o estoque entre palavras diferentes misturaria as verificações.
- Usar um `HashSet` (presença/ausência) em vez de contagem — perde a informação de "quantas vezes", e o enunciado exige que cada caractere seja "usado uma vez" no sentido de quantidade, não só presença.
- Esquecer de somar `word.length()` (o comprimento da palavra) em vez de só contar quantas palavras "boas" existem — o enunciado pede a SOMA dos comprimentos, não a contagem de palavras.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Duas palavras válidas | `words=["cat","bt","hat","tree"], chars="atach"` | 6 | "cat" e "hat" cabem no estoque, "bt" e "tree" não |
| Todas cabem | `words=["hello","world"], chars="welldonehoneyr"` | 10 | ambas cabem no estoque disponível |
| Nenhuma cabe | `words=["abc"], chars="xyz"` | 0 | nenhuma letra de "abc" existe no estoque |
| Palavra com letra repetida excedendo o estoque | `words=["aab"], chars="ab"` | 0 | "aab" precisa de 2 'a's, mas o estoque só tem 1 |

## 🔗 Conexões

- Problemas irmãos: [0383] Ransom Note (exatamente a mesma técnica de "cobre o estoque?"), [0748] Shortest Completing Word (mesma ideia de comparação de arrays de contagem de 26 letras)
- No backend: verificação de disponibilidade de peças/ingredientes antes de montar um pedido (ex.: "este pedido pode ser atendido com o estoque atual?"), aplicando a mesma lógica de contagem para cada pedido de forma independente contra o inventário disponível.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
