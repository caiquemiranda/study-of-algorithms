# [3258] Count Substrings That Satisfy K-Constraint I

> 🔗 [LeetCode 3258](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#String` `#Easy`

## 📜 O Problema

Dada uma string **binária** `s` e um inteiro `k`, uma string binária satisfaz a **k-constraint** se: o número de `'0'`s é no máximo `k`, **ou** o número de `'1'`s é no máximo `k`. Retorne o número de substrings de `s` que satisfazem a k-constraint.

**Exemplos:**
```
Input:  s = "10101", k = 1
Output: 12
Explicação: toda substring, exceto "1010", "10101" e "0101", satisfaz a k-constraint.

Input:  s = "1010101", k = 2
Output: 25

Input:  s = "11111", k = 1
Output: 15
Explicação: todas as substrings satisfazem (count0 é sempre 0 ≤ k).
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 50` → entrada pequena, mas a técnica de dois ponteiros generaliza para strings bem maiores
- `1 <= k <= s.length` → `k` sempre cabe dentro do tamanho da string

## 🧭 Como reconhecer o padrão

"Contar substrings que satisfazem uma condição sobre contagens de caracteres numa janela" é o padrão clássico de dois ponteiros para contagem: encolher a janela pela esquerda só torna as contagens **menores ou iguais**, então a condição nunca piora ao encolher. Isso significa que, para cada `right`, existe um `left` mínimo tal que toda substring `[l', right]` com `l' >= left` também satisfaz a condição — bastando somar `right - left + 1` de uma vez.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada substring `[left, right]` (todos os O(n²) pares), contar `'0'`s e `'1'`s do zero e checar a condição.

- Tempo: O(n³) · Espaço: O(1)
- **Por que não basta:** recomputa as contagens de zero a cada substring candidata, mesmo quando a maioria dos caracteres é compartilhada entre substrings vizinhas terminando no mesmo `right`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use dois ponteiros. Para cada `right`, mantenha as contagens de `'0'` e `'1'` na janela `[left, right]`. Enquanto AMBAS as contagens excederem `k` (violando a condição), encolha `left`. Quando a janela satisfizer a condição, toda substring `[l', right]` com `l' >= left` também satisfaz — some `right - left + 1` ao total.

## 🎬 Exemplo passo a passo

`s = "10101"`, `k = 1` (índices: 1₀ 0₁ 1₂ 0₃ 1₄)

| right | char | count0,count1 (após incluir) | Encolhe? | left final | válidas (right-left+1) | total acumulado |
|---|---|---|---|---|---|---|
| 0 | 1 | 0,1 | não | 0 | 1 | 1 |
| 1 | 0 | 1,1 | não | 0 | 2 | 3 |
| 2 | 1 | 1,2 | não | 0 | 3 | 6 |
| 3 | 0 | 2,2 | sim: remove s[0]='1' → 2,1 | 1 | 3 | 9 |
| 4 | 1 | 2,2 | sim: remove s[1]='0' → 1,2 | 2 | 3 | 12 |

Resultado final: `12` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `left` e `right` cada um avança no máximo `n` vezes ao todo (amortizado)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countKConstraintSubstrings(String s, int k) {
    int left = 0;
    int count0 = 0;
    int count1 = 0;
    long total = 0;

    for (int right = 0; right < s.length(); right++) {
        if (s.charAt(right) == '0') {
            count0++;
        } else {
            count1++;
        }

        while (count0 > k && count1 > k) {
            if (s.charAt(left) == '0') {
                count0--;
            } else {
                count1--;
            }
            left++;
        }

        total += right - left + 1; // toda substring [l', right] com l' >= left também satisfaz
    }

    return (int) total;
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

- A condição é um **OU**: basta que uma das contagens (`0`s ou `1`s) seja `<= k` — a condição de encolhimento é o oposto, só encolhe quando **ambas** excedem `k`.
- Esquecer que, uma vez que `[left, right]` satisfaz a condição, toda substring `[l', right]` com `l' >= left` também satisfaz — por isso basta somar `right - left + 1` de uma vez, sem enumerar cada substring individualmente.
- Usar `int` para o total funciona aqui (`n<=50` limita o total a `n(n+1)/2=1275`), mas `long` é hábito mais seguro ao acumular contagens que crescem quadraticamente com `n`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só um tipo de caractere | `s="11111"`, `k=1` | 15 | count0 é sempre 0 ≤ k, toda substring satisfaz (n(n+1)/2=15) |
| k igual ao tamanho da string | `s="10101"`, `k=5` | 15 | k tão grande que qualquer substring satisfaz |
| String de tamanho mínimo | `s="0"`, `k=1` | 1 | única substring, count0=1≤1 |
| Exemplo maior do enunciado | `s="1010101"`, `k=2` | 25 | só substrings maiores (que teriam >2 de cada dígito) ficam de fora |

## 🔗 Conexões

- Problemas irmãos: [0209] Minimum Size Subarray Sum (mesma técnica de dois ponteiros com condição monotônica ao encolher), [3306] Count of Substrings Containing Every Vowel and K Consonants II (mesma ideia de "contar todas as substrings válidas terminando em right somando right-left+1")
- No backend: contar quantos intervalos de um log satisfazem uma regra de composição — por exemplo, no máximo `k` eventos de erro OU no máximo `k` eventos de sucesso — útil para relatórios de janelas de estabilidade.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
