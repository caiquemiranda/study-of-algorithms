# [1207] Unique Number of Occurrences

> 🔗 [LeetCode 1207](https://leetcode.com/problems/unique-number-of-occurrences/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Easy`

## 📜 O Problema

Dado um array de inteiros `arr`, retorne `true` se o número de ocorrências de cada valor no array é **único**, ou `false` caso contrário.

**Exemplos:**
```
Input:  arr = [1,2,2,1,1,3]
Output: true
Explicação: o valor 1 tem 3 ocorrências, 2 tem 2 e 3 tem 1. Nenhum par de valores tem a mesma quantidade de ocorrências.

Input:  arr = [1,2]
Output: false

Input:  arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 1000` → pequeno, O(n) resolve com folga
- `-1000 <= arr[i] <= 1000` → valores podem ser negativos, hash map lida bem com isso

## 🧭 Como reconhecer o padrão

"As frequências em si precisam ser únicas" é um problema de "hash map de hash map" — primeiro conte a frequência de cada valor (hash map valor→contagem), depois verifique se os VALORES desse mapa (as próprias contagens) são todos distintos entre si (colocando-os num hash set e comparando tamanhos).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Contar a frequência de cada valor num hash map; depois, para cada par de valores distintos, comparar suas frequências percorrendo o mapa inteiro de novo para cada um.

- Tempo: O(n + k²), onde k é o número de valores distintos — comparação par a par das frequências · Espaço: O(k)
- **Por que não basta:** repete a comparação de frequências par a par, quando um hash set das próprias frequências decide "há duplicata?" em uma única passada, comparando o tamanho do set com o número de chaves do mapa.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um hash map `valor → frequência` percorrendo o array. Depois, coloque todos os VALORES desse mapa (as frequências) num hash set. Se o tamanho do set for igual ao número de chaves do mapa, todas as frequências são únicas → `true`; senão, houve pelo menos uma repetição → `false`.

## 🎬 Exemplo passo a passo

`arr = [1,2,2,1,1,3]` — frequência: `{1:3, 2:2, 3:1}`

| Passo | valor | frequência[valor] | já no set de frequências? |
|---|---|---|---|
| 1 | 1 | 3 | não, adiciona {3} |
| 2 | 2 | 2 | não, adiciona {3,2} |
| 3 | 3 | 1 | não, adiciona {3,2,1} |

Número de chaves no mapa (3) == tamanho do set de frequências (3) → **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para contar + uma passada para checar unicidade
- **Espaço:** O(k) — k = número de valores distintos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean uniqueOccurrences(int[] arr) {
    Map<Integer, Integer> frequencia = new HashMap<>();
    for (int num : arr) {
        frequencia.merge(num, 1, Integer::sum);
    }

    Set<Integer> frequenciasVistas = new HashSet<>(frequencia.values());
    // se alguma frequência se repete, o set fica menor que a quantidade de chaves do mapa
    return frequenciasVistas.size() == frequencia.size();
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

- Comparar os VALORES originais do array (`arr[i]`) em vez das FREQUÊNCIAS deles — o enunciado pede unicidade das contagens, não dos valores; valores já são naturalmente "únicos" como chaves de um mapa de frequência.
- Esquecer que `new HashSet<>(map.values())` já elimina duplicatas automaticamente — não precisa de lógica manual de comparação par a par.
- Achar que precisa ordenar as frequências antes de comparar — não precisa; a comparação de tamanhos entre o set e o mapa já captura a existência de duplicatas, sem precisar de ordem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Frequências únicas | `[1,2,2,1,1,3]` | true | 1 tem freq 3, 2 tem freq 2, 3 tem freq 1 — todas diferentes |
| Frequências repetidas | `[1,2]` | false | ambos os valores têm frequência 1 (empate) |
| Valores negativos e positivos | `[-3,0,1,-3,1,1,1,-3,10,0]` | true | -3:3, 0:2, 1:4, 10:1 — todas as frequências diferentes |
| Array de um elemento | `[5]` | true | uma única frequência (1), trivialmente única |

## 🔗 Conexões

- Problemas irmãos: [0242] Valid Anagram (mesma base de contagem de frequência), [0387] First Unique Character in a String (mesma ideia de usar frequência como critério de decisão)
- No backend: validação de distribuição de dados (ex.: garantir que nenhuma categoria de produto tem exatamente a mesma quantidade de vendas que outra, para desempate em relatórios), ou detecção de colisões em sistemas de contagem de eventos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
