# [0622] Design Circular Queue

> 🔗 [LeetCode 622](https://leetcode.com/problems/design-circular-queue/) · Dificuldade: 🟡 medium · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Array` `#Design` `#RingBuffer` `#Medium`

## 📜 O Problema

Projete uma fila circular (ring buffer) de capacidade fixa `k`, seguindo FIFO. Implemente `MyCircularQueue`:
- `MyCircularQueue(k)`: inicializa com capacidade `k`.
- `enQueue(value)`: insere um elemento; retorna `true` se bem-sucedido.
- `deQueue()`: remove um elemento; retorna `true` se bem-sucedido.
- `Front()` / `Rear()`: retornam o primeiro/último elemento, ou `-1` se vazia.
- `isEmpty()` / `isFull()`: checam o estado da fila.

Não é permitido usar a fila (`Queue`) pronta da linguagem.

**Exemplos:**
```
Input:
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
[null, true, true, true, false, 3, true, true, true, 4]

Explicação: capacidade 3. Insere 1,2,3 (todas true); insere 4 (false, cheia);
Rear() → 3; isFull() → true; deQueue() → true (remove o 1); insere 4 (true, há espaço agora);
Rear() → 4
```

**Restrições (e o que elas denunciam):**
- `1 <= k <= 1000`, até `3000` chamadas → capacidade pequena e fixa, conhecida desde o construtor — não há necessidade de crescer dinamicamente
- "sem usar a fila pronta da linguagem" → obriga a implementar o mecanismo de FIFO manualmente
- **Capacidade fixa e conhecida de antemão** → é a peça-chave: com capacidade fixa, um **array circular** (índices andando em módulo `k`) resolve todas as operações em O(1), sem nunca precisar realocar nem deslocar elementos — não há vantagem em usar uma lista encadeada aqui, porque o problema não precisa da flexibilidade de crescer além de `k`

## 🧭 Como reconhecer o padrão

"Estrutura FIFO de capacidade fixa, reaproveitando o espaço liberado" é a assinatura do **array circular (ring buffer)**: em vez de deslocar elementos ao remover do início (como um array comum faria), os índices de início e fim "andam" em módulo `k`, reaproveitando as posições livres deixadas por remoções anteriores. É uma técnica de array, não de linked list — mesmo que uma lista duplamente encadeada também resolvesse o problema, ela gastaria memória extra por nó (ponteiros) sem ganhar nada em troca, já que a capacidade nunca ultrapassa `k`.

## 🐢 Solução 1 — Força bruta (lista dinâmica, removendo sempre do início)

Usa uma lista dinâmica comum (`ArrayList`). `enQueue` adiciona no fim; `deQueue` remove o elemento do **início** com `remove(0)`.

- Tempo: `enQueue` O(1) amortizado, mas `deQueue` é O(n) — remover o primeiro elemento de um `ArrayList` desloca todos os elementos seguintes uma posição para trás · Espaço: O(k)
- **Por que não basta:** com até 3000 chamadas, `deQueue`s repetidos custando O(n) cada podem custar até O(n × chamadas) no total — desperdício claro quando a capacidade é fixa e pequena. O array circular resolve `deQueue` em O(1) verdadeiro, sem deslocar nada, "andando" o índice de início em vez de mover os dados.

## 💡 Solução 2 — A ideia otimizada (intuição)

Um array de tamanho fixo `k`, mais um índice `head` (posição do elemento mais antigo) e um contador `count` (quantos elementos estão ocupados). A posição do próximo elemento a inserir (`tail`) é sempre `(head + count) % k` — o módulo é o que faz o índice "dar a volta" para o início do array quando chega ao fim, reaproveitando espaços liberados por `deQueue`s anteriores. `enQueue` escreve em `tail` e incrementa `count`; `deQueue` só anda `head = (head + 1) % k` e decrementa `count` — nenhum dado é fisicamente movido em nenhuma das duas operações.

## 🎬 Exemplo passo a passo

`MyCircularQueue(3)`, sequência do enunciado

| Operação | `head` antes | `count` antes | Ação | Array (posições ocupadas) | Retorno |
|---|---|---|---|---|---|
| `enQueue(1)` | 0 | 0 | `tail=(0+0)%3=0`; `buf[0]=1` | `[1,_,_]` | `true` |
| `enQueue(2)` | 0 | 1 | `tail=(0+1)%3=1`; `buf[1]=2` | `[1,2,_]` | `true` |
| `enQueue(3)` | 0 | 2 | `tail=(0+2)%3=2`; `buf[2]=3` | `[1,2,3]` | `true` |
| `enQueue(4)` | 0 | 3 | `count == k` → cheia | `[1,2,3]` | `false` |
| `Rear()` | — | 3 | `buf[(0+3-1)%3] = buf[2]` | — | `3` |
| `isFull()` | — | 3 | `count == k` | — | `true` |
| `deQueue()` | 0 | 3 | `head=(0+1)%3=1`; `count=2` | `[_,2,3]` (posição 0 "livre") | `true` |
| `enQueue(4)` | 1 | 2 | `tail=(1+2)%3=0`; `buf[0]=4` (reaproveita a posição livre!) | `[4,2,3]` | `true` |
| `Rear()` | — | 3 | `buf[(1+3-1)%3] = buf[0]` | — | `4` |

Resultado final: `[null, true, true, true, false, 3, true, true, true, 4]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) para todas as operações — só aritmética de índice, nenhum deslocamento nem alocação
- **Espaço:** O(k) — um único array alocado uma vez no construtor, nunca redimensionado

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MyCircularQueue {
    private final int[] buf;
    private int head; // índice do elemento mais ANTIGO (o próximo a sair)
    private int count; // quantos slots estão ocupados agora

    public MyCircularQueue(int k) {
        buf = new int[k];
        head = 0;
        count = 0;
    }

    public boolean enQueue(int value) {
        if (isFull()) return false;
        int tail = (head + count) % buf.length; // % faz o índice "dar a volta" ao chegar no fim
        buf[tail] = value;
        count++;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % buf.length; // só anda o índice — o valor antigo em buf[head] não é apagado, só ignorado
        count--;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : buf[head];
    }

    public int Rear() {
        return isEmpty() ? -1 : buf[(head + count - 1) % buf.length];
    }

    public boolean isEmpty() {
        return count == 0;
    }

    public boolean isFull() {
        return count == buf.length;
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

- **Usar só `head` e `tail` sem um contador (`count`) para distinguir "vazia" de "cheia"**: quando `head == tail`, isso pode significar tanto fila vazia quanto fila cheia — sem `count` (ou sem sacrificar um slot do array como sentinela), essa ambiguidade quebra `isEmpty`/`isFull`.
- **Esquecer o módulo (`% buf.length`) ao calcular `tail` ou ao avançar `head`**: sem ele, o índice cresce indefinidamente e estoura os limites do array assim que a fila "dá a volta" depois de vários ciclos de enQueue/deQueue.
- **Calcular `Rear()` como `buf[tail]` diretamente**: `tail` (a próxima posição livre) não é o último elemento válido — o último elemento válido está em `(head + count - 1) % k`, uma posição antes de onde o próximo `enQueue` escreveria.
- **"Limpar" o valor antigo em `deQueue`**: não é necessário (nem eficiente) zerar `buf[head]` ao remover — o valor antigo simplesmente é ignorado até ser sobrescrito por um `enQueue` futuro; tentar limpá-lo é trabalho extra sem benefício.

## 🧪 Casos de teste para validar

| Caso | Sequência | Esperado | Por quê |
|---|---|---|---|
| Fila vazia | `Front()`/`Rear()` sem nenhum `enQueue` | `-1` em ambos | `isEmpty()` verdadeiro logo de início |
| Capacidade 1 | `k=1; enQueue(5); enQueue(6)` | `true`, depois `false` | a fila enche com um único elemento |
| Encher e esvaziar completamente | `k=2; enQueue(1); enQueue(2); deQueue(); deQueue(); isEmpty()` | `true` no final | valida que `count` volta a 0 corretamente |
| Dar a volta no array (wrap-around) | `k=3`, sequência do enunciado | `[null,true,true,true,false,3,true,true,true,4]` | trace acima — o índice `tail` volta para `0` depois do `deQueue` |
| `deQueue` em fila vazia | `deQueue()` sem nenhum `enQueue` antes | `false` | `isEmpty()` bloqueia a remoção |

## 🔗 Conexões

- Problemas irmãos: **[0641] Design Circular Deque** (mesma técnica de array circular, mas permitindo inserir/remover também pela frente), **[0232] Implement Queue using Stacks** (outra forma de implementar uma fila do zero, mas com duas pilhas em vez de array circular)
- No backend: o array circular é a estrutura por trás de **ring buffers de sistemas de logging** (buffer circular de tamanho fixo que sobrescreve os registros mais antigos), **buffers de áudio/vídeo em streaming** (produtor escreve, consumidor lê, ambos "andando" em círculo sobre o mesmo bloco de memória) e implementações de fila lock-free de alta performance, onde evitar realocação e deslocamento de memória é crítico para desempenho.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
