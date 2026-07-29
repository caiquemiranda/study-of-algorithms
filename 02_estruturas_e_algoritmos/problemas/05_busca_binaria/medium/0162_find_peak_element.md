# [0162] Find Peak Element

> 🔗 [LeetCode 162](https://leetcode.com/problems/find-peak-element/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Um "elemento de pico" é estritamente maior que seus vizinhos. Dado um array `nums` (0-indexado), ache **qualquer** pico e retorne o índice dele. Considere que `nums[-1] = nums[n] = -∞` (as bordas do array são sempre "vizinhas" de valores infinitamente pequenos).

**Exemplos:**
```
Input:  nums = [1,2,3,1]          Output: 2   (3 é pico)
Input:  nums = [1,2,1,3,5,6,4]    Output: 1 ou 5   (2 é pico, 6 também é)
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 1000` → O(n) passaria, mas o enunciado exige explicitamente O(log n)
- "You must write an algorithm that runs in O(log n) time" → busca binária obrigatória, mesmo o array **não estando ordenado**
- `nums[i] != nums[i+1]` para todo `i` → sem elementos vizinhos iguais, toda comparação entre vizinhos decide uma direção clara (subindo ou descendo), o que é a chave para aplicar busca binária num array não ordenado

## 🧭 Como reconhecer o padrão

Este problema quebra a intuição de "busca binária só funciona em array ordenado" — na verdade, ela funciona sempre que existe uma condição que permite **descartar metade do espaço com certeza**. Aqui: se `nums[mid] < nums[mid+1]`, a sequência está subindo, então existe **garantidamente** um pico à direita de `mid` (mesmo que o array não seja monótono depois) — porque, no pior caso, a subida "esbarra" na borda direita, que vale `-∞`, formando um pico ali.

## 🐢 Solução 1 — Força bruta

Percorrer o array comparando cada elemento com os vizinhos até achar um pico.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige O(log n) — e ignora que a direção da inclinação local (`nums[mid]` vs `nums[mid+1]`) já garante a existência de um pico de um dos lados, sem precisar examinar todos os elementos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Compare `nums[mid]` com seu vizinho da direita `nums[mid+1]`:
- Se `nums[mid] < nums[mid+1]`, a sequência sobe de `mid` para `mid+1` — existe um pico em algum lugar à direita (inclusive `mid+1` pode ser o próprio pico) → `left = mid + 1`.
- Se `nums[mid] > nums[mid+1]`, a sequência desce — existe um pico à esquerda ou o próprio `mid` já é um pico → `right = mid`.

Quando `left == right`, esse índice é garantidamente um pico (não existe mais "para onde subir" em nenhuma direção dentro do intervalo restante).

## 🎬 Exemplo passo a passo

`nums = [1, 2, 1, 3, 5, 6, 4]`

| Passo | left | mid | right | nums[mid] vs nums[mid+1] | Decisão |
|---|---|---|---|---|---|
| 1 | 0 | 3 (val 3) | 6 | nums[3]=3 < nums[4]=5 → subindo | `left = 4` |
| 2 | 4 | 5 (val 6) | 6 | nums[5]=6 > nums[6]=4 → descendo | `right = 5` |
| 3 | 4 | 4 | 5 | nums[4]=5 < nums[5]=6 → subindo | `left = 5` |
| 4 | 5 | — | 5 | `left == right` → fim | retorna 5 |

Resultado final: `5` ✔ (nums[5]=6 é maior que os vizinhos nums[4]=5 e nums[6]=4)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do espaço de busca
- **Espaço:** O(1) — dois ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findPeakElement(int[] nums) {
    int left = 0, right = nums.length - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] < nums[mid + 1]) {
            // Subindo: existe pico garantido à direita (no limite, a própria borda
            // funciona como pico, já que nums[n] é considerado -infinito).
            left = mid + 1;
        } else {
            // Descendo (ou mid já é maior que mid+1): pico está em mid ou à esquerda.
            // Não descartamos "mid" (right = mid, não mid - 1).
            right = mid;
        }
    }
    // left == right: não há mais "subida" possível em nenhuma direção -> é um pico.
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

- **Achar que o array precisa estar ordenado**: é a armadilha conceitual central deste problema — busca binária não exige ordenação global, só uma condição monotônica local que permita descartar metade do espaço com certeza.
- **`right = mid - 1` em vez de `right = mid`**: quando `nums[mid] > nums[mid+1]`, `mid` PODE ser o próprio pico — descartá-lo prematuramente perde a resposta correta (mesmo erro clássico de [0278] First Bad Version).
- **Comparar `nums[mid]` com `nums[mid-1]` em vez de `nums[mid+1]`**: funciona também, mas exige ajustar a direção de todas as decisões — misturar as duas convenções no meio do código é fonte comum de bug.
- **Esquecer as "bordas infinitas"**: um array estritamente crescente (`[1,2,3,4]`) tem seu único pico no último índice — a regra `nums[n] = -∞` garante que a busca sempre convirja para ele corretamente, sem tratamento especial.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento | `nums=[1]` | 0 | borda mínima, único índice é trivialmente pico |
| Estritamente crescente | `nums=[1,2,3,4]` | 3 | pico na borda direita |
| Estritamente decrescente | `nums=[4,3,2,1]` | 0 | pico na borda esquerda |
| Pico simples no meio | `nums=[1,2,3,1]` | 2 | trace simples do primeiro exemplo |
| Múltiplos picos possíveis | `nums=[1,2,1,3,5,6,4]` | 1 ou 5 | testa que qualquer pico válido é aceito |

## 🔗 Conexões

- Problemas irmãos: **[0153] Find Minimum in Rotated Sorted Array** (mesma ideia de usar inclinação local para descartar metade do espaço), **[0704] Binary Search** (o padrão-base, aqui adaptado para array não ordenado)
- No backend: encontrar um máximo local numa métrica que varia ao longo do tempo (ex.: pico de uso de CPU numa janela de monitoramento) sem escanear a série inteira usa esse mesmo raciocínio — "para que lado a métrica está subindo agora" já é suficiente para guiar a busca.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
