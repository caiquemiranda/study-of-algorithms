# [0532] K-diff Pairs in an Array

> 🔗 [LeetCode 532](https://leetcode.com/problems/k-diff-pairs-in-an-array/) · Dificuldade: 🟡 medium · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-29 · Revisões: —

Tags: `#ArraysEHashing` `#BuscaBinaria` `#Medium`

## 📜 O Problema

Dado um array de inteiros `nums` e um inteiro `k`, retorne a quantidade de pares **k-diff únicos**: pares `(nums[i], nums[j])` com `i != j` e `|nums[i] - nums[j]| == k`.

**Exemplos:**
```
Input:  nums = [3,1,4,1,5], k = 2    Output: 2   (pares (1,3) e (3,5) — repetições de valor não contam de novo)
Input:  nums = [1,2,3,4,5], k = 1    Output: 4   ((1,2),(2,3),(3,4),(4,5))
Input:  nums = [1,3,1,5,4], k = 0    Output: 1   (só (1,1): dois elementos IGUAIS contam se k=0)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → força bruta O(n²) chega a 10^8, arriscado; existe algo em O(n)
- `0 <= k <= 10^7` → **`k` pode ser zero**, um caso especial importante: pares com diferença 0 exigem valores **iguais** (não distintos), então a lógica muda de "existe o complemento?" para "esse valor se repete?"
- "pares **únicos**" → a resposta conta **valores distintos** que formam pares, não pares de índices — repetições do mesmo valor (`1` aparecendo duas vezes no exemplo 1) não geram pares extras

## 🧭 Como reconhecer o padrão

"Para cada valor, existe outro valor a uma distância fixa `k`?" é o padrão de **complemento via hash**, o mesmo do Two Sum: para cada número `x`, o parceiro que resolveria a condição é `x + k` (ou `x - k`, mas basta checar uma direção se percorrer todos os valores únicos). Contar ocorrências com um hash map resolve tanto o caso geral (`k > 0`) quanto o caso especial (`k = 0`) sem precisar ordenar nada.

## 🐢 Solução 1 — Força bruta

Para cada par `(i, j)` com `i < j`, verificar se `|nums[i] - nums[j]| == k`, guardando pares de **valores** já contados para não repetir.

- Tempo: O(n²) · Espaço: O(n) para os pares já vistos · **Por que não basta:** com `n` até 10^4, o número de pares chega a ~5×10^7 — funciona, mas contando ocorrências primeiro (hash map), a resposta sai em uma única passada por valor único, sem comparar todos os pares.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um hash map de **contagem de ocorrências** de cada valor em `nums`. Depois:
- Se `k == 0`: conte quantos valores têm contagem `>= 2` (esses formam um par consigo mesmo, já que precisam de dois índices diferentes com o mesmo valor).
- Se `k > 0`: para cada valor **único** `x` no mapa, verifique se `x + k` também existe no mapa — se existir, é um par válido. Como cada `x` é único, não há risco de contar o mesmo par duas vezes (checar só `x + k`, nunca `x - k`, evita contar `(x, x+k)` e `(x+k, x)` como pares diferentes).

## 🎬 Exemplo passo a passo

`nums = [3, 1, 4, 1, 5]`, `k = 2`

| Passo | Estrutura | Elemento | Ação | Estado |
|---|---|---|---|---|
| 1 | contagem = `{}` | (construção) | conta ocorrências de cada valor | `{3:1, 1:2, 4:1, 5:1}` |
| 2 | pares = 0 | x=3 | `3+2=5` está no mapa? sim | pares=1 |
| 3 | pares = 1 | x=1 | `1+2=3` está no mapa? sim | pares=2 |
| 4 | pares = 2 | x=4 | `4+2=6` está no mapa? não | pares=2 |
| 5 | pares = 2 | x=5 | `5+2=7` está no mapa? não | pares=2 |

Resultado final: `2` ✔ (pares (1,3) e (3,5), cada valor único processado uma vez)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para contar, outra para checar cada valor único (no máximo `n` valores distintos)
- **Espaço:** O(n) — o hash map de contagem

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findPairs(int[] nums, int k) {
    Map<Integer, Integer> contagem = new HashMap<>();
    for (int x : nums) {
        contagem.merge(x, 1, Integer::sum);
    }

    int pares = 0;
    for (Map.Entry<Integer, Integer> entrada : contagem.entrySet()) {
        int valor = entrada.getKey();

        if (k == 0) {
            // Caso especial: par (valor, valor) exige DUAS ocorrências do mesmo número.
            if (entrada.getValue() >= 2) {
                pares++;
            }
        } else {
            // Caso geral: procura o "complemento" valor+k (não precisa checar valor-k
            // também, pois cada par só é contado a partir do menor dos dois valores).
            if (contagem.containsKey(valor + k)) {
                pares++;
            }
        }
    }
    return pares;
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

- **Esquecer o caso especial `k == 0`**: sem tratamento próprio, `valor + 0 == valor` sempre "encontraria a si mesmo" no mapa — mas isso não garante que existam **dois índices diferentes** com esse valor. É preciso checar `contagem[valor] >= 2`, não apenas a existência da chave.
- **`k` negativo**: o enunciado garante `k >= 0`, mas vale entender por quê: `|nums[i]-nums[j]|` é sempre não negativo, então `k` negativo nunca teria solução — não é um caso de borda que o código precisa tratar aqui.
- **Checar `valor - k` além de `valor + k`**: gera contagem duplicada — cada par `(a, a+k)` já é encontrado uma única vez ao processar o valor `a` e checar `a+k`; checar a direção oposta a partir de `a+k` contaria o mesmo par de novo.
- **Confundir "pares de valores únicos" com "pares de índices"**: a resposta conta combinações de **valores distintos**, não quantas vezes fisicamente aparecem no array — o exemplo 1 tem dois `1`s, mas isso não dobra a contagem de pares.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 sem repetição | `nums=[1,2,3,4], k=0` | 0 | nenhum valor se repete |
| k=0 com repetição | `nums=[1,3,1,5,4], k=0` | 1 | testa o caso especial (trace do terceiro exemplo) |
| Todos consecutivos | `nums=[1,2,3,4,5], k=1` | 4 | testa cadeia completa de pares |
| Sem nenhum par válido | `nums=[1,2,3], k=10` | 0 | diferença maior que qualquer par possível |
| Exemplo do enunciado | `nums=[3,1,4,1,5], k=2` | 2 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[1346] Check If N and Its Double Exist** (mesmo padrão de complemento via hash, checando `2x` em vez de `x+k`), **[0001] Two Sum** (a raiz do padrão de complemento)
- No backend: encontrar pares de registros com uma diferença fixa (ex.: transações separadas por exatamente um valor de taxa específico, ou eventos de log espaçados por um intervalo fixo de tempo) usa a mesma técnica de contagem por hash em vez de comparar todos os pares.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tags do LeetCode incluindo `two-pointers`, `binary-search`, `sorting` — abordagens válidas que exigem ordenar primeiro, O(n log n)), mas a técnica ótima é contagem por hash map em O(n), sem qualquer ordenação. Por isso o documento foi classificado em `01_arrays_e_hashing`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
