# [0705] Design HashSet

> 🔗 [LeetCode 705](https://leetcode.com/problems/design-hashset/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArraysEHashing` `#HashTable` `#Design` `#Easy`

## 📜 O Problema

Projete um `HashSet` **sem usar nenhuma biblioteca pronta de hash table**. Implemente a classe `MyHashSet` com:
- `add(key)`: insere `key` no conjunto.
- `contains(key)`: retorna se `key` existe no conjunto.
- `remove(key)`: remove `key` do conjunto, se existir (senão, não faz nada).

**Exemplos:**
```
Input:
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output:
[null, null, null, true, false, null, true, null, false]

Explicação:
add(1) → set={1}; add(2) → set={1,2}; contains(1) → true; contains(3) → false;
add(2) → set continua {1,2} (já existia); contains(2) → true; remove(2) → set={1};
contains(2) → false
```

**Restrições (e o que elas denunciam):**
- `0 <= key <= 10^6` → o universo de chaves é grande o suficiente para inviabilizar um array direto ingênuo do tamanho do maior valor possível sem desperdiçar memória de forma didática — é o cenário certo para **hashing com buckets**, a técnica que este problema existe para ensinar
- "no máximo `10^4` chamadas" → confirma que O(1) médio por operação é alcançável e é o que se espera; O(n) por chamada (busca linear) ainda passaria no juiz por causa do limite baixo, mas não é a lição do problema
- "sem bibliotecas prontas de hash table" → a implementação de `HashMap`/`HashSet`/`unordered_set` da linguagem está proibida; é preciso construir a função de hash e o tratamento de colisão na mão

## 🧭 Como reconhecer o padrão

Embora o enunciado não mencione array nem dicionário, "implemente um conjunto do zero" é fundamentalmente um problema de **função de hash + tratamento de colisão** — o mesmo mecanismo por trás de todo `HashMap`/`HashSet` de biblioteca (ver [fundamentos](../../../fundamentos/01_arrays_e_hashing.md)). A ideia central: converter a chave numa posição de **bucket** com uma função de hash, e resolver colisões (chaves diferentes caindo no mesmo bucket) encadeando os valores dentro de cada bucket.

## 🐢 Solução 1 — Força bruta (lista com busca linear)

Guarda todas as chaves numa lista simples (`ArrayList`/`List`). `add` só insere se `contains` (busca linear) disser que a chave ainda não está lá; `remove` percorre a lista procurando a chave para tirá-la.

- Tempo: O(n) por chamada (`n` = quantidade de chaves já inseridas) · Espaço: O(n)
- **Por que não basta:** com até `10^4` chamadas, no pior caso (`10^4` chaves todas inseridas antes de uma busca) cada operação pode varrer toda a lista — funciona dentro do limite deste problema, mas não escala e ignora completamente a ideia de hashing que o problema pede para exercitar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de guardar as chaves soltas numa lista, distribui-as em um array fixo de **buckets** (por exemplo, 1000 buckets). Uma função de hash simples (`key % numeroDeBuckets`) decide em qual bucket cada chave cai. Como chaves diferentes podem cair no mesmo bucket (colisão), cada bucket guarda uma pequena lista encadeada das chaves que caíram nele — daí o nome **separate chaining**. Toda operação vira: calcular o bucket em O(1), depois buscar dentro daquele bucket (que, em média, tem só `n / numeroDeBuckets` elementos).

## 🎬 Exemplo passo a passo

Com `numeroDeBuckets = 1000`, sequência `add(1)`, `add(2)`, `contains(1)`, `contains(3)`, `add(2)`, `contains(2)`, `remove(2)`, `contains(2)`:

| Operação | bucket = key % 1000 | Ação no bucket | Resultado |
|---|---|---|---|
| `add(1)` | 1 | bucket[1] = [1] | — |
| `add(2)` | 2 | bucket[2] = [2] | — |
| `contains(1)` | 1 | busca em bucket[1]=[1], acha | `true` |
| `contains(3)` | 3 | bucket[3] está vazio | `false` |
| `add(2)` | 2 | 2 já está em bucket[2], não duplica | — |
| `contains(2)` | 2 | busca em bucket[2]=[2], acha | `true` |
| `remove(2)` | 2 | remove 2 de bucket[2] → bucket[2]=[] | — |
| `contains(2)` | 2 | bucket[2] está vazio | `false` |

Resultado final: `[null, null, null, true, false, null, true, null, false]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) médio por operação — o hash leva ao bucket em O(1); com boa distribuição, cada bucket tem poucos elementos (`n / numeroDeBuckets`), então a busca dentro dele é praticamente constante
- **Espaço:** O(n + b) — `n` chaves armazenadas mais `b` buckets alocados de antemão

## 💻 Implementações

### Java (referência completa e comentada)
```java
class MyHashSet {
    private static final int NUM_BUCKETS = 1000; // fixo: suficiente p/ boa distribuição c/ até 10^4 chaves
    private final List<Integer>[] buckets;

    @SuppressWarnings("unchecked")
    public MyHashSet() {
        buckets = new List[NUM_BUCKETS];
        for (int i = 0; i < NUM_BUCKETS; i++) {
            buckets[i] = new LinkedList<>(); // cada bucket resolve colisão por encadeamento
        }
    }

    private int hash(int key) {
        return key % NUM_BUCKETS; // função de hash simples: módulo já distribui bem chaves uniformes
    }

    public void add(int key) {
        List<Integer> bucket = buckets[hash(key)];
        if (!bucket.contains(key)) { // evita duplicata — add não deve inserir a mesma key duas vezes
            bucket.add(key);
        }
    }

    public void remove(int key) {
        buckets[hash(key)].remove(Integer.valueOf(key)); // Integer.valueOf: remove POR VALOR, não por índice
    }

    public boolean contains(int key) {
        return buckets[hash(key)].contains(key);
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

- **Java: `bucket.remove(key)` em vez de `bucket.remove(Integer.valueOf(key))`**: em uma `List<Integer>`, `remove(int)` remove **por índice**, não por valor — é preciso forçar o overload correto com `Integer.valueOf(key)` (ou `(Integer) key`).
- **Não checar duplicata em `add`**: se `add` inserir sem checar `contains` primeiro, a mesma chave pode aparecer duas vezes no bucket, o que não quebra `contains` mas desperdiça memória e pode confundir `remove` (que só tira uma ocorrência).
- **Escolher poucos buckets (ex.: 1)**: degenera para a força bruta — todo mundo cai no mesmo bucket e vira uma busca linear disfarçada. O número de buckets precisa ser proporcional à quantidade esperada de chaves.
- **Confundir com Design HashMap (LC 706)**: aqui só existe presença/ausência da chave; no 706 cada chave carrega um valor associado — a estrutura de bucket muda de "lista de chaves" para "lista de pares chave-valor".

## 🧪 Casos de teste para validar

| Caso | Sequência | Esperado | Por quê |
|---|---|---|---|
| Contains em conjunto vazio | `contains(1)` sem add antes | `false` | bucket correspondente nunca foi tocado, mas precisa existir vazio |
| Add duplicado | `add(1); add(1); contains(1)` | `true` (e só 1 cópia internamente) | garante que `add` não duplica |
| Remove de chave inexistente | `remove(5)` sem `add(5)` antes | nada acontece, sem erro | `remove` deve ser no-op silencioso |
| Chaves que colidem no mesmo bucket | `add(1); add(1001)` com 1000 buckets | ambas presentes, bucket[1] com 2 elementos | valida o encadeamento (chaining) da colisão |
| Chave no limite | `add(1000000); contains(1000000)` | `true` | testa o maior valor permitido pela restrição |

## 🔗 Conexões

- Problemas irmãos: **[0706] Design HashMap** (mesma estrutura de buckets, mas guardando pares chave-valor em vez de só chaves), **[0146] LRU Cache** (também combina hashing com outra estrutura — lista dupla — para O(1) por operação)
- No backend: é literalmente como um `HashMap`/`Dictionary` de qualquer linguagem funciona por baixo dos panos — array de buckets + função de hash + encadeamento (ou open addressing). Entender essa implementação explica por que hash maps degradam para O(n) sob ataque de **Hash DoS** (chaves maliciosas escolhidas para colidir todas no mesmo bucket) e por que **resize/rehash** é necessário quando o fator de carga cresce demais.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
