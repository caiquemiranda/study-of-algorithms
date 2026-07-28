# [1695] Maximum Erasure Value

> 🔗 [LeetCode 1695](https://leetcode.com/problems/maximum-erasure-value/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dado um array de inteiros positivos `nums`, você quer apagar um subarray contendo **elementos únicos**. A pontuação obtida ao apagar o subarray é igual à **soma** de seus elementos. Retorne a **pontuação máxima** que você pode obter apagando **exatamente um** subarray.

**Exemplos:**
```
Input:  nums = [4,2,4,5,6]
Output: 17
Explicação: o subarray ótimo aqui é [2,4,5,6].

Input:  nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explicação: o subarray ótimo é [5,2,1] ou [1,2,5].
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `1 <= nums[i] <= 10^4` → valores positivos, sem impacto na monotonicidade da soma (mas isso aqui não é o que importa — o que importa é a unicidade)

## 🧭 Como reconhecer o padrão

"Maior subarray de elementos únicos, maximizando uma soma" é o mesmo padrão de [0003] Longest Substring Without Repeating Characters, mas mantendo uma SOMA em vez de um comprimento: expande-se a janela; ao encontrar um duplicado, encolhe-se pela esquerda até ele sumir da janela.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, checar se todos os elementos são únicos (usando um `Set`) e somar.

- Tempo: O(n³) (O(n²) subarrays, O(n) para validar e somar cada um) · Espaço: O(n) por checagem
- **Por que não basta:** revalida a unicidade e recalcula a soma do zero a cada subarray candidato, mesmo quando ele é apenas o anterior estendido em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um `Set` com os valores da janela atual e uma soma corrente. Ao encontrar um valor já presente no set, encolha pela esquerda (removendo do set e subtraindo da soma) até o duplicado sumir. Adicione o novo valor e atualize a melhor soma.

## 🎬 Exemplo passo a passo

`nums = [4,2,4,5,6]`

| right | valor | Já visto na janela? | Ação | sum | melhor |
|---|---|---|---|---|---|
| 0 | 4 | não | adiciona | 4 | 4 |
| 1 | 2 | não | adiciona | 6 | 6 |
| 2 | 4 | sim | remove nums[0]=4 até sumir da janela → left=1, sum=2; adiciona o novo 4 | 6 | 6 |
| 3 | 5 | não | adiciona | 11 | 11 |
| 4 | 6 | não | adiciona | 17 | 17 |

Resultado final: `17` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n) para o set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maximumUniqueSubarray(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    int left = 0;
    int windowSum = 0;
    int best = 0;

    for (int right = 0; right < nums.length; right++) {
        while (seen.contains(nums[right])) {
            seen.remove(nums[left]);
            windowSum -= nums[left];
            left++;
        }
        seen.add(nums[right]);
        windowSum += nums[right];
        best = Math.max(best, windowSum);
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

- "Elementos únicos" refere-se a valores únicos DENTRO da janela atual, não no array inteiro — o mesmo valor pode reaparecer depois que sai da janela.
- É o mesmo padrão de [0003] Longest Substring Without Repeating Characters, mas mantendo uma SOMA em vez de um comprimento.
- Esquecer de subtrair `nums[left]` de `windowSum` ao encolher deixa a soma inflada, contando elementos que já saíram da janela.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Todos únicos | `[1,2,3]` | 6 | array inteiro já serve |
| Todos iguais | `[5,5,5]` | 5 | só um elemento cabe por vez na janela |
| Duplicata logo no início | `[5,2,1,2,5,2,1,2,5]` | 8 | melhor janela é [5,2,1] ou [1,2,5], soma 8 |
| Exemplo do enunciado | `[4,2,4,5,6]` | 17 | melhor janela é [2,4,5,6] |

## 🔗 Conexões

- Problemas irmãos: [0003] Longest Substring Without Repeating Characters (mesmíssima técnica, mas maximizando comprimento em vez de soma), [3090] Maximum Length Substring With Two Occurrences (mesma família de limitar repetições numa janela)
- No backend: calcular o maior "lote" de itens distintos processáveis em sequência, somando seus valores, útil em sistemas que não permitem processar o mesmo item duas vezes num mesmo ciclo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
