# [0706] Design HashMap

> 🔗 [LeetCode 706](https://leetcode.com/problems/design-hashmap/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArraysEHashing` `#HashTable` `#Design` `#Easy`

## 📜 O Problema

Projete um `HashMap` **sem usar nenhuma biblioteca pronta de hash table**. Implemente a classe `MyHashMap` com:
- `MyHashMap()`: inicializa o mapa vazio.
- `put(key, value)`: insere o par `(key, value)`. Se `key` já existir, atualiza o `value`.
- `get(key)`: retorna o `value` associado a `key`, ou `-1` se não existir.
- `remove(key)`: remove o mapeamento de `key`, se existir.

**Exemplos:**
```
Input:
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output:
[null, null, null, 1, -1, null, 1, null, -1]

Explicação:
put(1,1) → {1:1}; put(2,2) → {1:1, 2:2}; get(1) → 1; get(3) → -1 (não existe);
put(2,1) → atualiza {1:1, 2:1}; get(2) → 1; remove(2) → {1:1}; get(2) → -1
```

**Restrições (e o que elas denunciam):**
- `0 <= key, value <= 10^6` → universo de chaves grande, o mesmo cenário do LC 705 que justifica hashing com buckets em vez de um array direto do tamanho do maior valor
- "no máximo `10^4` chamadas" a `put`, `get` e `remove` → confirma que O(1) médio é alcançável e esperado
- "sem bibliotecas prontas" → proíbe usar `HashMap`/`dict`/`unordered_map` nativos; é preciso construir a função de hash e o tratamento de colisão manualmente

## 🧭 Como reconhecer o padrão

Igual ao LC 705 (Design HashSet), mas cada posição agora guarda um **par** `(key, value)` em vez de só a chave — a diferença central é que `put` precisa **atualizar** o valor se a chave já existir, em vez de só evitar duplicata. A técnica continua sendo **função de hash + buckets com encadeamento** (ver [fundamentos](../../../fundamentos/01_arrays_e_hashing.md)).

## 🐢 Solução 1 — Força bruta (lista de pares com busca linear)

Guarda todos os pares `(key, value)` numa lista simples. `put` percorre a lista procurando a chave: se achar, atualiza o valor; senão, adiciona um par novo. `get` e `remove` também percorrem a lista inteira procurando a chave.

- Tempo: O(n) por chamada · Espaço: O(n)
- **Por que não basta:** com até `10^4` chamadas passa dentro do limite de tempo do juiz, mas no pior caso cada operação varre todos os pares já inseridos — ignora a ideia de hashing que o problema existe para ensinar e não escalaria para um mapa de produção.

## 💡 Solução 2 — A ideia otimizada (intuição)

A mesma estrutura de buckets do Design HashSet, mas cada bucket guarda uma lista de **pares** `(key, value)` em vez de só chaves. `hash(key)` leva ao bucket certo em O(1); dentro do bucket, procura-se o par pela chave:
- `put`: se achar um par com a mesma `key`, **atualiza** o valor; senão, adiciona um par novo no bucket.
- `get`: procura o par pela chave no bucket; achou, retorna o valor — senão, retorna `-1`.
- `remove`: procura e remove o par pela chave no bucket.

## 🎬 Exemplo passo a passo

Com `numeroDeBuckets = 1000`, sequência `put(1,1)`, `put(2,2)`, `get(1)`, `get(3)`, `put(2,1)`, `get(2)`, `remove(2)`, `get(2)`:

| Operação | bucket = key % 1000 | Ação no bucket | Resultado |
|---|---|---|---|
| `put(1,1)` | 1 | bucket[1] = [(1,1)] | — |
| `put(2,2)` | 2 | bucket[2] = [(2,2)] | — |
| `get(1)` | 1 | acha par (1,1) em bucket[1] | `1` |
| `get(3)` | 3 | bucket[3] vazio | `-1` |
| `put(2,1)` | 2 | acha (2,2), **atualiza** para (2,1) | — |
| `get(2)` | 2 | acha par (2,1) em bucket[2] | `1` |
| `remove(2)` | 2 | remove (2,1) de bucket[2] → bucket[2]=[] | — |
| `get(2)` | 2 | bucket[2] vazio | `-1` |

Resultado final: `[null, null, null, 1, -1, null, 1, null, -1]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) médio por operação — hash leva ao bucket em O(1); com boa distribuição, buscar/atualizar dentro do bucket é praticamente constante
- **Espaço:** O(n + b) — `n` pares armazenados mais `b` buckets alocados de antemão

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MyHashMap {
    private static final int NUM_BUCKETS = 1000; // fixo: suficiente p/ boa distribuição c/ até 10^4 chaves
    private final List<int[]>[] buckets; // cada elemento do bucket é um par {key, value}

    @SuppressWarnings("unchecked")
    public MyHashMap() {
        buckets = new List[NUM_BUCKETS];
        for (int i = 0; i < NUM_BUCKETS; i++) {
            buckets[i] = new LinkedList<>();
        }
    }

    private int hash(int key) {
        return key % NUM_BUCKETS;
    }

    public void put(int key, int value) {
        List<int[]> bucket = buckets[hash(key)];
        for (int[] par : bucket) {
            if (par[0] == key) {
                par[1] = value; // key já existe: ATUALIZA o valor, não duplica o par
                return;
            }
        }
        bucket.add(new int[]{key, value}); // key nova: adiciona o par
    }

    public int get(int key) {
        for (int[] par : buckets[hash(key)]) {
            if (par[0] == key) return par[1];
        }
        return -1; // key não encontrada: contrato do problema exige -1, não exceção
    }

    public void remove(int key) {
        List<int[]> bucket = buckets[hash(key)];
        // Iterator explícito: remover durante um for-each direto lança ConcurrentModificationException.
        Iterator<int[]> it = bucket.iterator();
        while (it.hasNext()) {
            if (it.next()[0] == key) {
                it.remove();
                return;
            }
        }
    }
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

- **Java: remover de uma `List` enquanto itera com for-each direto**: lança `ConcurrentModificationException`; é preciso usar `Iterator.remove()` explicitamente (como no código acima) ou reconstruir a lista.
- **`put` inserir um par novo sem checar se a chave já existe**: quebra o contrato "se a key já existir, atualiza o value" — a chave apareceria duplicada no bucket, e `get` sempre retornaria o primeiro par encontrado (potencialmente o valor antigo).
- **Confundir "chave não encontrada" com "valor 0"**: como `0 <= value <= 10^6`, um valor legítimo pode ser `0` — o retorno de "não encontrado" precisa ser um sentinel fora do domínio válido (`-1`), nunca `0`.
- **Esquecer que `get` deve retornar `-1`, não lançar exceção ou retornar `null`**: o contrato do problema é explícito sobre esse valor de retorno.

## 🧪 Casos de teste para validar

| Caso | Sequência | Esperado | Por quê |
|---|---|---|---|
| Get em mapa vazio | `get(1)` sem put antes | `-1` | bucket correspondente nunca foi tocado |
| Put atualiza valor existente | `put(1,10); put(1,20); get(1)` | `20` | garante que a 2ª chamada atualiza, não duplica |
| Remove de chave inexistente | `remove(5)` sem `put(5,_)` antes | nada acontece, sem erro | `remove` deve ser no-op silencioso |
| Valor igual a zero | `put(1,0); get(1)` | `0` | garante que `0` não é confundido com "não encontrado" |
| Chaves que colidem no mesmo bucket | `put(1,1); put(1001,2)` com 1000 buckets | `get(1)==1` e `get(1001)==2` | valida que o encadeamento distingue pares no mesmo bucket |

## 🔗 Conexões

- Problemas irmãos: **[0705] Design HashSet** (mesma estrutura, sem valor associado), **[0146] LRU Cache** (combina esta mesma ideia de hashing com uma lista dupla para políticas de expiração em O(1))
- No backend: é a implementação real de qualquer `HashMap`/`Dictionary`/`dict` de linguagem — buckets + hash + colisão por encadeamento (ou open addressing nas implementações mais avançadas). O mesmo mecanismo explica o **fator de carga** (quando resize/rehash acontece) e por que hash maps com má distribuição de chaves degradam para O(n).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
