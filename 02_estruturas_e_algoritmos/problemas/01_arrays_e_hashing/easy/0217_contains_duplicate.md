# [0217] Contains Duplicate

> 🔗 [LeetCode 217](https://leetcode.com/problems/contains-duplicate/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums`, retorne `true` se algum valor aparece **pelo menos duas vezes**, e `false` se todos os elementos são distintos.

**Exemplos:**
```
Input:  nums = [1,2,3,1]                       Output: true  (1 aparece 2x)
Input:  nums = [1,2,3,4]                       Output: false (todos distintos)
Input:  nums = [1,1,1,3,3,4,3,2,4,2]           Output: true
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) (10 bilhões de operações) estoura; o esperado é O(n) ou O(n log n)
- `-10^9 <= nums[i] <= 10^9` → os valores não cabem confortavelmente num array de contagem indexado por valor (seria preciso um deslocamento gigante) — hashing é a resposta natural

## 🧭 Como reconhecer o padrão

"Existe duplicata?" é o gatilho mais direto da categoria de hashing: sempre que a pergunta é sobre **existência/repetição** sem se importar com a posição, um `Set` resolve em O(1) por consulta.

## 🐢 Solução 1 — Força bruta

Comparar cada elemento com todos os outros que vêm depois dele, com dois laços aninhados.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** com n = 100.000, são até 5 bilhões de comparações — muito além do que roda em tempo aceitável. Cada comparação individual é barata, mas a quantidade delas é o problema.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array uma vez guardando cada valor visto num `Set`. Antes de adicionar um novo valor, verifique se ele **já está** no conjunto — se estiver, encontramos a duplicata na hora; não precisa nem terminar de percorrer o array.

## 🎬 Exemplo passo a passo

`nums = [1, 2, 3, 1]`

| Passo | num | 'num' está no set? | Ação | set após |
|---|---|---|---|---|
| 1 | 1 | não | adiciona | `{1}` |
| 2 | 2 | não | adiciona | `{1,2}` |
| 3 | 3 | não | adiciona | `{1,2,3}` |
| 4 | 1 | **sim** | retorna `true` imediatamente | — |

Resultado final: **true** ✔ — nem precisou processar o array inteiro.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — no pior caso (sem duplicatas), uma passada completa; consulta e inserção no set são O(1) médio
- **Espaço:** O(n) — no pior caso, todos os elementos vão parar no set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean containsDuplicate(int[] nums) {
    Set<Integer> vistos = new HashSet<>();

    for (int n : nums) {
        // add() retorna false se o elemento JÁ EXISTIA no set — evita 2 operações separadas
        if (!vistos.add(n)) {
            return true;
        }
    }
    return false;
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

- Fazer `if (vistos.contains(n)) return true; else vistos.add(n);` — funciona, mas faz **duas** operações de hash em vez de uma; `add()` do Java já retorna se o item era novo.
- Esquecer a alternativa de **ordenar primeiro** (O(n log n), O(1) espaço extra se ordenar in-place) — é um trade-off tempo×espaço válido de mencionar em entrevista.
- **Java**: `HashSet<Integer>` faz autoboxing de `int` para `Integer` — para arrays muito grandes isso tem custo de memória; em cenários de performance extrema, um `BitSet` ou array ordenado evita o boxing.
- Assumir que os valores cabem em um array de contagem direta — com `nums[i]` podendo ser `-10^9` a `10^9`, um array indexado por valor precisaria de bilhões de posições: inviável.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento | `[7]` | false | borda mínima, impossível ter duplicata |
| Duplicata no início | `[5,5,1,2]` | true | testa a saída antecipada |
| Duplicata no fim | `[1,2,3,3]` | true | testa que percorre até o fim quando precisa |
| Valores negativos | `[-1,-1,2]` | true | garante que negativos são tratados como qualquer int |

## 🔗 Conexões

- Problemas irmãos: **[0219] Contains Duplicate II** (agora com restrição de distância `k` entre os índices — usa a mesma ideia de set, mas com janela deslizante), **[0220] Contains Duplicate III** (com tolerância de valor — combina busca binária/bucket)
- No backend: deduplicação de eventos por chave de idempotência (Fase 6.4), detecção de chave duplicada antes de um `INSERT` em batch, e verificação de unicidade de e-mail/CPF em cadastro usam exatamente este padrão de "set de vistos".

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
