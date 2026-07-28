# [0387] First Unique Character in a String

> 🔗 [LeetCode 387](https://leetcode.com/problems/first-unique-character-in-a-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#ArraysEHashing` `#Counting` `#Easy`

## 📜 O Problema

Dada uma string `s`, encontre o **primeiro** caractere que não se repete nela e retorne seu índice. Se ele não existir, retorne `-1`.

**Exemplos:**
```
Input:  s = "leetcode"
Output: 0
Explicação: o caractere 'l' no índice 0 é o primeiro que não ocorre em nenhum outro índice.

Input:  s = "loveleetcode"
Output: 2

Input:  s = "aabb"
Output: -1
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n²) (para cada caractere, varrer a string inteira contando) estoura; o esperado é O(n) ou próximo disso
- `s` consiste apenas de letras minúsculas do inglês → o alfabeto é fixo em 26 símbolos, o que permite trocar um hash map genérico por um **array de contagem de tamanho fixo** (mais rápido e sem overhead de hashing)

## 🧭 Como reconhecer o padrão

"Encontrar o primeiro elemento com uma certa propriedade de frequência" (aqui, "aparece exatamente uma vez") é a assinatura clássica de contagem por hashing: primeiro você precisa saber **quantas vezes** cada caractere aparece no total, e só depois consegue decidir, olhando a string de novo em ordem, qual é o primeiro que se qualifica. Isso é `01_arrays_e_hashing`, não stack: não há aninhamento nem ordem de "último a entrar, primeiro a sair" envolvida — é puramente sobre frequência.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i` da string, conte quantas vezes `s[i]` aparece em toda a string (varrendo `s` de novo). O primeiro índice cuja contagem for exatamente 1 é a resposta.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** para `n = 10^5`, recontar a string inteira para cada um dos `n` caracteres significa até 10^10 operações — impraticável dentro do limite de tempo. O trabalho de contar está sendo refeito do zero a cada posição, quando poderia ser feito uma única vez e reaproveitado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Separe o problema em duas passadas independentes, cada uma O(n):

1. **Primeira passada:** percorra `s` uma vez e conte a frequência de cada caractere num array de tamanho 26 (índice `c - 'a'`).
2. **Segunda passada:** percorra `s` de novo, em ordem, e retorne o índice do primeiro caractere cuja contagem no array é exatamente 1.

A chave é que a primeira passada já sabe o "resultado final" de frequência de cada letra antes da segunda passada começar a decidir — assim você nunca precisa "olhar para frente" durante a decisão.

## 🎬 Exemplo passo a passo

`s = "loveleetcode"` (índices 0 a 11: `l,o,v,e,l,e,e,t,c,o,d,e`)

| Passo | Ação | Estado |
|---|---|---|
| 1 | 1ª passada: conta frequências | `l:2, o:2, v:1, e:4, t:1, c:1, d:1` |
| 2 | 2ª passada, índice 0 (`l`) | contagem de `l` é 2 → não é único, continua |
| 3 | índice 1 (`o`) | contagem de `o` é 2 → não é único, continua |
| 4 | índice 2 (`v`) | contagem de `v` é 1 → **único!** retorna `2` |

Resultado final: `2` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas lineares independentes pela string (2n ainda é O(n))
- **Espaço:** O(1) — o array de contagem tem tamanho fixo 26, independente do tamanho de `s`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int firstUniqChar(String s) {
    int[] freq = new int[26]; // alfabeto fixo: array bate hash map em velocidade e simplicidade

    // 1ª passada: conta a frequência total de cada letra
    for (int i = 0; i < s.length(); i++) {
        freq[s.charAt(i) - 'a']++;
    }

    // 2ª passada: primeira letra cuja frequência total é 1
    for (int i = 0; i < s.length(); i++) {
        if (freq[s.charAt(i) - 'a'] == 1) {
            return i;
        }
    }

    return -1; // nenhum caractere único encontrado
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

- Tentar decidir a unicidade numa **única** passada sem pré-computar as frequências — na primeira vez que você vê um caractere, ainda não sabe se ele vai se repetir mais adiante na string; por isso as duas passadas são necessárias (ou uma estrutura que rastreie "ainda não sei", como uma fila de candidatos).
- Usar `HashMap<Character, Integer>` em vez de `int[26]` — funciona, mas é mais lento (hashing de objetos `Character`, boxing/unboxing) para um alfabeto tão pequeno e fixo.
- Esquecer o `-1` quando nenhum caractere é único — em `"aabb"`, toda letra se repete, e a segunda passada nunca encontra `freq == 1`; o loop precisa de um retorno padrão fora dele.
- Confundir "índice do caractere" com "quantidade de caracteres únicos" — a resposta é a **posição** do primeiro caractere não repetido, não quantos existem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhum único | `"aabb"` | -1 | toda letra aparece pelo menos 2 vezes |
| Único é o primeiro caractere | `"leetcode"` | 0 | já cobre o caso feliz mais simples |
| Único no meio | `"loveleetcode"` | 2 | testa que a busca não para no primeiro índice, e sim no primeiro que atende à condição |
| String de um único caractere | `"z"` | 0 | caractere sozinho é trivialmente único |

## 🔗 Conexões

- Problemas irmãos: [0242] Valid Anagram (mesma técnica de array de contagem de 26 posições), [0169] Majority Element (outra decisão baseada em frequência, mas buscando o elemento MAIS frequente em vez do primeiro único)
- No backend: contagem de frequência com array/hash fixo é a base de deduplicação e de detecção de eventos "únicos" em streams de dados (ex.: identificar o primeiro request não-repetido num log, ou a primeira ocorrência de um valor sem duplicata numa tabela antes de aplicar uma constraint UNIQUE).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
