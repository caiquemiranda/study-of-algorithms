# [0392] Is Subsequence

> 🔗 [LeetCode 392](https://leetcode.com/problems/is-subsequence/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#DynamicProgramming` `#Easy`

## 📜 O Problema

Dadas duas strings `s` e `t`, retorne `true` se `s` for uma **subsequência** de `t`. Uma subsequência é formada removendo alguns (ou nenhum) caracteres da string original, sem mudar a ordem relativa dos que restam (ex.: `"ace"` é subsequência de `"abcde"`, mas `"aec"` não é).

**Exemplos:**
```
Input:  s = "abc", t = "ahbgdc"
Output: true

Input:  s = "axc", t = "ahbgdc"
Output: false
```

**Restrições (e o que elas denunciam):**
- `0 <= s.length <= 100`, `0 <= t.length <= 10^4` → `t` pode ser bem maior que `s`; `s` vazio é um caso de borda válido (subsequência vazia sempre existe)
- Só letras minúsculas → sem necessidade de normalizar case
- Follow-up: bilhões de `s` diferentes contra o mesmo `t` → sinaliza que existe uma versão com pré-processamento de `t` para consultas repetidas, mais eficiente que refazer o scan linear a cada vez

## 🧭 Como reconhecer o padrão

"Verificar se uma sequência aparece **na ordem**, permitindo pular elementos no meio" é resolvido de forma greedy com dois ponteiros: um em `s`, outro em `t`, ambos só andando pra frente — nunca precisa voltar, porque a primeira ocorrência válida de cada caractere de `s` é sempre a melhor escolha (não faz diferença "guardar" um caractere de `t` pra usar depois).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Tratar como o problema geral de **Longest Common Subsequence** (LCS): construir uma tabela de programação dinâmica `dp[i][j]` = tamanho da maior subsequência comum entre `s[0..i)` e `t[0..j)`, e checar se `dp[s.length][t.length] == s.length`.

- Tempo: O(s.length × t.length) · Espaço: O(s.length × t.length) para a tabela
- **Por que não basta:** o problema só pede uma resposta **sim/não** (se `s` é subsequência de `t`), não o tamanho da maior subsequência comum entre duas strings arbitrárias. Para essa pergunta mais simples, uma estratégia greedy resolve em uma única passada, sem precisar de tabela nenhuma — LCS completo é over-engineering aqui.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um ponteiro `i` em `s` e um ponteiro `j` em `t`. Percorra `t` do início ao fim com `j`; sempre que `t[j]` for igual ao caractere que `s[i]` está esperando, avance `i` também. Ao final, se `i` alcançou o fim de `s`, é porque todo caractere de `s` foi encontrado em ordem dentro de `t` — logo, é subsequência.

## 🎬 Exemplo passo a passo

`s = "abc"`, `t = "ahbgdc"`, `i` e `j` começam em 0

| Passo | j | t[j] | s[i] esperado | Match? | Ação |
|---|---|---|---|---|---|
| 1 | 0 | `a` | `a` (i=0) | sim | i=1, j=1 |
| 2 | 1 | `h` | `b` (i=1) | não | j=2 (i mantém) |
| 3 | 2 | `b` | `b` (i=1) | sim | i=2, j=3 |
| 4 | 3 | `g` | `c` (i=2) | não | j=4 |
| 5 | 4 | `d` | `c` (i=2) | não | j=5 |
| 6 | 5 | `c` | `c` (i=2) | sim | i=3, j=6 |

`j` chega ao fim de `t` (6); `i = 3 == s.length()` → **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(t.length) — `j` percorre `t` uma única vez; `i` nunca ultrapassa `s.length`
- **Espaço:** O(1) — só os dois índices `i` e `j`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isSubsequence(String s, String t) {
    int i = 0; // ponteiro em s: próximo caractere que precisamos encontrar
    int j = 0; // ponteiro em t: varre a string maior

    while (i < s.length() && j < t.length()) {
        if (s.charAt(i) == t.charAt(j)) {
            i++; // só avança em s quando o caractere esperado é encontrado
        }
        j++; // t sempre avança, casando ou não (greedy: usa a 1ª ocorrência)
    }

    return i == s.length(); // percorreu s inteiro? então é subsequência de t
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

- Avançar `i` mesmo sem match — isso pularia um caractere de `s` sem de fato encontrá-lo em `t`, gerando falso positivo.
- Achar que é preciso montar uma tabela de DP (O(s×t)) — a estratégia greedy com dois ponteiros já é ótima para esta pergunta de existência; DP só seria necessário se o problema pedisse o tamanho da maior subsequência comum (LCS) entre duas strings quaisquer.
- No cenário do follow-up (bilhões de `s` contra o mesmo `t`), repetir o scan O(t) para cada `s` fica caro — a saída é pré-processar `t` guardando, para cada letra, a lista ordenada de índices onde ela aparece, e para cada caractere de `s` fazer busca binária pela próxima posição válida (O(t) de pré-processamento + O(s log t) por consulta).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| `s` vazio | `s=""`, `t="ahbgdc"` | true | subsequência vazia é válida em qualquer string; `i` já começa igual a `s.length()=0` |
| `t` vazio, `s` não vazio | `s="a"`, `t=""` | false | loop não executa, `i` nunca avança, `0 != 1` |
| `s` igual a `t` | `s="abc"`, `t="abc"` | true | casamento perfeito em sequência |
| Ordem errada | `s="axc"`, `t="ahbgdc"` | false | `'x'` nunca aparece depois do `'a'` casado, na posição certa |

## 🔗 Conexões

- Problemas irmãos: [0524] Longest Word in Dictionary through Deleting (mesma checagem de subsequência aplicada a várias palavras candidatas), [1143] Longest Common Subsequence (a versão "cheia" com DP, quando o problema pede o tamanho, não só a existência)
- No backend: validar se uma sequência de eventos observados (ex.: cliques do usuário, transições de estado) respeita uma ordem esperada, permitindo eventos extras no meio — o mesmo padrão de "verificar ordem parcial preservada" aparece em validação de fluxos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
