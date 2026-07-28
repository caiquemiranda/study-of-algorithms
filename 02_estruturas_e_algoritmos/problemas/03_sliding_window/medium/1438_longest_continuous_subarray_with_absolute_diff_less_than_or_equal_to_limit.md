# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

> 🔗 [LeetCode 1438](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#MonotonicQueue` `#Medium`

## 📜 O Problema

Dado um array de inteiros `nums` e um inteiro `limit`, retorne o tamanho do maior subarray **não vazio** tal que a diferença absoluta entre quaisquer dois elementos desse subarray seja menor ou igual a `limit`.

**Exemplos:**
```
Input:  nums = [8,2,4,7], limit = 4
Output: 2

Input:  nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explicação: o subarray [2,4,7,2] tem diferença máxima |2-7|=5 <= 5.

Input:  nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) recalculando max/min a cada janela é arriscado; O(n) é o esperado
- `1 <= nums[i] <= 10^9`, `0 <= limit <= 10^9` → a condição depende só do MAIOR e do MENOR elemento da janela (a diferença entre esses dois já cobre qualquer par)

## 🧭 Como reconhecer o padrão

"Maior janela onde a diferença entre o maior e o menor elemento respeita um limite" exige saber o máximo e o mínimo da janela atual em tempo O(1) enquanto ela desliza — a estrutura certa é um **deque monotônico**: um deque decrescente (para o máximo) e outro crescente (para o mínimo), cada um guardando índices e descartando do fim qualquer valor que nunca mais poderia ser o extremo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, calcular o máximo e o mínimo do subarray percorrendo-o inteiro.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula max/min do zero a cada subarray candidato, ignorando que apenas um elemento muda entre janelas vizinhas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha dois deques de índices: `maxDeque` (decrescente, o maior valor sempre na frente) e `minDeque` (crescente, o menor sempre na frente). Ao incluir um novo elemento, remova do FIM de cada deque todo valor "dominado" pelo novo (nunca mais seria extremo). A diferença entre as frentes dos dois deques é a diferença max-min da janela inteira; enquanto exceder `limit`, encolha pela esquerda, removendo das frentes os índices que saíram da janela.

## 🎬 Exemplo passo a passo

`nums = [10,1,2,4,7,2]`, `limit = 5`

| Evento | maxDeque (valores) | minDeque (valores) | max | min | diff | Ação | melhor |
|---|---|---|---|---|---|---|---|
| right=0: inclui 10 | [10] | [10] | 10 | 10 | 0 | válida | 1 |
| right=1: inclui 1 | [10,1] | [1] | 10 | 1 | 9 | encolhe (left=1) → maxDeque=[1] | 1 (janela [1,1]) |
| right=2: inclui 2 | [2] | [1,2] | 2 | 1 | 1 | válida | 2 |
| right=3: inclui 4 | [4] | [1,2,4] | 4 | 1 | 3 | válida | 3 |
| right=4: inclui 7 | [7] | [1,2,4,7] | 7 | 1 | 6 | encolhe (left=2) → minDeque=[2,4,7] | 3 (janela [2,4]) |
| right=5: inclui 2 | [7,2] | [2,2] | 7 | 2 | 5 | válida | 4 |

Resultado final: `4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada índice entra e sai de cada deque no máximo uma vez
- **Espaço:** O(n) no pior caso para os deques

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int longestSubarray(int[] nums, int limit) {
    Deque<Integer> maxDeque = new ArrayDeque<>(); // índices, valores decrescentes do topo
    Deque<Integer> minDeque = new ArrayDeque<>(); // índices, valores crescentes do topo
    int left = 0;
    int best = 0;

    for (int right = 0; right < nums.length; right++) {
        while (!maxDeque.isEmpty() && nums[maxDeque.peekLast()] < nums[right]) {
            maxDeque.pollLast();
        }
        maxDeque.addLast(right);

        while (!minDeque.isEmpty() && nums[minDeque.peekLast()] > nums[right]) {
            minDeque.pollLast();
        }
        minDeque.addLast(right);

        while (nums[maxDeque.peekFirst()] - nums[minDeque.peekFirst()] > limit) {
            left++;
            if (maxDeque.peekFirst() < left) {
                maxDeque.pollFirst();
            }
            if (minDeque.peekFirst() < left) {
                minDeque.pollFirst();
            }
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
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

- Os deques guardam ÍNDICES, não valores diretamente — isso permite saber quando um elemento "sai" da janela (comparando o índice na frente do deque com `left`).
- Ao inserir um novo elemento, remove-se do FIM do deque todo valor que nunca mais poderia ser o máximo/mínimo (por já ser "dominado" pelo novo elemento) — é isso que mantém o deque monotônico e o topo sempre correto em O(1).
- Comparar `nums[maxDeque.peekFirst()] - nums[minDeque.peekFirst()]` dá a diferença entre o MAIOR e o MENOR da janela inteira, que é sempre `>=` a diferença entre quaisquer dois elementos dela — checar só essa diferença já garante a condição para TODOS os pares.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| limit=0 (só repetições) | `nums=[4,2,2,2,4,4,2,2]`, `limit=0` | 3 | maior trecho de valores idênticos consecutivos |
| Array de um elemento | `nums=[5]`, `limit=0` | 1 | um único elemento sempre tem diff=0 |
| Array inteiro cabe | `nums=[1,2,3]`, `limit=100` | 3 | limite folgado o bastante pro array todo |
| Exemplo do enunciado | `nums=[10,1,2,4,7,2]`, `limit=5` | 4 | subarray [2,4,7,2] (índices 2-5) tem diff máximo 5 |

## 🔗 Conexões

- Problemas irmãos: [0239] Sliding Window Maximum (mesma técnica-base de deque monotônico para manter o máximo de uma janela em O(1) amortizado), [1004] Max Consecutive Ones III (mesma família de janela variável com uma condição de validade a checar a cada passo)
- No backend: detectar o maior intervalo de tempo onde uma métrica (latência, temperatura) se manteve dentro de uma faixa de variação aceitável, sem picos nem quedas abruptas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
