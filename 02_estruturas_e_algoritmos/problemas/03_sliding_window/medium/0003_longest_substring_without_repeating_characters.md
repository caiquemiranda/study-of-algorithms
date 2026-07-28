# [0003] Longest Substring Without Repeating Characters

> 🔗 [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Dada uma string `s`, encontre o comprimento da **maior substring** sem caracteres duplicados.

**Exemplos:**
```
Input:  s = "abcabcbb"
Output: 3
Explicação: a resposta é "abc", de comprimento 3.

Input:  s = "bbbbb"
Output: 1
Explicação: a resposta é "b", de comprimento 1.

Input:  s = "pwwkew"
Output: 3
Explicação: a resposta é "wke". Note que "pwke" é subsequência, não substring, e não conta.
```

**Restrições (e o que elas denunciam):**
- `0 <= s.length <= 5 * 10^4` → O(n²) força bruta é arriscado nesse tamanho; O(n) é o esperado
- `s` consiste em letras, dígitos, símbolos e espaços → alfabeto amplo demais para um array fixo de 26 posições; um `HashMap` (ou array indexado pelo código ASCII/Unicode) é a estrutura certa

## 🧭 Como reconhecer o padrão

"Maior substring sem caracteres repetidos" é o exemplo mais canônico de janela deslizante **variável**: expande-se a janela pela direita; quando um caractere repetido aparece dentro da janela atual, a janela encolhe pela esquerda até logo depois da última ocorrência desse caractere — sem nunca recomeçar do zero.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, checar se a substring `s[left..right]` tem todos os caracteres únicos usando um `Set` criado do zero.

- Tempo: O(n³) (O(n²) substrings, O(n) para checar cada uma) · Espaço: O(min(n, charset))
- **Por que não basta:** recomputa a checagem de unicidade do zero a cada substring candidata, sem aproveitar que substrings vizinhas compartilham quase todos os caracteres.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um mapa `lastSeen` com o último índice onde cada caractere apareceu. Ao processar `s[right]`, se ele já apareceu **dentro da janela atual** (`lastSeen[c] >= left`), mova `left` para `lastSeen[c] + 1`. Atualize `lastSeen[c] = right` e o melhor comprimento (`right - left + 1`).

## 🎬 Exemplo passo a passo

`s = "pwwkew"` (índices: p0 w1 w2 k3 e4 w5)

| right | char | lastSeen[char] antes | left antes | left depois | comprimento | melhor |
|---|---|---|---|---|---|---|
| 0 | p | — | 0 | 0 | 1 | 1 |
| 1 | w | — | 0 | 0 | 2 | 2 |
| 2 | w | 1 | 0 | 2 (1+1) | 1 | 2 |
| 3 | k | — | 2 | 2 | 2 | 2 |
| 4 | e | — | 2 | 2 | 3 | 3 |
| 5 | w | 2 | 2 | 3 (2+1) | 3 | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `right` percorre a string uma vez; `left` só avança, nunca retrocede
- **Espaço:** O(min(n, charset)) para o mapa de últimas ocorrências

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> lastSeen = new HashMap<>();
    int left = 0;
    int best = 0;

    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        if (lastSeen.containsKey(c) && lastSeen.get(c) >= left) {
            left = lastSeen.get(c) + 1; // pula pra depois da última ocorrência dentro da janela
        }
        lastSeen.put(c, right);
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

- Mover `left` para `lastSeen[c] + 1` mesmo quando a última ocorrência de `c` está FORA da janela atual (antes de `left`) faz `left` retroceder incorretamente — sempre checar `lastSeen[c] >= left` antes de atualizar.
- Usar apenas um `Set` (sem guardar a posição) obriga a remover elementos um a um do início até o duplicado sumir, virando O(n) por remoção no pior caso; guardar o ÍNDICE da última ocorrência permite pular direto, O(1) amortizado.
- String vazia (`s.length() == 0`, permitido pelas restrições) deve retornar `0` — o loop simplesmente não executa, e `best` permanece `0` por padrão.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| String vazia | `""` | 0 | nenhum caractere para formar substring |
| Todos os caracteres iguais | `"bbbbb"` | 1 | qualquer caractere sozinho já é a maior substring sem repetição |
| Sem nenhuma repetição | `"abcabcbb"` | 3 | "abc" é a maior substring sem duplicatas |
| Repetição fora da janela atual | `"pwwkew"` | 3 | "wke" é a resposta; "pwke" pareceria maior mas não é substring contígua válida |

## 🔗 Conexões

- Problemas irmãos: [0159] Longest Substring with At Most Two Distinct Characters (mesma técnica, generalizando o limite de 0 para até 2 caracteres distintos), [0076] Minimum Window Substring (mesma família de janela variável com mapa de última ocorrência/contagem, buscando o extremo oposto — a MENOR janela que CONTÉM algo, em vez da MAIOR que EVITA algo)
- No backend: detectar a maior janela de tempo sem eventos duplicados num stream de logs — por exemplo, o maior intervalo sem repetição de um mesmo código de erro consecutivo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
