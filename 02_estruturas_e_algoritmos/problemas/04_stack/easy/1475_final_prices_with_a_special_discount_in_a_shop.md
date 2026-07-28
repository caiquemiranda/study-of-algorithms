# [1475] Final Prices With a Special Discount in a Shop

> 🔗 [LeetCode 1475](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Array`

## 📜 O Problema

Você recebe um array de inteiros `prices`, onde `prices[i]` é o preço do `i`-ésimo item de uma loja.

Há um desconto especial: se você comprar o item `i`, receberá um desconto igual a `prices[j]`, onde `j` é o menor índice tal que `j > i` e `prices[j] <= prices[i]`. Caso não exista tal `j`, você não recebe desconto.

Retorne um array `answer` onde `answer[i]` é o preço final pago pelo item `i`, considerando o desconto.

**Exemplos:**
```
Input:  prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explicação:
- item 0 (preço 8): desconto = prices[1]=4 → paga 8-4=4
- item 1 (preço 4): desconto = prices[3]=2 → paga 4-2=2
- item 2 (preço 6): desconto = prices[3]=2 → paga 6-2=4
- itens 3 e 4: sem desconto

Input:  prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explicação: array estritamente crescente, nenhum item encontra um preço menor ou igual à direita.

Input:  prices = [10,1,1,6]
Output: [9,0,1,6]
```

**Restrições (e o que elas denunciam):**
- `1 <= prices.length <= 500` → mesmo O(n²) passaria tranquilamente, mas o padrão do problema (e a categoria) pede a solução O(n) com monotonic stack
- `1 <= prices[i] <= 1000` → valores pequenos e positivos, sem necessidade de tratar preços negativos ou zero

## 🧭 Como reconhecer o padrão

"Para cada elemento, encontrar o primeiro elemento à direita que é **menor ou igual**" é a variação em espelho do clássico "próximo maior elemento" — mesma técnica de monotonic stack, só invertendo a condição de comparação (aqui buscamos o próximo **menor-ou-igual**, não o próximo maior).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i`, varra os índices `j > i` em ordem até achar o primeiro `prices[j] <= prices[i]`; subtraia esse valor do preço de `i` (ou não subtraia nada se não encontrar).

- Tempo: O(n²) · Espaço: O(1) extra
- **Por que não basta:** para cada item, você refaz uma busca que reaproveitaria trabalho já feito por buscas anteriores. Com uma pilha monotônica, cada elemento resolve a pendência de todos os elementos maiores que ele ainda aguardando na pilha, numa única passada O(n).

## 💡 Solução 2 — A ideia otimizada (intuição)

Inicialize `answer` como uma cópia de `prices` (o preço final "sem desconto" default). Use uma pilha de **índices**, mantida de forma que os preços correspondentes fiquem crescentes de baixo para cima. Percorra o array da esquerda para a direita: enquanto o preço atual for **menor ou igual** ao preço do índice no topo da pilha, esse topo acabou de encontrar seu desconto (o preço atual) — desempilhe e subtraia o preço atual de `answer[topo]`. Depois empilhe o índice atual. Quem sobrar na pilha no final nunca encontrou desconto, e mantém o valor original em `answer`.

## 🎬 Exemplo passo a passo

`prices = [8,4,6,2,3]`

| Passo | i | prices[i] | Ação do while (compara com prices[topo]) | Pilha (índices) após | answer após |
|---|---|---|---|---|---|
| 1 | 0 | 8 | pilha vazia | `[0]` | `[8,_,_,_,_]` |
| 2 | 1 | 4 | 4 <= prices[0]=8 → pop 0, answer[0]=8-4=4 | `[1]` | `[4,4,_,_,_]` |
| 3 | 2 | 6 | 6 > prices[1]=4 → mantém | `[1,2]` | `[4,4,6,_,_]` |
| 4 | 3 | 2 | 2 <= prices[2]=6 → pop 2, answer[2]=6-2=4; 2 <= prices[1]=4 → pop 1, answer[1]=4-2=2 | `[3]` | `[4,2,4,2,_]` |
| 5 | 4 | 3 | 3 > prices[3]=2 → mantém | `[3,4]` | `[4,2,4,2,3]` |

Sobrou `[3, 4]` na pilha → nunca encontraram desconto, `answer[3]` e `answer[4]` continuam com o valor original.

Resultado final: `[4, 2, 4, 2, 3]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada índice entra e sai da pilha no máximo uma vez
- **Espaço:** O(n) — a pilha guarda no máximo todos os índices, mais o array `answer` (que é a própria saída)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] finalPrices(int[] prices) {
    int[] answer = prices.clone();       // default: sem desconto, mesmo preço original
    Deque<Integer> pilha = new ArrayDeque<>(); // guarda ÍNDICES, precisamos escrever em answer[idx]

    for (int i = 0; i < prices.length; i++) {
        // enquanto o preço atual for <= ao preço do topo, o atual é o desconto do topo
        while (!pilha.isEmpty() && prices[i] <= prices[pilha.peek()]) {
            int idx = pilha.pop();
            answer[idx] = prices[idx] - prices[i];
        }
        pilha.push(i);
    }
    // quem sobra na pilha nunca teve desconto: answer já está correto (cópia original)

    return answer;
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

- Usar a condição `prices[i] < prices[pilha.peek()]` (estritamente menor) em vez de `<=` — o enunciado é explícito que o desconto vale para preço **menor ou igual**; perder o "ou igual" faz o caso `[10,1,1,6]` calcular errado (o segundo `1` também deveria ser considerado desconto do primeiro `1`).
- Guardar **valores** na pilha em vez de **índices** — como você precisa escrever o resultado em `answer[idx]` (uma posição específica do array de saída), é necessário saber o índice, não só o valor do preço.
- Esquecer de inicializar `answer` como cópia de `prices` — sem isso, os itens que nunca encontram desconto (sobram na pilha) ficariam sem valor definido.
- Confundir a direção da monotonia: aqui a pilha deve ficar com preços **crescentes** de baixo para cima (buscamos o próximo **menor**), o oposto da busca por "próximo maior elemento".

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Array estritamente crescente | `[1,2,3,4,5]` | `[1,2,3,4,5]` | nenhum elemento encontra um menor-ou-igual à direita |
| Empates consecutivos | `[10,1,1,6]` | `[9,0,1,6]` | testa a condição `<=`: o segundo `1` desconta o primeiro `1` |
| Único elemento | `[5]` | `[5]` | sem ninguém à direita, nunca há desconto |
| Array estritamente decrescente | `[5,4,3,2,1]` | `[1,1,1,1,1]` | cada item é descontado pelo item imediatamente seguinte |

## 🔗 Conexões

- Problemas irmãos: [0496] Next Greater Element I (mesma técnica de monotonic stack, mas buscando o próximo maior em vez do próximo menor-ou-igual), [0739] Daily Temperatures (monotonic stack retornando distância em vez de diferença de valor)
- No backend: essa técnica de "para cada item, achar o próximo evento que o resolve/desconta/supera" aparece em cálculo de descontos em cascata de e-commerce, em análise de séries de preços (achar quando um ativo cai abaixo do preço atual pela primeira vez), e em qualquer processamento onde cada elemento pendente é resolvido pelo primeiro evento subsequente que satisfaz uma condição.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
