# [0035] Search Insert Position

> 🔗 [LeetCode 35](https://leetcode.com/problems/search-insert-position/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array **ordenado** de inteiros **distintos** e um `target`. Se `target` existe no array, retorne o índice dele. Se não existe, retorne o índice onde ele **entraria** para manter o array ordenado.

**Exemplos:**
```
Input:  nums = [1,3,5,6], target = 5    Output: 2   (5 está no índice 2)
Input:  nums = [1,3,5,6], target = 2    Output: 1   (2 entraria entre 1 e 3)
Input:  nums = [1,3,5,6], target = 7    Output: 4   (7 entraria depois do fim)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → O(n) até passaria, mas o enunciado exige explicitamente O(log n)
- "You must write an algorithm with O(log n) runtime complexity" → é o convite direto para busca binária
- `nums` contém valores **distintos** ordenados **ascendentemente** → sem duplicatas, cada comparação decide com certeza

## 🧭 Como reconhecer o padrão

"Array ordenado" + "ache o índice de X (ou onde X entraria) em O(log n)" é a assinatura mais pura de busca binária. A parte interessante é que "índice de inserção" nada mais é do que **a posição do primeiro elemento >= target** — ou seja, um "lower bound" clássico (ver [fundamentos](../../../fundamentos/05_busca_binaria.md)).

## 🐢 Solução 1 — Força bruta

Percorrer o array da esquerda para a direita e parar no primeiro elemento `>= target`; se chegar ao fim, o índice é `nums.length`.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige O(log n) explicitamente, e ignora a informação mais valiosa do problema — o array já está ordenado, então dá para descartar metade dos candidatos a cada comparação.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de pensar "existe o target?", pense "qual é o primeiro índice cujo valor é `>= target`?". Fazendo busca binária com essa pergunta, o resultado serve para os dois casos ao mesmo tempo:
- Se `nums[índice] == target`, é a posição dele.
- Se não achar, sobra exatamente a posição onde ele entraria (o primeiro valor maior que ele).

A cada passo, se `nums[mid] < target`, sabemos que mid e tudo antes dele é irrelevante — a resposta está estritamente à direita (`left = mid + 1`). Se `nums[mid] >= target`, mid é um candidato válido, mas pode existir um candidato melhor (mais à esquerda) — então guardamos mid como candidato e continuamos buscando à esquerda (`right = mid - 1`). Quando o laço termina, `left` é a resposta.

## 🎬 Exemplo passo a passo

`nums = [1, 3, 5, 6]`, `target = 2`

| Passo | left | mid | right | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 (val 1) | 1 (val 3) | 3 (val 6) | 3 >= 2 → candidato válido | `right = 0` |
| 2 | 0 (val 1) | 0 (val 1) | 0 (val 1) | 1 < 2 → descarta mid | `left = 1` |
| 3 | 1 | — | 0 | `left > right` → fim | retorna `left = 1` |

Resultado final: `1` ✔ (2 entraria entre o índice 0 e o 1)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do espaço de busca
- **Espaço:** O(1) — só dois/três ponteiros, versão iterativa

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int searchInsert(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {
        // left + (right-left)/2 evita overflow de int em arrays gigantes
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;                     // achou exatamente o alvo
        } else if (nums[mid] < target) {
            left = mid + 1;                 // resposta está estritamente à direita
        } else {
            right = mid - 1;                // mid é candidato, mas busca à esquerda por um melhor
        }
    }
    // Quando o laço termina, "left" ultrapassou "right" e aponta exatamente
    // para o primeiro elemento >= target — que é o índice de inserção.
    return left;
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

- **Retornar `mid` em vez de `left` ao final**: quando o target não existe, o laço termina com `left > right`, e é `left` (não `mid` da última iteração) que guarda a resposta correta.
- **Usar `right = mid` em vez de `mid - 1`**: sem decrementar, o laço pode não convergir (loop infinito) quando o candidato válido é o próprio `mid`.
- **Target menor que todo mundo ou maior que todo mundo**: são as bordas que mais derrubam soluções ingênuas — teste sempre `target` antes do primeiro e depois do último elemento.
- **Confundir com "achar o valor exato"**: aqui a busca binária precisa devolver uma posição mesmo quando o valor não está no array — não é um "existe/não existe" simples.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento, achou | `nums=[5], target=5` | 0 | borda mínima, valor existe |
| Um elemento, não achou | `nums=[5], target=2` | 0 | entraria antes do único elemento |
| Menor que todos | `nums=[1,3,5,6], target=0` | 0 | entraria no início |
| Maior que todos | `nums=[1,3,5,6], target=7` | 4 | entraria no fim (índice = length) |
| Valor exato no meio | `nums=[1,3,5,6], target=5` | 2 | caso feliz, achou de cara |

## 🔗 Conexões

- Problemas irmãos: **[0704] Binary Search** (a busca binária "pura", sem o caso de inserção), **[0034] Find First and Last Position of Element in Sorted Array** (mesma técnica de lower bound, aplicada duas vezes)
- No backend: é exatamente o que uma função `bisect.insort` (Python) ou um índice B-tree fazem para manter uma coleção ordenada — encontrar em O(log n) onde um novo registro deve entrar sem precisar reordenar tudo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
