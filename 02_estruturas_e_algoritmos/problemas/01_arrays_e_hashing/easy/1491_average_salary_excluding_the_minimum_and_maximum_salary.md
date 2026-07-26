# [1491] Average Salary Excluding the Minimum and Maximum Salary

> 🔗 [LeetCode 1491](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Você recebe um array de inteiros **únicos** `salary`, onde `salary[i]` é o salário do `i`-ésimo funcionário. Retorne a média salarial excluindo o menor e o maior salário. Respostas dentro de `10^-5` da resposta real são aceitas.

**Exemplos:**
```
Input:  salary = [4000,3000,1000,2000]
Output: 2500.00000
Explicação: mínimo é 1000, máximo é 4000. Média excluindo esses dois: (2000+3000)/2 = 2500

Input:  salary = [1000,2000,3000]
Output: 2000.00000
Explicação: mínimo é 1000, máximo é 3000. Média excluindo esses dois: 2000/1 = 2000
```

**Restrições (e o que elas denunciam):**
- `3 <= salary.length <= 100` → O(n) resolve com folga
- valores únicos → não há ambiguidade sobre "qual" mínimo/máximo excluir (não há empate)

## 🧭 Como reconhecer o padrão

"Excluir o mínimo e o máximo de um cálculo agregado" é resolvido numa única passada, rastreando soma total, mínimo e máximo simultaneamente — a resposta é `(soma - min - max) / (n - 2)`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Ordenar o array, remover o primeiro e o último elemento, e calcular a média do restante.

- Tempo: O(n log n) · Espaço: O(n) para o array ordenado (ou modificação in-place)
- **Por que não basta:** ordenar é mais trabalho do que necessário quando só o mínimo, o máximo e a soma total importam — nenhuma outra informação de ordem é usada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única passada acumulando `soma`, `minimo` e `maximo`. Resultado: `(soma - minimo - maximo) / (n - 2)`.

## 🎬 Exemplo passo a passo

`salary = [4000,3000,1000,2000]`

| Passo | i | salary[i] | soma | minimo | maximo |
|---|---|---|---|---|---|
| 1 | 0 | 4000 | 4000 | 4000 | 4000 |
| 2 | 1 | 3000 | 7000 | 3000 | 4000 |
| 3 | 2 | 1000 | 8000 | 1000 | 4000 |
| 4 | 3 | 2000 | 10000 | 1000 | 4000 |

`(10000 - 1000 - 4000) / (4-2) = 5000/2 = 2500.0` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public double average(int[] salary) {
    int soma = 0;
    int minimo = Integer.MAX_VALUE;
    int maximo = Integer.MIN_VALUE;

    for (int s : salary) {
        soma += s;
        minimo = Math.min(minimo, s);
        maximo = Math.max(maximo, s);
    }

    return (soma - minimo - maximo) / (double) (salary.length - 2);
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

- Fazer a divisão como inteiro em vez de forçar ponto flutuante (`(double)`) — perderia a parte fracionária do resultado.
- Ordenar o array desnecessariamente quando só min/max/soma importam — funciona, mas é mais trabalho do que preciso.
- Esquecer que os valores são garantidos ÚNICOS — não há ambiguidade de "qual" ocorrência do mínimo/máximo excluir, sempre é uma única instância de cada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | [4000,3000,1000,2000] | 2500.0 | exclui min=1000 e max=4000 |
| Array mínimo (3 elementos) | [1000,2000,3000] | 2000.0 | sobra só o elemento do meio |
| Valores no limite | [1000,1000000,500000] | 500000.0 | funciona com valores extremos do intervalo |
| Quatro elementos próximos | [5,3,4,6] | 4.5 | exclui 3 e 6, média de 4 e 5 |

## 🔗 Conexões

- Problemas irmãos: [1619] Mean of Array After Removing Some Elements (mesmo domínio, mas removendo uma porcentagem em vez de só min/max), [0747] Largest Number At Least Twice of Others (mesmo padrão de rastrear extremos numa passada)
- No backend: cálculo de médias "aparadas" (trimmed mean) em análises estatísticas, comum para reduzir o impacto de outliers em relatórios de RH ou benchmarks de performance.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
