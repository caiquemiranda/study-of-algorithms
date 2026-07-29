# [1608] Special Array With X Elements Greater Than or Equal X

> 🔗 [LeetCode 1608](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array `nums` de inteiros não negativos. O array é **especial** se existe um número `x` tal que existem **exatamente `x`** valores em `nums` que são **maiores ou iguais a `x`**. `x` não precisa estar presente no array. Retorne `x` se o array for especial, senão `-1` (garantido que `x` é único se existir).

**Exemplos:**
```
Input:  nums = [3,5]          Output: 2   (2 valores — 3 e 5 — são >= 2)
Input:  nums = [0,0]          Output: -1  (nenhum x funciona)
Input:  nums = [0,4,3,0,4]    Output: 3   (3 valores — 4,3,4 — são >= 3)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 100` → array pequeno, força bruta O(n²) passaria fácil, mas o padrão certo é busca binária depois de ordenar
- `0 <= nums[i] <= 1000` → como `x` só pode variar de `0` a `n` (não adianta `x` maior que o tamanho do array — nunca haveria `x` elementos suficientes), o espaço de candidatos é pequeno e monotônico
- "x não precisa ser elemento de nums" → x é uma propriedade sobre **contagem**, não sobre presença — pista de que a resposta vem de contar, não de buscar um valor específico

## 🧭 Como reconhecer o padrão

Ordenando o array de forma **decrescente**, a posição `i` (0-indexada) tem exatamente `i+1` elementos "até ali" (incluindo ele mesmo) que são `>= nums[i]` (assumindo ordenação decrescente sem buracos de contagem). A pergunta "existe posição onde o valor bate com a contagem" vira uma comparação monotônica `nums[i] - (i+1)`, que só decresce conforme `i` avança — o sinal clássico de busca binária pela fronteira.

## 🐢 Solução 1 — Força bruta

Para cada candidato `x` de `0` até `n`, contar quantos elementos de `nums` são `>= x`; se a contagem bater com `x`, retorna `x`.

- Tempo: O(n²) — `n+1` candidatos, cada um custando uma varredura O(n) · Espaço: O(1)
- **Por que não basta:** repete a contagem do zero para cada candidato, ignorando que, se o array estiver ordenado, a contagem de elementos `>= x` pode ser obtida em O(log n) por busca binária em vez de recontar tudo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums` em ordem **decrescente**. Agora, na posição `i`, se `nums[i] >= i + 1`, significa que existem pelo menos `i+1` elementos (os `i+1` primeiros, já que estão ordenados decrescente) que são `>= nums[i]` — ou seja, `x = i+1` é um candidato plausível.

Como o array está ordenado decrescente, a expressão `nums[i] - (i + 1)` é **estritamente decrescente** conforme `i` cresce (o valor só diminui ou mantém, e `i+1` sempre cresce) — então busque binariamente o **maior índice `i`** onde `nums[i] >= i + 1`. Se esse índice existir, a resposta é `i + 1`; senão, não existe `x` válido (retorna `-1`).

## 🎬 Exemplo passo a passo

`nums = [3, 5]` → ordenado decrescente: `[5, 3]`

| Passo | left | mid | right | nums[mid] vs mid+1 | Decisão |
|---|---|---|---|---|---|
| 1 | 0 | 0 (val 5) | 1 | 5 >= 1 → candidato válido | guarda i=0, `left = 1` |
| 2 | 1 | 1 (val 3) | 1 | 3 >= 2 → candidato válido | guarda i=1, `left = 2` |
| 3 | 2 | — | 1 | `left > right` → fim | melhor candidato: i=1 |

Resultado final: `x = i + 1 = 2` ✔ (2 elementos — 3 e 5 — são `>= 2`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a busca binária em si é O(log n)
- **Espaço:** O(log n) a O(n) — dependendo do algoritmo de sort da linguagem

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int specialArray(int[] nums) {
    Integer[] ordenado = Arrays.stream(nums).boxed().toArray(Integer[]::new);
    Arrays.sort(ordenado, Collections.reverseOrder());  // ordena decrescente

    int left = 0, right = ordenado.length - 1;
    int melhorIndice = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (ordenado[mid] >= mid + 1) {
            // Existem pelo menos mid+1 elementos >= ordenado[mid] (os mid+1 primeiros).
            // Guarda como candidato e tenta um índice ainda maior.
            melhorIndice = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    // Sem candidato válido: nenhum x satisfaz a condição.
    return melhorIndice == -1 ? -1 : melhorIndice + 1;
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

- **Ordenar crescente em vez de decrescente**: a lógica `nums[i] >= i+1` só faz sentido com ordenação decrescente (onde os maiores valores vêm primeiro, alinhando índice baixo com contagem alta); ordenar crescente exige inverter toda a fórmula.
- **Esquecer que pode não existir candidato**: `nums = [0,0]` nunca satisfaz `nums[i] >= i+1` para nenhum `i` (`0 >= 1` é falso, `0 >= 2` é falso) — o retorno `-1` precisa de tratamento explícito.
- **Tentar `x = 0` como caso especial**: como todo elemento de `nums` é não negativo, `x = 0` exigiria "zero elementos são `>= 0`", o que é impossível com array não vazio (todo elemento é `>= 0`) — por isso o problema nunca considera `x = 0` como resposta válida.
- **Confundir "maior índice válido" com "primeiro índice válido"**: a garantia de unicidade do problema torna isso irrelevante na prática, mas didaticamente é importante entender que buscamos o candidato que maximiza `i+1` mantendo a condição verdadeira.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem solução | `nums=[0,0]` | -1 | nenhum x satisfaz, testa o caso de falha |
| Um elemento | `nums=[0]` | -1 | 0 elementos podem ser >= 0? não, já que o único elemento é 0 e conta como >=0 |
| Um elemento positivo | `nums=[5]` | 1 | 1 elemento (o próprio 5) é >= 1 |
| Múltiplos candidatos aparentes | `nums=[0,4,3,0,4]` | 3 | trace parcial no enunciado, testa duplicatas |
| Exemplo do enunciado | `nums=[3,5]` | 2 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[2529] Maximum Count of Positive Integer and Negative Integer** (busca binária por fronteira em array ordenado), **[0704] Binary Search** (o padrão-base), **[0441] Arranging Coins** (busca binária sobre uma condição derivada de índice)
- No backend: achar um "ponto fixo" onde uma métrica de ranking (ex.: "quantos itens têm score >= score do item na posição N") se auto-referencia é o mesmo raciocínio usado no cálculo do índice-h de citações acadêmicas — o próprio LeetCode cita essa analogia como motivação do problema.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
