# [1021] Remove Outermost Parentheses

> 🔗 [LeetCode 1021](https://leetcode.com/problems/remove-outermost-parentheses/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#String` `#Easy`

## 📜 O Problema

Uma string de parênteses válida é vazia (`""`), ou `"(" + A + ")"`, ou `A + B`, onde `A` e `B` também são strings de parênteses válidas.

Uma string válida `s` é **primitiva** se ela é não vazia e não existe forma de dividi-la em `s = A + B` com `A` e `B` ambas não vazias e válidas.

Dada uma string válida `s`, considere sua decomposição primitiva: `s = P1 + P2 + ... + Pk`. Retorne `s` após remover os parênteses mais externos de **cada** `Pi` da decomposição.

**Exemplos:**
```
Input:  s = "(()())(())"
Output: "()()()"
Explicação: decomposição primitiva "(()())" + "(())".
Removendo os parênteses externos de cada uma: "()()" + "()" = "()()()".

Input:  s = "(()())(())(()(()))"
Output: "()()()()(())"

Input:  s = "()()"
Output: ""
Explicação: decomposição "()" + "()". Removendo os externos de cada uma: "" + "" = "".
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → precisa de solução O(n); nada de reconstruir a string repetidamente
- `s[i]` é `'('` ou `')'` → só dois caracteres possíveis, simplifica a lógica de decisão
- `s` é garantidamente uma string de parênteses válida → não é preciso validar balanceamento, só rastrear profundidade

## 🧭 Como reconhecer o padrão

"Remover o par de parênteses mais externo de cada bloco primitivo" é sobre rastrear **profundidade de aninhamento**: o parêntese mais externo de um bloco primitivo é sempre o que está no nível de profundidade 0 → 1 (abertura) ou 1 → 0 (fechamento). Isso é a mesma ideia de contagem de profundidade que sustenta uma pilha de parênteses — na prática, um contador de profundidade já é suficiente aqui, mas o raciocínio de "cada abertura empilha, cada fechamento desempilha" é o mesmo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Encontre cada bloco primitivo separadamente (rastreando quando o contador de parênteses abertos volta a zero para marcar o fim de um bloco), depois para cada bloco remova manualmente o primeiro e o último caractere e concatene os resultados numa nova string.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** essa abordagem já é O(n), mas costuma ser implementada com fatiamento de substrings (`substring()`) a cada bloco encontrado, o que gera cópias intermediárias desnecessárias. A solução ótima decide, caractere a caractere, se ele deve ou não entrar no resultado — sem nunca precisar isolar blocos manualmente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um contador `profundidade` que sobe a cada `'('` e desce a cada `')'`. A observação central: o parêntese mais **externo** de cada bloco primitivo é exatamente aquele que faz a profundidade **sair de 0** (abertura, profundidade 0→1) ou **voltar para 0** (fechamento, profundidade 1→0). Todo outro parêntese — os que ocorrem com profundidade ≥ 1 antes e depois da operação — é "interno" e deve ser mantido. Então: para cada `'('`, inclua-o no resultado só se a profundidade **antes** de incrementar já não era 0 (ou seja, incremente primeiro e verifique se o novo valor é > 1); para cada `')'`, inclua-o só se a profundidade **antes** de decrementar era > 1.

## 🎬 Exemplo passo a passo

`s = "(()())(())"`

| Passo | Caractere | Profundidade antes → depois | É externo? | Vai pro resultado? | Resultado parcial |
|---|---|---|---|---|---|
| 1 | `(` | 0 → 1 | sim (abre bloco) | não | `` |
| 2 | `(` | 1 → 2 | não | sim | `(` |
| 3 | `)` | 2 → 1 | não | sim | `()` |
| 4 | `(` | 1 → 2 | não | sim | `()(` |
| 5 | `)` | 2 → 1 | não | sim | `()()` |
| 6 | `)` | 1 → 0 | sim (fecha bloco) | não | `()()` |
| 7 | `(` | 0 → 1 | sim (abre bloco) | não | `()()` |
| 8 | `(` | 1 → 2 | não | sim | `()()(` |
| 9 | `)` | 2 → 1 | não | sim | `()()()` |
| 10 | `)` | 1 → 0 | sim (fecha bloco) | não | `()()()` |

Resultado final: `"()()()"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string, decisão O(1) por caractere
- **Espaço:** O(n) — para construir a string de resultado (não conta como espaço "extra" de análise, já que é a própria saída); O(1) de espaço auxiliar além disso (só o contador de profundidade)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String removeOuterParentheses(String s) {
    StringBuilder resultado = new StringBuilder();
    int profundidade = 0;

    for (char c : s.toCharArray()) {
        if (c == '(') {
            if (profundidade > 0) {          // não é o externo (profundidade já era >= 1 antes de abrir)
                resultado.append(c);
            }
            profundidade++;
        } else { // c == ')'
            profundidade--;
            if (profundidade > 0) {          // não é o externo (ainda sobra profundidade depois de fechar)
                resultado.append(c);
            }
        }
    }

    return resultado.toString();
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

- Checar a profundidade **depois** de incrementar/decrementar de forma errada — para `'('`, a checagem certa é "profundidade **antes** de incrementar > 0" (equivalente ao código acima, que testa antes do `profundidade++`); inverter a ordem do incremento e da checagem quebra a lógica.
- Confundir a condição de `'('` com a de `')'` — ambas usam `profundidade > 0`, mas uma é testada **antes** de incrementar e a outra **depois** de decrementar; copiar a mesma condição sem ajustar a ordem das operações gera off-by-one.
- Tentar resolver com uma pilha explícita de caracteres — funciona, mas é over-engineering: como você só precisa saber a **profundidade numérica**, não o conteúdo empilhado, um contador inteiro é suficiente e mais simples.
- Esquecer que a entrada já é garantida válida — não é preciso checar `profundidade < 0` ou string desbalanceada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único bloco primitivo simples | `"()"` | `""` | remove o único par, que é totalmente externo |
| Blocos aninhados profundamente | `"((()))"` | `"(())"` | só o par mais externo (profundidade 0↔1) é removido, os 2 internos ficam |
| Múltiplos blocos primitivos vazios por dentro | `"()()"` | `""` | cada bloco é `"()"`, sem conteúdo interno a preservar |
| Mistura de blocos simples e aninhados | `"(()(()))"` | `"()(())"` | testa que a lógica generaliza para blocos únicos com múltiplos níveis internos |

## 🔗 Conexões

- Problemas irmãos: [0020] Valid Parentheses (mesma família de rastrear parênteses, mas validando em vez de remover), [1614] Maximum Nesting Depth of the Parentheses (mesmo contador de profundidade, usado para achar o máximo em vez de filtrar caracteres)
- No backend: rastrear profundidade de aninhamento sem guardar o conteúdo aparece em parsers que só precisam saber "em que nível de indentação/bloco estou" (ex.: parsers de JSON minificando ou reformatando estrutura, ou detecção de nível de aninhamento em templates HTML/XML).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
