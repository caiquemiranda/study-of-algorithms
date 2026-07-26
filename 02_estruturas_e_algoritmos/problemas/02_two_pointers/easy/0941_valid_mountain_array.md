# [0941] Valid Mountain Array

> 🔗 [LeetCode 941](https://leetcode.com/problems/valid-mountain-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array de inteiros `arr`, retorne `true` se e somente se ele é um **array montanha** válido.

`arr` é um array montanha se e somente se:
- `arr.length >= 3`
- Existe algum `i` com `0 < i < arr.length - 1` tal que:
  - `arr[0] < arr[1] < ... < arr[i-1] < arr[i]`
  - `arr[i] > arr[i+1] > ... > arr[arr.length-1]`

**Exemplos:**
```
Input:  arr = [2,1]
Output: false

Input:  arr = [3,5,5]
Output: false

Input:  arr = [0,3,2,1]
Output: true
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 10^4` → O(n) esperado
- `0 <= arr[i] <= 10^4` → sem negativos, não afeta a lógica de comparação
- precisa de um PICO estrito (nem no início nem no fim do array), com subida estritamente crescente e descida estritamente decrescente

## 🧭 Como reconhecer o padrão

"Validar uma forma que sobe e depois desce" (uma "montanha") é resolvido com dois ponteiros caminhando de direções opostas até convergir no topo — se convergirem exatamente no mesmo índice (que não seja a primeira nem a última posição), é uma montanha válida.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Encontrar o índice do valor máximo do array (o possível pico), e então verificar separadamente, em duas passadas completas, se o trecho antes dele é estritamente crescente e o trecho depois é estritamente decrescente.

- Tempo: O(n) — na prática já é linear (achar o máximo, checar subida, checar descida) · Espaço: O(1)
- **Por que não basta:** embora já seja O(n), essa abordagem depende de achar o valor MÁXIMO primeiro (que pode ter empates, complicando a lógica de "qual índice é o pico real"); os dois ponteiros resolvem isso de forma mais direta, sem precisar identificar o máximo explicitamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um ponteiro `esquerda` começando em 0, subindo enquanto `arr[esquerda] < arr[esquerda+1]`. Use um ponteiro `direita` começando no último índice, subindo (em direção ao início) enquanto `arr[direita] < arr[direita-1]`. Se os dois pararem exatamente no mesmo índice, e esse índice não é nem o primeiro nem o último elemento do array, é uma montanha válida.

## 🎬 Exemplo passo a passo

`arr = [0,3,2,1]`

| Passo | Ponteiro | Posição | Condição | Ação |
|---|---|---|---|---|
| 1 | esquerda | 0 | arr[0]=0 < arr[1]=3 | avança: esquerda=1 |
| 2 | esquerda | 1 | arr[1]=3 < arr[2]=2? não | para: esquerda=1 |
| 3 | direita | 3 (último índice) | arr[3]=1 < arr[2]=2 | avança: direita=2 |
| 4 | direita | 2 | arr[2]=2 < arr[1]=3 | avança: direita=1 |
| 5 | direita | 1 | arr[1]=3 < arr[0]=0? não | para: direita=1 |

`esquerda(1) == direita(1)`, e não é nem índice 0 nem o último índice (3) → **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada ponteiro percorre o array no máximo uma vez
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean validMountainArray(int[] arr) {
    int n = arr.length;
    int esquerda = 0;
    int direita = n - 1;

    // sobe a partir da esquerda enquanto a sequência é estritamente crescente
    while (esquerda < n - 1 && arr[esquerda] < arr[esquerda + 1]) {
        esquerda++;
    }
    // sobe a partir da direita (em direção ao início) enquanto é estritamente crescente nesse sentido
    while (direita > 0 && arr[direita] < arr[direita - 1]) {
        direita--;
    }

    // o pico precisa ser o mesmo índice para os dois ponteiros, e não pode ser a borda
    return esquerda == direita && esquerda != 0 && direita != n - 1;
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

- Esquecer de checar `esquerda != 0` e `direita != n - 1` — sem isso, um array totalmente crescente (`[1,2,3]`, sem descida) ou totalmente decrescente (`[3,2,1]`, sem subida) passaria como "válido" incorretamente, pois os ponteiros ainda convergiriam num único ponto na borda.
- Usar `<=` em vez de `<` nas condições dos loops — o enunciado exige estritamente crescente/decrescente; um platô (`[1,2,2,1]`) não é uma montanha válida.
- Não tratar arrays muito curtos (`length < 3`) — o enunciado já garante que uma montanha válida precisa de pelo menos 3 elementos; com `length <= 2`, os ponteiros nunca convergem longe o suficiente das bordas, e a checagem final já retorna `false` naturalmente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só desce | `[2,1]` | false | não há subida antes do topo, `esquerda` fica preso em 0 |
| Platô no topo | `[3,5,5]` | false | "5,5" não é estritamente crescente nem decrescente |
| Montanha válida | `[0,3,2,1]` | true | caso padrão do enunciado |
| Só sobe (sem descida) | `[1,2,3]` | false | ponteiro direita nunca se move, converge na borda direita |

## 🔗 Conexões

- Problemas irmãos: [0852] Peak Index in a Mountain Array (mesma "forma" de array, mas já garantida válida — pede só o índice do pico via busca binária), [0896] Monotonic Array (mesmo domínio de validar uma propriedade de ordem percorrendo o array)
- No backend: validação de séries temporais em formato de "pico único" (ex.: métricas que sobem até um ápice e depois caem, como tráfego de um evento) antes de aplicar uma análise que assume esse formato.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
