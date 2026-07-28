# [0735] Asteroid Collision

> 🔗 [LeetCode 735](https://leetcode.com/problems/asteroid-collision/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Array` `#Simulation`

## 📜 O Problema

Você recebe um array `asteroids` representando asteroides numa linha, onde o índice representa a posição relativa. O valor absoluto é o tamanho, e o sinal é a direção (positivo = direita, negativo = esquerda). Todos se movem na mesma velocidade.

Quando dois asteroides colidem, o menor explode; se forem do mesmo tamanho, ambos explodem. Dois asteroides movendo na mesma direção nunca colidem. Retorne o estado final dos asteroides após todas as colisões.

**Exemplos:**
```
Input:  asteroids = [5,10,-5]
Output: [5,10]
Explicação: 10 e -5 colidem, resultando em 10 (maior sobrevive). 5 e 10 nunca colidem (mesma direção).

Input:  asteroids = [8,-8]
Output: []
Explicação: tamanhos iguais, ambos explodem.

Input:  asteroids = [10,2,-5]
Output: [10]
Explicação: 2 e -5 colidem, resultando em -5 (maior). 10 e -5 colidem, resultando em 10.
```

**Restrições (e o que elas denunciam):**
- `2 <= asteroids.length <= 10^4` → precisa de solução O(n); simular colisões par a par ingenuamente seria arriscado
- `-1000 <= asteroids[i] <= 1000`, `asteroids[i] != 0` → tamanhos sempre não-nulos, simplifica a lógica de comparação (nunca há empate por "tamanho zero")

## 🧭 Como reconhecer o padrão

"Simular colisões sequenciais onde só o elemento mais recente (à esquerda, ainda vivo) pode colidir com o próximo" é a assinatura de stack: um asteroide indo para a direita só é ameaçado por um asteroide futuro indo para a esquerda, e a colisão relevante é sempre entre o **mais recente sobrevivente** (topo da pilha) e o **próximo a chegar** — exatamente como uma pilha de "sobreviventes até agora" funciona.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular repetidamente uma varredura completa do array procurando um par adjacente `[positivo, negativo]` (indicando colisão iminente), resolvê-lo, e reiniciar a varredura até não haver mais colisões possíveis.

- Tempo: O(n²) pior caso · Espaço: O(n)
- **Por que não basta:** cada colisão resolvida pode expor uma nova colisão em cascata (como no exemplo `[10,2,-5]`, onde resolver `2` vs `-5` expõe uma nova colisão entre `10` e o resultado), forçando uma nova varredura completa a cada resolução. Uma pilha resolve tudo numa única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `asteroids` da esquerda para a direita com uma pilha representando os sobreviventes até agora. Para cada asteroide: se ele for **positivo**, ou se a pilha estiver vazia, ou se o topo for **negativo** (mesma direção relativa, nunca colidem), simplesmente empilhe. Se o asteroide atual for **negativo** e o topo da pilha for **positivo**, há colisão: compare os tamanhos em um laço — enquanto o topo (positivo, menor) for menor que o asteroide atual, desempilhe-o (ele explode) e continue verificando o novo topo; se os tamanhos forem iguais, ambos explodem (desempilhe o topo e descarte o atual); se o topo for maior, o asteroide atual explode (não é empilhado). Esse laço captura naturalmente o efeito cascata.

## 🎬 Exemplo passo a passo

`asteroids = [3,5,-6,2,-1,4]`

| Passo | Asteroide | Ação (compara com topo, resolve colisão) | Pilha após |
|---|---|---|---|
| 1 | 3 | positivo → empilha | `[3]` |
| 2 | 5 | positivo → empilha | `[3, 5]` |
| 3 | -6 | topo `5` (positivo, menor) → explode, pop; topo `3` (positivo, menor) → explode, pop; pilha vazia → `-6` sobrevive, empilha | `[-6]` |
| 4 | 2 | topo `-6` é negativo (mesma direção que... não, 2 é positivo e topo negativo: sem colisão, direções opostas mas -6 já passou) → empilha direto | `[-6, 2]` |
| 5 | -1 | topo `2` (positivo, MAIOR que 1) → `-1` explode, não empilha | `[-6, 2]` |
| 6 | 4 | topo `2` é positivo, mas asteroide atual (4) também é positivo → mesma direção, sem colisão, empilha | `[-6, 2, 4]` |

Resultado final: `[-6, 2, 4]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada asteroide é empilhado e desempilhado no máximo uma vez, mesmo considerando o efeito cascata
- **Espaço:** O(n) — pilha, pior caso nenhuma colisão ocorre (todos sobrevivem)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] asteroidCollision(int[] asteroids) {
    Deque<Integer> pilha = new ArrayDeque<>();

    for (int ast : asteroids) {
        boolean vivo = true;
        // só há colisão quando o atual vai para a ESQUERDA e o topo vai para a DIREITA
        while (vivo && ast < 0 && !pilha.isEmpty() && pilha.peek() > 0) {
            if (pilha.peek() < -ast) {
                pilha.pop();          // topo (menor) explode, atual continua verificando o próximo topo
            } else if (pilha.peek() == -ast) {
                pilha.pop();          // tamanhos iguais: ambos explodem
                vivo = false;
            } else {
                vivo = false;          // topo é maior: o atual explode
            }
        }
        if (vivo) {
            pilha.push(ast);
        }
    }

    // reconstrói na ordem correta (pilha guarda de baixo pra cima o resultado)
    int[] resultado = new int[pilha.size()];
    for (int i = resultado.length - 1; i >= 0; i--) {
        resultado[i] = pilha.pop();
    }
    return resultado;
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

- Esquecer a condição completa de colisão — só há colisão quando o asteroide atual é **negativo** (vai para a esquerda) **e** o topo da pilha é **positivo** (vai para a direita); qualquer outra combinação de sinais significa que eles nunca vão se encontrar (mesma direção, ou já se afastando).
- Tratar o caso de tamanhos iguais incorretamente — quando `|topo| == |atual|`, **ambos** explodem: o topo deve ser desempilhado, e o asteroide atual não deve ser empilhado; esquecer de desempilhar o topo (ou empilhar o atual por engano) quebra o resultado.
- Sair do laço de colisão cedo demais — o `while` precisa continuar verificando o **novo** topo após cada explosão, porque o efeito cascata pode envolver múltiplos asteroides empilhados anteriormente (como no exemplo, onde `-6` destrói tanto `5` quanto `3`).
- Empilhar o asteroide atual antes de resolver todas as colisões pendentes — a ordem correta é: resolver o laço de colisões primeiro, e só empilhar no final se o asteroide atual sobreviveu (`vivo == true`).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Mesma direção, nunca colidem | `[5,10]` | `[5,10]` | ambos positivos, sem interação |
| Tamanhos iguais se destroem mutuamente | `[8,-8]` | `[]` | testa o caso de empate exato |
| Efeito cascata (um destrói vários) | `[10,2,-5]` | `[10]` | um asteroide grande sobrevive a múltiplas colisões em sequência |
| Colisão isolada seguida de sobrevivente independente | `[3,5,-6,2,-1,4]` | `[-6,2,4]` | combina cascata, colisão simples e sobrevivência sem interação, tudo no mesmo array |

## 🔗 Conexões

- Problemas irmãos: [0682] Baseball Game (mesma ideia de simular estado sequencial com pilha, decisões dependem só do topo), [0402] Remove K Digits (outra pilha resolvendo comparações em cascata entre o topo e o elemento atual)
- No backend: simulação de "o mais recente pode ser invalidado pelo próximo evento oposto, em cascata" aparece em motores de matching de ordens de compra/venda (order matching engines em bolsas de valores, onde ordens de compra e venda "colidem" e se cancelam por tamanho), e em sistemas de resolução de conflitos onde eventos concorrentes se anulam mutuamente conforme chegam.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
