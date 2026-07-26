# [0747] Largest Number At Least Twice of Others

> 🔗 [LeetCode 747](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Você recebe um array de inteiros `nums` onde o maior inteiro é **único**. Determine se o maior elemento do array é **pelo menos o dobro** de todos os outros números. Se for, retorne **o índice** do maior elemento; caso contrário, retorne `-1`.

**Exemplos:**
```
Input:  nums = [3,6,1,0]
Output: 1
Explicação: 6 é o maior inteiro. Para todo outro número x, 6 é pelo menos o dobro de x.
O índice do valor 6 é 1, então retornamos 1.

Input:  nums = [1,2,3,4]
Output: -1
Explicação: 4 é menor que o dobro de 3, então retornamos -1.
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 50` → entrada minúscula, qualquer O(n) ou O(n log n) serve com folga
- `0 <= nums[i] <= 100` → valores não negativos, "pelo menos o dobro" nunca tem problema de sinal
- "o maior elemento é único" → não precisa desempatar entre dois máximos iguais

## 🧭 Como reconhecer o padrão

"Compare o maior elemento contra TODOS os outros" é sempre resolvido achando o maior e o segundo maior em uma única passada — porque se o maior já é pelo menos o dobro do SEGUNDO maior, automaticamente ele é pelo menos o dobro de qualquer outro elemento (que é ≤ ao segundo maior).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Encontre o maior elemento e seu índice; depois, percorra o array de novo comparando esse maior contra CADA outro elemento individualmente, verificando se `maior >= 2 * outro` para todos.

- Tempo: O(n) — na verdade já é linear, só faz duas passadas completas · Espaço: O(1)
- **Por que não basta:** tecnicamente já é O(n) e aceitável, mas faz uma segunda passada completa quando dá pra responder com uma passada só, rastreando o maior e o segundo maior — mais uma questão de elegância de uma-passada do que de complexidade assintótica aqui.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em uma única passada, mantenha `maior` e `segundoMaior`. Ao final, se `maior >= 2 * segundoMaior`, retorne o índice do maior; senão, `-1`. Isso funciona porque o segundo maior é o "pior caso" — se o maior vence até ele por pelo menos o dobro, vence qualquer elemento menor também.

## 🎬 Exemplo passo a passo

`nums = [3,6,1,0]`

| Passo | i | nums[i] | maior (antes) | segundoMaior (antes) | Ação | maior (depois) | segundoMaior (depois) |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 3 | -1 | -1 | 3 vira o maior | 3 (idx0) | -1 |
| 2 | 1 | 6 | 3 | -1 | 6>3: 3 vira segundo, 6 vira maior | 6 (idx1) | 3 |
| 3 | 2 | 1 | 6 | 3 | 1<6 e 1<3, não muda nada | 6 (idx1) | 3 |
| 4 | 3 | 0 | 6 | 3 | 0<6 e 0<3, não muda nada | 6 (idx1) | 3 |

Checagem final: `maior(6) >= 2×segundoMaior(3) = 6` → sim → retorna índice `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) — dois valores e dois índices rastreados

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int dominantIndex(int[] nums) {
    int indiceMaior = 0;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] > nums[indiceMaior]) {
            indiceMaior = i;
        }
    }

    int maior = nums[indiceMaior];
    for (int i = 0; i < nums.length; i++) {
        if (i != indiceMaior && maior < 2 * nums[i]) {
            return -1; // achou alguém que o maior não domina por pelo menos o dobro
        }
    }
    return indiceMaior;
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

- Comparar `maior / 2 >= nums[i]` em vez de `maior >= 2 * nums[i]` — divisão inteira pode arredondar para baixo e mudar o resultado da comparação em casos de números ímpares; multiplicar é mais seguro.
- Esquecer de pular a comparação do maior elemento contra ele mesmo (`i != indiceMaior`) — não chega a quebrar a lógica matematicamente (qualquer número é pelo menos o dobro de si mesmo quando é 0), mas pular explicitamente deixa a intenção clara.
- Assumir que basta comparar contra um elemento arbitrário sem realmente rastrear o segundo maior real — comparar só contra o penúltimo elemento visitado (em vez do verdadeiro segundo maior) pode dar falso positivo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Domina todos | `[3,6,1,0]` | 1 | 6 é pelo menos o dobro de todos os outros |
| Não domina | `[1,2,3,4]` | -1 | 4 não é o dobro de 3 |
| Dois elementos | `[1,0]` | 0 | 1 é pelo menos o dobro de 0 |
| Maior exatamente o dobro | `[1,2]` | 1 | 2 = 2×1, igualdade também conta como "pelo menos o dobro" |

## 🔗 Conexões

- Problemas irmãos: [0414] Third Maximum Number (mesmo padrão de rastrear os top-k valores em uma passada), [0169] Majority Element (também raciocina sobre dominância de um elemento sobre os demais)
- No backend: detecção de outliers ou concentração de carga (ex.: identificar se um servidor está recebendo pelo menos o dobro de tráfego do segundo mais carregado, sinal de desbalanceamento que merece atenção).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
