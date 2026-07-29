# [0350] Intersection of Two Arrays II

> 🔗 [LeetCode 350](https://leetcode.com/problems/intersection-of-two-arrays-ii/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArraysEHashing` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Dado dois arrays `nums1` e `nums2`, retorne a interseção deles — mas agora cada elemento deve aparecer no resultado **tantas vezes quanto aparece nos dois arrays** (o mínimo das duas contagens). A ordem não importa.

**Exemplos:**
```
Input:  nums1 = [1,2,2,1], nums2 = [2,2]        Output: [2,2]
Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]    Output: [4,9]   ([9,4] também é aceito)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums1.length, nums2.length <= 1000` → tamanho pequeno, força bruta O(n*m) passaria, mas hashing resolve em O(n+m) sem esforço extra
- `0 <= nums1[i], nums2[i] <= 1000` → valores num intervalo pequeno; contagem por hashmap (ou até array de contagem) é natural
- **Follow up** ("e se um array já vier ordenado?", "e se `nums2` estiver em disco e não couber na memória?") → sinaliza que a solução "padrão" (hashmap) não é a única resposta certa: com array ordenado, dois ponteiros são mais eficientes em memória; com dados em disco, contar o array pequeno em memória e varrer o grande em streaming (com **busca binária** por elemento) é a resposta certa

## 🧭 Como reconhecer o padrão

Diferente da versão I (que só quer "existe ou não"), aqui a pergunta é "quantas vezes cada valor se repete nos dois arrays". Isso é a assinatura de **contagem de frequência com hashmap**: conte ocorrências no menor array, depois consuma essa contagem enquanto varre o outro.

## 🐢 Solução 1 — Força bruta

Para cada elemento de `nums1` ainda não "usado", procurar em `nums2` um elemento igual ainda não usado; se achar, marcar os dois como usados e adicionar ao resultado.

- Tempo: O(n × m) · Espaço: O(min(n,m)) para marcar usados
- **Por que não basta:** repete a busca em `nums2` para cada elemento de `nums1`, ignorando que contar ocorrências de antemão resolve tudo numa única passada por array.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um **hashmap de contagem** a partir do menor dos dois arrays (`valor -> quantas vezes aparece`). Depois percorra o outro array: para cada elemento, se ele existe no hashmap com contagem > 0, adiciona ao resultado e **decrementa** a contagem (para não usar o mesmo "crédito" duas vezes).

Contar no array menor primeiro reduz o espaço usado pelo hashmap, mas não é obrigatório — funciona igual com qualquer um dos dois, só muda o consumo de memória.

## 🎬 Exemplo passo a passo

`nums1 = [1, 2, 2, 1]`, `nums2 = [2, 2]`

| Passo | Estrutura | Elemento processado | Ação | Estado |
|---|---|---|---|---|
| 1 | contagem = `{1:2, 2:2}` | (construção a partir de nums1) | — | contagem pronta |
| 2 | resultado = `[]` | nums2[0] = 2 | contagem[2]=2 > 0 → adiciona, decrementa | resultado=`[2]`, contagem=`{1:2, 2:1}` |
| 3 | resultado = `[2]` | nums2[1] = 2 | contagem[2]=1 > 0 → adiciona, decrementa | resultado=`[2,2]`, contagem=`{1:2, 2:0}` |

Resultado final: `[2, 2]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — uma passada para contar, outra para consumir
- **Espaço:** O(min(n, m)) — o hashmap guarda só o menor dos dois arrays

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] intersect(int[] nums1, int[] nums2) {
    // Conta a partir do menor array para minimizar o tamanho do hashmap.
    if (nums1.length > nums2.length) {
        return intersect(nums2, nums1);
    }

    Map<Integer, Integer> contagem = new HashMap<>();
    for (int n : nums1) {
        contagem.merge(n, 1, Integer::sum);   // incrementa a contagem de "n"
    }

    List<Integer> resultado = new ArrayList<>();
    for (int n : nums2) {
        int restante = contagem.getOrDefault(n, 0);
        if (restante > 0) {
            resultado.add(n);
            contagem.put(n, restante - 1);    // "consome" uma ocorrência para não repetir demais
        }
    }

    // Converte List<Integer> para int[], formato exigido pelo enunciado.
    int[] saida = new int[resultado.size()];
    for (int i = 0; i < saida.length; i++) {
        saida[i] = resultado.get(i);
    }
    return saida;
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

- **Esquecer de decrementar a contagem**: sem isso, um valor que aparece 1 vez em `nums1` mas 3 vezes em `nums2` entraria 3 vezes no resultado em vez de apenas 1 (o mínimo entre as duas contagens).
- **Confundir com a versão I**: aqui repetições importam — `[2,2]` é diferente de `[2]`. Usar `Set` (como na versão I) perderia a contagem correta.
- **Ignorar os follow-ups**: se um array já está ordenado, dois ponteiros resolvem em O(n+m) sem gastar memória de hashmap; se `nums2` está em disco (não cabe na memória), a resposta certa é contar o array pequeno em memória e, para cada chunk lido de `nums2`, fazer busca binária (ou consulta ao hashmap) — é aí que "busca binária" genuinamente entra neste problema, mas só no cenário de memória limitada, não na solução geral.
- **Assumir que a ordem do resultado importa**: o enunciado aceita qualquer ordem — não há necessidade de ordenar a saída.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem interseção | `nums1=[1,2], nums2=[3,4]` | `[]` | garante que não quebra sem match |
| Contagens diferentes | `nums1=[1,2,2,1], nums2=[2,2]` | `[2,2]` | testa que usa o mínimo das contagens |
| Um array bem maior que o outro | `nums1=[1], nums2=[1,1,1,1]` | `[1]` | só 1 ocorrência em nums1 limita o resultado |
| Arrays idênticos com repetição | `nums1=[1,1,2], nums2=[1,1,2]` | `[1,1,2]` | interseção total preservando contagem |
| Um elemento cada, sem match | `nums1=[5], nums2=[6]` | `[]` | borda mínima sem interseção |

## 🔗 Conexões

- Problemas irmãos: **[0349] Intersection of Two Arrays** (mesma ideia, mas sem contar repetições), **[0242] Valid Anagram** (mesma técnica de hashmap de contagem para comparar duas coleções)
- No backend: contagem de interseção com multiplicidade é o mesmo padrão usado para conciliar estoques (quantas unidades de cada SKU aparecem tanto no pedido quanto no depósito) ou para calcular quantos itens em comum existem entre dois carrinhos de compra, contagem incluída.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente ao cenário de follow-up com dados em disco), mas a solução geral ótima é hashmap de contagem (O(n+m)); busca binária só entra como otimização de memória num cenário específico, então o documento foi classificado em `01_arrays_e_hashing`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
