# [1652] Defuse the Bomb

> 🔗 [LeetCode 1652](https://leetcode.com/problems/defuse-the-bomb/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array **circular** `code` de tamanho `n` e uma chave `k`. Substitua cada número **simultaneamente**: se `k > 0`, o `i`-ésimo número vira a soma dos próximos `k` números; se `k < 0`, vira a soma dos `-k` números anteriores; se `k == 0`, vira `0`. Como o array é circular, o próximo de `code[n-1]` é `code[0]`, e o anterior de `code[0]` é `code[n-1]`. Retorne o código decifrado.

**Exemplos:**
```
Input:  code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explicação: cada número vira a soma dos 3 próximos, dando a volta no array.

Input:  code = [1,2,3,4], k = 0
Output: [0,0,0,0]

Input:  code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explicação: cada número vira a soma dos 2 anteriores, dando a volta.
```

**Restrições (e o que elas denunciam):**
- `n == code.length`, `1 <= n <= 100` → tamanho pequeno, até força bruta O(n²) passaria, mas o padrão certo já é O(n)
- `1 <= code[i] <= 100` → valores sempre positivos, então somar mais elementos à janela sempre aumenta a soma (sem cancelamentos a considerar)
- `-(n-1) <= k <= n-1` → `|k|` nunca alcança `n`, então a janela de cada posição nunca "dá mais que uma volta" e nunca inclui o próprio elemento

## 🧭 Como reconhecer o padrão

"Soma de uma janela de tamanho fixo `|k|` ao redor de cada posição" é janela deslizante clássica — a única diferença é que o array é **circular**, então os índices da janela "dão a volta" usando aritmética modular em vez de pararem na borda do array.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, somar do zero os `|k|` vizinhos (à frente ou atrás, conforme o sinal de `k`), usando índice módulo `n` para tratar a circularidade.

- Tempo: O(n·|k|), que no pior caso (`|k|` próximo de `n-1`) vira O(n²) · Espaço: O(n) para a saída
- **Por que não basta:** recalcula a soma da janela do zero para cada `i`, apesar de janelas consecutivas compartilharem quase todos os elementos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se `k == 0`, a resposta é um array de zeros, sem precisar de nenhuma janela. Caso contrário, calcule a soma da primeira janela relevante (`|k|` elementos) uma única vez e deslize: a cada passo, subtrai o elemento que sai da janela e soma o que entra — sempre usando índice circular (módulo `n`, com cuidado para índices negativos).

## 🎬 Exemplo passo a passo

`code = [5,7,1,4]`, `k = 3` (janela de cada `i` são os 3 **próximos** elementos, circular)

| i | Janela (índices) | Sai | Entra | Soma | result[i] |
|---|---|---|---|---|---|
| 0 (inicial) | 1,2,3 | — | — | 7+1+4=12 | 12 |
| 1 | 2,3,0 | code[1]=7 | code[0]=5 | 12-7+5=10 | 10 |
| 2 | 3,0,1 | code[2]=1 | code[1]=7 | 10-1+7=16 | 16 |
| 3 | 0,1,2 | code[3]=4 | code[2]=1 | 16-4+1=13 | 13 |

Resultado final: `[12,10,16,13]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — soma inicial O(|k|) mais `n` deslizamentos O(1) cada, e `|k| < n`
- **Espaço:** O(n) para o array de saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] decrypt(int[] code, int k) {
    int n = code.length;
    int[] result = new int[n];
    if (k == 0) {
        return result; // já inicializado com zeros
    }

    // start = deslocamento da janela em relação a cada i; windowSize = quantos elementos somar
    int start = k > 0 ? 1 : k;
    int windowSize = Math.abs(k);

    int windowSum = 0;
    for (int offset = 0; offset < windowSize; offset++) {
        windowSum += code[circularIndex(start + offset, n)];
    }

    for (int i = 0; i < n; i++) {
        result[i] = windowSum;
        int outIndex = circularIndex(start + i, n); // elemento que sai da janela ao avançar i
        int inIndex = circularIndex(start + i + windowSize, n); // elemento que entra
        windowSum += code[inIndex] - code[outIndex];
    }

    return result;
}

private int circularIndex(int index, int n) {
    return ((index % n) + n) % n; // dupla módulo: Java preserva o sinal do dividendo em %
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

- Em Java (e várias outras linguagens), o operador `%` pode retornar valor **negativo** quando o dividendo é negativo (`-2 % 4 == -2`, não `2`) — por isso é preciso o padrão `((x % n) + n) % n` para obter sempre um índice circular válido.
- Todas as substituições acontecem **simultaneamente**: as somas devem usar sempre o array `code` original, nunca um `result` parcialmente atualizado — senão a saída de uma posição contamina o cálculo da próxima.
- `k == 0` não é "uma janela de tamanho 0" dentro da lógica de deslizamento — é um caso especial que retorna zeros direto, tratado fora do loop principal.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 | `code=[1,2,3,4]`, `k=0` | [0,0,0,0] | regra explícita do enunciado |
| k positivo (olha à frente, circular) | `code=[5,7,1,4]`, `k=3` | [12,10,16,13] | soma dos 3 próximos, dando a volta |
| k negativo (olha atrás, circular) | `code=[2,4,9,3]`, `k=-2` | [12,5,6,13] | soma dos 2 anteriores, dando a volta |
| Array de 1 elemento | `code=[7]`, `k=0` | [0] | único elemento possível, k=0 zera |

## 🔗 Conexões

- Problemas irmãos: [0643] Maximum Average Subarray I (mesma técnica de soma deslizante, sem a complicação circular), [1094] Car Pooling (soma de janelas sobre um eixo, mesma ideia de "entra/sai" ainda que não circular)
- No backend: suavização de métricas cíclicas — por exemplo, tráfego médio por hora do dia num sistema que "dá a volta" à meia-noite — calculando somas móveis sem reprocessar tudo a cada janela.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
