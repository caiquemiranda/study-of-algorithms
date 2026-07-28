# [0232] Implement Queue using Stacks

> 🔗 [LeetCode 232](https://leetcode.com/problems/implement-queue-using-stacks/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#Design` `#Queue`

## 📜 O Problema

Implemente uma fila FIFO (first-in-first-out) usando **apenas duas pilhas**. A fila implementada deve suportar todas as operações de uma fila normal (`push`, `peek`, `pop` e `empty`).

Implemente a classe `MyQueue`:
- `void push(int x)`: empilha o elemento `x` no final da fila.
- `int pop()`: remove o elemento da frente da fila e o retorna.
- `int peek()`: retorna o elemento da frente da fila.
- `boolean empty()`: retorna `true` se a fila está vazia.

**Notas do enunciado:** você só pode usar operações padrão de pilha (`push to top`, `peek/pop from top`, `size`, `is empty`).

**Exemplos:**
```
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 1, 1, false]

Explicação:
myQueue.push(1); // fila: [1]
myQueue.push(2); // fila: [1, 2] (o mais à esquerda é a frente)
myQueue.peek();  // retorna 1
myQueue.pop();   // retorna 1, fila fica [2]
myQueue.empty(); // retorna false
```

**Restrições (e o que elas denunciam):**
- `1 <= x <= 9` → valores pequenos, sem risco de overflow
- No máximo `100` chamadas no total → o desafio é de **design correto**, não de performance bruta
- Follow-up "cada operação em O(1) **amortizado**" → sinaliza que existe uma solução onde o custo de mover elementos entre pilhas é raro o suficiente para não pesar na média, mesmo que uma operação isolada custe O(n)

## 🧭 Como reconhecer o padrão

Assim como o [0225] (o problema espelhado), este é um exercício de "simular uma estrutura usando as primitivas de outra". A diferença de ordem entre pilha (LIFO) e fila (FIFO) precisa ser compensada — aqui, a sacada é que **inverter uma pilha duas vezes devolve a ordem original**, e é isso que permite transformar LIFO em FIFO usando duas pilhas.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Manter uma única pilha `entrada`. A cada `push`, empilha normalmente. Para `pop`/`peek`, transfira **todos** os elementos de `entrada` para uma pilha `saida` vazia toda vez que for consultar a frente — isso inverte a ordem, colocando o elemento mais antigo no topo de `saida`. Depois de consultar/remover, devolva os elementos de volta para `entrada` (ou refaça a transferência a cada chamada).

- Tempo: O(n) por `pop`/`peek` (sempre transfere tudo) · Espaço: O(n)
- **Por que não basta:** funciona, mas desperdiça trabalho: se você faz `pop()` duas vezes seguidas, a segunda chamada não deveria precisar re-inverter tudo de novo — o elemento seguinte já estaria pronto no topo de `saida` se ela não fosse esvaziada de volta. A solução ótima evita esse retrabalho.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use duas pilhas: `entrada` (recebe os `push`) e `saida` (serve os `pop`/`peek`). A regra de ouro: **só transfira de `entrada` para `saida` quando `saida` estiver vazia**. Empilhar em `entrada` inverte a ordem uma vez; transferir de `entrada` para `saida` inverte de novo — duas inversões restauram a ordem original (FIFO). Enquanto `saida` tiver elementos, use-a diretamente: eles já estão na ordem certa e não precisam ser tocados de novo. Isso significa que cada elemento é movido **no máximo duas vezes** em toda a sua vida (uma vez para `entrada`, uma vez de `entrada` para `saida`) — daí o O(1) amortizado.

## 🎬 Exemplo passo a passo

Sequência: `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`

| Passo | Operação | entrada | saida | Ação | Retorno |
|---|---|---|---|---|---|
| 1 | `push(1)` | `[1]` | `[]` | empilha em entrada | — |
| 2 | `push(2)` | `[1, 2]` | `[]` | empilha em entrada | — |
| 3 | `peek()` | `[]` | `[2, 1]` | saida vazia → transfere tudo de entrada (inverte): topo de saida é `1` | `1` |
| 4 | `pop()` | `[]` | `[2]` | saida não vazia → usa direto, desempilha topo | `1` |
| 5 | `empty()` | `[]` | `[2]` | ambas pilhas checadas, saida ainda tem `2` | `false` |

Resultado final: `[null, null, null, 1, 1, false]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) amortizado para todas as operações — cada elemento é movido de `entrada` para `saida` exatamente uma vez em toda sua vida útil, então o custo total de `n` operações é O(n), ou seja, O(1) em média por operação
- **Espaço:** O(n) — os elementos ficam distribuídos entre as duas pilhas

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MyQueue {
    private Deque<Integer> entrada = new ArrayDeque<>();
    private Deque<Integer> saida = new ArrayDeque<>();

    public void push(int x) {
        entrada.push(x);            // sempre entra pela pilha de entrada
    }

    public int pop() {
        transferirSeNecessario();
        return saida.pop();         // topo de saida = frente lógica da fila
    }

    public int peek() {
        transferirSeNecessario();
        return saida.peek();
    }

    public boolean empty() {
        return entrada.isEmpty() && saida.isEmpty();
    }

    // só mexe em saida quando ela está vazia: preserva a ordem já invertida corretamente
    private void transferirSeNecessario() {
        if (saida.isEmpty()) {
            while (!entrada.isEmpty()) {
                saida.push(entrada.pop()); // segunda inversão: restaura ordem FIFO
            }
        }
    }
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

- Transferir de `entrada` para `saida` mesmo quando `saida` já tem elementos — isso embaralha a ordem: os elementos "velhos" que já estavam prontos em `saida` ficariam por cima dos elementos "novos" recém-invertidos, invertendo a ordem de saída.
- Achar que cada `pop`/`peek` custa O(n) sempre — o pior caso individual é O(n) (quando `saida` está vazia e precisa da transferência completa), mas o custo **amortizado** é O(1) porque essa transferência completa só acontece esporadicamente.
- Checar `empty()` olhando só uma das duas pilhas — a fila só está vazia se **ambas** `entrada` e `saida` estiverem vazias.
- Confundir `push`/`pop` de pilha (topo) com `push`/`pop` de fila (extremidades opostas) ao nomear variáveis — manter os nomes `entrada`/`saida` (ou `in`/`out`) ajuda a não perder o fio da lógica.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Fila vazia | `empty()` logo no início | `true` | nenhum `push` ainda ocorreu |
| Peek repetido sem pop | `push(1)`, `push(2)`, `peek()`, `peek()` | `1`, `1` | segunda chamada não deve re-transferir nem alterar o resultado |
| Intercalar push depois de pop parcial | `push(1)`, `push(2)`, `pop()`, `push(3)`, `pop()` | `1`, `2` | `push(3)` vai para `entrada` (vazia nesse momento) sem afetar o que já está pronto em `saida` |
| Esvaziar e checar `empty` | `push(1)`, `pop()`, `empty()` | `true` | depois de remover o único elemento, ambas pilhas ficam vazias |

## 🔗 Conexões

- Problemas irmãos: [0225] Implement Stack using Queues (o problema espelhado: simular pilha com filas), [0155] Min Stack (outra estrutura de pilha customizada, mas focada em consulta O(1) do mínimo)
- No backend: a técnica de "duas pilhas, uma de entrada e uma de saída" aparece em filas de eventos que precisam preservar ordem de chegada (FIFO) mas só têm acesso a uma estrutura de pilha nativa (ex.: implementações de undo/redo que reaproveitam call stacks, ou buffers de replay de eventos onde o custo amortizado O(1) é o que torna a solução viável em produção).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
