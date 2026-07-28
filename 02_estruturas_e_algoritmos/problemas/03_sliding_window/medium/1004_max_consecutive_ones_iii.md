# [1004] Max Consecutive Ones III

> 🔗 [LeetCode 1004](https://leetcode.com/problems/max-consecutive-ones-iii/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dado um array binário `nums` e um inteiro `k`, retorne o número máximo de `1`s consecutivos no array se você puder inverter até `k` zeros para uns.

**Exemplos:**
```
Input:  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Input:  nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `nums[i]` é `0` ou `1` → binário, simplificando a contagem de "quantos zeros" numa janela
- `0 <= k <= nums.length` → `k` pode cobrir o array inteiro, permitindo transformá-lo todo em 1s

## 🧭 Como reconhecer o padrão

"Maior janela de 1s permitindo inverter até `k` zeros" é o padrão clássico de "no máximo k elementos ruins numa janela": expande-se pela direita; se o número de zeros na janela exceder `k`, encolhe-se pela esquerda até voltar a ser válida.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, contar quantos zeros existem na janela e checar se `<= k`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recomputa a contagem de zeros do zero a cada janela candidata, quando apenas um elemento sai e um entra entre janelas vizinhas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha uma contagem de zeros na janela atual. Expanda `right`, incrementando a contagem se `nums[right] == 0`. Enquanto a contagem exceder `k`, encolha `left` (decrementando a contagem só se o elemento que sai é um zero). A cada passo válido, atualize o maior comprimento visto.

## 🎬 Exemplo passo a passo

`nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`

| right | nums[right] | zeros após incluir | Encolhe? | left final | comprimento | melhor |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | não | 0 | 1 | 1 |
| 1 | 1 | 0 | não | 0 | 2 | 2 |
| 2 | 1 | 0 | não | 0 | 3 | 3 |
| 3 | 0 | 1 | não | 0 | 4 | 4 |
| 4 | 0 | 2 | não | 0 | 5 | 5 |
| 5 | 0 | 3 | sim: avança left até o zero de nums[3] sair → left=4, zeros=2 | 4 | 2 | 5 |
| 6 | 1 | 2 | não | 4 | 3 | 5 |
| 7 | 1 | 2 | não | 4 | 4 | 5 |
| 8 | 1 | 2 | não | 4 | 5 | 5 |
| 9 | 1 | 2 | não | 4 | 6 | 6 |
| 10 | 0 | 3 | sim: remove nums[4]=0 → left=5, zeros=2 | 5 | 6 | 6 |

Resultado final: `6` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int longestOnes(int[] nums, int k) {
    int left = 0;
    int zeros = 0;
    int best = 0;

    for (int right = 0; right < nums.length; right++) {
        if (nums[right] == 0) {
            zeros++;
        }

        while (zeros > k) {
            if (nums[left] == 0) {
                zeros--;
            }
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
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

- Só decrementar `zeros` quando o elemento que SAI da janela é de fato um `0` — decrementar sempre (mesmo removendo um `1`) conta zeros errados e encolhe a janela mais do que deveria.
- `k` representa quantos zeros podem ser "gastos" (transformados em 1 via flip), não quantos elementos no total podem ser removidos — a condição de encolhimento é sobre a contagem de zeros na janela, não o tamanho dela.
- Esse é o mesmo padrão de [2379] Minimum Recolors to Get K Consecutive Black Blocks, mas com janela de tamanho VARIÁVEL (aqui queremos o maior comprimento possível) em vez de tamanho fixo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 (nenhum flip) | `nums=[1,0,1,1]`, `k=0` | 2 | sem poder inverter, o maior bloco de 1s consecutivos já existente é a resposta |
| k maior que o total de zeros | `nums=[0,0,1]`, `k=5` | 3 | dá pra inverter todos os zeros, array inteiro vira 1s |
| Só zeros | `nums=[0,0,0]`, `k=2` | 2 | só 2 dos 3 zeros podem virar 1 |
| Exemplo do enunciado | `nums=[1,1,1,0,0,0,1,1,1,1,0]`, `k=2` | 6 | melhor janela usa os 2 flips nos zeros das posições 4 e 10 |

## 🔗 Conexões

- Problemas irmãos: [2379] Minimum Recolors to Get K Consecutive Black Blocks (mesma ideia de contar um elemento "ruim" numa janela, mas com tamanho fixo em vez de buscar o maior tamanho possível), [3090] Maximum Length Substring With Two Occurrences (mesma técnica de expandir e encolher com uma condição de contagem)
- No backend: encontrar a maior sequência de requisições bem-sucedidas permitindo até `k` falhas toleradas dentro da janela, útil para métricas de disponibilidade com tolerância a falhas esporádicas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
