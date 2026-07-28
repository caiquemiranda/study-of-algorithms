# [3318] Find X-Sum of All K-Long Subarrays I

> 🔗 [LeetCode 3318](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Easy`

## 📜 O Problema

Dado um array `nums` de `n` inteiros e dois inteiros `k` e `x`, a **x-sum** de um array é calculada assim: conte as ocorrências de cada elemento; mantenha só as ocorrências dos `x` elementos mais frequentes (em empate, o de **maior valor** é considerado mais frequente); some o array resultante. Se o array tiver menos de `x` elementos distintos, a x-sum é a soma do array inteiro. Retorne um array `answer` de tamanho `n - k + 1` onde `answer[i]` é a x-sum do subarray `nums[i..i+k-1]`.

**Exemplos:**
```
Input:  nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6,10,12]
Explicação:
- [1,1,2,2,3,4]: top 2 frequências são 1(freq2) e 2(freq2) → 1+1+2+2 = 6
- [1,2,2,3,4,2]: top 2 são 2(freq3) e 4(freq1, desempate por valor) → 2+2+2+4 = 10
- [2,2,3,4,2,3]: top 2 são 2(freq3) e 3(freq2) → 2+2+2+3+3 = 12

Input:  nums = [3,8,7,8,7,5], k = 2, x = 2
Output: [11,15,15,15,12]
Explicação: como k == x, a x-sum é sempre a soma da janela inteira.
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 50`, `1 <= nums[i] <= 50`, `1 <= x <= k <= nums.length` → entrada pequena; qualquer abordagem O(n·k log k) é rápida o suficiente
- Desempate por "valor maior" → a comparação de frequências precisa de um segundo critério, não pode ordenar só por contagem

## 🧭 Como reconhecer o padrão

"Agregação sobre janela de tamanho **fixo** `k`" é sliding window fixo: mantém-se um mapa de frequências que é atualizado incrementalmente (soma o que entra, subtrai o que sai) enquanto a janela desliza, evitando reconstruir a contagem inteira a cada passo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada janela, reconstruir o mapa de frequência do zero percorrendo todos os `k` elementos, depois ordenar as entradas e somar as top `x`.

- Tempo: O(n · k log k) · Espaço: O(k) por janela
- **Por que não basta:** descarta o mapa da janela anterior e reconta tudo, mesmo que `k-1` dos `k` elementos sejam os mesmos da janela anterior — só um elemento sai e um entra a cada deslizamento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um único mapa de frequência ao longo de toda a varredura. Ao deslizar a janela, incremente a contagem do elemento que entra e decremente a do que sai (removendo a chave se a contagem chegar a zero). A cada posição, ordene as entradas do mapa por frequência decrescente (desempatando por valor decrescente) e some as `x` primeiras — se houver menos de `x` valores distintos, a soma automaticamente cobre a janela inteira.

## 🎬 Exemplo passo a passo

`nums = [1,1,2,2,3,4,2,3]`, `k = 6`, `x = 2`

| Janela | Sai | Entra | Frequências (valor:freq) | Top x=2 (freq desc, valor desc) | x-sum |
|---|---|---|---|---|---|
| [0..5] inicial | — | — | 1:2, 2:2, 3:1, 4:1 | 2(freq2), 1(freq2) | 2·2+1·2=6 |
| [1..6] | nums[0]=1 | nums[6]=2 | 1:1, 2:3, 3:1, 4:1 | 2(freq3), 4(freq1) | 2·3+4·1=10 |
| [2..7] | nums[1]=1 | nums[7]=3 | 2:3, 3:2, 4:1 | 2(freq3), 3(freq2) | 2·3+3·2=12 |

Resultado final: `[6,10,12]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n · d log d), onde `d` é o número de valores distintos na janela (`d <= k`) — dominado por ordenar as frequências a cada uma das `n-k+1` janelas
- **Espaço:** O(k) para o mapa de frequência e a lista de entradas por janela

## 💻 Implementações

### Java (referência completa e comentada)
```java
public long[] findXSum(int[] nums, int k, int x) {
    int n = nums.length;
    long[] answer = new long[n - k + 1];
    Map<Integer, Integer> freq = new HashMap<>();

    for (int i = 0; i < k; i++) {
        freq.merge(nums[i], 1, Integer::sum);
    }
    answer[0] = topXSum(freq, x);

    for (int right = k; right < n; right++) {
        int left = right - k;
        addToFreq(freq, nums[right], 1);
        addToFreq(freq, nums[left], -1); // remove o elemento que saiu da janela
        answer[right - k + 1] = topXSum(freq, x);
    }

    return answer;
}

private void addToFreq(Map<Integer, Integer> freq, int value, int delta) {
    int updated = freq.merge(value, delta, Integer::sum);
    if (updated == 0) {
        freq.remove(value); // não deixa "lixo" de contagem zero no mapa
    }
}

private long topXSum(Map<Integer, Integer> freq, int x) {
    List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(freq.entrySet());
    // ordena por frequência decrescente; em empate, valor maior primeiro
    entries.sort((a, b) -> {
        if (!a.getValue().equals(b.getValue())) {
            return b.getValue() - a.getValue();
        }
        return b.getKey() - a.getKey();
    });

    long sum = 0;
    for (int i = 0; i < Math.min(x, entries.size()); i++) {
        Map.Entry<Integer, Integer> entry = entries.get(i);
        sum += (long) entry.getKey() * entry.getValue();
    }
    return sum;
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

- Empate na frequência deve ser resolvido pelo **valor maior**, não pela ordem de inserção no mapa — esquecer o critério de desempate produz somas erradas em janelas com frequências repetidas.
- Quando a janela tem menos de `x` valores distintos, a x-sum é a soma de TODOS os elementos — mas isso já acontece naturalmente ao pegar `min(x, distinct.size())` entradas, sem precisar de um caso especial.
- Deixar entradas com contagem zero no mapa depois de remover um elemento que saiu da janela — isso polui a lista de candidatos com um valor "fantasma" que não deveria mais existir.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k igual a x | `nums=[3,8,7,8,7,5]`, `k=2`, `x=2` | [11,15,15,15,12] | com k==x, a x-sum é sempre a soma da janela inteira |
| Menos de x valores distintos numa janela | `nums=[1,1,1,1]`, `k=2`, `x=3` | [2,2,2] | só existe 1 valor distinto na janela, a soma total é usada |
| Empate de frequência resolvido por valor | `nums=[1,1,2,2,3,4,2,3]`, `k=6`, `x=2` | [6,10,12] | exemplo do enunciado, mostra o desempate por valor maior |
| Janela de tamanho 1 (k=x=1) | `nums=[5,3,9]`, `k=1`, `x=1` | [5,3,9] | cada janela tem um único elemento, que é sempre o "top 1" |

## 🔗 Conexões

- Problemas irmãos: [0480] Sliding Window Median (mesma família de manter uma estrutura agregada — aqui frequências, lá mediana — enquanto uma janela de tamanho fixo desliza), [0347] Top K Frequent Elements (mesma técnica de ranquear por frequência com desempate, aplicada a uma janela em vez do array inteiro)
- No backend: calcular métricas agregadas sobre os itens mais frequentes dentro de uma janela deslizante de eventos — por exemplo, os produtos mais vendidos nas últimas `k` transações de um fluxo de vendas em tempo real.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
