# [1763] Longest Nice Substring

> 🔗 [LeetCode 1763](https://leetcode.com/problems/longest-nice-substring/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#BitManipulation` `#Easy`

## 📜 O Problema

Uma string `s` é **nice** se, para toda letra do alfabeto que `s` contém, ela aparece tanto em maiúscula quanto em minúscula. Dado `s`, retorne a maior **substring** de `s` que é nice. Se houver empate, retorne a de ocorrência mais cedo. Se não houver nenhuma, retorne uma string vazia.

**Exemplos:**
```
Input:  s = "YazaAay"
Output: "aAa"
Explicação: 'A'/'a' é a única letra presente na substring, e ambas as caixas aparecem.

Input:  s = "Bb"
Output: "Bb"
Explicação: ambas as caixas de 'b' aparecem; a string inteira serve.

Input:  s = "c"
Output: ""
Explicação: não há substring nice.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → o array de tamanho pequeno permite até O(n²) com trabalho O(1) por passo, sem precisar de nada mais sofisticado
- `s` consiste em letras maiúsculas e minúsculas do alfabeto inglês → no máximo 26 letras distintas possíveis, cabendo perfeitamente em dois bitmasks de 26 bits (um para maiúsculas, outro para minúsculas)

## 🧭 Como reconhecer o padrão

"Maior substring que satisfaz uma condição sobre o conjunto de caracteres presentes" é resolvido expandindo uma janela caractere a caractere e mantendo, incrementalmente, um resumo do que já foi visto — aqui, dois bitmasks (letras maiúsculas vistas e minúsculas vistas). A janela `[left, right]` é válida exatamente quando os dois bitmasks são **iguais**: todo bit ligado em um está ligado no outro, ou seja, toda letra presente tem as duas caixas.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, extrair a substring `s[left..right]` e, para cada caractere dela, verificar se a versão de caixa oposta também aparece na MESMA substring (varredura completa a cada checagem).

- Tempo: O(n³) (O(n²) substrings, O(n) para validar cada uma) · Espaço: O(n) por substring extraída
- **Por que não basta:** recalcula do zero a checagem "toda letra tem seu par" a cada substring candidata, mesmo quando ela difere da anterior por apenas um caractere a mais.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada início `left`, expanda `right` mantendo dois bitmasks de 26 bits — um para letras maiúsculas vistas, outro para minúsculas. A cada caractere novo, ativa o bit correspondente no mask certo. Assim que `upperMask == lowerMask`, a janela `[left, right]` é nice; some seu comprimento contra o melhor resultado guardado até agora.

## 🎬 Exemplo passo a passo

`s = "YazaAay"` (índices: Y0 a1 z2 a3 A4 a5 y6) — mostrando a varredura a partir de `left = 3`, que produz o melhor resultado:

| right | char | upperMask (bits ligados) | lowerMask (bits ligados) | iguais? | comprimento | melhor |
|---|---|---|---|---|---|---|
| 3 | 'a' | {} | {a} | não | — | — |
| 4 | 'A' | {a} | {a} | sim | 2 (`aA`) | 2 |
| 5 | 'a' | {a} | {a} | sim | 3 (`aAa`) | 3 |
| 6 | 'y' | {a} | {a,y} | não | — | 3 |

Resultado final (considerando todos os `left`): `"aAa"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) — `n` valores de `left`, cada um expandindo `right` até o fim com trabalho O(1) por passo (operações de bitmask)
- **Espaço:** O(1) — dois inteiros de 26 bits, independente do tamanho da entrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String longestNiceSubstring(String s) {
    int n = s.length();
    int bestLen = 0;
    int bestStart = 0;

    for (int left = 0; left < n; left++) {
        int upperMask = 0;
        int lowerMask = 0;
        for (int right = left; right < n; right++) {
            char c = s.charAt(right);
            if (Character.isUpperCase(c)) {
                upperMask |= 1 << (c - 'A');
            } else {
                lowerMask |= 1 << (c - 'a');
            }
            // masks iguais = toda letra presente tem as duas caixas; ">" garante a ocorrência mais cedo em empates
            if (upperMask == lowerMask && right - left + 1 > bestLen) {
                bestLen = right - left + 1;
                bestStart = left;
            }
        }
    }

    return s.substring(bestStart, bestStart + bestLen);
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

- Comparar caracteres um a um com `Set`/`toUpperCase` a cada substring funciona, mas é mais lento e menos direto do que comparar dois bitmasks inteiros — a comparação `upperMask == lowerMask` resume toda a condição em uma única operação O(1).
- Usar `>=` em vez de `>` ao atualizar o melhor resultado quebra a regra de "retornar a ocorrência mais cedo em caso de empate" — a primeira janela do maior tamanho encontrada deve ser mantida.
- Quando nenhuma substring nice existe, `bestLen` permanece `0`; `s.substring(bestStart, bestStart)` deve retornar `""` — não tratar isso como erro ou usar `-1` como sentinela sem cuidado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Uma única letra, sem par | `"c"` | "" | 'c' não tem sua contraparte de caixa em lugar nenhum |
| String inteira já nice | `"Bb"` | "Bb" | ambas as caixas de 'b' presentes, a string toda serve |
| Nice no meio da string | `"YazaAay"` | "aAa" | a maior janela válida está entre os índices 3 e 5 |
| Múltiplas letras, todas com par | `"AaBbCc"` | "AaBbCc" | toda letra tem as duas caixas, a string inteira é nice |

## 🔗 Conexões

- Problemas irmãos: [0003] Longest Substring Without Repeating Characters (mesma ideia de expandir uma janela e validar uma condição a cada caractere novo), [0076] Minimum Window Substring (mesma família de "expandir e checar uma condição sobre o conjunto de caracteres da janela", usando contadores em vez de bitmask)
- No backend: validar consistência de dados emparelhados dentro de uma janela de eventos — por exemplo, garantir que todo "abrir sessão" tenha um "fechar sessão" correspondente dentro de um trecho de log analisado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
