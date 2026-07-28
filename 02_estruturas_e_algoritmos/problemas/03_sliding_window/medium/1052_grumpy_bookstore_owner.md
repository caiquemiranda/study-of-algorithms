# [1052] Grumpy Bookstore Owner

> 🔗 [LeetCode 1052](https://leetcode.com/problems/grumpy-bookstore-owner/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Uma livraria fica aberta por `n` minutos. `customers[i]` é o número de clientes que entram no início do minuto `i` (e saem no fim desse minuto). `grumpy[i]` é `1` se o dono está mal-humorado nesse minuto (clientes não ficam satisfeitos) ou `0` caso contrário. O dono conhece uma técnica secreta para ficar **não mal-humorado** por `minutes` minutos consecutivos, mas só pode usá-la **uma vez**. Retorne o número **máximo** de clientes satisfeitos ao longo do dia.

**Exemplos:**
```
Input:  customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explicação: usando a técnica nos últimos 3 minutos, satisfaz 1+1+1+1+7+5=16.

Input:  customers = [1], grumpy = [0], minutes = 1
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= minutes <= n <= 2 * 10^4` → O(n²) força bruta é arriscado; O(n) é o esperado
- `0 <= customers[i] <= 1000`, `grumpy[i]` é `0` ou `1` → valores pequenos, sem risco de overflow

## 🧭 Como reconhecer o padrão

"Escolher a melhor janela de tamanho **fixo** para maximizar um ganho extra sobre uma linha de base já garantida" é janela deslizante de tamanho fixo aplicada a uma métrica derivada: separe os clientes já satisfeitos (`grumpy[i]==0`, contam sempre) do "ganho potencial" (`grumpy[i]==1`, só contam se a janela da técnica secreta cobrir esse minuto), e maximize a soma desse ganho potencial numa janela de tamanho `minutes`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição possível da técnica secreta, somar do zero todos os clientes satisfeitos considerando aquela janela ativa.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula a soma total de clientes satisfeitos a cada posição candidata, quando só a contribuição da janela muda entre posições vizinhas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Calcule `base`: a soma de `customers[i]` para todo `i` onde `grumpy[i]==0` (já satisfeitos, independente da técnica). Depois, deslize uma janela de tamanho fixo `minutes` sobre um array "extra" (`customers[i]` se `grumpy[i]==1`, senão `0`), buscando a janela de maior soma — esse é o ganho adicional que a técnica secreta proporciona. A resposta é `base + maxExtra`.

## 🎬 Exemplo passo a passo

`customers = [1,0,1,2,1,1,7,5]`, `grumpy = [0,1,0,1,0,1,0,1]`, `minutes = 3`

extra (só onde grumpy=1): `[0,0,0,2,0,1,0,5]`

| Janela (índices) | Soma extra | Melhor |
|---|---|---|
| [0..2] | 0 | 0 |
| [1..3] | 2 | 2 |
| [2..4] | 2 | 2 |
| [3..5] | 3 | 3 |
| [4..6] | 1 | 3 |
| [5..7] | 6 | 6 |

base (clientes já satisfeitos, grumpy=0): `1+1+1+7=10`

Resultado final: `10 + 6 = 16` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1) além do array de entrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
    int n = customers.length;
    int base = 0;
    for (int i = 0; i < n; i++) {
        if (grumpy[i] == 0) {
            base += customers[i];
        }
    }

    int windowExtra = 0;
    for (int i = 0; i < minutes; i++) {
        if (grumpy[i] == 1) {
            windowExtra += customers[i];
        }
    }

    int maxExtra = windowExtra;
    for (int i = minutes; i < n; i++) {
        if (grumpy[i] == 1) {
            windowExtra += customers[i];
        }
        if (grumpy[i - minutes] == 1) {
            windowExtra -= customers[i - minutes];
        }
        maxExtra = Math.max(maxExtra, windowExtra);
    }

    return base + maxExtra;
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

- Somar `customers[i]` na janela deslizante SÓ quando `grumpy[i] == 1` — os minutos em que o dono já não está bravo contribuem para o `base`, não para a "janela de ganho extra".
- A técnica secreta cobre um intervalo de tamanho FIXO `minutes` — é a mesma técnica de janela fixa de [0643] Maximum Average Subarray I, aqui maximizando em vez de tirar média.
- Esquecer de somar o `base` no resultado final — a resposta não é só o "ganho extra" da técnica secreta, é o total de clientes já satisfeitos MAIS o ganho da janela escolhida.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nunca bravo | `customers=[5]`, `grumpy=[0]`, `minutes=1` | 5 | já satisfaz todo mundo, técnica secreta não muda nada |
| minutes igual ao array inteiro | `customers=[1,2]`, `grumpy=[1,1]`, `minutes=2` | 3 | usa a técnica no período inteiro, satisfaz todos |
| Sempre bravo, técnica cobre parte | `customers=[1,1,1]`, `grumpy=[1,1,1]`, `minutes=1` | 2 | base=0, melhor janela de 1 minuto cobre o maior valor extra (1) |
| Exemplo do enunciado | `customers=[1,0,1,2,1,1,7,5]`, `grumpy=[0,1,0,1,0,1,0,1]`, `minutes=3` | 16 | base=10 + 6 (melhor janela de ganho extra, minutos 5-7) |

## 🔗 Conexões

- Problemas irmãos: [0643] Maximum Average Subarray I (mesma técnica de janela fixa deslizando com ajuste incremental), [2379] Minimum Recolors to Get K Consecutive Black Blocks (mesma ideia de isolar uma janela de tamanho fixo que maximiza/minimiza uma métrica sobre uma condição binária)
- No backend: escolher a melhor janela de tempo fixa para aplicar uma intervenção limitada (ex.: um período de cache-warming) que maximize o ganho sobre uma linha de base já garantida.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
