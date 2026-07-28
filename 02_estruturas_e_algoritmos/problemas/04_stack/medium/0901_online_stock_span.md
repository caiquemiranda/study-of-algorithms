# [0901] Online Stock Span

> 🔗 [LeetCode 901](https://leetcode.com/problems/online-stock-span/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Design`

## 📜 O Problema

Projete um algoritmo que coleta cotações diárias de preço de uma ação e retorna o **span** do preço no dia atual. O span do preço num dia é o número máximo de dias **consecutivos** (contando a partir de hoje e voltando no tempo) em que o preço da ação foi **menor ou igual** ao preço de hoje.

Implemente a classe `StockSpanner`:
- `StockSpanner()`: inicializa o objeto.
- `int next(int price)`: retorna o span do preço de hoje, dado que o preço de hoje é `price`.

**Exemplos:**
```
Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output:
[null, 1, 1, 1, 2, 1, 4, 6]

Explicação:
next(100) → 1 (nenhum dia anterior)
next(80)  → 1 (80 < 100, span reinicia)
next(60)  → 1 (60 < 80, span reinicia)
next(70)  → 2 (70 >= 60, inclui o dia de 60 também)
next(60)  → 1 (60 < 70)
next(75)  → 4 (75 >= todos os últimos 4: 60,70,60,... acumula)
next(85)  → 6 (85 >= todos os últimos 6 dias)
```

**Restrições (e o que elas denunciam):**
- `1 <= price <= 10^5` → valores positivos, sem necessidade de tratar preços negativos ou zero
- No máximo `10^4` chamadas a `next` → precisa que cada chamada seja O(1) amortizado, não O(n) por chamada (que degradaria para O(n²) no total)

## 🧭 Como reconhecer o padrão

"Para cada novo elemento de um stream, encontrar quantos elementos consecutivos anteriores são menores ou iguais a ele" é a assinatura de **monotonic stack** aplicada a dados **online** (chegando um de cada vez, sem saber o futuro): em vez de guardar todos os preços e recalcular o span do zero a cada chamada, você mantém uma pilha decrescente de `(preço, span)`, onde cada entrada já representa um "bloco" de dias consecutivos que um preço maior futuro vai absorver de uma vez.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Guardar todos os preços já recebidos numa lista. A cada `next(price)`, percorrer a lista de trás para frente contando quantos preços consecutivos são `<= price`, parando no primeiro maior.

- Tempo: O(n) por chamada, O(n²) no total para `n` chamadas · Espaço: O(n)
- **Por que não basta:** cada chamada pode precisar reexaminar preços que já foram "resumidos" por chamadas anteriores — por exemplo, se os últimos 5 dias tiveram preços crescentes, uma nova chamada com preço ainda maior teria que percorrer todos os 5 de novo, quando essa informação já poderia estar agregada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha uma pilha de pares `(preço, span)`, com preços decrescentes do topo para a base (o topo tem o preço mais recente/menor "não resolvido"). Para cada novo `price`: comece com `span = 1` (pelo menos o próprio dia conta). Enquanto o topo da pilha tiver um preço **menor ou igual** ao atual, isso significa que aquele "bloco" inteiro de dias (representado pelo span guardado ali) está coberto pelo preço de hoje — desempilhe-o e **some** seu span ao span sendo calculado agora (o bloco inteiro é absorvido de uma vez, sem precisar reexaminar dia a dia). Empilhe `(price, span)` como o novo bloco representando hoje.

## 🎬 Exemplo passo a passo

Chamadas: `next(100)`, `next(80)`, `next(60)`, `next(70)`, `next(60)`, `next(75)`, `next(85)`

| Passo | price | Ação (desempilha blocos com preço <= atual, soma spans) | Pilha após (preço, span) | Retorno |
|---|---|---|---|---|
| 1 | 100 | pilha vazia, span=1 | `[(100,1)]` | 1 |
| 2 | 80 | topo (100) > 80, não desempilha, span=1 | `[(100,1),(80,1)]` | 1 |
| 3 | 60 | topo (80) > 60, não desempilha, span=1 | `[(100,1),(80,1),(60,1)]` | 1 |
| 4 | 70 | topo (60,1) <= 70 → pop, span=1+1=2; novo topo (80) > 70, para | `[(100,1),(80,1),(70,2)]` | 2 |
| 5 | 60 | topo (70) > 60, não desempilha, span=1 | `[(100,1),(80,1),(70,2),(60,1)]` | 1 |
| 6 | 75 | topo (60,1)<=75→pop,span=2; topo (70,2)<=75→pop,span=4; topo (80)>75, para | `[(100,1),(80,1),(75,4)]` | 4 |
| 7 | 85 | topo (75,4)<=85→pop,span=5; topo (80,1)<=85→pop,span=6; topo (100)>85, para | `[(100,1),(85,6)]` | 6 |

Resultado final: `[1, 1, 1, 2, 1, 4, 6]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) amortizado por chamada — cada dia é empilhado exatamente uma vez e desempilhado no máximo uma vez em toda a vida útil da pilha, então o custo total de `n` chamadas é O(n)
- **Espaço:** O(n) — a pilha guarda no máximo um bloco para cada dia, no pior caso (preços estritamente decrescentes, nunca mesclando)

## 💻 Implementações

### Java (referência completa e comentada)
```java
class StockSpanner {
    // pilha de pares (preço, span): preços decrescentes do topo para a base
    private final Deque<int[]> pilha = new ArrayDeque<>();

    public int next(int price) {
        int span = 1; // pelo menos o próprio dia conta

        // absorve todos os blocos anteriores cujo preço é <= hoje, somando seus spans de uma vez
        while (!pilha.isEmpty() && pilha.peek()[0] <= price) {
            span += pilha.pop()[1];
        }

        pilha.push(new int[]{price, span}); // hoje vira um novo bloco resumido
        return span;
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

- Usar `<` em vez de `<=` na condição do while — o enunciado define span como dias com preço **menor ou igual**, então empates (preço igual ao de hoje) também devem ser absorvidos no bloco atual.
- Esquecer de somar o `span` do bloco desempilhado, tratando cada desempilhamento como "+1 dia" — cada entrada da pilha já pode representar **múltiplos** dias resumidos (fruto de mesclagens anteriores); somar só 1 por pop perderia a informação agregada.
- Achar que é preciso guardar todos os preços históricos individualmente — a mesclagem em blocos é exatamente o que evita isso: uma vez que um bloco é absorvido por um preço maior, seus dias individuais nunca mais precisam ser reexaminados um a um.
- Inicializar `span` com `0` em vez de `1` — o próprio dia de hoje sempre conta como parte do seu próprio span, mesmo que nenhum bloco anterior seja absorvido.

## 🧪 Casos de teste para validar

| Caso | Input (sequência de `next`) | Esperado | Por quê |
|---|---|---|---|
| Primeira chamada | `next(50)` | 1 | sem histórico, span mínimo |
| Preços estritamente crescentes | `next(10)`, `next(20)`, `next(30)` | 1, 2, 3 | cada novo preço absorve tudo que veio antes, span cresce linearmente |
| Preços estritamente decrescentes | `next(30)`, `next(20)`, `next(10)` | 1, 1, 1 | nenhum bloco é absorvido, cada dia fica isolado na pilha |
| Preços repetidos (empate) | `next(50)`, `next(50)` | 1, 2 | testa a condição `<=`: preço igual também conta no span |

## 🔗 Conexões

- Problemas irmãos: [0739] Daily Temperatures (mesma técnica de monotonic stack, mas processando o array completo de uma vez em vez de dados chegando em stream), [0155] Min Stack (outra estrutura de pilha customizada respondendo consultas O(1))
- No backend: essa técnica de "resumir blocos consecutivos numa pilha para responder consultas sobre um stream em tempo real, sem reprocessar o histórico inteiro" é o mesmo princípio usado em sistemas de monitoramento que calculam janelas de tendência (ex.: "há quantos períodos consecutivos a métrica não piora") sobre dados chegando continuamente, sem armazenar e reprocessar todo o histórico a cada nova leitura.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
