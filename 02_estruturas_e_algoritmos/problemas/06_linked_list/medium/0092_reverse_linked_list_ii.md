# [0092] Reverse Linked List II

> 🔗 [LeetCode 92](https://leetcode.com/problems/reverse-linked-list-ii/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#ReversaoDePonteiros` `#Sentinela` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list simples e dois inteiros `left` e `right` (com `left <= right`, posições **1-indexadas**), inverta os nós da lista da posição `left` até a posição `right`, e retorne a lista resultante.

**Exemplos:**
```
Input:  head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input:  head = [5], left = 1, right = 1
Output: [5]
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 500`, `1 <= left <= right <= n` → posições sempre válidas dentro da lista; não é preciso validar limites
- `-500 <= Node.val <= 500` → sem risco de overflow
- Follow-up "resolva em uma passada" → descarta a solução óbvia de "extrair o trecho, inverter separadamente (como no LC 206), religar" em duas etapas visuais distintas; empurra para inverter **in-place**, nó a nó, dentro da própria passada de travessia

## 🧭 Como reconhecer o padrão

"Inverta só um trecho `[left, right]`" é a generalização direta do LC 206 (que inverte a lista inteira): a técnica central continua sendo **reversão de ponteiros**, mas agora é preciso guardar duas referências extras — o nó **antes** do trecho (para religar o início) e o nó que **era o início** do trecho (que vira a cauda, e precisa ser religado ao que sobrou depois do trecho) (ver [fundamentos](../../../fundamentos/06_linked_list.md)).

## 🐢 Solução 1 — Força bruta (extrair o trecho, inverter à parte, religar)

Percorre a lista até `left`, corta o trecho `[left, right]` da lista (desconectando as duas pontas), inverte esse pedaço isoladamente como no LC 206, e religa as três partes (antes do trecho + trecho invertido + depois do trecho).

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o tempo já é ótimo, mas conceitualmente processa a lista em "três etapas" separadas (cortar, inverter, religar) — o follow-up pede uma solução em **uma única passada**, que entrelaça a inversão com a religação usando o truque de "inserção pela frente" (ver Solução 2), sem nunca desconectar o trecho da lista principal.

## 💡 Solução 2 — A ideia otimizada (intuição)

Usa um sentinela (`dummy`) e anda `prev` até o nó **imediatamente antes** da posição `left`. O nó em `prev.next` (posição `left`) vai virar a **cauda** do trecho invertido — ele nunca se move, só os nós depois dele são "arrancados" e reinseridos logo após `prev`, um de cada vez (a técnica de **inserção pela frente**, "head insertion"). Repetindo isso `right - left` vezes, cada novo nó processado empurra o anterior para trás, invertendo o trecho inteiro sem nunca precisar de uma segunda passada ou de desconectar o resto da lista.

## 🎬 Exemplo passo a passo

`head = [1,2,3,4,5]`, `left = 2`, `right = 4`

Depois de andar `prev` até a posição 1 (`prev = nó de valor 1`) e fixar `cur = prev.next` (nó de valor 2, que será a cauda do trecho):

| Iteração | nxt (arrancado) | Ação (inserção pela frente) | Lista após a iteração |
|---|---|---|---|
| início | — | — | 1 → 2 → 3 → 4 → 5 |
| 1 | 3 | `2.next=4`; `3.next=2`; `1.next=3` | 1 → 3 → 2 → 4 → 5 |
| 2 | 4 | `2.next=5`; `4.next=2`; `1.next=4` | 1 → 4 → 3 → 2 → 5 |

`cur` (nó de valor 2) nunca se move — ele vira a cauda do trecho invertido, e cada `nxt` arrancado é inserido logo depois de `prev`.

Resultado final: `1 → 4 → 3 → 2 → 5` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada: `left - 1` passos para posicionar `prev`, mais `right - left` iterações de inserção pela frente
- **Espaço:** O(1) — sentinela e alguns ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode reverseBetween(ListNode head, int left, int right) {
    ListNode dummy = new ListNode(0, head); // sentinela: cobre o caso left == 1 (inverte desde a head)
    ListNode prev = dummy;

    // Anda até o nó IMEDIATAMENTE ANTES da posição left.
    for (int i = 0; i < left - 1; i++) {
        prev = prev.next;
    }

    // 'cur' é o nó na posição left — ele NUNCA se move: vira a cauda do trecho invertido.
    ListNode cur = prev.next;

    // A cada iteração, "arranca" o nó logo depois de cur e o insere logo depois de prev
    // (inserção pela frente). Isso empurra os nós já processados para trás, um a um.
    for (int i = 0; i < right - left; i++) {
        ListNode nxt = cur.next;
        cur.next = nxt.next;   // cur "pula" o nó arrancado
        nxt.next = prev.next;  // o nó arrancado aponta para o atual início do trecho
        prev.next = nxt;       // prev passa a apontar para o nó recém-inserido: novo início do trecho
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

- **Confundir a ordem das três reatribuições na inserção pela frente**: `cur.next = nxt.next` precisa vir **antes** de `nxt.next = prev.next`, senão `nxt.next` é sobrescrito antes de `cur` conseguir "pular" para o nó certo.
- **Mover `cur` a cada iteração**: `cur` fica **fixo** na posição `left` durante todo o processo — ele é a cauda do trecho, e é `nxt` (não `cur`) que avança/é arrancado a cada passo.
- **Não usar sentinela quando `left == 1`**: se o trecho a inverter começa na própria `head`, sem `dummy` seria preciso tratar a atualização da cabeça como caso especial.
- **Confundir posições 1-indexadas com 0-indexadas**: `left` e `right` contam a partir de 1, não de 0 — andar `left - 1` passos (não `left`) para posicionar `prev` é o ajuste correto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Trecho de 1 nó (`left == right`) | `head=[5], left=1, right=1` | `[5]` | o loop de inserção roda 0 vezes, nada muda |
| Inverter desde a cabeça | `head=[1,2,3], left=1, right=3` | `[3,2,1]` | equivale ao LC 206 inteiro, testa o sentinela cobrindo `left=1` |
| Inverter até o fim | `head=[1,2,3], left=2, right=3` | `[1,3,2]` | trecho termina no último nó da lista |
| Trecho no meio, exemplo do enunciado | `head=[1,2,3,4,5], left=2, right=4` | `[1,4,3,2,5]` | trace acima |
| Lista de 1 nó | `head=[1], left=1, right=1` | `[1]` | menor caso possível |

## 🔗 Conexões

- Problemas irmãos: **[0206] Reverse Linked List** (o caso particular `left=1, right=n`, mesma técnica sem precisar de `prev` externo), **[0025] Reverse Nodes in k-Group** (aplica esta mesma inversão parcial repetidamente, em blocos de tamanho `k`)
- No backend: inverter apenas um trecho de uma sequência encadeada, preservando o resto intacto, aparece em **edição de playlists/filas** (inverter a ordem de um intervalo de itens sem remontar a estrutura inteira) e em **replay parcial de eventos** onde só uma janela específica do histórico precisa ser processada em ordem reversa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
