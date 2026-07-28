# [2441] Largest Positive Integer That Exists With Its Negative

> 🔗 [LeetCode 2441](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array `nums` sem nenhum zero, encontre o maior inteiro positivo `k` tal que `-k` também esteja no array. Retorne `k`, ou `-1` se não existir nenhum.

**Exemplos:**
```
Input:  nums = [-1,2,-3,3]
Output: 3

Input:  nums = [-1,10,6,7,-7,1]
Output: 7
Explicação: 1 e 7 têm negativo correspondente; 7 é o maior.

Input:  nums = [-10,8,6,7,-2,-3]
Output: -1
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 1000` → O(n²) já passaria, mas O(n log n) (com sort) é mais elegante
- `-1000 <= nums[i] <= 1000`, sem zeros → intervalo pequeno e simétrico, favorável a ordenar e comparar das pontas
- Pede o **maior** k → sugere buscar primeiro nos valores de maior magnitude, não em qualquer ordem

## 🧭 Como reconhecer o padrão

"Encontrar o par de valores opostos (soma zero) de maior magnitude" é resolvido ordenando o array e usando dois ponteiros nas pontas: o valor mais negativo à esquerda, o mais positivo à direita. Como os ponteiros convergem das extremidades pra dentro, o primeiro par com soma zero encontrado já é, garantidamente, o de maior `k`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `nums[i]`, verificar se `-nums[i]` também existe no array (percorrendo tudo de novo), guardando o maior `k` válido encontrado.

- Tempo: O(n²) — uma busca linear completa para cada elemento · Espaço: O(1)
- **Por que não basta:** refaz a busca do zero para cada elemento, sem aproveitar nenhuma estrutura; ordenando o array primeiro, dois ponteiros encontram o par de maior magnitude numa única varredura combinada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums`. Use `left` no início (valor mais negativo) e `right` no fim (valor mais positivo). Se `nums[left] + nums[right] == 0`, achou um par válido — e como veio das pontas pra dentro, esse `nums[right]` já é o maior `k` possível, retorne na hora. Se a soma for positiva, `right` é "grande demais" pra ter par com o `left` atual — recue `right`. Se for negativa, `left` é "negativo demais" — avance `left`.

## 🎬 Exemplo passo a passo

`nums = [-1,10,6,7,-7,1]` → ordenado: `[-7,-1,1,6,7,10]`

| Passo | left (valor) | right (valor) | soma | Ação |
|---|---|---|---|---|
| 1 | 0 (-7) | 5 (10) | 3 | soma > 0 → `right--` (precisa de uma soma menor) |
| 2 | 0 (-7) | 4 (7) | 0 | match! retorna `nums[right] = 7` |

Resultado final: `7` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura com dois ponteiros depois é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort usado internamente

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findMaxK(int[] nums) {
    Arrays.sort(nums);
    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == 0) {
            return nums[right]; // achou o par; vindo das pontas pra dentro, já é o maior k
        } else if (sum > 0) {
            right--; // right é grande demais pra ter par com o left atual
        } else {
            left++; // left é negativo demais pra ter par com o right atual
        }
    }

    return -1;
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

- Continuar procurando depois de achar o primeiro `sum == 0` — não precisa: vindo das extremidades pra dentro, o primeiro par encontrado já é o de maior `k` possível.
- Esquecer de ordenar antes de aplicar os dois ponteiros — sem ordenação, mover `left` ou `right` não tem garantia nenhuma de aproximar de um par válido.
- Achar que `sum > 0` significa "esse par não existe de jeito nenhum" — significa só que ESSE `right` específico não combina com ESSE `left`; o algoritmo tenta um `right` menor na próxima iteração, sem desistir da busca inteira.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Único par válido | `[-1,2,-3,3]` | 3 | só `-3`/`3` formam par |
| Dois pares válidos | `[-1,10,6,7,-7,1]` | 7 | `-7`/`7` e `-1`/`1` são válidos, retorna o maior |
| Nenhum par válido | `[-10,8,6,7,-2,-3]` | -1 | nenhum valor tem seu negativo correspondente no array |
| Par nos extremos | `[-100,1,100]` | 100 | `-100` e `100` já são as pontas do array ordenado |

## 🔗 Conexões

- Problemas irmãos: [0167] Two Sum II - Input Array Is Sorted (mesma técnica de dois ponteiros buscando uma soma-alvo num array ordenado), [1099] Two Sum Less Than K (mesma família de explorar a ordenação pra restringir a busca)
- No backend: encontrar o maior par cliente/fornecedor com saldos opostos que se cancelam exatamente — por exemplo, conciliação financeira buscando o maior débito que tem um crédito correspondente de mesmo valor, aproveitando dados já ordenados.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
