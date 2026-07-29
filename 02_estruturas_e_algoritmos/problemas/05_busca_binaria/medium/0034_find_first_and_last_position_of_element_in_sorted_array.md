# [0034] Find First and Last Position of Element in Sorted Array

> 🔗 [LeetCode 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Dado um array `nums` ordenado de forma **não decrescente**, encontre a posição **inicial** e **final** de um `target`. Se não existir, retorne `[-1, -1]`.

**Exemplos:**
```
Input:  nums = [5,7,7,8,8,10], target = 8    Output: [3,4]
Input:  nums = [5,7,7,8,8,10], target = 6    Output: [-1,-1]
Input:  nums = [], target = 0                Output: [-1,-1]
```

**Restrições (e o que elas denunciam):**
- `0 <= nums.length <= 10^5` → O(n) passaria, mas o enunciado exige O(log n)
- "You must write an algorithm with O(log n) runtime complexity" → busca binária obrigatória, e como pede DOIS índices (início e fim), sugere DUAS buscas binárias
- `nums` pode ser **vazio** → caso de borda que precisa de tratamento antes (ou dentro) da busca binária

## 🧭 Como reconhecer o padrão

"Ache TODAS as ocorrências de um valor num array ordenado" é achar a **faixa contígua** onde ele aparece — exatamente a técnica de duas buscas binárias por fronteira (lower bound e upper bound) que já apareceu em [2089] Find Target Indices After Sorting Array, só que aqui o array já vem ordenado (sem precisar ordenar primeiro).

## 🐢 Solução 1 — Força bruta

Percorrer o array inteiro, guardando o primeiro e o último índice onde `nums[i] == target`.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige O(log n) explicitamente — e ignora que, num array ordenado, todas as ocorrências de `target` formam um bloco contíguo cujas duas bordas podem ser achadas por busca binária.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça duas buscas binárias independentes:
1. **Lower bound**: a primeira posição onde `nums[i] >= target`.
2. **Upper bound**: a primeira posição onde `nums[i] > target`.

Se `lowerBound` estiver fora dos limites do array OU `nums[lowerBound] != target`, o valor não existe — retorna `[-1,-1]`. Caso contrário, a resposta é `[lowerBound, upperBound - 1]` (o `-1` converte "primeira posição depois do bloco" para "última posição do bloco").

## 🎬 Exemplo passo a passo

`nums = [5,7,7,8,8,10]`, `target = 8`

| Busca | left | mid | right | Comparação | Resultado |
|---|---|---|---|---|---|
| lower bound (`>=8`) | 0 | 2 (val 7) | 5 | 7<8 → busca à direita | ... converge em índice 3 |
| upper bound (`>8`) | 0 | 2 (val 7) | 5 | 7 não é >8 → busca à direita | ... converge em índice 5 |

`lowerBound = 3` (nums[3]=8, confirma existência) · `upperBound = 5`

Resultado final: `[3, 5-1] = [3, 4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — duas buscas binárias independentes
- **Espaço:** O(1) — só ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] searchRange(int[] nums, int target) {
    int lower = lowerBound(nums, target);

    // Se lower está fora dos limites ou o valor ali não bate com target, não existe.
    if (lower == nums.length || nums[lower] != target) {
        return new int[]{-1, -1};
    }

    int upper = lowerBound(nums, target + 1);  // primeira posição > target
    return new int[]{lower, upper - 1};
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

- **Esquecer o array vazio**: `nums = []` precisa retornar `[-1,-1]` sem lançar exceção — a função `lowerBound` já lida bem com isso (retorna `0`, que é igual a `nums.length` quando o array é vazio), mas vale testar explicitamente.
- **Não verificar se o valor achado realmente é o `target`**: o lower bound retorna a primeira posição `>= target`, mesmo que `target` não exista no array (nesse caso, `nums[lower]` seria maior que `target`) — sem essa checagem, a função retornaria índices incorretos em vez de `[-1,-1]`.
- **Usar `target - 1` em vez de `target + 1` na segunda busca**: a lógica certa é achar a primeira posição **depois** do bloco (`> target`, ou seja, lower bound de `target+1`); usar `target - 1` buscaria a fronteira errada.
- **Overflow em `target + 1`**: com `target` no limite superior do tipo (`Integer.MAX_VALUE`), somar 1 estoura — em Java, considerar usar `long` para o cálculo do upper bound se as restrições permitirem valores extremos (aqui `target` cabe em `int` com folga, mas é um hábito a manter).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Array vazio | `nums=[], target=0` | `[-1,-1]` | borda mínima |
| Target ausente | `nums=[5,7,7,8,8,10], target=6` | `[-1,-1]` | cai num "buraco" entre valores |
| Uma única ocorrência | `nums=[5,7,7,8,8,10], target=10` | `[5,5]` | início e fim coincidem |
| Todos iguais ao target | `nums=[2,2,2], target=2` | `[0,2]` | faixa cobrindo o array inteiro |
| Exemplo do enunciado | `nums=[5,7,7,8,8,10], target=8` | `[3,4]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0035] Search Insert Position** (o lower bound isolado, sem o upper bound), **[2089] Find Target Indices After Sorting Array** (mesmo par de buscas, mas o array precisa ser ordenado primeiro)
- No backend: achar o intervalo completo de registros com uma chave específica num índice ordenado (ex.: todas as linhas de um `range scan` num banco de dados indexado por uma coluna) usa exatamente esse par de buscas binárias em vez de escanear tudo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
