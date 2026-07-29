# [2389] Longest Subsequence With Limited Sum

> 🔗 [LeetCode 2389](https://leetcode.com/problems/longest-subsequence-with-limited-sum/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#PrefixSum` `#Greedy` `#Easy`

## 📜 O Problema

Você recebe um array `nums` de tamanho `n` e um array `queries` de tamanho `m`. Para cada `queries[i]`, retorne o **maior tamanho** de uma subsequência de `nums` cuja soma seja `<= queries[i]`.

**Exemplos:**
```
Input:  nums = [4,5,2,1], queries = [3,10,21]    Output: [2,3,4]
        - soma <= 3: melhor é [2,1], tamanho 2
        - soma <= 10: melhor é [4,5,1], tamanho 3
        - soma <= 21: melhor é [4,5,2,1] (soma 12), tamanho 4
Input:  nums = [2,3,4,5], queries = [1]          Output: [0]
        (nem o menor elemento cabe: subsequência vazia)
```

**Restrições (e o que elas denunciam):**
- `1 <= n, m <= 1000` → força bruta testando todas as subsequências é exponencial, inviável; mesmo O(n×m) simples (1 milhão) seria aceitável, mas existe algo melhor e mais elegante
- `1 <= nums[i], queries[i] <= 10^6` → valores positivos, então "maior subsequência com soma <= q" é sempre resolvida escolhendo os **menores elementos primeiro** (uma escolha gulosa/greedy)
- Repetir a mesma pergunta para `m` queries diferentes → sinaliza pré-processar `nums` **uma vez** (ordenar + prefix sum) e responder cada query rapidamente, em vez de recalcular do zero

## 🧭 Como reconhecer o padrão

Como todo elemento é positivo, para maximizar o **tamanho** da subsequência dado um limite de soma, a escolha gulosa ótima é sempre pegar os elementos **menores primeiro** (eles "custam menos soma" por unidade de tamanho). Isso reduz o problema a: ordene `nums`, monte o array de **soma prefixada**, e para cada query ache — via busca binária — quantos elementos do prefixo cabem dentro do limite.

## 🐢 Solução 1 — Força bruta

Para cada query, tentar todas as subsequências possíveis (ou, de forma um pouco melhor, ordenar `nums` e somar elemento por elemento até estourar o limite, refazendo essa soma do zero a cada query).

- Tempo: O(n log n + m × n) — ordena uma vez, mas soma linearmente para cada query · Espaço: O(1) extra além da ordenação
- **Por que não basta:** somar do zero para cada query repete trabalho que já foi feito para queries anteriores — construir a soma prefixada **uma única vez** transforma cada consulta subsequente numa busca binária O(log n) em vez de uma soma O(n).

## 💡 Solução 2 — A ideia otimizada (intuição)

1. Ordene `nums` em ordem crescente — os menores elementos vêm primeiro (greedy: para caber o máximo de elementos, sempre prefira os mais baratos).
2. Construa o array de **soma prefixada**: `prefixo[i]` = soma dos `i+1` menores elementos.
3. Para cada `query`, faça busca binária (upper bound) pela **última posição do prefixo que ainda é `<= query`** — essa posição (+1, por ser 0-indexada) é o tamanho máximo da subsequência.

Como `prefixo` é estritamente crescente (todos os elementos são positivos), a busca binária funciona sem ambiguidade.

## 🎬 Exemplo passo a passo

`nums = [4,5,2,1]` → ordenado: `[1,2,4,5]` → `prefixo = [1,3,7,12]`

Query `= 10` (upper bound: quantos elementos do prefixo são `<= 10`)

| Passo | left | mid | right | prefixo[mid] | Comparação | Decisão |
|---|---|---|---|---|---|---|
| 1 | 0 | 2 (val 7) | 3 | 7 | 7 <= 10 → candidato válido | guarda contagem 3, `left = 3` |
| 2 | 3 | 3 (val 12) | 3 | 12 | 12 > 10 → não serve | `right = 2` |
| 3 | 3 | — | 2 | `left > right` → fim | — | melhor contagem: 3 |

Resultado para query=10: `3` ✔ (repetindo para queries 3 e 21: `2` e `4`)

Resultado final: `[2, 3, 4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O((n + m) log n) — ordenar custa O(n log n); cada uma das `m` queries custa O(log n) de busca binária no prefixo
- **Espaço:** O(n) — o array de soma prefixada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] answerQueries(int[] nums, int[] queries) {
    Arrays.sort(nums);                       // greedy: menores elementos primeiro maximizam o tamanho

    int[] prefixo = new int[nums.length];
    prefixo[0] = nums[0];
    for (int i = 1; i < nums.length; i++) {
        prefixo[i] = prefixo[i - 1] + nums[i];   // prefixo[i] = soma dos i+1 menores elementos
    }

    int[] resposta = new int[queries.length];
    for (int i = 0; i < queries.length; i++) {
        resposta[i] = contarDentroDoLimite(prefixo, queries[i]);
    }
    return resposta;
}

// Busca binária: quantos elementos do prefixo (estritamente crescente) são <= limite.
private int contarDentroDoLimite(int[] prefixo, int limite) {
    int left = 0, right = prefixo.length - 1;
    int melhorContagem = 0;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (prefixo[mid] <= limite) {
            melhorContagem = mid + 1;        // +1 porque mid é índice 0-based, mas queremos a CONTAGEM
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return melhorContagem;
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

- **Esquecer de ordenar `nums` antes de construir o prefixo**: sem ordenar, o prefixo não representa "os k menores elementos", e a busca binária perde o sentido — a soma dos primeiros k elementos do array original pode não ser a mínima possível para tamanho k.
- **Confundir índice com contagem**: `mid` é 0-indexado, mas a resposta é uma contagem — sempre `mid + 1`, não `mid`.
- **Query menor que o menor elemento**: deve retornar `0` (subsequência vazia) — a busca binária lida com isso naturalmente já que nenhum prefixo será `<= query`, mas vale testar explicitamente (ver exemplo 2 do enunciado).
- **Recalcular a soma para cada query**: é a armadilha mais comum — sem o prefixo pré-computado, cada query custaria O(n), e com `m` até 1000 isso ainda passaria, mas perde toda a elegância (e a escalabilidade) da técnica de busca binária sobre prefix sum.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Query menor que o menor elemento | `nums=[2,3,4,5], queries=[1]` | `[0]` | subsequência vazia, testa contagem zero |
| Query cobre tudo | `nums=[2,3,4,5], queries=[100]` | `[4]` | todos os elementos cabem |
| Um elemento, uma query | `nums=[5], queries=[5]` | `[1]` | borda mínima, cabe exatamente |
| Múltiplas queries variadas | `nums=[4,5,2,1], queries=[3,10,21]` | `[2,3,4]` | trace acima, cobre os três regimes |
| Elementos repetidos | `nums=[2,2,2], queries=[4]` | `[2]` | prefixo com valores iguais não quebra a busca (ainda estritamente crescente na soma) |

## 🔗 Conexões

- Problemas irmãos: **[1608] Special Array With X Elements Greater Than or Equal X** (busca binária depois de ordenar), **[1539] Kth Missing Positive Number** (busca binária sobre uma sequência derivada), **[0035] Search Insert Position** (o template de busca binária usado aqui)
- No backend: responder repetidamente "quantos itens cabem num orçamento" (ex.: quantos itens de um carrinho cabem dentro de um limite de peso/frete, escolhendo os mais baratos primeiro) é resolvido pré-computando a soma acumulada ordenada uma única vez e respondendo cada pergunta com busca binária, em vez de recalcular a cada requisição.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
