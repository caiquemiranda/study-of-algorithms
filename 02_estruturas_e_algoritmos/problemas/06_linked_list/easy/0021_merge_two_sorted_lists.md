# [0021] Merge Two Sorted Lists

> 🔗 [LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Sentinela` `#Easy`

## 📜 O Problema

Você recebe as cabeças (`head`) de duas linked lists **ordenadas**, `list1` e `list2`. Junte as duas em uma única lista **ordenada**, reaproveitando os próprios nós (sem criar nós novos), e retorne a cabeça do resultado.

**Exemplos:**
```
Input:  list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input:  list1 = [], list2 = []
Output: []

Input:  list1 = [], list2 = [0]
Output: [0]
```

**Restrições (e o que elas denunciam):**
- Número de nós em cada lista em `[0, 50]` → entradas minúsculas, mas isso não abre espaço para O(n²): a solução esperada é O(n) porque o problema já é "ordenado + juntar", a assinatura clássica de intercalação (merge)
- `-100 <= Node.val <= 100` → valores cabem em qualquer tipo, sem risco de overflow
- "ambas ordenadas em ordem não decrescente" → garante que basta comparar as duas cabeças a cada passo; nunca é preciso olhar mais à frente

## 🧭 Como reconhecer o padrão

Duas listas **já ordenadas** para combinar em uma só é o caso de uso canônico do **nó sentinela (dummy)** — ver [fundamentos](../../../fundamentos/06_linked_list.md), seção "Merge com sentinela". Sempre que o enunciado pede para "juntar preservando ordem" a partir de fontes já ordenadas, pense em dois ponteiros andando em paralelo, um por lista.

## 🐢 Solução 1 — Força bruta (copiar valores, ordenar, reconstruir)

Percorre as duas listas, guarda todos os valores num array, ordena o array e constrói uma lista nova a partir dele.

- Tempo: O(n log n) · Espaço: O(n)
- **Por que não basta:** joga fora a informação de que as listas já chegam ordenadas — a ordenação é trabalho redundante. Além disso, o problema pede para reaproveitar os nós existentes ("splicing"), não criar uma lista do zero.

## 💡 Solução 2 — A ideia otimizada (intuição)

Como as duas listas já estão ordenadas, o menor elemento **geral** está sempre em uma das duas cabeças. Basta comparar `list1.val` com `list2.val`, "pescar" o menor dos dois para a lista resultado, e avançar só o ponteiro daquela lista.

O truque de organização é o **nó sentinela (dummy)**: em vez de tratar "qual é o primeiro nó do resultado?" como caso especial, cria-se um nó descartável antes do início. O resultado real começa em `dummy.next`.

## 🎬 Exemplo passo a passo

`list1 = [1,2,4]`, `list2 = [1,3,4]`

| Passo | list1 (restante) | list2 (restante) | Comparação | Nó escolhido | cur.next |
|---|---|---|---|---|---|
| 1 | 1,2,4 | 1,3,4 | 1 <= 1 | 1 (de list1) | 1 |
| 2 | 2,4 | 1,3,4 | 2 > 1 | 1 (de list2) | 1→1 |
| 3 | 2,4 | 3,4 | 2 <= 3 | 2 (de list1) | 1→1→2 |
| 4 | 4 | 3,4 | 4 > 3 | 3 (de list2) | 1→1→2→3 |
| 5 | 4 | 4 | 4 <= 4 | 4 (de list1) | 1→1→2→3→4 |
| 6 | — | 4 | list1 acabou | resto de list2 (4) | 1→1→2→3→4→4 |

Resultado final: `1 → 1 → 2 → 3 → 4 → 4` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(m + n) — cada nó das duas listas é visitado exatamente uma vez
- **Espaço:** O(1) — só reorganiza ponteiros existentes, nenhum nó novo é alocado (fora do sentinela, que é descartado)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode dummy = new ListNode(0);   // sentinela: elimina o caso especial "quem é o 1º nó?"
    ListNode cur = dummy;

    while (list1 != null && list2 != null) {
        if (list1.val <= list2.val) {   // <= (não <) mantém estabilidade: em empate, list1 vem primeiro
            cur.next = list1;
            list1 = list1.next;
        } else {
            cur.next = list2;
            list2 = list2.next;
        }
        cur = cur.next;
    }

    // Uma das listas terminou antes: o restante da outra já está ordenado,
    // então basta "emendar" o que sobrou de uma vez (sem percorrer nó a nó).
    cur.next = (list1 != null) ? list1 : list2;

    return dummy.next;                  // a resposta real começa depois do sentinela
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

- **Criar nós novos em vez de reaproveitar os existentes**: o enunciado pede "splicing together the nodes" — a solução correta apenas rearranja os ponteiros `next`, nunca faz `new ListNode(val)` para copiar valores.
- **Esquecer de emendar o restante da lista mais longa**: quando o loop principal termina, uma das listas ainda pode ter nós — se você não fizer `cur.next = list1 or list2`, esses nós somem do resultado.
- **Usar `<` em vez de `<=` na comparação**: não muda a corretude do valor final, mas muda a ordem relativa em caso de empate — importante se a estabilidade for exigida em variações do problema.
- **Não usar sentinela**: sem ele, é preciso decidir manualmente qual das duas cabeças vira a cabeça do resultado antes do loop, duplicando lógica.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ambas vazias | `list1=[], list2=[]` | `[]` | loop nem roda, `cur.next` fica `null` |
| Uma vazia | `list1=[], list2=[0]` | `[0]` | testa o "emendar o restante" sem passar pelo loop |
| Listas de tamanhos diferentes | `list1=[1,2,4], list2=[1,3,4]` | `[1,1,2,3,4,4]` | exemplo do enunciado, trace acima |
| Valores duplicados entre listas | `list1=[1,1], list2=[1,1]` | `[1,1,1,1]` | garante que `<=` não perde nenhum nó em empate |
| Uma lista totalmente menor que a outra | `list1=[1,2], list2=[3,4]` | `[1,2,3,4]` | o loop principal esgota list1 rápido; resto de list2 precisa ser emendado inteiro |

## 🔗 Conexões

- Problemas irmãos: **[0023] Merge k Sorted Lists** (generaliza este merge para N listas com heap), **[0088] Merge Sorted Array** (mesma ideia de intercalação, mas em array em vez de lista encadeada)
- No backend: intercalar fontes já ordenadas é o núcleo do **merge sort externo** (juntar arquivos grandes maiores que a memória) e do passo de **merge** em bancos de dados que combinam resultados já ordenados de índices diferentes (merge join).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
