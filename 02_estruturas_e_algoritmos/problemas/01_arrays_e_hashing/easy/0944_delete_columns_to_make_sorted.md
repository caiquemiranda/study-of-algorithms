# [0944] Delete Columns to Make Sorted

> 🔗 [LeetCode 944](https://leetcode.com/problems/delete-columns-to-make-sorted/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#String` `#Easy`

## 📜 O Problema

Você recebe um array de `n` strings `strs`, todas do mesmo tamanho. As strings podem ser dispostas uma em cada linha, formando uma grade.

Você quer **deletar** as colunas que **não estão ordenadas lexicograficamente**. Uma coluna está ordenada se, lendo de cima para baixo, os caracteres estão em ordem não-decrescente.

Retorne **o número de colunas que você vai deletar**.

**Exemplos:**
```
Input:  strs = ["cba","daf","ghi"]
Output: 1
Explicação: a grade é
  cba
  daf
  ghi
Colunas 0 e 2 estão ordenadas, mas a coluna 1 ('b','a','h') não, então só 1 coluna precisa ser deletada.

Input:  strs = ["a","b"]
Output: 0

Input:  strs = ["zyx","wvu","tsr"]
Output: 3
Explicação: todas as 3 colunas estão desordenadas.
```

**Restrições (e o que elas denunciam):**
- `n == strs.length`, `1 <= n <= 100`, `1 <= strs[i].length <= 1000` → até 100.000 caracteres, O(colunas × linhas) resolve com folga
- todas as strings têm o MESMO comprimento → cada "coluna" é bem definida para todas as linhas

## 🧭 Como reconhecer o padrão

"Verifique uma propriedade coluna por coluna numa grade formada por strings de mesmo tamanho" é resolvido transpondo o raciocínio: para cada índice de coluna, percorra as linhas comparando pares consecutivos.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada coluna, percorrer todas as linhas comparando `strs[i][coluna]` com `strs[i-1][coluna]`; se algum par estiver fora de ordem, a coluna precisa ser deletada — na prática, já é essencialmente a solução ótima, pois não há uma versão "pior" relevante aqui.

- Tempo: O(colunas × linhas) — inevitável, pois cada célula da grade precisa ser olhada pelo menos uma vez · Espaço: O(1) extra
- **Por que vale nomear mesmo assim:** a armadilha aqui não é de complexidade, é de organização — iterar "coluna por fora, linha por dentro" (em vez de linha por fora) é o que torna a lógica de comparação simples.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada índice de coluna `c`, percorra as linhas de `i=1` até `n-1` comparando `strs[i].charAt(c)` com `strs[i-1].charAt(c)`. Se algum caractere for menor que o da linha anterior na mesma coluna, a coluna não está ordenada — conte-a e passe para a próxima coluna sem checar o resto das linhas.

## 🎬 Exemplo passo a passo

`strs = ["cba","daf","ghi"]`

| Passo | coluna | comparação de linhas | ordenada? | contador |
|---|---|---|---|---|
| 1 | 0 | 'c'≤'d'≤'g' | sim | 0 |
| 2 | 1 | 'b'≤'a'? não | não | 1 |
| 3 | 2 | 'a'≤'f'≤'i' | sim | 1 |

Resultado final: `1` ✔ (só a coluna 1 é deletada)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(colunas × linhas)
- **Espaço:** O(1) extra

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minDeletionSize(String[] strs) {
    int colunas = strs[0].length();
    int linhas = strs.length;
    int deletadas = 0;

    for (int c = 0; c < colunas; c++) {
        for (int i = 1; i < linhas; i++) {
            if (strs[i].charAt(c) < strs[i - 1].charAt(c)) {
                deletadas++; // esta coluna já não está ordenada, não precisa checar as outras linhas
                break;
            }
        }
    }
    return deletadas;
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

- Trocar a ordem dos loops (linha por fora, coluna por dentro) sem acumular corretamente "esta coluna já foi marcada" — leva a contar a mesma coluna mais de uma vez se não houver cuidado extra; iterar coluna por fora evita esse problema naturalmente.
- Usar `<=` em vez de `<` na comparação — colunas ordenadas permitem igualdade (`'b' <= 'b'` é válido, não desordenado); só `strs[i][c] < strs[i-1][c]` indica quebra de ordem.
- Esquecer o `break` ao encontrar a primeira quebra numa coluna — sem ele, a mesma coluna poderia ser contada mais de uma vez se houver múltiplas quebras nela.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Uma coluna desordenada | `["cba","daf","ghi"]` | 1 | só a coluna 1 quebra a ordem |
| Uma única coluna, uma letra por string | `["a","b"]` | 0 | uma única letra por string, sempre ordenada com uma linha |
| Todas as colunas desordenadas | `["zyx","wvu","tsr"]` | 3 | ordem estritamente decrescente em toda coluna |
| Já totalmente ordenado | `["abc","abd","abe"]` | 0 | nenhuma coluna precisa ser removida |

## 🔗 Conexões

- Problemas irmãos: [0955] Delete Columns to Make Sorted II (mesma ideia, mas com uma condição global de ordenação lexicográfica em vez de coluna por coluna), [0014] Longest Common Prefix (mesma técnica de percorrer posição por posição comparando todas as strings)
- No backend: validação de colunas de dados tabulares (ex.: CSV) que precisam estar ordenadas — útil em pipelines de qualidade de dados que verificam se cada campo respeita uma ordenação esperada antes de processar.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
