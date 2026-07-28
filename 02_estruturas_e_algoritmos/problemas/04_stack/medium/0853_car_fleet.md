# [0853] Car Fleet

> 🔗 [LeetCode 853](https://leetcode.com/problems/car-fleet/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Sorting`

## 📜 O Problema

Há `n` carros a certas distâncias da milha 0, viajando até a milha `target`. Você recebe `position[i]` (posição inicial) e `speed[i]` (velocidade) de cada carro. Um carro não pode ultrapassar outro, mas pode alcançá-lo e passar a viajar junto (na velocidade do mais lento). Uma **frota** (fleet) é um carro ou grupo de carros viajando juntos; a velocidade da frota é a **mínima** entre os carros que a compõem. Se um carro alcança uma frota exatamente na milha `target`, ainda conta como parte dela. Retorne o número de frotas que chegam ao destino.

**Exemplos:**
```
Input:  target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explicação:
- Carros de 10 (vel 2) e 8 (vel 4) formam uma frota, encontrando-se em 12 (no destino).
- Carro de 0 (vel 1) não alcança ninguém, é uma frota sozinho.
- Carros de 5 (vel 1) e 3 (vel 3) formam uma frota, se encontram em 6.

Input:  target = 10, position = [3], speed = [3]
Output: 1
```

**Restrições (e o que elas denunciam):**
- `n == position.length == speed.length`, `1 <= n <= 10^5` → precisa de solução O(n log n); comparar todos os pares de carros seria O(n²), inviável
- `0 < target <= 10^6`, `0 <= position[i] < target` → todas as posições são válidas e menores que o destino, sem casos de carro já chegado
- Todos os valores de `position` são únicos → não há ambiguidade de "empate" de posição inicial

## 🧭 Como reconhecer o padrão

"Determinar quais elementos se agrupam ao longo de um percurso, onde um elemento mais rápido atrás só pode alcançar (nunca ultrapassar) um mais lento à frente" é resolvido processando os carros em ordem de posição — do **mais próximo do destino para o mais distante** — com uma pilha que guarda o **tempo de chegada** de cada frota já formada. Um carro atrás só se junta à frota da frente se seu tempo de chegada (viajando sozinho) for **menor ou igual** ao tempo da frota à frente — nesse caso, ele é "segurado" e chega junto, não formando uma nova frota.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de carros, simular a posição de ambos ao longo do tempo e verificar se um alcança o outro antes do destino, agrupando-os; repetir até estabilizar os grupos.

- Tempo: O(n²) · Espaço: O(n)
- **Por que não basta:** para `n=10^5`, comparar todos os pares é 10^10 operações — inviável. Além disso, simular posição ao longo do tempo para detectar encontros é impreciso e complexo; comparar **tempos de chegada** diretamente é muito mais simples e exato.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule o **tempo que cada carro levaria para chegar ao destino viajando sozinho**: `(target - position[i]) / speed[i]`. Ordene os carros por posição **decrescente** (do mais próximo do destino para o mais distante — processando "de trás para frente" no espaço, mas do destino em direção à origem). Use uma pilha de tempos de chegada: para cada carro (na ordem processada), se seu tempo de chegada for **maior** que o tempo no topo da pilha, ele nunca alcança a frota à frente antes dela chegar — ele forma sua própria frota nova, empilhe seu tempo. Caso contrário (tempo menor ou igual), ele alcança a frota da frente e viaja junto com ela — não empilha nada novo (a frota já formada "absorve" esse carro, mantendo o tempo de chegada da frota, que é maior). O número de frotas é o tamanho final da pilha.

## 🎬 Exemplo passo a passo

`target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]`

Ordenando por posição decrescente e calculando tempo `(target-pos)/speed`:

| Carro (pos, vel) | Tempo de chegada sozinho |
|---|---|
| (10, 2) | (12-10)/2 = 1.0 |
| (8, 4) | (12-8)/4 = 1.0 |
| (5, 1) | (12-5)/1 = 7.0 |
| (3, 3) | (12-3)/3 = 3.0 |
| (0, 1) | (12-0)/1 = 12.0 |

| Passo | Carro (tempo) | Ação (compara com topo da pilha) | Pilha (tempos) após |
|---|---|---|---|
| 1 | (10, tempo 1.0) | pilha vazia → nova frota | `[1.0]` |
| 2 | (8, tempo 1.0) | `1.0` não é maior que o topo `1.0` → alcança a frota da frente, junta-se a ela | `[1.0]` |
| 3 | (5, tempo 7.0) | `7.0 > 1.0` → nunca alcança, nova frota | `[1.0, 7.0]` |
| 4 | (3, tempo 3.0) | `3.0` não é maior que o topo `7.0` → alcança, junta-se | `[1.0, 7.0]` |
| 5 | (0, tempo 12.0) | `12.0 > 7.0` → nunca alcança, nova frota | `[1.0, 7.0, 12.0]` |

Pilha final tem 3 tempos → 3 frotas.

Resultado final: `3` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação por posição; a passada com a pilha é O(n)
- **Espaço:** O(n) — para os pares ordenados e a pilha de tempos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int carFleet(int target, int[] position, int[] speed) {
    int n = position.length;
    Integer[] indices = new Integer[n];
    for (int i = 0; i < n; i++) indices[i] = i;
    // ordena os índices por posição DECRESCENTE (do mais perto do destino para o mais longe)
    Arrays.sort(indices, (a, b) -> position[b] - position[a]);

    Deque<Double> pilha = new ArrayDeque<>(); // tempos de chegada das frotas já formadas

    for (int idx : indices) {
        double tempo = (double) (target - position[idx]) / speed[idx];
        // se o tempo atual for maior que o topo, este carro nunca alcança a frota da frente
        if (pilha.isEmpty() || tempo > pilha.peek()) {
            pilha.push(tempo); // forma uma nova frota
        }
        // senão: alcança a frota da frente antes dela chegar, junta-se a ela (não empilha nada)
    }

    return pilha.size();
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

- Ordenar por posição **crescente** em vez de decrescente — a lógica depende de processar sempre o carro mais próximo do destino primeiro, já que ele é quem "define" a frota que os carros atrás podem alcançar.
- Usar `>=` em vez de `>` na comparação com o topo da pilha — quando o tempo é exatamente igual, o carro alcança a frota exatamente no destino (segundo o enunciado, isso ainda conta como parte da frota), então a condição de "nova frota" deve ser estritamente `tempo > topo`.
- Empilhar o tempo do carro que se junta a uma frota existente — isso contaria a mesma frota duas vezes; só se empilha quando uma **nova** frota é formada (o carro é rápido demais para alcançar a frente).
- Calcular o tempo com divisão inteira em vez de ponto flutuante — perder a precisão decimal pode fazer comparações de tempo darem resultado errado, especialmente quando os tempos são próximos mas não idênticos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único carro | `target=10, position=[3], speed=[3]` | 1 | caso trivial, sempre uma frota |
| Mesma velocidade nunca se alcançam | `target=10, position=[3,2,1], speed=[1,1,1]` | 3 | com velocidade igual, a distância entre os carros nunca diminui, cada um chega sozinho, formando 3 frotas |
| Todos convergem numa frota só | `target=100, position=[0,2,4], speed=[4,2,1]` | 1 | o carro mais lento vai à frente e os mais rápidos atrás o alcançam em cascata, formando uma única frota |
| Frota se forma exatamente no destino | `target=12, position=[10,8], speed=[2,4]` | 1 | ambos chegam ao destino no mesmo tempo (1.0), contam como uma única frota |

## 🔗 Conexões

- Problemas irmãos: [0739] Daily Temperatures (monotonic stack aplicado a um domínio diferente, mas mesma ideia de resolver comparações numa única passada), [0056] Merge Intervals (também depende de ordenação prévia para simplificar o agrupamento)
- No backend: essa técnica de "elementos posteriores só se agrupam com o anterior se não conseguem ultrapassá-lo" aparece em simulações de tráfego e filas de processamento onde a ordem de chegada e a velocidade de processamento determinam agrupamentos (batching) — por exemplo, agrupar requisições que chegam numa fila e são processadas na velocidade do "gargalo" mais lento à frente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
