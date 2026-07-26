# [1051] Height Checker

> 🔗 [LeetCode 1051](https://leetcode.com/problems/height-checker/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Sorting` `#CountingSort` `#Easy`

## 📜 O Problema

Uma escola vai tirar uma foto anual de todos os alunos. Os alunos precisam ficar em fila em **ordem não-decrescente** de altura. Essa ordem é representada pelo array `expected`, onde `expected[i]` é a altura esperada do `i`-ésimo aluno na fila.

Você recebe um array `heights` representando a **ordem atual** em que os alunos estão. Retorne **o número de índices** onde `heights[i] != expected[i]`.

**Exemplos:**
```
Input:  heights = [1,1,4,2,1,3]
Output: 3
Explicação:
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Índices 2, 4 e 5 não batem.

Input:  heights = [5,1,2,3,4]
Output: 5
Explicação: todos os índices não batem.

Input:  heights = [1,2,3,4,5]
Output: 0
Explicação: todos os índices batem.
```

**Restrições (e o que elas denunciam):**
- `1 <= heights.length <= 100`, `1 <= heights[i] <= 100` → entrada pequena E valores pequenos, ambas abordagens (sort padrão ou counting sort) resolvem com folga
- "ordem não-decrescente" → a referência (`expected`) é simplesmente o array ordenado

## 🧭 Como reconhecer o padrão

"Compare a ordem atual com a ordem que DEVERIA ser" é sempre resolvido gerando a versão ordenada como referência e comparando posição a posição — a única decisão de design é COMO gerar essa referência ordenada (sort genérico vs. counting sort, já que os valores são pequenos e limitados).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, descobrir "qual deveria ser a altura esperada nesta posição" contando, na força bruta, quantos elementos são menores ou iguais a `heights[i]` (um "rank" calculado do zero para cada posição).

- Tempo: O(n²) — para cada posição, recalcula o rank comparando com todos os outros elementos · Espaço: O(1) extra
- **Por que não basta:** recalcula informação de ordenação relativa que poderia ser obtida de uma vez só ordenando o array, em vez de refazer comparações O(n) para cada uma das n posições.

## 💡 Solução 2 — A ideia otimizada (intuição)

Crie uma cópia de `heights`, ordene essa cópia (é o array `expected`). Percorra ambos os arrays em paralelo, contando quantas posições têm valores diferentes.

## 🎬 Exemplo passo a passo

`heights = [1,1,4,2,1,3]`, `expected (ordenado) = [1,1,1,2,3,4]`

| Passo | i | heights[i] | expected[i] | diferente? | contador |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 1 | não | 0 |
| 2 | 1 | 1 | 1 | não | 0 |
| 3 | 2 | 4 | 1 | **sim** | 1 |
| 4 | 3 | 2 | 2 | não | 1 |
| 5 | 4 | 1 | 3 | **sim** | 2 |
| 6 | 5 | 3 | 4 | **sim** | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; poderia ser O(n + k) com counting sort, já que as alturas são limitadas a [1,100]
- **Espaço:** O(n) — para a cópia ordenada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int heightChecker(int[] heights) {
    int[] expected = heights.clone();
    Arrays.sort(expected); // a ordem "correta" é simplesmente o array ordenado

    int foraDeOrdem = 0;
    for (int i = 0; i < heights.length; i++) {
        if (heights[i] != expected[i]) {
            foraDeOrdem++;
        }
    }
    return foraDeOrdem;
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

- Esquecer de clonar o array antes de ordenar (`Arrays.sort(heights)` diretamente) — isso destruiria a ordem original de `heights`, que ainda é necessária para a comparação.
- Achar que precisa comparar VALORES relativos (ranking) em vez de comparar diretamente `heights[i] != expected[i]` — a comparação direta já é suficiente, pois `expected` é literalmente a versão ordenada de `heights`.
- Ignorar que counting sort (array de contagem de tamanho 101, já que alturas vão de 1 a 100) seria uma otimização válida aqui, dado o limite pequeno de valores — não é necessário para passar, mas é a resposta "ideal" sugerida pelas tags do problema.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Parcialmente fora de ordem | `[1,1,4,2,1,3]` | 3 | caso padrão do enunciado |
| Totalmente invertido | `[5,1,2,3,4]` | 5 | todas as posições diferem da esperada |
| Já ordenado | `[1,2,3,4,5]` | 0 | nenhuma posição difere |
| Todos iguais | `[3,3,3]` | 0 | array constante já está "ordenado" |

## 🔗 Conexões

- Problemas irmãos: [1122] Relative Sort Array (mesma família de comparar contra uma ordem de referência), [0075] Sort Colors (mesmo domínio de counting sort com valores limitados a um intervalo pequeno)
- No backend: validação de filas ou rankings (ex.: verificar quantos itens de uma lista de prioridade estão fora da ordem esperada antes de reprocessar, ou detectar quantos registros de um relatório não batem com a ordenação canônica esperada).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
