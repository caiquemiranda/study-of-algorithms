# [1636] Sort Array by Increasing Frequency

> 🔗 [LeetCode 1636](https://leetcode.com/problems/sort-array-by-increasing-frequency/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#HashTable` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums`, ordene o array em ordem **crescente** de frequência dos valores. Se múltiplos valores têm a mesma frequência, ordene-os em ordem **decrescente**.

Retorne o array ordenado.

**Exemplos:**
```
Input:  nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explicação: '3' tem frequência 1, '1' tem frequência 2, e '2' tem frequência 3.

Input:  nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explicação: '2' e '3' têm frequência 2, então são ordenados de forma decrescente.

Input:  nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 100` → pequeno, O(n log n) resolve com folga
- valores podem ser negativos → hash map lida bem, sem necessidade de array de contagem fixo

## 🧭 Como reconhecer o padrão

"Ordenar por uma métrica derivada (frequência), com desempate por outro critério" é resolvido contando a frequência de cada valor num hash map, e depois ordenando os ELEMENTOS ORIGINAIS usando um comparador customizado que usa a frequência como critério primário e o próprio valor (decrescente) como desempate.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada elemento, contar sua frequência percorrendo o array inteiro repetidamente, e depois ordenar usando essas contagens recalculadas a cada comparação.

- Tempo: O(n² log n) se a frequência for recalculada a cada comparação do sort · Espaço: O(n)
- **Por que não basta:** recalcular a frequência de um valor toda vez que ele é comparado durante a ordenação é extremamente redundante; pré-computar todas as frequências uma única vez antes de ordenar resolve isso.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um hash map `valor → frequência` com uma passada. Ordene uma cópia do array usando um comparador customizado: primeiro por `frequência[a]` crescente; em caso de empate, por valor decrescente.

## 🎬 Exemplo passo a passo

`nums = [2,3,1,3,2]` — frequência: `{2:2, 3:2, 1:1}`

| Passo | Critério | Ordenação resultante |
|---|---|---|
| 1 | por frequência crescente | 1 (freq 1) vem primeiro; 2 e 3 (freq 2) empatam |
| 2 | desempate: valor decrescente entre os empatados | 3 antes de 2 (3>2) |

Resultado final: `[1,3,3,2,2]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação
- **Espaço:** O(n) — para o mapa e o array de saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] frequencySort(int[] nums) {
    Map<Integer, Integer> frequencia = new HashMap<>();
    for (int num : nums) {
        frequencia.merge(num, 1, Integer::sum);
    }

    Integer[] boxed = Arrays.stream(nums).boxed().toArray(Integer[]::new);
    Arrays.sort(boxed, (a, b) -> {
        int freqA = frequencia.get(a);
        int freqB = frequencia.get(b);
        if (freqA != freqB) {
            return freqA - freqB; // frequência crescente
        }
        return b - a; // desempate: valor decrescente
    });

    int[] resultado = new int[nums.length];
    for (int i = 0; i < resultado.length; i++) {
        resultado[i] = boxed[i];
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

- Esquecer o critério de desempate (valor decrescente) quando as frequências empatam — o enunciado exige explicitamente essa ordem secundária, não é "qualquer ordem" entre valores de mesma frequência.
- Inverter o desempate (`a - b` em vez de `b - a`) — isso ordenaria os valores empatados em ordem CRESCENTE, quando o enunciado pede decrescente.
- Usar `int[]` diretamente com `Arrays.sort` (que só ordena em ordem natural) em vez de `Integer[]` com um comparador customizado — arrays primitivos em Java não aceitam `Comparator`, é preciso converter para o tipo boxed primeiro.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Frequências distintas | [1,1,2,2,2,3] | [3,1,1,2,2,2] | '3' tem freq 1, '1' tem freq 2, '2' tem freq 3 |
| Empate de frequência | [2,3,1,3,2] | [1,3,3,2,2] | '2' e '3' empatam com freq 2, '3' vem primeiro (maior valor) |
| Valores negativos | [-1,1,-6,4,5,-6,1,4,1] | [5,-1,4,4,-6,-6,1,1,1] | mistura de sinais não afeta a lógica de contagem/ordenação |
| Todos com a mesma frequência | [3,1,2] | [3,2,1] | todos freq 1, ordena só pelo desempate (decrescente) |

## 🔗 Conexões

- Problemas irmãos: [1122] Relative Sort Array (mesma técnica de contagem + reconstrução), [0451] Sort Characters By Frequency (mesmo domínio de ordenar por frequência, mas para caracteres em vez de números)
- No backend: ranking de itens por popularidade com critério de desempate (ex.: ordenar produtos por menor volume de vendas primeiro, desempatando por preço, útil em relatórios de itens "encalhados").

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
