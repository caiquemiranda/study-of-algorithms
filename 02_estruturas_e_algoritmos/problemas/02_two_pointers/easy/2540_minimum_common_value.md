# [2540] Minimum Common Value

> 🔗 [LeetCode 2540](https://leetcode.com/problems/minimum-common-value/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#TwoPointers` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Você recebe dois arrays de inteiros `nums1` e `nums2`, **ambos ordenados** de forma não decrescente. Retorne o **menor inteiro comum** aos dois arrays (que aparece pelo menos uma vez em cada). Se não houver nenhum, retorne `-1`.

**Exemplos:**
```
Input:  nums1 = [1,2,3], nums2 = [2,4]        Output: 2
Input:  nums1 = [1,2,3,6], nums2 = [2,3,4,5]  Output: 2   (2 e 3 são comuns, o menor é 2)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums1.length, nums2.length <= 10^5` → força bruta O(n×m) chegaria a 10^10, totalmente inviável
- "Both nums1 and nums2 are sorted in non-decreasing order" → sinal direto para uma técnica que aproveite a ordenação de **ambos** os arrays simultaneamente, sem precisar reordenar nada
- `1 <= nums1[i], nums2[j] <= 10^9` → valores grandes, então nada de bucket/contagem por índice direto; a técnica precisa depender só da ordenação

## 🧭 Como reconhecer o padrão

"Dois arrays **já ordenados**" + "ache o menor elemento em comum" é a assinatura clássica de **merge de dois arrays ordenados com dois ponteiros**: ande pelos dois arrays simultaneamente, sempre avançando o ponteiro que aponta para o menor valor, até os dois ponteiros baterem no mesmo valor (ou um dos arrays acabar).

## 🐢 Solução 1 — Força bruta

Para cada elemento de `nums1`, percorrer `nums2` inteiro procurando um valor igual; guardar o menor encontrado.

- Tempo: O(n × m) · Espaço: O(1)
- **Por que não basta:** com `n` e `m` até 10^5, o produto chega a 10^10 comparações — inviável. Ignora completamente que os dois arrays já vêm ordenados, o que permite uma varredura conjunta em uma única passada por cada.

Uma alternativa intermediária seria colocar `nums2` num hash set (O(m)) e varrer `nums1` guardando o menor valor presente no set (O(n)) — funciona em O(n+m), mas gasta espaço extra que a técnica de dois ponteiros dispensa (já que ambos os arrays estão ordenados).

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um ponteiro `i` em `nums1` e outro `j` em `nums2`, os dois começando em `0`. A cada passo, compare `nums1[i]` com `nums2[j]`:
- Se forem **iguais**, achou o menor comum — retorna esse valor (porque ambos os arrays estão ordenados, o primeiro encontro é necessariamente o menor).
- Se `nums1[i] < nums2[j]`, o valor de `nums1[i]` é menor demais para aparecer em `nums2` a partir de `j` (já que `nums2` só cresce daqui pra frente) → avança `i`.
- Se `nums1[i] > nums2[j]`, simetricamente, avança `j`.

Se um dos ponteiros chegar ao fim do array sem achar igualdade, não existe elemento comum — retorna `-1`.

## 🎬 Exemplo passo a passo

`nums1 = [1, 2, 3, 6]`, `nums2 = [2, 3, 4, 5]`

| Passo | i (val) | j (val) | Comparação | Decisão |
|---|---|---|---|---|
| 1 | 0 (1) | 0 (2) | 1 < 2 | `i++` |
| 2 | 1 (2) | 0 (2) | 2 == 2 → achou! | retorna 2 |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — cada ponteiro percorre seu array no máximo uma vez, nunca anda para trás
- **Espaço:** O(1) — só dois ponteiros inteiros, sem estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int getCommon(int[] nums1, int[] nums2) {
    int i = 0, j = 0;

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] == nums2[j]) {
            return nums1[i];             // primeiro encontro = o menor, já que ambos ordenados
        } else if (nums1[i] < nums2[j]) {
            i++;                         // nums1[i] é pequeno demais para reaparecer mais à frente em nums2
        } else {
            j++;                         // nums2[j] é pequeno demais para reaparecer mais à frente em nums1
        }
    }
    return -1;                           // um dos arrays acabou sem achar valor comum
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

- **Avançar os dois ponteiros ao mesmo tempo quando os valores diferem**: só avança o ponteiro do **menor** valor — avançar ambos pode pular por cima de um match válido.
- **Esquecer a condição de parada de um dos arrays**: o laço precisa checar `i < nums1.length && j < nums2.length` — parar cedo demais ou tarde demais causa acesso fora dos limites.
- **Tentar aplicar busca binária ingenuamente**: buscar cada elemento de `nums1` dentro de `nums2` via binary search funciona (O(n log m)), mas é estritamente pior que o passeio conjunto de dois ponteiros O(n+m) — por isso a categoria final é two pointers, não busca binária, mesmo a tag do LeetCode sugerindo as duas.
- **Duplicatas dentro do mesmo array**: não afetam a lógica — o algoritmo só se importa com a comparação entre os dois ponteiros atuais, repetições dentro de um único array são naturalmente puladas.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem elemento comum | `nums1=[1,2], nums2=[3,4]` | -1 | testa a condição de parada sem match |
| Um elemento cada, igual | `nums1=[5], nums2=[5]` | 5 | borda mínima com match imediato |
| Comum é o último de ambos | `nums1=[1,2,3], nums2=[3]` | 3 | testa convergência no fim dos arrays |
| Múltiplos comuns | `nums1=[1,2,3,6], nums2=[2,3,4,5]` | 2 | trace acima, garante que pega o menor |
| Arrays com muitas repetições | `nums1=[1,1,2,2,3], nums2=[2,2,2]` | 2 | duplicatas não confundem a lógica |

## 🔗 Conexões

- Problemas irmãos: **[0349] Intersection of Two Arrays** (mesma ideia de interseção, mas via hash set em arrays não ordenados), **[0167] Two Sum II - Input Array Is Sorted** (mesma técnica de dois ponteiros aproveitando ordenação)
- No backend: essa é literalmente a estratégia de **merge join** usada por bancos de dados para juntar duas tabelas já ordenadas pela chave — percorrer ambas simultaneamente é muito mais barato que um nested loop join ou até um hash join quando os dados já vêm ordenados (ex.: por índice).

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente a buscar cada elemento de um array no outro), mas a técnica ótima é o passeio conjunto com dois ponteiros (O(n+m), sem custo de log), então o documento foi classificado em `02_two_pointers`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
