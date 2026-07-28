# [0682] Baseball Game

> 🔗 [LeetCode 682](https://leetcode.com/problems/baseball-game/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#Array` `#Simulation`

## 📜 O Problema

Você mantém o placar de um jogo de baseball com regras estranhas. No início, o registro está vazio. Você recebe uma lista de strings `operations`, onde cada operação é uma das seguintes:

- Um inteiro `x`: registra uma nova pontuação `x`.
- `'+'`: registra uma nova pontuação igual à soma das duas pontuações anteriores.
- `'D'`: registra uma nova pontuação igual ao dobro da pontuação anterior.
- `'C'`: invalida a pontuação anterior, removendo-a do registro.

Retorne a soma de todas as pontuações no registro após aplicar todas as operações.

**Exemplos:**
```
Input:  ops = ["5","2","C","D","+"]
Output: 30
Explicação:
"5" → registro [5]
"2" → registro [5, 2]
"C" → remove o anterior → registro [5]
"D" → dobro do anterior (5*2=10) → registro [5, 10]
"+" → soma dos dois anteriores (5+10=15) → registro [5, 10, 15]
Soma total: 5+10+15 = 30

Input:  ops = ["1","C"]
Output: 0
Explicação: registra 1, depois invalida; registro fica vazio, soma = 0.
```

**Restrições (e o que elas denunciam):**
- `1 <= operations.length <= 1000` → qualquer solução O(n) é rápida o bastante; o desafio aqui é de correção da simulação, não de performance
- `operations[i]` é `"C"`, `"D"`, `"+"` ou um inteiro em `[-3*10^4, 3*10^4]` → confirma que só existem essas 4 categorias de operação, sem casos extras a tratar
- Para `"+"`, sempre há pelo menos duas pontuações anteriores; para `"C"`/`"D"`, sempre há pelo menos uma → o enunciado garante entradas válidas, não é preciso tratar "pilha vazia" como erro

## 🧭 Como reconhecer o padrão

"Manter um registro onde cada nova entrada pode depender só das **últimas** entradas, e uma operação pode desfazer a mais recente" é a assinatura de stack: `'+'` olha o topo e o penúltimo, `'D'` olha o topo, e `'C'` remove o topo — todas as operações giram em torno do "mais recente primeiro" (LIFO), exatamente o que uma pilha oferece nativamente.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Manter as pontuações numa lista comum (`ArrayList`) e, para cada operação, acessar os últimos elementos por índice (`lista.get(lista.size()-1)`) ou remover o último com `lista.remove(lista.size()-1)`.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** na prática, essa "força bruta" já tem a mesma complexidade da solução ótima — a diferença é só de ferramenta. Usar uma pilha (`Deque`) em vez de uma lista genérica deixa a intenção do código explícita (peek/pop/push no topo) e evita erros de índice como `size()-1` versus `size()-2`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use uma pilha para representar o registro na ordem em que as pontuações foram adicionadas. Para cada operação: se for um número, empilhe-o. Se for `'+'`, olhe (sem remover) os dois valores do topo, some-os e empilhe o resultado — sem remover os originais, pois eles continuam válidos no registro. Se for `'D'`, empilhe o dobro do topo atual. Se for `'C'`, apenas desempilhe (remove a pontuação mais recente). No final, some todos os valores que sobraram na pilha.

## 🎬 Exemplo passo a passo

`ops = ["5","-2","4","C","D","9","+","+"]`

| Passo | Operação | Ação | Pilha após |
|---|---|---|---|
| 1 | `"5"` | empilha 5 | `[5]` |
| 2 | `"-2"` | empilha -2 | `[5, -2]` |
| 3 | `"4"` | empilha 4 | `[5, -2, 4]` |
| 4 | `"C"` | desempilha topo (4) | `[5, -2]` |
| 5 | `"D"` | dobro do topo (-2*2=-4), empilha | `[5, -2, -4]` |
| 6 | `"9"` | empilha 9 | `[5, -2, -4, 9]` |
| 7 | `"+"` | soma dos 2 do topo (-4+9=5), empilha | `[5, -2, -4, 9, 5]` |
| 8 | `"+"` | soma dos 2 do topo (9+5=14), empilha | `[5, -2, -4, 9, 5, 14]` |

Soma final: `5 + (-2) + (-4) + 9 + 5 + 14 = 27`

Resultado final: `27` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelas operações, cada uma processada em O(1)
- **Espaço:** O(n) — pior caso, todas as operações são números e ficam empilhadas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int calPoints(String[] operations) {
    Deque<Integer> pilha = new ArrayDeque<>();

    for (String op : operations) {
        switch (op) {
            case "+" -> {
                // soma os dois do topo SEM removê-los do registro (ambos continuam válidos)
                int topo = pilha.pop();
                int penultimo = pilha.peek();
                pilha.push(topo);          // devolve o topo removido temporariamente
                pilha.push(topo + penultimo);
            }
            case "D" -> pilha.push(2 * pilha.peek());
            case "C" -> pilha.pop();       // invalida a pontuação mais recente
            default -> pilha.push(Integer.parseInt(op)); // é um número
        }
    }

    int soma = 0;
    for (int pontuacao : pilha) {
        soma += pontuacao;
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

- Para `'+'`, remover permanentemente os dois valores do topo ao invés de só lê-los — as duas pontuações anteriores continuam válidas no registro; só a **nova** soma é adicionada. Errar isso derruba a contagem final.
- Confundir a ordem de leitura em `'+'`: o resultado é `topo + penúltimo` (as duas pontuações mais recentes), não `primeiro + segundo` do registro inteiro.
- Interpretar `'D'` como "dobro da soma de todo o registro" em vez de "dobro só da pontuação anterior" — é sempre relativo ao topo mais recente.
- Usar `Integer.parseInt` sem antes checar se a string é um dos operadores especiais — tentar fazer parse de `"+"`, `"D"` ou `"C"` como número lança exceção; por isso o `switch`/`if` deve testar os operadores primeiro (ou usar `default` como no código acima).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só um número seguido de invalidação | `["1","C"]` | 0 | registro fica vazio, soma de nada é 0 |
| Sequência de `'+'` encadeados | `["5","2","+","+"]` (não trivial, mas ilustra) | soma cresce a cada `+` sem remover histórico | garante que `'+'` empilha, não substitui |
| `'D'` logo após um negativo | `ops` terminando com `"-2","D"` | dobro de um valor negativo é mais negativo | testa que a lógica de dobro funciona com sinais negativos |
| Só `'C'` em sequência anulando tudo | `["5","2","C","C"]` | 0 | cada `'C'` remove exatamente a pontuação mais recente restante |

## 🔗 Conexões

- Problemas irmãos: [0150] Evaluate Reverse Polish Notation (mesma ideia de simular operações com uma pilha de operandos), [0020] Valid Parentheses (stack simples para rastrear estado sequencial)
- No backend: simulação de operações com "desfazer a última ação" (aqui, `'C'`) é o mesmo padrão usado em undo/redo de editores e em sistemas de transações com savepoints, onde cada operação nova pode depender do estado mais recente e pode ser revertida sem afetar o histórico anterior.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
