# [1351] Count Negative Numbers in a Sorted Matrix

> 🔗 [LeetCode 1351](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Matrix` `#Easy`

## 📜 O Problema

Você recebe uma matriz `grid` de `m x n`, ordenada de forma **não crescente** tanto por linha quanto por coluna (cada linha e cada coluna vai do maior para o menor). Retorne quantos números **negativos** existem em `grid`.

**Exemplos:**
```
Input:  grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]    Output: 8
Input:  grid = [[3,2],[1,0]]                                        Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= m, n <= 100` → matriz pequena (até 10.000 células), até força bruta O(m×n) passaria tranquilo
- "sorted in non-increasing order both row-wise and column-wise" → cada linha é individualmente ordenada (decrescente) — a condição "é negativo" é **monotônica** dentro de cada linha, o convite direto para busca binária por linha
- **Follow up:** "Could you find an O(n+m) solution?" → sinaliza que existe uma técnica ainda mais rápida (caminhada em "escada" usando a ordenação das colunas também), citada como alternativa avançada, mas o binary-search por linha já é a técnica canônica ensinada para este problema dado o tamanho pequeno da matriz

## 🧭 Como reconhecer o padrão

Cada linha da matriz é, isoladamente, um array ordenado decrescente — e "onde a linha deixa de ser não-negativa e passa a ser negativa" é exatamente uma busca por **fronteira monotônica**, a mesma ideia de [0278] First Bad Version aplicada a cada linha.

## 🐢 Solução 1 — Força bruta

Percorrer cada célula da matriz e contar quantas são negativas.

- Tempo: O(m × n) · Espaço: O(1)
- **Por que não basta:** funciona dentro do limite do problema, mas ignora completamente a ordenação de cada linha — para cada linha, dá para achar o início dos negativos em O(log n) em vez de examinar célula por célula.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada linha (que está ordenada decrescente: primeiro os maiores/positivos, depois os negativos no final), faça busca binária pela **primeira posição onde o valor é negativo** — é um upper-bound "invertido": procuramos a fronteira entre "`>= 0`" e "`< 0`".

Uma vez achado esse índice `idx` na linha, a quantidade de negativos naquela linha é `n - idx` (tudo da posição `idx` até o fim). Some isso para todas as `m` linhas.

## 🎬 Exemplo passo a passo

Linha `[1, 1, -1, -2]` (linha de índice 2 do exemplo, `n = 4`)

| Passo | left | mid | right | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 (val 1) | 1 (val 1) | 3 (val -2) | 1 >= 0 → não é negativo | `left = 2` |
| 2 | 2 (val -1) | 2 (val -1) | 3 (val -2) | -1 < 0 → é negativo, candidato | guarda 2, `right = 1` |
| 3 | 2 | — | 1 | `left > right` → fim | primeiro negativo no índice 2 |

Negativos nesta linha: `4 - 2 = 2` (os valores -1 e -2) ✔ — repetindo para as 4 linhas do exemplo (`1+1+2+4`), o total é `8` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(m log n) — busca binária (O(log n)) repetida para cada uma das `m` linhas
- **Espaço:** O(1) — nenhuma estrutura auxiliar, só contadores

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countNegatives(int[][] grid) {
    int total = 0;
    int n = grid[0].length;

    for (int[] linha : grid) {
        total += n - primeiroNegativo(linha);
    }
    return total;
}

// Busca binária: acha o índice do primeiro elemento negativo na linha
// (a linha está ordenada não-crescente, então os negativos ficam todos no final).
private int primeiroNegativo(int[] linha) {
    int left = 0, right = linha.length - 1;
    int resultado = linha.length;          // se não achar negativo nenhum, resultado = length (zero negativos)

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (linha[mid] < 0) {
            resultado = mid;               // mid é negativo: candidato válido, tenta achar um índice menor ainda
            right = mid - 1;
        } else {
            left = mid + 1;                // mid não é negativo: fronteira está mais à direita
        }
    }
    return resultado;
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

- **Esquecer o caso "linha sem nenhum negativo"**: se a busca binária nunca encontra um valor negativo, `resultado` precisa ficar em `linha.length` (zero negativos) — inicializar a variável errado (ex.: com `-1` ou `0`) gera contagem incorreta.
- **Confundir "não crescente" com "estritamente decrescente"**: a matriz permite repetições (ex.: `[1,1,-1,-2]` tem dois `1`s) — a busca binária por fronteira lida bem com isso naturalmente, só um scan ingênuo que assume valores únicos quebraria.
- **Ignorar a otimização de colunas**: o follow-up O(n+m) usa uma "caminhada em escada" (começar no canto inferior-esquerdo e mover para cima/direita usando a ordenação de linhas E colunas simultaneamente) — mais rápida para matrizes bem quadradas, mas mais complexa de implementar; para `m, n <= 100`, o ganho prático é mínimo.
- **Aplicar busca binária na matriz inteira como se fosse 1D**: cada linha precisa da sua própria busca — a ordenação por coluna não torna a matriz "linearizável" em uma única busca binária direta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem negativos | `grid=[[3,2],[1,0]]` | 0 | testa a busca binária retornando "não achou" em toda linha |
| Todos negativos | `grid=[[-1,-2],[-3,-4]]` | 4 | testa a busca binária retornando índice 0 em toda linha |
| Matriz 1x1 negativa | `grid=[[-5]]` | 1 | borda mínima |
| Matriz 1x1 não negativa | `grid=[[0]]` | 0 | zero não conta como negativo |
| Exemplo do enunciado | `grid=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]` | 8 | trace acima, soma das 4 linhas |

## 🔗 Conexões

- Problemas irmãos: **[0278] First Bad Version** (mesma busca binária por fronteira monotônica, aplicada linha a linha aqui), **[0074] Search a 2D Matrix** (busca binária tratando a matriz como um array 1D "achatado")
- No backend: contar registros que satisfazem uma condição em dados particionados-e-ordenados (ex.: quantas linhas de um relatório já ordenado por data e por região estão "vencidas") é resolvido com a mesma ideia — busca binária por partição em vez de varrer tudo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
