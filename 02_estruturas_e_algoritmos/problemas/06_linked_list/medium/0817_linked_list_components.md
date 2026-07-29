# [0817] Linked List Components

> 🔗 [LeetCode 817](https://leetcode.com/problems/linked-list-components/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#HashTable` `#Medium`

## 📜 O Problema

Dado o `head` de uma linked list com valores **únicos** e um array `nums` (subconjunto dos valores da lista), conte o número de **componentes conectados** em `nums`: uma sequência máxima e não vazia de nós **consecutivos** na lista, onde todo nó pertence a `nums`.

**Exemplos:**
```
Input:  head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explicação: 0 e 1 são consecutivos e ambos em nums → um componente [0,1]. O 3 está isolado (2 não está em nums) → outro componente [3]. Total: 2.

Input:  head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explicação: [0,1] é um componente, [3,4] é outro (2 os separa). Total: 2.
```

**Restrições (e o que elas denunciam):**
- Número de nós `n` em `[1, 10^4]`, `1 <= nums.length <= n` → O(n) é o esperado
- Valores da lista **únicos** → garante que checar "este valor está em `nums`?" é uma pergunta bem definida (sem ambiguidade de qual ocorrência)
- "componente = sequência **consecutiva** de nós, todos em `nums`" → a palavra-chave é **consecutiva na lista**, não em `nums`; a ordem de `nums` é irrelevante, só importa quais valores da linked list original estão marcados

## 🧭 Como reconhecer o padrão

"Verifique pertencimento repetidamente" é a assinatura de **hashing** (ver [fundamentos de arrays/hashing](../../../fundamentos/01_arrays_e_hashing.md)): transformar `nums` num `HashSet` dá checagem O(1) por valor. A parte de **linked list** é usar essa checagem durante uma travessia simples, detectando onde cada "sequência de valores marcados" começa e termina — um componente termina exatamente quando o valor atual está em `nums` mas o **próximo** não está (ou não há próximo).

## 🐢 Solução 1 — Força bruta (checar pertencimento varrendo o array `nums`)

Para cada nó da lista, percorre o array `nums` inteiro para checar se o valor está lá (sem estrutura auxiliar). Conta uma nova "abertura de componente" sempre que o nó atual está em `nums` mas o nó anterior não estava (ou é o início da lista).

- Tempo: O(n × m), onde `m = nums.length` — para cada um dos `n` nós, uma varredura O(m) em `nums` · Espaço: O(1) extra
- **Por que não basta:** com `n` até 10^4, uma checagem O(m) por nó pode custar até `10^4 × 10^4 = 10^8` operações no pior caso — lento. Convertendo `nums` para um `HashSet` uma única vez (O(m)), cada checagem de pertencimento durante a travessia vira O(1).

## 💡 Solução 2 — A ideia otimizada (intuição)

Converte `nums` para um `HashSet` (checagem O(1)). Percorre a linked list uma vez: para cada nó, se seu valor está no set **e** (não há próximo nó **ou** o próximo não está no set), esse nó é o **fim** de um componente — incrementa o contador. Não é preciso marcar onde um componente **começa**; basta contar quantas vezes um componente **termina**, o que é exatamente o mesmo número.

## 🎬 Exemplo passo a passo

`head = [0,1,2,3]`, `nums = [0,1,3]` → `set = {0,1,3}`

| Nó (`cur`) | `cur.val` em `set`? | `cur.next` existe e está em `set`? | É fim de componente? | `count` após |
|---|---|---|---|---|
| 0 | sim | sim (`next=1`, está no set) | não (o componente continua) | 0 |
| 1 | sim | não (`next=2`, não está no set) | **sim** | 1 |
| 2 | não | — | não (nem começa um componente) | 1 |
| 3 | sim | não há próximo (`cur.next == null`) | **sim** | 2 |

Resultado final: `2` ✔ — bate com o esperado no enunciado (componentes `[0,1]` e `[3]`).

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — O(m) para construir o `HashSet`, O(n) para a travessia com checagens O(1)
- **Espaço:** O(m) para o `HashSet`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numComponents(ListNode head, int[] nums) {
    Set<Integer> set = new HashSet<>();
    for (int n : nums) set.add(n);

    int count = 0;
    ListNode cur = head;

    while (cur != null) {
        // Um nó marca o FIM de um componente quando ele está no set, mas o próximo
        // nó não está (ou não existe) — não é preciso rastrear onde o componente começou.
        boolean estaNoSet = set.contains(cur.val);
        boolean proximoContinua = cur.next != null && set.contains(cur.next.val);

        if (estaNoSet && !proximoContinua) {
            count++;
        }

        cur = cur.next;
    }

    return count;
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

- **Contar a "abertura" de um componente em vez do "fechamento"**: também funciona (é simétrico), mas exige rastrear o valor do nó **anterior** — contar o fechamento (nó atual em `set`, próximo não) é mais direto porque só olha o nó atual e o seguinte, sem precisar guardar histórico.
- **Esquecer de checar `cur.next != null` antes de `set.contains(cur.next.val)`**: sem essa checagem, o último nó da lista lança `NullPointerException` ao tentar ler `cur.next.val`.
- **Confundir "consecutivo em `nums`" com "consecutivo na lista"**: a ordem de `nums` não importa (é só um conjunto de valores marcados) — o que define um componente é a **adjacência na linked list original**, não a posição dentro do array `nums`.
- **Usar uma lista (`List`) em vez de `HashSet` para `nums`**: uma lista faria `contains` custar O(m) de novo, reintroduzindo o problema que o `HashSet` resolve.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Todos os valores marcados | `head=[1,2,3], nums=[1,2,3]` | `1` | a lista inteira é um único componente |
| Nenhum valor marcado | `head=[1,2,3], nums=[9]` | `0` | nenhum nó pertence a `nums` (a restrição garante `nums` ⊆ valores da lista, mas vale validar o caso degenerado) |
| Valores alternados (nenhum consecutivo) | `head=[1,2,3,4], nums=[1,3]` | `2` | cada valor marcado forma seu próprio componente de tamanho 1 |
| Componente na cauda, exemplo do enunciado | `head=[0,1,2,3], nums=[0,1,3]` | `2` | trace acima |
| Dois componentes separados, exemplo do enunciado | `head=[0,1,2,3,4], nums=[0,3,1,4]` | `2` | valida que a ordem de `nums` não importa, só a adjacência na lista |

## 🔗 Conexões

- Problemas irmãos: **[0128] Longest Consecutive Sequence** (mesma ideia de "detectar início/fim de sequência com hashing", mas em array em vez de linked list), **[0203] Remove Linked List Elements** (mesma travessia simples com uma checagem por nó, para uma finalidade diferente)
- No backend: contar sequências consecutivas marcadas dentro de uma estrutura ordenada aparece em **análise de disponibilidade de recursos** (contar blocos contíguos livres/ocupados numa lista de alocação) e em **detecção de rajadas (bursts) em séries temporais**, onde se quer contar quantos grupos consecutivos de eventos "marcados" (ex.: acima de um limiar) ocorreram, ignorando a ordem de qualquer conjunto de referência externo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
