# [0832] Flipping an Image

> 🔗 [LeetCode 832](https://leetcode.com/problems/flipping-an-image/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#BitManipulation` `#Matrix` `#Easy`

## 📜 O Problema

Dada uma matriz binária `n x n`, **inverta cada linha horizontalmente** (reverta a ordem dos elementos) e depois **inverta os bits** (cada `0` vira `1` e vice-versa). Retorne a matriz resultante.

**Exemplos:**
```
Input:  image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explicação: reverte cada linha → [[0,1,1],[1,0,1],[0,0,0]], depois inverte os bits.
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 20` → matriz pequena, qualquer solução O(n²) é rápida o suficiente; o ganho aqui é de elegância/passadas, não de ordem de grandeza
- Duas operações separadas no enunciado (reverter + inverter) → sugere que dá pra combiná-las numa única passada por linha, já que cada uma afeta uma posição só uma vez

## 🧭 Como reconhecer o padrão

"Reverter uma linha e aplicar uma transformação simples a cada elemento" é dois ponteiros nas pontas ([0344] Reverse String), com um adicional: em vez de só trocar os dois valores de lugar, você já entrega o valor **invertido** (`1 - valor`) na troca, fundindo as duas operações do enunciado num único passo por par de posições.

## 🐢 Solução 1 — Força bruta (duas passadas por linha)

Para cada linha, primeiro reverter (copiando para um array temporário de trás pra frente, ou usando um método pronto), e depois, numa segunda passada, inverter cada bit (`0` ↔ `1`).

- Tempo: O(n²) — já é o mínimo necessário, pois toda célula da matriz precisa ser tocada · Espaço: O(n) por linha se usar um array temporário para reverter
- **Por que não basta:** embora já seja ótimo em tempo assintótico, faz **duas passadas completas** por linha (uma para reverter, outra para inverter) e pode alocar uma cópia temporária; dois ponteiros combinam as duas operações numa única passada por linha, sem alocar nada extra.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada linha, use `left` no início e `right` no fim. Em vez de só trocar `row[left]` com `row[right]`, atribua a cada posição o valor **invertido** do lado oposto: `row[left] = 1 - row[right]` e `row[right] = 1 - row[left original]` (usando uma variável temporária pra não perder o valor original de `row[left]`). Se a linha tiver tamanho ímpar, o elemento do meio (`left == right`) não tem par pra trocar — só precisa ser invertido sozinho.

## 🎬 Exemplo passo a passo

Linha `[1,0,1]` (segunda linha do exemplo do enunciado, n=3)

| Passo | left | right | Ação | Linha depois |
|---|---|---|---|---|
| 1 | 0 | 2 | guarda `temp = row[0] = 1`; `row[0] = 1 - row[2] = 0`; `row[2] = 1 - temp = 0` | `[0,0,0]` (índice 1 ainda intocado) |
| 2 | 1 | 1 | `left == right` (meio): `row[1] = 1 - row[1] = 1` | `[0,1,0]` |

Resultado final da linha: `[0,1,0]` ✔ (bate com a linha 1 do output do enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) — cada uma das n linhas tem seus n elementos visitados uma única vez
- **Espaço:** O(1) extra — modifica a matriz in-place, sem array auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[][] flipAndInvertImage(int[][] image) {
    int n = image.length;

    for (int[] row : image) {
        int left = 0;
        int right = n - 1;

        while (left <= right) {
            if (left == right) {
                row[left] = 1 - row[left]; // elemento do meio: só inverte, sem par pra trocar
            } else {
                int temp = row[left];
                // troca as posições E já inverte o bit no mesmo passo
                row[left] = 1 - row[right];
                row[right] = 1 - temp;
            }
            left++;
            right--;
        }
    }

    return image;
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

- Reverter e inverter em duas passadas separadas — funciona, mas duplica o trabalho; combinar as duas operações num único swap (`1 - valor`) resolve em uma passada por linha.
- Esquecer o caso `left == right` (linha de tamanho ímpar) — o elemento do meio não tem par simétrico pra trocar, só precisa ser invertido sozinho.
- Usar `row[right]` já sobrescrito ao calcular `row[left]`, ou vice-versa — é por isso que a variável `temp` guarda o valor **original** de `row[left]` antes de qualquer escrita; sem ela, o cálculo do segundo lado usaria um valor já modificado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Matriz 1x1 | `[[0]]` | `[[1]]` | linha de tamanho 1: só inverte, sem swap |
| Linha ímpar | `[[1,0,1]]` | `[[0,1,0]]` | testa o elemento do meio isoladamente |
| Linha par "coincidente" | `[[1,1,0,0]]` | `[[1,1,0,0]]` | reverter + inverter pode devolver a mesma linha por coincidência |
| Exemplo do enunciado (matriz completa) | `[[1,1,0],[1,0,1],[0,0,0]]` | `[[1,0,0],[0,1,0],[1,1,1]]` | caso padrão com múltiplas linhas |

## 🔗 Conexões

- Problemas irmãos: [0344] Reverse String (mesma técnica de swap com dois ponteiros, sem a inversão de bits), [0048] Rotate Image (também manipula uma matriz in-place, mas com rotação em vez de flip horizontal)
- No backend: processamento de imagens binárias/máscaras — por exemplo, espelhar e negar uma máscara de bits usada em compressão ou processamento gráfico simples, com operações in-place sem alocar buffers extras.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
