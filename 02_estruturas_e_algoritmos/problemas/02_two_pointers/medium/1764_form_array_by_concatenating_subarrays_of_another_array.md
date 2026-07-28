# [1764] Form Array by Concatenating Subarrays of Another Array

> 🔗 [LeetCode 1764](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Medium`

## 📜 O Problema

Dado um array 2D `groups` e um array `nums`, verifique se dá pra escolher `n` subarrays **disjuntos** de `nums` tal que o `i`-ésimo subarray seja exatamente igual a `groups[i]`, e os subarrays apareçam em `nums` na **mesma ordem** de `groups`.

**Exemplos:**
```
Input:  groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
Output: true

Input:  groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
Output: false
Explicação: [10,-2] precisa vir antes de [1,2,3,4], mas está depois.

Input:  groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
Output: false
Explicação: os dois grupos só cabem compartilhando o índice do valor 3.
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^3`, `sum(groups[i].length) <= 10^3`, `nums.length <= 10^3` → uma busca ingênua ainda cabe, mas reaproveitar a posição onde cada grupo termina evita retrabalho
- Subarrays devem ser **disjuntos** e na **mesma ordem** → a busca de cada grupo nunca precisa considerar posições anteriores a onde o grupo anterior terminou

## 🧭 Como reconhecer o padrão

"Encontrar múltiplos padrões, em ordem, sem sobrepor posições já usadas" é a mesma busca de substring de [0028] Find the Index of the First Occurrence in a String, repetida para cada grupo — com a garantia extra de que o ponteiro em `nums` nunca recua entre um grupo e o próximo, só avança.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada grupo, testar todas as posições possíveis em `nums` (mesmo as que já foram usadas por grupos anteriores), e só depois verificar se a combinação escolhida respeita ordem e disjunção.

- Tempo: O(n^(número de grupos)) no pior caso, testando combinações de posições independentemente
- **Por que não basta:** ignora que a exigência de ordem e disjunção já elimina automaticamente qualquer posição anterior a onde o grupo anterior terminou; buscar cada grupo só a partir dali, sequencialmente, evita reconsiderar combinações inválidas de saída.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um ponteiro `i` marcando a partir de onde o próximo grupo pode começar em `nums` (inicialmente 0). Para cada grupo, procure a primeira posição `j >= i` onde os elementos de `nums[j..j+len-1]` batem exatamente com o grupo (igual à busca de substring do LC 28). Se encontrar, avance `i` para logo depois do subarray consumido e passe pro próximo grupo. Se nenhuma posição servir antes de `nums` acabar, a resposta é `false`.

## 🎬 Exemplo passo a passo

`groups = [[1,-1,-1],[3,-2,0]]`, `nums = [1,-1,0,1,-1,-1,3,-2,0]` (n=9)

| Passo | grupo | j (posição testada) | Comparação | Ação |
|---|---|---|---|---|
| 1 | `[1,-1,-1]` | 0 | `nums[0..2]=[1,-1,0]` ≠ grupo | tenta j=1 |
| 2 | `[1,-1,-1]` | 1 | `nums[1..3]=[-1,0,1]` ≠ grupo | tenta j=2 |
| 3 | `[1,-1,-1]` | 2 | `nums[2..4]=[0,1,-1]` ≠ grupo | tenta j=3 |
| 4 | `[1,-1,-1]` | 3 | `nums[3..5]=[1,-1,-1]` == grupo | match! `i=6` |
| 5 | `[3,-2,0]` | 6 | `nums[6..8]=[3,-2,0]` == grupo | match! `i=9` |

Todos os grupos foram encontrados em ordem → resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n × m) no pior caso — para cada grupo, a busca de posição pode escanear boa parte de `nums`; limitado pela soma dos tamanhos dos grupos e pelo tamanho de `nums`
- **Espaço:** O(1) além do necessário para os próprios arrays de entrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean canChoose(int[][] groups, int[] nums) {
    int i = 0; // posição em nums a partir de onde o próximo grupo pode começar
    int n = nums.length;

    for (int[] group : groups) {
        boolean found = false;
        int j = i;
        while (j + group.length <= n) {
            if (matches(nums, j, group)) {
                i = j + group.length; // consome o subarray; o próximo grupo começa depois dele
                found = true;
                break;
            }
            j++;
        }
        if (!found) {
            return false;
        }
    }

    return true;
}

private boolean matches(int[] nums, int start, int[] group) {
    for (int k = 0; k < group.length; k++) {
        if (nums[start + k] != group[k]) {
            return false;
        }
    }
    return true;
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

- Procurar cada grupo a partir da posição 0 de `nums`, em vez de a partir de onde o grupo anterior terminou — isso permitiria "voltar no tempo" e reutilizar posições já consumidas, violando ordem e disjunção.
- Esquecer de checar `j + group.length <= n` antes de comparar — sem esse limite, acessar `nums[j+k]` além do fim do array quebra o código quando o grupo não cabe mais no espaço restante.
- Achar que encontrar o grupo atual garante a resposta final `true` — o grupo atual pode ser encontrado, mas "gastar" `nums` de um jeito que o PRÓXIMO grupo não encontre mais espaço depois; a resposta só é `true` se TODOS os grupos forem encontrados em sequência.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Grupos em sequência | `groups=[[1,-1,-1],[3,-2,0]]`, `nums=[1,-1,0,1,-1,-1,3,-2,0]` | true | ambos os grupos encontrados em ordem, disjuntos |
| Ordem errada | `groups=[[10,-2],[1,2,3,4]]`, `nums=[1,2,3,4,10,-2]` | false | `[1,2,3,4]` aparece ANTES de `[10,-2]`, mas deveria vir depois |
| Sobreposição | `groups=[[1,2,3],[3,4]]`, `nums=[7,7,1,2,3,4,7,7]` | false | os únicos candidatos para os dois grupos compartilham o índice do valor 3 |
| Grupo ausente | `groups=[[5]]`, `nums=[1,2,3]` | false | 5 nunca aparece em `nums` |

## 🔗 Conexões

- Problemas irmãos: [0028] Find the Index of the First Occurrence in a String (mesma técnica de busca de padrão com dois ponteiros, repetida em sequência pra vários padrões), [1961] Check if String Is a Prefix of Array (mesma família de "consumir" um array progressivamente comparando com sub-blocos)
- No backend: validar se uma sequência de eventos observados contém, em ordem e sem sobreposição, uma série de padrões esperados — por exemplo, validar que um log de auditoria contém certas sequências de ações na ordem certa, sem reutilizar o mesmo evento em duas validações.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
