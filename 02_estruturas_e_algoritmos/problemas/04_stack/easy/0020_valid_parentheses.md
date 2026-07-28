# [0020] Valid Parentheses

> 🔗 [LeetCode 20](https://leetcode.com/problems/valid-parentheses/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` contendo apenas os caracteres `'('`, `')'`, `'{'`, `'}'`, `'['` e `']'`, determine se a string é válida.

Uma string é válida se: os parênteses de abertura são fechados pelo mesmo tipo de parênteses, e são fechados na ordem correta (cada fechamento corresponde à abertura mais recente ainda pendente).

**Exemplos:**
```
Input:  s = "()"
Output: true

Input:  s = "()[]{}"
Output: true

Input:  s = "(]"
Output: false

Input:  s = "([])"
Output: true

Input:  s = "([)]"
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^4` → tamanho pequeno, mas o esperado é O(n): uma única passada resolve, não precisa de nada quadrático
- `s` consiste apenas de `'()[]{}'` → não há necessidade de tratar outros caracteres; todo caractere é abertura ou fechamento

## 🧭 Como reconhecer o padrão

"Determinar se aninhamento de símbolos está balanceado" é a assinatura mais clássica de stack: cada abertura vira uma "pendência" que só pode ser resolvida pelo fechamento correspondente **mais recente** — exatamente o comportamento LIFO (last-in-first-out) de uma pilha.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Repetidamente procurar na string um par adjacente de abre-fecha válido (`"()"`, `"[]"` ou `"{}"`) e removê-lo, até não sobrar nenhum par para remover ou a string ficar vazia.

- Tempo: O(n²) · Espaço: O(n) — cada remoção pode exigir varrer a string de novo, e no pior caso há O(n) remoções
- **Por que não basta:** para `s` de até 10^4 caracteres, refazer a varredura completa a cada remoção degrada rápido; além disso simular "removeu, reconcatenou, procura de novo" é trabalhoso de implementar corretamente. Uma pilha resolve em uma única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra a string uma vez. Para cada caractere: se for uma **abertura**, empilhe. Se for um **fechamento**, ele só é válido se o topo da pilha for exatamente a abertura correspondente — nesse caso desempilhe; caso contrário (pilha vazia ou topo diferente), a string já é inválida. No final, a string só é válida se a pilha ficou vazia (nenhuma abertura ficou pendente sem fechar).

## 🎬 Exemplo passo a passo

`s = "([)]"`

| Passo | Caractere | Ação | Pilha após |
|---|---|---|---|
| 1 | `(` | abertura → empilha | `[(]` |
| 2 | `[` | abertura → empilha | `[(, []` |
| 3 | `)` | fechamento → topo é `[`, esperado `(` → **não bate** | — retorna `false` imediatamente |

Resultado final: `false` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string, cada caractere é empilhado/desempilhado no máximo uma vez
- **Espaço:** O(n) — pior caso, string só com aberturas (ex.: `"((((("`), todas ficam na pilha

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isValid(String s) {
    Deque<Character> pilha = new ArrayDeque<>(); // ArrayDeque, não Stack legado
    Map<Character, Character> pares = Map.of(')', '(', ']', '[', '}', '{');

    for (char c : s.toCharArray()) {
        if (pares.containsKey(c)) {              // é um fechamento
            // pilha vazia = fechamento sem abertura pendente; ou topo não bate com o par esperado
            if (pilha.isEmpty() || pilha.pop() != pares.get(c)) {
                return false;
            }
        } else {                                 // é uma abertura: vira pendência
            pilha.push(c);
        }
    }

    return pilha.isEmpty(); // sobrou pendência sem fechar = inválido
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

- Chamar `pop()`/`peek()` numa pilha vazia sem checar antes — em `"]"` sozinho, a pilha está vazia no primeiro fechamento; sempre valide `isEmpty()` antes de desempilhar.
- Verificar só a **contagem** de aberturas e fechamentos, ignorando a **ordem** — `"([)]"` tem 2 aberturas e 2 fechamentos de cada tipo, mas é inválido porque a ordem de fechamento está errada; só uma pilha (ordem LIFO) captura isso.
- Esquecer de checar se a pilha ficou vazia no final — `"((("` nunca falha durante o loop (nenhum fechamento aparece), mas termina com pendência: sem o `return pilha.isEmpty()` final, o código erroneamente aceitaria como válido.
- Usar `java.util.Stack` (classe legada e sincronizada, mais lenta) em vez de `ArrayDeque` como pilha em Java.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só aberturas | `"((("` | false | pilha não fica vazia no final |
| Só um fechamento | `"]"` | false | pilha vazia no momento do fechamento |
| Tipos intercalados corretamente | `"{[]}"` | true | cada fechamento bate com a abertura mais recente |
| Ordem errada (mesmos tipos) | `"([)]"` | false | contagem bate, mas LIFO é violado |
| String vazia é impossível aqui | — | — | restrição garante `length >= 1`, não precisa tratar `""` |

## 🔗 Conexões

- Problemas irmãos: [1021] Remove Outermost Parentheses (mesma ideia de rastrear profundidade de parênteses), [1614] Maximum Nesting Depth of the Parentheses (contagem de profundidade sem precisar de pilha explícita), [0032] Longest Valid Parentheses (stack de índices para achar o maior trecho válido)
- No backend: validação de aninhamento aparece em parsers de JSON/XML, em compiladores (checagem de blocos `{ }` e parênteses de expressões), e em qualquer validador de sintaxe que precise garantir que delimitadores fecham na ordem certa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
