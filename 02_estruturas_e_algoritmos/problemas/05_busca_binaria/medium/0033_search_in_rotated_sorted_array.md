# [0033] Search in Rotated Sorted Array

> 🔗 [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Um array `nums` ordenado crescente, com valores **distintos**, foi rotacionado num pivô desconhecido: `[0,1,2,4,5,6,7]` pode virar `[4,5,6,7,0,1,2]`. Dado o array já rotacionado e um `target`, retorne o índice de `target`, ou `-1` se não existir.

**Exemplos:**
```
Input:  nums = [4,5,6,7,0,1,2], target = 0    Output: 4
Input:  nums = [4,5,6,7,0,1,2], target = 3    Output: -1
Input:  nums = [1], target = 0                Output: -1
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 5000` → O(n) passaria, mas o enunciado exige explicitamente O(log n)
- "You must write an algorithm with O(log n) runtime complexity" → busca binária obrigatória
- "All values of nums are unique" → sem duplicatas, toda comparação com o meio decide com certeza de que lado está a metade ordenada

## 🧭 Como reconhecer o padrão

É a evolução direta de [0153] Find Minimum in Rotated Sorted Array: em vez de achar o ponto de rotação, aqui buscamos um valor específico. A sacada central: **mesmo rotacionado, pelo menos uma das duas metades ao redor de qualquer `mid` está sempre ordenada normalmente**. Identificar qual metade está ordenada permite decidir em O(1) se o alvo pode estar nela.

## 🐢 Solução 1 — Força bruta

Percorrer o array inteiro comparando cada elemento com `target`.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige O(log n) — e ignora que, apesar da rotação, o array ainda tem estrutura suficiente (duas metades ordenadas) para descartar metade dos candidatos a cada passo.

## 💡 Solução 2 — A ideia otimizada (intuição)

A cada iteração, olhe `nums[mid]` e compare com `nums[left]` para descobrir qual metade (esquerda ou direita de `mid`) está **normalmente ordenada**:
- Se `nums[left] <= nums[mid]`, a metade **esquerda** (`left` até `mid`) está ordenada. Verifique se `target` cai dentro desse intervalo (`nums[left] <= target < nums[mid]`); se sim, busque à esquerda, senão a direita.
- Caso contrário, a metade **direita** (`mid` até `right`) está ordenada. Verifique se `target` cai nela (`nums[mid] < target <= nums[right]`); se sim, busque à direita, senão a esquerda.

Em ambos os casos, uma metade inteira é descartada por comparação, mantendo O(log n).

## 🎬 Exemplo passo a passo

`nums = [4,5,6,7,0,1,2]`, `target = 0`

| Passo | left | mid | right | Metade ordenada | target no intervalo? | Decisão |
|---|---|---|---|---|---|---|
| 1 | 0 (4) | 3 (7) | 6 (2) | nums[0]=4 <= nums[3]=7 → esquerda ordenada | 0 não está em [4,7) | busca à direita: `left=4` |
| 2 | 4 (0) | 5 (1) | 6 (2) | nums[4]=0 <= nums[5]=1 → esquerda ordenada | 0 está em [0,1)? sim (0<=0<1) | busca à esquerda: `right=4` |
| 3 | 4 (0) | 4 (0) | 4 (0) | `nums[mid]==target` → achou! | — | retorna 4 |

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
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        }

        if (nums[left] <= nums[mid]) {
            // Metade esquerda [left..mid] está ordenada normalmente.
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;         // target cai dentro da metade ordenada
            } else {
                left = mid + 1;          // target está na outra metade (possivelmente rotacionada)
            }
        } else {
            // Metade direita [mid..right] está ordenada normalmente.
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;          // target cai dentro da metade ordenada
            } else {
                right = mid - 1;         // target está na outra metade
            }
        }
    }
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

- **Usar `<` em vez de `<=` em `nums[left] <= nums[mid]`**: quando o intervalo `[left, mid]` tem só um elemento (`left == mid`), essa comparação precisa incluir a igualdade para classificar corretamente a metade como ordenada.
- **Confundir os limites do intervalo "target dentro da metade ordenada"**: são assimétricos de propósito — `nums[left] <= target < nums[mid]` na metade esquerda (fecha em `left`, abre em `mid`, já que `mid` já foi comparado antes) e `nums[mid] < target <= nums[right]` na direita.
- **Tentar achar o pivô primeiro e depois fazer duas buscas binárias separadas**: funciona, mas é uma solução mais complexa (duas fases) quando dá para resolver em uma única passada de busca binária, identificando a metade ordenada a cada iteração.
- **Array sem rotação**: `[1,2,3,4,5]` é um caso válido (rotação de 0 posições) — o algoritmo precisa funcionar sem tratamento especial, e funciona, porque a "metade esquerda" sempre estará ordenada nesse caso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento, achou | `nums=[1], target=1` | 0 | borda mínima |
| Um elemento, não achou | `nums=[1], target=0` | -1 | borda mínima, ausente |
| Sem rotação | `nums=[1,2,3,4,5], target=3` | 2 | garante que funciona sem rotação real |
| Target é o pivô | `nums=[4,5,6,7,0,1,2], target=0` | 4 | trace acima, target no início da metade rotacionada |
| Target ausente | `nums=[4,5,6,7,0,1,2], target=3` | -1 | cai num "buraco" entre valores existentes |

## 🔗 Conexões

- Problemas irmãos: **[0153] Find Minimum in Rotated Sorted Array** (mesma estrutura, busca o pivô em vez de um valor), **[0081] Search in Rotated Sorted Array II** (mesmo problema, mas com duplicatas — degrada para O(n) no pior caso), **[0704] Binary Search** (o padrão-base sem rotação)
- No backend: buscar um valor num buffer circular (ring buffer) sem "desenrolar" fisicamente os dados é o mesmo problema — a estrutura tem duas rampas ordenadas, exatamente como um array rotacionado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
