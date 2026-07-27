# [1961] Check if String Is a Prefix of Array

> 🔗 [LeetCode 1961](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` e um array de strings `words`, determine se `s` é uma **string-prefixo** de `words` — ou seja, se `s` pode ser formada concatenando os primeiros `k` elementos de `words`, para algum `k` positivo até `words.length`.

**Exemplos:**
```
Input:  s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explicação: s = "i" + "love" + "leetcode".

Input:  s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explicação: impossível formar s com um prefixo de words.
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 100`, `1 <= words[i].length <= 20`, `1 <= s.length <= 1000` → tamanhos pequenos, mas O(s.length) já é natural
- `k` precisa ser **positivo** e no máximo `words.length` → não é preciso usar todas as palavras, só um prefixo do array `words`

## 🧭 Como reconhecer o padrão

"Verificar se uma string é formada pela concatenação sequencial de pedaços de uma lista" é resolvido com um ponteiro `i` marcando quanto de `s` já foi "consumido", comparado incrementalmente contra cada palavra de `words`, na ordem — sem nunca precisar montar a string concatenada inteira antes de comparar.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `k` de 1 até `words.length`, concatenar os primeiros `k` elementos numa string nova e comparar com `s` por igualdade.

- Tempo: O(words.length × s.length) — cada tentativa reconstrói e recompara do zero, mesmo repetindo o trabalho já feito na tentativa anterior · Espaço: O(s.length) por tentativa
- **Por que não basta:** recompara, a cada `k`, um prefixo que já tinha sido validado na tentativa anterior; comparar incrementalmente, avançando um ponteiro em `s` conforme cada palavra é confirmada, evita todo esse retrabalho.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um ponteiro `i` começando em 0, representando quantos caracteres de `s` já foram "consumidos" com sucesso. Para cada palavra de `words`, compare-a caractere a caractere com o trecho de `s` a partir de `i`; se baterem todos, avance `i` pelo tamanho da palavra. Se `i` alcançar exatamente `s.length()` a qualquer momento, `s` é uma string-prefixo válida — retorne `true` na hora, sem olhar as palavras restantes. Se alguma palavra não couber ou não bater, retorne `false` imediatamente.

## 🎬 Exemplo passo a passo

`s = "iloveleetcode"`, `words = ["i","love","leetcode","apples"]`

| Passo | word | Comparação com s[i..] | i depois |
|---|---|---|---|
| 1 | `"i"` | `s[0]='i'` vs `'i'`: igual | 1 |
| 2 | `"love"` | `s[1..4]="love"` vs `"love"`: igual | 5 |
| 3 | `"leetcode"` | `s[5..12]="leetcode"` vs `"leetcode"`: igual | 13 = `s.length()` → **retorna true** |

Resultado final: `true` ✔ (nem chega a olhar `"apples"`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(s.length) — no total, a soma dos tamanhos das palavras comparadas nunca ultrapassa o tamanho de `s`
- **Espaço:** O(1) — só o ponteiro `i`, sem montar nenhuma string nova

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isPrefixString(String s, String[] words) {
    int i = 0; // quantos caracteres de s já foram consumidos com sucesso

    for (String word : words) {
        int len = word.length();
        if (i + len > s.length()) {
            return false; // esta palavra não cabe mais no que resta de s
        }
        for (int j = 0; j < len; j++) {
            if (s.charAt(i + j) != word.charAt(j)) {
                return false;
            }
        }
        i += len;
        if (i == s.length()) {
            return true; // s foi totalmente formado por um prefixo de words
        }
    }

    return false; // percorreu todas as palavras sem completar s
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

- Concatenar todas as palavras primeiro e só depois comparar com `s` — funciona, mas gasta tempo/espaço reconstruindo uma string inteira quando basta comparar incrementalmente, palavra por palavra.
- Esquecer de checar `i + len > s.length()` antes de comparar — sem esse limite, ler `s.charAt(i+j)` além do fim de `s` lança exceção quando uma palavra "não cabe" mais no que resta.
- Retornar `true` só depois de processar TODAS as palavras — a condição de sucesso é `i == s.length()` a qualquer momento durante o processamento, mesmo com palavras sobrando no array depois disso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Prefixo exato | `s="iloveleetcode"`, `words=["i","love","leetcode","apples"]` | true | as 3 primeiras palavras formam `s` exatamente |
| Ordem errada | `s="iloveleetcode"`, `words=["apples","i","love","leetcode"]` | false | a primeira palavra já não bate com o início de `s` |
| Palavra não cabe mais | `s="ilov"`, `words=["i","love"]` | false | `"love"` (4 chars) não cabe no que resta de `s` (só 3 chars: `"lov"`) |
| k = words.length inteiro | `s="ab"`, `words=["a","b"]` | true | precisa consumir todas as palavras pra completar `s` |

## 🔗 Conexões

- Problemas irmãos: [0028] Find the Index of the First Occurrence in a String (mesma técnica de comparação caractere a caractere), [1768] Merge Strings Alternately (mesma família de compor uma string a partir de pedaços, com ponteiros rastreando o progresso)
- No backend: validar se um payload recebido é exatamente a concatenação de um prefixo de uma lista de campos esperados — por exemplo, validar um cabeçalho de protocolo binário formado por campos sequenciais conhecidos, parando assim que o cabeçalho é reconhecido.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
