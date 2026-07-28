# [2260] Minimum Consecutive Cards to Pick Up

> 🔗 [LeetCode 2260](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dado um array de inteiros `cards` onde `cards[i]` representa o valor da `i`-ésima carta. Um par de cartas é **matching** se as cartas têm o mesmo valor. Retorne o número **mínimo** de cartas **consecutivas** que você precisa pegar para ter um par matching entre as cartas pegas. Se for impossível, retorne `-1`.

**Exemplos:**
```
Input:  cards = [3,4,2,3,4,7]
Output: 4
Explicação: pegar [3,4,2,3] contém um par matching de valor 3.

Input:  cards = [1,0,5,3]
Output: -1
```

**Restrições (e o que elas denunciam):**
- `1 <= cards.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `0 <= cards[i] <= 10^6` → intervalo grande de valores, exigindo hashmap em vez de array de contagem indexado

## 🧭 Como reconhecer o padrão

"Menor trecho contíguo contendo uma duplicata" não precisa de dois ponteiros explícitos: basta rastrear a **última posição vista** de cada valor. Ao encontrar o mesmo valor de novo, a distância entre a ocorrência atual e a última é uma janela candidata — o mesmo princípio de [0219] Contains Duplicate II, mas aqui minimizando a distância em vez de compará-la a um limite fixo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(i,j)` com `i<j` e `cards[i]==cards[j]`, calcular `j-i+1` e manter o menor.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** testa todos os pares possíveis do mesmo valor, quando só o par mais PRÓXIMO de cada valor pode ser candidato à resposta mínima.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um mapa `lastSeen` com a última posição de cada valor. Ao processar `cards[i]`: se `cards[i]` já foi visto, a janela `i - lastSeen[cards[i]] + 1` é candidata — atualize o mínimo. Sempre atualize `lastSeen[cards[i]] = i` (a ocorrência mais recente é a que importa para a próxima comparação).

## 🎬 Exemplo passo a passo

`cards = [3,4,2,3,4,7]`

| i | cards[i] | Visto antes (índice)? | Janela candidata | Melhor |
|---|---|---|---|---|
| 0 | 3 | não | — | ∞ |
| 1 | 4 | não | — | ∞ |
| 2 | 2 | não | — | ∞ |
| 3 | 3 | sim (índice 0) | 3-0+1=4 | 4 |
| 4 | 4 | sim (índice 1) | 4-1+1=4 | 4 |
| 5 | 7 | não | — | 4 |

Resultado final: `4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n) para o mapa

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minimumCardPickup(int[] cards) {
    Map<Integer, Integer> lastSeen = new HashMap<>();
    int best = Integer.MAX_VALUE;

    for (int i = 0; i < cards.length; i++) {
        if (lastSeen.containsKey(cards[i])) {
            best = Math.min(best, i - lastSeen.get(cards[i]) + 1);
        }
        lastSeen.put(cards[i], i);
    }

    return best == Integer.MAX_VALUE ? -1 : best;
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

- Não é preciso manter uma janela deslizante explícita com dois ponteiros — como qualquer par forma uma janela válida, basta comparar cada índice atual com a ÚLTIMA ocorrência do mesmo valor, que já garante a menor distância possível para aquele valor.
- Atualizar `lastSeen` para o índice ATUAL após cada checagem (mesmo quando já havia sido visto) é essencial — isso garante que a próxima repetição do mesmo valor meça a distância a partir da ocorrência mais RECENTE, não da primeira.
- Se nenhum valor se repete em todo o array, a resposta é `-1` — nunca existe um par de cartas iguais para formar uma janela.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhuma repetição | `[1,0,5,3]` | -1 | todos os valores são únicos |
| Repetição adjacente | `[1,1]` | 2 | par mais próximo possível |
| Múltiplas repetições, escolhe a mais próxima | `[1,2,1,2,1]` | 3 | pares (1,1) e (2,2) mais próximos têm distância 3 cada |
| Exemplo do enunciado | `[3,4,2,3,4,7]` | 4 | par de 3's (índices 0,3) ou par de 4's (índices 1,4), ambos com janela 4 |

## 🔗 Conexões

- Problemas irmãos: [0219] Contains Duplicate II (mesma técnica-base de rastrear a última ocorrência de cada valor, aqui minimizando a distância em vez de checar contra um limite fixo), [1004] Max Consecutive Ones III (mesma família de raciocínio sobre janelas, embora com objetivo bem diferente)
- No backend: encontrar o menor lote de registros consecutivos de um log que já contém uma duplicata de algum identificador, útil para detectar rapidamente o menor "buffer" necessário antes de garantir colisão.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
