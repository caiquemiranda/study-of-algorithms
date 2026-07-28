# [1423] Maximum Points You Can Obtain from Cards

> 🔗 [LeetCode 1423](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#PrefixSum` `#Medium`

## 📜 O Problema

Há várias cartas em fila, cada uma com uma pontuação, dadas em `cardPoints`. Em cada passo, você pode pegar uma carta do início ou do fim da fila. Você deve pegar exatamente `k` cartas. Sua pontuação é a soma dos pontos das cartas pegas. Retorne a **pontuação máxima** possível.

**Exemplos:**
```
Input:  cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explicação: pegar as três cartas da direita dá 1+6+5=12.

Input:  cardPoints = [2,2,2], k = 2
Output: 4

Input:  cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
```

**Restrições (e o que elas denunciam):**
- `1 <= cardPoints.length <= 10^5` → O(2^k) testando todas as combinações de esquerda/direita é inviável; O(n) é o esperado
- `1 <= k <= cardPoints.length` → `k` pode cobrir o array inteiro

## 🧭 Como reconhecer o padrão

A virada de perspectiva: em vez de "maximizar a soma das `k` cartas pegas das pontas", pense em "minimizar a soma do bloco **contíguo** de `n-k` cartas que sobram no meio" — como as cartas retiradas vêm só das pontas, o que sobra é sempre um bloco contíguo. Minimizar esse bloco com janela deslizante de tamanho fixo maximiza a pontuação (`total - mínimo`).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todas as `k+1` formas de dividir as `k` cartas entre "pegar da esquerda" e "pegar da direita" (0 da esquerda e k da direita, 1 da esquerda e k-1 da direita, etc.), somando cada combinação.

- Tempo: O(k) já é razoável, mas recalcular cada soma do zero vira O(k²) · Espaço: O(1)
- **Por que não basta:** recalcula a soma das cartas escolhidas do zero para cada divisão, quando prefix sums (ou a técnica de janela complementar) evitam esse trabalho repetido.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule a soma total. Deslize uma janela de tamanho fixo `n-k` (o bloco central "descartado") e encontre a de MENOR soma. A resposta é `total - menorSomaDoBloco`.

## 🎬 Exemplo passo a passo

`cardPoints = [1,2,3,4,5,6,1]`, `k = 3` → bloco central de tamanho `n-k=4`

| Janela (tamanho n-k=4) | Soma | Mínimo até agora |
|---|---|---|
| [0..3] | 10 | 10 |
| [1..4] | 14 | 10 |
| [2..5] | 18 | 10 |
| [3..6] | 16 | 10 |

total = 22; Resultado final: `22 - 10 = 12` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxScore(int[] cardPoints, int k) {
    int n = cardPoints.length;
    int windowSize = n - k;

    int total = 0;
    for (int p : cardPoints) {
        total += p;
    }

    if (windowSize == 0) {
        return total; // k cobre o array inteiro, nenhum bloco central a descartar
    }

    int windowSum = 0;
    for (int i = 0; i < windowSize; i++) {
        windowSum += cardPoints[i];
    }

    int minWindow = windowSum;
    for (int i = windowSize; i < n; i++) {
        windowSum += cardPoints[i] - cardPoints[i - windowSize];
        minWindow = Math.min(minWindow, windowSum);
    }

    return total - minWindow;
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

- A virada de perspectiva é essencial: pense em "minimizar o bloco central de `n-k` cartas que SOBRAM", não em "maximizar as `k` escolhidas" diretamente.
- Quando `k == n` (todas as cartas), o bloco central tem tamanho `0` — a resposta é simplesmente `total`, sem nenhuma janela pra minimizar.
- O bloco central é sempre CONTÍGUO porque as cartas retiradas vêm exclusivamente das pontas — qualquer escolha de k cartas das pontas deixa exatamente um bloco contíguo no meio.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k igual ao array inteiro | `cardPoints=[9,7,7,9,7,7,9]`, `k=7` | 55 | todas as cartas são pegas, soma total |
| Todas as cartas iguais | `cardPoints=[2,2,2]`, `k=2` | 4 | qualquer escolha de 2 cartas soma 4 |
| Meio inacessível | `cardPoints=[1,1000,1]`, `k=1` | 1 | só as pontas são acessíveis com k=1; a carta do meio (1000) nunca pode ser pega sozinha |
| Exemplo do enunciado | `cardPoints=[1,2,3,4,5,6,1]`, `k=3` | 12 | melhor bloco central a deixar de fora soma 10 |

## 🔗 Conexões

- Problemas irmãos: [0643] Maximum Average Subarray I (mesma técnica-base de janela fixa deslizante), [1031] Maximum Sum of Two Non-Overlapping Subarrays (mesma família de raciocínio sobre combinações de segmentos do array, aqui via complemento em vez de soma direta)
- No backend: escolher os melhores itens das extremidades de uma fila/lista processável (primeiras e últimas transações de um lote) maximizando valor, equivalente a minimizar o "descarte" central.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
