# [0225] Implement Stack using Queues

> 🔗 [LeetCode 225](https://leetcode.com/problems/implement-stack-using-queues/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#Design` `#Queue`

## 📜 O Problema

Implemente uma pilha LIFO (last-in-first-out) usando **apenas duas filas**. A pilha implementada deve suportar todas as operações de uma pilha normal (`push`, `top`, `pop` e `empty`).

Implemente a classe `MyStack`:
- `void push(int x)`: empilha o elemento `x` no topo da pilha.
- `int pop()`: remove o elemento do topo da pilha e o retorna.
- `int top()`: retorna o elemento do topo da pilha.
- `boolean empty()`: retorna `true` se a pilha está vazia.

**Notas do enunciado:** você só pode usar operações padrão de fila (`push to back`, `peek/pop from front`, `size`, `is empty`).

**Exemplos:**
```
Input:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 2, 2, false]

Explicação:
myStack.push(1);
myStack.push(2);
myStack.top();   // retorna 2
myStack.pop();   // retorna 2
myStack.empty(); // retorna false
```

**Restrições (e o que elas denunciam):**
- `1 <= x <= 9` → valores pequenos, não há risco de overflow a considerar
- No máximo `100` chamadas no total → qualquer abordagem, mesmo O(n) por operação, é rápida o bastante; o desafio aqui é de **design**, não de performance bruta
- Follow-up "implemente usando só uma fila" → sinaliza que existe uma versão ainda mais enxuta, mas a solução com duas filas já é o suficiente para o problema principal

## 🧭 Como reconhecer o padrão

O problema pede explicitamente para simular o comportamento de uma estrutura (pilha) usando **apenas** as operações de outra (fila). Isso é um problema de "adaptar uma estrutura usando as primitivas de outra" — a técnica central é entender a diferença de ordem entre FIFO (fila) e LIFO (pilha) e compensar essa diferença ativamente a cada operação.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar duas filas, `principal` e `auxiliar`. Em cada `push`, insere o novo elemento na `auxiliar`, depois move **todos** os elementos que já estavam na `principal` para trás dele na `auxiliar` (recriando a ordem LIFO), e por fim troca os papéis das duas filas. Assim, o elemento mais recente sempre fica na frente da fila `principal`.

- Tempo: `push` O(n) (precisa mover todos os elementos anteriores) · `pop`/`top`/`empty` O(1) · Espaço: O(n)
- **Por que não basta:** essa já É essencialmente a solução ótima para este problema — com apenas duas filas permitidas e a restrição de só usar operações padrão de fila, não existe uma forma de fazer `push` em O(1) sem sacrificar `pop`/`top` (isso só é possível com **uma** fila rotacionando na hora do `pop`, que é o follow-up). A "força bruta" aqui já é aceitável dado o limite de 100 chamadas.

## 💡 Solução 2 — A ideia otimizada (intuição)

A sacada é: como filas só deixam você acessar a **frente**, para simular "o último que entrou é o primeiro que sai" você precisa reordenar a fila **no momento do `push`**, não no `pop`. Coloque o novo elemento numa fila auxiliar vazia, depois "reempilhe" por baixo dele todos os elementos antigos (retirando da fila principal e recolocando na auxiliar, na mesma ordem relativa). No final, o elemento recém-inserido fica na frente — exatamente onde a fila permite olhar/remover primeiro. `pop`, `top` e `empty` viram operações triviais de fila (`poll`/`peek`/`isEmpty`) porque o reordenamento já garantiu que a frente da fila sempre representa o topo da pilha.

## 🎬 Exemplo passo a passo

Sequência: `push(1)`, `push(2)`, `top()`, `pop()`, `empty()`

| Passo | Operação | auxiliar (constrói) | principal (resultado) | Retorno |
|---|---|---|---|---|
| 1 | `push(1)` | `[1]` | após mover 0 antigos e trocar: `[1]` | — |
| 2 | `push(2)` | começa `[2]`, move `1` da principal → `[2, 1]` | troca: `[2, 1]` | — |
| 3 | `top()` | — | `[2, 1]` | `peek()` = `2` |
| 4 | `pop()` | — | remove a frente: `[1]` | `2` |
| 5 | `empty()` | — | `[1]` não está vazia | `false` |

Resultado final: `[null, null, null, 2, 2, false]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** `push` O(n) — precisa mover todos os `n` elementos existentes a cada inserção; `pop`/`top`/`empty` O(1) — direto na frente da fila principal
- **Espaço:** O(n) — os elementos ficam guardados nas duas filas (nunca simultaneamente duplicados de forma permanente)

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MyStack {
    private Queue<Integer> principal = new LinkedList<>();
    private Queue<Integer> auxiliar = new LinkedList<>();

    public void push(int x) {
        auxiliar.offer(x);                 // novo elemento entra sozinho na auxiliar
        while (!principal.isEmpty()) {     // reempilha os antigos por baixo dele
            auxiliar.offer(principal.poll());
        }
        // troca os papéis: agora "auxiliar" (com o novo na frente) vira a principal
        Queue<Integer> troca = principal;
        principal = auxiliar;
        auxiliar = troca;
    }

    public int pop() {
        return principal.poll();           // frente da fila = topo da pilha, por construção
    }

    public int top() {
        return principal.peek();
    }

    public boolean empty() {
        return principal.isEmpty();
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

- Esquecer de mover **todos** os elementos antigos da `principal` para a `auxiliar` antes de trocar os papéis — se sobrar algum, a ordem LIFO quebra e `pop`/`top` retornam o elemento errado.
- Trocar a ordem: colocar o elemento novo **depois** dos antigos na auxiliar em vez de **antes** — isso reconstrói a fila original (FIFO), não uma pilha.
- Usar `Queue.remove()` esperando exceção em vez de `poll()`/poll retorna `null` se vazia — para este problema o enunciado garante chamadas válidas, mas em geral prefira `poll`/`offer` (não lançam exceção) a `remove`/`add` em filas Java.
- Achar que dá para fazer `push` O(1) com duas filas sem violar a restrição de "só operações padrão de fila" — não dá; o trade-off O(n) no `push` é inerente a essa abordagem (o follow-up com uma fila só faz o mesmo trabalho, mas com uma fila em vez de duas).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Pilha vazia | `empty()` logo no início | `true` | nenhum `push` ainda ocorreu |
| Um único elemento | `push(5)`, `top()`, `pop()` | `5`, `5` | caso trivial sem necessidade de reordenar nada |
| Múltiplos pushes seguidos | `push(1)`, `push(2)`, `push(3)`, `pop()` | `3` | o último inserido deve sair primeiro (LIFO), não o primeiro (que seria FIFO) |
| Esvaziar e checar `empty` | `push(1)`, `pop()`, `empty()` | `true` | depois de remover o único elemento, a pilha deve reportar vazia |

## 🔗 Conexões

- Problemas irmãos: [0232] Implement Queue using Stacks (o problema espelhado: simular fila com pilhas), [0155] Min Stack (outra estrutura de pilha customizada, mas focada em consulta O(1) do mínimo em vez de troca de ordem)
- No backend: entender a diferença entre FIFO e LIFO na prática é essencial ao escolher estrutura para filas de mensagens (Kafka, SQS — FIFO) versus pilhas de execução/undo (LIFO); esse tipo de exercício de "adaptar uma estrutura usando as primitivas de outra" também aparece ao implementar adaptadores/wrappers sobre APIs de terceiros que só expõem um subconjunto de operações.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
