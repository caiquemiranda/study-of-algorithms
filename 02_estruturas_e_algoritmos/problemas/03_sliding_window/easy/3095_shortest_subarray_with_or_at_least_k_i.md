# [3095] Shortest Subarray With OR at Least K I

> 🔗 [LeetCode 3095](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#BitManipulation` `#Easy`

## 📜 O Problema

Dado um array `nums` de inteiros **não negativos** e um inteiro `k`, um array é **especial** se o **OR bit a bit** de todos os seus elementos é **pelo menos** `k`. Retorne o comprimento do menor subarray **não vazio** especial de `nums`, ou `-1` se não existir nenhum.

**Exemplos:**
```
Input:  nums = [1,2,3], k = 2
Output: 1
Explicação: o subarray [3] tem OR = 3 >= 2.

Input:  nums = [2,1,8], k = 10
Output: 3
Explicação: o subarray [2,1,8] tem OR = 11 >= 10.

Input:  nums = [1,2], k = 0
Output: 1
Explicação: o subarray [1] já tem OR = 1 >= 0.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 50`, `0 <= nums[i] <= 50` → valores pequenos, cabem em poucos bits (até 6 bits, já que `50 < 64`)
- `0 <= k < 64` → o alvo também cabe em poucos bits; entrada pequena permite até força bruta O(n²), mas a técnica de janela com contagem de bits é a que generaliza para entradas maiores (ver a versão II deste problema)

## 🧭 Como reconhecer o padrão

"Menor subarray cujo OR bit a bit atinge um valor mínimo" parece pedir uma janela que encolhe pela esquerda enquanto a condição se mantém — só que o OR não é "reversível" como uma soma: remover um elemento não desliga automaticamente os bits que ele contribuiu, porque outro elemento da janela pode ter o mesmo bit ligado. A saída é manter, para cada um dos bits, **quantos** elementos da janela o têm ligado — um bit só desliga quando essa contagem chega a zero.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada início `left`, expandir `right` acumulando o OR do zero a cada subarray e verificando se já atingiu `k`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** funciona para `n <= 50`, mas não aproveita que, ao encolher a janela pela esquerda, só é preciso saber se algum bit "sumiu" da janela — sem isso, não dá pra transformar o algoritmo num único ponteiro duplo O(n) para entradas maiores.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um array `bitCount[32]` com quantos elementos da janela atual têm cada bit ligado, e um inteiro `orValue` com o OR atual da janela. Ao expandir `right`, faça OR de `nums[right]` em `orValue` e incremente os `bitCount` dos bits dele. Enquanto `orValue >= k`, registre o comprimento da janela como candidato e encolha pela esquerda: para cada bit de `nums[left]`, decremente `bitCount`; se algum contador chegar a zero, desligue esse bit em `orValue` (nenhum elemento restante o contribui mais).

## 🎬 Exemplo passo a passo

`nums = [1,2,3]`, `k = 2`

| Evento | orValue | Janela [left,right] | comprimento | ≥ k? | melhor |
|---|---|---|---|---|---|
| right=0: inclui nums[0]=1 | 1 | [0,0] | 1 | não | — |
| right=1: inclui nums[1]=2 | 3 | [0,1] | 2 | sim | 2 |
| encolhe: remove nums[0]=1 | 2 | [1,1] | 1 | sim | 1 |
| encolhe: remove nums[1]=2 | 0 | [2,1] (vazia) | — | não | 1 |
| right=2: inclui nums[2]=3 | 3 | [2,2] | 1 | sim | 1 (empate) |
| encolhe: remove nums[2]=3 | 0 | [3,2] (vazia) | — | não | 1 |

Resultado final: `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n · 32) = O(n) — cada elemento entra e sai da janela no máximo uma vez; cada entrada/saída processa até 32 bits
- **Espaço:** O(32) = O(1) — o array de contagem de bits

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumSubarrayLength(int[] nums, int k) {
    int n = nums.length;
    int[] bitCount = new int[32];
    int orValue = 0;
    int left = 0;
    int minLen = Integer.MAX_VALUE;

    for (int right = 0; right < n; right++) {
        orValue |= nums[right];
        addBits(bitCount, nums[right]);

        while (orValue >= k) {
            minLen = Math.min(minLen, right - left + 1);
            orValue = removeBits(bitCount, orValue, nums[left]);
            left++;
        }
    }

    return minLen == Integer.MAX_VALUE ? -1 : minLen;
}

private void addBits(int[] bitCount, int value) {
    for (int b = 0; b < 32; b++) {
        if (((value >> b) & 1) == 1) {
            bitCount[b]++;
        }
    }
}

private int removeBits(int[] bitCount, int orValue, int value) {
    for (int b = 0; b < 32; b++) {
        if (((value >> b) & 1) == 1) {
            bitCount[b]--;
            if (bitCount[b] == 0) {
                orValue &= ~(1 << b); // nenhum elemento da janela contribui mais com esse bit
            }
        }
    }
    return orValue;
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

- OR não é reversível como soma: não dá pra simplesmente "desfazer" um OR ao remover um elemento — é preciso contar quantos elementos contribuem para cada bit, e só desligar o bit quando a contagem chega a zero.
- Confundir "pelo menos k" com "igual a k" — o problema pede OR maior ou igual a `k`; uma vez satisfeita a condição, ainda vale a pena tentar encolher a janela pela esquerda para buscar algo menor.
- Esquecer o caso `k = 0`: qualquer subarray de tamanho 1 já tem OR `>= 0`, então a resposta é sempre `1` — o algoritmo já cobre isso naturalmente, mas vale conferir na hora de testar.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 | `nums=[1,2]`, `k=0` | 1 | qualquer subarray de 1 elemento já tem OR ≥ 0 |
| Nenhum subarray satisfaz | `nums=[1,2]`, `k=100` | -1 | OR máximo possível (3) nunca alcança 100 |
| Só o array inteiro serve | `nums=[1,2,4]`, `k=7` | 3 | só a OR de todos os 3 juntos (1\|2\|4=7) atinge k |
| Exemplo do enunciado | `nums=[2,1,8]`, `k=10` | 3 | só `[2,1,8]` junto tem OR 11 ≥ 10 |

## 🔗 Conexões

- Problemas irmãos: [0209] Minimum Size Subarray Sum (mesma estrutura de "encolher pela esquerda enquanto a condição se mantém", mas com soma em vez de OR), [3097] Shortest Subarray With OR at Least K II (mesmo problema com restrições maiores, exigindo esta técnica de contagem de bits em vez de força bruta)
- No backend: encontrar o menor lote de eventos cujas flags combinadas (OR bit a bit de permissões, por exemplo) cobrem um conjunto mínimo exigido de capacidades.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
