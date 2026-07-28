# [2697] Lexicographically Smallest Palindrome

> 🔗 [LeetCode 2697](https://leetcode.com/problems/lexicographically-smallest-palindrome/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Greedy` `#Easy`

## 📜 O Problema

Dada uma string `s`, você pode substituir qualquer caractere por outro. Torne `s` um palíndromo com o **mínimo** de operações; se houver mais de um palíndromo possível com esse mínimo, retorne o **lexicograficamente menor**.

**Exemplos:**
```
Input:  s = "egcfe"
Output: "efcfe"
Explicação: 1 operação (trocar 'g' por 'f').

Input:  s = "abcd"
Output: "abba"
Explicação: 2 operações.

Input:  s = "seven"
Output: "neven"
Explicação: 1 operação (trocar 's' por 'n').
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 1000` → O(n) esperado
- Precisa ser o **mínimo** de operações E o **lexicograficamente menor** entre os empates → duas exigências simultâneas, mas que acabam sendo resolvidas pela mesma decisão gulosa em cada par de posições

## 🧭 Como reconhecer o padrão

"Consertar um quase-palíndromo com o mínimo de mudanças, escolhendo o resultado lexicograficamente menor" usa dois ponteiros nas pontas convergindo pro centro — igual à checagem de [0125] Valid Palindrome, mas aqui, em vez de só comparar, cada par que diverge é **corrigido** escolhendo o menor dos dois caracteres para as duas posições (garante o mínimo de 1 troca por par E o menor valor possível).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de posições que diverge, considerar as duas possibilidades (igualar ambas ao caractere da esquerda, ou ambas ao da direita); testar as até `2^k` combinações possíveis (k = número de pares divergentes) e escolher a que gera a string lexicograficamente menor.

- Tempo: O(2^k × n) — exponencial no número de pares divergentes · Espaço: O(n) por candidato gerado
- **Por que não basta:** a escolha em cada par é totalmente **independente** das escolhas nos outros pares — mudar a decisão de um par não afeta se outro fica lexicograficamente menor. Um algoritmo guloso que decide cada par isoladamente já é ótimo; não há necessidade de testar combinações.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no início e `right` no fim. Sempre que `s[left] != s[right]`, escolha o **menor** dos dois caracteres e atribua-o às duas posições — isso resolve o par com exatamente 1 troca (mínimo possível) e garante o menor valor possível ali. Se já forem iguais, não faça nada (qualquer troca ali aumentaria o número de operações sem necessidade). Avance os dois ponteiros pra dentro até se cruzarem.

## 🎬 Exemplo passo a passo

`s = "egcfe"` (índices 0 a 4: `e,g,c,f,e`)

| Passo | left (valor) | right (valor) | Iguais? | Ação | Array depois |
|---|---|---|---|---|---|
| 1 | 0 (`e`) | 4 (`e`) | sim | nada muda | `[e,g,c,f,e]` |
| 2 | 1 (`g`) | 3 (`f`) | não | escolhe o menor `'f'`; `arr[1]='f'`, `arr[3]='f'` | `[e,f,c,f,e]` |
| 3 | 2 | 2 | — | `left == right` (meio), loop termina | `[e,f,c,f,e]` |

Resultado final: `"efcfe"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — os dois ponteiros juntos percorrem a string uma única vez
- **Espaço:** O(n) para o `char[]` (necessário em Java por strings serem imutáveis); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String makeSmallestPalindrome(String s) {
    char[] arr = s.toCharArray();
    int left = 0;
    int right = arr.length - 1;

    while (left < right) {
        if (arr[left] != arr[right]) {
            // escolhe o menor dos dois: garante mínimo de trocas E menor valor lexicográfico
            char menor = (char) Math.min(arr[left], arr[right]);
            arr[left] = menor;
            arr[right] = menor;
        }
        left++;
        right--;
    }

    return new String(arr);
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

- Escolher o caractere MAIOR entre os dois em vez do MENOR — ainda produz um palíndromo com o mínimo de trocas, mas não o lexicograficamente menor exigido pelo enunciado.
- Trocar só UM dos dois lados sem considerar qual dos dois é menor (ex.: sempre ajustar `right` para ficar igual a `left`) — pode preservar um caractere maior à esquerda quando o da direita era menor, perdendo a otimalidade lexicográfica.
- Trocar caracteres que já são iguais "por garantia" — isso aumentaria o número de operações além do mínimo necessário, violando a primeira exigência do enunciado (mínimo de operações antes de minimizar lexicograficamente).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um mismatch | `"egcfe"` | `"efcfe"` | só o par (g,f) diverge, escolhe o menor `'f'` |
| Múltiplos mismatches | `"abcd"` | `"abba"` | dois pares divergentes, tamanho par (sem meio) |
| Mismatch perto do início | `"seven"` | `"neven"` | par (s,n) diverge, escolhe `'n'` |
| Já é palíndromo | `"aba"` | `"aba"` | nenhum mismatch, nenhuma operação necessária |

## 🔗 Conexões

- Problemas irmãos: [0125] Valid Palindrome (mesma convergência de ponteiros nas pontas, mas só verificando em vez de construir), [0680] Valid Palindrome II (mesma família de "consertar" um quase-palíndromo com o mínimo de mudanças)
- No backend: normalizar registros para satisfazer uma restrição de simetria/consistência com o mínimo de alterações e a menor mudança possível em cada campo — por exemplo, reconciliar dois campos espelhados de um registro escolhendo sempre o valor "canônico" mais conservador entre os dois.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
