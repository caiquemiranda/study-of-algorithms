# [0434] Number of Segments in a String

> 🔗 [LeetCode 434](https://leetcode.com/problems/number-of-segments-in-a-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Parsing` `#Easy`

## 📜 O Problema

Dada uma string `s`, retorne **o número de segmentos na string**.

Um **segmento** é definido como uma sequência contígua de **caracteres que não são espaço**.

**Exemplos:**
```
Input:  s = "Hello, my name is John"
Output: 5
Explicação: os cinco segmentos são ["Hello,", "my", "name", "is", "John"]

Input:  s = "Hello"
Output: 1
```

**Restrições (e o que elas denunciam):**
- `0 <= s.length <= 300` → tamanho pequeno, qualquer O(n) resolve com folga; a string pode ser vazia
- `s` consiste de letras minúsculas/maiúsculas, dígitos, ou pontuação específica → pontuação grudada numa palavra não separa segmento nenhum
- "o único caractere de espaço em `s` é `' '`" → não precisa tratar tab, newline ou múltiplos tipos de espaço em branco

## 🧭 Como reconhecer o padrão

"Conte grupos separados por espaço" sempre pode ser resolvido com split, mas a versão eficiente conta transições espaço→não-espaço numa única passada, sem alocar substrings.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar `s.trim().split("\\s+")` e contar os elementos não vazios do array resultante.

- Tempo: O(n) (mas com constante alta por causa do motor de regex) · Espaço: O(n) para o array de substrings
- **Por que não basta:** não é errado, mas aloca uma string nova para cada palavra quando só o número de palavras importa — desperdício de memória evitável.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra a string uma vez. Toda vez que encontrar um caractere não-espaço que seja o **primeiro** do seu grupo (a posição é 0, ou o caractere anterior é espaço), conte mais um segmento.

## 🎬 Exemplo passo a passo

`s = "Hello, my name is John"`

| Passo | i | char | anterior é espaço? | Novo segmento? | count |
|---|---|---|---|---|---|
| 1 | 0 | H | (início da string) | sim | 1 |
| 2 | 7 | m | sim (depois da vírgula+espaço) | sim | 2 |
| 3 | 10 | n | sim | sim | 3 |
| 4 | 15 | i | sim | sim | 4 |
| 5 | 18 | J | sim | sim | 5 |

Resultado final: `5` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string
- **Espaço:** O(1) — só um contador inteiro, nenhuma alocação extra

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countSegments(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        // um novo segmento começa quando o caractere atual não é espaço
        // e (é o primeiro caractere OU o anterior era espaço)
        if (s.charAt(i) != ' ' && (i == 0 || s.charAt(i - 1) == ' ')) {
            count++;
        }
    }
    return count;
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

- Espaços múltiplos entre palavras (`"a   b"`) — `split(" ")` sem regex `+` gera strings vazias no meio; a contagem por transições não tem esse problema.
- String vazia (`""`) — o loop simplesmente não executa, retorna 0 corretamente.
- Espaços nas bordas (`" Hello "`) — não afetam a contagem porque a checagem é sempre "não-espaço precedido por espaço/início".
- Confundir "segmento" com "palavra separada por espaço único" — pontuação grudada numa palavra (`"Hello,"`) conta como parte do mesmo segmento, não separa.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| String vazia | `s=""` | 0 | nenhum caractere para formar segmento |
| Só espaços | `s="   "` | 0 | nenhum caractere não-espaço |
| Espaços múltiplos | `s="a   b"` | 2 | múltiplos espaços não criam segmentos vazios |
| Espaços nas bordas | `s=" Hello "` | 1 | bordas não afetam a contagem |

## 🔗 Conexões

- Problemas irmãos: [0058] Length of Last Word (mesmo tipo de parsing de string por espaços), [0151] Reverse Words in a String (mesma ideia de identificar grupos de não-espaço)
- No backend: parsing de comandos de CLI, tokenização simples de texto (contar campos separados por espaço num log) antes de aplicar um parser mais robusto.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
