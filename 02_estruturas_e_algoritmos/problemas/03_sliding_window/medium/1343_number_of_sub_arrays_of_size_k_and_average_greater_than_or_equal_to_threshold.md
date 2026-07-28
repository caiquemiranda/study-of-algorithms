# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

> 🔗 [LeetCode 1343](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dado um array de inteiros `arr` e dois inteiros `k` e `threshold`, retorne o número de subarrays de tamanho `k` com média maior ou igual a `threshold`.

**Exemplos:**
```
Input:  arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explicação: [2,5,5], [5,5,5] e [5,5,8] têm médias 4, 5 e 6.

Input:  arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 10^5` → O(n·k) recalculando cada janela do zero é arriscado; O(n) é o esperado
- `1 <= arr[i] <= 10^4`, `0 <= threshold <= 10^4` → comparar `soma >= threshold*k` evita divisão em ponto flutuante

## 🧭 Como reconhecer o padrão

"Contar janelas de tamanho **fixo** que satisfazem uma condição de média" é janela deslizante de tamanho fixo: em vez de dividir a soma por `k` a cada janela (arriscando erro de ponto flutuante), compare a soma diretamente contra `threshold * k`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada início `i`, somar os `k` elementos do zero e comparar a média com `threshold`.

- Tempo: O(n·k) · Espaço: O(1)
- **Por que não basta:** recalcula a soma inteira a cada janela, mesmo que `k-1` dos `k` elementos sejam os mesmos da janela anterior.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule a soma da primeira janela. Deslize subtraindo o elemento que sai e somando o que entra. Compare `soma >= threshold * k` (evitando divisão) a cada passo, contando as janelas válidas.

## 🎬 Exemplo passo a passo

`arr = [2,2,2,2,5,5,5,8]`, `k = 3`, `threshold = 4` → alvo: `soma >= 12`

| Janela | Soma | ≥ 12? | Contagem |
|---|---|---|---|
| [0..2] | 6 | não | 0 |
| [1..3] | 6 | não | 0 |
| [2..4] | 9 | não | 0 |
| [3..5] | 12 | sim | 1 |
| [4..6] | 15 | sim | 2 |
| [5..7] | 18 | sim | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numOfSubarrays(int[] arr, int k, int threshold) {
    long targetSum = (long) threshold * k;
    long windowSum = 0;
    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }

    int count = windowSum >= targetSum ? 1 : 0;
    for (int i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k];
        if (windowSum >= targetSum) {
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

- Comparar `soma >= threshold * k` em vez de `soma/k >= threshold` evita divisão em ponto flutuante e qualquer erro de arredondamento — matematicamente equivalente, mas exato.
- `threshold * k` pode chegar perto do limite de `int` em casos extremos — usar `long` para essa multiplicação é hábito seguro.
- Janela de tamanho fixo `k` — não há encolhimento algum, só deslizamento incremental.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k igual ao array inteiro | `arr=[5,5,5]`, `k=3`, `threshold=5` | 1 | única janela, média exatamente 5 |
| Nenhuma janela atinge o threshold | `arr=[1,1,1,1]`, `k=2`, `threshold=5` | 0 | média máxima possível é 1 |
| threshold=0 (sempre satisfaz) | `arr=[1,2]`, `k=1`, `threshold=0` | 2 | toda janela de tamanho 1 tem média >= 0 |
| Exemplo do enunciado | `arr=[2,2,2,2,5,5,5,8]`, `k=3`, `threshold=4` | 3 | 3 janelas de tamanho 3 têm média >= 4 |

## 🔗 Conexões

- Problemas irmãos: [0643] Maximum Average Subarray I (mesma técnica-base de janela fixa com soma incremental, aqui contando janelas válidas em vez de achar a máxima), [2379] Minimum Recolors to Get K Consecutive Black Blocks (mesma família de janela fixa deslizando com ajuste incremental)
- No backend: contar quantos intervalos de tempo fixo (ex.: janelas de 1 hora) de uma métrica atingem um SLA mínimo de desempenho médio.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
