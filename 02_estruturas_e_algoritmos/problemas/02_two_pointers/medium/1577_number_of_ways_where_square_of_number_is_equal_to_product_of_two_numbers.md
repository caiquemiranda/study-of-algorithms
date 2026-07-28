# [1577] Number of Ways Where Square of Number Is Equal to Product of Two Numbers

> 🔗 [LeetCode 1577](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Medium`

## 📜 O Problema

Dados dois arrays `nums1` e `nums2`, conte triplas de dois tipos: **Tipo 1** — `(i,j,k)` com `nums1[i]² == nums2[j] * nums2[k]` (`j < k`); **Tipo 2** — o mesmo só que com os papéis dos arrays trocados. Retorne o total combinado.

**Exemplos:**
```
Input:  nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explicação: 4² = 2 * 8.

Input:  nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explicação: todo elemento vale 1, qualquer combinação serve.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums1.length, nums2.length <= 1000` → uma busca ingênua O(n1×n2²) pode passar de 10⁹; O((n1+n2) log(n1+n2)) é o alvo
- `1 <= nums1[i], nums2[i] <= 10^5` → o quadrado de um elemento (até `10^10`) e o produto de dois (também até `10^10`) **estouram `int`**; é obrigatório usar `long`
- Dois tipos de triplas → são contagens independentes que se somam no resultado final

## 🧭 Como reconhecer o padrão

"Contar pares `(j,k)` num array cujo produto bate com um valor-alvo" é resolvido ordenando o array e usando dois ponteiros nas pontas: o produto de `arr[left] * arr[right]` só pode crescer (avançando `left`) ou diminuir (recuando `right`) de forma previsível num array ordenado, permitindo contar todos os pares válidos sem testar cada combinação.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada elemento de `nums1` (ou `nums2`), testar TODOS os pares `j < k` do outro array, verificando diretamente se o produto bate com o quadrado.

- Tempo: O(n1×n2² + n2×n1²) — pode passar de 10⁹ operações no pior caso · Espaço: O(1)
- **Por que não basta:** testa pares que, num array ordenado, poderiam ser descartados em bloco (produto claramente maior ou menor que o alvo); ordenar uma vez e usar dois ponteiros elimina toda essa varredura repetida.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene o array "alvo dos pares" (ex.: `nums2`, pra contar triplas Tipo 1). Para cada elemento de `nums1`, calcule `alvo = elemento²` e conte quantos pares `(left, right)` em `nums2` têm produto igual a `alvo`, usando dois ponteiros: se o produto for menor que o alvo, avance `left` (precisa de um produto maior); se for maior, recue `right`; se for igual, conte o(s) par(es) — cuidando de **empates** (quando há duplicatas, a contagem não é 1, é uma combinação). Repita o processo trocando os papéis dos dois arrays para as triplas Tipo 2, e some os dois totais.

## 🎬 Exemplo passo a passo

`nums1 = [7,4]`, `nums2 = [5,2,8,9]` → `nums2` ordenado: `[2,5,8,9]`

Contagem de pares em `nums2` com produto igual a `4² = 16` (o caso de `x=4` em `nums1`, que é onde está o único triplet válido):

| Passo | left (valor) | right (valor) | produto | Comparação | Ação |
|---|---|---|---|---|---|
| 1 | 0 (2) | 3 (9) | 18 | `18 > 16` | recua `right` |
| 2 | 0 (2) | 2 (8) | 16 | `16 == 16`, valores diferentes | conta `1×1=1` par; avança `left`, recua `right` |
| 3 | 1 | 1 | — | `left >= right` | loop termina |

Para `x=7` (target 49) e para todo `y` de `nums2` contra `nums1` ordenado (Tipo 2), a contagem é 0. Total: `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n1 log n1 + n2 log n2 + n1×log(n2) "amortizado" pela varredura) — na prática, O((n1+n2) log(n1+n2) + n1 + n2), já que cada chamada de contagem com dois ponteiros é O(tamanho do array ordenado)
- **Espaço:** O(log n) para o sort, mais o array clonado a ser ordenado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public long numTriplets(int[] nums1, int[] nums2) {
    return countType(nums1, nums2) + countType(nums2, nums1);
}

// conta triplas onde o quadrado de um elemento de "a" bate com um par (j<k) de "b"
private long countType(int[] a, int[] b) {
    int[] sortedB = b.clone();
    Arrays.sort(sortedB);
    long total = 0;
    for (int x : a) {
        long target = (long) x * x; // long: x pode ser até 10^5, x*x até 10^10
        total += countPairsWithProduct(sortedB, target);
    }
    return total;
}

private long countPairsWithProduct(int[] arr, long target) {
    int left = 0;
    int right = arr.length - 1;
    long count = 0;

    while (left < right) {
        long prod = (long) arr[left] * arr[right];
        if (prod < target) {
            left++;
        } else if (prod > target) {
            right--;
        } else if (arr[left] == arr[right]) {
            // todo elemento no intervalo [left, right] é igual: C(n, 2) pares
            long n = right - left + 1;
            count += n * (n - 1) / 2;
            break;
        } else {
            // conta quantas repetições existem de cada lado antes de avançar
            int countL = 1;
            while (left + 1 < right && arr[left + 1] == arr[left]) {
                left++;
                countL++;
            }
            int countR = 1;
            while (right - 1 > left && arr[right - 1] == arr[right]) {
                right--;
                countR++;
            }
            count += (long) countL * countR;
            left++;
            right--;
        }
    }

    return count;
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

- Não usar `long` para os produtos e quadrados — `10^5` ao quadrado já é `10^10`, que estoura `int` (limite ~2,1×10⁹); tanto o alvo quanto o produto comparado precisam ser `long`.
- Tratar um empate (`arr[left] == arr[right]`, todo o intervalo igual) como "1 par só" — quando há `n` elementos iguais nesse intervalo, o número de pares é `C(n,2) = n×(n-1)/2`, não `1`.
- Esquecer de somar as contribuições dos DOIS tipos (Tipo 1 vindo de `nums1`, Tipo 2 vindo de `nums2`) — são contagens independentes que se somam no resultado final, não uma escolhida em vez da outra.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo do enunciado | `nums1=[7,4]`, `nums2=[5,2,8,9]` | 1 | só um triplet Tipo 1 válido |
| Muitos empates | `nums1=[1,1]`, `nums2=[1,1,1]` | 9 | todo elemento vale 1, qualquer combinação serve |
| Dois triplets, tipos diferentes | `nums1=[7,7,8,3]`, `nums2=[1,2,9,7]` | 2 | um Tipo 1 e um Tipo 2 |
| Nenhum triplet possível | `nums1=[2]`, `nums2=[3,5]` | 0 | `2²=4`, e `3×5=15≠4`; nenhuma combinação bate |

## 🔗 Conexões

- Problemas irmãos: [0015] 3Sum (mesma técnica de dois ponteiros contando/achando pares com uma soma-alvo, aqui adaptada pra produto), [1099] Two Sum Less Than K (mesma família de contar pares que satisfazem uma condição numérica usando ordenação + dois ponteiros)
- No backend: contar combinações de registros de duas tabelas que satisfazem uma relação numérica exata — por exemplo, casar transações de crédito e débito cujo produto/soma bate com um valor de referência, evitando o produto cartesiano completo ao ordenar e usar dois ponteiros.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
