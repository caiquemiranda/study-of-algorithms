# [1619] Mean of Array After Removing Some Elements

> 🔗 [LeetCode 1619](https://leetcode.com/problems/mean-of-array-after-removing-some-elements/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array de inteiros `arr`, retorne a média dos inteiros restantes após remover os menores `5%` e os maiores `5%` dos elementos. Respostas dentro de `10^-5` da resposta real são aceitas.

**Exemplos:**
```
Input:  arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
Explicação: após remover o mínimo e o máximo, todos os elementos são iguais a 2, então a média é 2.

Input:  arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
Output: 4.00000
```

**Restrições (e o que elas denunciam):**
- `20 <= arr.length <= 1000`, múltiplo de 20 → garante que 5% é sempre um número inteiro de elementos
- `0 <= arr[i] <= 10^5` → valores pequenos, sem overflow

## 🧭 Como reconhecer o padrão

"Remover uma PORCENTAGEM dos extremos (menores/maiores) antes de calcular uma métrica agregada" é resolvido ordenando o array e usando os índices calculados a partir da porcentagem para definir o intervalo restante — generalização de [1491], que remove só 1 elemento de cada ponta.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Ordenar o array, remover os `5%` menores e `5%` maiores elementos criando um novo array, e calcular a média do que sobrou.

- Tempo: O(n log n) — dominado pela ordenação · Espaço: O(n) para o array reduzido
- Isso já é a abordagem correta e eficiente aqui; não há uma versão "pior" relevante além de não ordenar (o que tornaria impossível identificar os extremos sem comparação par a par O(n²)).

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Ordene o array. Calcule `remover = arr.length * 5 / 100` (quantos elementos remover de CADA ponta). Some os elementos do índice `remover` até `arr.length - remover - 1` (inclusive), e divida pela quantidade de elementos somados.

## 🎬 Exemplo passo a passo

`arr` com 20 elementos, quase todos "2" — `remover = 20 × 5 / 100 = 1` (remove 1 de cada ponta)

| Passo | Cálculo | Valor |
|---|---|---|
| 1 | remover | 1 |
| 2 | índice inicial (remover) | 1 |
| 3 | índice final (length-remover-1) | 18 |
| 4 | soma dos elementos de 1 a 18 | 18 × 2 = 36 |
| 5 | quantidade de elementos somados | 18 |
| 6 | média | 36/18 = 2.0 |

Resultado final: `2.00000` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação
- **Espaço:** O(1) extra (fora o array ordenado in-place)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public double trimMean(int[] arr) {
    Arrays.sort(arr);
    int n = arr.length;
    int remover = n * 5 / 100; // 5% de cada ponta, sempre inteiro dado que n é múltiplo de 20

    long soma = 0;
    int quantidade = 0;
    for (int i = remover; i < n - remover; i++) {
        soma += arr[i];
        quantidade++;
    }
    return (double) soma / quantidade;
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

- Calcular `remover` como `n * 0.05` usando ponto flutuante e depois arredondar — pode gerar imprecisão; como `n` é garantido múltiplo de 20, `n * 5 / 100` com aritmética inteira já é exato.
- Esquecer que a remoção acontece nas DUAS pontas simultaneamente — o intervalo de soma vai de `remover` até `n - remover - 1`, não só de um lado.
- Usar `int` para a soma em vez de `long` — com até 1000 elementos de até 10^5, a soma ainda cabe em `int`, mas usar `long` é mais seguro como hábito para evitar overflow em variações do problema com limites maiores.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Maioria dos elementos iguais | 20 elementos, quase todos "2" | 2.00000 | remoção das pontas não afeta o valor dominante |
| Distribuição variada | [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0] | 4.00000 | caso do enunciado com 20 elementos |
| Array maior (40 elementos) | ver exemplo 3 do enunciado | 4.77778 | ilustra que a técnica escala para arrays maiores |
| Todos os elementos iguais | 20 elementos, todos "7" | 7.00000 | remoção não muda nada quando não há variação |

## 🔗 Conexões

- Problemas irmãos: [1491] Average Salary Excluding the Minimum and Maximum Salary (mesma ideia, mas removendo só 1 elemento de cada ponta em vez de uma porcentagem), [1200] Minimum Absolute Difference (mesma técnica base de ordenar antes de processar)
- No backend: cálculo de médias aparadas (trimmed mean) em relatórios estatísticos para reduzir a influência de outliers (ex.: métricas de latência de rede, onde 5% dos valores mais extremos costumam ser ruído).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
