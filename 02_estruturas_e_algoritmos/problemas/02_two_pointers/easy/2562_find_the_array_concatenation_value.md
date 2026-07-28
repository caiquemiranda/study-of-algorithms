# [2562] Find the Array Concatenation Value

> 🔗 [LeetCode 2562](https://leetcode.com/problems/find-the-array-concatenation-value/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Simulation` `#Easy`

## 📜 O Problema

Dado um array `nums`, repita até ele esvaziar: se houver mais de um elemento, concatene o primeiro com o último (ex.: `15` e `49` viram `1549`), some ao "valor de concatenação" e remova os dois; se sobrar só um elemento, some-o e remova. Retorne o valor de concatenação final.

**Exemplos:**
```
Input:  nums = [7,52,2,4]
Output: 596
Explicação: 7+4 → 74; depois 52+2 → 522; total = 74+522 = 596.

Input:  nums = [5,14,13,8,12]
Output: 673
Explicação: 5+12→512; 14+8→148; sobra 13 sozinho; total = 512+148+13 = 673.
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 1000` → O(n) esperado
- `1 <= nums[i] <= 10^4` → concatenar dois valores de até 4 dígitos gera um número de até 8-9 dígitos; a SOMA acumulada ao longo de até 500 rodadas pode passar de `int`, exigindo `long`
- O processo sempre pega **primeiro e último** dos elementos restantes → sinaliza convergência das pontas pro centro, não uma ordem arbitrária

## 🧭 Como reconhecer o padrão

"Pegar repetidamente o primeiro e o último elemento restante, combinando-os" é dois ponteiros nas pontas convergindo pro centro — igual a [0088] Merge Sorted Array ou [0977] Squares of a Sorted Array, mas aqui simulando "remoção" sem nunca de fato remover nada da estrutura: só avançando os índices.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar uma lista de verdade (`ArrayList`) e remover literalmente o primeiro e o último elemento a cada rodada com `remove(0)` e `remove(size()-1)`.

- Tempo: O(n²) — `remove(0)` num `ArrayList` desloca todos os elementos restantes, custando O(n) por remoção · Espaço: O(n) para a cópia mutável da lista
- **Por que não basta:** a remoção do início é o gargalo — cada uma custa O(n), e há até `n/2` remoções, dando O(n²) no total. Dois ponteiros simulam exatamente o mesmo processo sem NUNCA mexer na estrutura, só avançando índices.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no início e `right` no fim do array original (sem removê-lo de verdade). Enquanto `left < right`, concatene `nums[left]` com `nums[right]`, some ao total, e avance os dois ponteiros pra dentro — isso simula exatamente "pegar o primeiro e o último e descartá-los". Se `left == right` ao final (array de tamanho ímpar), some esse elemento sozinho.

## 🎬 Exemplo passo a passo

`nums = [7,52,2,4]`

| Passo | left (valor) | right (valor) | Concatenação | Soma acumulada |
|---|---|---|---|---|
| 1 | 0 (7) | 3 (4) | `"7"+"4"="74"` → 74 | 74 |
| 2 | 1 (52) | 2 (2) | `"52"+"2"="522"` → 522 | 596 |

`left(2) >= right(1)` → loop termina, array de tamanho par (sem sobra)

Resultado final: `596` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada elemento é processado uma única vez pelos dois ponteiros
- **Espaço:** O(1) além do necessário pra representar a concatenação em texto

## 💻 Implementações

### Java (referência completa e comentada)
```java
public long findTheArrayConcVal(int[] nums) {
    int left = 0;
    int right = nums.length - 1;
    long total = 0;

    while (left < right) {
        total += Long.parseLong("" + nums[left] + nums[right]);
        left++;
        right--;
    }
    if (left == right) {
        total += nums[left]; // sobrou um elemento sozinho no meio (array de tamanho ímpar)
    }

    return total;
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

- Remover elementos de uma lista real (`ArrayList.remove(0)`) a cada rodada — cada remoção do início é O(n); dois ponteiros simulam a mesma coisa só avançando índices, sem custo de deslocamento.
- Esquecer o caso de array de tamanho ÍMPAR — quando `left == right`, sobra um elemento sozinho no meio, que entra na soma sem concatenar com nada, fora do loop principal.
- Usar `int` para o total (ou até para a concatenação individual) — concatenar dois valores de até `10^4` já gera um número de até 9 dígitos, e a soma acumulada ao longo de até 500 rodadas facilmente estoura `int`; `long` é a escolha segura.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Tamanho par | `[7,52,2,4]` | 596 | duas rodadas, concatenando as pontas |
| Tamanho ímpar | `[5,14,13,8,12]` | 673 | duas rodadas concatenando pontas + 1 elemento sozinho no meio |
| Único elemento | `[5]` | 5 | sem concatenação, só soma o próprio valor |
| Dois elementos | `[1,2]` | 12 | uma única rodada, concatena `"1"+"2"` |

## 🔗 Conexões

- Problemas irmãos: [0088] Merge Sorted Array (mesma ideia de processar as pontas de um array com dois ponteiros), [0977] Squares of a Sorted Array (mesma família de combinar valores das extremidades convergindo pro centro)
- No backend: processar um lote de dados combinando registros das extremidades — por exemplo, reconciliar um lote de transações emparelhando a primeira com a última cronologicamente, evitando remoções reais que custariam realocação de memória.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
