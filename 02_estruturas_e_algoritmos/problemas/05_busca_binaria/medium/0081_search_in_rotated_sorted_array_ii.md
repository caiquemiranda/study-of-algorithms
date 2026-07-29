# [0081] Search in Rotated Sorted Array II

> 🔗 [LeetCode 81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Mesmo problema do [0033] Search in Rotated Sorted Array, mas agora `nums` **pode conter duplicatas**. Dado o array rotacionado e um `target`, retorne `true` se ele existir, `false` caso contrário.

**Exemplos:**
```
Input:  nums = [2,5,6,0,0,1,2], target = 0    Output: true
Input:  nums = [2,5,6,0,0,1,2], target = 3    Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 5000` → mesmo teto do problema sem duplicatas
- "nums may contain duplicates" → a mudança central: sem valores únicos, `nums[left] == nums[mid] == nums[right]` pode acontecer sem revelar qual metade está ordenada — quebra a certeza que a versão sem duplicatas tinha
- **Follow up:** "Would this affect the runtime complexity? How and why?" → é o convite explícito para reconhecer que, no pior caso, a solução deixa de ser O(log n) e vira O(n)

## 🧭 Como reconhecer o padrão

A mesma ideia de [0033] (identificar qual metade ao redor de `mid` está ordenada) se aplica, mas com duplicatas surge um caso ambíguo: quando `nums[left] == nums[mid] == nums[right]`, é **impossível saber** de que lado está o "corte" da rotação usando só essa comparação — o array poderia ser `[1,0,1,1,1]` ou `[1,1,1,0,1]`, indistinguíveis pelos extremos. A saída é reduzir o intervalo "às cegas" (encolher `left` ou `right` em 1) até a ambiguidade desaparecer.

## 🐢 Solução 1 — Força bruta

Percorrer o array inteiro comparando cada elemento com `target`.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** na melhor das hipóteses (poucos casos ambíguos), a busca binária adaptada roda bem mais rápido que O(n) puro — mas o objetivo é entender por que, com duplicatas, não dá para GARANTIR O(log n) sempre, e por isso a busca binária ainda vale a pena mesmo sem a garantia formal do pior caso.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use a mesma lógica de [0033] Search in Rotated Sorted Array (identificar a metade ordenada e verificar se `target` cai nela), mas adicione um caso extra no início de cada iteração: se `nums[left] == nums[mid] && nums[mid] == nums[right]`, não dá pra decidir qual lado está ordenado — **encolha os dois extremos** (`left++`, `right--`) e tente de novo. Isso "descasca" duplicatas nas bordas até a ambiguidade sumir ou o intervalo esvaziar.

> Por que isso não quebra O(log n) sempre? Porque, no pior caso (array cheio de valores repetidos, ex.: `[1,1,1,1,1,1,1]` com um único `0` escondido), você pode acabar encolhendo um elemento de cada vez — degradando para O(n). É exatamente a resposta ao follow-up do enunciado.

## 🎬 Exemplo passo a passo

`nums = [2,5,6,0,0,1,2]`, `target = 3` (segundo exemplo do enunciado — este trace passa pelo caso de ambiguidade)

| Passo | left | mid | right | Ambíguo? | Metade ordenada | target no intervalo? | Decisão |
|---|---|---|---|---|---|---|---|
| 1 | 0 (2) | 3 (0) | 6 (2) | nums[0]=2, nums[3]=0, nums[6]=2 → não (nums[mid] difere) | nums[0]=2 > nums[3]=0 → direita ordenada | 3 em (0,2]? não (3>2) | busca à esquerda: `right=2` |
| 2 | 0 (2) | 1 (5) | 2 (6) | nums[0]=2, nums[1]=5, nums[2]=6 → não | nums[0]=2 <= nums[1]=5 → esquerda ordenada | 3 em [2,5)? sim | busca à esquerda: `right=0` |
| 3 | 0 (2) | 0 (2) | 0 (2) | nums[0]=nums[0]=nums[0]=2 → **ambíguo!** | — | — | encolhe: `left=1`, `right=-1` |
| 4 | 1 | — | -1 | `left > right` → fim | — | — | retorna false |

Resultado final: `false` ✔ (bate com o segundo exemplo do enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) em média, **O(n) no pior caso** — quando há muitas duplicatas ambíguas nas bordas, forçando o encolhimento um a um
- **Espaço:** O(1) — dois/três ponteiros, versão iterativa

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return true;
        }

        if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
            // Ambiguidade: não dá para saber qual metade está ordenada.
            // Encolhe os dois extremos e tenta de novo (é o que causa o pior caso O(n)).
            left++;
            right--;
        } else if (nums[left] <= nums[mid]) {
            // Metade esquerda ordenada (mesma lógica do LC 33).
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            // Metade direita ordenada.
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
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

- **Esquecer o caso de ambiguidade**: sem o `if (nums[left] == nums[mid] && nums[mid] == nums[right])`, a lógica de [0033] pode classificar a metade errada como "ordenada" quando na verdade os três valores são iguais mas escondem uma rotação no meio.
- **Achar que a complexidade continua O(log n)**: é a pegadinha central deste problema — o follow-up do próprio enunciado pergunta isso de propósito. Com muitas duplicatas (ex.: `[1,1,1,1,1,1,0,1]`), o algoritmo pode precisar encolher quase o array inteiro um elemento por vez.
- **Confundir com [0033]**: reaproveitar a solução sem duplicatas diretamente falha silenciosamente em casos como `[1,0,1,1,1]` buscando `0` — sem o tratamento de ambiguidade, a lógica pode descartar a metade que contém o alvo.
- **Retornar índice em vez de booleano**: diferente do LC 33 (que retorna o índice), este problema pede apenas `true`/`false` — com duplicatas, "o índice" nem sempre é único, então o enunciado simplifica para existência.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso ambíguo clássico | `nums=[1,0,1,1,1], target=0` | true | testa o encolhimento de bordas iguais |
| Pior caso (quase todo igual) | `nums=[1,1,1,1,1,1,1], target=2` | false | testa que o algoritmo termina mesmo degradando para O(n) |
| Sem rotação | `nums=[1,2,3,4,5], target=3` | true | garante que funciona sem rotação real |
| Target ausente com duplicatas | `nums=[2,5,6,0,0,1,2], target=3` | false | duplicatas não devem gerar falso positivo |
| Um elemento | `nums=[1], target=1` | true | borda mínima |

## 🔗 Conexões

- Problemas irmãos: **[0033] Search in Rotated Sorted Array** (a versão sem duplicatas, com garantia real de O(log n)), **[0153] Find Minimum in Rotated Sorted Array** (e sua irmã [0154] com duplicatas, mesma degradação de complexidade)
- No backend: é um lembrete importante de que otimizações baseadas em "estrutura assumida" (dados ordenados/particionados) podem degradar silenciosamente quando os dados reais têm mais repetição do que o esperado — o mesmo acontece com índices de banco de dados em colunas de baixa cardinalidade (poucos valores distintos), que perdem eficiência.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
