# [0242] Valid Anagram

> 🔗 [LeetCode 242](https://leetcode.com/problems/valid-anagram/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Sorting` `#Easy`

## 📜 O Problema

Dadas duas strings `s` e `t`, retorne `true` se `t` é um **anagrama** de `s` (mesmas letras, mesma quantidade de cada uma, ordem qualquer).

**Exemplos:**
```
Input:  s = "anagram", t = "nagaram"   Output: true
Input:  s = "rat", t = "car"           Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length, t.length <= 5 * 10^4` → precisa de O(n) ou O(n log n); força bruta comparando permutações está fora de cogitação
- "`s` e `t` consistem em letras minúsculas do inglês" → só 26 possibilidades, o que habilita um **array de contagem fixo de tamanho 26** em vez de hash map genérico (mais rápido na prática)
- Follow-up ("e se fossem caracteres Unicode?") → sinaliza que a solução com array fixo de 26 não generaliza; para Unicode, hash map é a resposta certa

## 🧭 Como reconhecer o padrão

"São anagramas?" é o exemplo mais clássico de **mapa de frequência**: se dois conjuntos de contagem de caracteres são idênticos, as strings são anagramas — não importa a ordem.

## 🐢 Solução 1 — Força bruta

Ordenar as duas strings (transformando em array de caracteres, ordenando, e comparando).

- Tempo: O(n log n) · Espaço: O(n) para os arrays intermediários
- **Por que não é a ideal:** funciona e já passa nas constraints, mas existe uma solução linear que evita pagar o custo da ordenação — é a diferença entre "resolveu" e "resolveu com o padrão certo".

## 💡 Solução 2 — A ideia otimizada (intuição)

Se os tamanhos diferem, já não são anagramas — descarte na hora. Senão, percorra `s` **incrementando** a contagem de cada letra e `t` **decrementando** simultaneamente, usando um único array de 26 posições. Se ao final todas as posições estão em zero, as contagens bateram perfeitamente.

## 🎬 Exemplo passo a passo

`s = "rat"`, `t = "car"` (tamanhos iguais: 3 e 3)

| Passo | letra de s | contagem[letra]++ | letra de t | contagem[letra]-- | contagem parcial (r,a,t,c) |
|---|---|---|---|---|---|
| 1 | r | +1 | c | -1 | r:1, c:-1 |
| 2 | a | +1 | a | -1 | r:1, a:0, c:-1 |
| 3 | t | +1 | r | -1 | r:0, a:0, t:1, c:-1 |

Ao final, `t:1` e `c:-1` **não são zero** → **false** ✔ ('t' sobrou de `s`, 'c' sobrou de `t` — letras diferentes)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas lineares (uma por string), cada acesso ao array é O(1)
- **Espaço:** O(1) — o array de contagem tem tamanho fixo (26), não cresce com a entrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false; // tamanhos diferentes: impossível ser anagrama, nem vale a pena contar
    }

    int[] contagem = new int[26]; // só letras minúsculas: 'a' a 'z'

    for (int i = 0; i < s.length(); i++) {
        contagem[s.charAt(i) - 'a']++; // soma a presença de cada letra de s
        contagem[t.charAt(i) - 'a']--; // subtrai a presença de cada letra de t no MESMO array
    }

    // se s e t têm exatamente as mesmas letras nas mesmas quantidades, tudo cancela para 0
    for (int c : contagem) {
        if (c != 0) return false;
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

- Esquecer de checar `s.length() != t.length()` antes de tudo — sem isso, `"aab"` vs `"ab"` pode gerar comportamento incorreto ou índice fora do array.
- **Java**: `s.charAt(i) - 'a'` só funciona corretamente se a string tiver garantidamente letras minúsculas — para o follow-up com Unicode, isso quebra e é preciso trocar para `HashMap<Character, Integer>`.
- Usar dois arrays separados (um para `s`, outro para `t`) e depois comparar — funciona, mas gasta o dobro de memória sem necessidade; um único array com incremento/decremento é mais elegante.
- **Python**: lembrar que `Counter(s) == Counter(t)` já resolve isso de forma idiomática — mas em entrevista, saiba explicar o que acontece por baixo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Anagrama simples | `s="anagram", t="nagaram"` | true | caso do enunciado |
| Tamanhos diferentes | `s="ab", t="a"` | false | pega direto no primeiro check |
| Mesmas letras, quantidades diferentes | `s="aab", t="abb"` | false | testa que CONTAGEM importa, não só quais letras existem |
| Strings idênticas | `s="abc", t="abc"` | true | caso trivial (toda string é anagrama de si mesma) |

## 🔗 Conexões

- Problemas irmãos: **[0049] Group Anagrams** (agrupar vários anagramas usando a mesma ideia de "chave canônica" de contagem), **[0438] Find All Anagrams in a String** (combina esta ideia com sliding window)
- No backend: comparação de assinaturas de dados (ex.: verificar se dois payloads têm os mesmos campos, sem se importar com a ordem de serialização JSON) e detecção de mensagens duplicadas com campos reordenados usam frequência de elementos da mesma forma.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
