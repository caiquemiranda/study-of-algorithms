# [1550] Three Consecutive Odds

> 🔗 [LeetCode 1550](https://leetcode.com/problems/three-consecutive-odds/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array de inteiros `arr`, retorne `true` se existirem três números ímpares consecutivos no array. Caso contrário, retorne `false`.

**Exemplos:**
```
Input:  arr = [2,6,4,1]
Output: false
Explicação: não há três ímpares consecutivos.

Input:  arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explicação: [5,7,23] são três ímpares consecutivos.
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 1000` → O(n) resolve com folga

## 🧭 Como reconhecer o padrão

"Existem 3 elementos consecutivos que satisfazem uma condição" é o mesmo padrão de contador de streak: cresce enquanto a condição (ser ímpar) se mantém, reseta ao encontrar um par.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, checar se `arr[i]`, `arr[i+1]` e `arr[i+2]` são todos ímpares, sem reaproveitar checagens de janelas anteriores.

- Tempo: O(n) na prática (só 3 checagens por posição), mas recalcula checagens que a janela anterior já fez · Espaço: O(1)
- **Por que vale nomear mesmo assim:** não é uma diferença de complexidade assintótica, é uma questão de elegância — um contador de streak evita reverificar o mesmo elemento múltiplas vezes.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única passada com um contador de ímpares consecutivos; reseta a 0 ao encontrar um par; retorna `true` assim que o contador atinge 3.

## 🎬 Exemplo passo a passo

`arr = [1,2,34,3,4,5,7,23,12]`

| Passo | i | arr[i] | é ímpar? | contador |
|---|---|---|---|---|
| 1 | 0 | 1 | sim | 1 |
| 2 | 1 | 2 | não | 0 |
| 3 | 2 | 34 | não | 0 |
| 4 | 3 | 3 | sim | 1 |
| 5 | 4 | 4 | não | 0 |
| 6 | 5 | 5 | sim | 1 |
| 7 | 6 | 7 | sim | 2 |
| 8 | 7 | 23 | sim | 3 (atinge o alvo!) |

Resultado final: `true` ✔ (encontrado no passo 8, sem processar o resto do array)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — com possível saída antecipada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean threeConsecutiveOdds(int[] arr) {
    int contador = 0;
    for (int num : arr) {
        if (num % 2 != 0) {
            contador++;
            if (contador == 3) {
                return true; // já achou 3 ímpares consecutivos
            }
        } else {
            contador = 0; // par quebra a sequência
        }
    }
    return false;
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

- Usar `num % 2 == 1` em vez de `num % 2 != 0` — hábito mais seguro para lidar com números negativos em outras linguagens (não afeta este problema, já que os valores aqui são positivos).
- Esquecer de resetar o contador ao encontrar um número par — sem o reset, a contagem ficaria incorreta somando ímpares não-consecutivos.
- Verificar `contador >= 3` só no final do loop (depois de processar todo o array) em vez de checar a cada incremento — funciona, mas perde a chance de retornar mais cedo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem 3 consecutivos | [2,6,4,1] | false | nenhuma sequência de 3 ímpares |
| Sequência no meio | [1,2,34,3,4,5,7,23,12] | true | [5,7,23] são 3 ímpares consecutivos |
| Exatamente 3 elementos ímpares | [1,3,5] | true | array inteiro já é a sequência |
| Sequência maior que 3 | [1,3,5,7,9] | true | detecta assim que atinge 3, mesmo havendo mais |

## 🔗 Conexões

- Problemas irmãos: [0485] Max Consecutive Ones (mesmo padrão de contador de streak), [1437] Check If All 1's Are at Least Length K Places Away (mesmo domínio de rastrear posições numa passada)
- No backend: detecção de padrões de anomalia consecutivos em séries de sensores (ex.: alertar se 3 leituras seguidas de temperatura estão fora do padrão esperado).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
