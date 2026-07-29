# [0497] Random Point in Non-overlapping Rectangles

> 🔗 [LeetCode 497](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#PrefixSum` `#Medium`

## 📜 O Problema

Você recebe um array de retângulos **sem sobreposição** `rects`, onde `rects[i] = [a, b, x, y]` descreve o canto inferior-esquerdo `(a,b)` e o superior-direito `(x,y)`. Implemente a classe `Solution` com o método `pick()`, que retorna um ponto **inteiro** aleatório dentro da área coberta por algum retângulo, de forma que **todo ponto inteiro tenha a mesma probabilidade** de ser escolhido (incluindo pontos na borda).

**Exemplo:**
```
Solution solution = new Solution([[-2,-2,1,1], [2,2,4,6]]);
solution.pick(); // ex.: [1,-2]
solution.pick(); // ex.: [1,-1]
solution.pick(); // ex.: [-1,-2]
```

**Restrições (e o que elas denunciam):**
- `1 <= rects.length <= 100`, `xi - ai <= 2000`, `yi - bi <= 2000` → retângulos podem ter até ~4 milhões de pontos cada, então **enumerar todos os pontos de todos os retângulos** para sortear é inviável em memória
- "todo ponto inteiro deve ter a mesma probabilidade" → retângulos maiores (mais pontos) precisam ter mais chance de ser escolhidos, **proporcional à sua área** — não dá pra sortear "qual retângulo" com peso uniforme entre eles
- "Até 10^4 chamadas a `pick`" → cada chamada precisa ser rápida (idealmente O(log n) no número de retângulos), já que o pré-processamento acontece só uma vez no construtor

## 🧭 Como reconhecer o padrão

"Sortear um item de uma coleção onde cada item tem um **peso** diferente (aqui, a área do retângulo)" é o padrão de **soma prefixada de pesos + busca binária**: construa o array de somas acumuladas das áreas, sorteie um número no intervalo total, e ache via busca binária em qual "faixa de peso" esse número caiu — exatamente a mesma técnica de [0528] Random Pick with Weight, aplicada aqui a áreas 2D em vez de pesos 1D.

## 🐢 Solução 1 — Força bruta

Enumerar e guardar **todos** os pontos inteiros de todos os retângulos numa lista, e sortear um índice uniformemente nessa lista a cada chamada de `pick()`.

- Tempo: O(1) por chamada, mas O(∑ área) de pré-processamento e memória · Espaço: O(∑ área)
- **Por que não basta:** com retângulos de até 2000×2000 pontos cada e até 100 retângulos, a lista de pontos pode chegar a centenas de milhões de entradas — inviável em memória, mesmo que cada `pick()` individual fosse rápido depois.

## 💡 Solução 2 — A ideia otimizada (intuição)

No construtor, calcule a **área** (quantidade de pontos inteiros) de cada retângulo — `(x-a+1) * (y-b+1)` — e monte um array de **soma prefixada** dessas áreas. A área total é o último valor da soma prefixada.

A cada chamada de `pick()`:
1. Sorteie um inteiro `r` uniforme no intervalo `[0, áreaTotal - 1]`.
2. Faça busca binária (upper bound) no array de soma prefixada para achar **qual retângulo** contém a posição `r` — um retângulo com área maior ocupa uma faixa maior da soma prefixada, logo tem mais chance de ser escolhido, proporcionalmente à sua área.
3. Dentro do retângulo escolhido, sorteie `x` uniformemente em `[a, x]` e `y` uniformemente em `[b, y]` (independentes um do outro).

## 🎬 Exemplo passo a passo

`rects = [[-2,-2,1,1], [2,2,4,6]]`

| Retângulo | Largura×Altura | Área | Soma prefixada |
|---|---|---|---|
| 0: [-2,-2,1,1] | (1-(-2)+1) × (1-(-2)+1) = 4×4 | 16 | 16 |
| 1: [2,2,4,6] | (4-2+1) × (6-2+1) = 3×5 | 15 | 31 |

Área total: `31`. Suponha que o sorteio inicial devolveu `r = 20` (dentro de `[0, 30]`):

| Passo | left | mid | right | somaPrefixada[mid] | Comparação | Decisão |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 (16) | 1 | 16 | 16 <= 20 → não é o retângulo | `left = 1` |
| 2 | 1 | 1 (31) | 1 | 31 | `left==right` → fim | idx = 1 |

O ponto sorteado cai no **retângulo 1**: `[2,2,4,6]`. Sorteia-se então `x` uniforme em `[2,4]` e `y` uniforme em `[2,6]` — por exemplo, `[3,5]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no construtor (n = número de retângulos) para montar a soma prefixada; O(log n) por chamada de `pick()`
- **Espaço:** O(n) para a soma prefixada — independente do tamanho de cada retângulo

## 💻 Implementações

### Java (referência completa e comentada)
```java
class Solution {
    private final int[][] rects;
    private final long[] somaPrefixada;
    private final Random random = new Random();

    public Solution(int[][] rects) {
        this.rects = rects;
        this.somaPrefixada = new long[rects.length];

        long acumulado = 0;
        for (int i = 0; i < rects.length; i++) {
            int a = rects[i][0], b = rects[i][1], x = rects[i][2], y = rects[i][3];
            long area = (long) (x - a + 1) * (y - b + 1);  // long: retângulos grandes podem estourar int
            acumulado += area;
            somaPrefixada[i] = acumulado;
        }
    }

    public int[] pick() {
        long areaTotal = somaPrefixada[somaPrefixada.length - 1];
        long r = (long) (random.nextDouble() * areaTotal);  // sorteio uniforme em [0, areaTotal)

        int idx = upperBound(r);                             // qual retângulo contém a posição r

        int a = rects[idx][0], b = rects[idx][1], x = rects[idx][2], y = rects[idx][3];
        int px = a + random.nextInt(x - a + 1);               // x uniforme em [a, x]
        int py = b + random.nextInt(y - b + 1);               // y uniforme em [b, y]
        return new int[]{px, py};
    }

    // Busca binária: primeiro índice onde somaPrefixada[idx] > alvo.
    private int upperBound(long alvo) {
        int left = 0, right = somaPrefixada.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (somaPrefixada[mid] <= alvo) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
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

- **Esquecer o `+1` no cálculo da área**: os pontos são inteiros e **inclusivos** nas bordas — um retângulo de `a=1` a `x=4` cobre os pontos `1,2,3,4`, ou seja, `4-1+1=4` pontos, não `4-1=3`.
- **Sortear "qual retângulo" com peso uniforme (ignorando a área)**: daria a mesma probabilidade para um retângulo de 1 ponto e um de 4 milhões de pontos — viola diretamente o requisito de "todo ponto tem a mesma probabilidade".
- **Overflow em `int` no cálculo da área**: com retângulos de até 2000×2000 e coordenadas até 10^9, use `long` tanto para a área individual quanto para a soma acumulada.
- **Confundir sorteio dentro do retângulo**: `x` e `y` são sorteados **independentemente** um do outro dentro dos limites do retângulo escolhido — não é preciso (nem correto) fazer outra busca binária aqui, é só um sorteio uniforme direto.

## 🧪 Casos de teste para validar

| Caso | Input | Comportamento esperado | Por quê |
|---|---|---|---|
| Um único retângulo, um ponto | `rects=[[1,1,1,1]]` | sempre retorna `[1,1]` | borda mínima, retângulo de área 1 |
| Retângulos de área muito diferente | `rects=[[0,0,0,0],[1,1,1000,1000]]` | quase sempre cai no segundo retângulo | testa que o peso é proporcional à área |
| Retângulo "fino" (linha) | `rects=[[0,0,5,0]]` | `y` sempre 0, `x` uniforme em [0,5] | testa altura 1 |
| Múltiplos retângulos pequenos | `rects=[[0,0,0,0],[5,5,5,5],[10,10,10,10]]` | cada um escolhido ~1/3 das vezes | todos com área 1, pesos iguais |
| Exemplo do enunciado | `rects=[[-2,-2,1,1],[2,2,4,6]]` | retângulo 0 (~52%) vs retângulo 1 (~48%) | proporção real de áreas 16:15 |

## 🔗 Conexões

- Problemas irmãos: **[0528] Random Pick with Weight** (o mesmo padrão de soma prefixada + busca binária, em 1D em vez de área 2D), **[0398] Random Pick Index** (outra variação de amostragem aleatória sobre uma coleção)
- No backend: sortear um servidor/shard proporcionalmente à sua capacidade (em vez de uniformemente entre servidores) para balanceamento de carga ponderado usa exatamente essa técnica de soma prefixada de pesos + busca binária.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
