# [0905] Sort Array By Parity

> 🔗 [LeetCode 905](https://leetcode.com/problems/sort-array-by-parity/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array `nums`, mova todos os números **pares** para o início e todos os **ímpares** para o fim. Retorne **qualquer** array que satisfaça essa condição (a ordem dentro de cada grupo não importa).

**Exemplos:**
```
Input:  nums = [3,1,2,4]
Output: [2,4,3,1]
Explicação: [4,2,3,1], [2,4,1,3] e [4,2,1,3] também seriam aceitos.

Input:  nums = [0]
Output: [0]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 5000` → O(n) esperado
- `0 <= nums[i] <= 5000` → só não-negativos, então `% 2` sempre dá `0` ou `1` sem surpresas
- Aceita **qualquer** array válido → não precisa preservar a ordem relativa dentro de cada grupo, o que abre espaço pra trocas "livres" com dois ponteiros

## 🧭 Como reconhecer o padrão

"Particionar um array em dois grupos por uma condição binária, sem se importar com a ordem interna" é resolvido com dois ponteiros nas pontas: um vindo da esquerda procurando um ímpar fora do lugar, outro vindo da direita procurando um par fora do lugar — quando os dois acham algo errado, trocam de posição.

## 🐢 Solução 1 — Força bruta (duas listas)

Percorrer o array uma vez, colocando os pares numa lista e os ímpares em outra; depois concatenar as duas listas (pares primeiro).

- Tempo: O(n) · Espaço: O(n) — duas listas auxiliares guardando todos os elementos
- **Por que não basta:** já é O(n) em tempo, mas usa espaço extra proporcional ao tamanho da entrada; dois ponteiros fazem a mesma reorganização in-place, trocando elementos diretamente no array original.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no início e `right` no fim. Avance `left` enquanto `nums[left]` já for par (já está no lugar certo). Recue `right` enquanto `nums[right]` já for ímpar (também já está certo). Quando `left` parar num ímpar e `right` parar num par, os dois estão "trocados" — troque-os de posição e continue.

## 🎬 Exemplo passo a passo

`nums = [3,1,2,4]` (índices 0 a 3)

| Passo | left | right | nums[left] | nums[right] | Ação |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 3 (ímpar) | 4 (par) | troca → `[4,1,2,3]`; left=1, right=2 |
| 2 | 1 | 2 | 1 (ímpar) | 2 (par) | troca → `[4,2,1,3]`; left=2, right=1 |
| 3 | 2 | 1 | — | — | `left >= right`, loop termina |

Resultado final: `[4,2,1,3]` ✔ (uma das saídas explicitamente aceitas pelo enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada elemento é visitado no máximo uma vez por cada ponteiro
- **Espaço:** O(1) — só os índices `left`/`right` e uma variável temporária pra troca

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] sortArrayByParity(int[] nums) {
    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
        if (nums[left] % 2 == 0) {
            left++; // já é par, já está no lugar certo
        } else if (nums[right] % 2 == 1) {
            right--; // já é ímpar, já está no lugar certo
        } else {
            // nums[left] é ímpar e nums[right] é par: os dois estão trocados
            int tmp = nums[left];
            nums[left] = nums[right];
            nums[right] = tmp;
            left++;
            right--;
        }
    }

    return nums;
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

- Avançar os dois ponteiros junto com o swap, mesmo quando só um deles precisava mover — se `nums[left]` já é par (não precisa de swap), avançar `right` também faria pular uma posição sem checá-la.
- Achar que a ordem relativa dentro dos pares/ímpares precisa ser preservada — o enunciado aceita **qualquer** array válido, então trocar posições livremente com swap é permitido (ao contrário de, por exemplo, [0026] Remove Duplicates, que exige preservar ordem).
- Assumir que `%` pode dar resultado negativo — aqui a constraint garante `nums[i] >= 0`, então `% 2` sempre é `0` ou `1`; em contextos com números negativos, essa checagem de paridade precisaria de cuidado extra.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado (uma saída válida) | Por quê |
|---|---|---|---|
| Caso padrão | `[3,1,2,4]` | `[4,2,1,3]` (ou outra válida) | mistura de pares e ímpares |
| Único elemento | `[0]` | `[0]` | `left == right`, loop não executa |
| Já ordenado | `[2,4,1,3]` | `[2,4,1,3]` (sem swaps) | `left` sempre encontra par, `right` sempre encontra ímpar |
| Todos pares | `[2,4,6]` | `[2,4,6]` | nenhum swap necessário, `left` avança até o fim |

## 🔗 Conexões

- Problemas irmãos: [0922] Sort Array By Parity II (mesma ideia, mas exige alternância estrita par/ímpar por posição), [0075] Sort Colors (mesma família de particionamento in-place com múltiplos ponteiros, mas em 3 grupos)
- No backend: particionar uma coleção in-place por uma condição binária — por exemplo, separar registros ativos de inativos antes de processar em lote, sem alocar duas listas separadas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
