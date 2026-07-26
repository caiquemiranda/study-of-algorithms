# [1450] Number of Students Doing Homework at a Given Time

> 🔗 [LeetCode 1450](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Você recebe dois arrays de inteiros `startTime` e `endTime` e um inteiro `queryTime`. O `i`-ésimo aluno começou a fazer a lição de casa no tempo `startTime[i]` e terminou no tempo `endTime[i]`.

Retorne o número de alunos fazendo lição de casa no tempo `queryTime` — mais formalmente, o número de alunos onde `queryTime` está no intervalo `[startTime[i], endTime[i]]`, inclusive.

**Exemplos:**
```
Input:  startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explicação: temos 3 alunos: o primeiro começou em 1 e terminou em 3, não fazia nada no tempo 4.
O segundo começou em 2 e terminou em 2, também não fazia nada no tempo 4.
O terceiro começou em 3 e terminou em 7, era o único fazendo lição de casa no tempo 4.

Input:  startTime = [4], endTime = [4], queryTime = 4
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= startTime.length <= 100` → O(n) resolve com folga
- `1 <= startTime[i] <= endTime[i] <= 1000` → intervalos fechados nos dois extremos

## 🧭 Como reconhecer o padrão

"Quantos intervalos contêm um ponto X" com poucos intervalos é resolvido com uma passada simples comparando cada intervalo com o ponto de consulta — não precisa de estrutura mais sofisticada para n pequeno.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Já é a solução ótima aqui, pois n é pequeno: para cada aluno, verificar se `startTime[i] <= queryTime <= endTime[i]`.

- Tempo: O(n) · Espaço: O(1)
- **Por que vale nomear mesmo assim:** não há uma versão "pior" real; a única armadilha é usar comparação estrita em vez de inclusiva.

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Percorra os dois arrays em paralelo, incrementando um contador toda vez que `queryTime` cai dentro do intervalo `[startTime[i], endTime[i]]`.

## 🎬 Exemplo passo a passo

`startTime = [1,2,3]`, `endTime = [3,2,7]`, `queryTime = 4`

| Passo | i | startTime[i] | endTime[i] | 4 está no intervalo? |
|---|---|---|---|---|
| 1 | 0 | 1 | 3 | não (4>3) |
| 2 | 1 | 2 | 2 | não (4>2) |
| 3 | 2 | 3 | 7 | sim |

Resultado final: `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
    int contador = 0;
    for (int i = 0; i < startTime.length; i++) {
        if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
            contador++;
        }
    }
    return contador;
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

- Usar `<` em vez de `<=` — o intervalo é fechado nas duas pontas (inclusive), então `queryTime` igual ao início ou fim ainda conta.
- Tentar otimizar prematuramente com estruturas de dados complexas (ex.: array de diferença) para n ≤ 100 — desnecessário, a passada linear já é ótima para este tamanho.
- Confundir `startTime[i]` com `endTime[i]` na comparação — o intervalo válido é sempre `startTime[i] <= endTime[i]`, garantido pelo enunciado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um aluno no intervalo | startTime=[1,2,3], endTime=[3,2,7], queryTime=4 | 1 | só o terceiro aluno cobre o tempo 4 |
| Consulta exatamente na borda | startTime=[4], endTime=[4], queryTime=4 | 1 | intervalo de duração zero, ainda inclusivo |
| Nenhum aluno | startTime=[1], endTime=[2], queryTime=5 | 0 | consulta fora de todos os intervalos |
| Todos cobrem | startTime=[1,1,1], endTime=[10,10,10], queryTime=5 | 3 | todos os intervalos cobrem o ponto |

## 🔗 Conexões

- Problemas irmãos: [0252] Meeting Rooms (mesmo domínio de intervalos), [1893] Check if All the Integers in a Range Are Covered (mesma ideia de verificar cobertura de um ponto/intervalo)
- No backend: verificação de quantas sessões/processos estavam ativos num timestamp específico (ex.: monitoramento de concorrência em sistemas distribuídos).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
