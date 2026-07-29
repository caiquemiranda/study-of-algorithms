# [0540] Single Element in a Sorted Array

> 🔗 [LeetCode 540](https://leetcode.com/problems/single-element-in-a-sorted-array/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-29 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Você recebe um array **ordenado** onde todo elemento aparece **exatamente duas vezes**, exceto um único elemento que aparece **exatamente uma vez**. Encontre esse elemento único.

**Exemplos:**
```
Input:  nums = [1,1,2,3,3,4,4,8,8]    Output: 2
Input:  nums = [3,3,7,7,10,11,11]     Output: 10
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n) passaria, mas o enunciado exige explicitamente O(log n) e O(1) de espaço
- "Your solution must run in O(log n) time and O(1) space" → busca binária obrigatória, e proíbe qualquer hash set de contagem (que gastaria O(n) de espaço)
- "array ordenado" + "pares, exceto um" → antes do elemento único, cada par começa num índice **par** (0, 2, 4, ...); depois dele, esse padrão se desloca — é essa quebra de paridade que a busca binária localiza

## 🧭 Como reconhecer o padrão

Sem o elemento único, o array teria só pares alinhados em índices `(par, par+1)`. A presença do elemento único **empurra** todo o alinhamento uma posição para a direita a partir de onde ele está. "Ache o ponto exato onde um padrão de alinhamento se rompe" é busca binária por fronteira — a mesma ideia de [0162] Find Peak Element, aplicada à paridade de índices em vez de inclinação de valores.

## 🐢 Solução 1 — Força bruta

Percorrer o array de dois em dois (`i = 0, 2, 4, ...`) comparando `nums[i]` com `nums[i+1]`; o primeiro índice onde eles diferem contém o elemento único (ou, se chegar ao fim, o último elemento é o único).

- Tempo: O(n/2) = O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige O(log n) — e ignora que a "quebra de alinhamento" entre pares é uma fronteira monotônica: antes dela, pares sempre começam em índice par; depois, sempre em índice ímpar. Isso permite descartar metade do array a cada comparação.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça busca binária, sempre forçando `mid` para um índice **par** (se `mid` calculado for ímpar, decremente 1). Compare `nums[mid]` com `nums[mid+1]`:
- Se forem **iguais**, o par em `mid` está intacto — o elemento único está **depois** dele → `left = mid + 2`.
- Se forem **diferentes**, o alinhamento já quebrou em `mid` ou antes — o elemento único está **em `mid` ou antes dele** → `right = mid`.

Quando `left == right`, esse índice é o elemento único.

## 🎬 Exemplo passo a passo

`nums = [1,1,2,3,3,4,4,8,8]` (n=9)

| Passo | left | mid (forçado par) | right | nums[mid] vs nums[mid+1] | Decisão |
|---|---|---|---|---|---|
| 1 | 0 | 4 (val 3) | 8 | nums[4]=3 ≠ nums[5]=4 → quebrou | `right = 4` |
| 2 | 0 | 2 (val 2) | 4 | nums[2]=2 ≠ nums[3]=3 → quebrou | `right = 2` |
| 3 | 0 | 1→0 (val 1) | 2 | nums[0]=1 == nums[1]=1 → par intacto | `left = 2` |
| 4 | 2 | — | 2 | `left == right` → fim | retorna nums[2] |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do espaço de busca
- **Espaço:** O(1) — dois ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int singleNonDuplicate(int[] nums) {
    int left = 0, right = nums.length - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (mid % 2 == 1) {
            mid--;                       // força mid a ser par, para comparar com mid+1 corretamente
        }

        if (nums[mid] == nums[mid + 1]) {
            // Par intacto em mid: o elemento único está depois desse par.
            left = mid + 2;
        } else {
            // Alinhamento já quebrou: o elemento único está em mid ou antes.
            right = mid;
        }
    }
    // left == right: encontrou o índice do elemento único.
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

- **Esquecer de forçar `mid` para par**: comparar `nums[mid]` com `nums[mid+1]` só faz sentido quando `mid` é o **início** de um par candidato — se `mid` for ímpar, a comparação correta seria com `nums[mid-1]`, o que bagunça a lógica. Forçar `mid` para par simplifica tudo para uma única regra.
- **`left = mid + 1` em vez de `mid + 2`**: quando o par em `mid` está intacto, o próximo candidato válido é `mid + 2` (pulando o par inteiro) — usar `mid + 1` reexamina o mesmo par pela metade.
- **`right = mid - 1` em vez de `mid`**: quando o alinhamento quebra em `mid`, o próprio `mid` PODE ser o elemento único — descartá-lo perde a resposta (mesmo erro clássico de [0278] First Bad Version e [0162] Find Peak Element).
- **Usar XOR (técnica de [0136] Single Number) sem aproveitar a ordenação**: funcionaria em O(n), mas ignora a restrição de O(log n) — o array ordenado é a pista de que a resposta esperada é busca binária, não XOR linear.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único elemento | `nums=[5]` | 5 | borda mínima, array de tamanho 1 |
| Elemento único no início | `nums=[1,2,2,3,3]` | 1 | fronteira logo no primeiro índice |
| Elemento único no fim | `nums=[3,3,7,7,10,11,11]` | 10 | segundo exemplo do enunciado, fronteira perto do fim |
| Elemento único no meio | `nums=[1,1,2,3,3,4,4,8,8]` | 2 | trace acima |
| Valores repetidos exceto um zero | `nums=[0,1,1,2,2]` | 0 | testa valor mínimo permitido pela restrição |

## 🔗 Conexões

- Problemas irmãos: **[0136] Single Number** (mesmo objetivo, mas array não ordenado, resolvido com XOR O(n)), **[0162] Find Peak Element** (mesma técnica de busca binária por fronteira sem array totalmente ordenado por valor)
- No backend: detectar o ponto exato onde um padrão de alinhamento par/ímpar se rompe (ex.: validar que registros de transação vêm sempre em pares débito/crédito consecutivos, achando rapidamente onde um registro órfão quebra o padrão) usa esse mesmo raciocínio de busca binária sobre paridade de posição.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
