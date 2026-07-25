# 04 — Stack e Monotonic Stack

> LIFO: o último que entra é o primeiro que sai. Soluções em [`../problemas/04_stack/`](../problemas/04_stack/).

## 1. Conceito Central e Analogia Didática

- **Stack** resolve estruturas de **aninhamento** e "o pendente mais recente primeiro": parênteses, undo, avaliação de expressão, call stack.
- **Monotonic Stack**: pilha mantida sempre crescente ou decrescente; quem chega e viola a monotonia **desempilha** os anteriores — e cada desempilhado descobre ali sua resposta ("meu próximo maior é quem me tirou").
- Transforma a família "próximo maior/menor elemento" de O(n²) para O(n).

**Analogia:** pilha de pratos: você só mexe no do topo. Na versão monotônica, imagine pessoas numa fila olhando para frente, cada uma esperando alguém **mais alto** chegar: quando chega, todas as mais baixas à frente dele descobrem sua resposta de uma vez e saem da fila.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se envolve **parênteses/colchetes/tags balanceados** → stack simples.
- Se pede o **"próximo elemento maior/menor à esquerda/direita"** → monotonic stack.
- Se pergunta "quantos dias até X maior" / "quem este elemento enxerga" → monotonic stack com índices.
- Se pede avaliação de **expressão pós-fixa (RPN)** ou parsing aninhado → stack de operandos.
- Se pede "maior retângulo/área em histograma" → monotonic stack (o hard clássico).

## 3. Templates de Código

### Parênteses válidos

```java
// Java — ArrayDeque, não java.util.Stack (legado sincronizado, mais lento)
public boolean isValid(String s) {
    Deque<Character> pilha = new ArrayDeque<>();
    Map<Character, Character> pares = Map.of(')', '(', ']', '[', '}', '{');
    for (char c : s.toCharArray()) {
        if (pares.containsKey(c)) {                       // é fechamento:
            if (pilha.isEmpty() || pilha.pop() != pares.get(c)) return false; // topo DEVE ser o par
        } else {
            pilha.push(c);                                // abertura: vira pendência
        }
    }
    return pilha.isEmpty();  // pendência sobrando = aberto sem fechar
}
```

```python
def is_valid(s):
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = []
    for ch in s:
        if ch in pares:
            if not pilha or pilha.pop() != pares[ch]:  # fecha sem par correspondente no topo
                return False
        else:
            pilha.append(ch)
    return not pilha
```

### Monotonic stack (Daily Temperatures — próximo maior à direita)

```java
// Java — pilha de ÍNDICES com temperaturas decrescentes
public int[] dailyTemperatures(int[] temps) {
    int[] resp = new int[temps.length];
    Deque<Integer> pilha = new ArrayDeque<>();      // guarda índices, não valores: precisamos da distância
    for (int i = 0; i < temps.length; i++) {
        while (!pilha.isEmpty() && temps[pilha.peek()] < temps[i]) {
            int j = pilha.pop();                    // j acabou de descobrir seu "próximo maior": i
            resp[j] = i - j;                        // distância em dias
        }
        pilha.push(i);                              // i vira pendente à espera de alguém maior
    }
    return resp;                                    // quem sobrou na pilha fica com 0 (nunca esquenta)
}
```

```python
def daily_temperatures(temps):
    resp = [0] * len(temps)
    pilha = []                                  # índices com temps decrescentes
    for i, t in enumerate(temps):
        while pilha and temps[pilha[-1]] < t:   # t resolve a espera de todos os menores no topo
            j = pilha.pop()
            resp[j] = i - j
        pilha.append(i)
    return resp
```

## 4. Walkthrough Visual (Teste de Mesa)

`dailyTemperatures([73, 74, 71, 76])`

| i | temps[i] | ação do while | pilha após (índices) | resp parcial |
|---|---|---|---|---|
| 0 | 73 | — | `[0]` | `[0,0,0,0]` |
| 1 | 74 | pop 0 (73<74) → resp[0]=1 | `[1]` | `[1,0,0,0]` |
| 2 | 71 | — (71<74 mantém monotonia) | `[1,2]` | `[1,0,0,0]` |
| 3 | 76 | pop 2 → resp[2]=1; pop 1 → resp[1]=2 | `[3]` | `[1,2,1,0]` |

- Resultado: `[1, 2, 1, 0]` ✔ — o índice 3 fica na pilha (nunca chega dia mais quente).

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade |
|---|---|
| push / pop / peek | O(1) |
| Algoritmo monotonic completo | O(n) amortizado |
| Espaço | O(n) pior caso |

- O `while` interno não torna O(n²): **cada índice entra e sai da pilha no máximo uma vez** — o custo total dos pops é n.

## 6. Pegadinhas e Erros Comuns

- `pop()`/`peek()` em pilha vazia → sempre cheque `isEmpty()` primeiro.
- Errar a **direção da monotonia**: decrescente encontra "próximo maior"; crescente encontra "próximo menor". Desenhe antes de codar.
- Guardar **valores** quando o problema pede distância/posição → guarde **índices**.
- **Java**: usar `java.util.Stack` (classe legada, métodos sincronizados) em vez de `ArrayDeque`.
- **Java**: `Deque.push/pop` operam na CABEÇA — não misture com `addLast` no mesmo código.
- **Python**: `list.pop(0)` é O(n) — pilha usa `append`/`pop()` do fim; fila usa `collections.deque`.
- Esquecer o flush final (elementos que sobram na pilha precisam de valor default ou sentinela).

## 7. Aplicações no Mundo Real (Backend)

- **Call stack**: frames de função, stack trace que você lê em todo bug (e `StackOverflowError` em recursão profunda).
- **Parsing**: JSON/XML/expressões — validação de aninhamento em parsers e compiladores.
- **Undo/rollback**: editores, transações aninhadas com savepoints (PostgreSQL) empilham estados.
- **Spring**: a cadeia de interceptors/filtros desempilha na ordem inversa na saída da requisição — comportamento LIFO.
- Monotonic stack aparece em análise de séries (drawdown máximo, skyline de preços).

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟢 Easy |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | 🟡 Medium |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | 🟡 Medium |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟡 Medium |
| 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | 🟡 Medium |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | 🔴 Hard |
