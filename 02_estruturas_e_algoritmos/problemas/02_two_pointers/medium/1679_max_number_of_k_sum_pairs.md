# [1679] Max Number of K-Sum Pairs

> 🔗 [LeetCode 1679](https://leetcode.com/problems/max-number-of-k-sum-pairs/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Medium`

## 📜 O Problema

Dado um array `nums` e um inteiro `k`, em cada operação você pode escolher dois números cuja soma seja `k` e removê-los. Retorne o número **máximo** de operações possíveis.

**Exemplos:**
```
Input:  nums = [1,2,3,4], k = 5
Output: 2
Explicação: remove (1,4), depois (2,3).

Input:  nums = [3,1,3,4,3], k = 6
Output: 1
Explicação: remove os dois primeiros 3's; sobra [1,4,3] sem mais pares.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) é arriscado, O(n log n) é o esperado
- `1 <= nums[i], k <= 10^9` → intervalo grande, mas a soma de dois valores no limite (`2×10^9`) ainda cabe num `int`
- Cada número só pode ser usado em **uma** operação → é uma remoção real, não uma contagem de pares repetíveis

## 🧭 Como reconhecer o padrão

"Formar o máximo de pares cuja soma bate com um alvo, cada elemento usado no máximo uma vez" é o padrão clássico de Two Sum sobre array ordenado: dois ponteiros nas pontas, ajustando conforme a soma atual for maior ou menor que o alvo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(i, j)` com `i < j`, verificar diretamente se `nums[i] + nums[j] == k`, indo removendo (ou marcando como usado) os pares encontrados.

- Tempo: O(n²) · Espaço: O(1) além do controle de "usado"
- **Por que não basta:** testa todos os pares possíveis, mesmo que a maioria nunca pudesse somar `k`; ordenando o array, dois ponteiros decidem em qual direção mover sem testar combinação por combinação.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums`. Use `left` no início e `right` no fim. Se `nums[left] + nums[right] == k`, achou um par — conte e avance os dois ponteiros (ambos "usados"). Se a soma for menor que `k`, `left` está pequeno demais — avance `left`. Se for maior, `right` está grande demais — recue `right`.

## 🎬 Exemplo passo a passo

`nums = [3,1,3,4,3]`, `k = 6` → ordenado: `[1,3,3,3,4]`

| Passo | left (valor) | right (valor) | soma | Ação |
|---|---|---|---|---|
| 1 | 0 (1) | 4 (4) | 5 | `soma < k` → avança `left` |
| 2 | 1 (3) | 4 (4) | 7 | `soma > k` → recua `right` |
| 3 | 1 (3) | 3 (3) | 6 | match! conta 1; avança `left`, recua `right` |

`left(2) >= right(2)` → loop termina. Total: `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura com dois ponteiros depois é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort usado internamente

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxOperations(int[] nums, int k) {
    Arrays.sort(nums);
    int left = 0;
    int right = nums.length - 1;
    int count = 0;

    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == k) {
            count++;
            left++;
            right--;
        } else if (sum < k) {
            left++;
        } else {
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

- Esquecer de ordenar antes de aplicar dois ponteiros — sem ordenação, mover `left` ou `right` não tem garantia de aproximar de uma soma igual a `k`.
- Quando `soma == k`, avançar só um dos ponteiros — os dois números formam um par e são "removidos" juntos; ambos precisam avançar, senão o mesmo elemento seria reutilizado.
- Assumir cegamente que a soma sempre cabe em `int` sem checar os limites do enunciado — aqui `2×10^9` ainda cabe (limite do `int` é ~2,147×10^9), mas é o tipo de conta que vale sempre conferir quando os valores se aproximam do limite, em vez de supor.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Todos pareados | `[1,2,3,4]`, k=5 | 2 | dois pares exatos, array esvazia completamente |
| Com sobras | `[3,1,3,4,3]`, k=6 | 1 | só um par soma 6, sobram 3 elementos sem par |
| Nenhum par | `[1,1,1]`, k=10 | 0 | nenhuma soma alcança k |
| Duplicatas formando múltiplos pares | `[2,2,2,2]`, k=4 | 2 | todos os pares (2,2) somam 4 |

## 🔗 Conexões

- Problemas irmãos: [0167] Two Sum II - Input Array Is Sorted (mesma técnica, mas retorna os índices de UM par em vez de contar todos), [0015] 3Sum (mesma família, generalizando pra triplas)
- No backend: parear transações que se cancelam (ex.: um crédito e um débito de valores complementares) o máximo de vezes possível, processando um lote ordenado por valor.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
