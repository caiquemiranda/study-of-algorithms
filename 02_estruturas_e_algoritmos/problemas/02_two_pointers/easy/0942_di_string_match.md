# [0942] DI String Match

> 🔗 [LeetCode 942](https://leetcode.com/problems/di-string-match/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#String` `#Easy`

## 📜 O Problema

Uma permutação `perm` de `n+1` inteiros (`0` a `n`) pode ser representada por uma string `s` de tamanho `n`, onde `s[i] == 'I'` se `perm[i] < perm[i+1]`, e `s[i] == 'D'` se `perm[i] > perm[i+1]`. Dada `s`, reconstrua **qualquer** permutação válida.

**Exemplos:**
```
Input:  s = "IDID"
Output: [0,4,1,3,2]

Input:  s = "III"
Output: [0,1,2,3]

Input:  s = "DDI"
Output: [3,2,0,1]
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n) esperado
- `s[i]` é `'I'` ou `'D'` → só duas decisões possíveis por posição, o que sugere uma construção gulosa direta em vez de busca
- Aceita **qualquer** permutação válida → existe liberdade de escolha; não precisa ser a única solução "correta"

## 🧭 Como reconhecer o padrão

"Construir uma sequência que satisfaz uma relação de ordem local (maior/menor que o vizinho) usando cada valor uma única vez" é resolvido gulosamente com dois ponteiros nos **extremos** dos valores disponíveis: um marcando o menor valor ainda não usado, outro o maior. Um `'I'` sempre pode usar o menor disponível (garante que o próximo seja maior); um `'D'` sempre pode usar o maior disponível (garante que o próximo seja menor).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar todas as permutações possíveis de `[0..n]` e testar, para cada uma, se ela satisfaz a sequência de `'I'`/`'D'` do enunciado.

- Tempo: O((n+1)! × n) — o espaço de busca cresce fatorialmente · Espaço: O(n) por permutação testada
- **Por que não basta:** o espaço de busca explode mesmo para `n` pequeno; como o problema aceita **qualquer** permutação válida, existe uma construção direta (gulosa) que nunca precisa buscar ou validar nada depois de pronta.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `low = 0` e `high = n`, representando o menor e o maior valor ainda não usados. Percorra `s`: se o caractere for `'I'`, use `low` na posição atual e avance `low` (o próximo valor, seja ele qual for, será maior); se for `'D'`, use `high` e recue `high` (o próximo será menor). Ao final, sobra exatamente um valor (`low == high` nesse ponto) para a última posição da permutação.

## 🎬 Exemplo passo a passo

`s = "IDID"` (n=4), `low` começa em 0, `high` em 4

| Passo | i | s[i] | Ação | perm parcial | low depois | high depois |
|---|---|---|---|---|---|---|
| 1 | 0 | `I` | `perm[0] = low(0)` | `[0]` | 1 | 4 |
| 2 | 1 | `D` | `perm[1] = high(4)` | `[0,4]` | 1 | 3 |
| 3 | 2 | `I` | `perm[2] = low(1)` | `[0,4,1]` | 2 | 3 |
| 4 | 3 | `D` | `perm[3] = high(3)` | `[0,4,1,3]` | 2 | 2 |
| 5 | fim | — | `perm[4] = low (= high = 2)` | `[0,4,1,3,2]` | — | — |

Resultado final: `[0,4,1,3,2]` ✔ (bate exatamente com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada por `s`, cada posição decide entre `low` e `high` em O(1)
- **Espaço:** O(n) para o array de resposta (exigido pelo problema); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] diStringMatch(String s) {
    int n = s.length();
    int[] perm = new int[n + 1];
    int low = 0;
    int high = n;

    for (int i = 0; i < n; i++) {
        if (s.charAt(i) == 'I') {
            perm[i] = low++; // menor valor disponível: garante perm[i] < próximo
        } else {
            perm[i] = high--; // maior valor disponível: garante perm[i] > próximo
        }
    }
    perm[n] = low; // sobra um único valor no final, e low == high nesse ponto

    return perm;
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

- Tentar montar a permutação sequencialmente (`0,1,2,3,...`) e "corrigir" depois — sem a estratégia gulosa de menor/maior disponível, fica muito mais difícil garantir a comparação certa em toda posição sem backtracking.
- Esquecer o último elemento (`perm[n] = low`) — o loop só preenche `n` posições (`s.length()`), mas a permutação tem `n+1` elementos; sobra sempre um valor no final.
- Achar que precisa validar a permutação gerada — a construção gulosa garante corretude por definição (cada escolha já satisfaz a comparação exigida com a próxima), não há necessidade de checagem posterior.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Alternado | `"IDID"` | `[0,4,1,3,2]` | mistura de crescente/decrescente |
| Só crescente | `"III"` | `[0,1,2,3]` | só o ponteiro `low` é usado |
| Só decrescente (com uma exceção) | `"DDI"` | `[3,2,0,1]` | inverte no final com um único `'I'` |
| Caractere único | `"I"` | `[0,1]` | menor permutação possível, n=1 |

## 🔗 Conexões

- Problemas irmãos: [0031] Next Permutation (também constrói uma permutação respeitando uma relação de ordem entre elementos vizinhos), [0556] Next Greater Element III (mesma família de manipular posições respeitando uma comparação local)
- No backend: geração gulosa de sequências que satisfazem restrições locais de ordem — por exemplo, montar um cronograma onde cada item precisa ser maior/menor que o anterior, sem precisar buscar entre todas as combinações possíveis.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
