# [1566] Detect Pattern of Length M Repeated K or More Times

> 🔗 [LeetCode 1566](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array de inteiros positivos `arr`, encontre um padrão de tamanho `m` que se repita `k` ou mais vezes. Um **padrão** é um subarray (subsequência consecutiva) composto por um ou mais valores, repetido múltiplas vezes **consecutivamente** e **sem sobreposição**.

Retorne `true` se existe um padrão de tamanho `m` repetido `k` ou mais vezes; caso contrário, retorne `false`.

**Exemplos:**
```
Input:  arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explicação: o padrão (4) de tamanho 1 se repete 4 vezes consecutivas.

Input:  arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: true
Explicação: o padrão (1,2) de tamanho 2 se repete 2 vezes consecutivas. O padrão (2,1) também é válido.

Input:  arr = [1,2,1,2,1,3], m = 2, k = 3
Output: false
Explicação: o padrão (1,2) tem tamanho 2 mas repete só 2 vezes. Não há padrão de tamanho 2
repetido 3 ou mais vezes.
```

**Restrições (e o que elas denunciam):**
- `2 <= arr.length <= 100` → pequeno, permite força bruta O(n×m) sem problema
- `1 <= m <= 100`, `2 <= k <= 100` → padrão e repetições também pequenos

## 🧭 Como reconhecer o padrão

"Existe um padrão de tamanho fixo M que se repete K vezes consecutivas, sem sobreposição" é resolvido testando, para cada posição inicial possível, se os próximos `m*k` elementos formam exatamente K cópias consecutivas do bloco de tamanho M começando ali.

## 🐢 Solução 1 — Força bruta (e também a solução aceita aqui)

Para cada posição inicial `i` de 0 até `n - m*k`, verificar se `arr[i+j] == arr[i + (j % m)]` para todo `j` de 0 até `m*k - 1` — ou seja, se o bloco se repete perfeitamente.

- Tempo: O(n × m × k) — para cada posição inicial, verifica m*k elementos · Espaço: O(1)
- **Por que é aceitável aqui:** com n, m, k todos ≤ 100, o pior caso é 100×100×100 = 1.000.000 — perfeitamente rápido para este tamanho de entrada.

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Não há uma segunda técnica assintoticamente melhor que valha a pena aqui — dado o limite pequeno de n, m e k, a enumeração completa já É a solução esperada. A única "otimização" prática é cortar cedo: comparar o bloco elemento a elemento e abortar assim que a primeira divergência aparecer, em vez de gerar as k cópias do bloco antes de comparar.

## 🎬 Exemplo passo a passo

`arr = [1,2,4,4,4,4]`, `m=1, k=3`

| Passo | posição inicial testada | bloco | repete k=3 vezes a partir daqui? |
|---|---|---|---|
| 1 | i=0 (bloco=[1]) | [1] | não (arr[1]=2≠1) |
| 2 | i=1 (bloco=[2]) | [2] | não (arr[2]=4≠2) |
| 3 | i=2 (bloco=[4]) | [4] | sim (arr[2]=arr[3]=arr[4]=4) |

Resultado final: `true` ✔ (encontrado em i=2, sem precisar testar i=3)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n × m × k)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean containsPattern(int[] arr, int m, int k) {
    int n = arr.length;

    for (int i = 0; i + m * k <= n; i++) {
        if (repetePadrao(arr, i, m, k)) {
            return true;
        }
    }
    return false;
}

private boolean repetePadrao(int[] arr, int inicio, int m, int k) {
    for (int j = 0; j < m * k; j++) {
        // o elemento em (inicio+j) precisa bater com o elemento correspondente dentro do primeiro bloco
        if (arr[inicio + j] != arr[inicio + (j % m)]) {
            return false;
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

- Esquecer o limite correto do loop externo (`i + m*k <= n`, não `i < n`) — sem essa checagem, o código tentaria acessar índices fora dos limites do array ao testar posições próximas do fim.
- Confundir "padrão que se repete" com "subsequência" — a repetição precisa ser CONSECUTIVA e SEM SOBREPOSIÇÃO, exatamente `m*k` elementos contíguos formando k blocos idênticos de tamanho m.
- Usar `j % k` em vez de `j % m` — a comparação precisa ser sempre contra o PRIMEIRO bloco de tamanho `m`, então o índice de referência é `inicio + (j % m)`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Padrão de tamanho 1 | arr=[1,2,4,4,4,4], m=1, k=3 | true | "4" repetido 4 vezes, mais que k=3 necessário |
| Padrão de tamanho 2 | arr=[1,2,1,2,1,1,1,3], m=2, k=2 | true | "(1,2)" se repete 2 vezes consecutivas |
| Padrão não repete o suficiente | arr=[1,2,1,2,1,3], m=2, k=3 | false | "(1,2)" só repete 2 vezes, precisa de 3 |
| Array muito pequeno para o padrão | arr=[1,2], m=2, k=2 | false | precisaria de 4 elementos (m*k), só tem 2 |

## 🔗 Conexões

- Problemas irmãos: [0459] Repeated Substring Pattern (mesmo domínio de detecção de periodicidade, mas em strings), [1668] Maximum Repeating Substring (mesma ideia de encontrar repetições consecutivas de um padrão)
- No backend: detecção de padrões cíclicos em séries de dados de sensores ou logs (ex.: identificar se uma sequência de eventos se repete de forma consistente, sinalizando um comportamento periódico esperado ou anômalo).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
