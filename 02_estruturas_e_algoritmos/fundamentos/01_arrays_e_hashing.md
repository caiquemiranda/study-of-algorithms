# 01 — Arrays e Hashing

> A base de tudo. ~40% dos problemas de entrevista se resolvem com array + hash map. Problemas em [`../problemas/01_arrays_e_hashing/`](../problemas/01_arrays_e_hashing/).

## Conceito

**Array**: memória contígua, acesso por índice em O(1), inserção/remoção no meio em O(n). A contiguidade é o motivo de ser rápido na prática (localidade de cache — ver Fase 1.1).

**Hash Map / Hash Set**: troca **espaço por tempo**. Uma função de hash mapeia a chave para um bucket; busca/inserção/remoção em O(1) médio (O(n) no pior caso com colisões). É a ferramenta nº 1 para eliminar loops aninhados: sempre que você escrever `for` dentro de `for` procurando "algo que combine", pergunte se um hash map não elimina o loop interno.

**Ideias-chave que caem junto:**
- **Mapa de frequência**: `Counter`/`dict` contando ocorrências — anagramas, elementos majoritários, top-K
- **Chave canônica**: transformar cada elemento numa forma normalizada para agrupar (ex.: ordenar as letras de uma palavra para agrupar anagramas, ou usar tupla de contagem de 26 letras)
- **Prefix Sum**: `prefix[i] = soma de nums[0..i-1]` → soma de qualquer intervalo em O(1): `soma(i,j) = prefix[j+1] - prefix[i]`. Com hash map de prefixos vistos, resolve "subarray com soma k" em O(n)
- **Set para existência**: "já vi esse elemento?" em O(1)

## Como reconhecer no enunciado

- "encontre **dois** elementos que..." → hash map (complemento)
- "existe duplicata / quantas vezes aparece" → set / mapa de frequência
- "agrupe os que são equivalentes" → hash map com chave canônica
- "soma de subarray / intervalo" → prefix sum
- "em O(n)" quando a solução óbvia é O(n²) → quase sempre hashing

## Templates

```python
# Complemento (Two Sum) — O(n)
def two_sum(nums, target):
    vistos = {}                       # valor -> índice
    for i, n in enumerate(nums):
        if target - n in vistos:
            return [vistos[target - n], i]
        vistos[n] = i

# Chave canônica (Group Anagrams) — O(n·k)
from collections import defaultdict
def group_anagrams(strs):
    grupos = defaultdict(list)
    for s in strs:
        chave = tuple(sorted(s))      # ou tupla de contagem de 26 letras
        grupos[chave].append(s)
    return list(grupos.values())

# Prefix sum + hash map (subarrays com soma k) — O(n)
def subarray_sum(nums, k):
    contagem, prefixo, resp = {0: 1}, 0, 0
    for n in nums:
        prefixo += n
        resp += contagem.get(prefixo - k, 0)
        contagem[prefixo] = contagem.get(prefixo, 0) + 1
    return resp
```

## Complexidade típica

| Operação | Array | Hash Map |
|---|---|---|
| Acesso por índice/chave | O(1) | O(1) médio |
| Busca por valor | O(n) | O(1) médio |
| Inserção/remoção no fim | O(1) amortizado | O(1) médio |
| Inserção/remoção no meio | O(n) | — |

## Erros comuns

- Usar lista como chave de dict (não é hasheável) — converta para `tuple`
- Esquecer que hash map **não mantém ordem de classificação** (dict do Python mantém ordem de *inserção*)
- No prefix sum, esquecer o caso base `{0: 1}` (subarray que começa no índice 0)
- Ordenar quando um mapa de frequência resolvia (O(n log n) vs O(n))
- Em Java: `==` em vez de `.equals()` para chaves; violar o contrato `equals`/`hashCode`

## Problemas recomendados (ordem de estudo)

| Problema | Dificuldade |
|---|---|
| 217. Contains Duplicate | 🟢 easy |
| 242. Valid Anagram | 🟢 easy |
| 1. Two Sum | 🟢 easy |
| 49. Group Anagrams | 🟡 medium |
| 347. Top K Frequent Elements | 🟡 medium |
| 238. Product of Array Except Self | 🟡 medium |
| 36. Valid Sudoku | 🟡 medium |
| 271. Encode and Decode Strings | 🟡 medium |
| 128. Longest Consecutive Sequence | 🟡 medium |
| 560. Subarray Sum Equals K | 🟡 medium |

## Conexão com backend

Hash map é a estrutura por trás de: `HashMap`/`ConcurrentHashMap` do Java, índices hash de banco, cache (Redis é um hash map gigante em rede), tabela de sessões, deduplicação de eventos (idempotência). Colisões forjadas já foram vetor de ataque real (Hash DoS — Fase 2.2).
