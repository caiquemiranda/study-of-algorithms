# [1040] Moving Stones Until Consecutive II

> 🔗 [LeetCode 1040](https://leetcode.com/problems/moving-stones-until-consecutive-ii/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Sorting` `#Medium`

## 📜 O Problema

Há pedras em posições diferentes no eixo X, dadas pelo array `stones`. Uma pedra é chamada de **endpoint** se está na posição mínima ou máxima. Em uma jogada, você pega uma pedra endpoint e a move para uma posição desocupada de forma que ela deixe de ser endpoint. O jogo termina quando as pedras ocupam três posições consecutivas. Retorne um array `[min, max]` com o número mínimo e máximo de jogadas possíveis.

**Exemplos:**
```
Input:  stones = [7,4,9]
Output: [1,2]
Explicação: mover 4->8 termina em 1 jogada. Ou mover 9->5, 4->6 termina em 2 jogadas.

Input:  stones = [6,5,4,3,10]
Output: [2,3]
```

**Restrições (e o que elas denunciam):**
- `3 <= stones.length <= 10^4` → O(n²) é aceitável, mas O(n log n) (dominado pela ordenação) é o esperado
- `1 <= stones[i] <= 10^9`, valores **únicos** → precisa ordenar antes de qualquer análise de vizinhança

## 🧭 Como reconhecer o padrão

"Quantas pedras cabem numa janela de `n` posições consecutivas" (depois de ordenar) é janela deslizante de tamanho fixo sobre um array ordenado: para cada posição, uma janela de `n` pedras que caiba no menor intervalo de posições revela quantos "buracos" (posições vazias) precisam ser preenchidos — cada buraco custa uma jogada, exceto um caso especial isolado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular o jogo movendo pedras endpoint uma a uma de todas as formas possíveis, buscando o mínimo e o máximo de jogadas por busca exaustiva.

- Tempo: exponencial (explora todas as sequências de jogadas possíveis) · Espaço: O(2^n) no pior caso
- **Por que não basta:** o número de sequências de jogadas cresce descontroladamente; o problema tem uma estrutura matemática (baseada em ordenação e contagem de "buracos") que dispensa qualquer simulação.

## 💡 Solução 2 — A ideia otimizada (intuição)

**Máximo:** só as duas pedras mais extremas podem, em jogadas isoladas, "pular" para logo antes/depois da segunda pedra mais próxima da outra ponta, uma por jogada — o máximo é `max(stones[n-2]-stones[0]-(n-2), stones[n-1]-stones[1]-(n-2))`.

**Mínimo:** deslize uma janela de `n` pedras (em índice) sobre o array ordenado, encontrando a que cabe no menor intervalo de posições. Se a janela já cobre `n-1` posições consecutivas exatas (só falta 1 pedra "de fora"), o mínimo para essa configuração é 2 (caso especial: a pedra de fora fica presa entre duas pedras já ocupadas). Senão, o mínimo de jogadas é `n - (pedras já dentro da janela)`.

## 🎬 Exemplo passo a passo

`stones = [7,4,9]` → ordenado: `[4,7,9]`, n=3

**Máximo:** `max(stones[1]-stones[0]-(n-2), stones[2]-stones[1]-(n-2)) = max(7-4-1, 9-7-1) = max(2,1) = 2`

**Mínimo** (janela de tamanho n=3 sobre o array ordenado, por índice):
| right | Encolhe left até caber em n posições | pedras na janela (cnt) | Caso especial (cnt=n-1 e span=n-2)? | mínimo candidato |
|---|---|---|---|---|
| 0 | left=0 | 1 | não | n-cnt=2 |
| 1 | left=1 (stones[1]-stones[0]+1=4>3) | 1 | não | n-cnt=2 |
| 2 | left=1 (stones[2]-stones[1]+1=3<=3, sem mover) | 2 | sim, mas span(9-7=2)≠n-2(1) → não se aplica | n-cnt=1 |

Resultado final: `[1, 2]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura da janela depois é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] numMovesStonesII(int[] stones) {
    Arrays.sort(stones);
    int n = stones.length;

    if (stones[n - 1] - stones[0] + 1 == n) {
        return new int[]{0, 0}; // já consecutivas, nenhuma jogada necessária
    }

    int maxMoves = Math.max(
        stones[n - 2] - stones[0] - (n - 2),
        stones[n - 1] - stones[1] - (n - 2)
    );

    int minMoves = n;
    int left = 0;
    for (int right = 0; right < n; right++) {
        while (stones[right] - stones[left] + 1 > n) {
            left++; // encolhe até a janela caber em n posições consecutivas
        }
        int count = right - left + 1; // pedras já dentro da janela de n posições
        if (count == n - 1 && stones[right] - stones[left] == n - 2) {
            minMoves = Math.min(minMoves, 2); // caso especial: pedra isolada presa entre duas ocupadas
        } else {
            minMoves = Math.min(minMoves, n - count);
        }
    }

    return new int[]{minMoves, maxMoves};
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

- Só as pedras endpoint podem ser movidas, e movê-las precisa fazer com que deixem de ser endpoint — isso é o que restringe o máximo às duas pedras mais próximas de cada ponta, e não a qualquer par arbitrário.
- O caso especial do mínimo (`count == n-1` e `span == n-2`) representa uma configuração onde `n-1` pedras já são consecutivas e sobra exatamente 1 pedra isolada — mover essa pedra sozinha não fecha o buraco em 1 jogada porque ela ficaria presa entre duas pedras ocupadas ao tentar se aproximar; são necessárias 2 jogadas.
- Ordenar é obrigatório antes de qualquer cálculo — sem ordenação, "vizinhança" e "buracos" não fazem sentido posicional.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já consecutivas | `[3,4,5]` | [0,0] | nenhuma jogada necessária |
| Caso especial (2 jogadas mínimas) | `[6,5,4,3,10]` | [2,3] | um buraco isolado exige 2 jogadas, não 1 |
| Tamanho mínimo (3 pedras) | `[7,4,9]` | [1,2] | exemplo do enunciado |
| Pedras muito espaçadas | `[1,10,100]` | [2,2] | ambos os extremos precisam de 1 jogada cada, mínimo=máximo |

## 🔗 Conexões

- Problemas irmãos: [1183] Maximum Number of Ones (mesma família de raciocínio sobre janelas em arrays ordenados), [0011] Container With Most Water (mesma técnica-base de dois ponteiros guiados por posições extremas)
- No backend: calcular o esforço mínimo/máximo de "compactar" recursos espalhados (ex.: IDs de servidores, faixas de portas) em um intervalo contíguo, movendo apenas os elementos das bordas por vez.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
