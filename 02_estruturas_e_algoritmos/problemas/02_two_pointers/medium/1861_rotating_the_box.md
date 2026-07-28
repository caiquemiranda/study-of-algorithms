# [1861] Rotating the Box

> 🔗 [LeetCode 1861](https://leetcode.com/problems/rotating-the-box/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Matrix` `#Simulation` `#Medium`

## 📜 O Problema

Dada uma matriz `boxGrid` representando uma caixa vista de lado, com pedras (`'#'`), obstáculos fixos (`'*'`) e espaços vazios (`'.'`), a caixa é rotacionada 90° no sentido horário, e as pedras caem por gravidade (param num obstáculo, noutra pedra, ou no fundo). Retorne a matriz resultante.

**Exemplos:**
```
Input:  boxGrid = [["#",".","#"]]
Output: [["."],["#"],["#"]]
```

**Restrições (e o que elas denunciam):**
- `1 <= m, n <= 500` → O(m×n) esperado, simulação célula a célula repetida seria arriscada
- Obstáculos não se movem, pedras caem até esbarrar em algo → sugere processar cada linha "de baixo pra cima" (ou, antes da rotação, "da direita pra esquerda"), reiniciando o ponto de parada a cada obstáculo

## 🧭 Como reconhecer o padrão

A gravidade age **depois** da rotação, mas é mais simples simular o efeito **antes** de rotacionar: numa rotação de 90° no sentido horário, "cair pra baixo" na matriz final corresponde a "cair pra **direita**" na matriz original. Isso vira um problema de compactar elementos pra um lado dentro de cada linha — a mesma ideia de [0283] Move Zeroes, mas com "paredes" (os obstáculos) que reiniciam a zona de compactação.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada pedra, simular fisicamente a queda célula por célula (mover uma posição de cada vez até esbarrar em algo), repetindo passadas completas pela matriz até nenhuma pedra se mover mais.

- Tempo: O(m×n) por passada, com múltiplas passadas até estabilizar — pode chegar a O((m×n)²) no pior caso (uma pedra "escorregando" célula a célula ao longo de toda a fileira)
- **Por que não basta:** cada pedra pode precisar de até `n` passos individuais pra chegar ao destino final; dois ponteiros resolvem a posição final de TODAS as pedras de uma fileira numa única passada, sem simular o movimento intermediário.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada linha, use um ponteiro `write` começando na posição mais à direita (onde a próxima pedra deve "pousar") e um ponteiro `read` varrendo a linha da direita pra esquerda. Ao encontrar um obstáculo (`'*'`), reinicie `write` para logo à esquerda dele (novo "chão"). Ao encontrar uma pedra (`'#'`), mova-a para a posição `write` (limpando a posição original) e recue `write`. Espaços vazios são ignorados. Depois de aplicar isso em toda linha, faça a rotação 90° de verdade (transposição com inversão de índice).

## 🎬 Exemplo passo a passo

`boxGrid = [["#",".","#"]]` — linha única `"#.#"` (n=3), `write` começa em 2

| Passo | read | row[read] | Ação | write depois | Linha parcial |
|---|---|---|---|---|---|
| 1 | 2 | `#` | limpa `row[2]`, coloca `'#'` em `row[write=2]` | 1 | `"#.#"` (sem mudança visível) |
| 2 | 1 | `.` | nada | 1 | `"#.#"` |
| 3 | 0 | `#` | limpa `row[0]`, coloca `'#'` em `row[write=1]` | 0 | `".##"` |

Linha após gravidade: `".##"`. Rotacionando 90° (matriz 1×3 vira 3×1): resultado = `[["."],["#"],["#"]]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(m × n) — cada linha é compactada em uma passada, mais O(m×n) para a rotação
- **Espaço:** O(m × n) para a matriz de resultado (exigida pelo problema)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public char[][] rotateTheBox(char[][] boxGrid) {
    int m = boxGrid.length;
    int n = boxGrid[0].length;

    // etapa 1: simula a gravidade "pra direita" em cada linha (equivale a "pra baixo" após a rotação)
    for (char[] row : boxGrid) {
        int write = n - 1;
        for (int read = n - 1; read >= 0; read--) {
            if (row[read] == '*') {
                write = read - 1; // obstáculo: reinicia a zona de "queda" logo à esquerda dele
            } else if (row[read] == '#') {
                row[read] = '.';
                row[write] = '#';
                write--;
            }
        }
    }

    // etapa 2: rotação 90° no sentido horário
    char[][] result = new char[n][m];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            result[j][m - 1 - i] = boxGrid[i][j];
        }
    }

    return result;
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

- Esquecer de "limpar" a posição original da pedra (`row[read] = '.'`) antes de movê-la — se `read != write`, deixar o `'#'` original intacto criaria uma pedra duplicada.
- Não reiniciar `write` ao encontrar um obstáculo — o obstáculo é um "chão" novo; pedras à esquerda dele não podem cair além dele, então `write` precisa voltar para `read - 1` nesse ponto.
- Confundir a direção da simulação — a gravidade real age pra BAIXO depois da rotação, mas simular isso ANTES de rotacionar significa que, na matriz original, as pedras precisam cair pra DIREITA; inverter a direção faz o resultado sair espelhado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado (linha após gravidade) | Por quê |
|---|---|---|---|
| Uma pedra e um espaço | `[["#",".","#"]]` | `".##"` | caso mínimo do enunciado |
| Obstáculo interrompe a queda | `[["#",".","*","."]]` | `".#*."` | pedra não passa do obstáculo, zona de queda reinicia |
| Sem pedras | `[[".",".","."]]` | `"..."` | nenhuma pedra pra mover |
| Pedra já compactada | `[[".",".","#"]]` | `"..#"` | pedra já está na posição final, sem mudança |

## 🔗 Conexões

- Problemas irmãos: [0283] Move Zeroes (mesma técnica de compactar elementos pra um lado usando dois ponteiros), [0048] Rotate Image (mesma operação de rotação de matriz 90°, sem a etapa de gravidade)
- No backend: simular reorganização física de itens numa grade sob restrições de "empilhamento" — por exemplo, compactar itens numa prateleira de armazém respeitando divisórias fixas, processando cada fileira independentemente com dois ponteiros.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
