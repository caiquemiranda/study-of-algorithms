# [0448] Find All Numbers Disappeared in an Array

> 🔗 [LeetCode 448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#CyclicSort` `#Easy`

## 📜 O Problema

Dado um array `nums` com `n` inteiros, onde `nums[i]` está no intervalo `[1, n]`, retorne **um array com todos os inteiros do intervalo `[1, n]` que não aparecem em `nums`**.

**Exemplos:**
```
Input:  nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input:  nums = [1,1]
Output: [2]
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^5` → precisa de O(n), não O(n²)
- `1 <= nums[i] <= n` → cada valor cabe como índice válido (1-based) dentro do próprio array — isso habilita o truque de "usar o array como hash table", sem estrutura extra
- Follow-up pede O(n) tempo e O(1) espaço extra (sem contar a lista de saída) → sinaliza que existe um truque in-place além do hash set óbvio

## 🧭 Como reconhecer o padrão

"Range `[1,n]` e array de tamanho `n`" é a assinatura clássica do truque de "usar o próprio array como hash table" (marcação de sinal), porque cada valor de 1 a n mapeia para exatamente um índice de 0 a n-1.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Um hash set com todos os números de 1 a n; remova cada `nums[i]` do set. O que sobrar no set são os números ausentes.

- Tempo: O(n) · Espaço: O(n) por causa do hash set
- **Por que não basta:** não viola a restrição de tempo, mas o follow-up pede resolver sem espaço extra, e o hash set gasta memória desnecessária quando o próprio array pode ser reaproveitado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada valor `v = nums[i]`, marque a posição `v-1` como "visitada" negando o valor que está lá (se ainda for positivo). No final, os índices que continuam positivos são os números que nunca apareceram (`índice + 1`).

## 🎬 Exemplo passo a passo

`nums = [4,3,2,7,8,2,3,1]`

| Passo | i | valor lido (abs) | índice marcado | nums antes | nums depois |
|---|---|---|---|---|---|
| 1 | 0 | 4 | 3 | nums[3]=7 | nums[3]=-7 |
| 2 | 1 | 3 | 2 | nums[2]=2 | nums[2]=-2 |
| 3 | 2 | 2 | 1 | nums[1]=3 | nums[1]=-3 |
| 4 | 3 | 7 | 6 | nums[6]=3 | nums[6]=-3 |
| 5 | 4 | 8 | 7 | nums[7]=1 | nums[7]=-1 |
| 6 | 5 | 2 | 1 | nums[1]=-3 (já negativo) | sem mudança |
| 7 | 6 | 3 | 2 | nums[2]=-2 (já negativo) | sem mudança |
| 8 | 7 | 1 | 0 | nums[0]=4 | nums[0]=-4 |

Array final: `[-4,-3,-2,-7,8,2,-3,-1]`. Índices ainda positivos: 4 (valor 8) e 5 (valor 2) → números ausentes = `[5, 6]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas simples pelo array
- **Espaço:** O(1) extra — a lista de saída não conta como espaço extra, conforme o próprio enunciado do follow-up

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> findDisappearedNumbers(int[] nums) {
    int n = nums.length;
    // fase 1: usa o sinal de nums[idx] para marcar "o valor (idx+1) já apareceu"
    for (int i = 0; i < n; i++) {
        int idx = Math.abs(nums[i]) - 1; // valor v aponta para o índice v-1
        if (nums[idx] > 0) {
            nums[idx] = -nums[idx]; // marca como visto, sem perder o valor original (abs recupera depois)
        }
    }

    List<Integer> ausentes = new ArrayList<>();
    // fase 2: índice ainda positivo nunca foi "apontado" por nenhum valor -> (idx+1) está ausente
    for (int i = 0; i < n; i++) {
        if (nums[i] > 0) {
            ausentes.add(i + 1);
        }
    }
    return ausentes;
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

- Esquecer de usar `Math.abs()` ao ler `nums[i]` na fase 1 — depois que um valor é negado, lê-lo de novo sem `abs` dá índice negativo e `ArrayIndexOutOfBoundsException`.
- Negar a mesma posição duas vezes sem checar se já é negativa — não quebra a lógica (a checagem `> 0` já evita isso), mas negar de novo inverteria o sinal errado.
- Esquecer de restaurar o array se um caller externo esperasse os valores originais depois — aqui não é exigido, mas é uma pegadinha comum em variações do problema.
- Duplicatas no array (ex.: `[1,1]`) são esperadas e não quebram o algoritmo — várias ocorrências do mesmo valor só marcam a mesma posição repetidamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo do enunciado | `[4,3,2,7,8,2,3,1]` | `[5,6]` | caso padrão com duplicatas |
| Todos presentes | `[1,2,3]` | `[]` | nenhum índice fica positivo |
| Todos iguais | `[1,1]` | `[2]` | número 2 nunca é apontado |
| Um elemento | `[1]` | `[]` | menor entrada possível |

## 🔗 Conexões

- Problemas irmãos: [0041] First Missing Positive (mesma técnica de índice-como-hash, versão mais difícil), [0287] Find the Duplicate Number (mesma ideia de usar o array como estrutura de marcação)
- No backend: detectar IDs ausentes numa sequência esperada (ex.: números de fatura ou pedido que deveriam ser contíguos), útil para auditoria de dados sem gastar memória extra numa varredura de milhões de registros.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
