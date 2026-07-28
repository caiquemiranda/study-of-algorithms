# [0933] Number of Recent Calls

> 🔗 [LeetCode 933](https://leetcode.com/problems/number-of-recent-calls/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Queue` `#Design` `#DataStream`

## 📜 O Problema

Implemente a classe `RecentCounter`, que conta o número de requisições recentes dentro de uma janela de tempo.

- `RecentCounter()`: inicializa o contador com zero requisições.
- `int ping(int t)`: adiciona uma nova requisição no instante `t` (em milissegundos) e retorna quantas requisições aconteceram nos últimos `3000` milissegundos (incluindo a nova), ou seja, no intervalo `[t - 3000, t]`.

É garantido que cada chamada a `ping` usa um valor de `t` estritamente maior que o da chamada anterior.

**Exemplos:**
```
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output:
[null, 1, 2, 3, 3]

Explicação:
ping(1)    → requests = [1], intervalo [-2999,1] → 1
ping(100)  → requests = [1,100], intervalo [-2900,100] → 2
ping(3001) → requests = [1,100,3001], intervalo [1,3001] → 3
ping(3002) → requests = [1,100,3001,3002], intervalo [2,3002] → 3 (o "1" saiu da janela)
```

**Restrições (e o que elas denunciam):**
- `1 <= t <= 10^9` → os tempos podem ser grandes, mas isso não afeta a estrutura da solução, só o tipo numérico (cabe em `int`)
- `t` é **estritamente crescente** a cada chamada → garante que a fila de requisições está sempre em ordem cronológica; nunca é preciso reordenar nada, só remover do início
- No máximo `10^4` chamadas → cada requisição só entra e sai da estrutura uma vez, então mesmo O(n) amortizado total é rapidíssimo

## 🧭 Como reconhecer o padrão

"Manter uma janela deslizante baseada em **tempo** (não em índice fixo), descartando o que ficou velho demais, e contando o que resta" é o padrão de uma fila: novos elementos entram sempre no fim (ordem cronológica garantida pelo enunciado), e elementos antigos saem sempre pela frente assim que ficam fora da janela — nunca do meio ou do fim. Isso é exatamente o comportamento FIFO de uma fila.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Guardar todos os tempos de ping numa lista. A cada `ping(t)`, percorrer a lista inteira contando quantos valores estão dentro de `[t - 3000, t]`.

- Tempo: O(n) por chamada, O(n²) no total para `n` chamadas · Espaço: O(n)
- **Por que não basta:** a cada `ping`, você reconta do zero requisições que já foram contadas antes — como os tempos só crescem, uma vez que uma requisição fica fora da janela ela nunca mais volta a ficar dentro, então recontá-la a cada chamada é trabalho desperdiçado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha uma fila (ordem de chegada = ordem cronológica, já que `t` é estritamente crescente) só com as requisições que ainda estão dentro da janela de 3000ms. A cada `ping(t)`: primeiro, enfileire o novo `t`. Depois, remova da **frente** da fila todos os tempos menores que `t - 3000` (ficaram velhos demais). O que sobrar na fila é exatamente a resposta — não precisa contar nada à parte, o tamanho da fila já é a contagem, porque cada elemento só é removido quando definitivamente sai da janela (nunca reentra, já que o tempo só avança).

## 🎬 Exemplo passo a passo

Chamadas: `ping(1)`, `ping(100)`, `ping(3001)`, `ping(3002)`

| Passo | Chamada | Enfileira | Remove da frente (< t-3000) | Fila após | Retorno (tamanho) |
|---|---|---|---|---|---|
| 1 | `ping(1)` | 1 | nada (1-3000 = -2999, nada é menor) | `[1]` | 1 |
| 2 | `ping(100)` | 100 | nada (100-3000 = -2900) | `[1, 100]` | 2 |
| 3 | `ping(3001)` | 3001 | nada (3001-3000 = 1; `1` não é `< 1`) | `[1, 100, 3001]` | 3 |
| 4 | `ping(3002)` | 3002 | remove `1` (3002-3000=2; `1 < 2`) | `[100, 3001, 3002]` | 3 |

Resultado final: `[1, 2, 3, 3]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) amortizado por chamada — cada requisição é enfileirada exatamente uma vez e removida no máximo uma vez em toda sua vida, então o custo total de `n` chamadas é O(n)
- **Espaço:** O(n) pior caso — se todas as requisições couberem na mesma janela de 3000ms, a fila guarda todas

## 💻 Implementações

### Java (referência completa e comentada)
```java
class RecentCounter {
    private final Deque<Integer> fila = new ArrayDeque<>(); // ordem cronológica garantida pelo enunciado

    public int ping(int t) {
        fila.addLast(t);                       // nova requisição sempre entra no fim
        while (fila.peekFirst() < t - 3000) {   // remove da frente tudo que ficou fora da janela
            fila.pollFirst();
        }
        return fila.size();                     // o que resta já é a contagem da janela [t-3000, t]
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

- Usar `ArrayList`/`List` e remover do índice 0 (`list.remove(0)`) — isso é O(n) por remoção porque desloca todos os elementos restantes; use uma fila real (`ArrayDeque` com `pollFirst`) que remove da frente em O(1).
- Errar o limite da janela: o intervalo é **inclusive** `[t - 3000, t]`, então a condição de remoção é `< t - 3000` (estritamente menor), não `<= t - 3000` — um ping exatamente em `t - 3000` ainda conta.
- Esquecer que a janela é sempre relativa ao `t` **atual** da chamada, não a um relógio externo — cada `ping` recalcula sua própria janela `[t-3000, t]`, então a condição de remoção usa o `t` recém-recebido.
- Achar que precisa contar manualmente os elementos válidos — como a fila só contém exatamente os elementos dentro da janela (os de fora já foram removidos), `fila.size()` já é a resposta, sem precisar de outro loop de contagem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Primeira chamada | `ping(1)` | 1 | só a própria requisição existe, nada a remover |
| Todas dentro da mesma janela | `ping(1)`, `ping(2)`, `ping(3)` | 1, 2, 3 | nenhuma sai da janela ainda (diferença máxima é 2ms) |
| Exatamente no limite da janela | `ping(1)`, `ping(3001)` | 1, 2 | `3001 - 3000 = 1`, e `1` não é `< 1`, então continua contando (limite inclusive) |
| Logo após o limite | `ping(1)`, `ping(3002)` | 1, 1 | `3002 - 3000 = 2`, e `1 < 2`, então `1` sai da janela |

## 🔗 Conexões

- Problemas irmãos: [0239] Sliding Window Maximum (janela deslizante com deque, mas mantendo o máximo em vez de contar), [1700] Number of Students Unable to Eat Lunch (outra estrutura de fila simulando ordem de chegada)
- No backend: essa é exatamente a técnica por trás de **rate limiting** com janela deslizante (sliding window rate limiter) — contar quantas requisições um cliente fez nos últimos N segundos para decidir se uma nova requisição deve ser bloqueada, descartando da fila os registros de requisições antigas conforme o tempo avança.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
