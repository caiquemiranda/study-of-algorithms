# [0414] Third Maximum Number

> 🔗 [LeetCode 414](https://leetcode.com/problems/third-maximum-number/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums`, retorne o **terceiro maior valor distinto**. Se ele não existir (menos de 3 valores distintos), retorne o **maior** valor.

**Exemplos:**
```
Input:  nums = [3,2,1]   Output: 1  (1º=3, 2º=2, 3º=1)
Input:  nums = [1,2]     Output: 2  (só 2 distintos: não há 3º, retorna o máximo)
Input:  nums = [2,2,3,1] Output: 1  (os dois 2's contam como um só valor distinto)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → qualquer O(n log n) passa fácil, mas o **follow-up pede O(n)** — é o gatilho para a versão de uma passada só
- `-2^31 <= nums[i] <= 2^31 - 1` → os valores ocupam a faixa inteira de `int`; isso significa que você **não pode usar `Integer.MIN_VALUE` como "sentinela de vazio"** sem cuidado, porque ele pode ser um valor real do array
- "duplicatas contam como um só valor distinto" → a palavra-chave é **distinto**; ela é o motivo de precisarmos rastrear "já vi este valor?" e não só "quantos números processei"

## 🧭 Como reconhecer o padrão

"Os K maiores/menores elementos" com K **pequeno e fixo** (aqui K=3) é o irmão mais simples da família Top-K — não precisa de heap: basta manter K variáveis rastreando os K melhores vistos até agora, atualizadas em uma única passada.

## 🐢 Solução 1 — Força bruta

Ordenar o array em ordem decrescente, remover duplicatas, e verificar se sobrou pelo menos 3 elementos distintos.

- Tempo: O(n log n) — dominado pela ordenação · Espaço: O(n) para a lista sem duplicatas
- **Por que não é a ótima:** já é uma solução boa e aceitável, mas o problema tem um follow-up explícito pedindo O(n) — dá para resolver sem ordenar nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha três variáveis — `primeiro`, `segundo`, `terceiro` — representando os três maiores valores **distintos** vistos até agora, inicializadas com "vazio" (usando `Long.MIN_VALUE` como sentinela, já que os valores do array cabem em `int` mas não necessariamente em todo o intervalo de `long`). Para cada número: se ele já é igual a um dos três, ignore (não é um novo distinto); senão, "empurre" os maiores para baixo conforme necessário.

## 🎬 Exemplo passo a passo

`nums = [2, 2, 3, 1]`

| num | já é igual a 1º/2º/3º? | Ação | primeiro | segundo | terceiro |
|---|---|---|---|---|---|
| início | — | — | -∞ | -∞ | -∞ |
| 2 | não | 2 > -∞: vira o novo 1º (empurra os outros) | 2 | -∞ | -∞ |
| 2 | **sim** (igual ao 1º) | ignora, não é distinto | 2 | -∞ | -∞ |
| 3 | não | 3 > 2: vira o novo 1º (2 desce para 2º) | 3 | 2 | -∞ |
| 1 | não | 1 não é maior que 3 nem 2, mas é maior que -∞: vira o 3º | 3 | 2 | 1 |

`terceiro` não é mais o sentinela (-∞) → retorna **1** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelo array, com no máximo 3 comparações por elemento
- **Espaço:** O(1) — apenas três variáveis, independente do tamanho de `nums`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int thirdMax(int[] nums) {
    // usa Long para o sentinela: valores de nums cabem em int, então Long.MIN_VALUE
    // nunca é confundido com um valor real do array (diferente de usar Integer.MIN_VALUE)
    long primeiro = Long.MIN_VALUE, segundo = Long.MIN_VALUE, terceiro = Long.MIN_VALUE;

    for (int n : nums) {
        if (n == primeiro || n == segundo || n == terceiro) {
            continue; // não é um valor NOVO e distinto: ignora (a regra chave do problema)
        }
        if (n > primeiro) {
            terceiro = segundo; segundo = primeiro; primeiro = n;   // empurra os dois para baixo
        } else if (n > segundo) {
            terceiro = segundo; segundo = n;                        // empurra só o terceiro
        } else if (n > terceiro) {
            terceiro = n;                                           // só entra na 3ª posição
        }
    }

    // se 'terceiro' nunca foi preenchido, não existem 3 distintos: cai para o maior
    return (terceiro == Long.MIN_VALUE) ? (int) primeiro : (int) terceiro;
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

- Usar `Integer.MIN_VALUE` (em vez de `Long.MIN_VALUE`) como sentinela de "vazio" — se o array **realmente contiver** `Integer.MIN_VALUE`, o algoritmo não consegue distinguir "ainda vazio" de "o valor real é esse".
- Esquecer o `continue` para valores **repetidos** — sem ele, `[1,1,1]` seria tratado como se tivesse 3 distintos (quando na verdade só existe o valor 1, e a resposta correta é o próprio 1 como máximo).
- Ordem das comparações: checar `n > segundo` **antes** de checar `n > primeiro` faria um número grande nunca chegar à primeira posição — a ordem decrescente de checagem (primeiro → segundo → terceiro) é essencial.
- **Java**: fazer o cast `(int) primeiro` só é seguro porque sabemos que, se `primeiro` não é mais o sentinela, ele veio de um `int` do array original — não faça isso com valores realmente fora do range de `int`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só 2 distintos | `[1,2]` | 2 | não existe 3º, cai para o máximo |
| Exatamente 3 distintos | `[3,2,1]` | 1 | caso simples do enunciado |
| Com duplicatas | `[2,2,3,1]` | 1 | duplicata não conta como novo distinto |
| Todos iguais | `[5,5,5]` | 5 | só 1 distinto, cai para o máximo (que é o próprio valor) |
| Valor extremo | `[Integer.MIN_VALUE]` | Integer.MIN_VALUE | prova que o sentinela `long` não confunde este caso |

## 🔗 Conexões

- Problemas irmãos: **[0215] Kth Largest Element in an Array** (a versão generalizada para K qualquer, geralmente resolvida com heap — ver [09_heap_priority_queue](../../../fundamentos/09_heap_priority_queue.md)), **[0169] Majority Element** (outro problema de "rastrear o(s) candidato(s) certo(s) em uma passada")
- No backend: manter os "top 3 endpoints mais lentos" em um dashboard leve (sem heap, quando K é fixo e pequeno) ou rastrear os últimos N valores extremos de uma métrica em tempo real usa exatamente esta técnica de variáveis fixas em vez de estrutura de dados completa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
