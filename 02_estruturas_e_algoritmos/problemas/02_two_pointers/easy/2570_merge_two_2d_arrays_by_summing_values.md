# [2570] Merge Two 2D Arrays by Summing Values

> 🔗 [LeetCode 2570](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dados `nums1` e `nums2`, onde cada `[id, val]` associa um id (único, ordenado crescente) a um valor, mescle os dois num único array ordenado por id: cada id aparece uma vez, com valor igual à soma dos valores desse id nos dois arrays (`0` se o id não existir num deles).

**Exemplos:**
```
Input:  nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]

Input:  nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums1.length, nums2.length <= 200` → O(n+m) esperado
- Ids **únicos** e ambos os arrays em ordem **estritamente crescente** → exatamente a condição necessária para mesclar com dois ponteiros, sem precisar reordenar nada
- Ids ausentes valem `0` → equivale a "pegar o que existe" quando não há correspondência do outro lado

## 🧭 Como reconhecer o padrão

"Mesclar duas listas chave-valor já ordenadas pela chave, somando valores de chaves em comum" é o mesmo padrão de merge de [0088] Merge Sorted Array e [0021] Merge Two Sorted Lists: dois ponteiros avançam pelos dois arrays comparando as chaves (ids) atuais — o menor id "vence" e entra no resultado sozinho; ids iguais somam e avançam os dois ponteiros juntos.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar um `HashMap<Integer,Integer>` (id → soma), percorrendo os dois arrays e acumulando os valores por id; depois extrair as chaves, ordená-las, e montar o resultado.

- Tempo: O((n+m) log(n+m)) — dominado pela ordenação das chaves no final · Espaço: O(n+m) para o mapa
- **Por que não basta:** os dois arrays JÁ vêm ordenados por id; usar um mapa e reordenar do zero ignora completamente essa estrutura. Dois ponteiros mesclam direto, na ordem certa, sem nenhuma reordenação posterior.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `i` em `nums1` e `j` em `nums2`. Compare os ids atuais (`nums1[i][0]` vs `nums2[j][0]`): se forem iguais, some os valores e avance os dois ponteiros; se `nums1[i][0]` for menor, ele "vence" (nenhuma correspondência em `nums2` ainda), adicione-o sozinho e avance só `i`; caso contrário, faça o simétrico com `nums2` e `j`. Quando um dos arrays esgotar, copie o restante do outro diretamente (ele já está ordenado).

## 🎬 Exemplo passo a passo

`nums1 = [[1,2],[2,3],[4,5]]`, `nums2 = [[1,4],[3,2],[4,1]]`

| Passo | nums1[i] | nums2[j] | Comparação | Ação | Resultado parcial |
|---|---|---|---|---|---|
| 1 | [1,2] | [1,4] | id 1 == id 1 | soma → `[1,6]` | `[[1,6]]` |
| 2 | [2,3] | [3,2] | id 2 < id 3 | pega de nums1 → `[2,3]` | `[[1,6],[2,3]]` |
| 3 | [4,5] | [3,2] | id 4 > id 3 | pega de nums2 → `[3,2]` | `[[1,6],[2,3],[3,2]]` |
| 4 | [4,5] | [4,1] | id 4 == id 4 | soma → `[4,6]` | `[[1,6],[2,3],[3,2],[4,6]]` |

Ambos os ponteiros esgotam juntos → resultado final: `[[1,6],[2,3],[3,2],[4,6]]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — cada elemento dos dois arrays é visitado exatamente uma vez
- **Espaço:** O(n + m) para o array de resultado (exigido pelo problema); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
    List<int[]> result = new ArrayList<>();
    int i = 0;
    int j = 0;

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i][0] == nums2[j][0]) {
            result.add(new int[]{nums1[i][0], nums1[i][1] + nums2[j][1]});
            i++;
            j++;
        } else if (nums1[i][0] < nums2[j][0]) {
            result.add(nums1[i]);
            i++;
        } else {
            result.add(nums2[j]);
            j++;
        }
    }
    // copia o que sobrou de qualquer um dos dois arrays (o outro já esgotou)
    while (i < nums1.length) {
        result.add(nums1[i++]);
    }
    while (j < nums2.length) {
        result.add(nums2[j++]);
    }

    return result.toArray(new int[result.size()][]);
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

- Esquecer de copiar o restante de um dos arrays depois que o outro esgota — se `nums1` acabar antes de `nums2` (ou vice-versa), os elementos restantes do array mais longo ainda precisam entrar no resultado, na ordem em que estão.
- Comparar os arrays `nums1[i]` e `nums2[j]` inteiros em vez de comparar só `nums1[i][0]` com `nums2[j][0]` — a comparação de ordenação é só pelo id, o valor não entra na decisão.
- Ao encontrar ids iguais, avançar só um dos ponteiros — sem avançar OS DOIS, o mesmo id seria reprocessado na próxima iteração, gerando uma entrada duplicada ou incorreta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ids em comum | `nums1=[[1,2],[2,3],[4,5]]`, `nums2=[[1,4],[3,2],[4,1]]` | `[[1,6],[2,3],[3,2],[4,6]]` | ids 1 e 4 aparecem nos dois, valores somados |
| Sem ids em comum | `nums1=[[2,4],[3,6],[5,5]]`, `nums2=[[1,3],[4,3]]` | `[[1,3],[2,4],[3,6],[4,3],[5,5]]` | mescla simples, como um merge de listas ordenadas |
| Sobra no final | `nums1=[[1,1]]`, `nums2=[[1,1],[2,2]]` | `[[1,2],[2,2]]` | depois do id 1 (somado), sobra o id 2 de nums2 sozinho |
| Sem ids em comum, tamanho 1 | `nums1=[[1,5]]`, `nums2=[[2,10]]` | `[[1,5],[2,10]]` | nenhuma soma, só ordenação por id |

## 🔗 Conexões

- Problemas irmãos: [0088] Merge Sorted Array (mesma técnica de mesclar duas sequências ordenadas com dois ponteiros), [0021] Merge Two Sorted Lists (mesma ideia aplicada a listas encadeadas)
- No backend: mesclar dois conjuntos de métricas/contadores já ordenados por chave — por exemplo, agregar contagens de eventos de dois shards de um sistema distribuído, cada um já ordenado por ID de evento, somando valores de chaves em comum sem precisar reordenar nada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
