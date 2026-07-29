# [0167] Two Sum II - Input Array Is Sorted

> 🔗 [LeetCode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#TwoPointers` `#BuscaBinaria` `#Medium`

## 📜 O Problema

Você recebe um array `numbers`, **1-indexado** e já ordenado de forma não decrescente, e um `target`. Encontre dois números que somem `target` e retorne seus índices **1-indexados** `[index1, index2]` (com `index1 < index2`). Garantido que existe **exatamente uma** solução, e você não pode usar o mesmo elemento duas vezes.

**Exemplos:**
```
Input:  numbers = [2,7,11,15], target = 9    Output: [1,2]   (2+7=9)
Input:  numbers = [2,3,4], target = 6        Output: [1,3]   (2+4=6)
Input:  numbers = [-1,0], target = -1        Output: [1,2]   (-1+0=-1)
```

**Restrições (e o que elas denunciam):**
- `2 <= numbers.length <= 3 * 10^4` → O(n²) força bruta chega a 9×10^8, arriscado; existe algo melhor
- "numbers is sorted in non-decreasing order" → a informação mais valiosa do problema: um array já ordenado permite descartar candidatos com certeza a cada comparação
- "Your solution must use only constant extra space" → essa restrição **proíbe** o hash map de complemento (que usaria O(n) de espaço) — é o convite direto para dois ponteiros, que resolve em O(1) de espaço extra usando a ordenação

## 🧭 Como reconhecer o padrão

"Array **ordenado**" + "ache um par cuja soma bate com um alvo" + "espaço constante" é a assinatura mais clássica de **dois ponteiros convergentes**: um no início, outro no fim, movendo-se um em direção ao outro conforme a soma atual é maior ou menor que o alvo.

## 🐢 Solução 1 — Força bruta

Para cada par `(i, j)` com `i < j`, verificar se `numbers[i] + numbers[j] == target`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** com `n` até 3×10^4, o número de pares chega a ~4.5×10^8 — lento demais. Ignora completamente que o array está ordenado, o que permite eliminar candidatos inteiros a cada comparação em vez de testar par por par.

Uma alternativa mais rápida seria um hash map de complemento (como no [0001] Two Sum original), resolvendo em O(n) tempo — mas o enunciado **proíbe espaço extra além de O(1)**, então essa opção fica descartada aqui.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha dois ponteiros, `left` no início e `right` no fim do array. Compare `numbers[left] + numbers[right]` com `target`:
- Se a soma for **igual** ao alvo, achou — retorna os índices (convertidos para 1-indexado).
- Se a soma for **menor** que o alvo, o único jeito de aumentar a soma é trazer um número maior — avança `left` (o array só cresce à direita).
- Se a soma for **maior** que o alvo, avança `right` para trazer um número menor.

Como o array está ordenado, mover o ponteiro "errado" nunca perderia uma solução válida: se a soma já é pequena demais, nenhum `right` menor (mais à esquerda) ajudaria — só um `left` maior pode aumentar a soma.

## 🎬 Exemplo passo a passo

`numbers = [2, 7, 11, 15]`, `target = 9`

| Passo | left (val) | right (val) | soma | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 (2) | 3 (15) | 17 | 17 > 9 → grande demais | `right--` |
| 2 | 0 (2) | 2 (11) | 13 | 13 > 9 → grande demais | `right--` |
| 3 | 0 (2) | 1 (7) | 9 | 9 == 9 → achou! | retorna índices |

Resultado final: `[0+1, 1+1] = [1, 2]` ✔ (convertendo de 0-indexado para 1-indexado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada ponteiro percorre o array no máximo uma vez, nunca anda para trás
- **Espaço:** O(1) — só dois ponteiros inteiros, satisfaz a restrição de espaço constante

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] twoSum(int[] numbers, int target) {
    int left = 0, right = numbers.length - 1;

    while (left < right) {
        int soma = numbers[left] + numbers[right];

        if (soma == target) {
            // +1 em cada índice: o enunciado pede resposta 1-indexada.
            return new int[]{left + 1, right + 1};
        } else if (soma < target) {
            left++;                      // soma pequena demais: só um "left" maior resolve
        } else {
            right--;                     // soma grande demais: só um "right" menor resolve
        }
    }
    return new int[]{};                  // inalcançável: o enunciado garante exatamente uma solução
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

- **Esquecer o `+1` na conversão de índice**: o enunciado pede resposta **1-indexada**, mas a implementação naturalmente trabalha com índices 0-indexados internamente — retornar os índices "crus" sem somar 1 é o erro mais comum deste problema específico.
- **Usar hash map por hábito (como no Two Sum original)**: funciona corretamente, mas viola a restrição explícita de espaço O(1) — vale entender por que dois ponteiros é a resposta "certa" aqui, não só uma alternativa.
- **Mover o ponteiro errado**: quando a soma é maior que o alvo, mover `left` (em vez de `right`) só pode piorar ou manter a soma (já que o array está ordenado) — nunca ajuda a diminuir.
- **Tentar usar o mesmo elemento duas vezes**: o laço `left < right` (estrito) já impede isso naturalmente, já que os dois ponteiros nunca coincidem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Solução nos extremos | `numbers=[2,7,11,15], target=9` | `[1,2]` | trace acima |
| Solução não nos extremos | `numbers=[2,3,4], target=6` | `[1,3]` | testa que left avança até achar |
| Com negativos | `numbers=[-1,0], target=-1` | `[1,2]` | borda mínima com valor negativo |
| Dois elementos, único par possível | `numbers=[1,2], target=3` | `[1,2]` | borda mínima do tamanho do array |
| Target negativo com soma de negativos | `numbers=[-3,-1,0,2,4], target=-4` | `[1,2]` | soma de dois negativos |

## 🔗 Conexões

- Problemas irmãos: **[0001] Two Sum** (a versão sem ordenação, resolvida com hash map em vez de dois ponteiros), **[2540] Minimum Common Value** (dois ponteiros aproveitando dois arrays ordenados), **[2824] Count Pairs Whose Sum is Less than Target** (mesma técnica de convergência, mas contando em vez de achar um par exato)
- No backend: essa é a técnica usada para casar registros de duas fontes já ordenadas por uma chave numérica (ex.: conciliar pagamentos com faturas ordenadas por valor) sem gastar memória extra — o mesmo princípio de "merge" com ponteiros convergentes.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente a buscar o complemento de cada elemento via binary search, O(n log n)), mas a técnica ótima — e a exigida pela restrição de espaço O(1) — é dois ponteiros convergentes em O(n), então o documento foi classificado em `02_two_pointers`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
