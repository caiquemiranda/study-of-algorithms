# [0581] Shortest Unsorted Continuous Subarray

> 🔗 [LeetCode 581](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Array`

## 📜 O Problema

Dado um array de inteiros `nums`, encontre um **subarray contínuo** tal que, se você ordenar só esse subarray em ordem não-decrescente, o array inteiro fica ordenado. Retorne o **comprimento** do menor subarray com essa propriedade.

**Exemplos:**
```
Input:  nums = [2,6,4,8,10,9,15]
Output: 5
Explicação: ordenando [6,4,8,10,9] o array inteiro fica ordenado.

Input:  nums = [1,2,3,4]
Output: 0

Input:  nums = [1]
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → o follow-up pede O(n), sinalizando que existe solução linear além da abordagem óbvia de ordenar (O(n log n))
- `-10^5 <= nums[i] <= 10^5` → valores dentro de faixa razoável, sem necessidade de tratamento especial de overflow

## 🧭 Como reconhecer o padrão

"Encontrar os limites (esquerda e direita) de uma região que **viola** a ordem crescente esperada" é resolvido com **duas pilhas monotônicas**: uma passada da esquerda para a direita com pilha crescente identifica o limite **direito** (o índice mais à direita que precisa se mover porque é menor que algo à sua esquerda), e uma passada da direita para a esquerda com pilha decrescente identifica o limite **esquerdo** (o índice mais à esquerda que precisa se mover porque é maior que algo à sua direita).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Criar uma cópia ordenada de `nums`, comparar elemento a elemento com o original, encontrando o primeiro e o último índice onde os dois arrays divergem.

- Tempo: O(n log n) (dominado pela ordenação) · Espaço: O(n) para a cópia
- **Por que não basta:** essa solução já é bastante boa e passa nos limites do problema, mas o enunciado explicitamente pergunta no follow-up se é possível resolver em O(n) — ordenar sempre paga um custo O(n log n) que pode ser evitado com uma abordagem baseada em monotonic stack.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use duas pilhas monotônicas de **índices** para encontrar os limites da região desordenada:

1. **Passada esquerda→direita** (pilha crescente): sempre que `nums[i]` for **menor** que o valor no topo da pilha, isso significa que todos os índices desempilhados (que são maiores que `nums[i]`, mas vieram antes dele) estão fora de ordem — atualize `esquerda = min(esquerda, índice_desempilhado)`.
2. **Passada direita→esquerda** (pilha decrescente): sempre que `nums[i]` for **maior** que o valor no topo da pilha, os índices desempilhados estão fora de ordem — atualize `direita = max(direita, índice_desempilhado)`.

No final, se nenhum índice foi marcado (`direita` nunca mudou), o array já está ordenado, retorne 0. Caso contrário, a resposta é `direita - esquerda + 1`.

## 🎬 Exemplo passo a passo

`nums = [2,6,4,8,10,9,15]`

**Passada esquerda→direita (pilha crescente de índices, encontra `esquerda`):**

| i | nums[i] | Ação do while (pop se topo > atual) | Pilha após | esquerda após |
|---|---|---|---|---|
| 0 | 2 | pilha vazia | `[0]` | ∞ (nada ainda) |
| 1 | 6 | `2<=6`, não remove | `[0,1]` | ∞ |
| 2 | 4 | `6>4` → pop idx1, esquerda=min(∞,1)=1 | `[0,2]` | 1 |
| 3 | 8 | `4<=8`, não remove | `[0,2,3]` | 1 |
| 4 | 10 | não remove | `[0,2,3,4]` | 1 |
| 5 | 9 | `10>9` → pop idx4, esquerda=min(1,4)=1 | `[0,2,3,5]` | 1 |
| 6 | 15 | não remove | `[0,2,3,5,6]` | 1 |

**Passada direita→esquerda (pilha decrescente de índices, encontra `direita`):**

| i | nums[i] | Ação do while (pop se topo < atual) | direita após |
|---|---|---|---|
| 6 | 15 | pilha vazia | -1 |
| 5 | 9 | 15>9, não remove | -1 |
| 4 | 10 | 9<10 → pop idx5, direita=max(-1,5)=5 | 5 |
| 3 | 8 | não remove | 5 |
| 2 | 4 | não remove | 5 |
| 1 | 6 | não remove | 5 |
| 0 | 2 | não remove | 5 |

`esquerda=1`, `direita=5` → comprimento `5-1+1=5`

Resultado final: `5` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas lineares, cada uma com uma pilha onde cada índice é empilhado e desempilhado no máximo uma vez
- **Espaço:** O(n) — as duas pilhas guardam no máximo todos os índices

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findUnsortedSubarray(int[] nums) {
    int n = nums.length;
    int esquerda = n, direita = -1;

    // passada esquerda -> direita: pilha crescente encontra o limite DIREITO
    Deque<Integer> pilhaCres = new ArrayDeque<>();
    for (int i = 0; i < n; i++) {
        while (!pilhaCres.isEmpty() && nums[pilhaCres.peek()] > nums[i]) {
            esquerda = Math.min(esquerda, pilhaCres.pop());
        }
        pilhaCres.push(i);
    }

    // passada direita -> esquerda: pilha decrescente encontra o limite ESQUERDO
    Deque<Integer> pilhaDecr = new ArrayDeque<>();
    for (int i = n - 1; i >= 0; i--) {
        while (!pilhaDecr.isEmpty() && nums[pilhaDecr.peek()] < nums[i]) {
            direita = Math.max(direita, pilhaDecr.pop());
        }
        pilhaDecr.push(i);
    }

    return direita == -1 ? 0 : direita - esquerda + 1;
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

- Confundir qual pilha determina qual limite — a pilha **crescente** (esquerda→direita) encontra o limite **direito** (índices que precisam se mover para a direita ficando "presos" atrás de valores maiores), e a pilha **decrescente** (direita→esquerda) encontra o limite **esquerdo**; inverter os papéis quebra o resultado.
- Esquecer o caso "já ordenado" — se `direita` nunca for atualizado (continua `-1`), a resposta correta é `0`, não `-1 - esquerda + 1` (que daria um número negativo sem sentido).
- Usar `>=`/`<=` em vez de `>`/`<` nas condições do while — elementos **iguais** não violam a ordem não-decrescente, então não devem disparar atualização dos limites.
- Achar que essa é a única solução O(n) — existe também uma solução com duas passadas simples rastreando `max` (esquerda→direita) e `min` (direita→esquerda) sem pilha nenhuma, com O(1) de espaço extra; a versão com pilha aqui foi escolhida por consistência com a categoria, mas vale saber que a alternativa sem pilha existe e usa menos memória.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já ordenado | `[1,2,3,4]` | 0 | nenhuma pilha desempilha nada, `direita` fica -1 |
| Único elemento | `[1]` | 0 | trivialmente ordenado, sem nada a comparar |
| Totalmente desordenado (decrescente) | `[5,4,3,2,1]` | 5 | o array inteiro precisa ser reordenado |
| Desordem só no meio | `[2,6,4,8,10,9,15]` | 5 | caso do enunciado, testa os limites exatos da região afetada |

## 🔗 Conexões

- Problemas irmãos: [0769] Max Chunks To Make Sorted (mesma ideia de identificar regiões que precisam ser processadas juntas para alcançar ordenação), [0496] Next Greater Element I (mesma técnica de monotonic stack aplicada a uma pergunta diferente)
- No backend: identificar a menor região de um conjunto de dados que precisa ser reprocessada para restaurar uma invariante de ordenação aparece em sistemas de cache invalidation parcial (só invalidar/reordenar o trecho afetado por uma mudança, não o dataset inteiro) e em otimização de índices de banco de dados após inserções fora de ordem.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
