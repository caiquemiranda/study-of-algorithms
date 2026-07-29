# [2089] Find Target Indices After Sorting Array

> 🔗 [LeetCode 2089](https://leetcode.com/problems/find-target-indices-after-sorting-array/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array `nums` e um `target`. Um "índice alvo" é um índice `i` tal que `nums[i] == target`. Ordene `nums` em ordem não decrescente e retorne a **lista de índices alvo** (em ordem crescente) nesse array já ordenado. Se não houver nenhum, retorne lista vazia.

**Exemplos:**
```
Input:  nums = [1,2,5,2,3], target = 2    Output: [1,2]
        (depois de ordenar: [1,2,2,3,5] → os índices 1 e 2 valem 2)
Input:  nums = [1,2,5,2,3], target = 3    Output: [3]
Input:  nums = [1,2,5,2,3], target = 5    Output: [4]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 100` → array pequeno; até uma busca linear depois de ordenar já resolveria, mas o padrão que a categoria ensina é achar a **faixa de ocorrências** via busca binária
- `1 <= nums[i], target <= 100` → valores pequenos, sem risco de overflow
- "ordene, depois ache os índices" → depois de ordenar, todas as ocorrências de `target` ficam **contíguas** — a assinatura clássica de achar um intervalo `[primeiro, último]` num array ordenado

## 🧭 Como reconhecer o padrão

"Array ordenado" + "ache TODAS as posições onde um valor aparece" é achar a fronteira **inferior** (primeira ocorrência) e a fronteira **superior** (depois da última ocorrência) via duas buscas binárias — exatamente o padrão de [0034] Find First and Last Position of Element in Sorted Array, só que aqui o enunciado já entrega a ordenação como parte do problema.

## 🐢 Solução 1 — Força bruta

Ordenar `nums` e depois percorrer o array inteiro comparando cada elemento com `target`, coletando os índices que baterem.

- Tempo: O(n log n) para ordenar + O(n) para varrer = O(n log n) · Espaço: O(n) para a resposta
- **Por que não basta:** a varredura linear ignora que, num array já ordenado, as ocorrências de `target` formam um bloco contíguo — dá para achar o início e o fim desse bloco em O(log n) em vez de O(n), embora aqui o ganho seja pequeno dado o tamanho do array.

## 💡 Solução 2 — A ideia otimizada (intuição)

Depois de ordenar `nums`, faça duas buscas binárias:
1. **Lower bound**: a primeira posição onde `nums[i] >= target`.
2. **Upper bound**: a primeira posição onde `nums[i] > target`.

Todo índice entre `lowerBound` (inclusive) e `upperBound` (exclusive) é um índice alvo — basta gerar essa faixa. Se `lowerBound == upperBound`, `target` não existe no array, e a resposta é lista vazia.

## 🎬 Exemplo passo a passo

`nums = [1, 2, 5, 2, 3]` → ordenado: `[1, 2, 2, 3, 5]`, `target = 2`

| Busca | left | mid | right | Comparação | Resultado |
|---|---|---|---|---|---|
| lower bound (`>=2`) | 0 | 2 (val 2) | 4 | 2>=2 → candidato, busca à esquerda | ... converge em índice 1 |
| upper bound (`>2`) | 0 | 2 (val 2) | 4 | 2 não é >2 → busca à direita | ... converge em índice 3 |

Faixa de índices: `[1, 3)` → índices `1` e `2`

Resultado final: `[1, 2]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; as duas buscas binárias são O(log n) cada
- **Espaço:** O(log n) a O(n) para o sort, mais O(k) para a resposta (k = quantidade de índices alvo)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> targetIndices(int[] nums, int target) {
    Arrays.sort(nums);                       // habilita busca binária por faixa

    int inicio = lowerBound(nums, target);   // primeira posição >= target
    int fim = lowerBound(nums, target + 1);  // primeira posição > target (== lower bound de target+1)

    List<Integer> resultado = new ArrayList<>();
    for (int i = inicio; i < fim; i++) {
        resultado.add(i);                    // todo índice nessa faixa contígua vale target
    }
    return resultado;
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

- **Ordenar o array errado**: o problema pede os índices **depois** de ordenar — se você calcular os índices no array original (antes de ordenar), a resposta fica completamente errada.
- **Usar `upperBound(target)` implementado do zero em vez de `lowerBound(target+1)`**: são equivalentes matematicamente, mas reaproveitar a mesma função `lowerBound` com `target+1` evita duplicar lógica e reduz chance de bug de off-by-one.
- **Esquecer o caso "target não existe"**: se `lowerBound(target) == lowerBound(target+1)`, a faixa está vazia — o laço `for` simplesmente não adiciona nada, o que já é o comportamento correto, mas vale testar explicitamente.
- **Achar que a ordem original importa para o resultado**: a resposta é sobre o array **já ordenado** — os índices originais são irrelevantes.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Target ausente | `nums=[1,2,3], target=5` | `[]` | testa faixa vazia (lowerBound == upperBound) |
| Target único | `nums=[1,2,5,2,3], target=3` | `[3]` | uma só ocorrência |
| Target é o maior valor | `nums=[1,2,5,2,3], target=5` | `[4]` | fronteira no fim do array ordenado |
| Todos iguais ao target | `nums=[7,7,7], target=7` | `[0,1,2]` | faixa contígua cobrindo o array inteiro |
| Exemplo do enunciado | `nums=[1,2,5,2,3], target=2` | `[1,2]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0034] Find First and Last Position of Element in Sorted Array** (o mesmo padrão de lower/upper bound, versão "clássica"), **[0035] Search Insert Position** (lower bound isolado)
- No backend: achar todos os registros com uma chave específica num índice ordenado (ex.: todas as linhas de log de um mesmo `request_id` num arquivo ordenado por chave) é resolvido com o mesmo par de buscas binárias em vez de escanear o arquivo inteiro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
