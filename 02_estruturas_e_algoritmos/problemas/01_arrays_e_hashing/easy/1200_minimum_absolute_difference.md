# [1200] Minimum Absolute Difference

> 🔗 [LeetCode 1200](https://leetcode.com/problems/minimum-absolute-difference/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array de inteiros **distintos** `arr`, encontre todos os pares de elementos com a menor diferença absoluta entre quaisquer dois elementos. Retorne uma lista de pares em ordem crescente (em relação aos pares), onde cada par `[a, b]` segue:
- `a, b` são de `arr`
- `a < b`
- `b - a` é igual à menor diferença absoluta entre quaisquer dois elementos de `arr`

**Exemplos:**
```
Input:  arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explicação: a menor diferença absoluta é 1. Lista todos os pares com essa diferença, em ordem crescente.

Input:  arr = [1,3,6,10,15]
Output: [[1,3]]

Input:  arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
```

**Restrições (e o que elas denunciam):**
- `2 <= arr.length <= 10^5` → precisa O(n log n); O(n²) (todos os pares) seria 10^10 — inviável
- `-10^6 <= arr[i] <= 10^6` → valores podem ser negativos, mas a diferença absoluta funciona igual
- elementos distintos → não precisa tratar diferença zero entre elementos iguais

## 🧭 Como reconhecer o padrão

"Menor diferença entre quaisquer dois elementos" é sempre resolvido ordenando o array primeiro — depois de ordenado, a menor diferença SEMPRE está entre elementos ADJACENTES na ordenação (nunca entre elementos distantes), então uma única passada linear depois do sort já resolve.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de índices `(i, j)` com `i < j`, calcular `|arr[i] - arr[j]|` e manter o menor valor encontrado, junto com os pares que o atingem.

- Tempo: O(n²) — todos os pares possíveis · Espaço: O(1) extra
- **Por que não basta:** com n até 10^5, n² chega a 10^10 comparações — inviável; a maioria dessas comparações é redundante, já que a menor diferença nunca ocorre entre elementos "distantes" no valor.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene o array. Percorra pares adjacentes (`arr[i]` e `arr[i-1]`), calculando `arr[i] - arr[i-1]` (já positivo, pois está ordenado). Rastreie o menor valor visto; sempre que encontrar um par com essa diferença mínima, adicione-o à lista de resultado.

## 🎬 Exemplo passo a passo

`arr = [4,2,1,3]` — ordenado: `[1,2,3,4]`

| Passo | i | arr[i] | arr[i-1] | diferença | minDif | resultado |
|---|---|---|---|---|---|---|
| 1 | 1 | 2 | 1 | 1 | 1 | [[1,2]] |
| 2 | 2 | 3 | 2 | 1 | 1 (empate) | [[1,2],[2,3]] |
| 3 | 3 | 4 | 3 | 1 | 1 (empate) | [[1,2],[2,3],[3,4]] |

Resultado final: `[[1,2],[2,3],[3,4]]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação
- **Espaço:** O(n) — para o resultado (e o array ordenado, se não for in-place)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<List<Integer>> minimumAbsDifference(int[] arr) {
    Arrays.sort(arr);

    int minDif = Integer.MAX_VALUE;
    for (int i = 1; i < arr.length; i++) {
        minDif = Math.min(minDif, arr[i] - arr[i - 1]); // já ordenado, a diferença é sempre não-negativa
    }

    List<List<Integer>> resultado = new ArrayList<>();
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] - arr[i - 1] == minDif) {
            resultado.add(Arrays.asList(arr[i - 1], arr[i])); // par adjacente que atinge a diferença mínima
        }
    }
    return resultado;
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

- Comparar elementos não-adjacentes depois de ordenar (ex.: `arr[i]` com `arr[i-2]`) — depois de ordenado, a menor diferença NUNCA ocorre entre elementos não-adjacentes; comparar isso é desperdício e nunca vai bater o mínimo real.
- Esquecer que pode haver MÚLTIPLOS pares com a mesma diferença mínima — o enunciado pede todos eles, não só o primeiro encontrado.
- Calcular `minDif` e já ir montando o resultado numa única passada — funciona, mas exige limpar o resultado toda vez que encontra uma diferença menor; separar em duas passadas (achar o mínimo, depois coletar os pares) é mais simples de raciocinar.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Múltiplos pares empatados | `[4,2,1,3]` | [[1,2],[2,3],[3,4]] | todos os pares adjacentes após ordenar têm diferença 1 |
| Um único par mínimo | `[1,3,6,10,15]` | [[1,3]] | menor diferença é 2, só um par a atinge |
| Valores negativos misturados | `[3,8,-10,23,19,-4,-14,27]` | [[-14,-10],[19,23],[23,27]] | ordenação lida naturalmente com negativos |
| Array de dois elementos | `[5,1]` | [[1,5]] | menor entrada possível, um único par |

## 🔗 Conexões

- Problemas irmãos: [0220] Contains Duplicate III (também busca diferenças mínimas, mas com restrição de janela de índices), [0561] Array Partition (mesma técnica base de ordenar antes de processar pares)
- No backend: análise de dados para encontrar os registros mais "próximos" entre si num conjunto (ex.: preços de produtos mais parecidos, ou timestamps de eventos mais próximos), onde ordenar primeiro reduz drasticamente o espaço de busca.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
