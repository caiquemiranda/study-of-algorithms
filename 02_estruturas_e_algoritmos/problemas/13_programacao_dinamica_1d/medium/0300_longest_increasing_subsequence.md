# [0300] Longest Increasing Subsequence

> 🔗 [LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/) · Dificuldade: 🟡 medium · Categoria: [`13_programacao_dinamica_1d`](../../../fundamentos/13_programacao_dinamica_1d.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ProgramacaoDinamica1D` `#BuscaBinaria` `#Medium`

## 📜 O Problema

Dado um array de inteiros `nums`, retorne o **tamanho** da maior subsequência **estritamente crescente** (os elementos não precisam ser contíguos, só manter a ordem relativa).

**Exemplos:**
```
Input:  nums = [10,9,2,5,3,7,101,18]    Output: 4   (subsequência [2,3,7,101])
Input:  nums = [0,1,0,3,2,3]            Output: 4
Input:  nums = [7,7,7,7,7,7,7]          Output: 1   (repetidos não formam subsequência crescente)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 2500` → O(n²) chega a ~6.25 milhões de operações, tranquilamente aceitável — mas não O(2^n)
- **Follow up:** "Can you come up with an algorithm that runs in O(n log(n))?" → sinaliza que existe uma técnica além da DP O(n²), usando busca binária (ver Conexões)
- "subsequência" (não "subarray") → os elementos escolhidos não precisam ser contíguos, só preservar a ordem original — é isso que torna o problema exponencial na força bruta (cada elemento pode ou não entrar na subsequência)

## 🧭 Como reconhecer o padrão

"Maior/menor subsequência com uma propriedade" que depende apenas de decisões anteriores (incluir ou não cada elemento, comparando com o que veio antes) é a assinatura de **programação dinâmica 1D**: defina um estado `dp[i]` = "a resposta considerando o problema até o índice `i`", e construa a solução combinando resultados de subproblemas menores.

## 🐢 Solução 1 — Força bruta

Para cada elemento, decidir recursivamente se ele entra ou não na subsequência (explorando as duas opções), comparando sempre com o último elemento escolhido.

- Tempo: O(2^n) — cada um dos `n` elementos tem 2 escolhas independentes · Espaço: O(n) de pilha de recursão
- **Por que não basta:** com `n` até 2500, `2^n` é astronomicamente inviável. Ignora que muitos desses subproblemas se repetem (a mesma pergunta "qual a maior subsequência crescente começando aqui, dado que o último valor escolhido foi X" aparece várias vezes) — é exatamente o que a programação dinâmica evita recalcular.

## 💡 Solução 2 — A ideia otimizada (intuição)

Defina `dp[i]` = **o tamanho da maior subsequência crescente que termina exatamente no índice `i`**. Para calcular `dp[i]`, olhe todos os índices `j < i`: se `nums[j] < nums[i]`, então dá para "estender" a subsequência que termina em `j` — `dp[i] = max(dp[i], dp[j] + 1)`. Se nenhum `j` anterior tiver valor menor, `dp[i] = 1` (a subsequência é o próprio elemento sozinho).

A resposta final é o **maior valor entre todos os `dp[i]`** (a subsequência ótima pode terminar em qualquer posição, não necessariamente na última).

## 🎬 Exemplo passo a passo

`nums = [10, 9, 2, 5, 3, 7, 101, 18]`

| i | nums[i] | Melhor j < i com nums[j] < nums[i] | dp[i] |
|---|---|---|---|
| 0 | 10 | nenhum | 1 |
| 1 | 9 | nenhum (10 não é < 9) | 1 |
| 2 | 2 | nenhum | 1 |
| 3 | 5 | j=2 (nums[2]=2, dp[2]=1) | 2 |
| 4 | 3 | j=2 (nums[2]=2, dp[2]=1) | 2 |
| 5 | 7 | j=3 ou j=4 (dp=2) | 3 |
| 6 | 101 | j=5 (nums[5]=7, dp[5]=3) | 4 |
| 7 | 18 | j=5 (nums[5]=7, dp[5]=3) | 4 |

Resultado final: `max(dp) = 4` ✔ (a subsequência `[2,3,7,101]`, refletida em dp[6], ou `[2,3,7,18]` refletida em dp[7])

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) — para cada `i`, olha todos os `j < i`
- **Espaço:** O(n) — o array `dp`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int lengthOfLIS(int[] nums) {
    int n = nums.length;
    int[] dp = new int[n];
    Arrays.fill(dp, 1);          // toda posição sozinha já é uma subsequência de tamanho 1

    int maior = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                // Estende a subsequência que termina em j, se isso melhorar dp[i].
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        maior = Math.max(maior, dp[i]);
    }
    return maior;
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

- **Achar que `dp[n-1]` (o último índice) já é a resposta**: a subsequência ótima pode terminar em QUALQUER posição — é preciso tirar o máximo de todo o array `dp`, não só olhar a última célula.
- **Usar `<=` em vez de `<` na comparação**: o problema pede **estritamente** crescente — `[7,7,7]` tem LIS de tamanho 1, não 3; usar `<=` contaria repetições como válidas.
- **Confundir subsequência com subarray**: a subsequência não precisa ser contígua — `nums[j]` pode estar muito antes de `nums[i]` no array, desde que `j < i`. Um erro comum é só comparar elementos vizinhos.
- **Esquecer a inicialização `dp[i] = 1`**: todo elemento sozinho é uma subsequência crescente válida de tamanho 1 — sem essa base, o cálculo de `max` fica incorreto para elementos sem nenhum `j` anterior menor.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento | `nums=[5]` | 1 | borda mínima |
| Todos iguais | `nums=[7,7,7,7,7,7,7]` | 1 | testa "estritamente" crescente |
| Já ordenado crescente | `nums=[1,2,3,4,5]` | 5 | LIS é o array inteiro |
| Ordenado decrescente | `nums=[5,4,3,2,1]` | 1 | nenhum par forma sequência crescente |
| Exemplo do enunciado | `nums=[10,9,2,5,3,7,101,18]` | 4 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0673] Number of Longest Increasing Subsequence** (mesma DP, mas conta quantas LIS existem), **[0354] Russian Doll Envelopes** (LIS disfarçado em 2 dimensões), **[1143] Longest Common Subsequence** (DP 2D irmã, mesma família de "subsequência ótima")
- No backend: encontrar a maior sequência de eventos "compatíveis entre si" respeitando uma ordem (ex.: o maior conjunto de versões de dependências que podem ser atualizadas em ordem crescente sem conflito) usa o mesmo raciocínio de DP sobre subsequências.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente à otimização O(n log n) via *patience sorting*: manter um array `tails` onde `tails[k]` é o menor valor final possível de uma subsequência crescente de tamanho `k+1`, atualizado a cada elemento novo com uma busca binária pela posição de substituição). Essa técnica O(n log n) é real e mais rápida, mas o problema é classicamente um problema de programação dinâmica — a tabela de decisão deste repositório lista LIS explicitamente como sinal de `13_programacao_dinamica_1d`, e a DP O(n²) já resolve dentro do limite do enunciado (n ≤ 2500). Documento classificado em `13_programacao_dinamica_1d`, com a técnica de busca binária citada aqui como otimização avançada para quem quiser o desafio extra.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
