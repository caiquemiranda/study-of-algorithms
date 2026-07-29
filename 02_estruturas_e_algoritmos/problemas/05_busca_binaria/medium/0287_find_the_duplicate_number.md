# [0287] Find the Duplicate Number

> 🔗 [LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Você recebe um array `nums` com `n + 1` inteiros, cada um no intervalo `[1, n]`. Existe **exatamente um** número repetido (pode aparecer 2 ou mais vezes). Encontre esse número **sem modificar o array** e usando **apenas espaço constante**.

**Exemplos:**
```
Input:  nums = [1,3,4,2,2]    Output: 2
Input:  nums = [3,1,3,4,2]    Output: 3
Input:  nums = [3,3,3,3,3]    Output: 3
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^5`, `nums.length == n + 1` → n+1 números espremidos num intervalo de tamanho n: pelo **princípio da casa dos pombos**, pelo menos um valor se repete — é essa garantia que sustenta toda a lógica de contagem
- "without modifying the array" + "constant extra space" → proíbe tanto ordenar in-place com marcação quanto usar hash set (O(n) de espaço) — empurra para uma técnica que só usa contadores
- **Follow up:** "Can you solve in linear runtime?" → sinaliza que existe uma solução O(n) (Floyd's cycle detection, ver Pegadinhas), mas a busca binária sobre o **intervalo de valores** `[1, n]` também resolve elegantemente em O(n log n), sem precisar tratar o array como uma lista encadeada implícita

## 🧭 Como reconhecer o padrão

A pergunta central não é "onde no array está o duplicado", mas "**qual valor** é o duplicado". Isso é **busca binária na resposta**: em vez de buscar num array ordenado, buscamos num intervalo de valores candidatos `[1, n]`, usando o princípio da casa dos pombos como critério de decisão — "quantos elementos de `nums` são `<= mid`? Se forem mais que `mid`, o duplicado está em `[1, mid]`."

## 🐢 Solução 1 — Força bruta

Para cada par `(i, j)` com `i < j`, verificar se `nums[i] == nums[j]`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** com `n` até 10^5, o número de pares chega a ~5×10^9 — inviável. Ignora completamente a estrutura do problema (valores confinados a `[1, n]`), que permite uma abordagem por contagem muito mais direta.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça busca binária no intervalo de **valores** `[1, n]` (não em índices do array). Para cada candidato `mid`, conte quantos elementos de `nums` são `<= mid`:
- Se essa contagem for **maior que `mid`**, então, pelo princípio da casa dos pombos, o duplicado está em `[1, mid]` (há mais números `<= mid` do que valores distintos possíveis nesse intervalo) → busca à **esquerda** (`right = mid`).
- Se a contagem for `<= mid`, o duplicado está em `[mid+1, n]` → busca à **direita** (`left = mid + 1`).

Cada iteração precisa varrer o array inteiro para contar (O(n)), mas o número de iterações é O(log n) — total O(n log n).

## 🎬 Exemplo passo a passo

`nums = [1, 3, 4, 2, 2]` (n = 4)

| Passo | left | mid | right | contagem(nums[i] <= mid) | Comparação | Decisão |
|---|---|---|---|---|---|---|
| 1 | 1 | 2 | 4 | valores <=2: {1,2,2} → 3 | 3 > 2 → duplicado em [1,2] | `right = 2` |
| 2 | 1 | 1 | 2 | valores <=1: {1} → 1 | 1 > 1? não → duplicado em [2,2] | `left = 2` |
| 3 | 2 | — | 2 | `left == right` → fim | — | retorna 2 |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — O(log n) iterações da busca binária, cada uma custando O(n) para contar
- **Espaço:** O(1) — só contadores e ponteiros, sem modificar `nums`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findDuplicate(int[] nums) {
    int left = 1, right = nums.length - 1;   // n = nums.length - 1; valores vão de 1 a n

    while (left < right) {
        int mid = left + (right - left) / 2;

        int contagem = 0;
        for (int x : nums) {
            if (x <= mid) {
                contagem++;
            }
        }

        if (contagem > mid) {
            // Mais elementos <= mid do que valores possíveis nesse intervalo:
            // pelo princípio da casa dos pombos, o duplicado está em [left, mid].
            right = mid;
        } else {
            left = mid + 1;                  // duplicado está em [mid+1, right]
        }
    }
    // left == right: intervalo reduzido a um único valor -> é o duplicado.
    return left;
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

- **Confundir busca binária no VALOR com busca binária no ÍNDICE**: aqui `mid` representa um valor candidato (não uma posição do array) — o array nem precisa estar ordenado para essa técnica funcionar, já que a contagem sempre varre tudo.
- **Usar `>=` em vez de `>` na comparação da contagem**: o critério do princípio da casa dos pombos é estrito — `contagem > mid` (mais elementos do que "slots" disponíveis) é o que garante a existência do duplicado naquele lado.
- **Esquecer que existe uma solução O(n)**: o follow-up do enunciado aponta para o algoritmo de **Floyd (tartaruga e lebre)**, tratando o array como uma lista encadeada implícita (`nums[i]` aponta para o próximo índice) — detectar o ciclo e achar sua entrada dá O(n) tempo com O(1) espaço, estritamente melhor que os O(n log n) da busca binária. É a mesma técnica de [0142] Linked List Cycle II, aplicada sobre índices em vez de ponteiros reais.
- **Tentar modificar o array para marcar visitados**: violaria a restrição explícita do enunciado ("without modifying the array") — mesmo sendo uma solução O(n) tentadora (marcar `nums[|x|]` como negativo), está fora das regras aqui.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Duplicado no início | `nums=[3,1,3,4,2]` | 3 | segundo exemplo do enunciado |
| Todos iguais | `nums=[3,3,3,3,3]` | 3 | caso extremo, todo elemento é o duplicado |
| Menor array possível | `nums=[1,1]` | 1 | borda mínima (n=1) |
| Duplicado é o maior valor | `nums=[1,2,3,4,4]` | 4 | testa fronteira no fim do intervalo [1,n] |
| Exemplo do enunciado | `nums=[1,3,4,2,2]` | 2 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0142] Linked List Cycle II** (mesmíssima técnica de Floyd, mencionada como alternativa O(n) aqui), **[0268] Missing Number** (também envolve valores confinados a um intervalo, mas resolvido com XOR), **[0041] First Missing Positive** (outro problema de "valores como índices" em espaço O(1))
- No backend: detectar um registro duplicado num intervalo fechado de IDs (ex.: validar que um lote de tickets sequenciais não tem número repetido) sem alocar uma estrutura de marcação extra usa esse mesmo raciocínio de contagem por faixa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
