# [1208] Get Equal Substrings Within Budget

> 🔗 [LeetCode 1208](https://leetcode.com/problems/get-equal-substrings-within-budget/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#PrefixSum` `#Medium`

## 📜 O Problema

Dadas duas strings `s` e `t` de mesmo comprimento e um inteiro `maxCost`, você quer transformar `s` em `t`. Trocar o caractere `i` de `s` pelo de `t` custa `|s[i] - t[i]|` (diferença absoluta entre os valores ASCII). Retorne o comprimento máximo de uma substring de `s` que pode ser transformada na substring correspondente de `t` com custo total `<= maxCost`. Se nenhuma substring puder ser transformada, retorne `0`.

**Exemplos:**
```
Input:  s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explicação: "abc" de s pode virar "bcd", custando 3.

Input:  s = "abcd", t = "cdef", maxCost = 3
Output: 1

Input:  s = "abcd", t = "acde", maxCost = 0
Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n²) força bruta é arriscado; O(n) é o esperado
- `0 <= maxCost <= 10^6` → `maxCost` pode ser `0`, exigindo caracteres já idênticos
- `s` e `t` consistem só em letras minúsculas → o custo por posição é sempre não-negativo, garantindo a monotonicidade necessária pra técnica de janela

## 🧭 Como reconhecer o padrão

"Maior substring cujo custo acumulado (sempre não-negativo) cabe num orçamento" é dois ponteiros clássico: encolher a janela pela esquerda enquanto o custo exceder o orçamento é seguro, porque cada custo individual é `>= 0` — a mesma estrutura de [0209] Minimum Size Subarray Sum, aqui maximizando em vez de minimizar.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, somar os custos do zero e checar se `<= maxCost`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** recalcula a soma de custo inteira a cada par, ignorando que valores não-negativos permitem manter uma soma corrente que só cresce ao expandir e só diminui ao encolher.

## 💡 Solução 2 — A ideia otimizada (intuição)

Expanda `right`, somando `|s[right]-t[right]|` a uma soma corrente. Enquanto a soma exceder `maxCost`, encolha `left` (subtraindo o custo do elemento que sai). A cada passo válido, atualize o maior comprimento visto.

## 🎬 Exemplo passo a passo

`s = "abcd"`, `t = "bcdf"`, `maxCost = 3` → custo por posição: `[1,1,1,2]`

| right | cost[right] | sum após incluir | Encolhe? | left final | comprimento | melhor |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | não | 0 | 1 | 1 |
| 1 | 1 | 2 | não | 0 | 2 | 2 |
| 2 | 1 | 3 | não | 0 | 3 | 3 |
| 3 | 2 | 5 | sim: remove cost[0]=1→4 (ainda>3!) → remove cost[1]=1→3 | 2 | 2 | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int equalSubstring(String s, String t, int maxCost) {
    int left = 0;
    int sum = 0;
    int best = 0;

    for (int right = 0; right < s.length(); right++) {
        sum += Math.abs(s.charAt(right) - t.charAt(right));

        while (sum > maxCost) {
            sum -= Math.abs(s.charAt(left) - t.charAt(left));
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
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

- O custo é sempre não-negativo (`|s[i]-t[i]| >= 0`), o que garante a monotonicidade necessária pra técnica de encolher a janela — sem essa garantia, o encolhimento poderia pular a resposta correta.
- Calcular o custo sob demanda (`Math.abs(s.charAt(i)-t.charAt(i))`) evita alocar um array auxiliar de custos, mas o resultado é matematicamente idêntico a pré-computar um array `cost[]`.
- `maxCost = 0` é um caso válido: a resposta é o maior trecho onde `s` e `t` já são idênticos (nenhuma troca permitida).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| maxCost=0 | `s="abcd"`, `t="acde"`, `maxCost=0` | 1 | só o primeiro caractere já é igual ('a'='a'); nenhuma troca permitida |
| Nenhuma janela grande cabe | `s="abcd"`, `t="cdef"`, `maxCost=3` | 1 | cada posição custa 2, só uma cabe no orçamento |
| s e t idênticos | `s="abc"`, `t="abc"`, `maxCost=0` | 3 | custo zero em toda posição, string inteira serve |
| Exemplo do enunciado | `s="abcd"`, `t="bcdf"`, `maxCost=3` | 3 | "abc"→"bcd" custa exatamente 3 |

## 🔗 Conexões

- Problemas irmãos: [0209] Minimum Size Subarray Sum (mesma técnica de dois ponteiros com condição monotônica, aqui maximizando em vez de minimizar), [1004] Max Consecutive Ones III (mesma ideia de "orçamento" de mudanças permitidas dentro de uma janela)
- No backend: encontrar o maior trecho de um arquivo ou payload que pode ser sincronizado dentro de um orçamento de banda/latência limitado, custando proporcionalmente à diferença byte a byte entre versões.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
