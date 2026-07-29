# [1019] Next Greater Node In Linked List

> 🔗 [LeetCode 1019](https://leetcode.com/problems/next-greater-node-in-linked-list/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list com `n` nós, para cada nó encontre o valor do **próximo nó maior**: o primeiro nó à frente dele (mais à direita) com valor **estritamente maior**. Retorne um array `answer` (1-indexado na posição, 0-indexado no array) onde `answer[i]` é esse valor, ou `0` se não existir.

**Exemplos:**
```
Input:  head = [2,1,5]
Output: [5,5,0]

Input:  head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

**Restrições (e o que elas denunciam):**
- Número de nós `n` em `[1, 10^4]` → O(n²) (para cada nó, varrer o resto da lista) pode chegar a 10^8 no pior caso — arriscado; O(n) é a meta segura
- `1 <= Node.val <= 10^9` → sem risco de overflow, mas confirma que os valores não servem como índice de array auxiliar (são grandes demais)

## 🧭 Como reconhecer o padrão

Apesar do input ser uma `ListNode`, "para cada elemento, encontre o **próximo maior à direita**" é a assinatura clássica de **monotonic stack** (ver [fundamentos](../../../fundamentos/04_stack.md)) — exatamente o mesmo problema do LC 496/739, só que a fonte de dados é uma linked list em vez de um array. Pela regra de ouro de classificação ("técnica da solução ótima, não tipo do input"), isso é um problema de pilha, não de linked list: a única adaptação necessária é converter a lista para um array de valores antes de aplicar a técnica (porque a pilha monotônica precisa andar para frente e para trás em termos de índice, o que uma linked list simples não permite diretamente).

## 🐢 Solução 1 — Força bruta (para cada nó, varrer o resto da lista)

Para cada nó, percorre todos os nós **depois** dele até achar o primeiro com valor maior (ou chegar ao fim, retornando `0`).

- Tempo: O(n²) — no pior caso (lista estritamente decrescente), cada nó varre o resto inteiro da lista sem nunca achar o próximo maior · Espaço: O(n) para o array de resposta
- **Por que não basta:** com `n` até 10^4, O(n²) chega a 10^8 operações no pior caso — arriscado dentro do tempo esperado. Cada trecho da lista acaba sendo varrido repetidamente para nós diferentes, quando uma pilha monotônica resolve todo mundo numa única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, converte a linked list para um array `vals` (uma passada O(n)) — isso dá acesso por índice, necessário para a pilha monotônica funcionar com a mesma lógica do LC 496. Depois, percorre `vals` mantendo uma **pilha monotônica decrescente de índices**: para cada posição `i`, enquanto o valor no topo da pilha for **menor** que `vals[i]`, esse topo acabou de achar seu próximo maior (é `vals[i]`) — desempilha e preenche `answer[topo] = vals[i]`. Depois empilha o índice `i`. No final, quem sobrar na pilha nunca achou um maior à direita, e mantém o valor default `0`.

## 🎬 Exemplo passo a passo

`head = [2,7,4,3,5]` → `vals = [2,7,4,3,5]`

| `i` | `vals[i]` | Ação do `while` (desempilha e resolve) | Pilha após (índices) | `answer` após |
|---|---|---|---|---|
| 0 | 2 | pilha vazia, nada a resolver | `[0]` | `[0,0,0,0,0]` |
| 1 | 7 | `vals[0]=2 < 7` → pop 0, `answer[0]=7` | `[1]` | `[7,0,0,0,0]` |
| 2 | 4 | `vals[1]=7 < 4`? não → mantém monotonia | `[1,2]` | `[7,0,0,0,0]` |
| 3 | 3 | `vals[2]=4 < 3`? não → mantém monotonia | `[1,2,3]` | `[7,0,0,0,0]` |
| 4 | 5 | `vals[3]=3 < 5` → pop 3, `answer[3]=5`; `vals[2]=4 < 5` → pop 2, `answer[2]=5`; `vals[1]=7 < 5`? não → para | `[1,4]` | `[7,0,5,5,0]` |

Sobrou `[1,4]` na pilha → `answer[1]` e `answer[4]` mantêm `0` (nunca acharam um maior à direita).

Resultado final: `[7,0,5,5,0]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — converter a lista é O(n); cada índice entra e sai da pilha no máximo uma vez, então o `while` no total (somado por toda a execução) é O(n)
- **Espaço:** O(n) — o array `vals`, a pilha e o array de resposta são todos proporcionais a `n`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] nextLargerNodes(ListNode head) {
    List<Integer> vals = new ArrayList<>();
    for (ListNode cur = head; cur != null; cur = cur.next) {
        vals.add(cur.val); // converte a lista para array: dá acesso por índice p/ a pilha monotônica
    }

    int n = vals.size();
    int[] answer = new int[n]; // default 0: cobre automaticamente "não achou próximo maior"
    Deque<Integer> pilha = new ArrayDeque<>(); // guarda ÍNDICES em ordem decrescente de valor

    for (int i = 0; i < n; i++) {
        while (!pilha.isEmpty() && vals.get(pilha.peek()) < vals.get(i)) {
            answer[pilha.pop()] = vals.get(i); // vals[i] é o próximo maior de quem estava no topo
        }
        pilha.push(i);
    }

    return answer;
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

- **Guardar valores na pilha em vez de índices**: como o array `vals` pode ter valores repetidos e a resposta é indexada por **posição**, não por valor, é preciso guardar o **índice** na pilha para saber onde escrever em `answer` quando o desempate acontecer.
- **Usar `<=` em vez de `<` na comparação do `while`**: o enunciado pede "estritamente maior" — usar `<=` faria um valor igual "resolver" o topo da pilha incorretamente.
- **Tentar aplicar a pilha monotônica direto sobre a linked list**: uma pilha monotônica precisa comparar o elemento atual com o topo em O(1) e eventualmente "voltar" a processar posições anteriores — isso é natural com índices de array, mas não tem equivalente direto percorrendo só `next` de uma lista encadeada.
- **Esquecer que `answer` já começa com `0` (o default de `int[]` em Java)**: não é necessário inicializar explicitamente os "sem próximo maior" — só os elementos resolvidos pelo `while` são sobrescritos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único nó | `head = [5]` | `[0]` | nenhum nó à frente, pilha nunca resolve nada |
| Sequência estritamente crescente | `head = [1,2,3]` | `[2,3,0]` | cada nó resolve o anterior imediatamente, pilha nunca acumula mais de 1 |
| Sequência estritamente decrescente | `head = [3,2,1]` | `[0,0,0]` | pior caso: nenhum nó encontra maior à direita, todos ficam na pilha até o fim |
| Valores duplicados | `head = [2,2,2]` | `[0,0,0]` | "estritamente maior" exclui empates — nenhum 2 resolve outro 2 |
| Exemplo maior do enunciado | `head = [2,7,4,3,5]` | `[7,0,5,5,0]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0496] Next Greater Element I** (mesma técnica, sobre array em vez de linked list), **[0503] Next Greater Element II** (mesma técnica, mas array circular), **[0739] Daily Temperatures** (mesma ideia, retornando a distância até o próximo maior em vez do valor)
- No backend: "para cada evento, encontre o próximo que o supera" aparece em **análise de séries temporais financeiras** (achar o próximo momento em que um preço supera o atual, sinalizando reversão de tendência) e em **sistemas de monitoramento** que precisam saber quando um alerta pendente foi "resolvido" pelo próximo evento que ultrapassa um limiar.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
