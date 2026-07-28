# [0155] Min Stack

> 🔗 [LeetCode 155](https://leetcode.com/problems/min-stack/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Design` `#Medium`

## 📜 O Problema

Projete uma pilha que suporte `push`, `pop`, `top`, e recuperar o elemento **mínimo** em tempo constante.

Implemente a classe `MinStack`:
- `MinStack()`: inicializa o objeto da pilha.
- `void push(int value)`: empilha o elemento `value`.
- `void pop()`: remove o elemento do topo da pilha.
- `int top()`: retorna o elemento do topo.
- `int getMin()`: retorna o elemento mínimo da pilha.

Você deve implementar uma solução com complexidade de tempo O(1) para **cada** função.

**Exemplos:**
```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output:
[null,null,null,null,-3,null,0,-2]

Explicação:
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // retorna -3
minStack.pop();
minStack.top();    // retorna 0
minStack.getMin(); // retorna -2
```

**Restrições (e o que elas denunciam):**
- `-2^31 <= val <= 2^31 - 1` → valores cabem em `int`, mas o range completo sinaliza que não dá para usar um valor "sentinela" como `Integer.MIN_VALUE` para representar "nenhum mínimo ainda", já que ele é um valor válido de entrada
- `pop`, `top` e `getMin` sempre são chamados em pilhas não vazias → não é preciso tratar pilha vazia nessas operações
- No máximo `3*10^4` chamadas, e **cada função deve ser O(1)** → a restrição central do problema: descarta qualquer solução que recalcule o mínimo varrendo a pilha (isso seria O(n) por chamada de `getMin`)

## 🧭 Como reconhecer o padrão

"Pilha customizada com uma consulta extra O(1)" é um problema de **design de estrutura de dados** sobre stack: a operação `getMin` parece exigir conhecer todo o histórico da pilha, mas a observação chave é que o mínimo só muda quando você empilha um valor menor ou desempilha o próprio mínimo atual — e ambos os eventos podem ser rastreados **incrementalmente**, em paralelo à pilha principal, sem recalcular nada.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Manter só a pilha de valores normal. Para `getMin()`, percorrer toda a pilha (ou converter para array) e encontrar o menor valor a cada chamada.

- Tempo: `push`/`pop`/`top` O(1) · `getMin` O(n) · Espaço: O(n)
- **Por que não basta:** o enunciado exige explicitamente que **todas** as operações sejam O(1), incluindo `getMin`. Varrer a pilha inteira a cada consulta de mínimo viola essa restrição diretamente — com até 3*10^4 chamadas, isso poderia degradar para O(n²) no total se `getMin` for chamado repetidamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha **duas pilhas em paralelo**: a pilha principal (`valores`) com os elementos normais, e uma pilha auxiliar (`minimos`) que, no topo, sempre reflete o mínimo da pilha principal **até aquele ponto**. A cada `push(v)`: empilhe `v` em `valores`, e empilhe em `minimos` o **menor entre `v` e o topo atual de `minimos`** (ou só `v` se `minimos` estiver vazia). A cada `pop()`: desempilhe de **ambas** as pilhas juntas — como cada posição de `minimos` corresponde exatamente à mesma posição em `valores`, remover o topo de uma sincroniza com remover o topo da outra, e o novo topo de `minimos` automaticamente já é o mínimo correto do que sobrou. `getMin()` é só `minimos.peek()`.

## 🎬 Exemplo passo a passo

Sequência: `push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`

| Passo | Operação | valores após | minimos após | Retorno |
|---|---|---|---|---|
| 1 | `push(-2)` | `[-2]` | `[-2]` (minimos vazia, então só -2) | — |
| 2 | `push(0)` | `[-2, 0]` | `[-2, -2]` (min(0, -2) = -2) | — |
| 3 | `push(-3)` | `[-2, 0, -3]` | `[-2, -2, -3]` (min(-3, -2) = -3) | — |
| 4 | `getMin()` | `[-2, 0, -3]` | `[-2, -2, -3]` | topo de minimos = `-3` |
| 5 | `pop()` | `[-2, 0]` | `[-2, -2]` | remove topo de ambas |
| 6 | `top()` | `[-2, 0]` | `[-2, -2]` | topo de valores = `0` |
| 7 | `getMin()` | `[-2, 0]` | `[-2, -2]` | topo de minimos = `-2` |

Resultado final: `[-3, 0, -2]` (nas posições de retorno) ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) para todas as operações (`push`, `pop`, `top`, `getMin`) — cada uma mexe só no topo de uma ou duas pilhas
- **Espaço:** O(n) — a pilha auxiliar `minimos` guarda um valor para cada elemento de `valores` (mesmo tamanho, sem economia, mas ainda linear)

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MinStack {
    private final Deque<Integer> valores = new ArrayDeque<>();
    private final Deque<Integer> minimos = new ArrayDeque<>(); // topo = mínimo até aquele ponto

    public void push(int val) {
        valores.push(val);
        // se minimos está vazia, val É o mínimo; senão, compara com o mínimo anterior
        int minimoAtual = minimos.isEmpty() ? val : Math.min(val, minimos.peek());
        minimos.push(minimoAtual);
    }

    public void pop() {
        valores.pop();
        minimos.pop(); // remove em sincronia: cada posição de minimos espelha valores
    }

    public int top() {
        return valores.peek();
    }

    public int getMin() {
        return minimos.peek(); // já é o mínimo corrente, sem recalcular nada
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

- Guardar só **um** valor de mínimo global (uma variável, não uma pilha) — isso quebra quando o mínimo atual é removido por um `pop()`: sem uma pilha auxiliar sincronizada, você perde o "segundo menor" que deveria virar o novo mínimo, e precisaria varrer tudo de novo (violando o O(1)).
- Esquecer de empilhar em `minimos` a cada `push`, mesmo quando o novo valor **não** é menor que o mínimo atual — a pilha `minimos` precisa ter **exatamente** o mesmo tamanho que `valores` em todo momento, repetindo o mínimo anterior quando o novo valor não bate recorde, para que o `pop()` sincronizado funcione.
- Usar `Integer.MIN_VALUE` como sentinela para "pilha vazia, nenhum mínimo ainda" — a restrição `-2^31 <= val <= 2^31-1` inclui exatamente esse valor como entrada válida, então um sentinela colidiria com um valor real; a checagem `minimos.isEmpty()` é a forma segura.
- Chamar `pop()` em `valores` mas esquecer de sincronizar `minimos` (ou vice-versa) — as duas pilhas precisam andar sempre em lockstep; um pop desalinhado corrompe todos os `getMin()` seguintes.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Mínimo é removido e precisa ser recalculado | `push(1)`, `push(2)`, `getMin()`, `pop()`, `getMin()` | 1, 1 | o valor 1 continua sendo mínimo mesmo após o pop, testando que não há falso recálculo |
| Valores repetidos iguais ao mínimo | `push(0)`, `push(0)`, `pop()`, `getMin()` | 0 | mesmo com duplicatas do mínimo, a pilha sincronizada mantém o valor correto após um pop |
| Só um elemento | `push(5)`, `getMin()`, `top()` | 5, 5 | caso trivial sem histórico de comparação |
| Valores estritamente decrescentes | `push(3)`, `push(2)`, `push(1)`, `getMin()` | 1 | cada push bate um novo recorde de mínimo, testando a atualização constante |

## 🔗 Conexões

- Problemas irmãos: [0225] Implement Stack using Queues (outro problema de design de pilha customizada), [0496] Next Greater Element I (outra estrutura auxiliar — mapa — mantida em paralelo a uma pilha para responder consultas O(1))
- No backend: manter uma estrutura auxiliar sincronizada para responder consultas agregadas em O(1) é o mesmo princípio usado em caches que mantêm min/max/contadores atualizados incrementalmente (em vez de recalcular varrendo todos os dados), como em janelas de métricas de monitoramento que precisam expor "mínimo da janela atual" sem reprocessar tudo a cada leitura.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
