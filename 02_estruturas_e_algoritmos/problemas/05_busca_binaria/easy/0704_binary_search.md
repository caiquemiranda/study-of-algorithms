# [0704] Binary Search

> 🔗 [LeetCode 704](https://leetcode.com/problems/binary-search/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums` **ordenado crescentemente** e um `target`, encontre o índice de `target` no array. Se não existir, retorne `-1`.

**Exemplos:**
```
Input:  nums = [-1,0,3,5,9,12], target = 9    Output: 4
Input:  nums = [-1,0,3,5,9,12], target = 2    Output: -1
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → O(n) passaria, mas o enunciado exige explicitamente O(log n)
- "You must write an algorithm with O(log n) runtime complexity" → é o convite mais direto possível para busca binária: este é literalmente o problema-título da categoria
- "nums is sorted in ascending order", "all the integers in nums are unique" → sem duplicatas, cada comparação decide com certeza qual metade descartar

## 🧭 Como reconhecer o padrão

Este É o padrão: array ordenado + encontrar um valor em O(log n). Todo problema desta categoria é uma variação disto — busca por fronteira, busca na resposta, busca em array rotacionado — mas a essência é sempre a mesma: manter um intervalo `[left, right]` que contém a resposta e descartar metade dele a cada comparação com o elemento do meio.

## 🐢 Solução 1 — Força bruta

Percorrer o array do início ao fim comparando cada elemento com `target`.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige O(log n) explicitamente — e ignora completamente a informação de que o array está ordenado. Se `nums[i]` não é o alvo, saber se ele é maior ou menor já diz de que lado buscar; percorrer sequencialmente joga essa informação fora.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha dois ponteiros, `left` e `right`, delimitando a região onde `target` ainda pode estar. A cada passo, olhe o elemento do meio (`mid`):
- Se `nums[mid] == target`, achou — retorna `mid`.
- Se `nums[mid] < target`, o array ordenado garante que tudo até `mid` (inclusive) é menor que o alvo → descarta a metade esquerda, `left = mid + 1`.
- Se `nums[mid] > target`, descarta a metade direita, `right = mid - 1`.

Se `left` ultrapassar `right`, o intervalo de busca ficou vazio — `target` não existe no array.

## 🎬 Exemplo passo a passo

`nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

| Passo | left | mid | right | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 (val -1) | 2 (val 3) | 5 (val 12) | 3 < 9 → busca à direita | `left = 3` |
| 2 | 3 (val 5) | 4 (val 9) | 5 (val 12) | 9 == 9 → achou! | retorna 4 |

Resultado final: `4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do espaço de busca
- **Espaço:** O(1) — dois/três ponteiros, versão iterativa

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {
        // left + (right-left)/2 evita overflow de int em arrays com índices grandes
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;                  // achou o alvo
        } else if (nums[mid] < target) {
            left = mid + 1;              // alvo está estritamente à direita de mid
        } else {
            right = mid - 1;             // alvo está estritamente à esquerda de mid
        }
    }
    // left > right: o intervalo de busca ficou vazio sem achar o alvo.
    return -1;
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

- **`(left + right) / 2` em vez de `left + (right - left) / 2`**: em arrays gigantes com índices próximos do limite de `int`, a soma direta estoura — hábito a criar desde o problema mais básico da categoria.
- **`left <= right` vs `left < right`**: aqui buscamos um valor exato que pode não existir, então o laço precisa continuar enquanto `left <= right` (intervalo não vazio) e retornar `-1` fora dele — usar `<` faria perder o último candidato possível.
- **Esquecer de tratar array vazio implícito**: a restrição garante `nums.length >= 1`, mas é bom hábito lembrar que `right = nums.length - 1` já cobre o caso de 1 elemento corretamente (`left == right == 0`).
- **Confundir com "índice de inserção"**: aqui, se `target` não existe, a resposta é `-1` — não o índice onde ele entraria (isso é o [0035] Search Insert Position).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento, achou | `nums=[5], target=5` | 0 | borda mínima, presente |
| Um elemento, não achou | `nums=[5], target=-5` | -1 | borda mínima, ausente |
| Alvo é o primeiro | `nums=[-1,0,3,5,9,12], target=-1` | 0 | fronteira esquerda |
| Alvo é o último | `nums=[-1,0,3,5,9,12], target=12` | 5 | fronteira direita |
| Alvo ausente | `nums=[-1,0,3,5,9,12], target=2` | -1 | cai entre dois elementos existentes |

## 🔗 Conexões

- Problemas irmãos: **[0035] Search Insert Position** (mesmo template, mas devolve onde inserir em vez de -1), **[0374] Guess Number Higher or Lower** (mesma lógica com um oráculo de API em vez de array), **[0153] Find Minimum in Rotated Sorted Array** (busca binária num array "quebrado")
- No backend: é o algoritmo por trás de qualquer índice ordenado — de um índice de banco de dados (B-tree) a uma busca em log ordenado por timestamp — sempre que os dados estão ordenados, O(log n) bate O(n) por uma margem gigantesca em coleções grandes.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
