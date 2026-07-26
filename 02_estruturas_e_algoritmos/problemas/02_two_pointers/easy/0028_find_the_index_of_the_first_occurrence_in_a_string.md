# [0028] Find the Index of the First Occurrence in a String

> 🔗 [LeetCode 28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#StringMatching` `#Easy`

## 📜 O Problema

Dadas duas strings `needle` e `haystack`, retorne o índice da **primeira ocorrência** de `needle` dentro de `haystack`, ou `-1` se `needle` não aparecer.

**Exemplos:**
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explicação: "sad" ocorre nos índices 0 e 6. A primeira é no 0.

Input:  haystack = "leetcode", needle = "leeto"
Output: -1
Explicação: "leeto" não aparece em "leetcode".
```

**Restrições (e o que elas denunciam):**
- `1 <= haystack.length, needle.length <= 10^4` → uma solução O(n·m) ingênua pode chegar a 10^8 comparações no pior caso; boa parte da otimização aqui é evitar desperdício de espaço/tempo em cada tentativa, não necessariamente baixar a ordem de grandeza
- `haystack` e `needle` só têm letras minúsculas → sem necessidade de normalizar case ou tratar caracteres especiais
- `needle` pode ser **maior** que `haystack` → nesse caso não há posição inicial válida, a resposta é sempre -1

## 🧭 Como reconhecer o padrão

"Procurar uma string dentro de outra, posição por posição" é resolvido com dois ponteiros: um ponteiro externo `i` marca onde a tentativa de casamento começa em `haystack`, e um ponteiro interno `j` avança comparando `haystack[i+j]` com `needle[j]` enquanto os caracteres coincidem, parando no primeiro mismatch (sem alocar substrings novas a cada tentativa).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição inicial `i` de 0 até `haystack.length - needle.length`, extrair a substring `haystack.substring(i, i + needle.length)` e comparar com `needle` usando igualdade de strings.

- Tempo: O(n·m) · Espaço: O(m) por tentativa — `substring()` cria uma cópia nova de até `m` caracteres em cada uma das até `n-m+1` tentativas
- **Por que não basta:** além do tempo já ser O(n·m) no pior caso, cada tentativa aloca uma string nova só para comparar e descartar — desperdício de espaço que a versão com dois ponteiros elimina comparando caractere a caractere direto no `haystack` original.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mesma ideia da força bruta, mas sem criar substrings: para cada posição inicial `i`, use um ponteiro `j` que compara `haystack[i+j]` com `needle[j]` um caractere por vez. Se `j` chegar ao fim de `needle` sem mismatch, `i` é a resposta. Se houver mismatch, descarta essa tentativa **sem alocar nada** e tenta o próximo `i`. Isso corta o trabalho na primeira diferença (early exit), em vez de comparar strings inteiras.

## 🎬 Exemplo passo a passo

`haystack = "leetcode"` (n=8), `needle = "leeto"` (m=5), tentativas de `i = 0` até `i = n - m = 3`

| Passo | i (posição inicial) | Comparação caractere a caractere | j alcançado | Resultado |
|---|---|---|---|---|
| 1 | 0 | l-l, e-e, e-e, t-t, depois `c` ≠ `o` | 4 | mismatch em j=4, tenta próximo i |
| 2 | 1 | `e` ≠ `l` | 0 | mismatch imediato |
| 3 | 2 | `e` ≠ `l` | 0 | mismatch imediato |
| 4 | 3 | `t` ≠ `l` | 0 | mismatch imediato; i+1=4 já passa do limite (n-m=3) |

Nenhum `i` fez `j` alcançar `m=5` → retorna `-1` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n·m) no pior caso (ex.: `haystack = "aaaaaaaaab"`, `needle = "aaab"` quase sempre avança quase todo `needle` antes de falhar); na prática, com textos comuns, o mismatch costuma vir logo no início de cada tentativa, ficando perto de O(n)
- **Espaço:** O(1) — nenhuma substring é criada, só os índices `i` e `j`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int strStr(String haystack, String needle) {
    int n = haystack.length();
    int m = needle.length();

    for (int i = 0; i <= n - m; i++) { // <= n-m: precisa sobrar espaço pro needle inteiro
        int j = 0;
        // avança j enquanto os caracteres, a partir de i, continuam coincidindo
        while (j < m && haystack.charAt(i + j) == needle.charAt(j)) {
            j++;
        }
        if (j == m) { // percorreu needle inteiro sem mismatch: achou
            return i;
        }
        // mismatch: descarta esta tentativa (sem alocar nada) e passa pro próximo i
    }

    return -1;
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

- Achar que essa técnica de dois ponteiros já é O(n) no pior caso — não é: ela é O(n·m). Garantir O(n+m) de verdade exige o algoritmo KMP (usa uma tabela de prefixos para nunca "voltar" o ponteiro de `haystack` depois de um mismatch parcial) — otimização fora do escopo de dois ponteiros simples, mas importante saber que ela existe.
- Usar `i < n` como limite do loop externo em vez de `i <= n - m` — se `needle` for maior que o espaço restante em `haystack`, `haystack.charAt(i + j)` explode com índice fora dos limites.
- Não considerar `needle.length() > haystack.length()` — nesse caso `n - m` é negativo, e o loop externo simplesmente não deve executar nenhuma vez (a condição `i <= n - m` já cobre isso corretamente se `n - m` for tratado como `int`, sem cast para tipo sem sinal).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ocorrência no início | `haystack="sadbutsad"`, `needle="sad"` | 0 | primeiro casamento completo já em i=0 |
| Needle ausente | `haystack="leetcode"`, `needle="leeto"` | -1 | nenhum i completa o casamento até o fim |
| Needle == haystack | `haystack="a"`, `needle="a"` | 0 | caso mínimo, m=n, casa na única posição possível |
| Needle maior que haystack | `haystack="ab"`, `needle="abc"` | -1 | `n - m` é negativo, loop externo não executa |

## 🔗 Conexões

- Problemas irmãos: [0459] Repeated Substring Pattern (mesma família de casamento de padrão em string), [0187] Repeated DNA Sequences (também compara janelas de string, mas via sliding window + hashing em vez de comparação direta)
- No backend: é a base de qualquer busca de substring "na mão" — validar se um token aparece dentro de um payload maior, ou implementar um `contains()` simplificado; os motores reais de `String.indexOf`/`Contains` das linguagens usam variantes otimizadas (Boyer-Moore, Two-Way) do mesmo problema.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
