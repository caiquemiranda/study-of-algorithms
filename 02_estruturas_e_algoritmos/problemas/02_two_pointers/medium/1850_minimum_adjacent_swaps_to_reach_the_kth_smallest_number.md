# [1850] Minimum Adjacent Swaps to Reach the Kth Smallest Number

> 🔗 [LeetCode 1850](https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Greedy` `#Medium`

## 📜 O Problema

Dada uma string `num` (um número grande) e um inteiro `k`, um número é **maravilhoso** se é uma permutação dos dígitos de `num` e é maior que `num`. Encontre o `k`-ésimo menor número maravilhoso e retorne o número **mínimo de trocas de dígitos adjacentes** necessárias para transformar `num` nele.

**Exemplos:**
```
Input:  num = "5489355142", k = 4
Output: 2

Input:  num = "11112", k = 4
Output: 4

Input:  num = "00123", k = 1
Output: 1
Explicação: o 1º maravilhoso é "00132"; 1 troca adjacente (índices 3 e 4).
```

**Restrições (e o que elas denunciam):**
- `2 <= num.length <= 1000`, `1 <= k <= 1000` → gerar todas as permutações é inviável (fatorial); k pequeno sugere aplicar "próxima permutação" repetidamente
- Garantido que a `k`-ésima existe → não precisa tratar overflow do espaço de permutações

## 🧭 Como reconhecer o padrão

Este problema tem duas etapas, e a primeira usa dois ponteiros de forma direta: encontrar a "próxima permutação" de um número é feito localizando dois pontos de quebra por varredura (da direita pra esquerda) e depois **revertendo um sufixo** — exatamente a técnica de swap nas pontas de [0344] Reverse String, aplicada sobre o trecho que sobrou depois da troca inicial.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar TODAS as permutações do multiset de dígitos de `num`, ordená-las, e pegar a `k`-ésima maior que `num`.

- Tempo: O(n! log n!) só pra gerar e ordenar as permutações — inviável até para `n` moderado
- **Por que não basta:** o número de permutações cresce fatorialmente. O algoritmo de "próxima permutação" encontra a permutação seguinte em O(n), sem gerar nenhuma outra — repetir isso `k` vezes (`k <= 1000`) já é suficiente.

## 💡 Solução 2 — A ideia otimizada (intuição)

**Etapa 1 — achar o alvo:** aplique "próxima permutação" `k` vezes sobre `num`. Cada aplicação: (a) varra da direita pra esquerda procurando o maior índice `i` onde `dígito[i] < dígito[i+1]` (o "ponto de quebra"); (b) varra de novo da direita procurando o maior índice `j > i` com `dígito[j] > dígito[i]`; (c) troque `dígito[i]` com `dígito[j]`; (d) **reverta** o sufixo `[i+1, n-1]` com dois ponteiros nas pontas — isso transforma o sufixo (que estava decrescente) no menor arranjo possível, garantindo que essa é a MENOR permutação maior que a atual.

**Etapa 2 — contar trocas:** com o número alvo em mãos, para cada posição `i` de `num` que não bate com o alvo, procure à frente (`j > i`) o próximo dígito igual ao esperado, e "borbulhe" ele até a posição `i` com trocas adjacentes sucessivas, contando cada uma.

## 🎬 Exemplo passo a passo

`num = "00123"`, `k = 1` (uma aplicação de próxima permutação)

**Etapa 1:** `[0,0,1,2,3]` → ponto de quebra `i=3` (`2 < 3`) → maior `j>3` com dígito `> 2` é `j=4` (`3`) → troca `digito[3]` com `digito[4]`: `[0,0,1,3,2]` → reverte o sufixo `[4,4]` (um único elemento, sem mudança) → alvo = `"00132"`

**Etapa 2:** transformar `"00123"` em `"00132"`

| i | num[i] | alvo[i] | Ação | Trocas acumuladas |
|---|---|---|---|---|
| 0,1,2 | `0,0,1` | `0,0,1` | já batem, nenhuma troca | 0 |
| 3 | `2` | `3` | procura `3` à frente (encontra em j=4); borbulha até i=3 | 1 |
| 4 | `2` | `2` | já bate (depois da troca anterior) | 1 |

Resultado final: `1` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(k×n) para as `k` aplicações de próxima permutação, mais O(n²) no pior caso para contar as trocas — no total, viável dentro dos limites (`n, k <= 1000`)
- **Espaço:** O(n) para os arrays de dígitos manipulados

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int getMinSwaps(String num, int k) {
    char[] target = num.toCharArray();
    for (int t = 0; t < k; t++) {
        nextPermutation(target);
    }

    char[] arr = num.toCharArray();
    int n = arr.length;
    int swaps = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == target[i]) {
            continue;
        }
        int j = i + 1;
        while (arr[j] != target[i]) {
            j++;
        }
        // borbulha o dígito encontrado até a posição i, uma troca adjacente por vez
        while (j > i) {
            char tmp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = tmp;
            j--;
            swaps++;
        }
    }

    return swaps;
}

private void nextPermutation(char[] d) {
    int n = d.length;
    int i = n - 2;
    // acha o maior índice i onde d[i] < d[i+1] (o "ponto de quebra")
    while (i >= 0 && d[i] >= d[i + 1]) {
        i--;
    }
    if (i >= 0) {
        int j = n - 1;
        // acha o maior índice j > i com d[j] > d[i]
        while (d[j] <= d[i]) {
            j--;
        }
        char tmp = d[i];
        d[i] = d[j];
        d[j] = tmp;
    }
    // reverte o sufixo [i+1, n-1] com dois ponteiros — a mesma técnica do Reverse String
    int left = i + 1;
    int right = n - 1;
    while (left < right) {
        char tmp = d[left];
        d[left] = d[right];
        d[right] = tmp;
        left++;
        right--;
    }
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

- Esquecer o passo de REVERTER o sufixo depois da troca — sem reverter, o sufixo continua na ordem decrescente original, o que NÃO é a menor permutação possível para aquele prefixo; a reversão é o que garante o menor arranjo.
- Aplicar "próxima permutação" sobre o `num` original em vez de sobre uma cópia — o `num` original ainda é necessário na Etapa 2 como ponto de partida para contar as trocas.
- Contar as trocas de forma errada ao "borbulhar" o dígito — cada troca adjacente move o dígito encontrado em `j` apenas UMA posição por vez; o total de trocas para trazê-lo até `i` é exatamente `j - i`, não `1`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Múltiplas trocas | `num="5489355142"`, `k=4` | 2 | 4 aplicações de próxima permutação, depois 2 trocas pra alcançar o alvo |
| Muitos dígitos repetidos | `num="11112"`, `k=4` | 4 | o `2` precisa "subir" 4 posições através dos `1`s |
| Caso mínimo | `num="00123"`, `k=1` | 1 | uma única troca adjacente resolve |
| k grande | `num` com muitas permutações possíveis, `k` no limite | (varia) | testa que aplicar "próxima permutação" repetidamente não degrada em tempo |

## 🔗 Conexões

- Problemas irmãos: [0031] Next Permutation (a etapa 1 deste problema, isolada), [0344] Reverse String (a técnica de reversão usada dentro da próxima permutação)
- No backend: gerar a `k`-ésima configuração seguinte de um conjunto de parâmetros em ordem lexicográfica sem enumerar todas as anteriores (ex.: avançar por combinações de teste em ordem determinística), e medir o "custo de transição" entre duas configurações via trocas adjacentes.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
