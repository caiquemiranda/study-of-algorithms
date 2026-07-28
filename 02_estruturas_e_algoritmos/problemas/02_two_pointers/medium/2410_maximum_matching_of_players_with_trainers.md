# [2410] Maximum Matching of Players With Trainers

> 🔗 [LeetCode 2410](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Greedy` `#Sorting` `#Medium`

## 📜 O Problema

Dado `players[i]` (habilidade de cada jogador) e `trainers[j]` (capacidade de cada treinador), um jogador pode ser pareado com um treinador se `players[i] <= trainers[j]`. Cada jogador usa no máximo um treinador, e vice-versa. Retorne o número **máximo** de pares possíveis.

**Exemplos:**
```
Input:  players = [4,7,9], trainers = [8,2,5,8]
Output: 2

Input:  players = [1,1,1], trainers = [10]
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= players.length, trainers.length <= 10^5` → força bruta O(n×m) pode chegar a 10^10; O((n+m) log(n+m)) é o esperado
- `1 <= players[i], trainers[j] <= 10^9` → sem casos negativos ou zero pra tratar
- **É literalmente o mesmo problema de [0455] Assign Cookies** — só os nomes mudam (jogador/treinador em vez de criança/biscoito), a lógica é idêntica

## 🧭 Como reconhecer o padrão

"Combinar dois grupos por um critério de limiar (`<=`), maximizando o número de pares" é resolvido ordenando os dois arrays e usando dois ponteiros greedy: tente satisfazer o jogador **menos** habilidoso restante com o treinador de **menor** capacidade suficiente — se esse treinador não servir nem pra ele, não serve pra nenhum outro jogador (todos os demais são igual ou mais habilidosos).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada jogador (em qualquer ordem), percorrer todos os treinadores ainda não usados procurando algum com capacidade suficiente.

- Tempo: O(n × m) — no pior caso, cada jogador escaneia todos os treinadores restantes · Espaço: O(1) além do controle de "usado"
- **Por que não basta:** ignora a estrutura que a ordenação oferece; sem processar jogadores e treinadores do menor para o maior, não há garantia de estar fazendo a escolha ótima a cada passo, e o tempo vira quadrático.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `players` e `trainers`. Use `i` no jogador menos habilidoso ainda não pareado, e `j` no treinador de menor capacidade ainda não usado. Se `trainers[j] >= players[i]`, esse treinador serve pra esse jogador — conte e avance os dois ponteiros. Se não servir, esse treinador é fraco demais até para o jogador menos exigente de todos os restantes, então descarte-o avançando só `j`.

## 🎬 Exemplo passo a passo

`players = [4,7,9]` (ordenado), `trainers = [2,5,8,8]` (ordenado)

| Passo | i | j | players[i] | trainers[j] | Suficiente? | Ação |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 4 | 2 | não | descarta o treinador: j=1 |
| 2 | 0 | 1 | 4 | 5 | sim | pareia: i=1, j=2, count=1 |
| 3 | 1 | 2 | 7 | 8 | sim | pareia: i=2, j=3, count=2 |
| 4 | 2 | 3 | 9 | 8 | não | descarta o treinador: j=4 (fim) |

Resultado final: `count = 2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n + m log m) — dominado pela ordenação dos dois arrays; o scan com dois ponteiros depois é O(n + m)
- **Espaço:** O(log n + log m) para o espaço interno do sort

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int matchPlayersAndTrainers(int[] players, int[] trainers) {
    Arrays.sort(players);
    Arrays.sort(trainers);

    int i = 0;
    int j = 0;
    int count = 0;

    while (i < players.length && j < trainers.length) {
        if (trainers[j] >= players[i]) {
            // treinador atual dá conta do jogador menos habilidoso restante: pareia os dois
            count++;
            i++;
            j++;
        } else {
            // treinador fraco demais até pro jogador menos exigente: não serve pra ninguém mais
            j++;
        }
    }

    return count;
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

- Não ordenar os dois arrays antes — sem ordenação, a escolha greedy "usa o treinador de menor capacidade suficiente" não tem garantia de ser ótima.
- Avançar `i` e `j` juntos mesmo quando `trainers[j] < players[i]` — isso descartaria um jogador que ainda poderia ser pareado com um treinador de capacidade maior.
- Achar que é um problema diferente de [0455] Assign Cookies só porque os nomes mudaram — é exatamente o mesmo problema, com a mesma solução.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | `players=[4,7,9]`, `trainers=[8,2,5,8]` | 2 | dois pares válidos, um jogador fica sem treinador |
| Mais jogadores que treinadores | `players=[1,1,1]`, `trainers=[10]` | 1 | só um treinador disponível, mesmo servindo pra todos |
| Nenhum par possível | `players=[10]`, `trainers=[1,2,3]` | 0 | nenhum treinador tem capacidade suficiente |
| Todos pareáveis | `players=[1,2]`, `trainers=[2,3]` | 2 | ambos os jogadores encontram treinador |

## 🔗 Conexões

- Problemas irmãos: [0455] Assign Cookies (o MESMO problema, com outro enunciado — citado explicitamente no próprio enunciado deste), [0016] 3Sum Closest (mesma família de "ordenar e usar dois ponteiros com decisão greedy" sobre arrays)
- No backend: alocação greedy de recursos com requisito mínimo — por exemplo, atribuir servidores com capacidade mínima a tarefas que exigem um limiar de CPU/memória, maximizando quantas tarefas são atendidas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
