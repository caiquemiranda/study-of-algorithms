# [2396] Strictly Palindromic Number

> 🔗 [LeetCode 2396](https://leetcode.com/problems/strictly-palindromic-number/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Math` `#Medium`

## 📜 O Problema

Um inteiro `n` é **estritamente palindrômico** se, para **toda** base `b` entre `2` e `n-2` (inclusive), a representação de `n` nessa base for um palíndromo. Dado `n`, retorne se ele é estritamente palindrômico.

**Exemplos:**
```
Input:  n = 9
Output: false
Explicação: 9 em base 2 = "1001" (palíndromo), mas em base 3 = "100" (não é palíndromo).

Input:  n = 4
Output: false
Explicação: 4 em base 2 = "100", não é palíndromo.
```

**Restrições (e o que elas denunciam):**
- `4 <= n <= 10^5` → sugere testar todas as bases de `2` até `n-2`, convertendo e checando palíndromo em cada uma
- "Para TODA base" → basta UMA base falhar pra já responder `false`, permitindo parar cedo

## 🧭 Como reconhecer o padrão

"Verificar se a representação de um número numa base é palíndromo" é a mesma checagem de [0125] Valid Palindrome aplicada a uma sequência de dígitos em vez de caracteres — dois ponteiros nas pontas dos dígitos, convergindo pro centro.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada base `b`, converter `n` para uma string de dígitos nessa base, gerar a versão revertida dessa string, e comparar as duas.

- Tempo: O(n log n) — até `n-4` bases, cada conversão e reversão custando O(log n) dígitos · Espaço: O(log n) por base testada
- **Por que não basta:** funciona, mas cria uma cópia revertida a cada base testada; dois ponteiros comparam os dígitos diretamente, sem nunca gerar essa cópia.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada base `b` de `2` a `n-2`, converta `n` para um array de dígitos nessa base (divisões sucessivas por `b`). Use dois ponteiros nas pontas do array de dígitos para checar se é palíndromo, exatamente como em [0125]. Se qualquer base falhar, pare imediatamente e retorne `false`.

**A virada de mesa:** existe uma prova matemática que torna essa checagem toda desnecessária. Na base `b = n - 2` (que está sempre dentro do intervalo testado, para qualquer `n >= 5`), `n` se escreve como `1 * (n-2) + 2` — ou seja, os dígitos são sempre `[1, 2]`, e `1 != 2` nunca é palíndromo. Para `n = 4`, a única base testada é `b=2`, e `4` em binário é `"100"`, também não palíndromo. **Conclusão: dentro da constraint do problema (`n >= 4`), a resposta é SEMPRE `false`** — a solução verdadeiramente ótima é `return false;` em O(1), sem converter nem comparar nada.

## 🎬 Exemplo passo a passo

`n = 9` (demonstrando a checagem base a base, antes de aplicar o atalho matemático)

| Passo | base b | dígitos de n | Checagem com dois ponteiros | Resultado |
|---|---|---|---|---|
| 1 | 2 | `[1,0,0,1]` | `left=0('1')` = `right=3('1')`; `left=1('0')` = `right=2('0')`; convergem sem mismatch | é palíndromo, continua pra próxima base |
| 2 | 3 | `[1,0,0]` | `left=0('1')` ≠ `right=2('0')` | NÃO é palíndromo → **retorna false** |

Resultado final: `false` ✔ (bate com o enunciado — nem precisou testar as bases 4 a 7)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) — usando o atalho matemático (`return false` direto); O(n log n) se implementar a checagem completa sem a observação
- **Espaço:** O(1) no atalho; O(log n) por base se implementar a checagem completa

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isStrictlyPalindromic(int n) {
    // prova matemática: na base (n-2), n sempre vira os dígitos [1, 2] (1 != 2),
    // e para n=4 a única base testada (b=2) já falha ("100" não é palíndromo);
    // logo, nenhum n >= 4 nunca passa em TODAS as bases — a resposta é sempre false
    return false;
}

// checagem completa (não necessária dada a prova acima, mas é a técnica de dois
// ponteiros que este problema pretende ensinar)
private boolean isPalindromicInBase(int n, int base) {
    List<Integer> digits = new ArrayList<>();
    int num = n;
    while (num > 0) {
        digits.add(num % base);
        num /= base;
    }

    int left = 0;
    int right = digits.size() - 1;
    while (left < right) {
        if (!digits.get(left).equals(digits.get(right))) {
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

- Implementar a checagem completa (loop por todas as bases) sem perceber que a resposta é sempre `false` — não é um erro de lógica, mas é um desperdício de esforço; vale sempre procurar esse tipo de "prova escondida" em problemas que pedem "para TODO x, verifique Y".
- Errar o intervalo de bases — é `2` até `n-2` **inclusive**; usar `n-1` ou esquecer o `-2` muda quais bases são testadas (embora, dada a prova, isso não mude a resposta final para este problema específico).
- Esquecer que `n=4` só testa a base `2` (intervalo `[2, n-2] = [2, 2]`) — um caso de borda que precisa ser tratado se implementar a checagem completa sem o atalho.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo do enunciado | `n=9` | false | falha já na base 3 |
| Menor valor da constraint | `n=4` | false | falha na única base testada (2) |
| Valor grande | `n=99999` | false | a prova matemática cobre todo o domínio da constraint |
| Qualquer `n >= 4` | `n=` qualquer valor válido | false | não existe contraexemplo dentro de `4 <= n <= 10^5` |

## 🔗 Conexões

- Problemas irmãos: [0125] Valid Palindrome (mesma técnica de checagem com dois ponteiros, aqui aplicada a dígitos em vez de caracteres), [1332] Remove Palindromic Subsequences (mesma família de problema onde uma prova matemática reduz drasticamente o espaço de respostas possíveis)
- No backend: reconhecer quando uma validação aparentemente cara ("para todo X, verifique Y") esconde uma prova que torna a resposta constante — evita implementar e rodar uma checagem cara em produção quando ela sempre daria o mesmo resultado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
