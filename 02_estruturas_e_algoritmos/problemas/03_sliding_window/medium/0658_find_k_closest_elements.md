# [0658] Find K Closest Elements

> 🔗 [LeetCode 658](https://leetcode.com/problems/find-k-closest-elements/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#TwoPointers` `#Medium`

## 📜 O Problema

Dado um array de inteiros **ordenado** `arr`, e dois inteiros `k` e `x`, retorne os `k` inteiros mais próximos de `x` no array. O resultado deve estar ordenado em ordem crescente. Um inteiro `a` é mais próximo de `x` que `b` se `|a-x| < |b-x|`, ou se `|a-x| == |b-x|` e `a < b`.

**Exemplos:**
```
Input:  arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input:  arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
```

**Restrições (e o que elas denunciam):**
- `arr` está ordenado em ordem crescente → propriedade essencial que permite encolher a busca a partir das duas pontas
- `1 <= k <= arr.length <= 10^4` → O(n log n) reordenando por distância é aceitável, mas O(n-k) encolhendo direto é ainda mais simples e eficiente

## 🧭 Como reconhecer o padrão

"Os `k` elementos mais próximos de um valor, num array **já ordenado**" é resolvido encolhendo uma janela de tamanho `n` até `k`: como o array está ordenado, os candidatos menos úteis estão sempre numa das duas pontas — remove-se a ponta mais distante de `x` repetidamente até sobrarem exatamente `k` elementos.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Calcular `|arr[i] - x|` para todo elemento, ordenar por essa distância (com desempate por valor) e pegar os `k` primeiros, depois reordenar o resultado.

- Tempo: O(n log n) · Espaço: O(n)
- **Por que não basta:** não aproveita que `arr` já está ordenado — reordenar tudo do zero ignora a estrutura que permitiria resolver com uma simples varredura das pontas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Comece com `left=0` e `right=n-1` (a janela inteira). Enquanto o tamanho da janela for maior que `k`, compare qual ponta está mais distante de `x`: se `x - arr[left] <= arr[right] - x`, o elemento da esquerda é igual ou mais próximo — descarte o da direita (`right--`); senão, descarte o da esquerda (`left++`). Ao final, `arr[left..right]` é a resposta.

## 🎬 Exemplo passo a passo

`arr = [1,2,3,4,5]`, `k = 4`, `x = 3`

| Passo | left,right (valores) | x-arr[left] | arr[right]-x | Ação |
|---|---|---|---|---|
| inicial | 0(1), 4(5) | 3-1=2 | 5-3=2 | empate → remove da direita (right--) |
| fim | 0(1), 3(4) | — | — | tamanho=4=k, para |

Resultado final: `[1,2,3,4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n-k) — cada passo do encolhimento é O(1), até `n-k` remoções
- **Espaço:** O(1) além da saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> findClosestElements(int[] arr, int k, int x) {
    int left = 0;
    int right = arr.length - 1;

    while (right - left + 1 > k) {
        if (x - arr[left] <= arr[right] - x) {
            right--; // elemento da esquerda é igual ou mais próximo; descarta o da direita
        } else {
            left++; // elemento da direita é estritamente mais próximo; descarta o da esquerda
        }
    }

    List<Integer> result = new ArrayList<>();
    for (int i = left; i <= right; i++) {
        result.add(arr[i]);
    }
    return result;
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

- No empate (`x - arr[left] == arr[right] - x`), a regra é sempre preferir o menor valor — por isso remove-se da DIREITA (mantendo o elemento mais à esquerda, que é o menor em caso de empate), nunca o contrário.
- Comparar `Math.abs(arr[left]-x)` e `Math.abs(arr[right]-x)` diretamente funciona, mas como o array está ordenado e a janela sempre contém `x` "por perto", `x - arr[left]` e `arr[right] - x` já são não-negativos na maioria dos casos úteis, dispensando o `abs`.
- Tentar resolver sem entender por que o array precisa estar ordenado — sem essa garantia, a técnica de encolher as pontas não funcionaria (não haveria garantia de que os elementos mais distantes estão nas extremidades).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| x menor que todo o array | `arr=[1,2,3,4,5]`, `k=4`, `x=-1` | [1,2,3,4] | os 4 menores valores são sempre os mais próximos de x muito pequeno |
| k igual ao tamanho do array | `arr=[1,2,3]`, `k=3`, `x=2` | [1,2,3] | nenhuma remoção necessária, array inteiro já é a resposta |
| Empate resolvido pelo menor valor | `arr=[1,1,2,3,4,5]`, `k=4`, `x=-1` | [1,1,2,3] | com x tão distante, sempre prefere os valores menores |
| Exemplo do enunciado | `arr=[1,2,3,4,5]`, `k=4`, `x=3` | [1,2,3,4] | empate resolvido removendo da direita |

## 🔗 Conexões

- Problemas irmãos: [0035] Search Insert Position (mesma base de trabalhar com array ordenado, aqui generalizada para uma janela de k elementos em vez de um único índice), [0003] Longest Substring Without Repeating Characters (mesma família de técnica de dois ponteiros, aqui encolhendo de fora pra dentro em vez de crescer)
- No backend: selecionar os k registros mais próximos de um valor de referência (timestamp, score) num conjunto já ordenado, sem precisar reordenar nem escanear tudo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
