# [0725] Split Linked List in Parts

> 🔗 [LeetCode 725](https://leetcode.com/problems/split-linked-list-in-parts/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list e um inteiro `k`, divida a lista em `k` partes consecutivas. O tamanho de cada parte deve ser o mais parecido possível (nenhuma diferença maior que 1 entre partes); partes mais cedo devem ser **maiores ou iguais** às mais tarde, e algumas podem ficar vazias (`[]`) se `k` for maior que o número de nós. Retorne um array com as `k` partes.

**Exemplos:**
```
Input:  head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]

Input:  head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explicação: 10 nós divididos em 3 partes: 10 = 3×3 + 1, então a 1ª parte fica com 1 nó a mais (4), as outras com 3.
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 1000]`, `1 <= k <= 50` → tanto listas menores que `k` (gerando partes vazias) quanto listas bem maiores que `k` precisam ser tratadas
- "tamanhos o mais parecidos possível, diferença máxima de 1" → é uma divisão de resto: com `n` nós e `k` partes, cada parte tem `n / k` nós (divisão inteira), e as primeiras `n % k` partes recebem **1 nó a mais** para absorver o resto — é aritmética pura, decidida **antes** de tocar em qualquer ponteiro
- "partes mais cedo ≥ partes mais tarde em tamanho" → confirma que o "nó extra" vai sempre para as primeiras partes, nunca distribuído do fim para o início

## 🧭 Como reconhecer o padrão

"Divida uma lista em `k` pedaços de tamanho quase igual" não usa fast & slow nem reversão — é **aritmética de divisão e resto** decidindo os tamanhos, seguida de uma travessia simples que **corta** a lista nos pontos certos (religando `next = null` a cada corte, como no LC 148 ao dividir para o merge sort, mas aqui repetido `k` vezes com tamanhos pré-calculados em vez de sempre no meio).

## 🐢 Solução 1 — Força bruta (contar tudo, copiar nós para arrays por parte)

Primeira passada: conta o total de nós (`n`). Calcula os tamanhos de cada uma das `k` partes. Segunda passada: percorre a lista copiando os **valores** para `k` arrays diferentes (um por parte), depois reconstrói `k` novas listas a partir desses arrays.

- Tempo: O(n + k) · Espaço: O(n) para os arrays intermediários + O(n) para as novas listas
- **Por que não basta:** o tempo já é ótimo, mas copiar valores para arrays intermediários é desnecessário — os nós originais já existem e só precisam ser **cortados** nos lugares certos (setando `next = null`), sem nunca alocar um nó novo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro conta `n` (número total de nós) numa passada. Calcula `base = n / k` (tamanho mínimo garantido por parte) e `extra = n % k` (quantas partes, a partir da primeira, recebem `base + 1` em vez de `base`). Depois, uma segunda passada percorre a lista `k` vezes: para a `i`-ésima parte, anda `tamanho[i] - 1` passos a partir do início dela, corta ali (`next = null` no nó atual, guardando o próximo antes de cortar), e usa o nó guardado como início da próxima parte.

## 🎬 Exemplo passo a passo

`head = [1,2,3,4,5,6,7,8,9,10]`, `k = 3` → `n = 10`, `base = 10/3 = 3`, `extra = 10 % 3 = 1`

| Parte `i` | Tamanho (`base` + 1 extra se `i < extra`) | Início da parte | Corte (após andar `tamanho-1` passos) | Próximo início |
|---|---|---|---|---|
| 0 | `3 + 1 = 4` (`0 < 1`) | nó `1` | anda 3 passos → para em `4`; corta `4.next` | nó `5` |
| 1 | `3 + 0 = 3` (`1 ≥ 1`) | nó `5` | anda 2 passos → para em `7`; corta `7.next` | nó `8` |
| 2 | `3 + 0 = 3` (`2 ≥ 1`) | nó `8` | anda 2 passos → para em `10`; `10.next` já era `null` | — (fim da lista) |

Resultado final: `[[1,2,3,4], [5,6,7], [8,9,10]]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para contar, mais uma passada total (somando todas as `k` partes) para cortar, já que cada nó é visitado no máximo duas vezes
- **Espaço:** O(k) para o array de resultado (as cabeças das partes) — os nós em si são reaproveitados, não copiados

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode[] splitListToParts(ListNode head, int k) {
    int n = 0;
    for (ListNode cur = head; cur != null; cur = cur.next) n++;

    int base = n / k;   // tamanho mínimo garantido de cada parte
    int extra = n % k;  // quantas partes (a partir da 1ª) recebem +1 nó

    ListNode[] resultado = new ListNode[k];
    ListNode cur = head;

    for (int i = 0; i < k && cur != null; i++) {
        resultado[i] = cur; // início desta parte

        int tamanho = base + (i < extra ? 1 : 0); // as primeiras 'extra' partes ganham o nó a mais
        for (int j = 0; j < tamanho - 1; j++) {
            cur = cur.next; // anda até o ÚLTIMO nó desta parte
        }

        ListNode proximo = cur.next; // guarda onde a próxima parte começa, ANTES de cortar
        cur.next = null;              // corta esta parte da próxima
        cur = proximo;
    }

    // Partes além do que a lista tem (k > n) ficam null no array — representam [] no resultado.
    return resultado;
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

- **Esquecer de guardar `cur.next` antes de cortar**: assim que `cur.next = null` é executado, a referência para o resto da lista original se perde — sem salvar `proximo` antes, o loop externo não sabe onde a próxima parte começa.
- **Distribuir o resto (`extra`) errado**: o enunciado exige que partes **mais cedo** sejam maiores ou iguais — dar o nó extra às **últimas** partes (em vez das primeiras `extra`) produz uma divisão tecnicamente válida em tamanho, mas na ordem errada.
- **Não tratar `k > n`**: quando há mais partes pedidas do que nós disponíveis, algumas partes ficam vazias (`null`/`[]`) — o loop `i < k && cur != null` já cobre isso automaticamente, parando assim que os nós acabam.
- **Calcular `tamanho - 1` errado ao andar até o fim da parte**: andar `tamanho` passos (em vez de `tamanho - 1`) a partir do início da parte ultrapassa o último nó dela, cortando no lugar errado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Lista vazia | `head=[], k=3` | `[[],[],[]]` | `cur` já é `null`, todas as partes ficam vazias |
| Mais partes que nós, exemplo do enunciado | `head=[1,2,3], k=5` | `[[1],[2],[3],[],[]]` | testa `k > n`: as duas últimas partes ficam vazias |
| Divisão exata | `head=[1,2,3,4], k=2` | `[[1,2],[3,4]]` | `extra=0`, todas as partes com o mesmo tamanho |
| Divisão com resto, exemplo do enunciado | `head=[1..10], k=3` | `[[1,2,3,4],[5,6,7],[8,9,10]]` | trace acima, valida a distribuição do resto nas primeiras partes |
| `k = 1` | `head=[1,2,3], k=1` | `[[1,2,3]]` | menor `k` possível, a única parte é a lista inteira |

## 🔗 Conexões

- Problemas irmãos: **[0086] Partition List** (também divide uma lista em duas partes, mas por valor em vez de por tamanho), **[0148] Sort List** (corta a lista ao meio repetidamente, com a mesma técnica de "guardar o próximo antes de cortar")
- No backend: dividir uma coleção em partes de tamanho equilibrado é o padrão usado em **particionamento de dados para processamento paralelo** (distribuir um dataset entre `k` workers, com o resto distribuído nos primeiros workers para equilibrar a carga) e em **paginação com balanceamento** (dividir um total de itens em páginas de tamanho o mais uniforme possível).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
