# [0227] Basic Calculator II

> 🔗 [LeetCode 227](https://leetcode.com/problems/basic-calculator-ii/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Math` `#String`

## 📜 O Problema

Dada uma string `s` que representa uma expressão, avalie essa expressão e retorne seu valor. A divisão inteira trunca em direção a zero. A expressão é sempre válida, e você **não pode** usar funções nativas de avaliação de string (como `eval()`).

**Exemplos:**
```
Input:  s = "3+2*2"
Output: 7

Input:  s = " 3/2 "
Output: 1

Input:  s = " 3+5 / 2 "
Output: 5
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 3 * 10^5` → precisa de solução O(n) numa única passada; nada de reprocessar a string várias vezes
- `s` consiste de inteiros e operadores `'+' '-' '*' '/'` separados por espaços → é preciso ignorar espaços e agrupar dígitos consecutivos em números multi-dígito
- Todos os resultados intermediários cabem em `[-2^31, 2^31-1]` → não é preciso se preocupar com overflow além do `int` padrão
- Sem parênteses na entrada → simplifica bastante: só precisamos respeitar a precedência de `*`/`/` sobre `+`/`-`, não aninhamento

## 🧭 Como reconhecer o padrão

"Avaliar uma expressão respeitando precedência de operadores" é a assinatura clássica de avaliação com pilha: `*` e `/` têm precedência maior que `+`/`-`, então eles precisam ser resolvidos **imediatamente** ao serem encontrados (usando o operando mais recente), enquanto `+` e `-` só definem o sinal do próximo número a ser somado no final. A pilha guarda os termos já resolvidos, aguardando a soma final.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Fazer duas passadas: primeiro resolver todas as multiplicações e divisões substituindo-as pelo resultado (reconstruindo uma lista de tokens menor), depois somar/subtrair o que sobrou da esquerda para a direita.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** essa abordagem já é O(n), mas exige duas passadas e reconstrução intermediária da lista de tokens. A solução ótima resolve tudo numa única passada, aplicando `*`/`/` no momento em que são encontrados (sobre o número anterior já processado), sem nunca precisar "voltar atrás".

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra a string acumulando dígitos num número atual. Guarde também o **último operador visto** (começando com `'+'` implícito). Sempre que encontrar um caractere que não seja dígito/espaço (ou chegar ao fim da string), você sabe que o número atual terminou — aplique o **operador anterior** sobre ele: se era `'+'`, empilhe o número; se era `'-'`, empilhe seu negativo; se era `'*'` ou `'/'`, desempilhe o valor anterior, combine com o número atual, e empilhe o resultado (resolvendo a precedência na hora). Atualize o operador para o caractere atual e zere o número. No final, a resposta é a soma de tudo que sobrou na pilha.

## 🎬 Exemplo passo a passo

`s = " 3+5 / 2 "` (adicionando um `'+'` sentinela ao final para forçar o processamento do último número)

| Passo | Caractere | num acumulado | operador pendente | Ação | Pilha após |
|---|---|---|---|---|---|
| 1 | `3` | 3 | `+` (inicial) | dígito, só acumula | `[]` |
| 2 | `+` | 3 | `+` | fecha número: op `+` → empilha 3; novo operador `+` | `[3]` |
| 3 | `5` | 5 | `+` | dígito, só acumula | `[3]` |
| 4 | `/` | 5 | `+` | fecha número: op `+` → empilha 5; novo operador `/` | `[3, 5]` |
| 5 | `2` | 2 | `/` | dígito, só acumula | `[3, 5]` |
| 6 | `+` (sentinela) | 2 | `/` | fecha número: op `/` → desempilha 5, calcula `5/2=2` (trunca), empilha 2 | `[3, 2]` |

Soma final: `3 + 2 = 5` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string
- **Espaço:** O(n) — pior caso, pilha guarda até n/2 termos (todos somados/subtraídos sem nenhuma multiplicação/divisão)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int calculate(String s) {
    Deque<Integer> pilha = new ArrayDeque<>();
    int num = 0;
    char operador = '+'; // operador PENDENTE, aplicado quando o número atual "fecha"

    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (Character.isDigit(c)) {
            num = num * 10 + (c - '0'); // acumula dígitos multi-dígito
        }
        // número "fecha" ao encontrar um operador ou chegar ao fim da string
        if ((!Character.isDigit(c) && c != ' ') || i == s.length() - 1) {
            switch (operador) {
                case '+' -> pilha.push(num);
                case '-' -> pilha.push(-num);
                case '*' -> pilha.push(pilha.pop() * num); // resolve precedência na hora
                case '/' -> pilha.push(pilha.pop() / num); // Java já trunca em direção a zero
            }
            operador = c;  // guarda o operador que vai valer para o PRÓXIMO número
            num = 0;
        }
    }

    int soma = 0;
    for (int termo : pilha) {
        soma += termo;
    }
    return soma;
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

- Esquecer de processar o **último** número da string — como a decisão de "fechar" o número atual é disparada por encontrar um operador, o último número (sem operador depois) precisa de um gatilho especial: checar `i == s.length() - 1` além de checar caracteres não-dígito.
- Usar divisão inteira que trunca "para baixo" (floor) em vez de "em direção a zero" — Java e C++ já truncam corretamente por padrão, mas em Python `//` faz floor division, que difere para operandos negativos (é preciso ajustar manualmente).
- Confundir o **operador pendente** (que se aplica ao número que acabou de terminar) com o caractere atual (que vira o operador pendente para o *próximo* número) — a ordem de atualização importa: primeiro aplica o operador antigo, só depois atualiza `operador = c`.
- Ignorar espaços incorretamente, tratando-os como se fossem "fim de número" — um espaço no meio de `"3 + 2"` não deveria disparar o fechamento antes de encontrar de fato o `'+'`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só multiplicação/divisão | `"2*3/2"` | 3 | testa a resolução imediata de `*`/`/` sem nenhum `+`/`-` |
| Precedência com subtração | `"3-2*2"` | -1 | garante que `*` é resolvido antes de somar ao resultado final |
| Espaços extras em vários pontos | `" 3 + 5 / 2 "` | 5 | espaços não devem interferir no agrupamento de números nem operadores |
| Divisão com resultado negativo | `"0-3/2"` | 0 | `-3/2 = -1.5`, truncado em direção a zero vira `-1`, mas aqui a subtração ocorre como `0 - (3/2)`, testando a ordem correta de operações |

## 🔗 Conexões

- Problemas irmãos: [0150] Evaluate Reverse Polish Notation (mesma ideia de pilha de operandos, mas em notação pós-fixa em vez de infixa), [0224] Basic Calculator (versão com parênteses, exige uma pilha adicional para escopos aninhados)
- No backend: avaliação de expressões com precedência de operadores é a base de parsers de fórmulas em planilhas, motores de regras de negócio (rule engines) que avaliam condições compostas, e interpretadores de linguagens de query que precisam respeitar precedência sem depender de `eval()` (que seria um risco de segurança com entrada não confiável).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
