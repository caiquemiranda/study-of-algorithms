# [0641] Design Circular Deque

> 🔗 [LeetCode 641](https://leetcode.com/problems/design-circular-deque/) · Dificuldade: 🟡 medium · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Array` `#Design` `#RingBuffer` `#Medium`

## 📜 O Problema

Projete uma deque circular (fila dupla) de capacidade fixa `k`. Implemente `MyCircularDeque`:
- `MyCircularDeque(k)`: inicializa com capacidade `k`.
- `insertFront(value)` / `insertLast(value)`: insere na frente/no fim; retorna `true` se bem-sucedido.
- `deleteFront()` / `deleteLast()`: remove da frente/do fim; retorna `true` se bem-sucedido.
- `getFront()` / `getRear()`: retornam o primeiro/último elemento, ou `-1` se vazia.
- `isEmpty()` / `isFull()`: checam o estado.

**Exemplos:**
```
Input:
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
[null, true, true, true, false, 2, true, true, true, 4]

Explicação: capacidade 3. insertLast(1) → [1]; insertLast(2) → [1,2]; insertFront(3) → [3,1,2];
insertFront(4) → false (cheia); getRear() → 2; isFull() → true;
deleteLast() → [3,1]; insertFront(4) → [4,3,1]; getFront() → 4
```

**Restrições (e o que elas denunciam):**
- `1 <= k <= 1000`, até `2000` chamadas → capacidade pequena e fixa, mesma natureza do LC 622
- **Capacidade fixa e conhecida** + **inserção/remoção pelos DOIS lados** → é a generalização direta do array circular: em vez de só um índice `head` que avança para frente (fila simples), aqui `head` também precisa **andar para trás** (`insertFront`), o que exige cuidado extra com módulo de número negativo

## 🧭 Como reconhecer o padrão

Mesma assinatura do LC 622 (array circular por capacidade fixa conhecida), mas agora nos dois sentidos: "insira/remova tanto na frente quanto no fim, em O(1), com capacidade fixa" continua sendo resolvido com aritmética de índices em módulo `k` — só que agora o índice de início (`head`) pode se mover em **qualquer direção**.

## 🐢 Solução 1 — Força bruta (lista dinâmica, inserindo/removendo nas duas pontas)

Usa uma `ArrayList`. `insertLast`/`deleteLast` operam no fim (O(1) amortizado); `insertFront`/`deleteFront` operam no início, exigindo deslocar todos os outros elementos uma posição — `add(0, value)` e `remove(0)` são O(n).

- Tempo: O(1) para operações no fim, mas **O(n)** para operações na frente · Espaço: O(k)
- **Por que não basta:** metade das operações do problema (`insertFront`/`deleteFront`) fica O(n) nessa abordagem — com até 2000 chamadas, isso pode custar até O(n × chamadas) no total. Um array circular resolve as quatro operações (frente e fim) em O(1) verdadeiro, sem deslocar nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

O mesmo array de tamanho fixo `k`, índice `head` e contador `count` do LC 622 — mas agora `head` também pode **retroceder**: para `insertFront`, calcula-se a nova posição andando `head` uma casa para trás **em módulo `k`**, usando `(head - 1 + k) % k` (o `+ k` antes do módulo evita índice negativo, já que a maioria das linguagens não trata módulo de número negativo do jeito "matemático"). `insertLast` continua igual ao LC 622 (escreve em `(head + count) % k`). `deleteFront` anda `head` para frente; `deleteLast` só precisa **encolher `count`** — a posição lógica do antigo último elemento simplesmente deixa de contar, sem precisar mover `head`.

## 🎬 Exemplo passo a passo

`MyCircularDeque(3)`, sequência do enunciado

| Operação | `head` antes | `count` antes | Ação | Deque lógica (frente→fim) | Retorno |
|---|---|---|---|---|---|
| `insertLast(1)` | 0 | 0 | `tail=(0+0)%3=0`; `buf[0]=1` | `[1]` | `true` |
| `insertLast(2)` | 0 | 1 | `tail=(0+1)%3=1`; `buf[1]=2` | `[1,2]` | `true` |
| `insertFront(3)` | 0 | 2 | `head=(0-1+3)%3=2`; `buf[2]=3` | `[3,1,2]` | `true` |
| `insertFront(4)` | 2 | 3 | `count == k` → cheia | `[3,1,2]` | `false` |
| `getRear()` | — | 3 | `buf[(2+3-1)%3] = buf[1] = 2` | — | `2` |
| `isFull()` | — | 3 | `count == k` | — | `true` |
| `deleteLast()` | 2 | 3 | `count--` (não mexe em `head`) | `[3,1]` | `true` |
| `insertFront(4)` | 2 | 2 | `head=(2-1+3)%3=1`; `buf[1]=4` (reaproveita a posição do antigo `2`) | `[4,3,1]` | `true` |
| `getFront()` | — | 3 | `buf[head] = buf[1] = 4` | — | `4` |

Resultado final: `[null, true, true, true, false, 2, true, true, true, 4]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) para todas as operações — só aritmética de índice, sem deslocamento
- **Espaço:** O(k) — um único array alocado uma vez

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MyCircularDeque {
    private final int[] buf;
    private int head; // índice do elemento da FRENTE
    private int count;

    public MyCircularDeque(int k) {
        buf = new int[k];
        head = 0;
        count = 0;
    }

    public boolean insertFront(int value) {
        if (isFull()) return false;
        // "+ buf.length" antes do módulo evita índice negativo: head pode estar em 0,
        // e 0 - 1 = -1 não é um índice válido sem essa correção.
        head = (head - 1 + buf.length) % buf.length;
        buf[head] = value;
        count++;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) return false;
        int tail = (head + count) % buf.length;
        buf[tail] = value;
        count++;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) return false;
        head = (head + 1) % buf.length;
        count--;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) return false;
        count--; // basta encolher: a posição lógica do antigo último elemento some sem mover head
        return true;
    }

    public int getFront() {
        return isEmpty() ? -1 : buf[head];
    }

    public int getRear() {
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

- **Esquecer o `+ buf.length` antes do módulo em `insertFront`**: `(head - 1) % buf.length` pode dar um índice **negativo** quando `head == 0` (dependendo da linguagem, módulo de número negativo não "dá a volta" para o final do array automaticamente) — Java, por exemplo, mantém o sinal do dividendo em `%`.
- **Mover `head` em `deleteLast`**: `deleteLast` remove o elemento do **fim**, não do início — `head` não deve mudar, só `count` diminui.
- **Reaproveitar a lógica do LC 622 sem adaptar `insertFront`**: o LC 622 (fila simples) só precisa de `head` andando para frente; aqui, ignorar a possibilidade de `head` andar para trás faz `insertFront` sempre falhar ou calcular a posição errada.
- **Calcular `getRear()` sem usar `count`**: assim como no LC 622, o último elemento válido está em `(head + count - 1) % k`, nunca em um índice fixo — a posição "física" do fim muda conforme elementos entram e saem dos dois lados.

## 🧪 Casos de teste para validar

| Caso | Sequência | Esperado | Por quê |
|---|---|---|---|
| Deque vazia | `getFront()`/`getRear()` sem inserções | `-1` em ambos | `isEmpty()` verdadeiro |
| `insertFront` fazendo `head` cruzar o índice 0 | `k=3; insertLast(1); insertFront(2); insertFront(3)` | todas `true`; deque lógica `[3,2,1]` | valida o `+ buf.length` no cálculo de `head` |
| Capacidade 1, inserindo dos dois lados | `k=1; insertFront(1); insertLast(2)` | `true`, depois `false` (cheia com 1 elemento) | garante que `isFull` funciona mesmo com `k=1` |
| Esvaziar e reencher totalmente | `k=2; insertLast(1); insertLast(2); deleteFront(); deleteFront(); isEmpty()` | `true` no final | valida que `count` volta a 0 corretamente após remoções dos dois tipos |
| Exemplo do enunciado | sequência completa acima | `[null,true,true,true,false,2,true,true,true,4]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0622] Design Circular Queue** (a versão mais simples deste problema, só com inserção no fim e remoção na frente), **[0239] Sliding Window Maximum** (usa uma deque, embora não circular, para manter candidatos de uma janela deslizante)
- No backend: uma deque circular de capacidade fixa é o mecanismo por trás de **buffers de histórico "undo" com limite** (ex.: manter só as últimas N ações, descartando a mais antiga ao adicionar uma nova além do limite) e de **work-stealing queues** usadas em runtimes de processamento paralelo, onde threads inserem/removem tarefas de ambas as pontas de uma fila compartilhada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
