# [0150] Evaluate Reverse Polish Notation

> 🔗 [LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Array` `#Math`

## 📜 O Problema

Você recebe um array de strings `tokens` representando uma expressão aritmética em **notação polonesa reversa** (RPN). Avalie a expressão e retorne o resultado inteiro.

Os operadores válidos são `'+'`, `'-'`, `'*'` e `'/'`. Cada operando pode ser um inteiro ou outra sub-expressão. A divisão entre inteiros sempre **trunca em direção a zero**. Não há divisão por zero. A entrada é sempre uma expressão RPN válida.

**Exemplos:**
```
Input:  tokens = ["2","1","+","3","*"]
Output: 9
Explicação: ((2 + 1) * 3) = 9

Input:  tokens = ["4","13","5","/","+"]
Output: 6
Explicação: (4 + (13 / 5)) = 6

Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

**Restrições (e o que elas denunciam):**
- `1 <= tokens.length <= 10^4` → precisa de solução O(n); nada de reprocessar a expressão inteira várias vezes
- `tokens[i]` é um operador ou um inteiro em `[-200, 200]` → valores pequenos, mas resultados intermediários podem crescer com as operações; o enunciado garante que tudo cabe em 32 bits, então não é preciso tratar overflow manualmente
- Não há divisão por zero e a expressão é sempre válida → não é preciso validar a estrutura da RPN nem tratar erros aritméticos

## 🧭 Como reconhecer o padrão

RPN é a assinatura clássica de avaliação com pilha: como os operandos vêm **antes** do operador (ao contrário da notação infixa `"2 + 1"`), você só sabe que precisa combinar dois valores quando encontra o operador — e os dois valores a combinar são sempre os **últimos dois processados**, exatamente o topo da pilha.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Tentar converter a expressão RPN para notação infixa (adicionando parênteses e reordenando operadores) e depois usar um parser de expressões matemáticas convencional para avaliar.

- Tempo: O(n) na conversão, mas com uma constante bem maior e complexidade de implementação alta · Espaço: O(n)
- **Por que não basta:** converter RPN para infixa é desnecessariamente complexo — RPN foi desenhada justamente para ser avaliada diretamente, sem precisar de parênteses ou regras de precedência de operadores. Uma pilha resolve isso numa única passada, sem nenhuma conversão intermediária.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra os tokens da esquerda para a direita com uma pilha de operandos. Para cada token: se for um número, empilhe-o. Se for um operador, desempilhe os **dois** valores mais recentes (o penúltimo empilhado é o operando da esquerda, o último é o da direita — a ordem importa para `-` e `/`), aplique a operação, e empilhe o resultado de volta. Ao final de todos os tokens, sobra exatamente um valor na pilha: o resultado da expressão inteira.

## 🎬 Exemplo passo a passo

`tokens = ["4","13","5","/","+"]`

| Passo | Token | Ação | Pilha após |
|---|---|---|---|
| 1 | `"4"` | número → empilha | `[4]` |
| 2 | `"13"` | número → empilha | `[4, 13]` |
| 3 | `"5"` | número → empilha | `[4, 13, 5]` |
| 4 | `"/"` | operador → desempilha `5` (direita) e `13` (esquerda), calcula `13 / 5 = 2` (trunca em direção a zero), empilha | `[4, 2]` |
| 5 | `"+"` | operador → desempilha `2` (direita) e `4` (esquerda), calcula `4 + 2 = 6`, empilha | `[6]` |

Resultado final: `6` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada token é processado uma única vez, com operações O(1) de pilha
- **Espaço:** O(n) — pior caso, todos os tokens são números antes de qualquer operador (embora a RPN válida limite isso na prática, o pior caso teórico da pilha ainda é O(n))

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int evalRPN(String[] tokens) {
    Deque<Integer> pilha = new ArrayDeque<>();
    Set<String> operadores = Set.of("+", "-", "*", "/");

    for (String token : tokens) {
        if (operadores.contains(token)) {
            int direita = pilha.pop();  // o segundo operando empilhado é sempre o da direita
            int esquerda = pilha.pop(); // o primeiro é o da esquerda
            int resultado = switch (token) {
                case "+" -> esquerda + direita;
                case "-" -> esquerda - direita;
                case "*" -> esquerda * direita;
                default -> esquerda / direita; // "/" — divisão inteira de Java já trunca em direção a zero
            };
            pilha.push(resultado);
        } else {
            pilha.push(Integer.parseInt(token)); // token é um número (inclui negativos, ex.: "-11")
        }
    }

    return pilha.pop(); // sobra exatamente um valor: o resultado final
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

- Inverter a ordem `esquerda`/`direita` ao desempilhar — como a pilha é LIFO, o primeiro `pop()` retorna o operando mais recente (o da **direita** da operação), não o da esquerda; para `+` e `*` a ordem não importa, mas para `-` e `/` inverter dá o resultado errado (ex.: `13 - 5` vira `5 - 13` se trocado).
- Usar divisão inteira que trunca "para baixo" (floor) em vez de "em direção a zero" — em Java e C++ a divisão inteira nativa já trunca em direção a zero, mas em Python (`//`) o comportamento padrão é floor division, que difere para operandos negativos (ex.: `-7 // 2` dá `-4` em Python, mas o esperado é `-3`); é preciso ajustar manualmente em Python.
- Tentar fazer `Integer.parseInt` num token que é um operador — sempre checar primeiro se o token é `"+"`, `"-"`, `"*"` ou `"/"` antes de tentar convertê-lo para número; cuidado especial com `"-11"` (número negativo), que não deve ser confundido com o operador `"-"` (a checagem de operador deve ser por igualdade exata de string, não por conter `'-'`).
- Esquecer que ao final deve sobrar exatamente **um** valor na pilha — se sobrar mais de um, é sinal de uma expressão malformada (mas o enunciado garante que isso não acontece).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Operação simples | `["2","1","+","3","*"]` | 9 | caso básico de duas operações encadeadas |
| Divisão que trunca em direção a zero | `["4","13","5","/","+"]` | 6 | `13/5` é `2.6`, truncado para `2` (não arredondado) |
| Número negativo como operando | `["10","6","9","3","+","-11","*","/","*","17","+","5","+"]` | 22 | testa que "-11" é tratado como número, não como operador de subtração |
| Divisão com resultado negativo | `tokens` terminando com `"-7","2","/"` (ilustrativo) | trunca em direção a zero, não para baixo | testa a pegadinha de truncamento com operandos negativos |

## 🔗 Conexões

- Problemas irmãos: [0224] Basic Calculator (avaliação de expressão infixa completa, com parênteses e precedência — mais complexo que RPN), [0682] Baseball Game (mesma ideia de simular operações sequenciais com uma pilha de valores)
- No backend: avaliação de expressões com pilha é a base de calculadoras, interpretadores de linguagens de query (muitos motores de banco de dados compilam expressões para uma forma pós-fixa internamente), e de máquinas virtuais baseadas em pilha (como a JVM, que executa bytecode empilhando operandos antes de cada instrução aritmética).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
