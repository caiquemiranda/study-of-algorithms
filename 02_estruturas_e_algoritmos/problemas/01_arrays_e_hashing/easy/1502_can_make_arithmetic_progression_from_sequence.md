# [1502] Can Make Arithmetic Progression From Sequence

> 🔗 [LeetCode 1502](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Uma sequência de números é chamada de **progressão aritmética** se a diferença entre quaisquer dois elementos consecutivos é a mesma. Dado um array de números `arr`, retorne `true` se o array pode ser reordenado para formar uma progressão aritmética. Caso contrário, retorne `false`.

**Exemplos:**
```
Input:  arr = [3,5,1]
Output: true
Explicação: podemos reordenar como [1,3,5] ou [5,3,1], com diferenças 2 e -2 respectivamente.

Input:  arr = [1,2,4]
Output: false
Explicação: não há como reordenar os elementos para obter uma progressão aritmética.
```

**Restrições (e o que elas denunciam):**
- `2 <= arr.length <= 1000` → O(n log n) resolve com folga
- valores podem ser negativos → diferença ainda funciona igual

## 🧭 Como reconhecer o padrão

"Pode ser reorganizado para formar uma progressão aritmética" é resolvido ordenando o array primeiro — uma vez ordenado, a única forma de ser uma PA válida é ter a MESMA diferença entre TODOS os pares adjacentes.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todas as permutações do array, verificando para cada uma se ela forma uma PA válida.

- Tempo: O(n!) · Espaço: O(n!)
- **Por que não basta:** astronomicamente inviável; a ordenação já revela a única disposição candidata (a menos de inversão), sem precisar testar nenhuma outra ordem.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene o array. Calcule a diferença esperada `d = arr[1] - arr[0]`. Percorra o array verificando se `arr[i] - arr[i-1] == d` para todo `i`; se alguma diferença for diferente, não é uma PA.

## 🎬 Exemplo passo a passo

`arr = [3,5,1]` — ordenado: `[1,3,5]`, `d = arr[1]-arr[0] = 2`

| Passo | i | arr[i] | arr[i-1] | diferença | == d(2)? |
|---|---|---|---|---|---|
| 1 | 1 | 3 | 1 | 2 | sim |
| 2 | 2 | 5 | 3 | 2 | sim |

Todas as diferenças batem → **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação
- **Espaço:** O(1) extra (ou O(n) se não ordenar in-place)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean canMakeArithmeticProgression(int[] arr) {
    Arrays.sort(arr);
    int diferenca = arr[1] - arr[0];

    for (int i = 2; i < arr.length; i++) {
        if (arr[i] - arr[i - 1] != diferenca) {
            return false; // quebrou o padrão de progressão aritmética
        }
    }
    return true;
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

- Tentar verificar a PA SEM ordenar primeiro — a ordem original do array raramente já é a de uma PA; ordenar é o que revela se ela EXISTE.
- Calcular a diferença esperada usando um par que não seja `arr[0]` e `arr[1]` (depois de ordenado) — qualquer par adjacente serve como referência, mas usar o primeiro par é o mais direto.
- Esquecer o caso `arr.length == 2` — qualquer array de 2 elementos é trivialmente uma PA válida; o código já lida com isso naturalmente (o loop de comparação não executa).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| PA válida | [3,5,1] | true | reordenado vira [1,3,5], diferença constante 2 |
| Não é PA | [1,2,4] | false | diferenças 1 e 2, inconsistentes |
| Array de dois elementos | [5,1] | true | sempre válido com só 2 elementos |
| Valores negativos | [-3,-1,-5,-7] | true | reordenado vira [-7,-5,-3,-1], diferença constante 2 |

## 🔗 Conexões

- Problemas irmãos: [1200] Minimum Absolute Difference (mesma técnica base de ordenar antes de comparar pares adjacentes), [1637] Widest Vertical Area Between Two Points Containing No Points (mesmo domínio de ordenar e comparar diferenças consecutivas)
- No backend: validação de sequências numéricas regulares em dados de séries temporais (ex.: verificar se os timestamps de um conjunto de eventos são igualmente espaçados após reordenação).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
