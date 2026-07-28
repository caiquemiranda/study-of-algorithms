# [0649] Dota2 Senate

> 🔗 [LeetCode 649](https://leetcode.com/problems/dota2-senate/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Queue` `#Greedy` `#String`

## 📜 O Problema

No mundo de Dota2, há dois partidos: Radiant e Dire. O senado é composto por senadores dos dois partidos, e a votação é feita em rodadas. Em cada rodada, cada senador (na ordem em que aparece na string, ciclicamente) pode: **banir o direito de voto** de outro senador (permanentemente, nesta e em todas as rodadas seguintes), ou **anunciar vitória** se todos os senadores com direito a voto restantes forem do mesmo partido.

Você recebe uma string `senate`, onde `'R'` e `'D'` representam os partidos. Supondo que cada senador joga a melhor estratégia possível para seu partido, retorne qual partido vence: `"Radiant"` ou `"Dire"`.

**Exemplos:**
```
Input:  senate = "RD"
Output: "Radiant"
Explicação: o senador R bane o D na rodada 1; na rodada 2, só R vota, então R vence.

Input:  senate = "RDD"
Output: "Dire"
Explicação: R bane o primeiro D; o segundo D bane R; sobra só D, que vence.
```

**Restrições (e o que elas denunciam):**
- `n == senate.length`, `1 <= n <= 10^4` → precisa de solução O(n) ou O(n log n); simular rodada por rodada sem otimização poderia degradar
- `senate[i]` é `'R'` ou `'D'` → só dois partidos, o que permite raciocinar diretamente sobre "quem vem primeiro" entre os dois grupos

## 🧭 Como reconhecer o padrão

"Processar elementos em ordem circular, onde cada um pode eliminar o próximo oponente encontrado, e o processo se repete em rodadas até sobrar só um grupo" é a assinatura de simulação com **fila**: cada senador só se importa com o **próximo oponente pela frente** (não com todos de uma vez), e quem sobrevive uma rodada "volta para o fim da fila" para a próxima rodada — comportamento FIFO clássico, análogo a [1700] Number of Students Unable to Eat Lunch.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular rodada por rodada com uma lista mutável: em cada rodada, percorrer os senadores restantes na ordem, e cada um bane o próximo oponente que encontrar (marcando-o como removido); repetir até só sobrar um partido.

- Tempo: O(n²) pior caso (cada rodada pode ser O(n), e o número de rodadas também pode ser O(n)) · Espaço: O(n)
- **Por que não basta:** remover elementos de uma lista no meio da iteração é custoso e propenso a bugs de índice (você não pode simplesmente remover enquanto itera). A solução com duas filas resolve isso naturalmente, sem precisar "pular" elementos removidos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use duas filas, uma com os **índices** dos senadores `Radiant` e outra com os índices dos senadores `Dire`, na ordem original. A cada passo, compare a frente das duas filas: o senador com o **menor índice** age primeiro (ele vem antes na ordem de votação) e bane o da outra fila (remove-o permanentemente, sem recolocá-lo). O senador vencedor desta comparação volta para o **fim da sua própria fila**, mas com um índice **`+n`** (representando que ele age de novo só na próxima rodada, depois de todos os outros que ainda restam nesta rodada). Repita até uma das filas esvaziar — o partido da fila não-vazia vence.

## 🎬 Exemplo passo a passo

`senate = "RDD"` (n=3), índices: R=0, D=1, D=2

filaR inicial: `[0]` · filaD inicial: `[1, 2]`

| Passo | Frente filaR | Frente filaD | Quem age primeiro (menor índice) | Ação | filaR após | filaD após |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | R (0<1) | R bane D(idx1); R volta ao fim com idx `0+3=3` | `[3]` | `[2]` |
| 2 | 3 | 2 | D (2<3) | D bane R(idx3); D volta ao fim com idx `2+3=5` | `[]` | `[5]` |

`filaR` esvaziou → Dire vence.

Resultado final: `"Dire"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) no pior caso — cada senador pode votar em até O(log n) rodadas antes de ser banido ou vencer (o número de senadores efetivamente ativos tende a cair; na prática a maioria das análises trata como O(n) amortizado, já que cada índice é enfileirado um número limitado de vezes)
- **Espaço:** O(n) — as duas filas guardam no máximo todos os índices originais

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String predictPartyVictory(String senate) {
    int n = senate.length();
    Queue<Integer> filaR = new LinkedList<>();
    Queue<Integer> filaD = new LinkedList<>();

    for (int i = 0; i < n; i++) {
        if (senate.charAt(i) == 'R') {
            filaR.offer(i);
        } else {
            filaD.offer(i);
        }
    }

    while (!filaR.isEmpty() && !filaD.isEmpty()) {
        int r = filaR.poll();
        int d = filaD.poll();
        // quem tem o índice menor age primeiro nesta rodada e bane o oponente
        if (r < d) {
            filaR.offer(r + n); // sobrevive; volta para o fim, mas só age na PRÓXIMA rodada (+n)
        } else {
            filaD.offer(d + n);
        }
        // o perdedor simplesmente não é reenfileirado: está banido
    }

    return filaR.isEmpty() ? "Dire" : "Radiant";
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

- Esquecer o `+n` ao reenfileirar o vencedor da comparação — sem esse deslocamento, o algoritmo perderia a noção de "rodada": o senador voltaria à fila com o mesmo índice relativo, e a comparação de "quem vem primeiro" pararia de refletir corretamente a ordem circular entre rodadas.
- Reenfileirar o **perdedor** por engano — o perdedor (aquele com índice maior na comparação) é banido permanentemente e nunca mais participa; só o vencedor da comparação volta para sua fila.
- Achar que basta comparar `r` e `d` sem consumir ambos da frente antes de decidir — os dois precisam ser retirados (`poll()`) das respectivas filas antes da comparação, já que ambos "gastam sua vez" nesta interação, independentemente de quem vence.
- Confundir esse problema com uma simulação baseada em pilha — apesar da categoria do repositório agrupar problemas de estrutura linear, a técnica correta aqui é **fila** (FIFO, ordem de chegada), não pilha (LIFO); tentar resolver com uma pilha não captura a semântica de "volta para o fim da fila".

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso mínimo, dois partidos | `"RD"` | `"Radiant"` | R age primeiro (índice menor) e bane D imediatamente |
| Maioria de um partido | `"RDD"` | `"Dire"` | testa múltiplas rodadas até um partido prevalecer |
| Só um partido presente | `"RRRR"` | `"Radiant"` | sem oponentes, vitória imediata sem nenhuma rodada de banimento |
| Um único senador de cada, ordem invertida | `"DR"` | `"Dire"` | testa que a ordem dos índices (não a ordem alfabética do partido) decide quem age primeiro |

## 🔗 Conexões

- Problemas irmãos: [1700] Number of Students Unable to Eat Lunch (mesma técnica de simulação com filas rotacionando), [2073] Time Needed to Buy Tickets (outra simulação de fila circular, mas resolvida com matemática direta em vez de simulação)
- No backend: simulação de eliminação competitiva em rodadas com "quem chega primeiro age primeiro" aparece em algoritmos de leader election distribuídos (ex.: Bully Algorithm), em sistemas de votação/consenso distribuído, e em escalonadores round-robin onde processos "sobreviventes" retornam ao fim da fila para a próxima rodada de execução.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
