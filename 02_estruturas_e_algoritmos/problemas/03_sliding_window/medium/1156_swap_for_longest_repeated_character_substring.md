# [1156] Swap For Longest Repeated Character Substring

> 🔗 [LeetCode 1156](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Medium`

## 📜 O Problema

Você recebe uma string `text` e pode trocar (swap) duas posições dela uma única vez. Retorne o comprimento da maior substring com caracteres repetidos que você consegue obter.

**Exemplos:**
```
Input:  text = "ababa"
Output: 3
Explicação: trocando o primeiro 'b' com o último 'a' (ou vice-versa), a maior substring repetida vira "aaa".

Input:  text = "aaabaaa"
Output: 6
Explicação: trocando o 'b' com um 'a' de fora, forma "aaaaaa" de comprimento 6.

Input:  text = "aaaaa"
Output: 5
Explicação: nenhuma troca necessária, "aaaaa" já é a resposta.
```

**Restrições (e o que elas denunciam):**
- `1 <= text.length <= 2 * 10^4` → O(n²) força bruta é arriscado; O(n) é o esperado
- `text` consiste só em letras minúsculas → no máximo 26 caracteres distintos

## 🧭 Como reconhecer o padrão

"Maior trecho de um único caractere repetido, com no máximo uma troca posicional" é resolvido comprimindo a string em **runs** (blocos de caracteres iguais consecutivos) numa única passada — a mesma ideia de "expandir enquanto o caractere se mantém" de uma janela — e depois analisando pares de runs vizinhos separados por exatamente um caractere diferente (o "intruso" a ser trocado).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de posições `(i, j)`, simular a troca e recalcular o maior trecho repetido resultante do zero.

- Tempo: O(n³) (O(n²) trocas possíveis, O(n) para reavaliar cada uma) · Espaço: O(n) por simulação
- **Por que não basta:** simula fisicamente cada troca possível e reprocessa a string inteira, quando a estrutura do problema (runs de caracteres) permite decidir a melhor troca sem simular nenhuma.

## 💡 Solução 2 — A ideia otimizada (intuição)

Comprima `text` em uma lista de `(caractere, comprimento)` (runs). Para cada run isolado, o melhor resultado é `min(comprimento + 1, frequência total desse caractere)` — o `+1` representa "emprestar" um caractere igual de algum outro lugar do texto via a troca, limitado pela quantidade real disponível. Para dois runs do MESMO caractere separados por exatamente um run de comprimento 1 (o "intruso"), combine-os: `min(comprimento1 + comprimento2 + 1, frequência total)`.

## 🎬 Exemplo passo a passo

`text = "aaabaaa"` → runs: `[('a',3), ('b',1), ('a',3)]`, frequência total: a=6, b=1

| Grupo (idx) | Caractere | Comprimento do run | Isolado: min(len+1, freq total) | Combinação com run+2 (se houver gap de 1) | Melhor |
|---|---|---|---|---|---|
| 0 | a | 3 | min(4,6)=4 | grupo2 também é 'a' (gap de 1 'b') → combinado=3+3=6, min(7,6)=6 | 6 |
| 1 | b | 1 | min(2,1)=1 | — (não há grupo b em idx+2) | 6 |
| 2 | a | 3 | min(4,6)=4 | — (não há grupo idx+4) | 6 |

Resultado final: `6` ✔ (junta os dois blocos de 'a' trocando o 'b' do meio por um 'a' "emprestado" de fora)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para agrupar em runs + uma passada sobre os grupos
- **Espaço:** O(n) no pior caso para a lista de grupos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxRepOpt1(String text) {
    int n = text.length();
    List<int[]> groups = new ArrayList<>(); // {caractere, comprimento do run}

    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && text.charAt(j) == text.charAt(i)) {
            j++;
        }
        groups.add(new int[]{text.charAt(i), j - i});
        i = j;
    }

    int[] freq = new int[26];
    for (char c : text.toCharArray()) {
        freq[c - 'a']++;
    }

    int best = 0;
    for (int idx = 0; idx < groups.size(); idx++) {
        char c = (char) groups.get(idx)[0];
        int len = groups.get(idx)[1];
        int total = freq[c - 'a'];

        best = Math.max(best, Math.min(len + 1, total)); // run isolado + 1 caractere "emprestado"

        if (idx + 2 < groups.size()
                && groups.get(idx + 2)[0] == groups.get(idx)[0]
                && groups.get(idx + 1)[1] == 1) {
            int combined = len + groups.get(idx + 2)[1];
            best = Math.max(best, Math.min(combined + 1, total)); // junta os dois runs trocando o "intruso" do meio
        }
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

- O `min(len+1, total)` é essencial: só dá pra "emprestar" um caractere extra do MESMO tipo se ele existir em algum outro lugar do texto (`total > len` do run atual) — sem esse limite, um run que já usa TODAS as ocorrências do caractere (como em "aaaaa") pareceria poder crescer além do que realmente existe.
- Combinar dois runs do mesmo caractere só é válido se estiverem separados por EXATAMENTE um caractere diferente — um gap de 2 ou mais caracteres não pode ser resolvido com uma única troca.
- Esquecer o caso de um único run isolado (sem nenhum outro run do mesmo caractere por perto) — mesmo sem combinação, ainda vale checar se dá pra estender esse run sozinho com um caractere emprestado de fora.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já é tudo repetido | `"aaaaa"` | 5 | nenhuma troca ajuda, o texto inteiro já é um único caractere |
| Troca combina dois blocos | `"aaabaaa"` | 6 | troca o 'b' do meio por um 'a' emprestado, juntando os dois blocos de 'a' |
| Troca simples sem combinação | `"ababa"` | 3 | melhor opção é combinar "a_a" trocando o 'b' isolado |
| Sem caractere sobrando pra emprestar | `"ab"` | 1 | cada caractere aparece só uma vez, nenhuma extensão é possível |

## 🔗 Conexões

- Problemas irmãos: [3090] Maximum Length Substring With Two Occurrences (mesma família de manipular composição de caracteres numa janela, aqui com uma troca permitida em vez de um limite de ocorrências), [0424] Longest Repeating Character Replacement (mesmo objetivo — maior trecho de um único caractere repetido — mas trocando qualquer caractere livremente em vez de UMA troca posicional específica)
- No backend: calcular a maior sequência de status idênticos possível permitindo corrigir um único registro "fora do padrão" em um lote de dados, útil para detectar quase-uniformidade em auditorias de consistência.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
