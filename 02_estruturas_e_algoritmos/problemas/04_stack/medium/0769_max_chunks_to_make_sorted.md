# [0769] Max Chunks To Make Sorted

> 🔗 [LeetCode 769](https://leetcode.com/problems/max-chunks-to-make-sorted/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Greedy`

## 📜 O Problema

Você recebe um array `arr` de tamanho `n` que é uma permutação dos inteiros `[0, n-1]`. Divida `arr` em algumas partes (chunks), ordene cada parte individualmente, e concatene-as — o resultado deve ser igual ao array totalmente ordenado. Retorne o **maior número de partes** possível que ainda garante esse resultado.

**Exemplos:**
```
Input:  arr = [4,3,2,1,0]
Output: 1
Explicação: dividir em duas ou mais partes não produz o array ordenado (ex.: [4,3],[2,1,0] vira [3,4,0,1,2]).

Input:  arr = [1,0,2,3,4]
Output: 4
Explicação: dividir em [1,0],[2],[3],[4] funciona — o máximo de partes possível.
```

**Restrições (e o que elas denunciam):**
- `n == arr.length`, `1 <= n <= 10` → tamanho minúsculo, qualquer solução O(n) ou até O(n²) é folgada; o desafio é a lógica, não performance
- `0 <= arr[i] < n`, elementos únicos → é garantidamente uma permutação de `[0, n-1]`, uma propriedade essencial: significa que o array ordenado é simplesmente `[0,1,...,n-1]`, o que permite comparar posição com valor diretamente

## 🧭 Como reconhecer o padrão

"Encontrar o maior número de partições tal que cada uma, ordenada isoladamente, ainda produza o array global ordenado" tem uma observação chave: como `arr` é uma permutação de `[0,n-1]`, um chunk terminando no índice `i` é válido se e somente se o **conjunto de valores** de `0` até `i` for exatamente `{arr[0], ..., arr[i]}` — ou seja, se o **máximo** dos valores vistos até `i` for igual a `i`. Rastrear esse "máximo do chunk atual" e decidir quando ele "fecha" (bate com a posição) é naturalmente modelado com uma pilha que guarda o máximo de cada chunk formado, mesclando chunks anteriores sempre que um valor baixo aparece e ainda pertence a um chunk já aberto.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todas as formas possíveis de particionar o array em partes contíguas, ordenar cada parte, concatenar, e verificar se o resultado é o array ordenado — escolhendo a partição com mais partes que funciona.

- Tempo: exponencial (2^(n-1) partições possíveis) · Espaço: exponencial
- **Por que não basta:** mesmo com `n<=10`, testar todas as 2^9=512 partições e ordenar cada uma é um desperdício de trabalho quando existe uma regra direta (baseada na propriedade de permutação) que decide o particionamento ótimo em uma única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `arr` mantendo uma pilha onde cada elemento representa o **valor máximo de um chunk já fechado**. Para cada novo valor `num`: se ele for maior ou igual ao topo da pilha (ou a pilha estiver vazia), ele começa um novo chunk — empilhe `num` como o máximo desse novo chunk. Caso contrário (`num` é menor que o topo), ele **pertence** ao chunk anterior (não pode formar um chunk isolado, porque um valor menor apareceu depois de um maior) — mescle todos os chunks cujo máximo é maior que `num` num único chunk, mantendo o **maior** valor entre eles como o novo topo (o valor mínimo `num` em si não determina o máximo do chunk mesclado; o máximo anterior continua sendo o teto). Ao final, o **tamanho da pilha** é o número de chunks.

## 🎬 Exemplo passo a passo

`arr = [1,0,2,3,4]`

| Passo | num | Ação | Pilha após (máximos de cada chunk) |
|---|---|---|---|
| 1 | 1 | pilha vazia → novo chunk | `[1]` |
| 2 | 0 | `0 < 1` (topo) → mescla: desempilha `1`, nada mais a desempilhar, reempilha o máximo `1` | `[1]` |
| 3 | 2 | `2 >= 1` (topo) → novo chunk | `[1, 2]` |
| 4 | 3 | `3 >= 2` (topo) → novo chunk | `[1, 2, 3]` |
| 5 | 4 | `4 >= 3` (topo) → novo chunk | `[1, 2, 3, 4]` |

A pilha final tem 4 elementos, representando os chunks `[1,0]` (máx 1), `[2]`, `[3]`, `[4]`.

Resultado final: `4` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada elemento é empilhado e desempilhado no máximo uma vez
- **Espaço:** O(n) — pior caso, array já ordenado, cada elemento forma seu próprio chunk

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxChunksToSorted(int[] arr) {
    Deque<Integer> pilha = new ArrayDeque<>(); // máximo de cada chunk já "fechado"

    for (int num : arr) {
        if (!pilha.isEmpty() && pilha.peek() > num) {
            // num pertence ao chunk anterior: mescla todos os chunks maiores que ele
            int maximoDoChunk = pilha.pop();
            while (!pilha.isEmpty() && pilha.peek() > num) {
                pilha.pop();
            }
            pilha.push(maximoDoChunk); // o teto do chunk mesclado continua sendo o maior valor visto
        } else {
            pilha.push(num); // num inicia um novo chunk independente
        }
    }

    return pilha.size(); // cada elemento restante representa um chunk válido
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

- Empilhar `num` (o valor mínimo que causou a mescla) em vez do **máximo** anterior — o valor que representa o teto do chunk mesclado precisa continuar sendo o maior valor já visto naquele chunk, não o valor baixo que disparou a mescla.
- Esquecer que essa técnica depende de `arr` ser uma **permutação exata** de `[0, n-1]` — a lógica de "máximo == posição final do chunk" só funciona porque não há gaps nem repetições nos valores; ela não generaliza diretamente para arrays arbitrários.
- Confundir esta técnica com uma solução mais simples que também resolve o problema: rastrear o **máximo corrido** da esquerda para a direita e contar quantas vezes `maximoCorrido == índice` — essa alternativa é O(n) e O(1) de espaço, sem pilha nenhuma; a versão com pilha aqui foi escolhida por consistência com a categoria, mas ambas são válidas e vale saber que a mais simples existe.
- Usar `>=` em vez de `>` na condição de mesclagem — valores **iguais** ao topo nunca ocorrem aqui (é uma permutação sem repetição), mas a comparação correta lógica é sempre "estritamente maior" para decidir mesclagem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já ordenado | `[0,1,2,3,4]` | 5 | cada elemento é seu próprio chunk, nenhuma mescla necessária |
| Totalmente invertido | `[4,3,2,1,0]` | 1 | só um chunk gigante funciona, qualquer divisão quebra a ordenação |
| Mescla parcial no início | `[1,0,2,3,4]` | 4 | testa a mescla de exatamente dois elementos, resto seguem independentes |
| Array de um único elemento | `[0]` | 1 | caso trivial, sempre um único chunk |

## 🔗 Conexões

- Problemas irmãos: [0581] Shortest Unsorted Continuous Subarray (mesma família de "identificar regiões que precisam ser tratadas em conjunto para alcançar ordenação"), [0768] Max Chunks To Make Sorted II (mesmo problema, mas sem a garantia de que `arr` é uma permutação, exigindo comparação com uma cópia ordenada)
- No backend: essa lógica de "particionar dados em blocos independentes que podem ser processados/ordenados isoladamente sem afetar o resultado global" aparece em otimização de merge sort externo (dividir arquivos grandes em blocos ordenáveis independentemente) e em paralelização de processamento de dados particionados por chave, onde é importante saber o maior número de partições seguras.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
