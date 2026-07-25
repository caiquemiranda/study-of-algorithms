# [0153] Find Minimum in Rotated Sorted Array

> 🔗 [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-24 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Um array **ordenado crescente e sem duplicatas** foi rotacionado num pivô desconhecido: `[0,1,2,4,5,6,7]` pode ter virado `[4,5,6,7,0,1,2]`. Encontre o **menor elemento**.

**Exemplos:**
```
Input:  nums = [3,4,5,1,2]        Output: 1
Input:  nums = [4,5,6,7,0,1,2]    Output: 0
Input:  nums = [11,13,15,17]      Output: 11   (rotação de 0 posições!)
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 5000` → O(n) passaria, **mas o enunciado exige O(log n)** — isso grita "busca binária"
- "todos os elementos são únicos" → sem duplicatas, toda comparação decide com certeza (a variante com duplicatas é o LC 154, que degrada para O(n) no pior caso)
- "ordenado e rotacionado" → a estrutura tem **duas rampas crescentes**, e o mínimo é o início da segunda

## 🧭 Como reconhecer o padrão

"Array ordenado (mesmo que rotacionado)" + "encontre em O(log n)" = busca binária. A pergunta certa não é "onde está o valor X?", e sim "**onde está o ponto de virada?**" — e busca binária serve para achar qualquer ponto de virada em espaço monotônico (ver [fundamentos](../../../fundamentos/05_busca_binaria.md)).

## 🐢 Solução 1 — Força bruta

Percorrer o array inteiro guardando o menor valor visto.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado pede O(log n) explicitamente — e ignora a informação mais valiosa do problema: o array está *quase* ordenado. Força bruta trata `[4,5,6,7,0,1,2]` como se fosse um array qualquer.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pense no array rotacionado como **duas rampas**: `[4,5,6,7]` e `[0,1,2]`. Todos os valores da primeira rampa são **maiores** que todos da segunda. O mínimo é o primeiro degrau da segunda rampa.

A sacada: compare o meio com o **último elemento** (`nums[right]`):
- `nums[mid] > nums[right]` → o meio está na **primeira** rampa → o mínimo está estritamente **à direita** de mid → `left = mid + 1`
- `nums[mid] <= nums[right]` → o meio está na **segunda** rampa (ou o array nem está rotacionado) → o mínimo é mid **ou está à esquerda** → `right = mid`

Cada comparação descarta metade. Quando `left == right`, sobrou exatamente o mínimo.

> Por que comparar com `right` e não com `left`? Porque com `right` os dois casos acima cobrem **tudo, inclusive o array não rotacionado** — sem precisar de caso especial. Comparar com `left` exige o teste extra `nums[left] < nums[right]` antes (é a pegadinha nº 1 abaixo).

## 🎬 Exemplo passo a passo

`nums = [4, 5, 6, 7, 0, 1, 2]`

| Passo | left | mid | right | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 (val 4) | 3 (val 7) | 6 (val 2) | 7 > 2 → mid na 1ª rampa | `left = 4` |
| 2 | 4 (val 0) | 5 (val 1) | 6 (val 2) | 1 ≤ 2 → mid na 2ª rampa | `right = 5` |
| 3 | 4 (val 0) | 4 (val 0) | 5 (val 1) | 0 ≤ 1 → mid pode ser o mínimo | `right = 4` |
| 4 | 4 | — | 4 | `left == right` → fim | retorna `nums[4]` |

Resultado final: `0` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do espaço de busca
- **Espaço:** O(1) — dois ponteiros, versão iterativa (a recursiva gastaria O(log n) de pilha à toa)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findMin(int[] nums) {
    int left = 0, right = nums.length - 1;

    while (left < right) {                      // para quando sobra 1 elemento
        // Previne integer overflow: (left+right) pode estourar int;
        // left + (right-left)/2 nunca estoura.
        int mid = left + (right - left) / 2;

        if (nums[mid] > nums[right]) {
            // mid está na 1ª rampa (parte alta). O "despenhadeiro" para o
            // mínimo está DEPOIS de mid — mid nunca é a resposta aqui.
            left = mid + 1;
        } else {
            // mid está na 2ª rampa (ou array não rotacionado).
            // mid PODE ser o mínimo, então não o descartamos: right = mid.
            right = mid;
        }
    }
    // Invariante do loop: o mínimo está sempre em [left, right].
    // left == right → achamos.
    return nums[left];
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

- **Comparar `mid` com `left`**: parece simétrico, mas quebra no array **não rotacionado** (`[1,2,3]`: `nums[mid] > nums[left]` mandaria a busca para a direita — errado). Exige o guard extra `if (nums[left] < nums[right]) return nums[left];`. Comparar com `right` dispensa tudo isso.
- **`left = mid` em vez de `mid + 1`**: com `nums[mid] > nums[right]`, mid comprovadamente NÃO é o mínimo; manter ele causa **loop infinito** quando restam 2 elementos.
- **`(left + right) / 2`** em Java/C++: overflow com arrays gigantes. Sempre `left + (right - left) / 2`.
- **Versão recursiva** (como a minha primeira solução): funciona, mas gasta O(log n) de pilha sem ganho — em entrevista, cite o trade-off e prefira iterativa.
- **Duplicatas mudam o problema**: com repetidos (`[3,3,1,3]`), `nums[mid] == nums[right]` não decide nada — é o LC 154, onde o pior caso vira O(n).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento | `[1]` | 1 | borda mínima |
| Sem rotação | `[1,2,3,4]` | 1 | o caso que quebra a comparação com `left` |
| Rotação de 1 | `[2,1]` | 1 | menor caso com decisão real |
| Mínimo no fim | `[2,3,4,5,1]` | 1 | rotação máxima |
| Exemplo clássico | `[4,5,6,7,0,1,2]` | 0 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0033] Search in Rotated Sorted Array** (mesma estrutura, agora buscando um alvo), **[0154] Find Minimum II** (com duplicatas), **[0704] Binary Search** (o pai de todos)
- No backend: achar o "ponto de virada" em dados ordenados-com-quebra é o mesmo raciocínio de localizar o offset onde um log circular (ring buffer) reiniciou, ou o commit que quebrou o build no `git bisect` — que é literalmente busca binária na história.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
