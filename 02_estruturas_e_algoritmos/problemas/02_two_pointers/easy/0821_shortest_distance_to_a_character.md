# [0821] Shortest Distance to a Character

> 🔗 [LeetCode 821](https://leetcode.com/problems/shortest-distance-to-a-character/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` e um caractere `c` que ocorre em `s`, retorne um array `answer` onde `answer[i]` é a **distância** (`abs(i - j)`) do índice `i` até a ocorrência **mais próxima** de `c` em `s`.

**Exemplos:**
```
Input:  s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Input:  s = "aaab", c = "b"
Output: [3,2,1,0]
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^4` → O(n²) é arriscado, O(n) é o esperado
- `c` ocorre **pelo menos uma vez** garantido → nunca existe um índice sem nenhum `c` de referência
- A distância mínima pode vir tanto de uma ocorrência **antes** quanto **depois** do índice `i` → sinaliza que uma única varredura (só olhando pra trás, por exemplo) não é suficiente

## 🧭 Como reconhecer o padrão

"Para cada posição, achar a distância até o elemento de referência mais próximo, podendo estar de qualquer lado" é resolvido com **duas varreduras em direções opostas** (duas passadas de ponteiro): uma da esquerda pra direita, guardando a posição do `c` mais recente já visto; outra da direita pra esquerda, guardando o `c` mais próximo ainda por vir — e a resposta final combina o melhor das duas.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i`, percorrer a string comparando a distância até **todas** as ocorrências de `c`, guardando a menor.

- Tempo: O(n × m), onde `m` é a quantidade de ocorrências de `c` (pode chegar a O(n²) se `c` for frequente) · Espaço: O(1) além do array de resposta
- **Por que não basta:** recalcula, para cada índice, a distância até ocorrências de `c` que claramente não são as mais próximas; só a ocorrência mais próxima à esquerda e a mais próxima à direita importam, e ambas podem ser rastreadas incrementalmente numa passada só de cada lado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça uma passada da **esquerda para a direita**, guardando em `prev` o índice do último `c` visto; em cada posição, `answer[i] = i - prev` (distância até o `c` mais próximo à esquerda, ou "infinito" se ainda não viu nenhum). Depois, faça uma passada da **direita para a esquerda**, guardando em `next` o índice do próximo `c` (visto de trás para frente); em cada posição, atualize `answer[i] = min(answer[i], next - i)`. Ao final, cada posição tem a menor distância entre as duas direções.

## 🎬 Exemplo passo a passo

`s = "aaab"`, `c = 'b'` (índices 0 a 3)

| Passo | Sentido | i | referência de `c` já vista | answer[i] |
|---|---|---|---|---|
| 1 | → | 0 | nenhuma ainda | ∞ (provisório) |
| 2 | → | 1 | nenhuma ainda | ∞ |
| 3 | → | 2 | nenhuma ainda | ∞ |
| 4 | → | 3 | índice 3 (é o próprio `'b'`) | 0 |
| 5 | ← | 3 | índice 3 | min(0, 0) = 0 |
| 6 | ← | 2 | índice 3 | min(∞, 1) = 1 |
| 7 | ← | 1 | índice 3 | min(∞, 2) = 2 |
| 8 | ← | 0 | índice 3 | min(∞, 3) = 3 |

Resultado final: `[3,2,1,0]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas lineares pela string
- **Espaço:** O(n) para o array de resposta (exigido pelo problema); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] shortestToChar(String s, char c) {
    int n = s.length();
    int[] answer = new int[n];
    int prev = Integer.MIN_VALUE / 2; // "nenhum c visto ainda" à esquerda; evita overflow no cálculo

    // varredura esquerda -> direita: distância até o c mais próximo à esquerda
    for (int i = 0; i < n; i++) {
        if (s.charAt(i) == c) {
            prev = i;
        }
        answer[i] = i - prev;
    }

    int next = Integer.MAX_VALUE / 2; // "nenhum c visto ainda" à direita
    // varredura direita -> esquerda: combina com a distância até o c mais próximo à direita
    for (int i = n - 1; i >= 0; i--) {
        if (s.charAt(i) == c) {
            next = i;
        }
        answer[i] = Math.min(answer[i], next - i);
    }

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

- Usar um sentinela ingênuo (como `-1` ou `0`) para "nenhum `c` visto ainda" — se a subtração `i - prev` puder dar overflow ou se confundir com um índice real, a distância calculada fica errada; valores como `Integer.MIN_VALUE/2` evitam os dois problemas.
- Fazer só UMA varredura (esquerda pra direita) — isso só encontra o `c` mais próximo **à esquerda**; índices antes da primeira ocorrência de `c` nunca teriam referência nessa direção, por isso a segunda varredura é obrigatória.
- Esquecer o `Math.min` na segunda varredura — sem combinar com o resultado da primeira, a segunda passada sobrescreveria a resposta em vez de só melhorá-la quando a ocorrência à direita for mais próxima.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo do enunciado | `s="loveleetcode"`, `c='e'` | `[3,2,1,0,1,0,0,1,2,2,1,0]` | várias ocorrências de `'e'`, testa empate (índice 4) |
| `c` só no final | `s="aaab"`, `c='b'` | `[3,2,1,0]` | só existe referência à direita para todos os índices anteriores |
| `c` na primeira posição | `s="baaa"`, `c='b'` | `[0,1,2,3]` | só existe referência à esquerda para todos os índices seguintes |
| `c` em todas as posições | `s="ccc"`, `c='c'` | `[0,0,0]` | distância 0 em todo índice |

## 🔗 Conexões

- Problemas irmãos: [1855] Maximum Distance Between a Pair of Values (também combina duas varreduras/ponteiros para achar uma distância ótima), [0042] Trapping Rain Water (mesma família de "pré-calcular o melhor valor à esquerda e à direita de cada posição")
- No backend: calcular, para cada evento de um log, a distância até o evento de erro mais próximo (antes ou depois) — útil em análise de causa raiz, correlacionando eventos próximos a uma falha.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
