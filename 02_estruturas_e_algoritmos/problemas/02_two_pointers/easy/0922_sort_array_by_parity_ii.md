# [0922] Sort Array By Parity II

> 🔗 [LeetCode 922](https://leetcode.com/problems/sort-array-by-parity-ii/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array `nums` com metade dos valores pares e metade ímpares, reorganize-o de forma que, sempre que `nums[i]` for ímpar, `i` seja um índice ímpar, e sempre que `nums[i]` for par, `i` seja um índice par. Retorne **qualquer** array que satisfaça essa condição.

**Exemplos:**
```
Input:  nums = [4,2,5,7]
Output: [4,5,2,7]
Explicação: [4,7,2,5], [2,5,4,7], [2,7,4,5] também seriam aceitos.

Input:  nums = [2,3]
Output: [2,3]
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 2 * 10^4`, tamanho sempre par, exatamente metade par/metade ímpar → garante que uma solução sempre existe e que o "encaixe" final é perfeito (não sobra nenhum valor sem posição correspondente)
- Aceita **qualquer** array válido → não precisa preservar ordem relativa, só a paridade posição-valor
- Follow-up pede in-place → descarta montar arrays auxiliares

## 🧭 Como reconhecer o padrão

"Encaixar cada valor num slot de paridade específica (posição par/ímpar), sem se importar com a ordem interna" é dois ponteiros **independentes**: um percorre só os índices pares, outro só os ímpares, cada um avançando de 2 em 2 — e trocando de lugar sempre que os dois estiverem "no slot errado" ao mesmo tempo.

## 🐢 Solução 1 — Força bruta (duas listas)

Separar os valores pares e ímpares em duas listas (mantendo a ordem original de cada), e depois intercalar: posição 0 recebe o primeiro par, posição 1 recebe o primeiro ímpar, posição 2 recebe o segundo par, e assim por diante.

- Tempo: O(n) · Espaço: O(n) — duas listas auxiliares guardando todos os elementos
- **Por que não basta:** o follow-up pede explicitamente uma solução in-place; montar listas separadas usa espaço proporcional ao tamanho da entrada, quando dá pra reorganizar trocando elementos diretamente no array original.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `even` começando em 0 (só visita índices pares, avançando de 2 em 2) e `odd` começando em 1 (só índices ímpares, também de 2 em 2). Enquanto `nums[even]` já for par, avance `even` — está no lugar certo. Enquanto `nums[odd]` já for ímpar, avance `odd` — também está certo. Quando `nums[even]` for ímpar E `nums[odd]` for par (os dois "errados" ao mesmo tempo), troque-os — cada um vai parar exatamente no slot de paridade que precisa.

## 🎬 Exemplo passo a passo

`nums = [4,2,5,7]` (n=4)

| Passo | even | odd | nums[even] | nums[odd] | Ação |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 4 (par, correto) | — | `even += 2` → even=2 |
| 2 | 2 | 1 | 5 (ímpar, errado) | 2 (par, errado) | troca `nums[2]` com `nums[1]` → `[4,5,2,7]` |
| 3 | 2 | 1 | 2 (agora par, correto) | — | `even += 2` → even=4 |
| 4 | 4 | 1 | — | — | `even >= n(4)`, loop termina |

Resultado final: `[4,5,2,7]` ✔ (bate exatamente com o output do enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — juntos, `even` e `odd` percorrem cada posição do array no máximo uma vez
- **Espaço:** O(1) — só os dois índices e uma variável temporária pra troca

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] sortArrayByParityII(int[] nums) {
    int n = nums.length;
    int even = 0;
    int odd = 1;

    while (even < n) {
        if (nums[even] % 2 == 0) {
            even += 2; // já está correto: valor par num índice par
            continue;
        }
        if (nums[odd] % 2 == 1) {
            odd += 2; // já está correto: valor ímpar num índice ímpar
            continue;
        }
        // nums[even] é ímpar (errado) e nums[odd] é par (errado): troca os dois
        int tmp = nums[even];
        nums[even] = nums[odd];
        nums[odd] = tmp;
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

- Avançar `even` e `odd` de 1 em 1 — eles cobrem só índices pares ou só ímpares, respectivamente; o passo tem que ser de **2 em 2** para cada um.
- Achar que precisa comparar `nums[even]` com `nums[odd]` por tamanho (maior/menor) — a única coisa que importa pra decidir o swap é a **paridade** de cada valor, não sua magnitude.
- Esquecer o `continue` (ou equivalente) depois de avançar `even`/`odd` sem fazer swap — sem isso, o código poderia tentar um swap desnecessário na mesma iteração em que um dos ponteiros já avançou.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado (uma saída válida) | Por quê |
|---|---|---|---|
| Caso padrão | `[4,2,5,7]` | `[4,5,2,7]` | mistura que precisa de exatamente 1 swap |
| Já correto | `[2,3]` | `[2,3]` | nenhum swap necessário |
| Totalmente trocado | `[1,2,3,4]` | `[2,1,4,3]` | precisa de 2 swaps pra encaixar todos os valores |
| Tamanho mínimo | `[0,1]` | `[0,1]` | já satisfaz a condição, ambos os ponteiros passam direto |

## 🔗 Conexões

- Problemas irmãos: [0905] Sort Array By Parity (mesma ideia, mas sem exigir alternância estrita por posição), [0075] Sort Colors (mesma família de particionamento in-place com múltiplos ponteiros)
- No backend: distribuir itens em posições alternadas de um buffer respeitando uma regra de paridade — por exemplo, alternar registros de dois tipos numa estrutura de acesso intercalado, como um round-robin binário.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
