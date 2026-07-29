# [0141] Linked List Cycle

> 🔗 [LeetCode 141](https://leetcode.com/problems/linked-list-cycle/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#FastSlow` `#Easy`

## 📜 O Problema

Dado `head`, a cabeça de uma linked list, determine se ela tem um **ciclo**: existe um nó que, seguindo repetidamente o ponteiro `next`, é alcançado de novo. A posição `pos` do nó onde a cauda se conecta não é passada como parâmetro — é só para descrever o exemplo. Retorne `true` se há ciclo, `false` caso contrário.

**Exemplos:**
```
Input:  head = [3,2,0,-4], pos = 1
Output: true
Explicação: a cauda (-4) aponta de volta para o nó de índice 1 (valor 2).

Input:  head = [1,2], pos = 0
Output: true
Explicação: o ciclo começa logo na cabeça.

Input:  head = [1], pos = -1
Output: false
Explicação: sem ciclo.
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → O(n) é tranquilo; a questão real é **espaço**, não tempo
- `-10^5 <= Node.val <= 10^5` → valores podem se repetir, então comparar `val` para saber "já vi este nó" não é seguro — é preciso comparar **identidade de nó** (referência)
- Follow-up "resolva com O(1) de memória" → empurra explicitamente para o algoritmo de Floyd (fast & slow) em vez de um `HashSet` de nós visitados

## 🧭 Como reconhecer o padrão

"Existe ciclo?" é a assinatura mais direta de **fast & slow (Floyd)** — ver [fundamentos](../../../fundamentos/06_linked_list.md), seção "Fast & Slow". Este é o problema mais simples da família: só pergunta `true`/`false`, sem precisar localizar onde o ciclo começa (isso é o irmão mais difícil, LC 142).

## 🐢 Solução 1 — Força bruta (hash set de nós visitados)

Percorre a lista guardando cada nó visitado num `HashSet` (por referência, não por valor). Se algum nó já estiver no set, há ciclo. Se chegar em `null`, não há.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** resolve corretamente, mas gasta memória proporcional ao tamanho da lista — desperdiça a estrutura mais barata disponível quando o follow-up pede explicitamente O(1) de espaço.

## 💡 Solução 2 — A ideia otimizada (intuição)

Dois ponteiros partem de `head`: `slow` anda 1 passo por vez, `fast` anda 2. Se não há ciclo, `fast` chega em `null` primeiro (como numa corrida numa pista reta). Se há ciclo, `fast` entra no ciclo e "dá voltas" mais rápido que `slow` — mais cedo ou mais tarde, `fast` alcança `slow` **por trás**, e os dois passam a ocupar o mesmo nó. Não é possível `fast` "pular por cima" de `slow` porque a cada passo a distância entre eles no ciclo diminui em exatamente 1.

## 🎬 Exemplo passo a passo

`head = [3,2,0,-4]`, `pos = 1` (nós: A=3, B=2, C=0, D=-4, e `D.next = B`)

| Passo | slow | fast | slow == fast? |
|---|---|---|---|
| início | A | A | — |
| 1 | B | C | não |
| 2 | C | B | não |
| 3 | D | D | **sim** → ciclo detectado |

Resultado final: `true` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — no pior caso, `fast` percorre a lista inteira mais uma volta completa do ciclo antes de alcançar `slow`, o que ainda é linear no número de nós
- **Espaço:** O(1) — apenas dois ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;

    // As DUAS checagens (fast != null E fast.next != null) protegem o salto duplo:
    // sem a segunda, fast.next.next explode quando fast é o último nó de uma lista sem ciclo.
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;

        if (slow == fast) {   // identidade de nó (==), não valor: val pode se repetir
            return true;
        }
    }

    return false; // fast chegou ao fim (null): não há ciclo
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

- **Comparar por valor (`slow.val == fast.val`) em vez de identidade (`slow == fast`)**: como `Node.val` pode se repetir, isso gera falso positivo numa lista sem ciclo mas com valores duplicados.
- **Esquecer `fast.next != null` na condição do loop**: checar só `fast != null` não é suficiente — `fast.next.next` ainda pode acessar além do fim da lista.
- **Inicializar `slow` e `fast` em nós diferentes**: os dois devem começar em `head`; começá-los em posições diferentes quebra a matemática da detecção.
- **Achar que basta contar um número máximo de passos como heurística de "provavelmente há ciclo"**: não é necessário nem correto — o encontro dos ponteiros é uma garantia matemática, não uma aproximação.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `false` | `fast` já é `null`, loop nem roda |
| Um nó, sem ciclo | `[1], pos=-1` | `false` | `fast.next` vira `null` na 1ª checagem |
| Um nó, ciclo nele mesmo | `[1], pos=0` | `true` | menor ciclo possível: o nó aponta para si mesmo |
| Ciclo começa na cabeça | `[1,2], pos=0` | `true` | garante que o encontro funciona mesmo com o ciclo cobrindo a lista inteira |
| Ciclo no meio | `[3,2,0,-4], pos=1` | `true` | exemplo do enunciado, trace acima |
| Lista maior sem ciclo | `[1,2,3,4,5], pos=-1` | `false` | `fast` percorre até o fim normalmente, sem encontro |

## 🔗 Conexões

- Problemas irmãos: **[0142] Linked List Cycle II** (mesma fase 1, mas precisa retornar o **nó** onde o ciclo começa), **[0202] Happy Number** (o mesmo algoritmo de Floyd aplicado a uma sequência numérica em vez de nós encadeados), **[0287] Find the Duplicate Number** (aplica Floyd's num array tratado como lista encadeada implícita via índices)
- No backend: detectar ciclo sem gastar memória extra é o mesmo raciocínio usado para achar referência circular em grafos de dependência (import cycles, containers de injeção de dependência) ou para garantir que uma cadeia `next`/`parent` (ex.: cadeia de redirecionamentos de URL) não entra em loop infinito.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
