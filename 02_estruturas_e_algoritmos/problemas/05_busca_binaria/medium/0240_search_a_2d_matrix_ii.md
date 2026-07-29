# [0240] Search a 2D Matrix II

> 🔗 [LeetCode 240](https://leetcode.com/problems/search-a-2d-matrix-ii/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Matrix` `#Medium`

## 📜 O Problema

Escreva um algoritmo eficiente para buscar um `target` numa matriz `m x n` onde: cada **linha** é ordenada crescente da esquerda para a direita, e cada **coluna** é ordenada crescente de cima para baixo. **Diferente de [0074] Search a 2D Matrix**, não existe garantia de que a matriz inteira forme uma sequência única (o primeiro elemento de uma linha pode ser menor que o último da linha anterior).

**Exemplos:**
```
Input:  matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
                   [10,13,14,17,24],[18,21,23,26,30]], target = 5     Output: true
Input:  matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
                   [10,13,14,17,24],[18,21,23,26,30]], target = 20    Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= n, m <= 300` → força bruta O(m×n) chega a 90.000, passa fácil, mas o enunciado pede explicitamente um "algoritmo eficiente"
- "Integers in each row/column are sorted in ascending order" (sem a garantia extra do LC 74) → **não** dá para achatar a matriz num único array 1D ordenado — a técnica de [0074] não se aplica aqui
- Cada linha, isoladamente, é um array ordenado → habilita busca binária **por linha**, mesmo sem a estrutura global do LC 74

## 🧭 Como reconhecer o padrão

Sem a garantia de sequência única, a matriz não pode ser tratada como um array 1D — mas cada linha continua sendo, isoladamente, um candidato perfeito para busca binária. Repetir a busca binária para cada linha resolve em O(m log n), mais lento que o "achatamento" do LC 74, mas ainda muito melhor que varrer tudo.

## 🐢 Solução 1 — Força bruta

Percorrer cada célula da matriz comparando com `target`.

- Tempo: O(m × n) · Espaço: O(1)
- **Por que não basta:** o enunciado pede um algoritmo eficiente — e ignora que cada linha (ou coluna) já está ordenada, permitindo eliminar candidatos em blocos em vez de célula por célula.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada linha da matriz, faça uma busca binária normal por `target` (a linha é um array ordenado comum). Se `target` estiver fora do intervalo `[linha[0], linha[n-1]]`, pule a busca binária naquela linha (otimização simples, já que ela certamente não contém o alvo). Se alguma busca encontrar `target`, retorna `true`; se todas as linhas forem testadas sem sucesso, retorna `false`.

> Existe uma técnica ainda mais rápida (O(m+n)): começar no canto **superior direito** e, a cada passo, mover para a **esquerda** se o valor atual for maior que `target`, ou para **baixo** se for menor — cada passo elimina uma linha OU uma coluna inteira. Veja a nota nas pegadinhas.

## 🎬 Exemplo passo a passo

`matrix` do enunciado, `target = 5`

| Linha | Array | Binary search encontra 5? |
|---|---|---|
| 0 | [1,4,7,11,15] | não (5 cairia entre os índices de 4 e 7) |
| 1 | [2,5,8,12,19] | sim |

Detalhe da busca binária na linha 1:

| Passo | left | mid | right | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 (2) | 2 (8) | 4 (19) | 8 > 5 → busca à esquerda | `right = 1` |
| 2 | 0 (2) | 0 (2) | 1 (5) | 2 < 5 → busca à direita | `left = 1` |
| 3 | 1 (5) | 1 (5) | 1 (5) | 5 == 5 → achou! | retorna true |

Resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(m log n) — busca binária (O(log n)) repetida para cada uma das `m` linhas
- **Espaço:** O(1) — nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean searchMatrix(int[][] matrix, int target) {
    for (int[] linha : matrix) {
        // Poda simples: se target está fora do intervalo da linha, nem tenta buscar nela.
        if (target < linha[0] || target > linha[linha.length - 1]) {
            continue;
        }
        if (buscaBinaria(linha, target)) {
            return true;
        }
    }
    return false;
}

private boolean buscaBinaria(int[] linha, int target) {
    int left = 0, right = linha.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (linha[mid] == target) {
            return true;
        } else if (linha[mid] < target) {
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

- **Tentar aplicar a técnica do LC 74 (achatar em 1D)**: quebra silenciosamente aqui, porque não existe garantia de que o primeiro elemento de uma linha seja maior que o último da linha anterior — a matriz NÃO é uma sequência única ordenada.
- **Esquecer a poda pelo intervalo `[linha[0], linha[n-1]]`**: sem ela, o algoritmo ainda funciona corretamente, mas gasta busca binária completa em linhas que obviamente não contêm o alvo.
- **Não conhecer a técnica staircase (O(m+n))**: começando no canto superior direito, se `matrix[linha][coluna] > target`, o alvo não pode estar naquela coluna (ela só cresce para baixo) → mova uma coluna para a esquerda; se for menor, o alvo não pode estar naquela linha (ela só cresce para a direita) → mova uma linha para baixo. Essa é a técnica mais citada como "a" solução deste problema, e vale conhecer mesmo que a busca binária por linha já resolva dentro do esperado.
- **Confundir com o LC 74**: são primos próximos, mas a estrutura da matriz é sutilmente diferente — misturar as duas soluções gera bugs difíceis de notar em testes pequenos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Matriz 1x1, presente | `matrix=[[5]], target=5` | true | borda mínima |
| Target menor que tudo | `matrix=[[1,4,7],[2,5,8],[3,6,9]], target=0` | false | poda por intervalo evita busca desnecessária |
| Target maior que tudo | `matrix=[[1,4,7],[2,5,8],[3,6,9]], target=100` | false | mesma poda, no extremo oposto |
| Target ausente "no meio" | `matrix` do enunciado, `target=20` | false | cai num buraco real da matriz (exemplo 2) |
| Exemplo do enunciado | `matrix` do enunciado, `target=5` | true | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0074] Search a 2D Matrix** (estrutura mais forte, permite achatar em 1D), **[1351] Count Negative Numbers in a Sorted Matrix** (mesma ideia de busca binária por linha numa matriz ordenada em ambas as direções)
- No backend: buscar um valor numa estrutura particionada onde cada partição está ordenada, mas as partições entre si não têm relação de ordem total (ex.: shards de um banco distribuído, cada um ordenado internamente) usa exatamente essa estratégia de busca binária por partição.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
