# [0205] Isomorphic Strings

> 🔗 [LeetCode 205](https://leetcode.com/problems/isomorphic-strings/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Dadas duas strings `s` e `t`, determine se são **isomórficas**: os caracteres de `s` podem ser substituídos para obter `t`, preservando a ordem, com a restrição de que a substituição é uma **bijeção** (nenhum caractere pode mapear para dois destinos diferentes, e nenhum destino pode receber dois caracteres diferentes).

**Exemplos:**
```
Input:  s = "egg", t = "add"   Output: true   ('e'->'a', 'g'->'d')
Input:  s = "f11", t = "b23"   Output: false  ('1' precisaria mapear para '2' E '3')
Input:  s = "paper", t = "title" Output: true
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 5 * 10^4` e `t.length == s.length` → força O(n): não há espaço para O(n²) real
- "consistem em qualquer caractere ASCII válido" → não dá para assumir só minúsculas; um array fixo de 26 não cobre tudo — hash map é mais seguro
- "nenhum caractere pode mapear para o mesmo" → **é isso que torna o problema uma bijeção**, e é o detalhe que a maioria esquece de verificar

## 🧭 Como reconhecer o padrão

Quando o problema fala em "mapear cada elemento de uma sequência para outra, sem repetir destino", é bijeção — e bijeção com hash map exige **duas direções de verificação**: `s[i] -> t[i]` E `t[i] -> s[i]`. Verificar só uma direção é o erro clássico desta categoria.

## 🐢 Solução 1 — Força bruta

Para cada posição `i`, comparar o padrão de ocorrência: verificar, com laços aninhados, se todas as posições onde `s[i]` aparece em `s` têm exatamente o mesmo caractere em `t`, e vice-versa.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** com n = 50.000, o quadrado estoura o tempo de execução. E a ideia de "conferir todas as ocorrências" é exatamente o que um hash map faz em O(1) por consulta.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha **dois mapas**: um traduzindo `s -> t` e outro traduzindo `t -> s`. Percorra as strings uma vez, caractere a caractere:
- Se `s[i]` já tem um destino mapeado, ele **precisa** ser `t[i]` — senão, false.
- Se `t[i]` já tem uma origem mapeada, ela **precisa** ser `s[i]` — senão, false.
- Se nenhum dos dois foi visto, registre o par nos dois mapas.

Os dois mapas juntos são o que garante a bijeção (um mapa sozinho só garante "função", não "bijeção").

## 🎬 Exemplo passo a passo

`s = "egg"`, `t = "add"` — testando isomorfismo

| i | s[i] | t[i] | s→t antes | t→s antes | Verificação | Ação |
|---|---|---|---|---|---|---|
| 0 | e | a | {} | {} | nenhum mapeado | registra e→a, a→e |
| 1 | g | d | {e:a} | {a:e} | nenhum mapeado | registra g→d, d→g |
| 2 | g | d | {e:a,g:d} | {a:e,d:g} | g→d já existe e bate; d→g já existe e bate | ok, continua |

Resultado final: **true** ✔ — todos os pares são consistentes nas duas direções.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada pelas strings, cada consulta de hash map é O(1)
- **Espaço:** O(k) — k = tamanho do alfabeto usado (no pior caso, O(n) se todos os caracteres forem distintos)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isIsomorphic(String s, String t) {
    Map<Character, Character> sParaT = new HashMap<>();
    Map<Character, Character> tParaS = new HashMap<>();

    for (int i = 0; i < s.length(); i++) {
        char cs = s.charAt(i);
        char ct = t.charAt(i);

        // checa a direção s -> t: cs já tem destino? precisa ser exatamente ct
        if (sParaT.containsKey(cs) && sParaT.get(cs) != ct) {
            return false;
        }
        // checa a direção t -> s: ct já tem origem? precisa ser exatamente cs
        // SEM ESTA CHECAGEM, "badc" mapeando de "aabb" passaria errado (não é bijeção)
        if (tParaS.containsKey(ct) && tParaS.get(ct) != cs) {
            return false;
        }

        sParaT.put(cs, ct);
        tParaS.put(ct, cs);
    }
    return true;
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

- **Usar só um mapa** (`s -> t`): passa em "egg"/"add" mas falha em casos como `s="ab"`, `t="aa"` — 'a'→'a' e 'b'→'a' não violam um único mapa de `s`, mas violam a bijeção porque dois caracteres mapeiam para o mesmo destino.
- **Java**: comparar `Character` com `!=` funciona para `char` primitivo dentro do `Map<Character,Character>` só porque o autoboxing de caracteres ASCII costuma cachear — mas é mais seguro usar `.equals()` ou comparar como `char` extraído.
- Esquecer que `s.length() == t.length()` é garantido pelo enunciado — não precisa verificar, mas não custa lembrar por que o loop é seguro.
- Achar que "mesma contagem de caracteres únicos" basta — não basta, a ORDEM e a correspondência posição a posição importam.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Bijeção simples | `s="egg", t="add"` | true | caso do enunciado |
| Um mapeia para dois | `s="foo", t="bar"` | false | 'o' precisaria virar 'a' e 'r' |
| Dois mapeiam para um (só 1 mapa detectaria errado) | `s="ab", t="aa"` | false | pega o erro do mapa único |
| Mesma string | `s="paper", t="paper"` | true | mapeamento identidade é válido |

## 🔗 Conexões

- Problemas irmãos: **[0290] Word Pattern** (mesma ideia de bijeção, mas caractere↔palavra em vez de caractere↔caractere), **[0242] Valid Anagram** (também compara duas strings, mas sem exigir bijeção posicional)
- No backend: validação de mapeamento 1-para-1 aparece em de-duplicação de chaves estrangeiras, migração de esquemas (garantir que cada ID antigo mapeia para exatamente um ID novo) e em detecção de aliasing de configuração.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
