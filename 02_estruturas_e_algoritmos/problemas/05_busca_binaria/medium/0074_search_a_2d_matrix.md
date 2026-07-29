# [0074] Search a 2D Matrix

> 🔗 [LeetCode 74](https://leetcode.com/problems/search-a-2d-matrix/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Matrix` `#Medium`

## 📜 O Problema

Você recebe uma matriz `matrix` de `m x n` com duas propriedades: cada linha é ordenada não decrescente, e o primeiro número de cada linha é maior que o último número da linha anterior (ou seja, a matriz inteira, lida linha por linha, é uma sequência ordenada única). Dado um `target`, retorne se ele existe na matriz.

**Exemplos:**
```
Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3    Output: true
Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13   Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= m, n <= 100` → força bruta O(m×n) chega a 10.000, passaria fácil, mas o enunciado exige explicitamente O(log(m*n))
- "You must write a solution in O(log(m * n)) time complexity" → o produto dentro do log é a pista decisiva: a matriz inteira se comporta como **um único array ordenado de tamanho m×n**, então busca binária "achata" a matriz sem precisar copiá-la
- "o primeiro de cada linha é maior que o último da anterior" → é essa propriedade específica que garante que não existem "quebras" — sem ela, a matriz seria como várias linhas ordenadas independentes (caso do [0240] Search a 2D Matrix II), que exige outra técnica

## 🧭 Como reconhecer o padrão

Quando uma matriz 2D é ordenada de forma que, lida em zigue-zague linha por linha, forma uma sequência **totalmente** ordenada (sem quebras entre linhas), ela é matematicamente equivalente a um array 1D — e qualquer índice `i` desse array 1D mapeia para `matrix[i / n][i % n]`. É a mesma busca binária de sempre, só com uma camada de conversão de índice.

## 🐢 Solução 1 — Força bruta

Percorrer cada célula da matriz (linha por linha, coluna por coluna) comparando com `target`.

- Tempo: O(m × n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige O(log(m*n)) — e ignora que a matriz inteira é, na prática, um único array ordenado "dobrado" em linhas, o que permite busca binária direta em vez de varredura completa.

## 💡 Solução 2 — A ideia otimizada (intuição)

Trate a matriz como um array 1D virtual de tamanho `m*n`, sem copiar nada. Faça busca binária normal nesse índice virtual `[0, m*n - 1]`; para cada `mid`, converta para coordenadas reais: `linha = mid / n`, `coluna = mid % n`, e compare `matrix[linha][coluna]` com `target` como faria num array comum.

## 🎬 Exemplo passo a passo

`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]` (m=3, n=4, total=12), `target = 3`

| Passo | left | mid (virtual) | right | linha, coluna | valor | Comparação | Decisão |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 5 | 11 | (5/4=1, 5%4=1) | matrix[1][1]=11 | 11 > 3 → busca à esquerda | `right = 4` |
| 2 | 0 | 2 | 4 | (2/4=0, 2%4=2) | matrix[0][2]=5 | 5 > 3 → busca à esquerda | `right = 1` |
| 3 | 0 | 0 | 1 | (0/4=0, 0%4=0) | matrix[0][0]=1 | 1 < 3 → busca à direita | `left = 1` |
| 4 | 1 | 1 | 1 | (1/4=0, 1%4=1) | matrix[0][1]=3 | 3 == 3 → achou! | retorna true |

Resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log(m × n)) — busca binária sobre o índice virtual do array "achatado"
- **Espaço:** O(1) — não copia a matriz, só converte índices

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean searchMatrix(int[][] matrix, int target) {
    int m = matrix.length, n = matrix[0].length;
    int left = 0, right = m * n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        // Converte o índice virtual (1D) para coordenadas reais (2D) sem copiar a matriz.
        int valor = matrix[mid / n][mid % n];

        if (valor == target) {
            return true;
        } else if (valor < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return false;
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

- **Trocar `mid / n` por `mid / m`**: a conversão certa usa o número de **colunas** (`n`) para achar a linha e a coluna — usar `m` (número de linhas) mistura tudo.
- **Fazer duas buscas binárias aninhadas (uma pela linha, outra pela coluna)**: funciona (O(log m + log n) = O(log(m*n)) também, matematicamente equivalente), mas é mais código para o mesmo resultado — a busca binária "achatada" é mais direta.
- **Confundir com [0240] Search a 2D Matrix II**: lá as linhas E colunas são ordenadas, mas **sem** a garantia de que a matriz inteira forma uma sequência única — nesse caso, achatar em 1D não funciona, e a técnica precisa ser outra (staircase ou binary search por linha).
- **Matriz com uma única linha ou coluna**: `matrix = [[1]]` (m=n=1) é a borda mínima — o índice virtual varia só entre `0` e `0`, e a conversão `mid/n, mid%n` ainda funciona corretamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Matriz 1x1, presente | `matrix=[[5]], target=5` | true | borda mínima, achou |
| Matriz 1x1, ausente | `matrix=[[5]], target=3` | false | borda mínima, não achou |
| Target é o primeiro elemento | `matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=1` | true | fronteira inicial da matriz achatada |
| Target é o último elemento | `matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=60` | true | fronteira final da matriz achatada |
| Target ausente | `matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13` | false | cai num "buraco" entre linhas |

## 🔗 Conexões

- Problemas irmãos: **[0240] Search a 2D Matrix II** (matriz ordenada por linha E coluna, mas sem a propriedade de sequência única — técnica diferente), **[0704] Binary Search** (o padrão-base que este problema "acha" via conversão de índice)
- No backend: tratar uma estrutura paginada (ex.: resultados de uma query dividida em páginas de tamanho fixo) como um único índice lógico contínuo, convertendo `posição -> (página, offset)`, é o mesmo truque de "achatar" coordenadas usado aqui.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
