# [1470] Shuffle the Array

> 🔗 [LeetCode 1470](https://leetcode.com/problems/shuffle-the-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado o array `nums` com `2n` elementos na forma `[x1,x2,...,xn,y1,y2,...,yn]`, retorne o array na forma `[x1,y1,x2,y2,...,xn,yn]`.

**Exemplos:**
```
Input:  nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explicação: como x1=2, x2=5, x3=1, y1=3, y2=4, y3=7, a resposta é [2,3,5,4,1,7].

Input:  nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Input:  nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 500`, `nums.length == 2n` → O(n) resolve com folga

## 🧭 Como reconhecer o padrão

"Reorganizar elementos de posições fixas conhecidas" é sempre um problema de simulação direta O(n): a posição de origem e destino de cada elemento é conhecida pela fórmula do enunciado, não precisa de nenhuma busca.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Já é a solução direta aqui (não existe uma versão mais lenta relevante): construir o array de saída, para cada `i` de 0 a n-1, colocar `nums[i]` (que é `xi`) e `nums[n+i]` (que é `yi`) nas posições `2i` e `2i+1`.

- Tempo: O(n) · Espaço: O(n) para o resultado
- **Por que vale nomear mesmo assim:** a única armadilha é confundir os índices de origem (`i` e `n+i`) com os de destino (`2i` e `2i+1`).

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Crie um array de saída de tamanho `2n`. Percorra `i` de `0` a `n-1`, escrevendo `nums[i]` na posição `2i` e `nums[n+i]` na posição `2i+1`.

## 🎬 Exemplo passo a passo

`nums = [2,5,1,3,4,7]`, `n = 3` — `x = [2,5,1]` (índices 0,1,2), `y = [3,4,7]` (índices 3,4,5)

| Passo | i | xi=nums[i] | yi=nums[n+i] | posição destino |
|---|---|---|---|---|
| 1 | 0 | 2 | 3 | resultado[0]=2, resultado[1]=3 |
| 2 | 1 | 5 | 4 | resultado[2]=5, resultado[3]=4 |
| 3 | 2 | 1 | 7 | resultado[4]=1, resultado[5]=7 |

Resultado final: `[2,3,5,4,1,7]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n) — para o array de saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] shuffle(int[] nums, int n) {
    int[] resultado = new int[2 * n];
    for (int i = 0; i < n; i++) {
        resultado[2 * i] = nums[i];         // xi
        resultado[2 * i + 1] = nums[n + i]; // yi
    }
    return resultado;
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

- Inverter a ordem (`yi` antes de `xi`) — o enunciado pede especificamente `x1,y1,x2,y2,...`, não o contrário.
- Confundir `nums[n+i]` com `nums[i+1]` — o segundo bloco do array (`y`) começa exatamente no índice `n`, não logo após o índice atual.
- Tentar fazer in-place sem um array auxiliar — é possível com truques de codificação em bits, mas é desnecessariamente complexo para o tamanho de entrada deste problema.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | nums=[2,5,1,3,4,7], n=3 | [2,3,5,4,1,7] | intercalação direta dos dois blocos |
| Valores repetidos | nums=[1,1,2,2], n=2 | [1,2,1,2] | duplicatas não afetam a lógica de posição |
| n mínimo | nums=[1,2], n=1 | [1,2] | menor entrada possível, já intercalada |
| Blocos com padrão espelhado | nums=[1,2,3,4,4,3,2,1], n=4 | [1,4,2,3,3,2,4,1] | ilustra intercalação com valores repetidos entre os blocos |

## 🔗 Conexões

- Problemas irmãos: [1528] Shuffle String (mesma ideia de mapear posição de origem para destino), [0189] Rotate Array (mesmo domínio de rearranjo posicional de array)
- No backend: reformatação de dados intercalados (ex.: converter um formato "colunar" de dados em "linhas" para exibição, como juntar arrays paralelos de nome e valor).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
