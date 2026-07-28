# [0594] Longest Harmonious Subsequence

> 🔗 [LeetCode 594](https://leetcode.com/problems/longest-harmonious-subsequence/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#ArraysEHashing` `#HashTable` `#Counting` `#Easy`

## 📜 O Problema

Um array é **harmonioso** se a diferença entre seu valor máximo e mínimo é **exatamente** `1`. Dado um array de inteiros `nums`, retorne o tamanho da sua maior **subsequência** harmoniosa entre todas as subsequências possíveis.

**Exemplos:**
```
Input:  nums = [1,3,2,2,5,2,3,7]
Output: 5
Explicação: a subsequência harmoniosa mais longa é [3,2,2,2,3].

Input:  nums = [1,2,3,4]
Output: 2
Explicação: [1,2], [2,3] e [3,4] têm todos tamanho 2.

Input:  nums = [1,1,1,1]
Output: 0
Explicação: nenhuma subsequência harmoniosa existe.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 2 * 10^4` → O(n²) testando todo par de valores é arriscado; O(n) é alcançável
- `-10^9 <= nums[i] <= 10^9` → o intervalo é enorme demais para um array de contagem indexado pelo valor; a ferramenta certa é um hashmap
- **Subsequência**, não subarray → a ordem/contiguidade dos índices escolhidos não importa, só quais valores entram e quantas vezes cada um aparece

## 🧭 Como reconhecer o padrão

A pergunta não fala em "subarray contíguo" nem em "janela de tamanho k" — fala em **subsequência**, isto é, qualquer subconjunto de elementos independente de posição. Isso descarta janela deslizante: o que importa aqui é só **contar** quantas vezes cada valor aparece e comparar a contagem de um valor com a do seu vizinho (`valor+1`) — a assinatura clássica de um problema de hashmap de frequência.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de valores distintos `(a, b)` presentes no array com `|a - b| == 1`, contar quantas vezes `a` e `b` aparecem (varrendo o array do zero a cada par) e somar.

- Tempo: O(n²) no pior caso · Espaço: O(1) além da saída
- **Por que não basta:** recontar ocorrências de `a` e `b` repetidamente para cada par candidato desperdiça trabalho — a contagem de cada valor não muda entre as consultas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte a frequência de cada valor num hashmap em uma única passada. Depois, para cada chave `key` do mapa que também tenha `key + 1` presente, o tamanho da subsequência harmoniosa formada pelos dois é `count[key] + count[key + 1]`. Basta manter o maior valor encontrado.

## 🎬 Exemplo passo a passo

`nums = [1,3,2,2,5,2,3,7]` → mapa de contagem: `{1:1, 3:2, 2:3, 5:1, 7:1}`

| key | count[key] | key+1 presente? | count[key+1] | soma | melhor até agora |
|---|---|---|---|---|---|
| 1 | 1 | sim (2) | 3 | 4 | 4 |
| 3 | 2 | não (4) | — | — | 4 |
| 2 | 3 | sim (3) | 2 | 5 | 5 |
| 5 | 1 | não (6) | — | — | 5 |
| 7 | 1 | não (8) | — | — | 5 |

Resultado final: `5` ✔ (par de valores 2 e 3, contagens 3+2)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para contar, outra sobre as chaves do mapa (no máximo `n` chaves distintas)
- **Espaço:** O(n) — o hashmap guarda, no pior caso, um valor distinto por elemento

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findLHS(int[] nums) {
    Map<Integer, Integer> count = new HashMap<>();
    for (int num : nums) {
        count.merge(num, 1, Integer::sum);
    }

    int best = 0;
    for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
        int key = entry.getKey();
        if (count.containsKey(key + 1)) {
            best = Math.max(best, entry.getValue() + count.get(key + 1));
        }
    }

    return best;
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

- A diferença deve ser **exatamente** 1, não "no máximo 1" — um array com todos os elementos iguais tem diferença 0 e não conta, por isso `[1,1,1,1]` retorna `0`.
- Confundir subsequência com subarray: como a contiguidade não importa, **não** é um problema de janela deslizante — dá pra somar contagens de valores espalhados livremente pelo array.
- Checar se `key + 1` existe no mapa **antes** de somar sua contagem — ignorar essa checagem causa erro de acesso a uma chave ausente (ou, tratando ausência como zero por engano, uma resposta incorreta silenciosa).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Todos iguais | `[1,1,1,1]` | 0 | diferença sempre 0, nunca exatamente 1 |
| Só um par possível | `[1,2,3,4]` | 2 | qualquer par consecutivo já é a resposta máxima |
| Tamanho mínimo com par válido | `[1,2]` | 2 | diferença exatamente 1, os dois elementos contam |
| Vários candidatos empatando | `[1,3,2,2,5,2,3,7]` | 5 | (2,3) somam 3+2=5, o maior entre todos os pares |

## 🔗 Conexões

- Problemas irmãos: [0128] Longest Consecutive Sequence (mesma ideia de agrupar valores vizinhos com hashmap/hashset, mas exigindo uma sequência contínua de valores em vez de só um par), [0001] Two Sum (mesma técnica-base: hashmap pra checar em O(1) se um valor relacionado ao atual existe)
- No backend: agrupar métricas em "buckets" adjacentes — por exemplo, somar quantos usuários estão nos níveis de experiência X e X+1 combinados — sem precisar ordenar o dataset inteiro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
