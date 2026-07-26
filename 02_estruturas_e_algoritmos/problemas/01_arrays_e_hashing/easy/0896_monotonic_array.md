# [0896] Monotonic Array

> 🔗 [LeetCode 896](https://leetcode.com/problems/monotonic-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Um array é **monotônico** se é monotone crescente ou monotone decrescente. Um array `nums` é monotone crescente se para todo `i <= j`, `nums[i] <= nums[j]`. É monotone decrescente se para todo `i <= j`, `nums[i] >= nums[j]`.

Dado um array de inteiros `nums`, retorne `true` se o array é monotônico, ou `false` caso contrário.

**Exemplos:**
```
Input:  nums = [1,2,2,3]
Output: true

Input:  nums = [6,5,4,4]
Output: true

Input:  nums = [1,3,2]
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → precisa O(n)
- `-10^5 <= nums[i] <= 10^5` → sem risco de overflow em comparações

## 🧭 Como reconhecer o padrão

"Verificar se o array segue uma ordem" é sempre resolvido rastreando duas possibilidades em paralelo (é crescente? é decrescente?) numa única passada, e checando no final se pelo menos uma delas se manteve verdadeira o tempo todo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Verificar separadamente, em duas passadas completas, se o array é inteiramente crescente E, se não for, se é inteiramente decrescente.

- Tempo: O(n) — já é linear (duas passadas independentes), mas percorre o array duas vezes no pior caso · Espaço: O(1)
- **Por que não basta:** tecnicamente já é O(n), mas dá pra decidir as duas possibilidades numa única passada, mantendo duas flags booleanas simultaneamente em vez de dois loops separados.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha duas flags, `crescente` e `decrescente`, ambas começando `true`. Percorra o array comparando pares adjacentes: se `nums[i] > nums[i-1]`, `decrescente` vira `false`; se `nums[i] < nums[i-1]`, `crescente` vira `false`. No final, o array é monotônico se `crescente || decrescente`.

## 🎬 Exemplo passo a passo

`nums = [1,3,2]`

| Passo | i | nums[i] | nums[i-1] | comparação | crescente | decrescente |
|---|---|---|---|---|---|---|
| 0 | — | — | — | (início) | true | true |
| 1 | 1 | 3 | 1 | 3>1 | true | false (quebrou decrescente) |
| 2 | 2 | 2 | 3 | 2<3 | false (quebrou crescente) | false |

Resultado final: `crescente(false) || decrescente(false) = false` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) — duas flags booleanas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isMonotonic(int[] nums) {
    boolean crescente = true;
    boolean decrescente = true;

    for (int i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            decrescente = false; // encontrou uma subida, não pode mais ser (não-estritamente) decrescente
        }
        if (nums[i] < nums[i - 1]) {
            crescente = false; // encontrou uma descida, não pode mais ser (não-estritamente) crescente
        }
    }
    return crescente || decrescente;
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

- Usar comparação estrita (`<`, `>`) em vez de permitir igualdade — o enunciado define monotonicidade com `<=` e `>=` (não-decrescente / não-crescente), então elementos repetidos (`[1,1,2]`) ainda são válidos.
- Fazer duas passadas separadas (uma para cada direção) em vez de manter as duas flags na mesma passada — funciona, mas processa o array duas vezes desnecessariamente.
- Esquecer o caso de array constante (`[5,5,5]`) — ele satisfaz TANTO crescente quanto decrescente simultaneamente, o que é o comportamento correto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Crescente com repetição | `[1,2,2,3]` | true | não-decrescente, repetição é permitida |
| Decrescente com repetição | `[6,5,4,4]` | true | não-crescente, repetição é permitida |
| Nem crescente nem decrescente | `[1,3,2]` | false | sobe e depois desce |
| Array constante | `[5,5,5]` | true | satisfaz ambas as direções ao mesmo tempo |

## 🔗 Conexões

- Problemas irmãos: [0674] Longest Continuous Increasing Subsequence (mesmo domínio de comparação de vizinhos), [0941] Valid Mountain Array (também valida uma "forma" específica do array numa única passada, mas exigindo subida seguida de descida)
- No backend: validação de séries temporais monotônicas (ex.: garantir que um timestamp de log ou um contador de versão nunca decresce, ou que uma métrica é consistentemente não-decrescente antes de aceitar os dados).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
