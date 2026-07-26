# [1534] Count Good Triplets

> 🔗 [LeetCode 1534](https://leetcode.com/problems/count-good-triplets/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array de inteiros `arr`, e três inteiros `a`, `b` e `c`, encontre o número de trios bons. Um trio `(arr[i], arr[j], arr[k])` é **bom** se as seguintes condições são verdadeiras:
- `0 <= i < j < k < arr.length`
- `|arr[i] - arr[j]| <= a`
- `|arr[j] - arr[k]| <= b`
- `|arr[i] - arr[k]| <= c`

Retorne o número de trios bons.

**Exemplos:**
```
Input:  arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explicação: existem 4 trios bons: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Input:  arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explicação: nenhum trio satisfaz todas as condições.
```

**Restrições (e o que elas denunciam):**
- `3 <= arr.length <= 100` → n pequeno o suficiente para permitir força bruta O(n³) = até 10^6, tranquilo
- `0 <= arr[i] <= 1000`, `0 <= a, b, c <= 1000` → sem overflow

## 🧭 Como reconhecer o padrão

Quando o enunciado pede para contar TRIOS que satisfazem uma condição, e o tamanho do array é pequeno (n ≤ 100, então n³ ≤ 10^6), a enumeração direta de todos os trios é a abordagem esperada — não é preciso buscar uma otimização mais sofisticada para esse tamanho.

## 🐢 Solução 1 — Força bruta (e também a solução aceita aqui)

Três loops aninhados percorrendo todos os trios `(i,j,k)` com `i<j<k`, verificando as três condições de diferença absoluta para cada um.

- Tempo: O(n³) — combinação de todos os trios possíveis · Espaço: O(1)
- **Por que é aceitável aqui:** com n ≤ 100, n³ é no máximo 1.000.000 — perfeitamente rápido; não há necessidade de estruturas de dados extras para este tamanho.

## 💡 Nota sobre otimização

Não há uma segunda solução "otimizada" relevante para o tamanho dado — este é um caso raro onde a enumeração completa já é a resposta esperada, dado o limite pequeno de n. Uma pequena melhoria prática é cortar cedo (`continue`) assim que a primeira condição falha, evitando entrar no loop mais interno à toa.

## 🎬 Exemplo passo a passo

`arr = [3,0,1,1,9,7]`, `a=7, b=2, c=3` — verificando o trio de índices (0,1,2) → valores (3,0,1):

| Passo | Verificação | Cálculo | Resultado |
|---|---|---|---|
| 1 | \|arr[0]-arr[1]\| <= a | \|3-0\|=3 <= 7 | sim |
| 2 | \|arr[1]-arr[2]\| <= b | \|0-1\|=1 <= 2 | sim |
| 3 | \|arr[0]-arr[2]\| <= c | \|3-1\|=2 <= 3 | sim |

Trio (3,0,1) é bom → conta 1. Repetindo para todos os C(6,3)=20 trios possíveis, encontramos 4 trios bons no total.

Resultado final: `4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n³)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countGoodTriplets(int[] arr, int a, int b, int c) {
    int contador = 0;
    int n = arr.length;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (Math.abs(arr[i] - arr[j]) > a) {
                continue; // já falha a primeira condição, nem vale checar k
            }
            for (int k = j + 1; k < n; k++) {
                if (Math.abs(arr[j] - arr[k]) <= b && Math.abs(arr[i] - arr[k]) <= c) {
                    contador++;
                }
            }
        }
    }
    return contador;
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

- Esquecer a restrição de ordem `i < j < k` — trocar a ordem dos índices no cálculo das diferenças quebra a correspondência entre cada condição e o par de índices que ela testa.
- Não aproveitar o `continue` antecipado quando a primeira condição já falha — não é um erro de correção, só uma otimização perdida.
- Achar que o problema pede combinações sem ordem (como um "conjunto" de 3 valores) — a posição no array importa para a restrição `i<j<k`, mesmo que os VALORES possam se repetir.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | arr=[3,0,1,1,9,7], a=7, b=2, c=3 | 4 | caso do enunciado |
| Nenhum trio bom | arr=[1,1,2,2,3], a=0, b=0, c=1 | 0 | restrições muito rígidas |
| Array mínimo (3 elementos) | arr=[1,2,3], a=1,b=1,c=2 | 1 | um único trio possível, e ele é bom |
| Todos os elementos iguais | arr=[5,5,5,5], a=0,b=0,c=0 | 4 | todas as diferenças são 0, C(4,3)=4 trios bons |

## 🔗 Conexões

- Problemas irmãos: [0015] 3Sum (mesmo domínio de enumerar trios, mas com técnica de dois ponteiros para arrays maiores), [1128] Number of Equivalent Domino Pairs (mesma ideia de contar combinações que satisfazem uma condição, mas com pares em vez de trios)
- No backend: análise combinatória em conjuntos pequenos de dados (ex.: encontrar grupos de 3 transações com valores dentro de faixas de tolerância específicas, útil em detecção de padrões suspeitos com volume de dados limitado).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
