# [1122] Relative Sort Array

> 🔗 [LeetCode 1122](https://leetcode.com/problems/relative-sort-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dados dois arrays `arr1` e `arr2`, os elementos de `arr2` são distintos, e todos os elementos de `arr2` também estão em `arr1`.

Ordene os elementos de `arr1` de forma que a ordem relativa dos itens siga a mesma ordem de `arr2`. Elementos que não aparecem em `arr2` devem ser colocados no final de `arr1`, em ordem **crescente**.

**Exemplos:**
```
Input:  arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Input:  arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
```

**Restrições (e o que elas denunciam):**
- `1 <= arr1.length, arr2.length <= 1000`, `0 <= arr1[i], arr2[i] <= 1000` → valores pequenos e limitados, habilita counting sort
- elementos de `arr2` são distintos e todos estão em `arr1` → cada valor de `arr2` define uma prioridade de ordenação única
- elementos de `arr1` que não estão em `arr2` vão pro final, em ordem crescente → precisa separar esses "extras" e ordená-los à parte

## 🧭 Como reconhecer o padrão

"Ordene um array segundo uma ordem de prioridade customizada definida por outro array" é resolvido contando a frequência de cada valor de `arr1` (counting sort, já que os valores são pequenos e limitados), e depois reconstruindo a saída: primeiro os valores de `arr2` na ordem dada (repetidos conforme a contagem), depois os valores restantes em ordem crescente.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada valor de `arr2`, percorrer `arr1` inteiro extraindo todas as ocorrências desse valor; no final, ordenar o que sobrou.

- Tempo: O(len(arr2) × len(arr1)) para extrair as ocorrências, mais O(k log k) para ordenar o restante · Espaço: O(n)
- **Por que não basta:** percorre `arr1` inteiro uma vez para CADA valor de `arr2`, quando uma única passada de contagem (counting sort) já captura a frequência de todos os valores de uma vez.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um array de contagem (`contagem[0..1000]`) percorrendo `arr1` uma única vez. Depois, percorra `arr2` na ordem dada, emitindo cada valor `contagem[valor]` vezes (e zerando essa contagem). Por fim, percorra o array de contagem inteiro (0 a 1000) emitindo os valores restantes (que não estavam em `arr2`) em ordem crescente natural.

## 🎬 Exemplo passo a passo

`arr1 = [2,3,1,3,2,4,6,7,9,2,19]`, `arr2 = [2,1,4,3,9,6]`

contagem: 1→1, 2→3, 3→2, 4→1, 6→1, 7→1, 9→1, 19→1

| Passo | Fase | valor | emissões | resultado parcial |
|---|---|---|---|---|
| 1 | arr2 | 2 | 2,2,2 | [2,2,2] |
| 2 | arr2 | 1 | 1 | [2,2,2,1] |
| 3 | arr2 | 4 | 4 | [2,2,2,1,4] |
| 4 | arr2 | 3 | 3,3 | [2,2,2,1,4,3,3] |
| 5 | arr2 | 9 | 9 | [2,2,2,1,4,3,3,9] |
| 6 | arr2 | 6 | 6 | [2,2,2,1,4,3,3,9,6] |
| 7 | restante (crescente) | 7 | 7 | [2,2,2,1,4,3,3,9,6,7] |
| 8 | restante (crescente) | 19 | 19 | [2,2,2,1,4,3,3,9,6,7,19] |

Resultado final: `[2,2,2,1,4,3,3,9,6,7,19]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + k) — n = len(arr1), k = intervalo de valores possíveis (1001) — melhor que O(n log n) de um sort genérico quando k é pequeno
- **Espaço:** O(n + k)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] relativeSortArray(int[] arr1, int[] arr2) {
    int[] contagem = new int[1001]; // valores de arr1 vão de 0 a 1000
    for (int valor : arr1) {
        contagem[valor]++;
    }

    int[] resultado = new int[arr1.length];
    int pos = 0;

    // primeiro, os valores de arr2, na ordem dada, repetidos conforme a contagem
    for (int valor : arr2) {
        while (contagem[valor] > 0) {
            resultado[pos++] = valor;
            contagem[valor]--;
        }
    }

    // depois, os valores restantes (que não estavam em arr2), em ordem crescente natural
    for (int valor = 0; valor < contagem.length; valor++) {
        while (contagem[valor] > 0) {
            resultado[pos++] = valor;
            contagem[valor]--;
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

- Usar um sort genérico com um comparador customizado (mapa `valor → prioridade` para os elementos de `arr2`, e uma prioridade "infinita" para os demais) — funciona e é mais genérico, mas é O(n log n); vale conhecer o counting sort como alternativa O(n + k) já que o problema garante valores pequenos e limitados.
- Esquecer que os valores repetidos em `arr1` (ex.: `2` aparece 3 vezes no exemplo) precisam aparecer o MESMO número de vezes na saída — o counting sort resolve isso naturalmente ao emitir `contagem[valor]` cópias.
- Não zerar a contagem de um valor depois de emiti-lo na fase de `arr2` — sem zerar, o mesmo valor seria emitido de novo na fase "restante", duplicando elementos incorretamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso com repetições | `arr1=[2,3,1,3,2,4,6,7,9,2,19], arr2=[2,1,4,3,9,6]` | [2,2,2,1,4,3,3,9,6,7,19] | caso padrão do enunciado |
| Sem elementos restantes | `arr1=[28,6,22,8,44,17], arr2=[22,28,8,6]` | [22,28,8,6,17,44] | "17" e "44" não estão em arr2, vão ordenados no final |
| arr2 cobre tudo | `arr1=[1,2,3], arr2=[3,2,1]` | [3,2,1] | nenhum elemento "restante" |
| Um único elemento repetido | `arr1=[5,5,5], arr2=[5]` | [5,5,5] | caso mínimo com repetição total |

## 🔗 Conexões

- Problemas irmãos: [1051] Height Checker (mesmo domínio de counting sort com valores limitados), [0075] Sort Colors (mesma técnica de counting sort aplicada a um caso especial de 3 valores)
- No backend: ordenação de itens segundo uma prioridade de negócio customizada (ex.: exibir produtos em destaque numa ordem específica primeiro, depois o restante do catálogo em ordem alfabética/numérica) — o mesmo padrão de "prioridade explícita + resto em ordem natural" aparece em rankings de e-commerce.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
