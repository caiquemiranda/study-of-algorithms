# [0977] Squares of a Sorted Array

> 🔗 [LeetCode 977](https://leetcode.com/problems/squares-of-a-sorted-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array `nums` ordenado em não decrescente (podendo conter negativos), retorne um array com o **quadrado** de cada número, também ordenado em não decrescente.

**Exemplos:**
```
Input:  nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Input:  nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → força bruta O(n log n) já passa, mas o follow-up pede O(n)
- `-10^4 <= nums[i] <= 10^4`, `nums` ordenado → inclui negativos; o valor mais negativo, ao ser elevado ao quadrado, pode virar o MAIOR valor do resultado
- Follow-up pede O(n) → sinaliza que existe uma forma de aproveitar a ordenação original sem reordenar do zero

## 🧭 Como reconhecer o padrão

"O maior resultado só pode vir de uma das duas pontas de um array ordenado" é a assinatura de dois ponteiros nos extremos: como o array tem negativos e positivos, o maior quadrado está sempre no valor de maior **magnitude** — que é ou o mais negativo (ponta esquerda) ou o mais positivo (ponta direita).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Elevar cada elemento ao quadrado e depois ordenar o array resultante com um sort genérico.

- Tempo: O(n log n) · Espaço: O(n) para o array de quadrados (mais o espaço interno do sort)
- **Por que não basta:** ignora que o array original já está ordenado; usar um sort genérico desperdiça essa estrutura. O follow-up pede explicitamente uma solução O(n), que só é possível explorando a ordenação existente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no início e `right` no fim do array original. Compare `nums[left]²` com `nums[right]²`: o **maior** dos dois é, necessariamente, o maior valor de todo o array de resultado ainda não preenchido — coloque-o na **última** posição livre do resultado (preenchendo de trás para frente) e avance o ponteiro correspondente. Repita até os ponteiros se cruzarem.

## 🎬 Exemplo passo a passo

`nums = [-4,-1,0,3,10]` (n=5)

| Passo | left (valor, quadrado) | right (valor, quadrado) | Maior | Ação |
|---|---|---|---|---|
| 1 | 0 (-4, 16) | 4 (10, 100) | 100 (right) | `result[4]=100`; right=3 |
| 2 | 0 (-4, 16) | 3 (3, 9) | 16 (left) | `result[3]=16`; left=1 |
| 3 | 1 (-1, 1) | 3 (3, 9) | 9 (right) | `result[2]=9`; right=2 |
| 4 | 1 (-1, 1) | 2 (0, 0) | 1 (left) | `result[1]=1`; left=2 |
| 5 | 2 (0, 0) | 2 (0, 0) | 0 (empate) | `result[0]=0`; right=1 (fim) |

Resultado final: `[0,1,9,16,100]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — os dois ponteiros juntos percorrem o array uma única vez
- **Espaço:** O(n) para o array de resultado (exigido pelo problema); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] sortedSquares(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    int left = 0;
    int right = n - 1;
    int write = n - 1;

    // o maior quadrado só pode vir de uma das pontas (valor mais negativo ou mais positivo)
    while (left <= right) {
        int leftSq = nums[left] * nums[left];
        int rightSq = nums[right] * nums[right];
        if (leftSq > rightSq) {
            result[write] = leftSq;
            left++;
        } else {
            result[write] = rightSq;
            right--;
        }
        write--;
    }

    return result;
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

- Elevar ao quadrado e ordenar com `Arrays.sort` — funciona, mas é O(n log n); o follow-up pede O(n), que exige aproveitar a ordenação original em vez de refazer do zero.
- Comparar `nums[left]` com `nums[right]` diretamente (sem elevar ao quadrado) — com negativos no array, é o valor **absoluto** (via quadrado) que decide qual extremo produz o maior resultado, não o valor bruto.
- Preencher o resultado da frente pra trás — como os MAIORES valores são descobertos primeiro (comparando as pontas), eles precisam ir para as **últimas** posições do array de resultado; preencher da frente exigiria saber de antemão quantos elementos "menores" existem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Mistura de negativos e positivos | `[-4,-1,0,3,10]` | `[0,1,9,16,100]` | caso padrão do enunciado |
| Só negativos | `[-7,-3,-1]` | `[1,9,49]` | maior quadrado vem do mais negativo (extremo esquerdo) |
| Só positivos | `[1,2,3]` | `[1,4,9]` | maior quadrado vem do mais positivo (extremo direito) |
| Único elemento | `[0]` | `[0]` | `left == right` desde o início |

## 🔗 Conexões

- Problemas irmãos: [0088] Merge Sorted Array (mesma técnica de mesclar de trás para frente com dois ponteiros), [0167] Two Sum II - Input Array Is Sorted (mesma família de explorar a ordenação existente com dois ponteiros nas pontas)
- No backend: reordenar dados já parcialmente ordenados aproveitando a estrutura existente, evitando um re-sort completo — por exemplo, recalcular uma métrica derivada (como "distância ao centro") de uma série já ordenada por outro critério, mantendo O(n).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
