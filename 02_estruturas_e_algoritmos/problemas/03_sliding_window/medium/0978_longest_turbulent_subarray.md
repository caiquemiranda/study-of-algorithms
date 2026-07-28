# [0978] Longest Turbulent Subarray

> 🔗 [LeetCode 978](https://leetcode.com/problems/longest-turbulent-subarray/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#DynamicProgramming` `#Medium`

## 📜 O Problema

Dado um array de inteiros `arr`, retorne o comprimento do maior subarray **turbulento**. Um subarray é turbulento se o sinal da comparação entre elementos adjacentes alterna a cada par: ou (`>`, `<`, `>`, `<`, ...) ou (`<`, `>`, `<`, `>`, ...).

**Exemplos:**
```
Input:  arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explicação: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

Input:  arr = [4,8,12,16]
Output: 2

Input:  arr = [100]
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 4 * 10^4` → O(n²) força bruta é arriscado; O(n) é o esperado
- `0 <= arr[i] <= 10^9` → valores grandes, mas sem risco de overflow (só comparações)

## 🧭 Como reconhecer o padrão

"Maior subarray onde o sinal da comparação entre vizinhos alterna" é resolvido mantendo dois contadores — `up` (comprimento do trecho turbulento terminando na posição atual cuja última comparação foi uma subida) e `down` (idem, mas terminando numa descida) — que se alimentam um do outro a cada passo, estendendo o "run" enquanto a alternância se mantém e resetando quando quebra.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, checar se todas as comparações consecutivas dentro do subarray alternam de sinal.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** revalida a alternância do zero a cada subarray candidato, mesmo quando ele é apenas o anterior estendido em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array comparando cada par de vizinhos. Se `arr[i] > arr[i-1]` (subida), `up = down + 1` e `down = 1` (a subida só pode estender um trecho que terminou em descida). Se `arr[i] < arr[i-1]` (descida), o inverso. Se forem iguais, ambos resetam para `1` (elementos iguais quebram qualquer turbulência).

## 🎬 Exemplo passo a passo

`arr = [9,4,2,10,7,8,8,1,9]`

| i | arr[i] vs arr[i-1] | up | down | melhor |
|---|---|---|---|---|
| 0 | — (início) | 1 | 1 | 1 |
| 1 | 4<9 (desce) | 1 | 2 | 2 |
| 2 | 2<4 (desce de novo) | 1 | 2 | 2 |
| 3 | 10>2 (sobe) | 3 | 1 | 3 |
| 4 | 7<10 (desce) | 1 | 4 | 4 |
| 5 | 8>7 (sobe) | 5 | 1 | 5 |
| 6 | 8==8 (igual) | 1 | 1 | 5 |
| 7 | 1<8 (desce) | 1 | 2 | 5 |
| 8 | 9>1 (sobe) | 3 | 1 | 5 |

Resultado final: `5` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxTurbulenceSize(int[] arr) {
    int up = 1;
    int down = 1;
    int best = 1;

    for (int i = 1; i < arr.length; i++) {
        if (arr[i] > arr[i - 1]) {
            up = down + 1;
            down = 1;
        } else if (arr[i] < arr[i - 1]) {
            down = up + 1;
            up = 1;
        } else {
            up = 1;
            down = 1;
        }
        best = Math.max(best, Math.max(up, down));
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

- `up` e `down` representam o comprimento do subarray turbulento terminando em `i` cuja última comparação foi, respectivamente, uma subida ou uma descida — atualizar um baseado no valor ANTERIOR do outro (não do mesmo) é o que garante a alternância.
- Elementos iguais (`arr[i] == arr[i-1]`) quebram qualquer turbulência — resetam `up` e `down` para 1, já que nem subida nem descida ocorreu.
- Inicializar `up` e `down` em `0` (em vez de `1`) faz o comprimento mínimo de um subarray de um único elemento ficar errado — todo array de tamanho >= 1 tem pelo menos um subarray turbulento de comprimento 1 (ele mesmo).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Array de um elemento | `[100]` | 1 | um único elemento é sempre um subarray turbulento trivial |
| Estritamente crescente (sem alternância) | `[4,8,12,16]` | 2 | qualquer par adjacente já é turbulento; três seguidos na mesma direção não |
| Elementos iguais quebram tudo | `[5,5,5]` | 1 | nenhuma subida nem descida ocorre em nenhum par |
| Exemplo do enunciado | `[9,4,2,10,7,8,8,1,9]` | 5 | subarray [4,2,10,7,8] (índices 1-5) alterna perfeitamente |

## 🔗 Conexões

- Problemas irmãos: [2760] Longest Even Odd Subarray With Threshold (mesma família de "expandir enquanto uma condição de alternância entre vizinhos se mantém"), [0413] Arithmetic Slices (mesma ideia de manter contadores incrementais que se resetam quando a condição quebra)
- No backend: detectar padrões de oscilação em séries temporais (ex.: preço de uma ação subindo e descendo alternadamente), útil para identificar volatilidade ou ruído versus tendência estável.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
