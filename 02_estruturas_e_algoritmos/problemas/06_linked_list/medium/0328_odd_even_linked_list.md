# [0328] Odd Even Linked List

> 🔗 [LeetCode 328](https://leetcode.com/problems/odd-even-linked-list/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#DoisPonteiros` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list, agrupe todos os nós de **índice ímpar** juntos, seguidos pelos de **índice par**, e retorne a lista reordenada. O 1º nó é considerado ímpar, o 2º é par, e assim por diante. A ordem relativa **dentro** de cada grupo deve ser preservada. Precisa ser resolvido em O(1) de espaço extra e O(n) de tempo.

**Exemplos:**
```
Input:  head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input:  head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → O(n) é o esperado
- `-10^6 <= Node.val <= 10^6` → sem risco de overflow
- "O(1) espaço extra e O(n) tempo" explícito no enunciado (não é follow-up, é requisito) → descarta qualquer cópia para array/lista auxiliar; a solução precisa reorganizar ponteiros in-place
- "preserve a ordem relativa dentro de cada grupo" → garante que a solução é sobre **filtrar e reconectar**, não sobre ordenar por algum critério

## 🧭 Como reconhecer o padrão

"Separe em dois grupos por posição, preservando ordem, numa única passada" é resolvido com **dois ponteiros correndo em paralelo** — um coletando os nós de posição ímpar, outro os de posição par — de forma muito parecida com o LC 86 (Partition List), mas aqui o critério de separação é a **posição**, não o valor, e as duas listas são construídas simultaneamente avançando os dois ponteiros a cada iteração (em vez de percorrer um ponteiro só e decidir para qual lista cada nó vai).

## 🐢 Solução 1 — Força bruta (copiar índices para dois arrays, reconstruir)

Percorre a lista com um contador de posição, copiando os nós de posição ímpar para um array e os de posição par para outro (na ordem em que aparecem). Reconstrói a lista concatenando os dois arrays.

- Tempo: O(n) · Espaço: O(n) para os dois arrays
- **Por que não basta:** o enunciado exige explicitamente O(1) de espaço extra — copiar os nós para arrays viola essa restrição diretamente, mesmo que o tempo já seja ótimo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantém dois ponteiros, `odd` (nós de posição ímpar) e `even` (nós de posição par), começando em `head` e `head.next` respectivamente — e guarda `evenHead` (a cabeça da lista par) para religar no final. A cada passo, avança os **dois** ponteiros juntos: `odd` pula para o próximo nó ímpar (`even.next`), e `even` pula para o próximo nó par (`odd.next`, já atualizado). Como os nós nunca são copiados, só "esticados" para o próximo da mesma paridade, a ordem relativa dentro de cada grupo é preservada automaticamente. No final, emenda: `odd.next = evenHead`.

## 🎬 Exemplo passo a passo

`head = [1,2,3,4,5]`

| Passo | odd (antes) | even (antes) | Ação | odd (depois) | even (depois) |
|---|---|---|---|---|---|
| início | 1 | 2 (`evenHead`) | — | 1 | 2 |
| 1 | 1 | 2 | `1.next=3` (`odd.next=even.next`); `2.next=4` (`even.next=odd.next`) | 3 | 4 |
| 2 | 3 | 4 | `3.next=5`; `4.next=null` (`5.next` original era `null`) | 5 | null |
| fim | 5 | null | `even == null`, loop encerra | — | — |

Emenda final: `odd.next = evenHead` → `5.next = 2`.

Resultado final: `1 → 3 → 5 → 2 → 4` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada, avançando os dois ponteiros em paralelo
- **Espaço:** O(1) — só três ponteiros (`odd`, `even`, `evenHead`), os nós são reaproveitados

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode oddEvenList(ListNode head) {
    if (head == null) return head; // lista vazia: nada a reorganizar

    ListNode odd = head, even = head.next, evenHead = even; // evenHead: guarda o início da 2ª metade p/ emendar no fim

    // even != null cobre lista de tamanho par acabando em even; even.next != null cobre
    // lista de tamanho ímpar acabando em odd — as duas checagens juntas evitam NullPointerException
    // nos dois casos.
    while (even != null && even.next != null) {
        odd.next = even.next;  // odd pula para o próximo nó ÍMPAR
        odd = odd.next;
        even.next = odd.next;  // even pula para o próximo nó PAR (usa o odd já atualizado)
        even = even.next;
    }

    odd.next = evenHead; // emenda: fim da lista ímpar aponta para o início da lista par
    return head;
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

- **Esquecer de guardar `evenHead` antes do loop**: sem essa referência salva no início, não há como emendar a lista ímpar à lista par no final — `even` já terá avançado para além do início.
- **Condição de parada incompleta (`even != null` sozinho)**: sem também checar `even.next != null`, `even.next = odd.next` pode ser executado quando `odd.next` (que seria o novo `even`) ainda não existe, ou o acesso a `even.next` explode em listas de tamanho ímpar — as duas condições juntas cobrem tanto listas pares quanto ímpares.
- **Atualizar `even` antes de `odd`, ou usar valores desatualizados**: a ordem das quatro linhas dentro do loop importa — `odd.next` precisa ser setado (e `odd` avançado) **antes** de `even.next = odd.next`, porque essa linha depende do novo valor de `odd`.
- **Confundir com "separar por valor" (LC 86)**: aqui o critério é **posição** (1º, 3º, 5º... vs. 2º, 4º, 6º...), não o valor do nó — os dois ponteiros avançam alternadamente pela mesma lista, não filtram por uma condição sobre `val`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head = []` | `[]` | retorna cedo, `head == null` |
| Um nó | `head = [1]` | `[1]` | `even` já é `null` (não existe `head.next`), loop nem roda |
| Dois nós | `head = [1,2]` | `[1,2]` | menor caso onde par e ímpar existem; loop roda 0 vezes (`even.next` é `null`), mas a emenda final já produz o resultado certo |
| Tamanho ímpar, exemplo do enunciado | `head = [1,2,3,4,5]` | `[1,3,5,2,4]` | trace acima |
| Tamanho par maior, exemplo do enunciado | `head = [2,1,3,5,6,4,7]` | `[2,3,6,7,1,5,4]` | valida o padrão numa lista de 7 nós com valores fora de ordem |

## 🔗 Conexões

- Problemas irmãos: **[0086] Partition List** (mesma estrutura de "duas listas construídas em paralelo, emendadas no final", mas separando por valor em vez de posição), **[0143] Reorder List** (também reorganiza a lista intercalando grupos, mas com um objetivo de intercalação diferente)
- No backend: separar um stream de dados em dois grupos por posição relativa (não por conteúdo) aparece em **algoritmos de particionamento round-robin** (distribuir itens alternadamente entre workers ou shards) e em **desmultiplexação de sinais intercalados** (ex.: separar frames pares/ímpares num protocolo de streaming que intercala dois fluxos de dados no mesmo canal).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
