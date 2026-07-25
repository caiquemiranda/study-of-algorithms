# 04 — Stack e Monotonic Stack

> LIFO: o último que entra é o primeiro que sai. Problemas em [`../problemas/04_stack/`](../problemas/04_stack/).

## Conceito

**Stack** resolve problemas com estrutura de **aninhamento** ou **"o mais recente pendente"**: parênteses balanceados, desfazer operações, avaliação de expressões, chamadas de função (a call stack da Fase 1.2 É uma stack).

**Monotonic Stack** é a variação que cai em entrevista: uma pilha mantida sempre **crescente ou decrescente**. Ao chegar um elemento que viola a monotonia, desempilhe — e cada elemento desempilhado acaba de **descobrir sua resposta** (ex.: "o próximo elemento maior que eu é o que me desempilhou"). Transforma O(n²) em O(n) para toda a família "próximo maior/menor elemento".

## Como reconhecer no enunciado

- Parênteses/colchetes/tags balanceados; validação de aninhamento
- "desfazer", "processar o mais recente primeiro", avaliação de expressão (RPN/notação polonesa)
- **"próximo elemento maior/menor à direita/esquerda"** → monotonic stack
- "quantos dias até uma temperatura maior", "maior retângulo no histograma", "visibilidade" (prédios que enxergam o pôr do sol)

## Templates

```python
# Parênteses válidos — O(n)
def is_valid(s):
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = []
    for ch in s:
        if ch in pares:
            if not pilha or pilha.pop() != pares[ch]:
                return False
        else:
            pilha.append(ch)
    return not pilha

# Monotonic stack — próximo maior à direita (Daily Temperatures), O(n)
def daily_temperatures(temps):
    resp = [0] * len(temps)
    pilha = []                       # índices com temperaturas DECRESCENTES
    for i, t in enumerate(temps):
        while pilha and temps[pilha[-1]] < t:
            j = pilha.pop()          # j descobriu seu "próximo maior": i
            resp[j] = i - j
        pilha.append(i)
    return resp

# Maior retângulo no histograma — O(n)
def largest_rectangle(heights):
    pilha = []                       # (índice, altura) crescente
    melhor = 0
    for i, h in enumerate(heights + [0]):    # sentinela 0 esvazia no fim
        inicio = i
        while pilha and pilha[-1][1] > h:
            idx, alt = pilha.pop()
            melhor = max(melhor, alt * (i - idx))
            inicio = idx             # o retângulo de h se estende para trás
        pilha.append((inicio, h))
    return melhor
```

## Complexidade típica

O(n): apesar do `while` interno, **cada elemento entra e sai da pilha no máximo uma vez** (análise amortizada — Fase 2.1). Espaço O(n).

## Erros comuns

- `pop()` em pilha vazia (sempre cheque `if pilha`)
- Errar a direção da monotonia (crescente acha "próximo menor"; decrescente acha "próximo maior") — desenhe um exemplo antes de codar
- Guardar valores quando precisava de **índices** (para calcular distâncias)
- Esquecer a sentinela/flush final quando elementos podem ficar na pilha

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 20. Valid Parentheses | 🟢 easy |
| 155. Min Stack | 🟡 medium |
| 150. Evaluate Reverse Polish Notation | 🟡 medium |
| 22. Generate Parentheses | 🟡 medium |
| 739. Daily Temperatures | 🟡 medium |
| 853. Car Fleet | 🟡 medium |
| 84. Largest Rectangle in Histogram | 🔴 hard |

## Conexão com backend

A call stack, o parsing de expressões e de JSON/XML (aninhamento), o "undo" de editores, e o DFS iterativo usam stack. Stack overflow por recursão profunda (Fase 1.2) é essa estrutura estourando o limite do frame.
