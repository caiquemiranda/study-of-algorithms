# [0796] Rotate String

> 🔗 [LeetCode 796](https://leetcode.com/problems/rotate-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#StringMatching` `#Easy`

## 📜 O Problema

Dadas duas strings `s` e `goal`, retorne `true` **se e somente se** `s` **pode se tornar** `goal` **depois de algumas rotações** em `s`.

Uma **rotação** em `s` consiste em mover o caractere mais à esquerda de `s` para a posição mais à direita.

- Por exemplo, se `s = "abcde"`, ela vira `"bcdea"` depois de uma rotação.

**Exemplos:**
```
Input:  s = "abcde", goal = "cdeab"
Output: true

Input:  s = "abcde", goal = "abced"
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length, goal.length <= 100` → entrada minúscula, qualquer O(n) ou até O(n²) resolve com folga
- `s` e `goal` consistem de letras minúsculas do inglês → sem preocupação de caixa

## 🧭 Como reconhecer o padrão

"A string pode se tornar outra através de rotações (mover caracteres do início para o fim)" é o mesmo truque de concatenação de [0459] Repeated Substring Pattern: qualquer rotação de `s` é uma substring contígua de `s+s`. Basta checar se `goal` é substring de `s+s` (com a checagem extra de tamanho igual).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar cada uma das `n` rotações possíveis de `s` manualmente (mover o primeiro caractere para o fim, um passo de cada vez) e comparar cada uma com `goal`.

- Tempo: O(n²) — n rotações possíveis, cada comparação de string custa O(n) · Espaço: O(n) por rotação gerada
- **Por que não basta:** reconstruir cada rotação inteira do zero repete trabalho; existe uma forma de testar "é alguma rotação" sem gerar nenhuma delas explicitamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se `s.length() != goal.length()`, já é impossível (rotação não muda o tamanho). Caso contrário, concatene `s+s` — essa string contém TODAS as rotações possíveis de `s` como substrings contíguas. Basta checar se `goal` é substring de `s+s`.

## 🎬 Exemplo passo a passo

`s = "abcde"`, `goal = "cdeab"`

| Passo | Construção | Valor |
|---|---|---|
| 1 | tamanhos batem? | sim (5 == 5) |
| 2 | s+s | "abcdeabcde" |
| 3 | goal aparece em s+s? | sim, a partir do índice 2 |

Resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) esperado — concatenação O(n) e uma busca de substring que, para n≤100, se comporta linearmente na prática (a implementação naive de `contains` do Java é O(n·m) no pior caso teórico geral, mas isso não se manifesta de forma relevante aqui)
- **Espaço:** O(n) — para a string concatenada `s+s`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean rotateString(String s, String goal) {
    // rotação não muda o tamanho: tamanhos diferentes já eliminam a possibilidade
    if (s.length() != goal.length()) {
        return false;
    }
    // s+s contém TODAS as rotações possíveis de s como substrings contíguas
    return (s + s).contains(goal);
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

- Esquecer de checar `s.length() != goal.length()` antes de concatenar — sem essa checagem, uma `goal` mais curta poderia aparecer "por acidente" dentro de `s+s` mesmo sem ser uma rotação válida (ex.: `s="aa", goal="a"` daria falso positivo).
- Implementar a geração manual de rotações com `substring` + concatenação dentro de um loop — funciona, mas é mais código e mais chance de erro de índice do que o truque de `s+s`.
- Confundir "rotação" com "qualquer reordenação" (anagrama) — rotação preserva a ordem relativa dos caracteres, só desloca o ponto de início; `"abcde"` e `"abced"` têm as mesmas letras mas `"abced"` não é uma rotação válida (ver exemplo 2 do enunciado).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Rotação válida | `s="abcde", goal="cdeab"` | true | caso padrão do enunciado |
| Mesmas letras, não é rotação | `s="abcde", goal="abced"` | false | ordem relativa quebrada, não é deslocamento simples |
| Tamanhos diferentes | `s="a", goal="aa"` | false | rotação nunca muda o tamanho da string |
| Strings iguais (rotação de 0 passos) | `s="abc", goal="abc"` | true | toda string é uma rotação trivial de si mesma |

## 🔗 Conexões

- Problemas irmãos: [0459] Repeated Substring Pattern (mesmo truque de concatenar `s+s` para testar propriedade cíclica), [0028] Find the Index of the First Occurrence in a String (mesma operação básica de busca de substring)
- No backend: detecção de duplicatas cíclicas em identificadores (ex.: verificar se dois hashes/tokens circulares representam o mesmo estado), validação de sequências em protocolos que permitem deslocamento de buffer circular.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
