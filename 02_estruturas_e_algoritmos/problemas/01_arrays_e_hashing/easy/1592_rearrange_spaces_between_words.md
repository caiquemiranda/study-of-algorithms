# [1592] Rearrange Spaces Between Words

> 🔗 [LeetCode 1592](https://leetcode.com/problems/rearrange-spaces-between-words/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Você recebe uma string `text` com palavras separadas por espaços. Cada palavra consiste em uma ou mais letras minúsculas e é separada por pelo menos um espaço. É garantido que `text` contém pelo menos uma palavra.

Rearranje os espaços de forma que haja um número **igual** de espaços entre cada par de palavras adjacentes, e esse número seja **maximizado**. Se não for possível redistribuir todos os espaços igualmente, coloque os espaços extras **no final**, mantendo o mesmo comprimento de `text`.

Retorne a string após rearranjar os espaços.

**Exemplos:**
```
Input:  text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explicação: há 9 espaços no total e 4 palavras. Dividimos igualmente: 9 / (4-1) = 3 espaços.

Input:  text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explicação: há 7 espaços no total e 3 palavras. 7 / (3-1) = 3 espaços mais 1 extra.
Colocamos esse espaço extra no final da string.
```

**Restrições (e o que elas denunciam):**
- `1 <= text.length <= 100` → pequeno, O(n) resolve com folga
- pelo menos uma palavra garantida → não precisa tratar texto vazio de palavras
- "distribuir igualmente, sobra no final" → precisa calcular divisão inteira e resto

## 🧭 Como reconhecer o padrão

"Redistribuir um recurso (espaços) igualmente entre posições (entre palavras), com sobra alocada num lugar fixo (no final)" é resolvido contando o total do recurso e o número de posições, calculando `total / posições` (quociente) e `total % posições` (resto), e reconstruindo com o quociente entre cada par e o resto no final.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Reconstruir a string caractere por caractere, tentando inserir os espaços um a um em cada posição entre palavras, ajustando dinamicamente conforme sobra.

- Tempo: O(n) — mesmo a versão "ingênua" ainda é O(n), a diferença é de organização do código · Espaço: O(n)
- **Por que vale nomear mesmo assim:** sem pré-calcular `total espaços / (palavras-1)` antecipadamente, a lógica de distribuição fica mais complicada de acertar (fácil de errar a última palavra ou o resto).

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte o total de espaços em `text` e extraia as palavras. Se houver só 1 palavra, o resultado é a palavra seguida de todos os espaços. Caso contrário, calcule `espacosEntrePalavras = totalEspacos / (numPalavras - 1)` e `espacosExtras = totalEspacos % (numPalavras - 1)`; junte as palavras com `espacosEntrePalavras` espaços entre cada par, e acrescente `espacosExtras` espaços no final.

## 🎬 Exemplo passo a passo

`text = " practice   makes   perfect"` — `totalEspacos = 7`, `palavras = ["practice","makes","perfect"]` (3 palavras)

| Passo | Cálculo | Valor |
|---|---|---|
| 1 | totalEspacos | 7 |
| 2 | numPalavras | 3 |
| 3 | espacosEntrePalavras = 7/(3-1) | 3 |
| 4 | espacosExtras = 7%(3-1) | 1 |
| 5 | montagem | "practice" + "   " + "makes" + "   " + "perfect" + " " |

Resultado final: `"practice   makes   perfect "` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String reorderSpaces(String text) {
    int totalEspacos = 0;
    for (char c : text.toCharArray()) {
        if (c == ' ') {
            totalEspacos++;
        }
    }

    String[] palavras = text.trim().split("\\s+");
    // se text.trim() ficar vazio, split ainda devolveria [""], então tratamos isso ao verificar length
    int numPalavras = palavras[0].isEmpty() ? 0 : palavras.length;

    StringBuilder resultado = new StringBuilder();
    if (numPalavras <= 1) {
        // com 0 ou 1 palavra, todos os espaços vão pro final, sem distribuição entre pares
        if (numPalavras == 1) {
            resultado.append(palavras[0]);
        }
        resultado.append(" ".repeat(totalEspacos));
    } else {
        int espacosEntre = totalEspacos / (numPalavras - 1);
        int espacosExtras = totalEspacos % (numPalavras - 1);
        for (int i = 0; i < numPalavras; i++) {
            resultado.append(palavras[i]);
            if (i < numPalavras - 1) {
                resultado.append(" ".repeat(espacosEntre));
            }
        }
        resultado.append(" ".repeat(espacosExtras));
    }
    return resultado.toString();
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

- Dividir por `numPalavras` em vez de `numPalavras - 1` — o número de "espaços entre pares de palavras adjacentes" é sempre `palavras - 1`, não o total de palavras.
- Esquecer o caso de UMA ÚNICA palavra — nesse caso não há "entre palavras" nenhum, TODOS os espaços vão para o final, e dividir por `numPalavras - 1` (que seria 0) causaria erro de divisão por zero.
- Usar `text.split(" ")` sem `trim()` e sem o `+` do regex (`\\s+`) — geraria tokens vazios por causa de espaços múltiplos ou espaços nas bordas do texto original.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Distribuição exata | "  this   is  a sentence " | "this   is   a   sentence" | 9 espaços / 3 pares = 3 cada, sem sobra |
| Sobra no final | " practice   makes   perfect" | "practice   makes   perfect " | 7 espaços / 2 pares = 3 cada, sobra 1 no final |
| Uma única palavra | "  hello  " | "hello    " | todos os 6 espaços vão para o final |
| Sem espaço nenhum | "word" | "word" | nenhum espaço para redistribuir |

## 🔗 Conexões

- Problemas irmãos: [0151] Reverse Words in a String (mesma técnica de tokenização por espaços), [1417] Reformat The String (mesmo domínio de reconstrução de string sob uma regra de distribuição)
- No backend: formatação de texto justificado em relatórios ou documentos (ex.: distribuir espaçamento uniformemente entre colunas de um relatório de texto plano).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
