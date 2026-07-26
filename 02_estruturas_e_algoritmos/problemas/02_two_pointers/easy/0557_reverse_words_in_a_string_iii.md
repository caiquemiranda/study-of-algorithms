# [0557] Reverse Words in a String III

> 🔗 [LeetCode 557](https://leetcode.com/problems/reverse-words-in-a-string-iii/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s`, reverta a ordem dos **caracteres dentro de cada palavra**, preservando os espaços e a ordem das palavras.

**Exemplos:**
```
Input:  s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Input:  s = "Mr Ding"
Output: "rM gniD"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 5 * 10^4` → O(n) esperado
- Sem espaços no início/fim, sem espaços múltiplos entre palavras → simplifica bastante: não é preciso limpar nada, só encontrar onde cada palavra começa e termina
- Pelo menos uma palavra garantida → sem caso de string vazia a tratar

## 🧭 Como reconhecer o padrão

"Reverter cada bloco delimitado por um separador, preservando os separadores e a ordem dos blocos" é a mesma ideia de [0541] Reverse String II — só que aqui o tamanho de cada bloco (palavra) é **variável**, delimitado por espaços, em vez de um `k` fixo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Dividir a string em palavras com `split(" ")`, reverter cada palavra com `StringBuilder.reverse()`, e juntar tudo de novo com `String.join(" ", ...)`.

- Tempo: O(n) · Espaço: O(n) — o `split` cria um array de substrings, e cada `StringBuilder` aloca uma cópia nova
- **Por que não basta:** funciona, mas gera várias alocações intermediárias (array de palavras + um objeto de reversão por palavra); dois ponteiros revertem cada palavra **diretamente** no array de caracteres original, sem cópias.

## 💡 Solução 2 — A ideia otimizada (intuição)

Converta `s` para `char[]`. Use um índice `start` marcando o início da palavra atual. Avance outro índice até achar o próximo espaço (ou o fim da string) — esse é o fim da palavra. Reverta o trecho `[start, fim]` com dois ponteiros nas pontas (igual ao LC 344). Depois, pule o espaço e repita a partir da próxima palavra.

## 🎬 Exemplo passo a passo

`s = "Mr Ding"` (índices 0 a 6: `M,r,' ',D,i,n,g`)

| Passo | início da palavra | fim da palavra | Ação | Resultado parcial |
|---|---|---|---|---|
| 1 | 0 | 1 (`"Mr"`) | troca `arr[0]` com `arr[1]` (`M` ↔ `r`) | `"rM Ding"` |
| 2 | 3 | 6 (`"Ding"`) | troca `arr[3]`↔`arr[6]` (`D`↔`g`) e `arr[4]`↔`arr[5]` (`i`↔`n`) | `"rM gniD"` |

Resultado final: `"rM gniD"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere é visitado no máximo duas vezes (uma para achar o fim da palavra, outra dentro da reversão)
- **Espaço:** O(n) para o `char[]` (necessário em Java por strings serem imutáveis); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String reverseWords(String s) {
    char[] arr = s.toCharArray();
    int n = arr.length;
    int start = 0;

    while (start < n) {
        int end = start;
        // avança até o fim da palavra atual (próximo espaço ou fim da string)
        while (end < n && arr[end] != ' ') {
            end++;
        }

        // reverte a palavra em [start, end-1] com dois ponteiros
        int left = start;
        int right = end - 1;
        while (left < right) {
            char tmp = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp;
            left++;
            right--;
        }

        start = end + 1; // pula o espaço e começa a próxima palavra
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

- Usar `split(" ")` + reverter + `join` — funciona, mas aloca um array de substrings e uma string reconstruída; dois ponteiros resolvem direto no `char[]` original, sem cópias.
- Esquecer o `+ 1` em `start = end + 1` — sem pular o espaço, o próximo "início de palavra" seria o próprio caractere de espaço.
- Assumir que pode haver espaços múltiplos entre palavras ou nas pontas — a constraint garante exatamente um espaço entre palavras e nenhum nas bordas; esse tipo de limpeza extra (necessária em [0151]) não é preciso aqui.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Frase com várias palavras | `"Let's take LeetCode contest"` | `"s'teL ekat edoCteeL tsetnoc"` | caso padrão, cada palavra revertida isoladamente |
| Duas palavras | `"Mr Ding"` | `"rM gniD"` | testa palavras de tamanhos diferentes |
| Uma única palavra | `"hello"` | `"olleh"` | sem espaço, a string toda é uma única "palavra" |
| Palavra de 1 caractere | `"a b"` | `"a b"` | palavras de tamanho 1 revertem pra si mesmas (`left == right`, sem swap) |

## 🔗 Conexões

- Problemas irmãos: [0344] Reverse String (mesma técnica de swap com dois ponteiros, mas na string inteira), [0541] Reverse String II (mesma ideia de reverter blocos, mas de tamanho fixo `k` em vez de delimitado por espaço)
- No backend: normalizar texto campo a campo dentro de um registro maior — por exemplo, aplicar uma transformação só dentro de cada token de um CSV, preservando os delimitadores originais.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
