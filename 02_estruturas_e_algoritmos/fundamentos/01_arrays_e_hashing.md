# 01 — Arrays e Hashing

> Categoria-base: ~40% das entrevistas passam por aqui. Soluções em [`../problemas/01_arrays_e_hashing/`](../problemas/01_arrays_e_hashing/).

## 1. Conceito Central e Analogia Didática

- **Array**: bloco contíguo de memória → acesso por índice em O(1), mas busca por valor exige varrer tudo, O(n).
- **Hash Map**: função de hash converte a chave em posição de bucket → busca/inserção/remoção em O(1) médio. É a troca clássica de **espaço por tempo**.
- **Regra de ouro**: viu `for` dentro de `for` procurando "algo que combine"? Um hash map quase sempre elimina o loop interno.

**Analogia:** o array é um prédio de apartamentos: se você sabe o número (índice), chega direto; se só sabe o nome do morador, bate de porta em porta. O hash map é a portaria com o livro de registros: fala o nome (chave) e o porteiro aponta o apartamento na hora.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se o problema pede **"dois elementos que somam/combinam"** → hash map guardando o **complemento**.
- Se pergunta **"existe duplicata?" / "quantas vezes aparece?"** → `Set` / mapa de frequência.
- Se pede para **"agrupar equivalentes"** (anagramas) → hash map com **chave canônica** (ex.: letras ordenadas).
- Se envolve **"soma de subarray/intervalo"** → **prefix sum** (+ hash map de prefixos vistos para "soma == k").
- Se exige **O(n)** onde o óbvio é O(n²) → quase sempre hashing.

## 3. Templates de Código

### Complemento (Two Sum)

```java
// Java — o par que falta vira consulta O(1) no mapa
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> vistos = new HashMap<>(); // valor -> índice: memória do que já passou
    for (int i = 0; i < nums.length; i++) {
        int complemento = target - nums[i];         // o número que FALTA para fechar a soma
        if (vistos.containsKey(complemento)) {
            return new int[]{vistos.get(complemento), i};
        }
        vistos.put(nums[i], i); // registra só DEPOIS da checagem: impede usar o mesmo elemento duas vezes
    }
    return new int[]{};
}
```

```python
# Python — mesmo raciocínio, dict nativo
def two_sum(nums, target):
    vistos = {}                          # valor -> índice
    for i, n in enumerate(nums):
        if target - n in vistos:         # o complemento já passou? achamos o par
            return [vistos[target - n], i]
        vistos[n] = i                    # registra depois: evita reutilizar o índice atual
```

### Prefix sum + hash map (subarrays com soma k)

```java
// Java — prefixo atual - k já apareceu? então existe subarray terminando aqui
public int subarraySum(int[] nums, int k) {
    Map<Integer, Integer> qtdPrefixo = new HashMap<>();
    qtdPrefixo.put(0, 1);                // caso base: subarray que começa no índice 0
    int prefixo = 0, resposta = 0;
    for (int n : nums) {
        prefixo += n;
        resposta += qtdPrefixo.getOrDefault(prefixo - k, 0); // cada prefixo antigo válido = 1 subarray
        qtdPrefixo.merge(prefixo, 1, Integer::sum);
    }
    return resposta;
}
```

```python
def subarray_sum(nums, k):
    qtd = {0: 1}                         # caso base: prefixo vazio
    prefixo = resposta = 0
    for n in nums:
        prefixo += n
        resposta += qtd.get(prefixo - k, 0)
        qtd[prefixo] = qtd.get(prefixo, 0) + 1
    return resposta
```

## 4. Walkthrough Visual (Teste de Mesa)

`twoSum(nums=[2, 7, 11, 15], target=9)`

| Iteração | i | nums[i] | complemento | complemento em vistos? | vistos após |
|---|---|---|---|---|---|
| 1 | 0 | 2 | 7 | não | `{2: 0}` |
| 2 | 1 | 7 | 2 | **sim (índice 0)** | — retorna `[0, 1]` ✔ |

- O array nem foi percorrido inteiro: o mapa devolveu a resposta assim que o par se completou.

## 5. Complexidade (Tempo e Espaço)

| Operação | Array | Hash Map |
|---|---|---|
| Acesso por índice/chave | O(1) | O(1) médio |
| Busca por valor | O(n) | O(1) médio / O(n) pior caso |
| Inserção no fim | O(1) amortizado | O(1) médio |
| Inserção no meio | O(n) | — |

- Hash é O(1) **médio** porque colisões existem; com função de hash ruim, degrada para O(n) (Hash DoS já foi ataque real).
- Prefix sum: O(n) para construir, O(1) por consulta de intervalo.

## 6. Pegadinhas e Erros Comuns

- **Java**: comparar chaves com `==` em vez de `.equals()` — para `Integer > 127` e Strings, `==` compara referência e falha silenciosamente.
- **Java**: sobrescrever `equals()` sem `hashCode()` (ou vice-versa) quebra o contrato → objeto "some" dentro do HashMap.
- **Python**: lista não pode ser chave de dict (mutável, não hasheável) → converta para `tuple`.
- Registrar o elemento no mapa **antes** de checar o complemento → aceita usar o mesmo índice duas vezes.
- Esquecer o caso base `{0: 1}` no prefix sum → perde todos os subarrays que começam no índice 0.
- Ordenar (O(n log n)) quando um mapa de frequência resolvia em O(n).

## 7. Aplicações no Mundo Real (Backend)

- **PostgreSQL**: índice **hash** e o hash join do planner são literalmente esta estrutura.
- **Redis**: um hash map gigante em rede — cache, sessão, deduplicação.
- **Spring Boot**: `@Cacheable` guarda resultado por chave; singletons do container vivem num `ConcurrentHashMap`.
- **Kafka/mensageria**: deduplicação por chave de idempotência = `Set` de IDs já processados.
- Prefix sum é a lógica de **métricas acumuladas** (bytes por janela, contadores de rate limit).

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟢 Easy |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 🟢 Easy |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 Medium |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | 🟡 Medium |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 Medium |
