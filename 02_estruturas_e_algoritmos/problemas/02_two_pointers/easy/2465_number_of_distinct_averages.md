# [2465] Number of Distinct Averages

> 🔗 [LeetCode 2465](https://leetcode.com/problems/number-of-distinct-averages/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array `nums` de tamanho par, enquanto `nums` não estiver vazio, repita: remova o mínimo, remova o máximo, calcule a média dos dois. Retorne quantas médias **distintas** foram calculadas ao longo do processo.

**Exemplos:**
```
Input:  nums = [4,1,4,0,3,5]
Output: 2
Explicação: remove (0,5)→2.5, remove (1,4)→2.5, remove (3,4)→3.5. Só 2 valores distintos.

Input:  nums = [1,100]
Output: 1
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 100`, tamanho sempre par → garante que min e max nunca "sobram" desemparelhados
- `0 <= nums[i] <= 100` → intervalo pequeno, mas não muda a estratégia
- "Em caso de empate, qualquer um pode ser removido" → sinaliza que a ORDEM de remoção entre iguais não afeta o resultado final

## 🧭 Como reconhecer o padrão

"Remover repetidamente o mínimo e o máximo restantes, combinando-os" é resolvido ordenando o array uma única vez: depois de ordenado, o mínimo e o máximo "restantes" a cada rodada são sempre as próximas posições nas **pontas** ainda não usadas — exatamente o que dois ponteiros convergindo (`left` crescendo, `right` diminuindo) representam.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular literalmente o processo descrito: a cada rodada, percorrer a coleção restante procurando o mínimo e o máximo atuais (sem pré-ordenar), removê-los, calcular a média e guardar num conjunto.

- Tempo: O(n²) — cada busca de mínimo/máximo é O(tamanho restante), repetida `n/2` vezes · Espaço: O(n) para o conjunto de resultados
- **Por que não basta:** refaz a busca de mínimo e máximo do zero a cada rodada; ordenando o array uma única vez, dois ponteiros nas pontas já sabem exatamente onde estão o mínimo e o máximo restantes, sem nenhuma busca repetida.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `nums`. Use `left` no início e `right` no fim. A cada passo, o par `(nums[left], nums[right])` é exatamente o mínimo e o máximo restantes (já que tudo entre eles ainda não foi processado, e tudo fora já foi). Guarde a **soma** `nums[left] + nums[right]` num `Set` (duas médias são iguais se e só se as somas forem iguais, já que ambas dividem pelo mesmo `2`) e avance os dois ponteiros pra dentro. O tamanho final do conjunto é a resposta.

## 🎬 Exemplo passo a passo

`nums = [4,1,4,0,3,5]` → ordenado: `[0,1,3,4,4,5]`

| Passo | left (valor) | right (valor) | soma | média equivalente | Set de somas depois |
|---|---|---|---|---|---|
| 1 | 0 (0) | 5 (5) | 5 | 2.5 | `{5}` |
| 2 | 1 (1) | 4 (4) | 5 | 2.5 (repetida) | `{5}` |
| 3 | 2 (3) | 3 (4) | 7 | 3.5 | `{5, 7}` |

Tamanho final do conjunto: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura com dois ponteiros depois é O(n)
- **Espaço:** O(n) para o conjunto de somas (no pior caso, todas distintas)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int distinctAverages(int[] nums) {
    Arrays.sort(nums);
    int n = nums.length;
    Set<Integer> sums = new HashSet<>(); // guarda a SOMA, não a média, evita comparação de ponto flutuante
    int left = 0;
    int right = n - 1;

    while (left < right) {
        sums.add(nums[left] + nums[right]); // duas médias são iguais <=> duas somas são iguais
        left++;
        right--;
    }

    return sums.size();
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

- Recalcular mínimo/máximo a cada rodada sem ordenar primeiro — depois de ordenado, o mínimo e o máximo "restantes" são sempre `nums[left]` e `nums[right]`, sem necessidade de buscar nada a cada iteração.
- Comparar médias como `double` diretamente num `Set<Double>` — funciona neste problema específico (a divisão por 2 sempre dá um valor exatamente representável em ponto flutuante), mas guardar a SOMA num `Set<Integer>` é mais simples e evita qualquer dúvida sobre comparação de ponto flutuante em geral.
- Esquecer que "duas médias iguais" equivale a "duas somas iguais" (ambas divididas pela mesma constante, 2) — por isso comparar as somas diretamente já resolve o problema sem nunca calcular a média de fato.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Médias repetidas | `[4,1,4,0,3,5]` | 2 | duas rodadas dão a mesma média (2.5), só 3.5 é distinta |
| Só um par | `[1,100]` | 1 | array de tamanho 2, uma única rodada |
| Todos os valores iguais | `[5,5,5,5]` | 1 | toda combinação min/max dá a mesma média |
| Array já ordenado, médias distintas | `[1,2,3,100]` | 2 | `(1+100)/2=50.5` e `(2+3)/2=2.5`, ambas diferentes |

## 🔗 Conexões

- Problemas irmãos: [0977] Squares of a Sorted Array (mesma técnica de ordenar e usar dois ponteiros nas pontas), [0011] Container With Most Water (mesma família de combinar os extremos de um array, avançando os ponteiros pra dentro)
- No backend: parear repetidamente os itens "mais extremos" de uma lista — por exemplo, balancear uma fila de tarefas emparelhando a mais urgente com a menos urgente, calculando alguma métrica combinada por rodada, usando ordenação prévia pra evitar buscas repetidas de mínimo/máximo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
