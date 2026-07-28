# [2460] Apply Operations to an Array

> 🔗 [LeetCode 2460](https://leetcode.com/problems/apply-operations-to-an-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Simulation` `#Easy`

## 📜 O Problema

Dado um array `nums` de tamanho `n` com inteiros não-negativos, aplique `n-1` operações **sequenciais**: na operação `i`, se `nums[i] == nums[i+1]`, multiplique `nums[i]` por `2` e zere `nums[i+1]`; senão, pule. Depois de todas as operações, empurre todos os `0`s para o final do array (preservando a ordem dos demais). Retorne o array resultante.

**Exemplos:**
```
Input:  nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]

Input:  nums = [0,1]
Output: [1,0]
Explicação: nenhuma operação se aplica, só desloca o zero.
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 2000` → O(n) ou O(n²) leve já passam, mas O(n) é natural e alcançável
- Operações **sequenciais**, não simultâneas → o resultado de uma operação pode afetar a comparação da próxima (ex.: um valor recém-zerado entra na comparação seguinte)
- "Empurrar zeros pro final preservando ordem" → é literalmente o mesmo problema de [0283] Move Zeroes, como uma segunda etapa

## 🧭 Como reconhecer o padrão

Este problema se resolve em duas etapas independentes: uma varredura sequencial simples (fundir vizinhos iguais), seguida exatamente pela técnica de dois ponteiros de [0283] Move Zeroes (ponteiro lento marcando a próxima posição livre, ponteiro rápido varrendo e trocando quando encontra um valor não-zero) para compactar o resultado.

## 🐢 Solução 1 — Força bruta (para a etapa de deslocamento)

Depois de aplicar a fusão sequencial (etapa obrigatória, sempre O(n)), fazer o deslocamento dos zeros construindo uma lista nova: percorrer o array coletando os não-zeros em ordem, depois preencher o restante com zeros, e copiar de volta.

- Tempo: O(n) · Espaço: O(n) extra para a lista auxiliar
- **Por que não basta:** já resolve a etapa de deslocamento em tempo linear, mas usa espaço proporcional ao array; dois ponteiros empurram os zeros pro final in-place com troca (swap), exatamente como em [0283], sem lista auxiliar nenhuma.

## 💡 Solução 2 — A ideia otimizada (intuição)

**Etapa 1 (fusão sequencial):** percorra o array com um índice `i` de `0` a `n-2`; se `nums[i] == nums[i+1]`, dobre `nums[i]` e zere `nums[i+1]`. **Etapa 2 (compactação):** aplique a técnica de [0283] Move Zeroes — ponteiro `lento` marcando a próxima posição livre para um valor não-zero, ponteiro `rápido` percorrendo e trocando (swap) sempre que encontrar um valor diferente de zero.

## 🎬 Exemplo passo a passo

`nums = [1,2,2,1,1,0]`

**Etapa 1 — fusão sequencial:**

| i | nums[i] | nums[i+1] | Iguais? | Ação | Array depois |
|---|---|---|---|---|---|
| 0 | 1 | 2 | não | pula | `[1,2,2,1,1,0]` |
| 1 | 2 | 2 | sim | `nums[1]*=2`, `nums[2]=0` | `[1,4,0,1,1,0]` |
| 2 | 0 | 1 | não | pula | `[1,4,0,1,1,0]` |
| 3 | 1 | 1 | sim | `nums[3]*=2`, `nums[4]=0` | `[1,4,0,2,0,0]` |
| 4 | 0 | 0 | sim (ambos zero) | `nums[4]*=2` (continua 0), `nums[5]=0` | `[1,4,0,2,0,0]` |

**Etapa 2 — compactação (técnica do LC 283):**

| rápido | nums[rápido] | Ação | Array depois |
|---|---|---|---|
| 0 | 1 | troca(lento=0, rápido=0), no-op | `[1,4,0,2,0,0]` |
| 1 | 4 | troca(lento=1, rápido=1), no-op | `[1,4,0,2,0,0]` |
| 2 | 0 | pula | `[1,4,0,2,0,0]` |
| 3 | 2 | troca(lento=2, rápido=3) | `[1,4,2,0,0,0]` |
| 4, 5 | 0, 0 | pula | `[1,4,2,0,0,0]` |

Resultado final: `[1,4,2,0,0,0]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada pra fusão, outra pra compactação
- **Espaço:** O(1) — ambas as etapas modificam o array in-place

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] applyOperations(int[] nums) {
    int n = nums.length;

    // etapa 1: fusão sequencial de vizinhos iguais
    for (int i = 0; i < n - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }

    // etapa 2: empurra os zeros pro final, preservando a ordem (igual LC 283)
    int lento = 0;
    for (int rapido = 0; rapido < n; rapido++) {
        if (nums[rapido] != 0) {
            int tmp = nums[lento];
            nums[lento] = nums[rapido];
            nums[rapido] = tmp;
            lento++;
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

- Aplicar as operações "todas ao mesmo tempo" olhando o array original, em vez de sequencialmente — o enunciado é explícito ("applied sequentially, not all at once"); o resultado de uma operação pode afetar a comparação da operação seguinte.
- Achar que dois zeros consecutivos não "casam" pela condição de igualdade — `nums[i]==nums[i+1]==0` também satisfaz a condição (`0*2=0`, continua `0`), sem efeito visível, mas tecnicamente é uma operação válida, não um caso a pular.
- Fazer a etapa 2 (mover zeros) ANTES da etapa 1 (fusão) — a ordem importa: a fusão depende dos valores originais estarem nas posições certas para produzir os pares iguais corretos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo do enunciado | `[1,2,2,1,1,0]` | `[1,4,2,0,0,0]` | várias fusões em cadeia, depois compactação |
| Nenhuma fusão possível | `[0,1]` | `[1,0]` | só desloca o zero, nenhuma fusão ocorre |
| Fusão em par único | `[3,3]` | `[6,0]` | uma única fusão, resultado já com zero no final |
| Sem zeros nem pares iguais | `[1,2,3]` | `[1,2,3]` | nenhuma operação muda nada |

## 🔗 Conexões

- Problemas irmãos: [0283] Move Zeroes (mesma técnica usada aqui como segunda etapa, para empurrar os zeros pro final), [2352] Equal Row and Column Pairs (também processa o array sequencialmente comparando elementos)
- No backend: processar um stream de eventos aplicando uma regra de fusão sequencial (ex.: mesclar transações consecutivas idênticas num extrato bancário) e depois compactar o resultado removendo entradas "vazias" geradas pela fusão.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
