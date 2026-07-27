# [1332] Remove Palindromic Subsequences

> 🔗 [LeetCode 1332](https://leetcode.com/problems/remove-palindromic-subsequences/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` composta só por `'a'` e `'b'`, em cada passo você pode remover uma **subsequência palindrômica** (não precisa ser contígua). Retorne o número **mínimo** de passos para esvaziar `s`.

**Exemplos:**
```
Input:  s = "ababa"
Output: 1
Explicação: s já é um palíndromo, remove tudo de uma vez.

Input:  s = "abb"
Output: 2
Explicação: remove "a", depois remove "bb".

Input:  s = "baabb"
Output: 2
Explicação: remove "baab", depois remove "b".
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 1000` → tamanho pequeno, mas a resposta real não depende do tamanho da string
- `s[i]` é `'a'` ou `'b'` **apenas** → essa é a peça-chave: com só dois símbolos possíveis, qualquer subsequência formada por um único símbolo repetido (ex.: `"aaa"` ou `"bb"`) já é um palíndromo por definição, já que todo caractere é igual ao seu espelhado

## 🧭 Como reconhecer o padrão

"Contar o mínimo de remoções de subsequência palindrômica" parece pedir uma busca cara, mas o alfabeto restrito a 2 símbolos transforma o problema em uma checagem simples: a resposta só pode ser `0` (string vazia), `1` (a string inteira já é palíndromo) ou `2` (qualquer outro caso — sempre dá pra remover todos os `'a'`s numa jogada e todos os `'b'`s na outra). A única verificação real necessária — "`s` é palíndromo?" — usa dois ponteiros nas pontas, como em [0125] Valid Palindrome.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Modelar como busca em grafo de estados: cada estado é uma versão de `s` com algumas letras removidas; uma aresta remove uma subsequência palindrômica levando a um estado menor. Fazer BFS a partir de `s` até alcançar a string vazia, contando os passos mínimos.

- Tempo: exponencial — o número de subsequências palindrômicas possíveis de remover a cada passo cresce exponencialmente com o tamanho da string
- **Por que não basta:** o problema tem uma estrutura muito mais simples do que "buscar o caminho ótimo" sugere. Como `s` só tem dois caracteres possíveis, qualquer subsequência formada só por `'a'`s (ou só por `'b'`s) já é palíndromo automaticamente — isso limita a resposta a no máximo 2 passos, tornando a busca completamente desnecessária.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pense no pior caso possível: você sempre pode remover **todos** os `'a'`s da string numa única jogada (formam uma subsequência tipo `"aaaa"`, palíndromo por definição), e depois remover todos os `'b'`s restantes em outra jogada — no máximo **2 passos**, sempre. A única forma de precisar de menos é se a string inteira já for um palíndromo (aí 1 passo remove tudo de uma vez) ou se já estiver vazia (0 passos). Então: cheque se `s` está vazia (0), senão cheque se `s` é palíndromo com dois ponteiros (1), senão a resposta é sempre 2.

## 🎬 Exemplo passo a passo

Checagem de palíndromo para `s = "abb"` (n=3, decide entre resposta 1 ou 2)

| Passo | left | right | s[left] | s[right] | Igual? | Ação |
|---|---|---|---|---|---|---|
| 1 | 0 | 2 | `a` | `b` | não | retorna `false` (não é palíndromo) imediatamente |

Como `s` não é palíndromo e não está vazia, a resposta é `2` ✔ (bate com o enunciado: remove `"a"`, depois `"bb"`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — a checagem de palíndromo com dois ponteiros é a única operação não-trivial
- **Espaço:** O(1) — só os índices dos ponteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int removePalindromeSub(String s) {
    if (s.isEmpty()) {
        return 0;
    }
    return isPalindrome(s) ? 1 : 2; // com alfabeto de 2 símbolos, 2 é sempre alcançável
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

- Tentar resolver como um problema geral de "mínimo de remoções de subsequência palindrômica" (que seria genuinamente difícil para alfabetos maiores) — a restrição de só 2 caracteres possíveis é o que torna a resposta sempre ≤ 2; sem perceber isso, é fácil cair numa solução exponencial desnecessária.
- Esquecer o caso de string vazia — embora a constraint garanta `s.length >= 1` na entrada, é bom não assumir cegamente que a resposta mínima é sempre 1.
- Achar que a resposta pode ser maior que 2 em algum caso — não pode: "remover todos os `'a'`s, depois todos os `'b'`s" sempre funciona em exatamente 2 passos quando `s` não é palíndromo, então 2 é sempre um teto alcançável.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já palíndromo | `"ababa"` | 1 | remove tudo de uma vez |
| Não palíndromo | `"abb"` | 2 | remove todos os `'a'`, depois todos os `'b'` |
| Não palíndromo, mais longo | `"baabb"` | 2 | mesma lógica, independe do tamanho da string |
| Um único caractere | `"a"` | 1 | qualquer string de 1 caractere já é palíndromo |

## 🔗 Conexões

- Problemas irmãos: [0125] Valid Palindrome (mesma técnica de checagem com dois ponteiros, usada aqui como sub-rotina), [1616] Split Two Strings to Make Palindrome (também explora a estrutura de palíndromos)
- No backend: reconhecer quando um problema aparentemente combinatório tem uma resposta constante (ou quase-constante) por causa de uma restrição escondida no domínio dos dados — aqui, só 2 símbolos possíveis — evitando implementar uma busca cara quando uma checagem simples resolve.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
