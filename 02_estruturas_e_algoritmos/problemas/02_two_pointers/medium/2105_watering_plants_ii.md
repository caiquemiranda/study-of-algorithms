# [2105] Watering Plants II

> 🔗 [LeetCode 2105](https://leetcode.com/problems/watering-plants-ii/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Simulation` `#Medium`

## 📜 O Problema

Alice rega as plantas da esquerda pra direita, Bob da direita pra esquerda, simultaneamente, cada um com sua própria lata (capacidades `capacityA`/`capacityB`). Se a água na lata não for suficiente para a planta atual, reabastece antes (instantaneamente) e depois rega. Se os dois chegarem à mesma planta, quem tiver **mais** água rega (empate: Alice). Retorne o número total de reabastecimentos.

**Exemplos:**
```
Input:  plants = [2,2,3,3], capacityA = 5, capacityB = 5
Output: 1

Input:  plants = [2,2,3,3], capacityA = 3, capacityB = 4
Output: 2

Input:  plants = [5], capacityA = 10, capacityB = 8
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^5` → O(n) esperado, e a simulação é inerentemente sequencial (não dá pra "pular" passos)
- `n` pode ser ímpar → sobra uma planta "do meio" tratada por uma regra de desempate especial, fora do loop principal
- `max(plants[i]) <= capacityA, capacityB` → cada lata cheia sempre é suficiente para qualquer planta individual (nunca precisa de 2 reabastecimentos seguidos pra uma só planta)

## 🧭 Como reconhecer o padrão

"Dois agentes avançando de direções opostas, cada um consumindo um recurso próprio até se encontrarem" é a simulação clássica de dois ponteiros: `i` avança da esquerda (Alice), `j` recua da direita (Bob), cada um mantendo seu próprio estado (água restante), até se cruzarem — com uma checagem extra pra planta do meio, se sobrar uma.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar uma lista real (`ArrayList`/`LinkedList`) representando as plantas restantes, removendo literalmente a primeira (Alice) e a última (Bob) a cada passo da simulação.

- Tempo: O(n²) — `remove(0)` num `ArrayList` desloca todos os elementos restantes, custando O(n) por remoção · Espaço: O(n) para a cópia mutável
- **Por que não basta:** a simulação em si já é sequencial (não há como pular passos), mas remover de verdade da estrutura é desnecessário — dois ponteiros simulam a mesma sequência de eventos sem nenhuma remoção física, com custo O(1) por passo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `i=0` (próxima planta de Alice) e `j=n-1` (próxima de Bob), com `waterA`/`waterB` começando cheios. A cada passo: se a água de Alice for insuficiente para `plants[i]`, reabasteça (conte); regue (subtraia) e avance `i`. Faça o mesmo para Bob com `j`, recuando. Repita enquanto `i < j`. Se sobrar `i == j` ao final (planta do meio), aplique a regra de desempate: quem tiver mais água rega; se nenhum dos dois tiver o suficiente, conte mais um reabastecimento.

## 🎬 Exemplo passo a passo

`plants = [2,2,3,3]`, `capacityA = 3`, `capacityB = 4`

| Passo | i | j | waterA (antes) | waterB (antes) | Ação Alice | Ação Bob | refills acumulado |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 3 | 3 | 4 | rega planta 0 (tem o suficiente) → waterA=1 | rega planta 3 (tem o suficiente) → waterB=1 | 0 |
| 2 | 1 | 2 | 1 | 1 | precisa de 2, só tem 1 → **reabastece**, rega → waterA=1 | precisa de 3, só tem 1 → **reabastece**, rega → waterB=1 | 2 |

`i(2) >= j(1)` → loop termina, `n` é par (sem planta do meio) → resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada planta é regada exatamente uma vez, por Alice ou por Bob
- **Espaço:** O(1) — só os índices e os níveis de água atuais

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumRefill(int[] plants, int capacityA, int capacityB) {
    int i = 0;
    int j = plants.length - 1;
    int waterA = capacityA;
    int waterB = capacityB;
    int refills = 0;

    while (i < j) {
        if (waterA < plants[i]) {
            refills++;
            waterA = capacityA;
        }
        waterA -= plants[i];
        i++;

        if (waterB < plants[j]) {
            refills++;
            waterB = capacityB;
        }
        waterB -= plants[j];
        j--;
    }

    // planta do meio (só existe quando n é ímpar): quem tiver mais água a rega
    if (i == j && Math.max(waterA, waterB) < plants[i]) {
        refills++;
    }

    return refills;
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

- Esquecer o caso da planta do MEIO quando `n` é ímpar — quando `i == j` ao final do loop, ainda sobra uma planta, com uma regra de desempate própria que precisa ser checada separadamente.
- Atualizar a água ANTES de checar se precisa reabastecer — a ordem certa é: checar se a água atual é insuficiente, reabastecer SE necessário, e só então subtrair o consumo.
- Confundir a condição de reabastecimento com "água == 0" — a condição certa é "água < necessário pra planta atual"; uma lata pode ter água sobrando mas ainda insuficiente para aquela planta específica.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um só reabastecimento | `plants=[2,2,3,3]`, capacityA=5, capacityB=5 | 1 | só Bob precisa reabastecer, na terceira planta |
| Dois reabastecimentos | `plants=[2,2,3,3]`, capacityA=3, capacityB=4 | 2 | ambos reabastecem no segundo passo |
| Planta única (regra de desempate) | `plants=[5]`, capacityA=10, capacityB=8 | 0 | só existe a planta do meio; Alice tem mais água e cobre sozinha |
| Latas exatamente suficientes | `plants=[1,1]`, capacityA=1, capacityB=1 | 0 | cada um rega exatamente sua planta sem sobrar nem faltar água |

## 🔗 Conexões

- Problemas irmãos: [0088] Merge Sorted Array (mesma estrutura de dois ponteiros avançando de direções opostas), [2570] Merge Two 2D Arrays by Summing Values (mesma família de simular um processo sequencial com estado acumulado por ponteiro)
- No backend: simular dois processos concorrentes consumindo um buffer/recurso limitado a partir de extremidades opostas de uma fila de trabalho — por exemplo, dois workers processando uma fila de tarefas a partir das pontas, cada um com sua própria capacidade, contando quantas vezes cada um precisa recarregar recursos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
