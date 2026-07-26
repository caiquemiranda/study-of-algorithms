# [1365] How Many Numbers Are Smaller Than the Current Number

> 🔗 [LeetCode 1365](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Sorting` `#CountingSort` `#Easy`

## 📜 O Problema

Dado o array `nums`, para cada `nums[i]`, descubra quantos números no array são menores que ele. Ou seja, para cada `nums[i]`, conte o número de `j` válidos tais que `j != i` **e** `nums[j] < nums[i]`.

Retorne a resposta num array.

**Exemplos:**
```
Input:  nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explicação:
Para nums[0]=8 existem quatro números menores (1, 2, 2 e 3).
Para nums[1]=1 não existe nenhum número menor.
Para nums[2]=2 existe um número menor (1).
Para nums[3]=2 existe um número menor (1).
Para nums[4]=3 existem três números menores (1, 2 e 2).

Input:  nums = [6,5,4,8]
Output: [2,1,0,3]

Input:  nums = [7,7,7,7]
Output: [0,0,0,0]
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 500` → pequeno, até O(n²) resolveria, mas O(n+k) é o padrão esperado
- `0 <= nums[i] <= 100` → valores pequenos e limitados, habilita counting sort em vez de comparação par a par

## 🧭 Como reconhecer o padrão

"Para cada elemento, quantos outros são menores que ele" com valores NUMÉRICOS PEQUENOS E LIMITADOS é sempre um sinal de counting sort: conte quantas vezes cada valor aparece, depois construa uma soma de prefixo sobre essas contagens — a soma de prefixo até `valor-1` já é a resposta para qualquer elemento igual a `valor`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada elemento `nums[i]`, percorrer o array inteiro contando quantos `nums[j]` (com `j != i`) são menores que ele.

- Tempo: O(n²) — para cada elemento, uma varredura completa do array · Espaço: O(1) extra
- **Por que não basta:** com n até 500, n² é só 250.000 (aceitável aqui), mas ainda recalcula a mesma comparação repetidamente para valores iguais, quando o counting sort resolve isso para TODOS os valores de uma vez em O(n+k).

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um array de contagem (`contagem[0..100]`) com a frequência de cada valor. Transforme esse array numa soma de prefixo (`contagem[v] += contagem[v-1]`), onde `contagem[v]` passa a representar "quantos elementos são <= v". Para cada elemento, a resposta é `contagem[nums[i]-1]` (ou 0 se `nums[i] == 0`).

## 🎬 Exemplo passo a passo

`nums = [8,1,2,2,3]`

contagem bruta: 1→1, 2→2, 3→1, 8→1. Soma de prefixo (contagem[v] = quantos elementos <= v): contagem[0]=0, contagem[1]=1, contagem[2]=3, contagem[3]=4, ..., contagem[7]=4, contagem[8]=5

| Passo | i | nums[i] | contagem[nums[i]-1] (ou 0 se nums[i]=0) |
|---|---|---|---|
| 1 | 0 | 8 | contagem[7]=4 |
| 2 | 1 | 1 | contagem[0]=0 |
| 3 | 2 | 2 | contagem[1]=1 |
| 4 | 3 | 2 | contagem[1]=1 |
| 5 | 4 | 3 | contagem[2]=3 |

Resultado final: `[4,0,1,1,3]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + k) — n = tamanho de nums, k = intervalo de valores (101)
- **Espaço:** O(k) — para o array de contagem

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] smallerNumbersThanCurrent(int[] nums) {
    int[] contagem = new int[101]; // valores de 0 a 100
    for (int num : nums) {
        contagem[num]++;
    }

    // transforma em soma de prefixo: contagem[v] passa a significar "quantos elementos são <= v"
    for (int v = 1; v <= 100; v++) {
        contagem[v] += contagem[v - 1];
    }

    int[] resultado = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
        resultado[i] = nums[i] == 0 ? 0 : contagem[nums[i] - 1]; // quantos são ESTRITAMENTE menores
    }
    return resultado;
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

- Usar `contagem[nums[i]]` em vez de `contagem[nums[i] - 1]` — isso incluiria elementos IGUAIS a `nums[i]` na contagem, quando o enunciado pede estritamente menores.
- Esquecer de tratar `nums[i] == 0` como caso especial — não existe `contagem[-1]`; se o valor é 0, a resposta é sempre 0 (nada é menor que o menor valor possível).
- Confundir a soma de prefixo (contagem acumulada `<= v`) com a contagem bruta (frequência exata de `v`) — a transformação in-place do array de contagem em soma de prefixo é o que torna a consulta O(1) por elemento.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | `[8,1,2,2,3]` | [4,0,1,1,3] | ilustra o tratamento de duplicatas e o menor valor |
| Sem empates | `[6,5,4,8]` | [2,1,0,3] | cada elemento tem uma contagem distinta |
| Todos iguais | `[7,7,7,7]` | [0,0,0,0] | nenhum elemento é menor que outro igual a ele |
| Contém o valor zero | `[0,2,1]` | [0,2,1] | zero sempre recebe contagem 0 |

## 🔗 Conexões

- Problemas irmãos: [1331] Rank Transform of an Array (mesma ideia de posição relativa, mas com rank sem buracos em vez de contagem), [1051] Height Checker (mesmo domínio de counting sort com valores pequenos e limitados)
- No backend: cálculo de percentil ou posição relativa de um valor numa distribuição (ex.: "quantos usuários gastaram menos que este usuário", usado em dashboards de analytics e sistemas de ranking).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
