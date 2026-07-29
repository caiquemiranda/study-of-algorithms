# [0237] Delete Node in a Linked List

> 🔗 [LeetCode 237](https://leetcode.com/problems/delete-node-in-a-linked-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Medium`

## 📜 O Problema

Existe uma linked list `head`, e você recebe apenas o `node` a ser deletado — **sem acesso à `head`**. Todos os valores da lista são únicos, e é garantido que `node` **não é o último nó**. "Deletar" significa: o valor de `node` não deve mais existir na lista, o tamanho diminui em 1, e a ordem de todos os outros nós é preservada.

**Exemplos:**
```
Input:  head = [4,5,1,9], node = 5
Output: [4,1,9]
Explicação: dado o 2º nó (valor 5), a lista vira 4 -> 1 -> 9.

Input:  head = [4,5,1,9], node = 1
Output: [4,5,9]
Explicação: dado o 3º nó (valor 1), a lista vira 4 -> 5 -> 9.
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[2, 1000]` → garante que sempre existe pelo menos mais um nó além de `node`, então a operação sempre tem como se realizar
- Valores **únicos** na lista → importante para o raciocínio, mas não é usado na técnica em si (só garante que o enunciado é bem definido)
- `node` **não é o último nó da lista** → essa é a restrição que **habilita** a solução: se `node` fosse o último, não haveria `node.next` para copiar, e a técnica não funcionaria
- **"você não tem acesso a `head`"** → esta é a restrição central do problema. Ela elimina de cara a forma "normal" de deletar um nó (achar o nó anterior a partir da cabeça e religar `prev.next = node.next`), porque não existe como percorrer a lista sem um ponto de partida

## 🧭 Como reconhecer o padrão

Sempre que um problema de linked list oferecer **só o próprio nó**, sem `head`, é sinal de que a solução não pode envolver travessia nenhuma — a única informação disponível é o que está alcançável **a partir de `node` para frente**. Isso força uma solução criativa: em vez de remover fisicamente `node` da lista (que exigiria o nó anterior), "disfarça-se" o nó seguinte como se fosse o próprio `node`.

## 🐢 Solução 1 — Força bruta (o jeito "normal" de deletar, que este problema proíbe)

Com acesso a `head`, o jeito padrão seria: percorrer a lista a partir de `head` até achar o nó **anterior** a `node`, e religar `prev.next = node.next` — a mesma ideia usada em [0203] Remove Linked List Elements.

- Tempo: O(n) para achar o nó anterior · Espaço: O(1)
- **Por que não basta:** aqui não é uma questão de eficiência — essa abordagem é **impossível** de executar, porque o enunciado explicitamente não fornece `head` nem qualquer forma de alcançar o nó anterior a `node`. A única informação disponível é `node` e tudo que vem depois dele.

## 💡 Solução 2 — A ideia otimizada (intuição)

Como não é possível remover `node` de verdade (não há como religar o ponteiro de quem aponta **para** ele), a solução é **copiar o conteúdo do próximo nó para dentro de `node`**, e então pular o próximo nó. Do ponto de vista de quem olha a lista a partir de `head`, o efeito é indistinguível de ter removido `node`: o valor de `node` "sumiu" (foi sobrescrito pelo valor seguinte), e o nó que sobra fisicamente desconectado é o que **era** o próximo — que ninguém mais referencia.

## 🎬 Exemplo passo a passo

`head = [4,5,1,9]`, `node` = o nó de valor `5` (2º nó da lista)

| Etapa | Ação | Estado de `node` | Lista vista a partir de `head` |
|---|---|---|---|
| início | — | valor `5`, aponta para o nó `1` | `4 → 5 → 1 → 9` |
| 1 | `node.val = node.next.val` (copia o valor `1` para dentro de `node`) | valor `1`, ainda aponta para o nó `1` (original) | `4 → 1 → 1 → 9` (temporariamente "duplicado") |
| 2 | `node.next = node.next.next` (pula o nó `1` original, que agora é redundante) | valor `1`, aponta para o nó `9` | `4 → 1 → 9` |

Resultado final (visto a partir de `head`, que continua sendo o mesmo objeto de sempre): `4 → 1 → 9` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) — só duas atribuições, nenhuma travessia
- **Espaço:** O(1) — nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public void deleteNode(ListNode node) {
    // Não é possível religar o ponteiro de quem aponta PARA node (não temos head).
    // Em vez disso, "transformamos" node no próximo nó, copiando seu valor e
    // pulando-o — o nó original seguinte fica órfão, mas ninguém mais o referencia.
    node.val = node.next.val;
    node.next = node.next.next;
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

- **Tentar percorrer a lista a partir de `node` para achar "o início"**: não existe ponteiro `prev` numa lista simples — a partir de `node` só se alcança o que vem **depois**, nunca o que vem antes.
- **Esquecer que a restrição "`node` não é o último nó" é o que garante que `node.next` sempre existe**: sem essa garantia, `node.next.val` explodiria com `NullPointerException` — é por isso que este truque não funciona para deletar o último nó da lista (nesse caso, seria necessário ter acesso ao penúltimo nó, o que exigiria percorrer a partir de `head`).
- **Achar que o nó "removido de verdade" é `node`**: fisicamente, o nó que fica desconectado é o que **era** `node.next` — `node` em si continua existindo no mesmo endereço de memória, só que agora carrega o valor (e o `next`) que antes pertenciam ao seu vizinho.
- **Aplicar esta técnica quando `head` estiver disponível e for mais natural resolver do jeito padrão**: este truque é a resposta certa **especificamente** para a restrição "sem acesso a `head`" — em qualquer outro contexto (como no LC 203), a solução padrão com sentinela é mais clara e mais geral.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Deletar o 2º nó, exemplo do enunciado | `head=[4,5,1,9], node=5` | `[4,1,9]` | trace acima |
| Deletar o 3º nó, exemplo do enunciado | `head=[4,5,1,9], node=1` | `[4,5,9]` | valida a técnica numa posição diferente |
| Lista de 2 nós, deletar o primeiro | `head=[1,2], node=1` (nó de valor 1) | `[2]` | menor caso possível; `node` vira uma cópia do único nó restante |
| Valores negativos | `head=[-3,-1,0], node` = nó de valor `-1` | `[-3,0]` | garante que a cópia de valor funciona independente do sinal |
| Nó a deletar é o penúltimo | `head=[1,2,3,4], node` = nó de valor `3` | `[1,2,4]` | valida que `node.next.next` (o novo próximo) pode ser o último nó da lista, sem problema |

## 🔗 Conexões

- Problemas irmãos: **[0203] Remove Linked List Elements** (a remoção "normal", com acesso a `head` e sentinela), **[0083] Remove Duplicates from Sorted List** (também remove nós religando ponteiros, mas com acesso completo à lista)
- No backend: "disfarçar" um objeto como se fosse outro, copiando dados e descartando a referência original, é o mesmo truque usado em certas implementações de **remoção O(1) de um elemento de um array não ordenado** (copiar o último elemento para a posição a remover e encolher o array) e em estruturas onde a **identidade do nó** (endereço/handle) precisa ser preservada mesmo quando seu conteúdo lógico muda — como em alguns esquemas de atualização in-place de registros referenciados por múltiplos ponteiros.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
