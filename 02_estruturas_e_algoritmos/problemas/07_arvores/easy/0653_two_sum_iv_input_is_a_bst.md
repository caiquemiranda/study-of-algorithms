# [0653] Two Sum IV - Input is a BST

> 🔗 [LeetCode 653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#HashSet`

## 📜 O Problema

Dado o `root` de uma BST e um inteiro `k`, retorne `true` se existirem **dois nós diferentes** cuja soma dos valores seja igual a `k`.

**Exemplos:**
```
Input:  root = [5,3,6,2,4,null,7], k = 9
Output: true

Input:  root = [5,3,6,2,4,null,7], k = 28
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^4]` → precisa de solução O(n), não O(n²)
- `-10^4 <= Node.val <= 10^4` e `-10^5 <= k <= 10^5` → valores cabem em `int` sem overflow
- "árvore garantida como BST válida" → a propriedade de ordenação existe, mas **não é obrigatória** para resolver este problema com a técnica mais direta (diferente de [0530]/[0501], aqui o hashset funciona igualmente bem numa árvore binária qualquer)

## 🧭 Como reconhecer o padrão

"Existem dois elementos cuja soma é X?" é o clássico Two Sum ([0001]), só que os elementos estão espalhados numa árvore em vez de um array. A técnica de hashset do Two Sum original se aplica igual: visitar os nós numa única passada, e para cada um, perguntar "o complemento (`k - valor`) já apareceu antes?".

## 🐢 Solução 1 — Força bruta (todos os pares de nós)

Coletar todos os valores da árvore numa lista (qualquer travessia serve) e depois testar **todo par** `(i, j)` com `i != j` para ver se `lista[i] + lista[j] == k`.

- Tempo: O(n²) · Espaço: O(n) para a lista
- **Por que não basta:** testar todo par cresce quadraticamente; com `n = 10^4`, isso são até 10^8 comparações — arriscado dentro do limite de tempo, e desnecessário porque, assim como no Two Sum de array, um hashset resolve em uma única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra a árvore (qualquer travessia serve, não precisa ser em-ordem) mantendo um `HashSet` dos valores já vistos. Em cada nó, verifique se `k - no.val` já está no set — se estiver, achou o par, retorna `true` na hora. Senão, adiciona `no.val` ao set e continua. Não é preciso ordenar nem usar a propriedade de BST, só "lembrar o que já vi".

## 🎬 Exemplo passo a passo

`root = [5,3,6,2,4,null,7]`, `k = 9` (usando pré-ordem: 5, 3, 2, 4, 6, 7)

```
      5
     / \
    3   6
   / \    \
  2   4    7
```

| Passo | Nó visitado | `k - no.val` | Está no set? | Ação | Set após |
|---|---|---|---|---|---|
| 1 | 5 | 4 | não (set vazio) | adiciona 5 | `{5}` |
| 2 | 3 | 6 | não | adiciona 3 | `{5,3}` |
| 3 | 2 | 7 | não | adiciona 2 | `{5,3,2}` |
| 4 | 4 | 5 | **sim** (5 já está no set) | retorna `true` | — |

Resultado final: `true` ✔ (4 + 5 = 9, bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado no máximo uma vez, com short-circuit assim que o par é encontrado
- **Espaço:** O(n) — pior caso, o set guarda quase todos os valores antes de achar (ou não achar) o par

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean findTarget(TreeNode root, int k) {
    return dfs(root, k, new HashSet<>());
}

private boolean dfs(TreeNode no, int k, Set<Integer> vistos) {
    if (no == null) return false;

    // já vimos o complemento antes? então esse par soma k
    if (vistos.contains(k - no.val)) return true;

    vistos.add(no.val);

    // short-circuit: se achou num lado, nem avalia o outro
    return dfs(no.left, k, vistos) || dfs(no.right, k, vistos);
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

- Testar `vistos.contains(no.val)` em vez de `vistos.contains(k - no.val)` — o que precisa estar no set é o **complemento**, não o próprio valor do nó atual.
- Contar o mesmo nó duas vezes quando `k` é o dobro do valor de um nó único na árvore (ex.: `k = 8` e existe só um nó de valor `4`) — o algoritmo já evita isso corretamente, porque o nó só é adicionado ao set **depois** de checar o complemento contra ele mesmo (então um nó nunca se soma com ele próprio antes de outro nó de mesmo valor existir).
- Ignorar a propriedade de BST achando que ela não ajuda em nada — ela não é necessária para o hashset, mas existe uma alternativa igualmente válida usando dois "iteradores" em-ordem (um crescente, um decrescente) avançando um em direção ao outro, no espírito de two-pointers, que só funciona **porque** é uma BST.
- Comparar todos os pares (a força bruta) numa árvore de 10^4 nós — funciona, mas é a diferença entre O(n) e O(n²) que a restrição está testando.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1], k = 2` | `false` | não existem dois nós diferentes para somar |
| Par existente perto da raiz | `root = [5,3,6,2,4,null,7], k = 9` | `true` | cobre o exemplo 1 do enunciado |
| Soma maior que qualquer par possível | `root = [5,3,6,2,4,null,7], k = 28` | `false` | cobre o exemplo 2, soma maior que a máxima possível na árvore |
| k igual ao dobro de um valor único | `root = [3,1,5], k = 6` | `false` | garante que um nó não se soma com ele mesmo (só existe um `3` na árvore) |

## 🔗 Conexões

- Problemas irmãos: [0001] Two Sum (o problema original em array, mesma técnica de hashset), [0530] Minimum Absolute Difference in BST (também é BST, mas a técnica ótima aqui é diferente — em-ordem com comparação sequencial, não hashset)
- No backend: buscar pares complementares com hashset aparece em detecção de transações que se cancelam mutuamente (ex.: um débito e um crédito de mesmo valor absoluto numa árvore de transações), e em verificação de integridade de dados onde pares de registros precisam somar um total esperado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
