# [1614] Maximum Nesting Depth of the Parentheses

> 🔗 [LeetCode 1614](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Easy`

## 📜 O Problema

Dada uma **string de parênteses válida** (VPS) `s`, retorne a profundidade de aninhamento de `s` — o número **máximo** de parênteses aninhados.

**Exemplos:**
```
Input:  s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explicação: o dígito 8 está dentro de 3 parênteses aninhados na string.

Input:  s = "(1)+((2))+(((3)))"
Output: 3
Explicação: o dígito 3 está dentro de 3 parênteses aninhados na string.

Input:  s = "()(())((()()))"
Output: 3
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → tamanho minúsculo, qualquer solução O(n) é folgada
- `s` consiste de dígitos `0-9` e caracteres `'+' '-' '*' '/' '(' ')'` → só os parênteses importam para a profundidade; os demais caracteres são "ruído" que deve ser ignorado
- É garantido que `s` é uma VPS (expressão de parênteses válida) → não é preciso validar balanceamento, só rastrear a profundidade máxima atingida

## 🧭 Como reconhecer o padrão

"Encontrar a profundidade **máxima** de aninhamento de parênteses" é a mesma ideia de contador de profundidade usada em [1021] Remove Outermost Parentheses: cada `'('` aumenta o nível, cada `')'` diminui. Aqui, em vez de decidir o que manter na string, você só precisa guardar o **maior valor** que esse contador atingiu durante toda a passada — um contador simples já captura o que uma pilha de parênteses faria, sem precisar empilhar nada de fato.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar uma pilha real: empilhar um marcador a cada `'('`, desempilhar a cada `')'`, e a cada empilhamento comparar o tamanho da pilha com o máximo guardado até agora.

- Tempo: O(n) · Espaço: O(n) — a pilha guarda até `n/2` marcadores no pior caso
- **Por que não basta:** essa abordagem já é O(n) em tempo, mas gasta espaço O(n) desnecessário — como você só precisa saber o **tamanho** que a pilha teria em cada momento (não o que está empilhado), um contador inteiro substitui a pilha inteira sem perder nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` uma vez com um contador `profundidade` começando em 0 e um `maximo` começando em 0. Para cada `'('`: incremente `profundidade` e atualize `maximo = max(maximo, profundidade)`. Para cada `')'`: decremente `profundidade`. Ignore qualquer outro caractere (dígitos e operadores não afetam o aninhamento). No final, `maximo` é a resposta.

## 🎬 Exemplo passo a passo

`s = "(1+(2*3)+((8)/4))+1"` (mostrando só os caracteres relevantes: parênteses)

| Passo | Caractere | Ação | profundidade após | máximo após |
|---|---|---|---|---|
| 1 | `(` | incrementa | 1 | 1 |
| 2 | `(` (antes de `2*3)`) | incrementa | 2 | 2 |
| 3 | `)` (fecha `2*3`) | decrementa | 1 | 2 |
| 4 | `(` (antes de `(8)`) | incrementa | 2 | 2 |
| 5 | `(` (antes de `8`) | incrementa | 3 | **3** |
| 6 | `)` (fecha `8`) | decrementa | 2 | 3 |
| 7 | `)` (fecha o segundo bloco) | decrementa | 1 | 3 |
| 8 | `)` (fecha o primeiro bloco) | decrementa | 0 | 3 |

Resultado final: `3` ✔ (bate com o enunciado — o dígito 8 estava no nível 3)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string
- **Espaço:** O(1) — só dois contadores inteiros, independente do tamanho de `s`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxDepth(String s) {
    int profundidade = 0;
    int maximo = 0;

    for (char c : s.toCharArray()) {
        if (c == '(') {
            profundidade++;
            maximo = Math.max(maximo, profundidade); // captura o pico logo ao abrir
        } else if (c == ')') {
            profundidade--;
        }
        // dígitos e operadores (+, -, *, /) são ignorados: não afetam aninhamento
    }

    return maximo;
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

- Atualizar `maximo` **depois** de decrementar em `')'` em vez de só ao incrementar em `'('` — a profundidade máxima só pode crescer ao abrir um parêntese; atualizar no fechamento não captura nada de novo e é trabalho redundante (mas não incorreto, já que o valor só decresce ali).
- Esquecer de ignorar dígitos e operadores — tentar tratá-los como se afetassem a profundidade quebra a contagem; a regra é simples: só `'('` e `')'` importam.
- Usar uma pilha real (guardando elementos) quando só o **tamanho** da pilha em cada instante importa — funciona, mas desperdiça O(n) de espaço sem necessidade.
- Confundir "profundidade máxima" com "número total de parênteses" — `"()()()"` tem 3 pares mas profundidade máxima 1 (nunca aninham), enquanto `"((()))"` tem 3 pares com profundidade máxima 3 (todos aninhados).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem aninhamento, só sequência | `"()()()"` | 1 | os pares são irmãos, nunca aninham entre si |
| Aninhamento total | `"((()))"` | 3 | cada parêntese aninha dentro do anterior |
| Mistura de aninhado e sequencial | `"()(())((()()))"` | 3 | o pico de profundidade ocorre no bloco mais interno do último grupo |
| Só dígitos, sem parênteses | (não ocorre pela restrição, mas ilustra) `"123"` | 0 | nenhum `'('` significa que a profundidade nunca sai de 0 |

## 🔗 Conexões

- Problemas irmãos: [1021] Remove Outermost Parentheses (mesmo contador de profundidade, usado para filtrar caracteres em vez de achar o pico), [0020] Valid Parentheses (mesma família de rastrear parênteses, mas validando balanceamento com pilha real)
- No backend: contadores de profundidade de aninhamento aparecem em analisadores de complexidade ciclomática de código (medir quantos `if`/`for` estão aninhados), em detecção de nível máximo de indentação de configs YAML/JSON, e em qualquer ferramenta de lint que precise reportar "aninhamento excessivo" sem precisar materializar a árvore inteira.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
