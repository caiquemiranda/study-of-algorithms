# [0904] Fruit Into Baskets

> 🔗 [LeetCode 904](https://leetcode.com/problems/fruit-into-baskets/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Você visita uma fazenda com árvores frutíferas em fila, representadas por um array `fruits`, onde `fruits[i]` é o tipo de fruta da árvore `i`. Você tem só **duas** cestas, cada uma podendo guardar **um único tipo** de fruta (sem limite de quantidade). Começando de qualquer árvore, você deve colher exatamente uma fruta de cada árvore, movendo-se para a direita, até encontrar uma árvore cuja fruta não caiba em nenhuma cesta. Retorne o **máximo** de frutas que você pode colher.

**Exemplos:**
```
Input:  fruits = [1,2,1]
Output: 3
Explicação: dá pra colher das 3 árvores.

Input:  fruits = [0,1,2,2]
Output: 3
Explicação: dá pra colher de [1,2,2].

Input:  fruits = [1,2,3,2,2]
Output: 4
Explicação: dá pra colher de [2,3,2,2].
```

**Restrições (e o que elas denunciam):**
- `1 <= fruits.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `0 <= fruits[i] < fruits.length` → os tipos de fruta cabem num intervalo conhecido, mas um `HashMap` funciona igualmente bem sem precisar dessa garantia

## 🧭 Como reconhecer o padrão

"Maior subarray contíguo com no máximo 2 tipos distintos" é o padrão clássico de "no máximo k distintos": expande-se a janela pela direita; quando o número de tipos distintos passa de 2, encolhe-se pela esquerda até voltar a ter só 2.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada início possível, avançar enquanto o número de tipos distintos de fruta coletados for `<= 2`, contando do zero a cada nova posição inicial.

- Tempo: O(n²) · Espaço: O(1) por tentativa
- **Por que não basta:** reinicia a contagem de tipos distintos do zero a cada início candidato, sem aproveitar o trabalho já feito em janelas vizinhas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um mapa `basket` com a contagem de cada tipo de fruta na janela atual. Expanda `right`, incrementando a contagem do tipo incluído. Enquanto `basket.size() > 2`, encolha `left` (decrementando e removendo do mapa quando a contagem chega a zero). A cada passo válido, atualize o maior comprimento visto.

## 🎬 Exemplo passo a passo

`fruits = [1,2,3,2,2]`

| right | fruta | mapa após incluir | distinct | Encolhe? | left final | comprimento | melhor |
|---|---|---|---|---|---|---|---|
| 0 | 1 | {1:1} | 1 | não | 0 | 1 | 1 |
| 1 | 2 | {1:1,2:1} | 2 | não | 0 | 2 | 2 |
| 2 | 3 | {1:1,2:1,3:1} | 3 | sim: remove fruits[0]=1 | 1 | 2 | 2 |
| 3 | 2 | {2:2,3:1} | 2 | não | 1 | 3 | 3 |
| 4 | 2 | {2:3,3:1} | 2 | não | 1 | 4 | 4 |

Resultado final: `4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1) — o mapa nunca guarda mais que 3 chaves a qualquer momento

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int totalFruit(int[] fruits) {
    Map<Integer, Integer> basket = new HashMap<>();
    int left = 0;
    int best = 0;

    for (int right = 0; right < fruits.length; right++) {
        basket.merge(fruits[right], 1, Integer::sum);

        while (basket.size() > 2) {
            int leftType = fruits[left];
            int updated = basket.merge(leftType, -1, Integer::sum);
            if (updated == 0) {
                basket.remove(leftType);
            }
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
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

- "Dois tipos de fruta" é literalmente "no máximo 2 chaves distintas no mapa" — o mesmo padrão de [3090] Maximum Length Substring With Two Occurrences, mas limitando TIPOS distintos em vez de OCORRÊNCIAS de cada tipo.
- Remover a chave do mapa quando a contagem chega a zero é essencial — deixá-la com valor 0 faria `basket.size()` contar um tipo que não está mais na janela.
- A resposta é sobre "árvores consecutivas a partir de qualquer início", ou seja, um subarray contíguo — não é permitido pular árvores no meio do caminho.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só um tipo de fruta | `[1,1,1,1]` | 4 | um único tipo sempre cabe nas 2 cestas |
| Exatamente dois tipos | `[1,2,1]` | 3 | array inteiro já respeita o limite de 2 tipos |
| Terceiro tipo força encolhimento | `[0,1,2,2]` | 3 | melhor janela é [1,2,2], descartando a árvore 0 |
| Exemplo maior do enunciado | `[1,2,3,2,2]` | 4 | melhor janela é [2,3,2,2], descartando a primeira árvore |

## 🔗 Conexões

- Problemas irmãos: [3090] Maximum Length Substring With Two Occurrences (mesmíssima técnica, mas limitando ocorrências por caractere em vez de tipos distintos), [0159] Longest Substring with At Most Two Distinct Characters (o mesmo problema, praticamente idêntico, aplicado a strings em vez de árvores)
- No backend: alocar um buffer limitado a `k` categorias distintas simultâneas (ex.: no máximo 2 conexões de protocolos diferentes abertas ao mesmo tempo) e encontrar a maior sequência de itens processáveis sem violar esse limite.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
