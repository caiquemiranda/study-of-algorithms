# [3507] Minimum Pair Removal to Sort Array I

> 🔗 [LeetCode 3507](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/) · Dificuldade: 🟢 easy · Categoria: [`09_heap_priority_queue`](../../../fundamentos/09_heap_priority_queue.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Heap` `#Simulacao` `#LazyDeletion` `#Easy`

## 📜 O Problema

Dado um array `nums`, você pode repetir a seguinte operação quantas vezes quiser:
- Escolha o par de elementos **adjacentes** com a **menor soma**. Se houver empate, escolha o mais à esquerda.
- Substitua o par pela sua soma (os dois elementos viram um só).

Retorne o **número mínimo de operações** necessárias para deixar `nums` **não decrescente** (cada elemento ≥ o anterior).

**Exemplos:**
```
Input:  nums = [5,2,3,1]
Output: 2
Explicação:
- O par (3,1) tem a menor soma (4). Após substituir: nums = [5,2,4].
- O par (2,4) tem a menor soma (6). Após substituir: nums = [5,6].
O array ficou não decrescente em duas operações.

Input:  nums = [1,2,2]
Output: 0
Explicação: o array já está ordenado.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 50` → array minúsculo; uma simulação O(n²) já passa folgado — a lição deste problema não é "sobreviver ao limite de tempo", é entender a **técnica que generaliza** (ver Conexões, a versão "II" deste problema tem `n` até 10^5)
- `-1000 <= nums[i] <= 1000` → soma de dois elementos cabe tranquilamente em `int`, mesmo depois de várias fusões acumuladas
- "escolha o **mais à esquerda** em caso de empate" → o algoritmo é totalmente determinístico: não há escolha estratégica a fazer, só simular fielmente a regra até o array ficar ordenado

## 🧭 Como reconhecer o padrão

"A cada passo, processe sempre o elemento **mais urgente agora** (aqui, o par de menor soma), repita até uma condição de parada" é a assinatura de **simulação com priority queue** — ver [fundamentos](../../../fundamentos/09_heap_priority_queue.md), seção "Como Reconhecer". É primo direto de problemas como **Last Stone Weight** (sempre pega as duas maiores pedras), com a diferença de que aqui os candidatos precisam ser **adjacentes** — o que exige combinar o heap com uma estrutura que sabe quem é vizinho de quem *depois* de fusões (uma lista duplamente encadeada simulada com arrays `prev`/`next`).

## 🐢 Solução 1 — Força bruta (rescanear o array inteiro a cada operação)

Mantém `nums` como uma lista mutável. A cada operação: percorre a lista inteira (O(n)) para achar o par adjacente de menor soma (mais à esquerda em caso de empate), substitui os dois elementos pela soma (O(n) por causa do deslocamento), e verifica se a lista já está não decrescente com outra passada (O(n)).

- Tempo: O(n) por operação × até `n` operações no pior caso = **O(n²)** · Espaço: O(n)
- **Por que ela já resolve este problema, mas não é a lição:** com `n <= 50`, O(n²) = 2500 passos, absurdamente rápido — essa força bruta passa sem problema na variante "I". O motivo para estudar a versão otimizada é que ela é a técnica que **generaliza**: a cada operação, só os pares **vizinhos ao ponto da fusão** realmente mudam — rescanear o array inteiro de novo é trabalho redundante que seria proibitivo se `n` fosse grande (como na variante "II", com `n` até 10^5).

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de rescanear tudo a cada operação, mantém-se:
1. Um **min-heap** de `(soma, índiceEsquerdo)` para todos os pares adjacentes **atualmente válidos**.
2. Uma **lista duplamente encadeada simulada** com arrays `prev[]`/`next[]` — permite, após fundir dois elementos, religar os vizinhos em O(1), sem deslocar nada.
3. Um contador `badPairs` de quantos pares adjacentes **violam** a ordem não decrescente — quando esse contador chega a zero, o array está ordenado e paramos.

A cada operação: tira do heap o par de menor soma (descartando entradas obsoletas via **lazy deletion** — pares cujos vizinhos já mudaram desde que foram empilhados), funde os dois elementos (o da esquerda absorve a soma, o da direita é marcado como "morto" e desligado da lista), religa os vizinhos, atualiza `badPairs` só para os (no máximo) 3 pares afetados pela fusão, e empurra para o heap os (no máximo) 2 novos pares adjacentes criados.

## 🎬 Exemplo passo a passo

`nums = [5,2,3,1]` (índices 0,1,2,3)

| Passo | Pares adjacentes ativos (soma) | Escolhido (mais à esquerda em empate) | Array após fusão | badPairs após |
|---|---|---|---|---|
| início | (5,2)=7, (2,3)=5, (3,1)=4 | — | [5,2,3,1] | 2 → `(5,2)` e `(3,1)` violam a ordem |
| 1 | menor soma = 4 | par (3,1) no índice 2 | [5,2,4] | 1 → só `(5,2)` ainda viola |
| 2 | (5,2)=7, (2,4)=6 | menor soma = 6, par (2,4) | [5,6] | 0 → array não decrescente, **para** |

Resultado final: `2` operações ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — cada uma das até `n-1` fusões faz no máximo O(1) operações de heap `push` (2 novas entradas) e a soma de todos os `pop`s (incluindo os descartados por lazy deletion) é limitada pelo total de entradas já inseridas, O(n); cada operação de heap custa O(log n)
- **Espaço:** O(n) — arrays `val`, `prev`, `next`, `alive` e o heap, todos proporcionais a `n`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumPairRemoval(int[] nums) {
    int n = nums.length;
    int[] val = new int[n];
    int[] prev = new int[n];
    int[] next = new int[n];
    boolean[] alive = new boolean[n];
    for (int i = 0; i < n; i++) {
        val[i] = nums[i];
        prev[i] = i - 1;
        next[i] = (i == n - 1) ? -1 : i + 1;
        alive[i] = true;
    }

    // (soma, índiceEsquerdo) — desempate pelo índice menor = par mais à esquerda
    PriorityQueue<int[]> heap = new PriorityQueue<>(
        (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1])
    );

    int badPairs = 0;
    for (int i = 0; i < n - 1; i++) {
        heap.offer(new int[]{val[i] + val[i + 1], i});
        if (val[i] > val[i + 1]) badPairs++;
    }

    int operacoes = 0;
    while (badPairs > 0) {
        int[] topo = heap.poll();
        int l = topo[1];
        int r = next[l];

        // Lazy deletion: o par mudou (vizinho diferente ou soma diferente) desde que foi empilhado.
        if (!alive[l] || r == -1 || !alive[r] || val[l] + val[r] != topo[0]) {
            continue;
        }

        int p = prev[l];
        int novoDireito = next[r];

        // Remove a contribuição em badPairs dos 3 pares que esta fusão vai destruir.
        if (p != -1 && val[p] > val[l]) badPairs--;
        if (val[l] > val[r]) badPairs--;
        if (novoDireito != -1 && val[r] > val[novoDireito]) badPairs--;

        // Funde: l absorve r; r é desligado da lista (não é mais um nó válido).
        val[l] += val[r];
        alive[r] = false;
        next[l] = novoDireito;
        if (novoDireito != -1) prev[novoDireito] = l;

        // Soma a contribuição em badPairs dos (até) 2 pares novos criados pela fusão.
        if (p != -1 && val[p] > val[l]) badPairs++;
        if (novoDireito != -1 && val[l] > val[novoDireito]) badPairs++;

        // Reempilha os pares vizinhos afetados — as entradas antigas ficam obsoletas
        // no heap, mas a checagem de lazy deletion no início do loop cuida delas.
        if (p != -1) heap.offer(new int[]{val[p] + val[l], p});
        if (novoDireito != -1) heap.offer(new int[]{val[l] + val[novoDireito], l});

        operacoes++;
    }

    return operacoes;
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

- **Rescanear o array inteiro para achar `badPairs` do zero a cada operação**: funciona, mas joga fora a otimização inteira — a ideia central é que uma fusão só afeta no máximo 3 pares existentes, então `badPairs` deve ser atualizado incrementalmente, não recalculado.
- **Esquecer o lazy deletion ao tirar do heap**: como o heap não suporta "atualizar prioridade" nativamente, entradas antigas de pares que já mudaram continuam lá — é obrigatório validar (`alive`, vizinhança e soma) antes de usar uma entrada tirada do heap.
- **Desempate errado no heap**: o problema exige o par **mais à esquerda** em caso de soma igual — sem o índice como critério de desempate no comparator, a resposta pode escolher o par errado e contar operações a mais ou a menos.
- **Confundir "menor soma" com "não ordenado"**: a regra de escolha do par a fundir é sempre pela **soma mínima**, independente de o par violar ou não a ordem — só o critério de **parada** depende de estar ordenado (`badPairs == 0`).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já ordenado | `nums = [1,2,2]` | `0` | `badPairs` começa em 0, o loop nem executa |
| Um único elemento | `nums = [5]` | `0` | não há pares adjacentes possíveis; trivialmente "ordenado" |
| Estritamente decrescente | `nums = [3,2,1]` | precisa fundir até restar 1 elemento | testa fusões em cadeia até não sobrar nenhum par ruim |
| Empate de soma, desempate à esquerda | `nums = [1,3,3,1]` (pares (1,3)=4 e (3,1)=4 empatam) | escolhe o par mais à esquerda primeiro | valida o critério de desempate do comparator |
| Exemplo do enunciado | `nums = [5,2,3,1]` | `2` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[3506] Minimum Pair Removal to Sort Array II** (mesmo problema, mas com `n` até 10^5 — exige exatamente a técnica heap + lista encadeada + lazy deletion apresentada aqui, e não passa com a força bruta O(n²)), **[1046] Last Stone Weight** (mesmo padrão de "sempre processe o par mais urgente agora" com heap, sem a restrição de adjacência)
- No backend: "sempre combine os dois itens mais baratos/urgentes adjacentes, repita até estabilizar" aparece em **compactação de séries temporais** (mesclar buckets adjacentes de baixa granularidade) e em **algoritmos de codificação de Huffman** (que usa a mesma ideia de heap, mas sem a restrição de adjacência) — o padrão geral de "heap + lazy deletion para invalidar entradas obsoletas" é o mesmo usado em filas de prioridade de escalonadores reais.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
