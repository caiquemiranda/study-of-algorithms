# [0724] Find Pivot Index

> 🔗 [LeetCode 724](https://leetcode.com/problems/find-pivot-index/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#PrefixSum` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums`, calcule o **índice pivô** desse array. O **índice pivô** é o índice onde a soma de todos os números **estritamente** à esquerda do índice é igual à soma de todos os números **estritamente** à direita dele. Se o índice está na borda esquerda do array, a soma à esquerda é `0` (não há elementos à esquerda); o mesmo vale para a borda direita.

Retorne **o índice pivô mais à esquerda**. Se não existir tal índice, retorne `-1`.

**Exemplos:**
```
Input:  nums = [1,7,3,6,5,6]
Output: 3
Explicação: soma à esquerda = 1+7+3 = 11, soma à direita = 5+6 = 11.

Input:  nums = [1,2,3]
Output: -1
Explicação: não existe índice que satisfaça a condição.

Input:  nums = [2,1,-1]
Output: 0
Explicação: soma à esquerda = 0 (sem elementos), soma à direita = 1+(-1) = 0.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → O(n) esperado; recalcular somas do zero para cada índice seria O(n²) e ainda passaria, mas o prefix sum é o padrão esperado
- `-1000 <= nums[i] <= 1000` → valores pequenos, a soma total cabe folgadamente em `int`

## 🧭 Como reconhecer o padrão

"Soma de tudo à esquerda == soma de tudo à direita de um índice" é a assinatura clássica de **prefix sum**: em vez de recalcular a soma de cada lado do zero para cada índice candidato, calcule a soma total uma vez e vá "movendo" a soma da esquerda incrementalmente.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i`, some manualmente todos os elementos à esquerda e todos à direita, comparando os dois totais.

- Tempo: O(n²) — para cada um dos n índices, refaz duas somas de até n elementos · Espaço: O(1)
- **Por que não basta:** a soma da esquerda no índice `i+1` é só a soma da esquerda no índice `i` mais `nums[i]` — recalcular do zero a cada índice ignora esse reaproveitamento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule a `somaTotal` do array uma vez. Percorra o array mantendo `somaEsquerda` (inicialmente 0); em cada índice `i`, a soma à direita é `somaTotal - somaEsquerda - nums[i]`. Se `somaEsquerda == somaDireita`, `i` é o pivô. Depois de checar, atualize `somaEsquerda += nums[i]` para o próximo índice.

## 🎬 Exemplo passo a passo

`nums = [1,7,3,6,5,6]`, `somaTotal = 28`

| Passo | i | nums[i] | somaEsquerda (antes) | somaDireita = total-esq-nums[i] | pivô? |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 28-0-1=27 | não (0≠27) |
| 2 | 1 | 7 | 1 | 28-1-7=20 | não (1≠20) |
| 3 | 2 | 3 | 8 | 28-8-3=17 | não (8≠17) |
| 4 | 3 | 6 | 11 | 28-11-6=11 | **sim** (11=11) |

Resultado final: índice `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas simples (soma total + busca do pivô)
- **Espaço:** O(1) extra

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int pivotIndex(int[] nums) {
    int somaTotal = 0;
    for (int n : nums) {
        somaTotal += n;
    }

    int somaEsquerda = 0;
    for (int i = 0; i < nums.length; i++) {
        int somaDireita = somaTotal - somaEsquerda - nums[i]; // tudo que não é esquerda nem o próprio elemento
        if (somaEsquerda == somaDireita) {
            return i; // primeiro índice que satisfaz -> já é o mais à esquerda, retorna direto
        }
        somaEsquerda += nums[i]; // acumula para o próximo índice
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

- Incluir `nums[i]` na `somaEsquerda` antes de comparar — o índice do pivô não conta a si mesmo em nenhum dos dois lados, só os elementos estritamente à esquerda e estritamente à direita.
- Esquecer que a resposta precisa ser o pivô mais à ESQUERDA em caso de múltiplos pivôs válidos — como o loop vai da esquerda para a direita e retorna assim que encontra, isso já é garantido naturalmente.
- Array com valores negativos (ex.: `[2,1,-1]`) — a soma pode "empatar" mesmo com números negativos misturados; o algoritmo funciona igual, só não assuma que a soma é sempre crescente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Pivô no meio | `[1,7,3,6,5,6]` | 3 | caso padrão do enunciado |
| Sem pivô | `[1,2,3]` | -1 | nenhuma soma bate |
| Pivô na borda esquerda | `[2,1,-1]` | 0 | soma à esquerda é 0 (vazia) e à direita também é 0 |
| Um único elemento | `[5]` | 0 | ambos os lados são vazios (soma 0 = soma 0) |

## 🔗 Conexões

- Problemas irmãos: [0303] Range Sum Query - Immutable (mesma técnica base de prefix sum), [0238] Product of Array Except Self (mesma ideia de "tudo exceto a posição atual", mas com produto em vez de soma)
- No backend: balanceamento de carga ou particionamento de dados (ex.: encontrar o ponto de corte em uma lista de tarefas onde o trabalho de um lado é igual ao do outro), análise financeira (ponto onde receita acumulada se iguala à despesa restante).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
