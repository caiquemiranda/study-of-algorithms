# [2000] Reverse Prefix of Word

> 🔗 [LeetCode 2000](https://leetcode.com/problems/reverse-prefix-of-word/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string `word` (0-indexada) e um caractere `ch`, reverta o segmento de `word` do índice `0` até a **primeira ocorrência** de `ch` (inclusive). Se `ch` não existir em `word`, não faça nada.

**Exemplos:**
```
Input:  word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explicação: primeira ocorrência de "d" é no índice 3; reverte de 0 a 3.

Input:  word = "xyxzxe", ch = "z"
Output: "zxyxxe"

Input:  word = "abcd", ch = "z"
Output: "abcd"
Explicação: "z" não existe, nenhuma reversão.
```

**Restrições (e o que elas denunciam):**
- `1 <= word.length <= 250` → entrada pequena, O(n) já é natural e suficiente
- `ch` pode não existir em `word` → é preciso checar essa ausência antes de qualquer reversão
- Reverte só até a **primeira** ocorrência (inclusive), não a string inteira → o resto de `word` depois desse ponto fica intocado

## 🧭 Como reconhecer o padrão

"Reverter um prefixo delimitado pela posição de um caractere específico" combina achar a posição-alvo (uma busca linear simples) com o padrão de dois ponteiros nas pontas de [0344] Reverse String — só que aqui a "ponta direita" não é o fim da string inteira, e sim a primeira ocorrência de `ch`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Achar o índice de `ch` com `indexOf`, depois construir uma string nova concatenando `new StringBuilder(word.substring(0, idx+1)).reverse()` com `word.substring(idx+1)`.

- Tempo: O(n) · Espaço: O(n) — cria substrings e um `StringBuilder` intermediários antes de montar o resultado final
- **Por que não basta:** já é O(n) em tempo, mas aloca cópias intermediárias (duas substrings + um StringBuilder) que dois ponteiros evitam completamente, revertendo direto no array de caracteres original.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ache o índice `idx` da primeira ocorrência de `ch` (com uma busca linear, ou `indexOf`). Se não existir (`idx == -1`), retorne `word` sem alterações. Caso contrário, converta `word` para `char[]` e reverta o trecho `[0, idx]` com dois ponteiros nas pontas desse intervalo — exatamente como em [0344] Reverse String, só que limitado a essa faixa.

## 🎬 Exemplo passo a passo

`word = "abcdefd"`, `ch = 'd'` — primeira ocorrência de `'d'` está no índice `3`

| Passo | left | right | Ação | Array depois |
|---|---|---|---|---|
| 1 | 0 | 3 | troca `arr[0]` com `arr[3]` (`a` ↔ `d`) | `[d,b,c,a,e,f,d]` |
| 2 | 1 | 2 | troca `arr[1]` com `arr[2]` (`b` ↔ `c`) | `[d,c,b,a,e,f,d]` |
| 3 | 2 | 1 | `left >= right`, loop termina | `[d,c,b,a,e,f,d]` |

Resultado final: `"dcbaefd"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — O(n) para achar `idx`, mais O(idx) para reverter o prefixo
- **Espaço:** O(n) para o `char[]` (necessário em Java por strings serem imutáveis); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String reversePrefix(String word, char ch) {
    int idx = word.indexOf(ch);
    if (idx == -1) {
        return word; // ch não existe, nada a fazer
    }

    char[] arr = word.toCharArray();
    int left = 0;
    int right = idx;
    while (left < right) {
        char tmp = arr[left];
        arr[left] = arr[right];
        arr[right] = tmp;
        left++;
        right--;
    }

    return new String(arr);
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

- Esquecer o caso de `ch` ausente (`indexOf` retorna `-1`) — sem essa checagem, tentar reverter até o índice `-1` é um erro; o enunciado é explícito: se `ch` não existe, não faça nada.
- Reverter o array inteiro em vez de só o prefixo `[0, idx]` — o enunciado pede reverter só até a primeira ocorrência de `ch` (inclusive); o resto da string permanece intocado.
- Usar a ÚLTIMA ocorrência de `ch` (`lastIndexOf`) em vez da primeira (`indexOf`) — é fácil confundir os dois métodos se não prestar atenção ao enunciado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caractere no meio | `word="abcdefd"`, `ch='d'` | `"dcbaefd"` | reverte só o prefixo até a primeira ocorrência de `'d'` |
| Caractere ausente | `word="abcd"`, `ch='z'` | `"abcd"` | nenhuma reversão, string retorna intacta |
| Caractere na primeira posição | `word="abcd"`, `ch='a'` | `"abcd"` | prefixo de tamanho 1, reversão não muda nada |
| Caractere no final | `word="abcd"`, `ch='d'` | `"dcba"` | reverte a string inteira, já que `'d'` é o último caractere |

## 🔗 Conexões

- Problemas irmãos: [0344] Reverse String (mesma técnica de swap com dois ponteiros, mas na string inteira), [0541] Reverse String II (mesma ideia de reverter só um trecho, mas por tamanho fixo em vez de por posição de um caractere)
- No backend: normalizar um campo de texto revertendo só até um delimitador específico — por exemplo, inverter a parte de um identificador antes do primeiro separador, mantendo o restante do formato intacto.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
