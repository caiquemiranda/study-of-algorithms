# [1385] Find the Distance Value Between Two Arrays

> 🔗 [LeetCode 1385](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Dados dois arrays de inteiros `arr1` e `arr2` e um inteiro `d`, retorne o **valor de distância** entre eles: a quantidade de elementos `arr1[i]` para os quais **não existe nenhum** `arr2[j]` com `|arr1[i] - arr2[j]| <= d`.

**Exemplos:**
```
Input:  arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2    Output: 2
        (4 e 5 não têm nenhum vizinho em arr2 dentro de d=2; 8 tem, pois |8-8|=0<=2)
Input:  arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3    Output: 2
```

**Restrições (e o que elas denunciam):**
- `1 <= arr1.length, arr2.length <= 500` → força bruta O(n×m) chega a 250.000, passa tranquilo, mas o padrão de busca binária é o mais didático e escala melhor
- `-1000 <= arr1[i], arr2[j] <= 1000`, `0 <= d <= 100` → intervalos pequenos, sem risco de overflow
- "não existe nenhum `arr2[j]`" → a condição é "para TODO elemento de arr2, a distância é maior que d" — equivalente a dizer que o **intervalo `[arr1[i]-d, arr1[i]+d]` não contém nenhum elemento de arr2**, o que é uma pergunta natural de busca binária num array ordenado

## 🧭 Como reconhecer o padrão

"Existe algum elemento do outro array dentro de uma faixa `[x-d, x+d]`?" é uma busca por **fronteira**: ordene `arr2` e, para cada elemento de `arr1`, encontre via busca binária o primeiro elemento `>= x-d`. Se esse elemento existir e for `<= x+d`, então existe vizinho dentro da distância — senão, não existe.

## 🐢 Solução 1 — Força bruta

Para cada `arr1[i]`, percorrer `arr2` inteiro verificando se algum `arr2[j]` satisfaz `|arr1[i] - arr2[j]| <= d`.

- Tempo: O(n × m) · Espaço: O(1)
- **Por que não basta:** funciona dentro do limite deste problema, mas repete a varredura completa de `arr2` para cada elemento de `arr1` — ordenando `arr2` uma única vez, cada consulta vira O(log m) em vez de O(m).

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `arr2` uma única vez (O(m log m)). Para cada `x` em `arr1`, faça busca binária pelo primeiro elemento de `arr2` que é `>= x - d` (lower bound). Se esse elemento existir **e** for `<= x + d`, existe vizinho dentro da faixa — `x` não conta para a distância. Caso contrário (não existe elemento `>= x-d`, ou o que existe já é maior que `x+d`), `x` conta para a resposta.

Como `arr2` está ordenado, o primeiro elemento `>= x-d` é o **candidato mais próximo por baixo** de estar dentro da faixa — se nem ele serve, nenhum outro elemento maior vai servir (todos estão ainda mais longe).

## 🎬 Exemplo passo a passo

`arr1 = [4, 5, 8]`, `arr2 ordenado = [1, 8, 9, 10]`, `d = 2`

| Passo | x | Faixa [x-d, x+d] | Busca binária (lower bound de x-d) | Achou dentro da faixa? | Conta para distância? |
|---|---|---|---|---|---|
| 1 | 4 | [2, 6] | primeiro `>=2` é 8 (índice 1) | 8 > 6 → não | sim (+1) |
| 2 | 5 | [3, 7] | primeiro `>=3` é 8 (índice 1) | 8 > 7 → não | sim (+1) |
| 3 | 8 | [6, 10] | primeiro `>=6` é 8 (índice 1) | 8 <= 10 → sim | não |

Resultado final: `2` ✔ (4 e 5 contam, 8 não)

## ⚡ Complexidade da solução ótima

- **Tempo:** O((n + m) log m) — ordenar `arr2` custa O(m log m), depois cada uma das `n` buscas binárias custa O(log m)
- **Espaço:** O(log m) a O(m) — dependendo do algoritmo de sort usado internamente pela linguagem

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
    Arrays.sort(arr2);                       // habilita busca binária por faixa
    int contador = 0;

    for (int x : arr1) {
        int idx = lowerBound(arr2, x - d);   // primeiro índice com arr2[idx] >= x - d
        // Se não existe tal índice (passou do fim) OU o candidato já excede x+d,
        // então nenhum elemento de arr2 está dentro da faixa [x-d, x+d].
        if (idx == arr2.length || arr2[idx] > x + d) {
            contador++;
        }
    }
    return contador;
}

// Busca binária clássica de lower bound: primeira posição com valor >= alvo.
private int lowerBound(int[] arr, int alvo) {
    int left = 0, right = arr.length;        // right = length (não length-1): representa "não achou"

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] < alvo) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
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

- **Esquecer de checar `idx == arr2.length`**: se `x - d` for maior que todos os elementos de `arr2`, a busca binária retorna um índice fora dos limites — acessar `arr2[idx]` sem essa checagem lança exceção de índice.
- **Checar só o candidato do lower bound**: como `arr2` está ordenado, se o primeiro elemento `>= x-d` já é maior que `x+d`, nenhum outro elemento (que só pode ser igual ou maior) vai servir — não precisa checar mais nada depois dele, mas também não precisa checar elementos antes (eles são todos `< x-d`, ou seja, fora da faixa por baixo).
- **`d = 0`**: vira uma checagem de igualdade exata (`arr2` contém `x`?) — bom caso de borda para confirmar que a lógica de faixa degenera corretamente.
- **Confundir "conta para distância" com "não conta"**: a resposta soma os elementos de `arr1` que **não têm** vizinho próximo — é fácil inverter a condição e contar o oposto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| d = 0 (igualdade exata) | `arr1=[1,2,3], arr2=[2,3,4], d=0` | 1 | só o 1 não tem par exato em arr2 |
| Nenhum elemento perto | `arr1=[1,2,3], arr2=[100,200], d=1` | 3 | todos ficam de fora da faixa |
| Todos dentro da faixa | `arr1=[1,2,3], arr2=[1,2,3], d=0` | 0 | todo elemento tem par exato |
| Um elemento cada | `arr1=[5], arr2=[10], d=4` | 1 | \|5-10\|=5 > 4, único elemento conta |
| Exemplo do enunciado | `arr1=[4,5,8], arr2=[10,9,1,8], d=2` | 2 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0035] Search Insert Position** (mesma busca de lower bound), **[0658] Find K Closest Elements** (busca binária por vizinhos mais próximos num array ordenado)
- No backend: verificar se existe algum registro "próximo o suficiente" de um valor de referência (ex.: detecção de duplicatas aproximadas por timestamp, ou correspondência de preços dentro de uma tolerância) é resolvido com essa mesma ideia de ordenar e buscar faixa em vez de comparar tudo com tudo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
