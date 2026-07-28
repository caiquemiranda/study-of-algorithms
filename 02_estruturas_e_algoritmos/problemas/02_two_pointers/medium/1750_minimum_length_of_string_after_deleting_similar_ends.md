# [1750] Minimum Length of String After Deleting Similar Ends

> 🔗 [LeetCode 1750](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Medium`

## 📜 O Problema

Dada uma string `s` com só `'a'`, `'b'`, `'c'`, repita quantas vezes quiser: escolha um prefixo não-vazio com caracteres todos iguais, um sufixo não-vazio com caracteres todos iguais (sem sobrepor o prefixo), ambos do MESMO caractere, e remova os dois. Retorne o menor tamanho possível de `s` ao final.

**Exemplos:**
```
Input:  s = "ca"
Output: 2
Explicação: primeiro e último caractere já diferem, nada é removido.

Input:  s = "cabaabac"
Output: 0
Explicação: remove 'c's, depois 'a's, depois 'b's, depois 'a's — sobra vazio.

Input:  s = "aabccabba"
Output: 3
Explicação: remove 'a's e depois 'b's — sobra "cca".
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n²) é arriscado, O(n) é o esperado
- Só 3 caracteres possíveis (`a`,`b`,`c`) → não muda a estratégia, só limita o alfabeto
- Cada rodada remove um BLOCO inteiro de caracteres iguais (não um caractere por vez) → sinaliza que o algoritmo deve pular blocos inteiros de uma vez, não avançar caractere por caractere

## 🧭 Como reconhecer o padrão

"Remover repetidamente prefixo e sufixo iguais até eles divergirem" é dois ponteiros nas pontas convergindo pro centro — igual à checagem de palíndromo de [0125], mas em vez de só comparar, cada rodada de igualdade **consome o bloco inteiro** de caracteres repetidos de cada lado antes de comparar de novo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular literalmente o processo: a cada rodada, escanear a string inteira pra achar o tamanho do prefixo e do sufixo de caracteres iguais, remover ambos criando uma substring nova, e repetir até não dar mais.

- Tempo: O(n²) no pior caso — várias rodadas, cada uma reconstruindo a string · Espaço: O(n) por rodada para a nova substring
- **Por que não basta:** recria a string a cada rodada; o processo inteiro pode ser simulado com dois ponteiros avançando pra dentro, sem NUNCA copiar ou remover de verdade — cada ponteiro só anda pra frente, nunca revisita uma posição.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no início e `right` no fim. Enquanto `s[left] == s[right]`, esse é o caractere sendo removido nesta rodada: avance `left` enquanto ele continuar igual a esse caractere (consumindo o bloco/prefixo inteiro), e recue `right` da mesma forma (consumindo o bloco/sufixo inteiro). Repita enquanto os caracteres nas novas pontas continuarem batendo (podendo ser um caractere diferente a cada rodada). Pare quando divergirem ou os ponteiros se cruzarem; o tamanho restante é `right - left + 1`.

## 🎬 Exemplo passo a passo

`s = "aabccabba"` (n=9)

| Passo | left (antes) | right (antes) | s[left] | s[right] | Ação | left (depois) | right (depois) |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 8 | `a` | `a` | remove todos os `'a'` das duas pontas | 2 | 7 |
| 2 | 2 | 7 | `b` | `b` | remove todos os `'b'` das duas pontas | 3 | 5 |
| 3 | 3 | 5 | `c` | `a` | diferentes, loop externo para | 3 | 5 |

Comprimento final: `right - left + 1 = 5 - 3 + 1 = 3` ✔ (a substring restante é `"cca"`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada posição da string é visitada no máximo uma vez, seja pelo `left` seja pelo `right`
- **Espaço:** O(1) — só os índices dos ponteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumLength(String s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right && s.charAt(left) == s.charAt(right)) {
        char c = s.charAt(left);
        // remove TODO o prefixo de caracteres iguais a c
        while (left <= right && s.charAt(left) == c) {
            left++;
        }
        // remove TODO o sufixo de caracteres iguais a c
        while (right >= left && s.charAt(right) == c) {
            right--;
        }
    }

    return right - left + 1; // dá 0 corretamente se tudo foi consumido
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

- Remover só UM caractere de cada ponta por vez em vez do BLOCO inteiro — o enunciado permite remover o prefixo/sufixo inteiro de uma vez; pular o bloco todo de uma vez é o que garante O(n) em vez de O(n²).
- Esquecer de checar `left <= right` (ou `right >= left`) dentro dos loops internos de remoção de bloco — sem essa checagem, ao remover um bloco que consome TODA a string restante, os ponteiros podem se cruzar e acessar índices inválidos.
- Achar que basta uma única remoção de prefixo/sufixo — o processo se repete enquanto os caracteres nas pontas continuarem iguais (podendo ser letras DIFERENTES a cada rodada, como `'a'` e depois `'b'` no exemplo 3); o loop externo continua até divergirem ou os ponteiros se cruzarem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Extremos diferentes | `"ca"` | 2 | primeiro e último caractere já diferem, nada é removido |
| Remove tudo | `"cabaabac"` | 0 | quatro rodadas de remoção consomem a string inteira |
| Sobra no meio | `"aabccabba"` | 3 | duas rodadas removem `'a'`s e `'b'`s, sobra `"cca"` |
| Único caractere | `"a"` | 1 | `left == right` desde o início, loop externo nem executa |

## 🔗 Conexões

- Problemas irmãos: [0125] Valid Palindrome (mesma convergência de ponteiros nas pontas), [0696] Count Binary Substrings (mesma ideia de trabalhar com blocos de caracteres repetidos consecutivos)
- No backend: "aparar" (trim) repetidamente um buffer ou log removendo blocos idênticos simétricos nas pontas até encontrar conteúdo genuinamente diferente — útil em comparação de streams com padding repetido nas extremidades.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
