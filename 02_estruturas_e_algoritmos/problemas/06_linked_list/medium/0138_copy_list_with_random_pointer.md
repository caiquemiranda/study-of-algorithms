# [0138] Copy List with Random Pointer

> 🔗 [LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#HashTable` `#Medium`

## 📜 O Problema

Uma linked list de `n` nós tem, além de `next`, um ponteiro extra `random` que pode apontar para **qualquer** nó da lista (ou `null`). Construa uma **cópia profunda** dessa lista: `n` nós totalmente novos, com os mesmos valores, onde `next` e `random` da cópia apontam para nós **da própria cópia** — nenhum ponteiro da cópia pode apontar de volta para a lista original.

**Exemplos:**
```
Input:  head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: cópia idêntica em estrutura (mesmos valores e mesmos padrões de random)

Input:  head = [[1,1],[2,1]]
Output: [[1,1],[2,1]] (cópia: nó de valor 1 e nó de valor 2, ambos com random apontando para o nó de valor 2 da CÓPIA)
```

**Restrições (e o que elas denunciam):**
- `0 <= n <= 1000` → O(n) é o esperado
- `-10^4 <= Node.val <= 10^4` → sem risco de overflow
- "`random` pode apontar para qualquer nó, inclusive um que ainda não foi copiado" → é o problema central: ao copiar um nó, seu `random` pode apontar para um nó que **ainda não existe** na cópia (está mais à frente na lista) — não dá para simplesmente copiar `random` na hora, é preciso alguma forma de "lembrar" o mapeamento original→cópia

## 🧭 Como reconhecer o padrão

"Copie uma estrutura encadeada preservando referências cruzadas arbitrárias" é resolvido classicamente com um **mapa de tradução** (original → cópia) — uma extensão do padrão de hashing da categoria de arrays/hashing aplicada a ponteiros de nós em vez de valores. A variação mais elegante evita até esse mapa **entrelaçando** a cópia dentro da própria lista original, temporariamente.

## 🐢 Solução 1 — Força bruta (HashMap de tradução original → cópia)

Duas passadas. Na 1ª, cria um nó de cópia para cada nó original (só com o valor, sem `next`/`random` ainda) e guarda num `HashMap<Node, Node>` o mapeamento original→cópia. Na 2ª, para cada nó original, usa o mapa para religar `copia.next = mapa.get(original.next)` e `copia.random = mapa.get(original.random)` (o mapa resolve o problema de "o alvo ainda não existia" — agora todos já existem).

- Tempo: O(n) · Espaço: O(n) para o `HashMap`
- **Por que não basta:** o tempo já é ótimo, e essa solução é totalmente válida — mas gasta memória extra proporcional a `n` só para guardar o mapeamento. Existe uma forma de "codificar" esse mapeamento na própria estrutura da lista, sem `HashMap`, entrelaçando cada cópia logo depois do original correspondente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em três fases, sem `HashMap`:
1. **Entrelaça**: para cada nó original `A`, cria a cópia `A'` e a insere logo **depois** de `A` na própria lista: `A → A' → B → B' → ...`. Agora, "a cópia de qualquer nó X" é sempre `X.next`.
2. **Copia os `random`**: para cada original `A` com `A.random` apontando para algum nó `X`, a cópia `A'` deve ter `random` apontando para `X'` — e como `X' = X.next` (graças ao entrelaçamento), basta `A'.random = A.random.next`. Nenhuma busca é necessária.
3. **Desentrelaça**: separa as duas listas de volta — restaura `next` dos nós originais e monta a lista de cópias lendo os nós intercalados.

## 🎬 Exemplo passo a passo

`head = [[1,1],[2,1]]` (nó A: valor 1, random aponta para o nó de índice 1 = ele mesmo B; nó B: valor 2, random aponta para índice 1 = ele mesmo B)

**Fase 1 — entrelaçar:**

| Antes | Depois |
|---|---|
| `A → B → null` | `A → A' → B → B' → null` |

**Fase 2 — copiar random** (`copia.random = original.random.next`):

| Nó original | `original.random` | `original.random.next` (= cópia do alvo) | `cópia.random` resultante |
|---|---|---|---|
| A | B | `B.next = B'` | `A'.random = B'` |
| B | B (ele mesmo) | `B.next = B'` | `B'.random = B'` |

**Fase 3 — desentrelaçar:** restaura `A.next = B`, `B.next = null` (lista original intacta); extrai `A' → B' → null` (lista copiada).

Resultado final: cópia `A'(val=1, random=B') → B'(val=2, random=B')` ✔ — bate com `[[1,1],[2,1]]` do enunciado (ambos com random apontando para o nó de índice 1 **da cópia**).

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — três passadas lineares (entrelaçar, copiar random, desentrelaçar)
- **Espaço:** O(1) extra — nenhuma estrutura auxiliar além dos nós da própria cópia (que fazem parte da saída exigida, não contam como espaço "extra")

## 💻 Implementações

### Java (referência completa e comentada)
```java
public Node copyRandomList(Node head) {
    if (head == null) return null;

    // Fase 1: intercala uma cópia logo depois de cada nó original.
    // Depois disso, "a cópia de X" é sempre X.next.
    for (Node cur = head; cur != null; cur = cur.next.next) {
        Node copy = new Node(cur.val);
        copy.next = cur.next;
        cur.next = copy;
    }

    // Fase 2: copia random em O(1) por nó — cur.random.next é a cópia de cur.random,
    // garantida pelo entrelaçamento da fase 1 (não precisa de busca nem mapa).
    for (Node cur = head; cur != null; cur = cur.next.next) {
        if (cur.random != null) {
            cur.next.random = cur.random.next;
        }
    }

    // Fase 3: desentrelaça — restaura a lista original e extrai a lista copiada.
    Node dummy = new Node(0);
    Node copyTail = dummy;
    for (Node cur = head; cur != null; cur = cur.next) {
        Node copy = cur.next;
        cur.next = copy.next;    // restaura o next ORIGINAL (o próximo nó original)
        copyTail.next = copy;
        copyTail = copy;
    }

    return dummy.next;
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

- **Copiar `random` antes de terminar o entrelaçamento inteiro**: a fase 2 depende de que **toda** cópia já exista intercalada, senão `original.random.next` pode ainda não ser a cópia certa se o `random` apontar para um nó "à frente" que ainda não foi processado.
- **Esquecer de checar `cur.random != null`**: nem todo nó tem `random` apontando para algo — sem a checagem, `null.next` explode.
- **Não restaurar a lista original na fase 3**: o problema não exige preservar a lista original intacta no papel, mas misturar as duas listas sem desentrelaçar corretamente faz a cópia (ou o original) ficar corrompida, com `next` apontando para os nós errados.
- **Confundir a ordem das atualizações na fase 3**: `copy.next` precisa ser lido **antes** de `cur.next` ser sobrescrito com `copy.next` (o próximo original) — inverter a ordem perde a referência ao restante da lista intercalada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `null` | retorna cedo, sem nenhum nó para processar |
| Um nó, random aponta para si mesmo | `head = [[1,0]]` | cópia de 1 nó com `random` apontando para si mesma | testa auto-referência sem confundir original com cópia |
| Random sempre null | `head = [[1,null],[2,null]]` | cópia com `next` correto e `random = null` em todos | valida que a fase 2 não quebra quando não há nenhum `random` |
| Todos os random no mesmo alvo | `head = [[1,1],[2,1]]` | ambos com `random` apontando para o nó de valor 2 da cópia | trace acima |
| Lista maior com randoms cruzados | `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]` | cópia estruturalmente idêntica, sem nenhum ponteiro apontando para a lista original | exemplo maior do enunciado, valida o caso geral |

## 🔗 Conexões

- Problemas irmãos: **[0133] Clone Graph** (mesma ideia de "copiar profundamente uma estrutura com referências cruzadas", mas resolvida com DFS/BFS + mapa em vez de entrelaçamento, porque um grafo não tem uma ordem linear para entrelaçar), **[0146] LRU Cache** (também combina hashing com ponteiros de nós, mas para uma finalidade diferente)
- No backend: clonar uma estrutura com referências internas cruzadas — sem vazar ponteiros para o original — é o padrão usado em **deep copy de objetos com referências circulares** (serialização/desserialização de grafos de objetos, como em ORMs que precisam clonar entidades relacionadas) e em **snapshots de estruturas de dados versionadas**, onde uma cópia precisa ser totalmente independente do estado original para permitir modificações isoladas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
