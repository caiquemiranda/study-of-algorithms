# [1877] Minimize Maximum Pair Sum in Array

> 🔗 [LeetCode 1877](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Greedy` `#Sorting` `#Medium`

## 📜 O Problema

Dado um array `nums` de tamanho par, agrupe todos os elementos em `n/2` pares (cada elemento em exatamente um par) de forma a **minimizar** a maior soma de par (`max pair sum`). Retorne esse valor mínimo do máximo.

**Exemplos:**
```
Input:  nums = [3,5,2,3]
Output: 7
Explicação: pares (3,3) e (5,2); max(6,7) = 7.

Input:  nums = [3,5,4,2,4,6]
Output: 8
Explicação: pares (3,5), (4,4), (6,2); todos somam 8.
```

**Restrições (e o que elas denunciam):**
- `2 <= n <= 10^5`, tamanho sempre par → O(n²) é arriscado, O(n log n) é o esperado
- Minimizar o MÁXIMO entre os pares (não a soma total, que é sempre a mesma independente do emparelhamento) → sinaliza uma estratégia gulosa de "equilibrar" os pares, não de somar

## 🧭 Como reconhecer o padrão

"Emparelhar elementos pra minimizar o maior par possível" é resolvido ordenando o array e combinando sempre o **menor** valor disponível com o **maior** valor disponível — dois ponteiros nas pontas convergindo pro centro, a mesma estrutura de [0977] Squares of a Sorted Array e [2465] Number of Distinct Averages.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todas as formas possíveis de agrupar o array em pares, calculando o maior par de cada agrupamento e mantendo o menor entre esses máximos.

- Tempo: O(n!) — o número de formas de agrupar `n` elementos em pares cresce em dupla-fatorial, explosivo até para `n` pequeno
- **Por que não basta:** claramente inviável. Ordenar o array e emparelhar sempre o menor disponível com o maior disponível é a estratégia gulosa comprovadamente ótima — qualquer outro emparelhamento só pode igualar ou piorar o máximo resultante.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums`. Use `left` no início e `right` no fim, formando o par `(nums[left], nums[right])` e avançando os dois pra dentro. Combinar o menor com o maior "equilibra" as somas — evita que dois valores grandes acabem no mesmo par (o que inflaria o máximo). Acompanhe a maior soma vista entre todos os pares formados; essa é a resposta.

## 🎬 Exemplo passo a passo

`nums = [3,5,4,2,4,6]` → ordenado: `[2,3,4,4,5,6]`

| Passo | left (valor) | right (valor) | soma do par | máximo acumulado |
|---|---|---|---|---|
| 1 | 0 (2) | 5 (6) | 8 | 8 |
| 2 | 1 (3) | 4 (5) | 8 | 8 |
| 3 | 2 (4) | 3 (4) | 8 | 8 |

`left(3) >= right(2)` → loop termina. Resultado final: `8` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura com dois ponteiros depois é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort usado internamente

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minPairSum(int[] nums) {
    Arrays.sort(nums);
    int left = 0;
    int right = nums.length - 1;
    int maxSum = 0;

    while (left < right) {
        maxSum = Math.max(maxSum, nums[left] + nums[right]);
        left++;
        right--;
    }

    return maxSum;
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

- Emparelhar elementos adjacentes no array ordenado (ex.: `nums[0]` com `nums[1]`) em vez de menor-com-maior — essa estratégia costuma gerar um máximo maior, pois concentra os dois maiores valores no mesmo par.
- Esquecer de ordenar antes de aplicar os dois ponteiros — sem ordenação, não há garantia de que `nums[left]` e `nums[right]` sejam de fato o menor e o maior disponíveis.
- Calcular a MÉDIA ou a SOMA total dos pares em vez do MÁXIMO entre eles — o problema pede minimizar o maior par, não otimizar a soma total (que é sempre igual à soma de todo o array, invariante a qualquer emparelhamento).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | `[3,5,2,3]` | 7 | menor com maior: (2,5)→7 e (3,3)→6, máximo é 7 |
| Todos pares iguais | `[3,5,4,2,4,6]` | 8 | os três pares resultam na mesma soma |
| Tamanho mínimo | `[1,2]` | 3 | único par possível |
| Valores repetidos | `[1,1,1,1]` | 2 | todo par soma 2, máximo é 2 |

## 🔗 Conexões

- Problemas irmãos: [0977] Squares of a Sorted Array (mesma técnica de ordenar e usar dois ponteiros nas pontas), [2465] Number of Distinct Averages (mesma família de combinar repetidamente o menor com o maior restante)
- No backend: balancear carga entre pares de recursos — por exemplo, distribuir tarefas pesadas e leves entre workers emparelhando a mais pesada com a mais leve disponível, minimizando o pior caso de carga combinada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
