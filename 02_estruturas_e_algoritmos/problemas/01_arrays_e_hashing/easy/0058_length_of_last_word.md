# [0058] Length of Last Word

> 🔗 [LeetCode 58](https://leetcode.com/problems/length-of-last-word/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` com palavras e espaços, retorne o **tamanho da última palavra**. Uma palavra é uma sequência máxima de caracteres que não são espaço.

**Exemplos:**
```
Input:  s = "Hello World"                  Output: 5   ("World")
Input:  s = "   fly me   to   the moon  "  Output: 4   ("moon")
Input:  s = "luffy is still joyboy"        Output: 6   ("joyboy")
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^4` → qualquer solução O(n) passa tranquilamente; não precisa de truque exótico
- "`s` consiste apenas em letras e espaços" → sem tabs/pontuação, o único delimitador é o espaço simples
- "há pelo menos uma palavra em `s`" → você nunca precisa tratar string totalmente vazia de palavras
- Repare no exemplo 2: **múltiplos espaços e espaços no fim são permitidos** — isso é a pegadinha do problema

## 🧭 Como reconhecer o padrão

Parsing simples de string, mas do jeito **eficiente**: em vez de depender de `split()` (que aloca um array novo), o padrão é **percorrer de trás para frente com dois marcadores** — um clássico de "processar string sem estrutura auxiliar", primo do two pointers.

## 🐢 Solução 1 — Força bruta

Usar `split(" ")` da linguagem, filtrar strings vazias (geradas pelos espaços múltiplos) e pegar o tamanho do último elemento.

- Tempo: O(n) · Espaço: O(n) — o `split` aloca um array com todas as palavras
- **Por que não é a ideal:** funciona e passa, mas gasta memória para um problema que só precisa de UM número. Interessante ver a versão O(1) de espaço.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ande a partir do **fim** da string com um ponteiro `i`:
1. Pule todos os espaços à direita (o "colchão" antes da última palavra).
2. A partir daí, conte quantos caracteres não-espaço existem até o próximo espaço (ou o início da string).

Dois ponteiros, uma passada, sem alocar nada.

## 🎬 Exemplo passo a passo

`s = "   fly me   to   the moon  "` (tamanho 28, índices 0 a 27)

| Passo | Ação | i após | Observação |
|---|---|---|---|
| 1 | pula espaços finais (índices 27, 26) | 25 | chegou no 'n' de "moon" |
| 2 | conta enquanto não for espaço: n-o-o-m | 21 | contou 4 caracteres |
| 3 | `s[21]` é espaço → para | — | fim da contagem |

Resultado final: **4** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — no pior caso percorre a string inteira uma vez
- **Espaço:** O(1) — só dois inteiros como ponteiros, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int lengthOfLastWord(String s) {
    int i = s.length() - 1;

    // Passo 1: pula os espaços do fim (o "colchão" depois da última palavra)
    while (i >= 0 && s.charAt(i) == ' ') {
        i--;
    }

    // Passo 2: conta os caracteres da última palavra, andando para trás
    int tamanho = 0;
    while (i >= 0 && s.charAt(i) != ' ') {
        tamanho++;
        i--;
    }

    return tamanho;
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

- Esquecer de pular os **espaços finais** antes de começar a contar — sem isso, a contagem começa em 0 (espaço) e devolve tamanho errado.
- Usar `s.strip()`/`s.trim()` + `split()` funciona, mas esconde a lógica que o problema quer que você pratique (e gasta espaço extra).
- Assumir que só existe **um** espaço entre palavras — o enunciado permite múltiplos.
- **Java**: `s.charAt(i)` em loop é O(1) (String é array de char por baixo) — diferente de linguagens onde indexar string é caro.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem espaços extras | `"Hello World"` | 5 | caso simples |
| Espaços múltiplos no fim | `"a   "` | 1 | testa o passo 1 sozinho |
| Uma palavra só | `"word"` | 4 | sem espaço nenhum |
| Espaços múltiplos entre palavras | `"a  bb   ccc"` | 3 | garante que o passo 2 para no espaço certo |

## 🔗 Conexões

- Problemas irmãos: **[0151] Reverse Words in a String** (mesma ideia, mas para a string inteira), **[0014] Longest Common Prefix** (outro parsing de string sem estrutura extra)
- No backend: parsing de linha de comando, de headers HTTP (`Content-Length: 42` — extrair o valor sem alocar array) e de logs de texto usa exatamente este padrão de varredura com ponteiros.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
