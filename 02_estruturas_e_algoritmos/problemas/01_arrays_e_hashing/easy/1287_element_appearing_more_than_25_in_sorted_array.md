# [1287] Element Appearing More Than 25% In Sorted Array

> 🔗 [LeetCode 1287](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array de inteiros **ordenado** em ordem não-decrescente, existe exatamente um inteiro no array que ocorre mais de 25% das vezes. Retorne esse inteiro.

**Exemplos:**
```
Input:  arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Input:  arr = [1,1]
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 10^4` → O(n) resolve com folga
- array já vem ORDENADO em ordem não-decrescente → elementos iguais ficam sempre AGRUPADOS de forma contígua, então contar "sequências" é suficiente (não precisa de hash map)
- garantido que existe exatamente um elemento que passa de 25% → não precisa tratar empate ou ausência de resposta

## 🧭 Como reconhecer o padrão

"Elemento que aparece mais que uma fração X do array, e o array já está ORDENADO" é um sinal para aproveitar que ocorrências duplicadas ficam agrupadas — em vez de um hash map de frequência (que ignoraria a ordenação), basta contar o tamanho de cada sequência contígua igual e comparar com o limiar.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar um hash map de frequência, contando cada valor do array, e depois percorrer o mapa procurando o valor cuja contagem excede 25% do tamanho do array.

- Tempo: O(n) — na verdade já é linear, mas ignora a informação extra de que o array está ordenado, gastando espaço O(k) desnecessário para o hash map · Espaço: O(k), k = valores distintos
- **Por que não basta:** não é assintoticamente pior, mas desperdiça a estrutura já ordenada do array (que garante que basta contar sequências contíguas, sem precisar de um mapa por valor).

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array com um contador de sequência atual. Toda vez que o valor mudar, reinicie o contador; toda vez que o contador ultrapassar `n/4`, esse valor já é a resposta (retorne imediatamente, sem esperar terminar a sequência).

## 🎬 Exemplo passo a passo

`arr = [1,2,2,6,6,6,6,7,10]` (n=9, limiar = 9/4 = 2.25, contagem > 2.25 significa >= 3)

| Passo | i | arr[i] | contador da sequência atual | contador > n/4 (2.25)? |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | não |
| 2 | 1 | 2 | 1 (novo valor, reinicia) | não |
| 3 | 2 | 2 | 2 | não |
| 4 | 3 | 6 | 1 (novo valor, reinicia) | não |
| 5 | 4 | 6 | 2 | não |
| 6 | 5 | 6 | 3 | **sim** (3 > 2.25) |

Resultado final: `6` ✔ (encontrado no passo 6, sem precisar processar o resto do array)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada, com possível saída antecipada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findSpecialInteger(int[] arr) {
    int n = arr.length;
    int contador = 1;

    for (int i = 1; i < n; i++) {
        if (arr[i] == arr[i - 1]) {
            contador++;
        } else {
            contador = 1; // valor mudou, reinicia contando o elemento atual
        }
        if (contador > n / 4.0) {
            return arr[i]; // já ultrapassou 25%, é a resposta garantida pelo enunciado
        }
    }
    return arr[0]; // caso raro: array pequeno onde o próprio primeiro elemento já domina sozinho
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

- Usar divisão inteira (`n / 4`) em vez de `n / 4.0` na comparação — para `n` não múltiplo de 4, a divisão inteira arredonda para baixo e pode aceitar uma contagem que na verdade não passa de 25% real (ex.: `n=9`, `n/4=2` inteiro, mas o limiar real é 2.25, não 2).
- Ignorar que o array está ordenado e usar um hash map de qualquer forma — funciona, mas é uma oportunidade perdida de resolver com O(1) de espaço extra em vez de O(k).
- Não considerar que a sequência vencedora pode estar em qualquer posição do array — o código já lida com isso naturalmente, pois a checagem acontece a cada iteração, não só ao trocar de valor.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sequência no meio | `[1,2,2,6,6,6,6,7,10]` | 6 | "6" aparece 4 vezes em 9 elementos (44%) |
| Array de dois elementos iguais | `[1,1]` | 1 | 100% de ocorrência, trivialmente passa de 25% |
| Sequência logo no início | `[5,5,5,6,7,8,9,10]` | 5 | "5" aparece 3 de 8 (37.5%), ultrapassa o limiar já no início |
| n não múltiplo de 4 | `[1,1,1,1,2]` | 1 | ilustra a importância de usar divisão em ponto flutuante |

## 🔗 Conexões

- Problemas irmãos: [0169] Majority Element (mesmo domínio de "elemento dominante", mas sem garantia de array ordenado), [0830] Positions of Large Groups (mesma técnica de contar sequências contíguas aproveitando agrupamento)
- No backend: detecção de valores dominantes em dados já ordenados (ex.: um relatório de vendas ordenado por produto onde um item responde por mais de 25% do volume) — aproveitar a ordenação evita estruturas de dados extras.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
