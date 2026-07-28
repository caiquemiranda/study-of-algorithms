# [2161] Partition Array According to Given Pivot

> 🔗 [LeetCode 2161](https://leetcode.com/problems/partition-array-according-to-given-pivot/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Medium`

## 📜 O Problema

Dado `nums` e um inteiro `pivot` (que existe em `nums`), reorganize o array de forma que: todo elemento menor que `pivot` venha antes de todo elemento maior; os iguais ao pivot fiquem no meio; e a ordem relativa **original** dentro de cada grupo (menores, e separadamente maiores) seja preservada.

**Exemplos:**
```
Input:  nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]

Input:  nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n) esperado
- `pivot` sempre existe em `nums` → garante que o grupo "igual" nunca é vazio
- Ordem relativa preservada dentro de cada grupo → **desqualifica** o particionamento clássico de convergência (tipo quicksort), que costuma embaralhar essa ordem; aqui é preciso saber de antemão ONDE cada grupo começa

## 🧭 Como reconhecer o padrão

"Particionar em grupos preservando a ordem original de cada um" não é resolvido com dois ponteiros convergindo das pontas (isso quebraria a ordem) — é resolvido pré-calculando o **tamanho** de cada grupo (menores, iguais, maiores) e usando um ponteiro de escrita **dedicado** para cada grupo, cada um começando no offset certo dentro do array de resultado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar três listas mutáveis, inserindo cada elemento na lista da sua categoria com `list.add(0, elemento)` sempre no início (para simular acúmulo), ou processando com remoções repetidas de uma cópia do array original.

- Tempo: O(n²) — cada inserção no início de uma lista desloca todos os elementos já presentes · Espaço: O(n) para as três listas
- **Por que não basta:** gasta tempo quadrático numa operação que deveria custar O(1) por elemento; pré-calcular quantos elementos existem em cada categoria permite saber exatamente ONDE cada um vai no resultado final, escrevendo direto sem nenhum deslocamento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, conte quantos elementos são menores que `pivot` (`lessCount`) e quantos são iguais (`equalCount`) — uma passada simples. Isso define os offsets: os "menores" começam na posição `0`, os "iguais" na posição `lessCount`, os "maiores" na posição `lessCount + equalCount`. Numa segunda passada por `nums`, escreva cada elemento na posição do seu grupo, usando um ponteiro de escrita **independente** para cada grupo (avançando só dentro do seu próprio bloco) — isso preserva a ordem relativa automaticamente, já que os elementos de cada grupo são escritos na ordem em que aparecem no `nums` original.

## 🎬 Exemplo passo a passo

`nums = [9,12,5,10,14,3,10]`, `pivot = 10` → `lessCount=3` (9,5,3), `equalCount=2` (10,10)

| Passo | num | Categoria | Ação | lessIdx | equalIdx | greaterIdx |
|---|---|---|---|---|---|---|
| 1 | 9 | < 10 | `result[0]=9` | 1 | 3 | 5 |
| 2 | 12 | > 10 | `result[5]=12` | 1 | 3 | 6 |
| 3 | 5 | < 10 | `result[1]=5` | 2 | 3 | 6 |
| 4 | 10 | == 10 | `result[3]=10` | 2 | 4 | 6 |
| 5 | 14 | > 10 | `result[6]=14` | 2 | 4 | 7 |
| 6 | 3 | < 10 | `result[2]=3` | 3 | 4 | 7 |
| 7 | 10 | == 10 | `result[4]=10` | 3 | 5 | 7 |

Resultado final: `[9,5,3,10,10,12,14]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para contar, outra para escrever no lugar certo
- **Espaço:** O(n) para o array de resultado (exigido pelo problema)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] pivotArray(int[] nums, int pivot) {
    int n = nums.length;
    int lessCount = 0;
    int equalCount = 0;
    for (int num : nums) {
        if (num < pivot) {
            lessCount++;
        } else if (num == pivot) {
            equalCount++;
        }
    }

    int[] result = new int[n];
    int lessIdx = 0;
    int equalIdx = lessCount;
    int greaterIdx = lessCount + equalCount;

    for (int num : nums) {
        if (num < pivot) {
            result[lessIdx++] = num;
        } else if (num == pivot) {
            result[equalIdx++] = num;
        } else {
            result[greaterIdx++] = num;
        }
    }

    return result;
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

- Tentar resolver com dois ponteiros convergindo das pontas (como no particionamento do quicksort) — essa técnica normalmente NÃO preserva a ordem relativa original; aqui, com a ordem sendo uma exigência explícita, são necessários ponteiros de escrita dedicados com offsets pré-calculados, não convergência.
- Esquecer de pré-calcular `lessCount` e `equalCount` ANTES da segunda passada — sem saber de antemão o tamanho de cada grupo, não dá pra saber onde cada um começa no resultado.
- Inverter a ordem dos offsets (menores → iguais → maiores) — os "menores" vêm no offset 0, os "iguais" no offset `lessCount`, os "maiores" no offset `lessCount + equalCount`; trocar essa ordem quebra a condição do enunciado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | `nums=[9,12,5,10,14,3,10]`, `pivot=10` | `[9,5,3,10,10,12,14]` | três grupos bem distribuídos |
| Um só menor | `nums=[-3,4,3,2]`, `pivot=2` | `[-3,2,4,3]` | um só elemento menor, resto maior (mais o próprio pivot) |
| Todos iguais ao pivot | `nums=[5,5,5]`, `pivot=5` | `[5,5,5]` | não há menores nem maiores, só o grupo do meio |
| Pivot é o menor valor | `nums=[1,2,3]`, `pivot=1` | `[1,2,3]` | nenhum elemento menor que o pivot |

## 🔗 Conexões

- Problemas irmãos: [0075] Sort Colors (mesma ideia de particionar em 3 grupos, mas sem exigir preservação de ordem — permite convergência clássica), [2149] Rearrange Array Elements by Sign (mesma técnica de calcular offsets e escrever direto nas posições finais)
- No backend: particionar registros de um relatório em três faixas (abaixo, igual, acima de um limiar) preservando a ordem cronológica original dentro de cada faixa — útil em relatórios financeiros que categorizam transações por valor sem embaralhar a ordem de ocorrência.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
