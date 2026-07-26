# [0459] Repeated Substring Pattern

> 🔗 [LeetCode 459](https://leetcode.com/problems/repeated-substring-pattern/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#StringMatching` `#Easy`

## 📜 O Problema

Dada uma string `s`, verifique se ela pode ser construída pegando uma substring dela e concatenando múltiplas cópias dessa substring.

**Exemplos:**
```
Input:  s = "abab"
Output: true
Explicação: é a substring "ab" duas vezes.

Input:  s = "aba"
Output: false

Input:  s = "abcabcabcabc"
Output: true
Explicação: é a substring "abc" quatro vezes, ou "abcabc" duas vezes.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^4` → O(n²) simples ainda passaria (10^8), mas existe um truque O(n) elegante que evita até testar divisores manualmente
- `s` consiste apenas de letras minúsculas → sem preocupação de caixa ou caracteres especiais

## 🧭 Como reconhecer o padrão

Quando o enunciado pede para detectar se uma string inteira é "periódica" (formada por repetições de um padrão menor), pense no truque de concatenar a string consigo mesma: qualquer propriedade cíclica de `s` fica visível dentro de `s+s`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada tamanho candidato `len` que seja divisor de `n` (de 1 até n/2), pegue o prefixo de tamanho `len` e verifique se repeti-lo `n/len` vezes reconstrói `s` exatamente.

- Tempo: O(n²) no pior caso (até n/2 candidatos, cada verificação O(n)) · Espaço: O(n) para a string reconstruída
- **Por que não basta:** com n=10^4 dá no máximo 10^8 operações — ainda passa, mas é bem mais trabalho do que o truque direto de concatenação, que resolve sem testar nenhum divisor manualmente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se `s` é formada por repetições de algum padrão `p` (pelo menos 2 vezes), então uma cópia "deslocada" de `s` aparece dentro de `s+s`, começando em algum ponto diferente de 0 e de n. Construa `doubled = (s+s)` removendo o primeiro e o último caractere, e verifique se `s` está contida nesse resultado cortado. Se `s` NÃO é periódica, a única forma de `s` aparecer dentro de `s+s` é bem no início (posição 0) ou bem no fim (posição n) — que foram cortadas — então ela não vai reaparecer na janela cortada.

## 🎬 Exemplo passo a passo

`s = "abab"`

| Passo | Construção | Valor |
|---|---|---|
| 1 | s | "abab" |
| 2 | s+s | "abababab" |
| 3 | (s+s) sem primeiro e último char | "bababa" |
| 4 | "abab" aparece em "bababa"? | sim, a partir da posição 1 |

Resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) esperado — uma concatenação O(n) e uma busca de substring que, para este padrão específico de entrada, se comporta linearmente na prática (a implementação naive de `contains`/`indexOf` do Java é O(n·m) no pior caso teórico geral, mas isso não se manifesta de forma relevante aqui)
- **Espaço:** O(n) — para a string concatenada `s+s`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean repeatedSubstringPattern(String s) {
    String doubled = s + s;
    // remove o primeiro e o último caractere para não deixar a cópia "trivial" (offset 0 ou n) valer
    String cortado = doubled.substring(1, doubled.length() - 1);
    return cortado.contains(s);
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

- Esquecer de cortar o primeiro e o último caractere de `s+s` — sem o corte, `s` sempre aparece em `s+s` (nas posições 0 e n), dando falso positivo mesmo quando `s` não é periódica.
- Tentar resolver enumerando apenas divisores de `n` sem essa observação de concatenação — funciona, mas é mais código e mais fácil de errar o laço de verificação.
- `String.contains()` do Java não é O(n) garantido no pior caso teórico (é busca ingênua) — para este limite específico (n ≤ 10^4) não chega a ser um problema prático.
- Achar que o padrão repetido precisa ter tamanho par ou metade exata — ele pode ter qualquer tamanho que divida `n` exatamente (ex.: `"abcabcabcabc"` repete um padrão de tamanho 3, não 2).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Repetição simples | `s="abab"` | true | padrão "ab" duas vezes |
| Sem repetição | `s="aba"` | false | nenhum padrão menor reconstrói a string |
| Múltiplas repetições | `s="abcabcabcabc"` | true | padrão "abc" (ou "abcabc") |
| Um único caractere | `s="a"` | false | não há como repetir um padrão menor que ele mesmo |

## 🔗 Conexões

- Problemas irmãos: [0028] Find the Index of the First Occurrence in a String (mesma família de busca de substring), [0796] Rotate String (mesmo truque de concatenar a string consigo mesma para testar propriedades cíclicas)
- No backend: detectar padrões periódicos em séries temporais ou logs (ex.: identificar se uma sequência de eventos se repete em ciclo fixo), útil também em ideias de compressão de dados (detecção de período).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
