# [2367] Number of Arithmetic Triplets

> 🔗 [LeetCode 2367](https://leetcode.com/problems/number-of-arithmetic-triplets/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums` **estritamente crescente** (0-indexado) e um inteiro positivo `diff`, uma tripla `(i, j, k)` é **aritmética** se `i < j < k`, `nums[j] - nums[i] == diff` e `nums[k] - nums[j] == diff`. Retorne a quantidade de triplas aritméticas.

**Exemplos:**
```
Input:  nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explicação: (1,2,4) e (2,4,5).

Input:  nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explicação: (0,2,4) e (1,3,5).
```

**Restrições (e o que elas denunciam):**
- `3 <= nums.length <= 200` → O(n²) ou até O(n³) ingênuo já passaria, mas O(n) é alcançável
- `nums` estritamente crescente → cada valor tem posição única e previsível; não há empates nem repetição a tratar
- `0 <= nums[i] <= 200`, `1 <= diff <= 50` → os alvos (`nums[i]+diff`, `nums[i]+2·diff`) crescem junto com `i`, o que permite ponteiros que só avançam

## 🧭 Como reconhecer o padrão

"Encontrar triplas com uma relação fixa de valores num array ordenado" é resolvido com ponteiros que avançam **junto**, nunca recuando: como `nums` é estritamente crescente, à medida que `i` avança, os valores-alvo que `j` e `k` precisam alcançar só crescem — então os três ponteiros (`i`, `j`, `k`) percorrem o array uma única vez, no total.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Três loops aninhados testando todo trio `i < j < k` e checando diretamente as duas condições de diferença.

- Tempo: O(n³) · Espaço: O(1)
- **Por que não basta:** testa combinações que nunca poderiam servir — fixados `i` e `j`, `k` só pode ser um único valor possível (`nums[i] + 2·diff`); não há motivo pra testar TODOS os `k`, muito menos todos os pares `(i,j)` sem aproveitar a ordenação.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada `i`, avance `j` até `nums[j]` alcançar (ou passar) o alvo `nums[i] + diff`; se bater exatamente, avance `k` até alcançar `nums[i] + 2·diff` e confirme igualdade. Como os alvos só crescem conforme `i` cresce, `j` e `k` nunca precisam voltar — eles continuam de onde pararam na iteração anterior, dando uma varredura total O(n) para os três ponteiros juntos.

## 🎬 Exemplo passo a passo

`nums = [0,1,4,6,7,10]`, `diff = 3`

| i | nums[i] | j encontrado | nums[j] | k encontrado | nums[k] | Tripla válida? |
|---|---|---|---|---|---|---|
| 0 | 0 | 2 | 4 | — | — | não (`nums[j] ≠ 0+3`) |
| 1 | 1 | 2 | 4 | 4 | 7 | sim → **(1,2,4)** |
| 2 | 4 | 4 | 7 | 5 | 10 | sim → **(2,4,5)** |
| 3 | 6 | 5 | 10 | — | — | não (`nums[j] ≠ 6+3=9`) |
| 4 | 7 | 5 | 10 | — | — | não (`k` sai dos limites) |
| 5 | 10 | — | — | — | — | não (`j` sai dos limites) |

Contagem final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — juntos, os três ponteiros percorrem o array no máximo uma vez cada
- **Espaço:** O(1) — só os índices `i`, `j`, `k` e o contador

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int arithmeticTriplets(int[] nums, int diff) {
    int n = nums.length;
    int count = 0;
    int j = 0;
    int k = 0;

    for (int i = 0; i < n; i++) {
        if (j <= i) {
            j = i + 1;
        }
        while (j < n && nums[j] < nums[i] + diff) {
            j++;
        }
        if (j >= n || nums[j] != nums[i] + diff) {
            continue; // não existe segundo elemento com a diferença certa
        }

        if (k <= j) {
            k = j + 1;
        }
        while (k < n && nums[k] < nums[i] + 2 * diff) {
            k++;
        }
        if (k < n && nums[k] == nums[i] + 2 * diff) {
            count++;
        }
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

- Deixar `j` e `k` reiniciarem do zero a cada novo `i` — como `nums` é estritamente crescente, os alvos só CRESCEM conforme `i` cresce; os ponteiros nunca precisam voltar, só avançar.
- Esquecer de checar `j >= n` (ou `k >= n`) antes de acessar `nums[j]`/`nums[k]` — sem essa checagem, o ponteiro pode ultrapassar o array procurando um valor que não existe.
- Confundir "avançou até um valor maior ou igual ao alvo" com "encontrou o alvo" — o `while` para em `nums[j] >= alvo`, mas é preciso confirmar com `==` depois, porque `nums[j]` pode ter passado direto do alvo sem nunca bater exatamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Dois triplets | `nums=[0,1,4,6,7,10]`, `diff=3` | 2 | (1,2,4) e (2,4,5) |
| Progressão aritmética completa | `nums=[4,5,6,7,8,9]`, `diff=2` | 2 | (0,2,4) e (1,3,5) |
| Nenhum triplet | `nums=[0,1,2]`, `diff=100` | 0 | diff grande demais para caber no array |
| Tamanho mínimo, único triplet possível | `nums=[1,2,3]`, `diff=1` | 1 | i=0, j=1, k=2 é o único candidato |

## 🔗 Conexões

- Problemas irmãos: [0015] 3Sum (mesma família de encontrar triplas com uma relação específica entre valores, usando ponteiros sobre um array ordenado), [1099] Two Sum Less Than K (mesma ideia de explorar a ordenação pra evitar busca exaustiva)
- No backend: detectar padrões de progressão regular em séries temporais ordenadas — por exemplo, encontrar três leituras de sensor igualmente espaçadas por um intervalo fixo, aproveitando que os dados já chegam ordenados por timestamp.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
