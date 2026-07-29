# [0146] LRU Cache

> 🔗 [LeetCode 146](https://leetcode.com/problems/lru-cache/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#HashTable` `#Design` `#Medium`

## 📜 O Problema

Projete um cache **LRU (Least Recently Used)** com capacidade fixa. Implemente `LRUCache`:
- `LRUCache(capacity)`: inicializa o cache com a capacidade dada.
- `get(key)`: retorna o valor de `key` se existir, senão `-1`. Contar como "uso recente".
- `put(key, value)`: insere ou atualiza `(key, value)`. Se isso ultrapassar a capacidade, **remove** a chave usada há mais tempo (least recently used).

Ambas as operações precisam rodar em **O(1) tempo médio**.

**Exemplos:**
```
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explicação:
cache(capacidade 2); put(1,1); put(2,2); get(1)→1 (1 vira o mais recente);
put(3,3) → excede a capacidade, remove a chave 2 (a menos recente); get(2)→-1;
put(4,4) → remove a chave 1 (agora a menos recente); get(1)→-1; get(3)→3; get(4)→4
```

**Restrições (e o que elas denunciam):**
- `1 <= capacity <= 3000`, até `2 * 10^5` chamadas → o requisito de **O(1) tempo médio** é levado a sério: com esse volume de chamadas, qualquer solução O(n) por operação (varrer tudo para achar a chave ou o item mais antigo) estoura o tempo
- `0 <= key <= 10^4`, `0 <= value <= 10^5` → sem risco de overflow
- "O(1) tempo médio para `get` **e** `put`" → é a restrição que decide a estrutura: é preciso acesso O(1) por chave (hashing) **e** capacidade de mover/remover um item em O(1) mantendo uma ordem de "recência" — só um array ou só um hash map, isoladamente, não entregam as duas coisas ao mesmo tempo

## 🧭 Como reconhecer o padrão

"Acesso O(1) por chave, combinado com uma ordem que muda a cada uso" é a assinatura exata de **hash map + lista duplamente encadeada** — ver [fundamentos](../../../fundamentos/06_linked_list.md), seção "Como Reconhecer": *"se combina lista + acesso O(1) por chave (LRU) → lista dupla + hash map"*. O hash map resolve "achar o nó da chave em O(1)"; a lista dupla resolve "mover esse nó para o início (mais recente) ou removê-lo do fim (mais antigo) em O(1)", algo que um array não consegue sem deslocar elementos.

## 🐢 Solução 1 — Força bruta (lista simples, busca e remoção lineares)

Guarda os pares `(key, value)` numa lista simples, na ordem de uso (mais recente por último, por exemplo). `get` percorre a lista procurando a chave — O(n) — e, se achar, move o item para o fim (também O(n), por causa do deslocamento). `put` funciona de forma parecida, e ao exceder a capacidade remove o item do início (o mais antigo).

- Tempo: O(n) por chamada · Espaço: O(capacity)
- **Por que não basta:** viola diretamente o requisito "O(1) tempo médio" — com até `2 × 10^5` chamadas, uma solução O(n) por chamada pode custar até `capacity × 2×10^5` operações no total, o que não passa dentro do limite de tempo esperado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Combina duas estruturas:
1. Um **HashMap<chave, nó>**, para achar o nó de qualquer chave em O(1), sem percorrer nada.
2. Uma **lista duplamente encadeada com sentinelas** (`head` e `tail` fictícios), onde a ordem física da lista **é** a ordem de uso: o nó logo depois de `head` é o mais recentemente usado (MRU), e o nó logo antes de `tail` é o menos recentemente usado (LRU).

Toda operação de acesso (`get` num item existente, ou `put` que atualiza/insere) **remove o nó de onde ele está e o reinsere logo após `head`** — ambas operações O(1) numa lista dupla, porque cada nó já sabe seus vizinhos (`prev`/`next`), sem precisar percorrer nada. Quando `put` excede a capacidade, o nó a remover é sempre o que está logo antes de `tail` — o LRU, encontrado em O(1).

## 🎬 Exemplo passo a passo

`capacity = 2`, sequência do enunciado. Notação da lista: `[MRU ... LRU]` (mais recente à esquerda).

| Operação | Ação na lista dupla | Lista após a operação | Retorno |
|---|---|---|---|
| `put(1,1)` | insere `1` no início | `[1]` | — |
| `put(2,2)` | insere `2` no início | `[2,1]` | — |
| `get(1)` | acha `1` no mapa, move para o início | `[1,2]` | `1` |
| `put(3,3)` | insere `3`; excede capacidade (3 itens) → remove o LRU (`2`) | `[3,1]` | — |
| `get(2)` | `2` não está no mapa | `[3,1]` (inalterada) | `-1` |
| `put(4,4)` | insere `4`; excede capacidade → remove o LRU (`1`) | `[4,3]` | — |
| `get(1)` | `1` não está no mapa | `[4,3]` | `-1` |
| `get(3)` | acha `3`, move para o início | `[3,4]` | `3` |
| `get(4)` | acha `4`, move para o início | `[4,3]` | `4` |

Resultado final: `[null, null, null, 1, null, -1, null, -1, 3, 4]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) por chamada — HashMap dá acesso O(1) ao nó; remover/reinserir num ponto conhecido de uma lista dupla é O(1), sem percorrer nada
- **Espaço:** O(capacity) — o mapa e a lista nunca crescem além da capacidade fixa

## 💻 Implementações

### Java (referência completa e comentada)
```java
class LRUCache {
    private class Node {
        int key, val;
        Node prev, next;
        Node(int key, int val) { this.key = key; this.val = val; }
    }

    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0); // sentinelas: eliminam casos especiais

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void insertAtFront(Node node) { // logo após head = a posição "mais recentemente usado"
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }

    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        Node node = map.get(key);
        remove(node);
        insertAtFront(node); // ler também conta como uso: promove para MRU
        return node.val;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            remove(map.get(key)); // já existe: tira do lugar antigo antes de reinserir atualizado
        }
        Node node = new Node(key, value);
        map.put(key, node);
        insertAtFront(node);

        if (map.size() > capacity) {
            Node lru = tail.prev; // nó logo antes do sentinela de cauda = o menos recentemente usado
            remove(lru);
            map.remove(lru.key);
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

- **Esquecer que `get` também conta como uso**: se `get` só ler o valor sem mover o nó para o início, a ordem de recência fica errada e o item evictado no próximo `put` pode não ser realmente o menos usado.
- **Não usar sentinelas (`head`/`tail` fictícios)**: sem eles, inserir/remover o primeiro ou último nó real exige checagens especiais (`if (list vazia)`, `if (é o único nó)`) espalhadas pelo código.
- **Em `put` de uma chave que já existe, esquecer de remover o nó antigo antes de reinserir**: sem isso, a mesma chave pode acabar com **dois nós** na lista dupla (um desatualizado), corrompendo a estrutura.
- **Usar `LinkedHashMap` (Java) achando que "é a mesma coisa"**: resolve na prática, mas não ensina a técnica por trás — o exercício deste problema é justamente entender como um LRU real é implementado por baixo dos panos.
- **Esquecer de remover do `HashMap` ao evictar**: remover só da lista dupla sem remover do mapa faz o mapa achar que a chave ainda existe, retornando um nó fantasma desconectado da lista.

## 🧪 Casos de teste para validar

| Caso | Sequência | Esperado | Por quê |
|---|---|---|---|
| Get em cache vazio | `get(1)` sem put antes | `-1` | mapa vazio, retorna cedo |
| Capacidade 1 | `capacity=1; put(1,1); put(2,2); get(1)` | `-1` | `put(2,2)` já evictou a chave 1 imediatamente |
| Put atualiza valor existente | `put(1,1); put(1,10); get(1)` | `10` | atualização não deve duplicar o nó nem mudar a chave |
| Get promove para MRU | `capacity=2; put(1,1); put(2,2); get(1); put(3,3); get(2)` | `-1` | `get(1)` promoveu 1 para MRU, então 2 (não 1) é evictado por `put(3,3)` |
| Exemplo do enunciado | sequência completa acima | `[null,null,null,1,null,-1,null,-1,3,4]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0138] Copy List with Random Pointer** (também combina hashing com manipulação de ponteiros de nós), **[0460] LFU Cache** (evolução do mesmo problema, trocando "menos recente" por "menos frequente" — exige uma estrutura ainda mais elaborada)
- No backend: LRU é **a** política de cache mais usada na prática — é literalmente como funcionam o `LinkedHashMap` do Java (com `accessOrder=true`), a biblioteca Caffeine, e a política de eviction padrão do Redis (`allkeys-lru`). Qualquer sistema que precisa manter "os N itens mais usados recentemente" em memória limitada — cache de queries de banco, cache de sessões HTTP, cache de páginas de um SO — usa essa mesma combinação de hash map + lista dupla.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
