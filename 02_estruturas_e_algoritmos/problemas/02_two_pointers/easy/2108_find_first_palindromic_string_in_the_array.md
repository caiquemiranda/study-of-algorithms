# [2108] Find First Palindromic String in the Array

> 🔗 [LeetCode 2108](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#String` `#Easy`

## 📜 O Problema

Dado um array de strings `words`, retorne a **primeira** string palindrômica do array. Se nenhuma for palíndromo, retorne a string vazia `""`.

**Exemplos:**
```
Input:  words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explicação: "racecar" também é palíndromo, mas não é o primeiro.

Input:  words = ["notapalindrome","racecar"]
Output: "racecar"

Input:  words = ["def","ghi"]
Output: ""
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 100`, `1 <= words[i].length <= 100` → entrada pequena, O(total de caracteres) já é natural
- Pede a **primeira** ocorrência → sinaliza busca de curto-circuito: pode parar assim que encontrar, sem processar o resto do array

## 🧭 Como reconhecer o padrão

"Checar se uma string lê igual de trás para frente" é a checagem de palíndromo de [0125] Valid Palindrome, aplicada palavra por palavra dentro de um array, parando na primeira que passar no teste.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra, criar sua versão revertida com `new StringBuilder(word).reverse().toString()` e comparar por igualdade com a original.

- Tempo: O(total de caracteres) · Espaço: O(m) por palavra testada — a cópia revertida
- **Por que não basta:** já tem a mesma ordem de tempo da versão otimizada, mas aloca uma string nova para cada palavra testada; dois ponteiros checam palíndromo sem nenhuma cópia, comparando os caracteres diretamente na palavra original.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `words` na ordem. Para cada palavra, use dois ponteiros nas pontas (`left`/`right`) comparando caracteres simétricos, como em [0125] Valid Palindrome. Assim que uma palavra passar na checagem completa, retorne-a imediatamente — não é preciso continuar olhando as demais.

## 🎬 Exemplo passo a passo

`words = ["abc","car","ada","racecar","cool"]`

| Passo | palavra | Checagem com dois ponteiros | Resultado |
|---|---|---|---|
| 1 | `"abc"` | `left=0('a')`, `right=2('c')` → diferentes | não é palíndromo, tenta a próxima |
| 2 | `"car"` | `left=0('c')`, `right=2('r')` → diferentes | não é palíndromo, tenta a próxima |
| 3 | `"ada"` | `left=0('a')`, `right=2('a')` → iguais; `left=1==right=1` (meio) → para | é palíndromo → **retorna "ada"** |

Resultado final: `"ada"` ✔ (nem chega a avaliar `"racecar"`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(total de caracteres em words) no pior caso (quando nenhuma é palíndromo ou a resposta está no final); bem menor na prática, graças ao curto-circuito
- **Espaço:** O(1) além do necessário pra retornar a string encontrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String firstPalindrome(String[] words) {
    for (String word : words) {
        if (isPalindrome(word)) {
            return word; // curto-circuito: primeira palindrômica encontrada
        }
    }
    return "";
}

private boolean isPalindrome(String s) {
    int left = 0;
    int right = s.length() - 1;
    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) {
            return false;
        }
        left++;
        right--;
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

- Continuar checando todas as palavras mesmo depois de achar a primeira palindrômica — o enunciado pede a PRIMEIRA; assim que encontrar, retorne na hora.
- Esquecer o caso em que nenhuma palavra é palíndromo — a resposta correta é a string vazia `""`, não `null` ou uma exceção.
- Reimplementar a checagem revertendo a string (`StringBuilder.reverse()`) em vez de comparar com dois ponteiros — funciona, mas gasta espaço O(m) por palavra à toa.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Múltiplos palíndromos | `["abc","car","ada","racecar","cool"]` | `"ada"` | retorna o primeiro, ignora `"racecar"` |
| Só um palíndromo, no final | `["notapalindrome","racecar"]` | `"racecar"` | precisa checar todas até achar |
| Nenhum palíndromo | `["def","ghi"]` | `""` | retorna string vazia |
| Palavra de 1 caractere | `["a"]` | `"a"` | qualquer string de 1 caractere já é palíndromo |

## 🔗 Conexões

- Problemas irmãos: [0125] Valid Palindrome (mesma técnica de checagem, usada aqui como sub-rotina), [0680] Valid Palindrome II (mesma checagem, mas com tolerância a 1 remoção)
- No backend: filtrar o primeiro item de uma coleção que satisfaz uma propriedade (busca de curto-circuito) — útil sempre que só o primeiro resultado importa e processar a coleção inteira seria desperdício.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
