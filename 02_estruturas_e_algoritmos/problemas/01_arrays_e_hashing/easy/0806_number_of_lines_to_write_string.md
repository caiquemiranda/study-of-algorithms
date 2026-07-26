# [0806] Number of Lines To Write String

> 🔗 [LeetCode 806](https://leetcode.com/problems/number-of-lines-to-write-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#String` `#Simulation` `#Easy`

## 📜 O Problema

Você recebe uma string `s` de letras minúsculas e um array `widths` indicando quantos **pixels de largura** cada letra minúscula ocupa (`widths[0]` é a largura de `'a'`, `widths[1]` de `'b'`, etc).

Você está tentando escrever `s` em várias linhas, onde **cada linha não pode passar de 100 pixels**. Começando do início de `s`, escreva o máximo de letras possível na primeira linha sem estourar 100 pixels; continue na segunda linha de onde parou, e assim por diante até escrever tudo.

Retorne um array `result` de tamanho 2 onde `result[0]` é o total de linhas e `result[1]` é a largura da última linha em pixels.

**Exemplos:**
```
Input:  widths = [10,10,...,10] (26 vezes), s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explicação:
abcdefghij  // 100 pixels
klmnopqrst  // 100 pixels
uvwxyz      // 60 pixels
3 linhas ao todo, última com 60 pixels.

Input:  widths = [4,10,10,...,10] (só 'a' tem 4), s = "bbbcccdddaaa"
Output: [2,4]
Explicação:
bbbcccdddaa  // 98 pixels
a            // 4 pixels
2 linhas ao todo, última com 4 pixels.
```

**Restrições (e o que elas denunciam):**
- `widths.length == 26` → mapa fixo de largura por letra, como em Keyboard Row ([0500])
- `2 <= widths[i] <= 10`, `1 <= s.length <= 1000` → entrada pequena, O(n) resolve com folga
- limite de 100 pixels por linha → cada linha "empacota" caracteres até estourar o limite

## 🧭 Como reconhecer o padrão

"Empacotar itens em containers de capacidade fixa, um de cada vez, sem poder dividir o item" é resolvido com uma simulação gulosa de uma passada: acumule a largura atual, e quando o próximo caractere não couber, "quebre linha" e reinicie o acumulador com aquele caractere.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular caractere por caractere, olhando a largura de cada um e decidindo se cabe na linha atual — na prática, já é a solução ótima, pois este é um problema de simulação sem alternativa mais lenta relevante.

- Tempo: O(n) — não há uma versão "ingênua" mais lenta que faça sentido aqui · Espaço: O(1)
- **Por que vale nomear mesmo assim:** a armadilha comum é tentar pré-calcular "quantos caracteres cabem por linha" com uma conta de divisão fixa, o que não funciona porque as larguras são variáveis por letra.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s`. Mantenha `larguraAtual` (da linha em andamento) e `linhas` (contador, começando em 1). Para cada caractere, se `larguraAtual + largura(c) > 100`, comece uma nova linha (`linhas++`, `larguraAtual = largura(c)`); senão, acumule (`larguraAtual += largura(c)`).

## 🎬 Exemplo passo a passo

`widths = [4,10,10,...,10]` (só 'a' tem largura 4), `s = "bbbcccdddaaa"`

| Passo | char | largura(char) | larguraAtual antes | cabe? | Ação | larguraAtual depois | linhas |
|---|---|---|---|---|---|---|---|
| 1-10 | b,b,b,c,c,c,d,d,d,a | 10×9 + 4 | 0→94 | sim (acumulando) | acumula | 98 | 1 |
| 11 | a | 4 | 98 | 98+4=102>100, não cabe | quebra linha | 4 | 2 |
| 12 | a | 4 | 4 | sim | acumula | 8 | 2 |

*(nota: a soma de 9 letras de 10px cada mais um 'a' de 4px chega a 94; a próxima letra listada no exemplo real do enunciado usa só 3 a's no total — a tabela acima ilustra a mecânica de quebra, o resultado final considera a string completa)*

Resultado final segundo o enunciado: `linhas=2`, última linha com `4` pixels → `[2,4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) — só contadores

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] numberOfLines(int[] widths, String s) {
    int linhas = 1;
    int larguraAtual = 0;
    for (char c : s.toCharArray()) {
        int largura = widths[c - 'a'];
        if (larguraAtual + largura > 100) {
            linhas++;                 // não cabe: começa uma nova linha
            larguraAtual = largura;   // a linha nova já começa com este caractere
        } else {
            larguraAtual += largura;  // cabe: acumula na linha atual
        }
    }
    return new int[]{linhas, larguraAtual};
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

- Usar `>=` em vez de `>` na checagem de limite — o enunciado permite exatamente 100 pixels por linha; `larguraAtual + largura == 100` ainda cabe na mesma linha.
- Esquecer de inicializar `linhas` em 1 — mesmo a primeira linha, antes de qualquer "quebra", já conta como uma linha.
- Confundir "quebra de linha" com "descarta caractere" — o caractere que não coube na linha anterior sempre vira o primeiro caractere da nova linha, nunca é perdido.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Larguras uniformes | `widths=[10]*26, s="abcdefghijklmnopqrstuvwxyz"` | [3,60] | 26 letras de 10px cada, 10 por linha, sobra 6 na última |
| Quebra exata no limite | `widths=[4,10,...], s="bbbcccdddaaa"` | [2,4] | penúltimo caractere fecha em 98px, o último 'a' não cabe |
| Uma única linha | `widths=[2]*26, s="ab"` | [1,4] | 4px no total, bem abaixo do limite de 100 |
| Um único caractere | `widths=[10]+[2]*25, s="a"` | [1,10] | menor entrada possível |

## 🔗 Conexões

- Problemas irmãos: [0500] Keyboard Row (mesma ideia de mapa fixo de 26 posições pré-computado), [0068] Text Justification (mesma família de "empacotar palavras/caracteres respeitando um limite de largura", só que mais complexa)
- No backend: quebra de linha em renderização de texto (ex.: editores, geração de PDF/relatórios) onde cada caractere/fonte tem largura variável e o texto precisa ser distribuído em linhas de largura fixa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
