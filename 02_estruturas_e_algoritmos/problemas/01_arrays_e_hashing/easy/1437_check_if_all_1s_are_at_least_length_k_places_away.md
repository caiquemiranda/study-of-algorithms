# [1437] Check If All 1's Are at Least Length K Places Away

> 🔗 [LeetCode 1437](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array binário `nums` e um inteiro `k`, retorne `true` se todos os `1`s estão a pelo menos `k` posições de distância uns dos outros; caso contrário, retorne `false`.

**Exemplos:**
```
Input:  nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explicação: cada um dos 1s está a pelo menos 2 posições de distância dos outros.

Input:  nums = [1,0,0,1,0,1], k = 2
Output: false
Explicação: o segundo e o terceiro 1 estão a apenas uma posição de distância.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n) esperado
- `0 <= k <= nums.length` → k pode ser 0 (sem restrição nenhuma de distância, sempre válido)
- `nums[i]` é 0 ou 1 → só dois valores possíveis

## 🧭 Como reconhecer o padrão

"Todos os elementos especiais (aqui, os 1s) precisam estar a pelo menos K posições de distância uns dos outros" é resolvido rastreando o ÍNDICE do último 1 visto, e a cada novo 1 encontrado, verificando se a distância até o anterior é suficiente — sem precisar comparar TODOS os pares de 1s entre si.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Coletar todos os índices onde `nums[i] == 1` numa lista, e depois comparar CADA PAR de índices consecutivos na lista, verificando se a diferença é >= k+1.

- Tempo: O(n) — na prática já é O(n) para coletar + O(m) para comparar pares (m = número de 1s) · Espaço: O(m) para a lista de índices
- **Por que não basta:** não é pior em complexidade, mas gasta espaço O(m) desnecessário guardando todos os índices, quando só o ÚLTIMO índice de 1 visto precisa ser lembrado a cada momento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array mantendo `indiceUltimoUm` (inicializado em um sentinela, como `-1`). Toda vez que encontrar um `1` na posição `i`, verifique se `i - indiceUltimoUm - 1 >= k` (a quantidade de posições ENTRE os dois 1s); se não for, retorne `false` na hora. Atualize `indiceUltimoUm = i`.

## 🎬 Exemplo passo a passo

`nums = [1,0,0,1,0,1]`, `k = 2`

| Passo | i | nums[i] | indiceUltimoUm (antes) | distância (i - anterior - 1) | válido (>= k)? | indiceUltimoUm (depois) |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | -1 (sentinela) | (primeiro 1, sem checagem) | — | 0 |
| 2 | 3 | 1 | 0 | 3-0-1=2 | sim (2>=2) | 3 |
| 3 | 5 | 1 | 3 | 5-3-1=1 | **não** (1<2) | — |

Resultado final: `false` ✔ (o segundo e o terceiro 1 estão a só 1 posição de distância, menos que k=2)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada, com possível saída antecipada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean kLengthApart(int[] nums, int k) {
    int indiceUltimoUm = -1; // -1 significa "ainda não vimos nenhum 1"

    for (int i = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            if (indiceUltimoUm != -1 && i - indiceUltimoUm - 1 < k) {
                return false; // 1s muito próximos, distância insuficiente
            }
            indiceUltimoUm = i; // atualiza para o índice do 1 mais recente
        }
    }
    return true;
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

- Não tratar o caso do PRIMEIRO 1 encontrado — não há "1 anterior" para comparar, então a checagem de distância deve ser pulada nessa primeira ocorrência (usar um sentinela como `-1` resolve isso naturalmente).
- Confundir "distância entre índices" com "número de posições ENTRE os 1s" — a fórmula correta é `i - indiceAnterior - 1` (subtrai 1 porque a distância entre índices já conta as duas posições dos próprios 1s, que não fazem parte do "espaço vazio" entre eles).
- Esquecer que `k = 0` sempre resulta em `true` — sem nenhuma restrição de distância, dois 1s podem até ser adjacentes; o código já lida com isso naturalmente (`distância < 0` nunca acontece, já que o mínimo é 0 para 1s adjacentes).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Distâncias suficientes | `nums=[1,0,0,0,1,0,0,1], k=2` | true | todos os 1s têm pelo menos 2 posições de distância |
| Distância insuficiente | `nums=[1,0,0,1,0,1], k=2` | false | o segundo e terceiro 1 estão muito próximos |
| Sem restrição (k=0) | `nums=[1,1,1], k=0` | true | k=0 permite 1s adjacentes |
| Um único 1 | `nums=[0,0,1,0,0], k=100` | true | sem outro 1 para comparar, sempre válido |

## 🔗 Conexões

- Problemas irmãos: [0485] Max Consecutive Ones (mesmo domínio de rastrear posições de 1s numa passada), [0605] Can Place Flowers (mesma ideia de verificar espaçamento mínimo entre elementos especiais)
- No backend: validação de restrições de espaçamento em agendamento (ex.: garantir que duas tarefas do mesmo tipo não sejam agendadas com menos de K minutos de intervalo, ou que sensores de eventos não disparem com muita frequência).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
