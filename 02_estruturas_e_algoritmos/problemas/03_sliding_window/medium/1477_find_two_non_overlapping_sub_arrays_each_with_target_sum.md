# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum

> 🔗 [LeetCode 1477](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dado um array de inteiros `arr` e um inteiro `target`, encontre **dois subarrays não sobrepostos** de `arr`, cada um com soma igual a `target`. Pode haver múltiplas respostas; você precisa encontrar aquela com a **menor** soma dos comprimentos dos dois subarrays. Retorne essa soma mínima, ou `-1` se não for possível.

**Exemplos:**
```
Input:  arr = [3,2,2,4,3], target = 3
Output: 2
Explicação: só dois subarrays têm soma 3 ([3] e [3]). A soma dos comprimentos é 2.

Input:  arr = [7,3,4,7], target = 7
Output: 2
Explicação: existem três subarrays de soma 7, mas escolhemos o primeiro e o terceiro ([7] e [7]).

Input:  arr = [4,3,2,6,2,3,4], target = 6
Output: -1
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `1 <= arr[i] <= 1000` → **todos os valores são positivos**, permitindo a técnica de dois ponteiros pra achar subarrays de soma exata

## 🧭 Como reconhecer o padrão

"Dois subarrays não sobrepostos com soma-alvo, minimizando a soma dos comprimentos" combina dois ponteiros (para achar, em cada `right`, o subarray de soma exata terminando ali) com um array auxiliar `best[i]` que guarda o menor comprimento de um subarray válido encontrado ATÉ o índice `i` — permitindo combinar qualquer subarray novo com o melhor "anterior" sem risco de sobreposição.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de subarrays `(i,j)` não sobrepostos, checar se ambos somam `target` e minimizar a soma dos comprimentos.

- Tempo: O(n³) ou pior · Espaço: O(1)
- **Por que não basta:** testa combinações de pares de subarrays exaustivamente, quando a soma sendo sempre positiva permite achar candidatos de forma incremental com dois ponteiros.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use dois ponteiros para encontrar, a cada `right`, se `[left, right]` soma exatamente `target` (encolhendo `left` enquanto a soma exceder). Mantenha um array `best[i]` = menor comprimento de subarray válido visto até `i`. Sempre que encontrar um novo subarray válido `[left, right]`, combine seu comprimento com `best[left-1]` (o melhor ANTES dele, garantindo não-sobreposição) para atualizar a resposta.

## 🎬 Exemplo passo a passo

`arr = [3,2,2,4,3]`, `target = 3`

| right | arr[right] | sum após shrink | ==target? | curLen | Combina com best[left-1]? | minLen até aqui | result |
|---|---|---|---|---|---|---|---|
| 0 | 3 | 3 | sim | 1 | left=0, sem combinação | 1 | ∞ |
| 1 | 2 | 2 (encolheu) | não | — | — | 1 | ∞ |
| 2 | 2 | 2 (encolheu) | não | — | — | 1 | ∞ |
| 3 | 4 | 0 (encolheu) | não | — | — | 1 | ∞ |
| 4 | 3 | 3 | sim | 1 | best[3]=1 → result=1+1=2 | 1 | 2 |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n) para o array `best`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minSumOfLengths(int[] arr, int target) {
    int n = arr.length;
    int[] best = new int[n]; // best[i] = menor comprimento de subarray válido terminando em ou antes de i
    Arrays.fill(best, Integer.MAX_VALUE);

    int left = 0;
    long sum = 0;
    int minLen = Integer.MAX_VALUE;
    int result = Integer.MAX_VALUE;

    for (int right = 0; right < n; right++) {
        sum += arr[right];

        while (sum > target) {
            sum -= arr[left];
            left++;
        }

        if (sum == target) {
            int curLen = right - left + 1;
            if (left > 0 && best[left - 1] != Integer.MAX_VALUE) {
                result = Math.min(result, best[left - 1] + curLen);
            }
            minLen = Math.min(minLen, curLen);
        }

        best[right] = minLen;
    }

    return result == Integer.MAX_VALUE ? -1 : result;
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

- `best[i]` guarda o MENOR comprimento de subarray válido encontrado até o índice `i` (inclusive) — não o comprimento do subarray que termina exatamente em `i`. Isso é o que permite combinar com um subarray posterior sem se preocupar com sobreposição.
- A combinação só é válida usando `best[left-1]` (o melhor ANTES do início da janela atual) — usar `best[right]` ou qualquer índice dentro da janela atual causaria sobreposição entre os dois subarrays.
- Como os valores são positivos, a técnica de encolher a janela é segura; sem essa garantia, seria necessário prefix sums com busca em vez de dois ponteiros.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só um subarray possível | `arr=[4,3,2,6,2,3,4]`, `target=6` | -1 | só existe um subarray com soma 6, não dá pra formar o par |
| Múltiplas opções, escolhe a melhor combinação | `arr=[7,3,4,7]`, `target=7` | 2 | [7] e [7] (índices 0 e 3) somam comprimento 2, melhor que [7] e [3,4] |
| Subarrays adjacentes mínimos | `arr=[3,2,2,4,3]`, `target=3` | 2 | [3] no início e [3] no fim, cada um de comprimento 1 |
| target maior que qualquer soma possível | `arr=[1,1]`, `target=10` | -1 | nenhum subarray sequer atinge o alvo sozinho |

## 🔗 Conexões

- Problemas irmãos: [0209] Minimum Size Subarray Sum (mesma técnica-base de dois ponteiros para achar o subarray mínimo com uma condição de soma), [1031] Maximum Sum of Two Non-Overlapping Subarrays (mesma família de combinar dois segmentos não sobrepostos, aqui minimizando comprimento total em vez de maximizar soma)
- No backend: encontrar os dois menores lotes de transações não sobrepostos que juntos atingem um valor-alvo específico, útil em conciliação de pagamentos parcelados.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
