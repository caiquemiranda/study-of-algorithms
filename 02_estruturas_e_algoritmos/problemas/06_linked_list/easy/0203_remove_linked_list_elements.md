# [0203] Remove Linked List Elements

> 🔗 [LeetCode 203](https://leetcode.com/problems/remove-linked-list-elements/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Sentinela` `#Easy`

## 📜 O Problema

Dado o `head` de uma linked list e um inteiro `val`, remova todos os nós cujo `Node.val == val` e retorne a nova cabeça.

**Exemplos:**
```
Input:  head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input:  head = [], val = 1
Output: []

Input:  head = [7,7,7,7], val = 7
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → O(n) é o esperado, uma única passada resolve
- `1 <= Node.val <= 50` e `0 <= val <= 50` → valores pequenos, sem risco de overflow; nada aqui exige truque numérico
- O terceiro exemplo (`[7,7,7,7]` → `[]`) denuncia o caso mais traiçoeiro: **a própria cabeça pode precisar ser removida**, inclusive repetidamente — é por isso que este problema é o exemplo clássico de quando usar um **nó sentinela**

## 🧭 Como reconhecer o padrão

"Remova nós que satisfazem uma condição" em qualquer posição da lista — incluindo a cabeça — é o caso de uso central do **nó sentinela (dummy)**: ver [fundamentos](../../../fundamentos/06_linked_list.md). Sem o sentinela, remover a cabeça vira um `if` especial separado do resto do loop; com ele, remover a cabeça é só mais uma remoção igual às outras.

## 🐢 Solução 1 — Força bruta (copiar os nós que sobrevivem)

Percorre a lista, copia os valores que **não** são iguais a `val` para uma lista nova, nó por nó.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** o tempo já é ótimo, mas alocar nós novos é desperdício — o problema pede para reorganizar a lista existente (religar ponteiros), não construir outra do zero.

## 💡 Solução 2 — A ideia otimizada (intuição)

Cria-se um nó sentinela (`dummy`) apontando para `head`, para que a cabeça real também possa ser removida sem tratamento especial. Um ponteiro `prev` começa no sentinela e um ponteiro `cur` começa em `head`. Para cada nó: se `cur.val == val`, "pula" ele religando `prev.next = cur.next` (e `prev` **não** avança, porque o próximo nó também pode ser igual a `val`); senão, avança os dois ponteiros juntos.

## 🎬 Exemplo passo a passo

`head = [1,2,6,3,4,5,6]`, `val = 6`

| Passo | prev | cur | cur.val == 6? | Ação |
|---|---|---|---|---|
| início | dummy | 1 | não | avança os dois |
| 1 | 1 | 2 | não | avança os dois |
| 2 | 2 | 6 | **sim** | `prev.next = cur.next` (pula o 6); prev fica em 2 |
| 3 | 2 | 3 | não | avança os dois |
| 4 | 3 | 4 | não | avança os dois |
| 5 | 4 | 5 | não | avança os dois |
| 6 | 5 | 6 | **sim** | `prev.next = cur.next` (pula o último 6); prev fica em 5 |
| 7 | 5 | null | — | loop termina |

Resultado final: `1 → 2 → 3 → 4 → 5` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela lista
- **Espaço:** O(1) — só o sentinela e dois ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode removeElements(ListNode head, int val) {
    ListNode dummy = new ListNode(0, head); // sentinela: cobre o caso "a própria head é removida"
    ListNode prev = dummy, cur = head;

    while (cur != null) {
        if (cur.val == val) {
            prev.next = cur.next; // pula o nó; prev NÃO avança — o próximo pode ser val de novo
        } else {
            prev = cur;            // só avança prev quando o nó atual sobrevive
        }
        cur = cur.next;
    }

    return dummy.next; // a nova cabeça pode não ser a antiga head
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

- **Avançar `prev` mesmo ao remover um nó**: se `prev = prev.next` acontecer no ramo de remoção, uma sequência de repetidos (ex.: `[7,7,7,7]`) deixa cópias passarem despercebidas, porque `prev` acaba apontando para um nó que também será removido.
- **Não usar sentinela e tratar a cabeça como caso especial**: funciona, mas exige um `while (head != null && head.val == val) head = head.next;` antes do loop principal — o sentinela elimina essa duplicação de lógica.
- **Retornar `head` em vez de `dummy.next`**: se a cabeça original for removida, `head` continua apontando para o nó antigo (já desconectado) — a resposta certa está em `dummy.next`.
- **Esquecer que a lista pode ficar totalmente vazia**: se todos os nós forem iguais a `val` (`[7,7,7,7]`), o resultado correto é `[]`, e o código deve chegar lá naturalmente sem tratamento extra.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head=[], val=1` | `[]` | `cur` já é `null`, loop nem roda |
| Todos os nós removidos | `head=[7,7,7,7], val=7` | `[]` | testa remoção repetida sem avançar `prev` |
| Cabeça removida, resto sobrevive | `head=[6,1,2], val=6` | `[1,2]` | valida que o sentinela cobre a remoção da própria head |
| Nenhum nó removido | `head=[1,2,3], val=9` | `[1,2,3]` | garante que a lista não é alterada quando `val` não aparece |
| Valor no meio, exemplo do enunciado | `head=[1,2,6,3,4,5,6], val=6` | `[1,2,3,4,5]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0083] Remove Duplicates from Sorted List** (também remove nós de uma lista, mas a condição é "duplicata do vizinho" em vez de "valor específico"), **[0021] Merge Two Sorted Lists** (mesmo uso do padrão nó sentinela para simplificar o caso da cabeça)
- No backend: filtrar registros de uma lista encadeada por uma condição — sem realocar tudo — é o padrão de **invalidação seletiva de cache** (remover apenas as entradas expiradas de uma lista de itens em memória) ou de **filas de eventos** onde eventos cancelados precisam ser removidos sem reconstruir a fila inteira.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
