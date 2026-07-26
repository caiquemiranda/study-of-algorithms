# [0859] Buddy Strings

> 🔗 [LeetCode 859](https://leetcode.com/problems/buddy-strings/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Dadas duas strings `s` e `goal`, retorne `true` se você pode trocar duas letras em `s` de forma que o resultado seja igual a `goal`; caso contrário, retorne `false`.

Trocar letras é definido como escolher dois índices `i` e `j` (0-indexed) tal que `i != j` e trocar os caracteres em `s[i]` e `s[j]`.

**Exemplos:**
```
Input:  s = "ab", goal = "ba"
Output: true
Explicação: você pode trocar s[0]='a' e s[1]='b' para obter "ba", igual a goal.

Input:  s = "ab", goal = "ab"
Output: false
Explicação: as únicas letras que você pode trocar são s[0]='a' e s[1]='b', resultando em "ba" != goal.

Input:  s = "aa", goal = "aa"
Output: true
Explicação: você pode trocar s[0]='a' e s[1]='a' para obter "aa", igual a goal.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length, goal.length <= 2×10^4` → precisa O(n), não O(n²)
- letras minúsculas apenas → sem complicação de caixa
- precisa que EXATAMENTE um swap (de índices diferentes) transforme `s` em `goal`

## 🧭 Como reconhecer o padrão

"Um único swap pode transformar A em B" é resolvido comparando as strings posição a posição: se os tamanhos diferem, é impossível; se são iguais e diferem em exatamente 2 posições que, trocadas, batem, funciona; se são idênticas, só funciona se houver uma letra duplicada em `s` (permitindo um "swap fantasma" que não muda nada).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar todos os pares possíveis de índices `(i, j)`, fazer o swap em `s`, e comparar o resultado com `goal`.

- Tempo: O(n³) — O(n²) pares de índices, cada comparação de string custa O(n) · Espaço: O(n) por string gerada
- **Por que não basta:** gera e descarta n² strings inteiras quando a resposta pode ser decidida observando só as posições onde `s` e `goal` diferem, sem nunca construir a string trocada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se `len(s) != len(goal)`, retorne `false`. Se `s == goal`, só é possível se existir letra repetida em `s` (via hash set: se o set de caracteres for menor que `len(s)`, há repetição). Caso contrário, encontre os índices onde `s[i] != goal[i]`; se houver exatamente 2 dessas posições e trocar os caracteres nelas faz `s` virar `goal`, retorne `true`.

## 🎬 Exemplo passo a passo

`s = "ab"`, `goal = "ba"`

| Passo | Verificação | Resultado |
|---|---|---|
| 1 | len(s) == len(goal)? | sim (2 == 2) |
| 2 | s == goal? | não |
| 3 | índices onde s[i] != goal[i] | [0, 1] |
| 4 | exatamente 2 diferenças? | sim |
| 5 | s[0]==goal[1] e s[1]==goal[0]? | 'a'=='a' ✓, 'b'=='b' ✓ |

Resultado final: `true` ✔ (trocar índices 0 e 1 em "ab" dá "ba")

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma ou duas passadas lineares
- **Espaço:** O(1) extra (fora o hash set de até 26 letras no caso de strings iguais)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean buddyStrings(String s, String goal) {
    if (s.length() != goal.length()) {
        return false;
    }

    if (s.equals(goal)) {
        // só funciona se houver letra repetida: o swap pode trocar duas ocorrências iguais entre si
        Set<Character> vistos = new HashSet<>();
        for (char c : s.toCharArray()) {
            if (!vistos.add(c)) {
                return true; // achou uma repetição
            }
        }
        return false;
    }

    List<Integer> diferencas = new ArrayList<>();
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) != goal.charAt(i)) {
            diferencas.add(i);
            if (diferencas.size() > 2) {
                return false; // mais de 2 diferenças, nenhum swap único resolve
            }
        }
    }

    if (diferencas.size() != 2) {
        return false; // 0 ou 1 diferença (com s != goal) nunca é resolvível com 1 swap
    }

    int i = diferencas.get(0);
    int j = diferencas.get(1);
    return s.charAt(i) == goal.charAt(j) && s.charAt(j) == goal.charAt(i);
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

- Esquecer o caso `s == goal` — parece que "nenhum swap é necessário", mas o enunciado exige um swap de fato (índices diferentes), então só funciona se houver letra duplicada para "trocar consigo mesma" sem mudar o resultado.
- Não checar `len(s) != len(goal)` antes de comparar caractere a caractere — acessar índices fora dos limites gera exceção.
- Achar que qualquer número de diferenças "≤ 2" funciona — só exatamente 2 diferenças (com as letras cruzadas batendo) é resolvível; 1 diferença sozinha nunca é (um swap sempre afeta 2 posições).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Swap simples resolve | `s="ab", goal="ba"` | true | trocar os 2 únicos índices resolve |
| Strings já iguais, sem duplicata | `s="ab", goal="ab"` | false | não há letra repetida para "swap fantasma" |
| Strings já iguais, com duplicata | `s="aa", goal="aa"` | true | trocar as duas posições de 'a' não muda nada, mas é um swap válido |
| Mais de 2 diferenças | `s="abcd", goal="badc"` | false | 4 posições diferem, um único swap não corrige todas |

## 🔗 Conexões

- Problemas irmãos: [0242] Valid Anagram (mesmo domínio de comparação de strings por conteúdo), [0796] Rotate String (mesma família de "uma operação transforma A em B")
- No backend: validação de proximidade entre strings (ex.: detectar erros de digitação de "2 caracteres trocados de lugar" em campos de formulário, como um código de produto digitado com dois dígitos invertidos).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
