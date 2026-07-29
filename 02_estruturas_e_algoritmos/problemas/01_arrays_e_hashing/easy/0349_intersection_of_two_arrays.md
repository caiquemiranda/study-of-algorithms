# [0349] Intersection of Two Arrays

> 🔗 [LeetCode 349](https://leetcode.com/problems/intersection-of-two-arrays/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArraysEHashing` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Dado dois arrays de inteiros `nums1` e `nums2`, retorne a **interseção** deles: os elementos que aparecem nos dois. Cada elemento do resultado deve ser **único** (sem repetir), e a ordem não importa.

**Exemplos:**
```
Input:  nums1 = [1,2,2,1], nums2 = [2,2]        Output: [2]
Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]    Output: [9,4]   ([4,9] também é aceito
```

**Restrições (e o que elas denunciam):**
- `1 <= nums1.length, nums2.length <= 1000` → tamanho pequeno, então até força bruta O(n*m) passaria, mas existe algo bem mais direto
- `0 <= nums1[i], nums2[i] <= 1000` → valores num intervalo pequeno e não-negativo, o que também abriria espaço para "contagem por bucket", mas hash set já resolve de forma simples e genérica
- "each element in the result must be unique" → sinal claro de que precisamos de uma estrutura que dedupe sozinha — é a assinatura de **conjunto (set)**

## 🧭 Como reconhecer o padrão

"Quais elementos aparecem em ambos os arrays" é o padrão de **interseção de conjuntos**: transforme um array numa estrutura de consulta O(1) (hash set) e varra o outro perguntando "esse elemento está no set?". Embora o enunciado tenha a tag `binary-search` no LeetCode (por causa de uma variante que ordena e faz busca binária), a técnica realmente ótima aqui é hashing — ver a nota de reclassificação no fim.

## 🐢 Solução 1 — Força bruta

Para cada elemento de `nums1`, percorrer `nums2` inteiro verificando se ele existe; se existir e ainda não estiver no resultado, adiciona.

- Tempo: O(n × m) · Espaço: O(n) para o resultado
- **Por que não basta:** para cada um dos `n` elementos de `nums1`, faz uma varredura O(m) em `nums2` — repete trabalho que poderia ser feito uma vez só transformando `nums2` numa estrutura de busca O(1).

Uma alternativa "busca binária": ordenar `nums2` (O(m log m)) e, para cada elemento de `nums1`, fazer busca binária nele (O(log m)) — total O((n+m) log m). É melhor que a força bruta, mas ainda perde para hashing.

## 💡 Solução 2 — A ideia otimizada (intuição)

Jogue todos os elementos de `nums1` num **hash set** — isso vira uma "lista de convidados" com consulta O(1). Depois percorra `nums2` uma única vez: cada elemento que estiver no set de `nums1` e ainda não tiver sido adicionado ao resultado é parte da interseção.

Não precisamos ordenar nada — um hash set não se importa com ordem, e resolve em uma passada por array.

## 🎬 Exemplo passo a passo

`nums1 = [4, 9, 5]`, `nums2 = [9, 4, 9, 8, 4]`

| Passo | Estrutura | Elemento processado | Ação | Estado |
|---|---|---|---|---|
| 1 | set1 = `{4, 9, 5}` | (construção do set a partir de nums1) | — | set1 pronto |
| 2 | resultado = `{}` | nums2[0] = 9 | 9 está em set1 → adiciona | resultado = `{9}` |
| 3 | resultado = `{9}` | nums2[1] = 4 | 4 está em set1 → adiciona | resultado = `{9,4}` |
| 4 | resultado = `{9,4}` | nums2[2] = 9 | 9 já está no resultado → ignora | resultado = `{9,4}` |
| 5 | resultado = `{9,4}` | nums2[3] = 8 | 8 não está em set1 → ignora | resultado = `{9,4}` |
| 6 | resultado = `{9,4}` | nums2[4] = 4 | já está no resultado → ignora | resultado = `{9,4}` |

Resultado final: `[9, 4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — uma passada para construir o set, outra para consultar
- **Espaço:** O(n + m) — o hash set de `nums1` mais o set/lista de resultado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] intersection(int[] nums1, int[] nums2) {
    Set<Integer> set1 = new HashSet<>();
    for (int n : nums1) {
        set1.add(n);                          // consulta O(1) depois, sem precisar ordenar nums1
    }

    Set<Integer> resultado = new HashSet<>();  // já garante unicidade sozinho
    for (int n : nums2) {
        if (set1.contains(n)) {
            resultado.add(n);
        }
    }

    // Converte o set de volta para array, formato exigido pelo enunciado.
    int[] saida = new int[resultado.size()];
    int i = 0;
    for (int n : resultado) {
        saida[i++] = n;
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

- **Usar `List` em vez de `Set` para o resultado**: sem uma estrutura que dedupe, é fácil adicionar o mesmo valor duas vezes quando ele se repete em `nums2` (ex.: o `9` aparece duas vezes em `nums2` no exemplo acima).
- **Colocar `nums2` inteiro no set em vez de `nums1`**: funciona igual em complexidade, mas prestar atenção em qual array vira "índice de consulta" evita confusão ao debugar.
- **Achar que precisa ordenar**: a tag `binary-search`/`sorting` do LeetCode sugere isso, mas ordenar custa O(n log n) — sem necessidade quando um hash set resolve em O(n) sem ordenar nada.
- **Esquecer de tratar arrays vazios ou sem interseção**: o resultado pode legitimamente ser um array vazio.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem interseção | `nums1=[1,2], nums2=[3,4]` | `[]` | garante que a função não quebra sem match algum |
| Todos repetidos, um resultado | `nums1=[1,1,1], nums2=[1,1]` | `[1]` | testa deduplicação |
| Arrays idênticos | `nums1=[1,2,3], nums2=[1,2,3]` | `[1,2,3]` (em qualquer ordem) | interseção total |
| Um elemento cada | `nums1=[5], nums2=[5]` | `[5]` | borda mínima |
| Exemplo do enunciado | `nums1=[4,9,5], nums2=[9,4,9,8,4]` | `[9,4]` ou `[4,9]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0350] Intersection of Two Arrays II** (mesma ideia, mas conta repetições em vez de deduplicar), **[1346] Check If N and Its Double Exist** (mesmo padrão de hash set para consulta O(1))
- No backend: interseção de conjuntos via hash é o mesmo raciocínio por trás de "quais usuários estão em duas listas de segmentação de marketing" ou "quais IDs de produto existem tanto no catálogo quanto no estoque" — problemas de reconciliação de dados resolvidos sem precisar de joins ordenados.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (por causa da tag `binary-search` no LeetCode, referente à variante ordenar+buscar), mas a técnica realmente ótima é hash set (O(n+m), sem precisar ordenar), então o documento foi classificado em `01_arrays_e_hashing`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
