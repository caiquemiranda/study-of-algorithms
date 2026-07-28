# [2696] Minimum String Length After Removing Substrings

> 🔗 [LeetCode 2696](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Simulation`

## 📜 O Problema

Você recebe uma string `s` composta só por letras **maiúsculas** do inglês. Em uma operação, você pode remover **qualquer** ocorrência das substrings `"AB"` ou `"CD"` de `s`. Retorne o **menor comprimento possível** da string resultante.

**Nota:** a string concatena após a remoção e pode produzir novas substrings `"AB"` ou `"CD"`.

**Exemplos:**
```
Input:  s = "ABFCACDB"
Output: 2
Explicação:
- Remove "AB" de "ABFCACDB" → "FCACDB"
- Remove "CD" de "FCACDB" → "FCAB"
- Remove "AB" de "FCAB" → "FC"
Comprimento final: 2.

Input:  s = "ACBBD"
Output: 5
Explicação: não é possível fazer nenhuma operação, o comprimento continua o mesmo.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → tamanho minúsculo, qualquer solução O(n) é folgada
- `s` consiste só de letras maiúsculas do inglês → não há necessidade de tratar minúsculas ou outros símbolos

## 🧭 Como reconhecer o padrão

Igual a [1047] e [1544], "remover repetidamente um par/substring adjacente que satisfaz uma condição, onde a remoção pode expor uma **nova** ocorrência que também precisa ser avaliada" é a assinatura de stack: o candidato a formar `"AB"` ou `"CD"` com o caractere atual é sempre o **último caractere ainda não cancelado** — o topo da pilha.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Repetidamente procurar na string a primeira ocorrência de `"AB"` ou `"CD"`, removê-la (reconstruindo a string), e recomeçar a busca do zero até nenhuma ocorrência ser encontrada.

- Tempo: O(n²) pior caso · Espaço: O(n) por cópia
- **Por que não basta:** cada remoção pode expor uma nova ocorrência que só aparece depois da concatenação (como no exemplo, onde remover `"AB"` expõe depois um `"CD"`), forçando uma nova varredura completa a cada remoção. Mesmo com `n <= 100` isso passaria, mas a solução com pilha resolve em uma única passada, sem reconstruir a string repetidamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` uma única vez com uma pilha. Para cada caractere: se o topo da pilha, junto com o caractere atual, formar `"AB"` (topo é `'A'` e atual é `'B'`) ou `"CD"` (topo é `'C'` e atual é `'D'`), isso é uma ocorrência a remover — desempilhe o topo (sem empilhar o atual, cancelando os dois). Caso contrário, empilhe o caractere atual. A pilha naturalmente lida com o efeito cascata: quando um par é removido, o caractere que ficou exposto por baixo (o novo topo) pode formar um novo par com o próximo caractere processado. No final, o tamanho da pilha é a resposta.

## 🎬 Exemplo passo a passo

`s = "ABFCACDB"`

| Passo | Caractere | Compara com topo | Ação | Pilha após |
|---|---|---|---|---|
| 1 | `A` | pilha vazia | empilha | `[A]` |
| 2 | `B` | topo `A` + `B` = "AB" → cancela | desempilha | `[]` |
| 3 | `F` | pilha vazia | empilha | `[F]` |
| 4 | `C` | topo `F` + `C`, não é par | empilha | `[F, C]` |
| 5 | `A` | topo `C` + `A`, não é par | empilha | `[F, C, A]` |
| 6 | `C` | topo `A` + `C`, não é par | empilha | `[F, C, A, C]` |
| 7 | `D` | topo `C` + `D` = "CD" → cancela | desempilha | `[F, C, A]` |
| 8 | `B` | topo `A` + `B` = "AB" → cancela | desempilha | `[F, C]` |

Resultado final: pilha `[F, C]`, comprimento `2` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere é empilhado e desempilhado no máximo uma vez
- **Espaço:** O(n) — pior caso (nenhuma substring removível), todos os caracteres ficam na pilha

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minLength(String s) {
    Deque<Character> pilha = new ArrayDeque<>();

    for (char c : s.toCharArray()) {
        if (!pilha.isEmpty() && ((pilha.peek() == 'A' && c == 'B')
                               || (pilha.peek() == 'C' && c == 'D'))) {
            pilha.pop();          // cancela o par "AB" ou "CD"
        } else {
            pilha.push(c);
        }
    }

    return pilha.size(); // não precisa reconstruir a string, só o tamanho final é pedido
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

- Checar só se o caractere atual é `'B'` ou `'D'`, sem confirmar o caractere do topo correspondente — `"BA"` não é uma ocorrência de `"AB"` (a ordem importa: precisa ser exatamente topo=`'A'` seguido de atual=`'B'`, não o contrário).
- Esquecer de checar `pilha.isEmpty()` antes de comparar com o topo — no primeiro caractere, ou logo após um cancelamento que esvazia a pilha, comparar com uma pilha vazia lança exceção.
- Tentar detectar `"AB"`/`"CD"` só olhando pares de índices fixos na string original (`s[i]` e `s[i+1]`) sem uma estrutura de pilha — isso falha no efeito cascata do enunciado, onde remover uma ocorrência pode expor uma nova que não era adjacente originalmente (exatamente o que acontece no exemplo `"ABFCACDB"`).
- Confundir esta técnica com contagem simples de ocorrências de `"AB"` e `"CD"` na string original — a resposta depende do efeito cascata, não é só `len(s) - 2 * (contagem de "AB" + contagem de "CD")` na string original.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Cancelamento em cascata | `"ABFCACDB"` | 2 | remover "CD" expõe um novo "AB" que não existia antes |
| Nenhuma remoção possível | `"ACBBD"` | 5 | não há "AB" nem "CD" em nenhum momento, string retorna intacta |
| String inteira se cancela | `"ABCD"` seguida de recombinação (ex.: `"ABCDAB"`) | menor que o original | testa múltiplos cancelamentos sequenciais sem sobreposição |
| Só `'A'`s e `'B'`s alternados de forma não cancelável | `"BABA"` | 4 | `"BA"` não é uma substring alvo (só "AB" e "CD" contam), nada é removido |

## 🔗 Conexões

- Problemas irmãos: [1047] Remove All Adjacent Duplicates In String (mesma técnica de cancelamento com pilha, mas o par é qualquer caractere igual ao adjacente), [1544] Make The String Great (cancelamento com pilha onde o par é a mesma letra em cases opostos)
- No backend: cancelamento em cascata de padrões fixos de 2 caracteres aparece em simplificação de expressões (ex.: operadores que se anulam como `"+-"` → nada), em parsers de protocolos binários que colapsam sequências de escape, e em qualquer pipeline de normalização de texto com regras de substituição que podem se encadear.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
