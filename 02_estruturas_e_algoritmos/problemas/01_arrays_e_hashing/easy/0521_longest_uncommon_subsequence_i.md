# [0521] Longest Uncommon Subsequence I

> 🔗 [LeetCode 521](https://leetcode.com/problems/longest-uncommon-subsequence-i/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Trick` `#Easy`

## 📜 O Problema

Dadas duas strings `a` e `b`, retorne **o comprimento da maior subsequência incomum entre `a` e `b`**. Se não existir tal subsequência, retorne `-1`.

Uma **subsequência incomum** entre duas strings é uma string que é subsequência de **exatamente uma** delas.

**Exemplos:**
```
Input:  a = "aba", b = "cdc"
Output: 3
Explicação: uma subsequência incomum é "aba", pois é subsequência de "aba" mas não de "cdc".
Note que "cdc" também é uma subsequência incomum.

Input:  a = "aaa", b = "bbb"
Output: 3
Explicação: as subsequências incomuns mais longas são "aaa" e "bbb".

Input:  a = "aaa", b = "aaa"
Output: -1
Explicação: toda subsequência de a também é subsequência de b, e vice-versa. Logo a resposta é -1.
```

**Restrições (e o que elas denunciam):**
- `1 <= a.length, b.length <= 100` → entrada minúscula; a dificuldade real é perceber a observação, não a complexidade
- letras minúsculas apenas → sem preocupação de caixa

## 🧭 Como reconhecer o padrão

Quando o enunciado parece pedir um algoritmo sofisticado de subsequência (LCS, subsequência comum) mas o tamanho é pequeno e a resposta só tem alguns valores possíveis, desconfie de que há uma observação matemática simples escondida — esse é o "truque" clássico deste problema.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar todas as subsequências de `a`, verificar para cada uma se ela NÃO é subsequência de `b`, guardando a maior; repetir para `b`.

- Tempo: O(2^n) — o número de subsequências de uma string de tamanho n é exponencial · Espaço: O(2^n) para armazenar/gerar as subsequências
- **Por que não basta:** mesmo com n≤100, 2^100 é astronomicamente inviável; o problema exige enxergar que a resposta não depende de enumerar nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se `a == b`, toda subsequência de uma é subsequência da outra, então não existe subsequência "incomum" → responda `-1`. Se `a != b`, a própria string mais longa entre `a` e `b` já é uma subsequência incomum válida: uma string `X` só pode ser subsequência de outra string `Y` se `len(X) <= len(Y)`. Se os tamanhos são diferentes, a mais longa não cabe dentro da mais curta. Se os tamanhos são iguais mas as strings são diferentes, nenhuma pode ser subsequência da outra sem ser idêntica a ela. Em ambos os casos, `max(len(a), len(b))` é a resposta.

## 🎬 Exemplo passo a passo

`a = "aba"`, `b = "cdc"`

| Passo | Verificação | Resultado |
|---|---|---|
| 1 | a == b? | não ("aba" ≠ "cdc") |
| 2 | len(a) | 3 |
| 3 | len(b) | 3 |
| 4 | max(len(a), len(b)) | 3 |

Resultado final: `3` ✔ ("aba" em si é uma subsequência incomum, pois não é subsequência de "cdc")

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — só a comparação de igualdade das strings (que já é O(n) internamente)
- **Espaço:** O(1) extra

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findLUSlength(String a, String b) {
    // se as strings são idênticas, qualquer subsequência de uma também é da outra -> não existe "incomum"
    if (a.equals(b)) {
        return -1;
    }
    // se são diferentes, a própria string mais longa já não pode ser subsequência da outra
    return Math.max(a.length(), b.length());
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

- Tentar resolver com um algoritmo de LCS (longest common subsequence) — é o caminho errado; o problema não pede a subsequência comum, pede a incomum, e a solução real é O(1) depois da observação, não O(n·m).
- Esquecer o caso `a == b` — é a única situação em que a resposta é `-1`; qualquer outro caso sempre tem resposta.
- Achar que precisa comparar caractere por caractere para achar "onde" a diferença está — não precisa; a igualdade total (ou não) das strings já é suficiente para decidir.
- Confundir com "Longest Common Subsequence" ([1143]) — são problemas praticamente opostos em espírito, apesar do nome parecido.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Strings diferentes, mesmo tamanho | `a="aba", b="cdc"` | 3 | nenhuma é subsequência da outra |
| Strings idênticas | `a="aaa", b="aaa"` | -1 | toda subsequência de uma é da outra |
| Tamanhos diferentes | `a="aaa", b="bbb"` | 3 | mesmo raciocínio, mostra o caso de tamanhos iguais mas conteúdos diferentes |
| Uma é prefixo da outra | `a="ab", b="abc"` | 3 | "abc" não é subsequência de "ab" (mais curta), resposta é o maior comprimento |

## 🔗 Conexões

- Problemas irmãos: [1143] Longest Common Subsequence (problema "oposto" conceitualmente), [0522] Longest Uncommon Subsequence II (mesma ideia, mas com uma lista de N strings em vez de duas)
- No backend: o padrão de "enxergar a resposta com uma observação matemática em vez de força bruta" aparece sempre que uma solução ingênua é exponencial e os limites pequenos do problema sugerem outra leitura.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
