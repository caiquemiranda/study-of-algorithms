# [2073] Time Needed to Buy Tickets

> 🔗 [LeetCode 2073](https://leetcode.com/problems/time-needed-to-buy-tickets/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Queue` `#Array` `#Simulation`

## 📜 O Problema

Há `n` pessoas numa fila para comprar ingressos, onde a pessoa `0` está na **frente** e a `(n-1)`-ésima está no **fim**. Você recebe um array `tickets`, onde `tickets[i]` é a quantidade de ingressos que a `i`-ésima pessoa quer comprar.

Cada pessoa leva **exatamente 1 segundo** para comprar 1 ingresso. Uma pessoa só compra 1 ingresso por vez e, se ainda quiser mais, volta **instantaneamente** para o **fim** da fila. Se não quiser mais ingressos, sai da fila.

Retorne o **tempo total** até a pessoa que estava **inicialmente na posição `k`** terminar de comprar todos os seus ingressos.

**Exemplos:**
```
Input:  tickets = [2,3,2], k = 2
Output: 6
Explicação: a fila roda em ciclos até a pessoa k (a 3ª, índice 2) esgotar seus 2 ingressos após 6 segundos no total.

Input:  tickets = [5,1,1,1], k = 0
Output: 8
```

**Restrições (e o que elas denunciam):**
- `n == tickets.length`, `1 <= n <= 100`, `1 <= tickets[i] <= 100` → tamanho e valores minúsculos; até uma simulação literal O(n × max(tickets)) passaria tranquilamente
- `0 <= k < n` → `k` é sempre um índice válido dentro da fila

## 🧭 Como reconhecer o padrão

O enunciado descreve literalmente uma **fila** que rotaciona: quem chega na frente compra um ingresso e, se quiser mais, volta pro fim — o padrão clássico de simulação com fila (FIFO). A observação que leva à solução ótima é que, para saber quanto tempo a pessoa `k` demora, você não precisa simular segundo a segundo: basta contar, para cada pessoa, **quantas vezes** ela chega à frente da fila **antes ou junto com** a última compra da pessoa `k`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simule literalmente com uma fila de pares `(índice, ingressos_restantes)`. A cada segundo, retire a pessoa da frente, decremente seus ingressos restantes, incremente o tempo; se ela ainda quiser mais, recoloque no fim da fila; se o índice retirado for `k` e seus ingressos chegaram a 0, retorne o tempo atual.

- Tempo: O(n × max(tickets)) · Espaço: O(n)
- **Por que não basta:** essa simulação já passaria nos limites deste problema, mas faz trabalho segundo a segundo quando a resposta pode ser calculada diretamente: cada pessoa `i` contribui com um número de segundos **previsível** sem precisar simular a rotação real da fila.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pense em quantas vezes cada pessoa `i` compra um ingresso **até o momento em que `k` termina**. A pessoa `k` termina depois de exatamente `tickets[k]` compras suas. Para qualquer outra pessoa `i`:
- Se `i` está **na frente de `k` ou é a própria `k`** (`i <= k`): ela terá a chance de comprar até `tickets[k]` ingressos junto com `k` (uma rodada a mais, já que passa antes) — então ela contribui `min(tickets[i], tickets[k])` segundos.
- Se `i` está **atrás de `k`** (`i > k`): ela só chega à frente **depois** que `k` já passou naquela rodada, então na última rodada de `k` ela não participa mais — contribui `min(tickets[i], tickets[k] - 1)` segundos.

A resposta é a soma dessas contribuições de todas as pessoas.

## 🎬 Exemplo passo a passo

`tickets = [2,3,2], k = 2` (então `tickets[k] = 2`)

| Passo | i | tickets[i] | i <= k? | Contribuição | Soma acumulada |
|---|---|---|---|---|---|
| 1 | 0 | 2 | sim (0<=2) | `min(2, 2) = 2` | 2 |
| 2 | 1 | 3 | sim (1<=2) | `min(3, 2) = 2` | 4 |
| 3 | 2 | 2 | sim (é o próprio k) | `min(2, 2) = 2` | 6 |

Não há índices `i > k` neste exemplo (k é o último). Resultado final: `6` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelo array `tickets`
- **Espaço:** O(1) — só um acumulador de tempo

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int timeRequiredToBuy(int[] tickets, int k) {
    int tempo = 0;
    int alvo = tickets[k]; // quantas rodadas completas a pessoa k precisa

    for (int i = 0; i < tickets.length; i++) {
        if (i <= k) {
            // está na frente de k (ou é k): participa até a rodada final de k, inclusive
            tempo += Math.min(tickets[i], alvo);
        } else {
            // está atrás de k: só participa até a rodada ANTERIOR à última de k
            tempo += Math.min(tickets[i], alvo - 1);
        }
    }

    return tempo;
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

- Usar `tickets[k]` para todo mundo, inclusive quem está atrás de `k` — quem está atrás só passa pela frente **depois** de `k` já ter comprado naquela rodada; usar `alvo` sem o `-1` para `i > k` conta uma compra a mais que nunca acontece antes de `k` terminar.
- Inverter a condição `i <= k` com `i < k` — a própria pessoa `k` deve usar `min(tickets[k], alvo)` que é simplesmente `tickets[k]` (ela sempre contribui o total de seus próprios ingressos), o que só acontece corretamente se `k` cair no ramo `i <= k`.
- Tentar simular segundo a segundo mesmo sabendo da fórmula — funciona para os limites pequenos deste problema, mas não generaliza e é mais propenso a bugs de índice de rotação de fila do que a contagem direta.
- Esquecer que a resposta é uma **soma de contribuições independentes**, não um valor único — cada pessoa da fila (inclusive `k`) contribui uma parcela de tempo, e a resposta final soma todas.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k é a primeira pessoa da fila | `tickets=[5,1,1,1], k=0` | 8 | testa o ramo `i > k` para todas as outras pessoas |
| k é a última pessoa da fila | `tickets=[2,3,2], k=2` | 6 | todos os outros estão `i <= k`, participam da rodada final |
| Só uma pessoa na fila | `tickets=[5], k=0` | 5 | sem ninguém mais, o tempo é simplesmente `tickets[k]` |
| Pessoa à frente quer poucos ingressos | `tickets=[1,5], k=1` | 6 | a pessoa 0 sai da fila logo no 1º segundo (`min(1,5)=1`); a pessoa k então compra os 5 restantes sozinha, sem mais ninguém para rotacionar (`min(5,5)=5`); soma total 6 |

## 🔗 Conexões

- Problemas irmãos: [1700] Number of Students Unable to Eat Lunch (outra simulação de fila que se resolve com contagem/matemática em vez de simulação literal), [0933] Number of Recent Calls (fila real onde a ordem e o tempo importam de fato)
- No backend: transformar uma simulação passo a passo numa fórmula de contagem direta é uma otimização comum em sistemas de filas de atendimento (call centers, filas de impressão) quando se quer estimar o tempo de espera de uma posição específica sem precisar simular o sistema inteiro em tempo real.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
