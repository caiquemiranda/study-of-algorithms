# [2824] Count Pairs Whose Sum is Less than Target

> 🔗 [LeetCode 2824](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#TwoPointers` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Dado um array `nums` (0-indexado) de tamanho `n` e um inteiro `target`, retorne **a quantidade de pares** `(i, j)` com `0 <= i < j < n` tais que `nums[i] + nums[j] < target`.

**Exemplos:**
```
Input:  nums = [-1,1,2,3,1], target = 2    Output: 3
        (pares válidos: (0,1), (0,2), (0,4))
Input:  nums = [-6,2,5,-2,-7,-1,3], target = -2    Output: 10
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length == n <= 50` → array minúsculo; até força bruta O(n²) (no máximo 1225 pares) resolveria instantaneamente, mas o padrão didático certo é ordenar + dois ponteiros
- `-50 <= nums[i], target <= 50` → valores pequenos, sem risco de overflow
- "pares `(i, j)` com `i < j`" → índices originais não importam para a contagem (só interessa quantos pares de **valores** satisfazem a soma), o que libera ordenar o array sem perder informação

## 🧭 Como reconhecer o padrão

"Conte pares cuja soma satisfaz uma desigualdade" num array (depois de ordenado) é o padrão de **dois ponteiros convergentes**: fixe o menor elemento à esquerda e o maior à direita; se a soma dos extremos já satisfaz a condição, **todos os elementos entre eles também satisfazem** (porque estão ordenados) — isso permite contar um bloco inteiro de pares de uma vez, em vez de par por par.

## 🐢 Solução 1 — Força bruta

Para cada par `(i, j)` com `i < j`, verificar se `nums[i] + nums[j] < target` e contar.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** com `n` até 50, funciona tranquilamente, mas ordenando o array primeiro e usando dois ponteiros, a contagem inteira sai em O(n) depois do sort — ensina a técnica que escala para `n` muito maiores.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums`. Use dois ponteiros, `left` no início e `right` no fim:
- Se `nums[left] + nums[right] < target`, então **todo** elemento entre `left+1` e `right` (inclusive), somado a `nums[left]`, também é menor que `target` — porque esses elementos são todos `<= nums[right]`. Some `right - left` ao contador de uma vez só, e avance `left` (para não recontar o mesmo `left` com outros pares menores).
- Se `nums[left] + nums[right] >= target`, a soma está grande demais — `nums[right]` é grande demais para combinar com **qualquer** elemento à esquerda dele nesta rodada; recue `right`.

Continue até `left >= right`.

## 🎬 Exemplo passo a passo

`nums = [-1, 1, 2, 3, 1]` → ordenado: `[-1, 1, 1, 2, 3]`, `target = 2`

| Passo | left (val) | right (val) | soma | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 (-1) | 4 (3) | 2 | 2 < 2? não | `right--` |
| 2 | 0 (-1) | 3 (2) | 1 | 1 < 2? sim | conta `right-left=3`, `left++` |
| 3 | 1 (1) | 3 (2) | 3 | 3 < 2? não | `right--` |
| 4 | 1 (1) | 2 (1) | 2 | 2 < 2? não | `right--` |
| 5 | 1 | 1 | — | `left >= right` → fim | — |

Resultado final: `3` ✔ (contados de uma vez no passo 2: os pares (-1,1), (-1,1) e (-1,2))

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura com dois ponteiros em si é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort da linguagem

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countPairs(List<Integer> nums, int target) {
    Collections.sort(nums);                  // habilita a técnica de dois ponteiros

    int left = 0, right = nums.size() - 1;
    int contador = 0;

    while (left < right) {
        if (nums.get(left) + nums.get(right) < target) {
            // nums[left] combinado com QUALQUER elemento entre left+1 e right
            // também soma menos que target, pois todos são <= nums[right].
            contador += right - left;
            left++;
        } else {
            right--;                          // nums[right] é grande demais para esta rodada
        }
    }
    return contador;
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

- **Contar par por par mesmo depois de ordenar**: perde a vantagem principal da técnica — quando `nums[left]+nums[right] < target`, contar o bloco inteiro de uma vez (`right - left`) é o que torna a varredura O(n) em vez de O(n²).
- **Avançar `right` quando a soma já satisfaz a condição**: inverte a lógica — quando a soma é pequena o suficiente, quem deve avançar é `left` (para explorar novos pares com um valor maior à esquerda), não `right`.
- **Usar `<=` em vez de `<`**: o enunciado pede soma **estritamente** menor que `target` — usar `<=` conta pares demais (ver a nota no próprio enunciado: `(0,3)` não conta porque a soma bate exatamente em `target`, não é menor).
- **Esquecer que `i < j` já está garantido pela técnica**: como `left` sempre fica à esquerda de `right` durante toda a execução, não há risco de contar o mesmo par duas vezes ou parear um elemento consigo mesmo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhum par válido | `nums=[5,5,5], target=1` | 0 | soma mínima (10) já excede o target |
| Todos os pares válidos | `nums=[1,1,1], target=10` | 3 | todos os C(3,2)=3 pares satisfazem |
| Dois elementos, borda mínima | `nums=[1,2], target=10` | 1 | único par possível, satisfaz |
| Com negativos | `nums=[-6,2,5,-2,-7,-1,3], target=-2` | 10 | trace maior do enunciado, testa negativos |
| Exemplo do enunciado | `nums=[-1,1,2,3,1], target=2` | 3 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0167] Two Sum II - Input Array Is Sorted** (mesma técnica de dois ponteiros convergentes), **[2540] Minimum Common Value** (dois ponteiros em arrays já ordenados), **3Sum Smaller (LC 259)** (mesma ideia, uma dimensão a mais: fixa um índice e conta pares com dois ponteiros)
- No backend: contar quantos pares de registros satisfazem uma restrição de soma/diferença (ex.: quantos pares de transações somam menos que um limite de risco) é resolvido com essa mesma técnica depois de ordenar, evitando comparar todos os pares manualmente.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente a buscar o limite de `j` para cada `i` via busca binária), mas a técnica canônica para "contar pares com soma limitada" é dois ponteiros convergentes depois de ordenar, então o documento foi classificado em `02_two_pointers`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
