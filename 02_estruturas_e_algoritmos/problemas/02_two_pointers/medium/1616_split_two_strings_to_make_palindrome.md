# [1616] Split Two Strings to Make Palindrome

> 🔗 [LeetCode 1616](https://leetcode.com/problems/split-two-strings-to-make-palindrome/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Medium`

## 📜 O Problema

Dadas duas strings `a` e `b` de mesmo tamanho, escolha um índice de corte e divida **as duas no mesmo ponto**: `a = aprefix + asuffix`, `b = bprefix + bsuffix`. Verifique se `aprefix + bsuffix` OU `bprefix + asuffix` forma um palíndromo, para **algum** ponto de corte.

**Exemplos:**
```
Input:  a = "x", b = "y"
Output: true
Explicação: corte vazio: "" + "y" = "y", palíndromo.

Input:  a = "xbdef", b = "xecab"
Output: false

Input:  a = "ulacfd", b = "jizalu"
Output: true
Explicação: corte em índice 3: "ula" + "alu" = "ulaalu", palíndromo.
```

**Restrições (e o que elas denunciam):**
- `1 <= a.length == b.length <= 10^5` → O(n²) (testar todo corte) é arriscado; O(n) é o esperado
- O corte é **compartilhado** entre as duas strings → não são duas escolhas independentes, é um único índice `k` aplicado aos dois
- Duas combinações possíveis (`aprefix+bsuffix` ou `bprefix+asuffix`) → dobra o trabalho, mas de forma simétrica

## 🧭 Como reconhecer o padrão

"Encontrar um ponto de corte que torna uma combinação de duas metades um palíndromo" usa dois ponteiros nas pontas de `a` e `b` **cruzados**: um em `a` pela esquerda, outro em `b` pela direita, avançando enquanto os caracteres coincidem — isso identifica até onde qualquer corte funcionaria; o que sobra no meio só precisa ser palíndromo usando **uma das duas strings sozinha**.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada possível índice de corte `k` (de `0` até `n`), montar `aprefix+bsuffix` e `bprefix+asuffix` como strings novas, e checar se alguma delas é palíndromo.

- Tempo: O(n²) — `n` cortes possíveis, cada checagem de palíndromo é O(n) · Espaço: O(n) por candidato montado
- **Por que não basta:** testa todo corte possível, mesmo que a maioria nunca pudesse formar um palíndromo; convergindo de fora pra dentro com dois ponteiros, o algoritmo identifica de uma vez só até onde as bordas "cruzadas" continuam batendo, sem testar corte por corte.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para checar se existe um corte que torna `aprefix + bsuffix` palíndromo: use `i` no início de `a` e `j` no fim de `b`, avançando enquanto `a[i] == b[j]` — cada acerto significa que aquele par de posições "espelhadas" já está garantido, não importa onde exatamente o corte caia (contanto que caia entre eles). Quando `a[i] != b[j]` (ou os ponteiros se cruzam), o corte só pode estar **antes de `i`** (o miolo restante vem todo de `b`) ou **depois de `j`** (o miolo vem todo de `a`) — por isso a resposta é `isPalindromeRange(a, i, j) OU isPalindromeRange(b, i, j)`. Repita trocando os papéis de `a` e `b` para cobrir a segunda combinação (`bprefix+asuffix`).

## 🎬 Exemplo passo a passo

Checando `aprefix + bsuffix` para `a = "ulacfd"`, `b = "jizalu"` (n=6)

| Passo | i | j | a[i] | b[j] | Iguais? | Ação |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | `u` | `u` | sim | avança: i=1, j=4 |
| 2 | 1 | 4 | `l` | `l` | sim | avança: i=2, j=3 |
| 3 | 2 | 3 | `a` | `a` | sim | avança: i=3, j=2 |
| 4 | 3 | 2 | — | — | `i >= j` | loop termina, intervalo vazio é palíndromo por vacuidade → **true** |

Como essa primeira checagem já deu `true`, nem é preciso testar a combinação `bprefix+asuffix` — resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — a convergência dos ponteiros e a checagem final de palíndromo, juntas, tocam cada posição no máximo uma vez, para cada uma das duas chamadas (`check(a,b)` e `check(b,a)`)
- **Espaço:** O(1) — só os índices dos ponteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean checkPalindromeFormation(String a, String b) {
    return check(a, b) || check(b, a); // as duas combinações possíveis de prefixo/sufixo
}

private boolean check(String a, String b) {
    int i = 0;
    int j = a.length() - 1;
    // avança enquanto os caracteres "cruzados" (a pela esquerda, b pela direita) coincidem
    while (i < j && a.charAt(i) == b.charAt(j)) {
        i++;
        j--;
    }
    // no ponto de mismatch (ou fim), o "miolo" restante precisa ser palíndromo
    // usando SÓ a ou SÓ b (as duas únicas posições possíveis pro corte)
    return isPalindromeRange(a, i, j) || isPalindromeRange(b, i, j);
}

private boolean isPalindromeRange(String s, int left, int right) {
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

- Esquecer de testar as DUAS combinações — `aprefix+bsuffix` e `bprefix+asuffix` são escolhas independentes; `check(a,b) || check(b,a)` cobre as duas (a segunda chamada troca os papéis).
- Confundir qual string checar no "miolo" — depois do mismatch em `(i,j)`, o corte só pode estar ANTES de `i` (miolo vem todo de `b`) ou DEPOIS de `j` (miolo vem todo de `a`); nunca uma mistura dos dois no meio.
- Achar que o loop de convergência (`a[i]==b[j]`) sozinho já determina a resposta — ele só encontra até onde dá pra "cruzar" as bordas; a resposta final ainda depende de checar se o que sobra no meio é palíndromo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Qualquer split serve | `a="x"`, `b="y"` | true | corte vazio: `""+"y"`, já é palíndromo trivial |
| Sem split possível | `a="xbdef"`, `b="xecab"` | false | nenhuma combinação de corte gera palíndromo |
| Split no meio | `a="ulacfd"`, `b="jizalu"` | true | corte em k=3 forma `"ulaalu"` |
| Strings já palíndromas isoladamente | `a="aba"`, `b="xyz"` | true | usar `a` inteira (miolo = `a` inteiro) já resolve |

## 🔗 Conexões

- Problemas irmãos: [0125] Valid Palindrome (mesma checagem de palíndromo com dois ponteiros, usada aqui como sub-rotina), [0680] Valid Palindrome II (mesma família de "quebrar" um quase-palíndromo até um ponto de decisão)
- No backend: validar se dois streams de dados relacionados podem ser combinados num único registro consistente, escolhendo um ponto de corte comum — útil em reconciliação de dados vindos de duas fontes que precisam "casar" numa fronteira específica.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
