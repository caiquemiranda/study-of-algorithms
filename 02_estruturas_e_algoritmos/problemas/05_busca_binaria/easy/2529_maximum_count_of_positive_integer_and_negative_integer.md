# [2529] Maximum Count of Positive Integer and Negative Integer

> 🔗 [LeetCode 2529](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array `nums` ordenado de forma **não decrescente**. Retorne o **maior** valor entre a quantidade de inteiros positivos e a quantidade de inteiros negativos em `nums`. Zero não conta nem como positivo nem como negativo.

**Exemplos:**
```
Input:  nums = [-2,-1,-1,1,2,3]      Output: 3   (3 positivos, 3 negativos, max=3)
Input:  nums = [-3,-2,-1,0,0,1,2]    Output: 3   (2 positivos, 3 negativos, max=3)
Input:  nums = [5,20,66,1314]        Output: 4   (4 positivos, 0 negativos, max=4)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 2000` → O(n) já passaria fácil, mas o enunciado tem um follow-up puxando para algo melhor
- "nums is sorted in a non-decreasing order" → sinal direto de busca binária: negativos ficam todos no início, positivos todos no fim, zeros (se houver) no meio
- **Follow up:** "Can you solve the problem in O(log(n)) time complexity?" → é o convite explícito para trocar a contagem linear por duas buscas binárias de fronteira

## 🧭 Como reconhecer o padrão

Como o array está ordenado, os negativos formam um bloco contíguo no início, seguido (opcionalmente) por zeros, seguido pelos positivos. "Contar quantos elementos satisfazem uma condição monotônica (`< 0` ou `> 0`) num array ordenado" é achar uma **fronteira** — o mesmo padrão de [2089] Find Target Indices e [0035] Search Insert Position.

## 🐢 Solução 1 — Força bruta

Percorrer o array inteiro contando quantos elementos são positivos e quantos são negativos; retornar o maior dos dois contadores.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o follow-up pede O(log n) — e a contagem linear ignora que o array já está ordenado, o que permite achar as duas fronteiras (onde os negativos terminam, onde os positivos começam) via busca binária em vez de examinar cada elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça duas buscas binárias de "lower bound":
1. **Primeira posição `>= 0`**: tudo antes dela é negativo → `quantidadeNegativos = essa posição`.
2. **Primeira posição `> 0`** (ou seja, `>= 1`): tudo depois dela (inclusive) é positivo → `quantidadePositivos = n - essa posição`.

A resposta é o maior entre `quantidadeNegativos` e `quantidadePositivos`. Os zeros, se existirem, ficam automaticamente excluídos de ambas as contagens porque cada busca usa uma fronteira diferente (`>= 0` exclui negativos; `>= 1` exclui zero e negativos).

## 🎬 Exemplo passo a passo

`nums = [-3, -2, -1, 0, 0, 1, 2]` (n = 7)

| Busca | left | mid | right | Comparação | Resultado |
|---|---|---|---|---|---|
| lower bound de `0` | 0 | 3 (val 0) | 6 | 0 >= 0 → candidato, busca à esquerda | converge em índice 3 |
| lower bound de `1` | 0 | 3 (val 0) | 6 | 0 < 1 → busca à direita | converge em índice 5 |

`quantidadeNegativos = 3` (índices 0,1,2) · `quantidadePositivos = 7 - 5 = 2` (índices 5,6)

Resultado final: `max(3, 2) = 3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — duas buscas binárias independentes
- **Espaço:** O(1) — só ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maximumCount(int[] nums) {
    int quantidadeNegativos = lowerBound(nums, 0);        // tudo antes daqui é < 0
    int quantidadePositivos = nums.length - lowerBound(nums, 1);  // tudo a partir daqui é > 0

    return Math.max(quantidadeNegativos, quantidadePositivos);
}

// Lower bound clássico: primeira posição com valor >= alvo.
private int lowerBound(int[] arr, int alvo) {
    int left = 0, right = arr.length;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] < alvo) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
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

- **Contar zero como positivo ou negativo**: o enunciado é explícito — zero não conta para nenhum dos dois. Usar `lower bound de 0` (não `-1`) e `lower bound de 1` (não `0`) é o que garante essa exclusão corretamente.
- **Reaproveitar a mesma chamada de lower bound para os dois casos**: são buscas com alvos diferentes (`0` e `1`) — usar o mesmo resultado para ambas as contagens é um erro comum de quem tenta "economizar" uma chamada.
- **Array sem negativos ou sem positivos**: `nums=[5,20,66,1314]` (todo positivo) deve dar `quantidadeNegativos = 0` — a busca binária lida com isso naturalmente (lower bound de 0 retorna índice 0), mas é bom validar esse caso de borda.
- **Achar que precisa ordenar**: o enunciado já garante que `nums` vem ordenado — ordenar de novo seria desperdício (e mudaria a complexidade de O(log n) para O(n log n)).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só negativos | `nums=[-5,-3,-1]` | 3 | testa quantidadePositivos = 0 |
| Só positivos | `nums=[5,20,66,1314]` | 4 | testa quantidadeNegativos = 0 |
| Só zeros | `nums=[0,0,0]` | 0 | nem positivo nem negativo, ambos contadores zerados |
| Empate | `nums=[-2,-1,-1,1,2,3]` | 3 | positivos e negativos empatados, max ainda funciona |
| Com zeros no meio | `nums=[-3,-2,-1,0,0,1,2]` | 3 | trace acima, zeros excluídos de ambas as contagens |

## 🔗 Conexões

- Problemas irmãos: **[2089] Find Target Indices After Sorting Array** (mesmo par de buscas por fronteira lower/upper bound), **[0035] Search Insert Position** (o lower bound usado como bloco de construção aqui), **[1608] Special Array With X Elements Greater Than or Equal X** (outra contagem via fronteira em array ordenado)
- No backend: contar quantos registros caem de cada lado de um limiar (ex.: quantas transações são débitos vs. créditos num extrato já ordenado por valor) é resolvido com o mesmo par de buscas binárias, sem precisar varrer o extrato inteiro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
