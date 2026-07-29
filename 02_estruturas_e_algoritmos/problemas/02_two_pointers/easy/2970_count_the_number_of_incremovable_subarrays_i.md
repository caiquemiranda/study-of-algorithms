# [2970] Count the Number of Incremovable Subarrays I

> 🔗 [LeetCode 2970](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#TwoPointers` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Você recebe um array `nums` de inteiros **positivos** (0-indexado). Um subarray é **"incremovível"** se, ao removê-lo de `nums`, o que sobra fica **estritamente crescente** (um array vazio conta como estritamente crescente). Retorne a **quantidade total** de subarrays incremovíveis.

**Exemplos:**
```
Input:  nums = [1,2,3,4]    Output: 10
        (o array já é crescente: TODO subarray não vazio é incremovível — são 10 no total)
Input:  nums = [6,5,7,8]    Output: 7
        ([5], [6], [5,7], [6,5], [5,7,8], [6,5,7], [6,5,7,8])
Input:  nums = [8,7,6,6]    Output: 3
        ([8,7,6], [7,6,6], [8,7,6,6] — repare que [8,7] NÃO conta: sobra [6,6], que não é ESTRITAMENTE crescente)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 50` → array minúsculo; até O(n³) (remover e checar cada subarray) roda instantaneamente, mas o padrão certo evita recalcular "é crescente?" do zero a cada remoção
- `1 <= nums[i] <= 50` → valores pequenos, sem risco de overflow
- "estritamente crescente" (não "não decrescente") → repetições quebram a condição — é a pegadinha central do terceiro exemplo (`[6,6]` não serve)

## 🧭 Como reconhecer o padrão

A remoção de um subarray `nums[l..r)` deixa dois pedaços: o **prefixo** `nums[0..l)` e o **sufixo** `nums[r..n)`. Para o resultado ser estritamente crescente, cada pedaço precisa ser crescente **internamente**, e o último elemento do prefixo precisa ser menor que o primeiro do sufixo. Pré-computando "até onde o prefixo continua crescente" e "a partir de onde o sufixo já é crescente", cada remoção vira uma checagem O(1) — e os dois índices `l` e `r` avançam de forma monotônica um em relação ao outro, a marca registrada de **dois ponteiros**.

## 🐢 Solução 1 — Força bruta

Para cada par `(l, r)` com `l < r`, construir o array resultante da remoção de `nums[l..r)` e verificar do zero se ele é estritamente crescente.

- Tempo: O(n³) — O(n²) pares `(l, r)`, cada verificação custando O(n) · Espaço: O(n) para o array temporário
- **Por que não basta:** refaz a checagem "é crescente?" inteira a cada remoção, mesmo que a maior parte do prefixo/sufixo não tenha mudado entre uma tentativa e outra — pré-computar essa informação uma vez evita o trabalho repetido.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pré-compute dois arrays booleanos em O(n):
- `prefixoCrescente[i]` = `true` se `nums[0..i]` (inclusive) é estritamente crescente.
- `sufixoCrescente[i]` = `true` se `nums[i..n-1]` (inclusive) é estritamente crescente.

Se o array inteiro já é crescente (`prefixoCrescente[n-1] == true`), **qualquer** subarray serve — a resposta é o total de subarrays não vazios: `n*(n+1)/2`.

Senão, para cada `l` (fim do prefixo mantido, de `0` a `n`) — mas só enquanto o prefixo `nums[0..l-1]` continuar crescente — teste cada `r` (início do sufixo mantido, de `l+1` a `n`). A remoção `nums[l..r)` é válida se:
1. `r == n` (sufixo vazio) **ou** `sufixoCrescente[r]` for verdadeiro, **e**
2. `l == 0` **ou** `r == n` **ou** `nums[l-1] < nums[r]` (o "encaixe" entre prefixo e sufixo).

Como `l` só avança enquanto o prefixo continua válido, e o `r` mínimo válido nunca diminui conforme `l` cresce, os dois índices se movem de forma consistente — é a essência de dois ponteiros aplicada a fronteiras, em vez de valores.

## 🎬 Exemplo passo a passo

`nums = [6, 5, 7, 8]` → `prefixoCrescente = [T,F,F,F]` (quebra logo em `6>5`), `sufixoCrescente = [F,T,T,T]` (a partir do índice 1, `5,7,8` já é crescente)

| l (prefixo mantido) | r (início do sufixo) | Removido `nums[l..r)` | sufixoCrescente[r] ou r==n? | Encaixe válido? | Conta? |
|---|---|---|---|---|---|
| 0 | 1 | [6] | sim (suf[1]=T) | l==0, sem checar | sim |
| 0 | 2 | [6,5] | sim (suf[2]=T) | l==0 | sim |
| 0 | 3 | [6,5,7] | sim (suf[3]=T) | l==0 | sim |
| 0 | 4 | [6,5,7,8] | r==n | r==n | sim |
| 1 | 2 | [5] | sim (suf[2]=T) | 6 < 7? sim | sim |
| 1 | 3 | [5,7] | sim (suf[3]=T) | 6 < 8? sim | sim |
| 1 | 4 | [5,7,8] | r==n | r==n | sim |
| 2 | — | — | prefixoCrescente[1]=F → `l` para de avançar aqui | — | — |

Resultado final: `7` ✔ (contagem bate exatamente com os 7 subarrays listados no enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) — pré-computo O(n) + até O(n²) pares `(l, r)` testados, cada um em O(1)
- **Espaço:** O(n) — os dois arrays de pré-computação

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int incremovableSubarrayCount(int[] nums) {
    int n = nums.length;

    boolean[] prefixoCrescente = new boolean[n];
    prefixoCrescente[0] = true;
    for (int i = 1; i < n; i++) {
        prefixoCrescente[i] = prefixoCrescente[i - 1] && nums[i - 1] < nums[i];
    }

    // Caso especial: array inteiro já crescente -> todo subarray não vazio serve.
    if (prefixoCrescente[n - 1]) {
        return n * (n + 1) / 2;
    }

    boolean[] sufixoCrescente = new boolean[n];
    sufixoCrescente[n - 1] = true;
    for (int i = n - 2; i >= 0; i--) {
        sufixoCrescente[i] = sufixoCrescente[i + 1] && nums[i] < nums[i + 1];
    }

    int contador = 0;
    for (int l = 0; l <= n; l++) {
        // "l" é o fim do prefixo mantido; ele só é válido se nums[0..l-1] for crescente.
        if (l > 0 && !prefixoCrescente[l - 1]) {
            break;                            // uma vez quebrado, nenhum "l" maior será válido
        }
        for (int r = l + 1; r <= n; r++) {
            boolean sufixoOk = (r == n) || sufixoCrescente[r];
            boolean encaixeOk = (l == 0) || (r == n) || (nums[l - 1] < nums[r]);
            if (sufixoOk && encaixeOk) {
                contador++;
            }
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

- **Confundir "não decrescente" com "estritamente crescente"**: `[6,6]` não é estritamente crescente — é a pegadinha central do terceiro exemplo (`[8,7,6,6]`), onde remover `[8,7]` deixa `[6,6]`, que **não** conta.
- **Esquecer o caso especial do array já crescente**: se `prefixoCrescente[n-1]` já é verdadeiro, TODO subarray não vazio é incremovível (inclusive o array inteiro, que deixa remanescente vazio) — tratar isso separadamente evita ter que testar o "encaixe" numa situação onde ele é sempre trivialmente satisfeito.
- **Esquecer o `r == n` (sufixo vazio)**: remover até o fim do array (`nums[l..n)`) deixa um sufixo vazio, que conta como estritamente crescente por definição do enunciado — sem esse caso especial, a contagem subestima o resultado.
- **Não parar o laço de `l` quando o prefixo quebra**: uma vez que `nums[0..l-1]` deixa de ser crescente, nenhum `l` maior será válido (o prefixo só piora) — continuar testando desperdiça trabalho, embora não gere resposta errada (só mais lento).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Array já crescente | `nums=[1,2,3,4]` | 10 | testa o atalho `n*(n+1)/2` |
| Um elemento | `nums=[5]` | 1 | borda mínima, único subarray possível |
| Duplicatas quebrando encaixe | `nums=[8,7,6,6]` | 3 | testa "estritamente" vs "não decrescente" |
| Decrescente puro | `nums=[3,2,1]` | 6 | remover qualquer subarray contíguo sempre deixa 0, 1 ou 2 elementos, todos triviais |
| Exemplo do enunciado | `nums=[6,5,7,8]` | 7 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[2824] Count Pairs Whose Sum is Less than Target** (mesma ideia de contar em bloco em vez de par a par), **[0128] Longest Consecutive Sequence** (também usa a noção de "sequência crescente contígua")
- No backend: decidir qual trecho de uma sequência de eventos pode ser "descartado" (ex.: logs de retry) sem quebrar uma invariante de ordenação (timestamps crescentes) usa o mesmo raciocínio de pré-computar prefixos/sufixos válidos em vez de revalidar a sequência inteira a cada tentativa.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente à variante "II" com constraints maiores, que de fato usa busca binária), mas para esta versão "I" (n <= 50) a técnica canônica é a varredura com dois índices e pré-computação O(n²), então o documento foi classificado em `02_two_pointers`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
