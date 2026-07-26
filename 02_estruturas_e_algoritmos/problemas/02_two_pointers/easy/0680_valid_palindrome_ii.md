# [0680] Valid Palindrome II

> 🔗 [LeetCode 680](https://leetcode.com/problems/valid-palindrome-ii/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Greedy` `#Easy`

## 📜 O Problema

Dada uma string `s`, retorne `true` se ela puder se tornar um palíndromo removendo **no máximo um** caractere.

**Exemplos:**
```
Input:  s = "aba"
Output: true

Input:  s = "abca"
Output: true
Explicação: remova o 'c'.

Input:  s = "abc"
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n) esperado
- `s` só tem letras minúsculas → sem normalização de case ou pontuação, diferente de [0125] Valid Palindrome
- "No máximo um" caractere removido → a decisão só precisa ser tomada uma vez, no primeiro (e único) mismatch permitido

## 🧭 Como reconhecer o padrão

"Verificar palíndromo com folga pra 1 erro" é [0125] Valid Palindrome com um ajuste greedy: dois ponteiros nas pontas convergem normalmente; no **primeiro** mismatch, sobra só uma decisão a tomar — remover o caractere da esquerda ou o da direita — e daí em diante não pode haver mais nenhum outro mismatch.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i` de `0` a `n-1`, construir a string sem o caractere `i` e checar se o resultado é palíndromo.

- Tempo: O(n²) — n candidatos a remover, cada checagem de palíndromo custa O(n) · Espaço: O(n) por candidato (a string sem o caractere `i`)
- **Por que não basta:** testa remoções em posições que nunca poderiam ajudar — se os dois ponteiros já convergiram sem problema até certo ponto, só o caractere exatamente no ponto do primeiro mismatch pode ser o culpado; testar todas as outras posições é trabalho desperdiçado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` e `right` nas pontas, avançando um em direção ao outro enquanto os caracteres coincidem. No **primeiro** mismatch, só existem duas hipóteses de salvar a resposta: remover o caractere de `left` (verificar se `s[left+1..right]` é palíndromo) ou remover o de `right` (verificar `s[left..right-1]`). Se qualquer uma das duas verificações (sem mais nenhuma tolerância a erro) passar, a resposta é `true`.

## 🎬 Exemplo passo a passo

`s = "abca"` (índices 0 a 3: `a,b,c,a`)

| Passo | left | right | s[left] | s[right] | Igual? | Ação |
|---|---|---|---|---|---|---|
| 1 | 0 | 3 | `a` | `a` | sim | avança: left=1, right=2 |
| 2 | 1 | 2 | `b` | `c` | não | testa `s[2..2]` (remover left) ou `s[1..1]` (remover right); ambos são palíndromo de 1 caractere → **true** |

Resultado final: `true` ✔ (equivalente a remover o `'c'`, como no enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — a convergência inicial dos ponteiros é O(n), e a checagem extra no primeiro (e único) mismatch também é O(n), executada só uma vez
- **Espaço:** O(1) — só os índices dos ponteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean validPalindrome(String s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) {
            // no primeiro mismatch, só resta testar remover UM dos dois lados
            return isPalindromeRange(s, left + 1, right) || isPalindromeRange(s, left, right - 1);
        }
        left++;
        right--;
    }

    return true; // nenhum mismatch: já é palíndromo sem remover nada
}

private boolean isPalindromeRange(String s, int left, int right) {
    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) {
            return false; // aqui não sobra mais tolerância: qualquer mismatch reprova
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

- Testar a remoção de só UM dos lados (ex.: sempre `right--`) no primeiro mismatch — o caractere "culpado" pode ser tanto o da esquerda quanto o da direita; é preciso testar as **duas** possibilidades e aceitar se qualquer uma funcionar.
- Permitir mais de uma remoção dentro de `isPalindromeRange` — o problema permite remover **no máximo um** caractere no total; por isso a checagem auxiliar não pode tolerar nenhum outro mismatch depois do primeiro.
- Achar que é preciso testar remover cada posição do array (força bruta O(n²)) — só o caractere exatamente no ponto do primeiro mismatch pode salvar a resposta; qualquer outra posição já estava "combinando" perfeitamente antes disso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já é palíndromo | `"aba"` | true | nenhum mismatch, nem precisa remover nada |
| Precisa remover um | `"abca"` | true | mismatch em `b`/`c`, remover um dos dois resolve |
| Impossível com 1 remoção | `"abc"` | false | removendo qualquer caractere ainda sobra mismatch |
| Um único caractere | `"a"` | true | `left == right`, o loop nem chega a comparar |

## 🔗 Conexões

- Problemas irmãos: [0125] Valid Palindrome (mesma técnica sem a permissão de remover 1 caractere), [0009] Palindrome Number (mesmo conceito de palíndromo, aplicado a número em vez de string)
- No backend: validação "tolerante a 1 erro" de dados quase corretos — por exemplo, aceitar um identificador como válido mesmo com um único caractere de digitação errado no meio, decidindo greedily qual lado do primeiro erro "gastar" a tolerância.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
