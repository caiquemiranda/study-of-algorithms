# [0636] Exclusive Time of Functions

> 🔗 [LeetCode 636](https://leetcode.com/problems/exclusive-time-of-functions/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Array` `#Medium`

## 📜 O Problema

Numa CPU de thread única, um programa executa `n` funções (IDs de `0` a `n-1`). Chamadas de função são armazenadas numa **call stack**: ao iniciar, o ID é empilhado; ao terminar, é desempilhado. A função no topo da pilha é a que está executando no momento.

Você recebe `logs`, uma lista de strings no formato `"{id}:{start|end}:{timestamp}"`. Por exemplo, `"0:start:3"` significa que a função 0 começou **no início** do timestamp 3, e `"1:end:2"` significa que a função 1 terminou **no fim** do timestamp 2. Uma função pode ser chamada múltiplas vezes, inclusive recursivamente.

O **tempo exclusivo** de uma função é a soma dos tempos de execução de todas as suas chamadas, **sem contar** o tempo gasto em subchamadas de outras funções. Retorne um array com o tempo exclusivo de cada função.

**Exemplos:**
```
Input:  n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
Explicação:
Função 0 começa em t=0, executa até chamar a função 1 em t=2 (2 unidades: t=0,1).
Função 1 executa de t=2 a t=5 (4 unidades: t=2,3,4,5).
Função 0 retoma em t=6, executa 1 unidade (t=6).
Total função 0: 2+1=3. Total função 1: 4.

Input:  n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Output: [8]
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 100`, `2 <= logs.length <= 500` → tamanho pequeno, qualquer solução O(logs.length) é folgada
- `0 <= timestamp <= 10^9` → timestamps grandes, mas a diferença entre eventos consecutivos é o que importa, não o valor absoluto
- Nenhum dois eventos "start" (ou "end") acontecem no mesmo timestamp; toda função tem um "end" para cada "start" → o log é garantidamente bem formado, sem eventos órfãos ou simultâneos ambíguos

## 🧭 Como reconhecer o padrão

O enunciado já entrega a estrutura: "call stack" — LIFO, exatamente como uma pilha de execução real funciona. A função no **topo** da pilha é sempre a que está executando "ativamente" no instante atual; funções abaixo dela estão pausadas, aguardando a função do topo terminar (ou ser interrompida por outra chamada).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada unidade de tempo entre o primeiro e o último timestamp, determinar qual função está no topo da pilha naquele instante (simulando push/pop conforme os logs) e incrementar o tempo exclusivo dessa função em 1.

- Tempo: O(intervalo total de tempo) · Espaço: O(n)
- **Por que não basta:** o intervalo de tempo pode ser até `10^9`, tornando essa simulação unidade-por-unidade completamente inviável. É preciso calcular a duração de cada trecho de execução **diretamente**, sem iterar timestamp por timestamp.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha uma pilha real de IDs de função (ou de pares `[id, timestampInicio]`) e uma variável `anterior` com o timestamp do último evento processado. Para cada log: se for `"start"`, e já havia uma função no topo da pilha, ela estava executando desde `anterior` até este novo `start` — credite `(timestampAtual - anterior)` a ela antes de empilhar a nova função; depois empilhe, e atualize `anterior = timestampAtual`. Se for `"end"`, a função do topo executou desde `anterior` até o fim **inclusive** deste timestamp — credite `(timestampAtual - anterior + 1)` a ela, desempilhe, e atualize `anterior = timestampAtual + 1` (porque "fim do timestamp X" significa que a próxima função só pode começar a contar a partir de X+1).

## 🎬 Exemplo passo a passo

`n=2`, `logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]`

| Passo | Log | Ação | Pilha após | anterior após | res após |
|---|---|---|---|---|---|
| 1 | `0:start:0` | pilha vazia, nada a creditar; empilha (0,0) | `[(0,0)]` | 0 | `[0,0]` |
| 2 | `1:start:2` | credita à função do topo (0): `2-0=2` → res[0]+=2; empilha (1,2) | `[(0,0),(1,2)]` | 2 | `[2,0]` |
| 3 | `1:end:5` | credita ao topo (1): `5-2+1=4` → res[1]+=4; desempilha | `[(0,0)]` | 6 | `[2,4]` |
| 4 | `0:end:6` | credita ao topo (0): `6-6+1=1` → res[0]+=1; desempilha | `[]` | 7 | `[3,4]` |

Resultado final: `[3, 4]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(logs.length) — uma única passada pelos logs, operações O(1) de pilha por log
- **Espaço:** O(n) — a pilha guarda no máximo o nível de aninhamento de chamadas recursivas, limitado por `n` funções distintas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] exclusiveTime(int n, List<String> logs) {
    int[] resposta = new int[n];
    Deque<Integer> pilha = new ArrayDeque<>(); // guarda IDs de função (a call stack real)
    int anterior = 0; // timestamp do último evento processado

    for (String log : logs) {
        String[] partes = log.split(":");
        int id = Integer.parseInt(partes[0]);
        String tipo = partes[1];
        int tempo = Integer.parseInt(partes[2]);

        if (tipo.equals("start")) {
            if (!pilha.isEmpty()) {
                // a função do topo estava executando desde "anterior" até este novo start
                resposta[pilha.peek()] += tempo - anterior;
            }
            pilha.push(id);
            anterior = tempo;
        } else { // "end"
            // a função do topo executa até o FIM deste timestamp, inclusive (+1)
            resposta[pilha.pop()] += tempo - anterior + 1;
            anterior = tempo + 1; // a próxima execução só começa a contar a partir daqui
        }
    }

    return resposta;
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

- Esquecer o `+1` ao processar `"end"` — "fim do timestamp X" inclui a própria unidade X na contagem, ao contrário de "início do timestamp X" (que ainda não consumiu tempo algum quando o evento acontece); confundir os dois gera contagens sistematicamente erradas em 1 unidade.
- Creditar tempo à função errada em `"start"` — o crédito antes de empilhar vai para a função que estava no **topo antes** desse novo `start` (a que está sendo interrompida), não para a função recém-iniciada.
- Não tratar recursão corretamente — quando a mesma função se chama recursivamente, ela aparece múltiplas vezes na pilha (em posições diferentes); o código não precisa de lógica especial para isso, porque a pilha trata cada chamada como uma entrada independente, mesmo que o `id` se repita.
- Esquecer de atualizar `anterior` em **ambos** os ramos (`start` e `end`) — sem isso, o próximo cálculo de intervalo usaria um timestamp desatualizado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem sobreposição de chamadas | `n=1, logs=["0:start:0","0:end:0"]` | `[1]` | uma única unidade de tempo (start e end no mesmo timestamp) |
| Recursão simples | `n=1, logs=["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]` | `[8]` | a mesma função se chama recursivamente múltiplas vezes |
| Duas funções alternando | `n=2, logs=["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]` | `[7,1]` | testa transição entre funções diferentes, não só recursão |
| Chamada única sem interrupção | `n=1, logs=["0:start:0","0:end:10"]` | `[11]` | intervalo simples do início ao fim, inclusive |

## 🔗 Conexões

- Problemas irmãos: [0682] Baseball Game (mesma ideia de simular estado sequencial com pilha), [0227] Basic Calculator II (outra simulação orientada a eventos processados sequencialmente)
- No backend: essa técnica de calcular tempo exclusivo por frame de execução é exatamente o que profilers de performance fazem (ex.: flame graphs, `perf`, profilers de linguagens de programação) para determinar quanto tempo cada função gastou "sozinha" versus quanto foi delegado a chamadas aninhadas — fundamental para identificar gargalos reais de performance.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
