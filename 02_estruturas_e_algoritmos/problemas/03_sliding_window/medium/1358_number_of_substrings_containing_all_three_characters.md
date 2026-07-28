# [1358] Number of Substrings Containing All Three Characters

> 🔗 [LeetCode 1358](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dada uma string `s` consistindo só dos caracteres **a**, **b** e **c**, retorne o número de substrings contendo **pelo menos** uma ocorrência de cada um desses três caracteres.

**Exemplos:**
```
Input:  s = "abcabc"
Output: 10

Input:  s = "aaacb"
Output: 3

Input:  s = "abc"
Output: 1
```

**Restrições (e o que elas denunciam):**
- `3 <= s.length <= 5 * 10^4` → O(n²) força bruta é arriscado; O(n) é o esperado
- `s` só contém `'a'`, `'b'` ou `'c'` → alfabeto de 3 símbolos, simplificando o rastreamento

## 🧭 Como reconhecer o padrão

"Contar substrings contendo pelo menos uma ocorrência de cada um de vários caracteres" é resolvido rastreando a **última posição vista** de cada caractere: para um `right` fixo, toda substring começando em `[0, minLast]` (onde `minLast` é a posição mais antiga entre as últimas ocorrências de a, b, c) e terminando em `right` contém os 3 caracteres — soma-se `minLast+1` de uma vez.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, checar se a substring contém os 3 caracteres.

- Tempo: O(n²) (ou O(n³) se recontar do zero) · Espaço: O(1)
- **Por que não basta:** revalida a presença dos 3 caracteres do zero a cada substring candidata, sem aproveitar a última posição já conhecida de cada um.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha `lastSeen[a]`, `lastSeen[b]`, `lastSeen[c]` (a última posição de cada caractere, `-1` se ainda não visto). A cada `right`, atualize a última posição do caractere atual. Se as 3 já apareceram (`minLast != -1`), toda substring começando em `0..minLast` e terminando em `right` contém os 3 — some `minLast+1` ao total.

## 🎬 Exemplo passo a passo

`s = "abcabc"` (índices: a0 b1 c2 a3 b4 c5)

| right | char | last[a],last[b],last[c] | minLast | contribuição (minLast+1) | total |
|---|---|---|---|---|---|
| 0 | a | 0,-1,-1 | -1 (falta b,c) | 0 | 0 |
| 1 | b | 0,1,-1 | -1 (falta c) | 0 | 0 |
| 2 | c | 0,1,2 | 0 | 1 | 1 |
| 3 | a | 3,1,2 | 1 | 2 | 3 |
| 4 | b | 3,4,2 | 2 | 3 | 6 |
| 5 | c | 3,4,5 | 3 | 4 | 10 |

Resultado final: `10` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numberOfSubstrings(String s) {
    int[] lastSeen = {-1, -1, -1};
    long count = 0;

    for (int right = 0; right < s.length(); right++) {
        lastSeen[s.charAt(right) - 'a'] = right;
        int minLast = Math.min(lastSeen[0], Math.min(lastSeen[1], lastSeen[2]));
        if (minLast != -1) {
            count += minLast + 1; // toda substring começando em 0..minLast e terminando em right é válida
        }
    }

    return (int) count;
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

- `minLast + 1` representa quantos inícios válidos existem (de `0` a `minLast`) — todos, combinados com o `right` atual, formam uma substring que contém os 3 caracteres, porque o caractere mais "antigo" visto ainda está dentro do intervalo `[0, right]`.
- Enquanto algum dos 3 caracteres ainda não apareceu, `minLast` continua `-1` e nenhuma contribuição é somada — a checagem `minLast != -1` é essencial.
- Usar `long` para o total é necessário: com `n` até `5×10^4`, o total pode chegar à ordem de `10^9`, passando do limite seguro de `int`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Tamanho mínimo, um de cada | `"abc"` | 1 | única substring possível já contém os 3 |
| Um caractere ausente | `"aabb"` | 0 | nunca há 'c' na string |
| Muitas repetições no início | `"aaacb"` | 3 | só as substrings terminando em 'b' (a partir do momento em que 'c' aparece) contam |
| Exemplo maior do enunciado | `"abcabc"` | 10 | contagem cresce rápido conforme mais caracteres já apareceram |

## 🔗 Conexões

- Problemas irmãos: [0076] Minimum Window Substring (mesma família de rastrear a última posição/contagem necessária de cada caractere-alvo), [3258] Count Substrings That Satisfy K-Constraint I (mesma técnica de "contar todas as substrings válidas terminando em right" somando de uma vez)
- No backend: contar quantas janelas de um fluxo de eventos contêm pelo menos uma ocorrência de cada tipo obrigatório de evento (início, processamento e fim de uma transação), útil em auditoria de completude de pipelines.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
