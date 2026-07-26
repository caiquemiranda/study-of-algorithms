# [0541] Reverse String II

> 🔗 [LeetCode 541](https://leetcode.com/problems/reverse-string-ii/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` e um inteiro `k`, reverta os primeiros `k` caracteres de cada bloco de `2k` caracteres, contando a partir do início. Se sobrarem menos que `k` caracteres no final, reverta todos eles. Se sobrarem entre `k` e `2k` (exclusive), reverta só os primeiros `k` e deixe o resto como está.

**Exemplos:**
```
Input:  s = "abcdefg", k = 2
Output: "bacdfeg"

Input:  s = "abcd", k = 2
Output: "bacd"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^4`, `1 <= k <= 10^4` → `k` pode ser maior que `s.length`; a última "reversão" pode ter menos que `k` caracteres
- Regra dos blocos de `2k` → sinaliza um loop com passo `2k`, não `k` — a segunda metade de cada bloco fica intocada

## 🧭 Como reconhecer o padrão

"Reverter uma sub-faixa de cada vez, com uma regra de tamanho de bloco" ainda é dois ponteiros nas pontas de [0344] Reverse String — a diferença é que aqui os ponteiros não cobrem a string inteira de uma vez, e sim **cada bloco de `k` caracteres**, sendo reiniciados a cada passo de `2k`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada bloco, extrair a substring correspondente, revertê-la com `StringBuilder.reverse()` (criando um objeto novo), e concatenar o resultado com o restante da string que não muda.

- Tempo: O(n) · Espaço: O(n) — cada bloco gera uma substring/StringBuilder temporário novo, além da string final
- **Por que não basta:** funciona, mas cria uma alocação nova para cada um dos até `n / (2k)` blocos; dois ponteiros revertem cada bloco **diretamente** no array de caracteres, sem nenhuma alocação extra por bloco.

## 💡 Solução 2 — A ideia otimizada (intuição)

Converta `s` para `char[]`. Percorra o array com um índice `i` de `2k` em `2k` caracteres. Em cada posição, reverta o trecho `[i, min(i + k - 1, n - 1)]` usando dois ponteiros nas pontas desse trecho (igual ao LC 344, só que num sub-intervalo). O `min` garante que, se sobrar menos que `k` caracteres no final, só o que existir é revertido.

## 🎬 Exemplo passo a passo

`s = "abcdefg"` (n=7), `k = 2` → blocos de `2k = 4` caracteres

| Passo | i (início do bloco) | left | right | Ação | Array depois |
|---|---|---|---|---|---|
| 1 | 0 | 0 | min(1, 6) = 1 | troca `s[0]` com `s[1]` (`a`↔`b`) | `[b,a,c,d,e,f,g]` |
| 2 | 4 | 4 | min(5, 6) = 5 | troca `s[4]` com `s[5]` (`e`↔`f`) | `[b,a,c,d,f,e,g]` |
| 3 | 8 | — | — | `i(8) >= n(7)`, loop termina | `[b,a,c,d,f,e,g]` |

Resultado final: `"bacdfeg"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere é tocado no máximo uma vez, mesmo somando todos os blocos
- **Espaço:** O(n) para o `char[]` (necessário em Java por strings serem imutáveis); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String reverseStr(String s, int k) {
    char[] arr = s.toCharArray();
    int n = arr.length;

    for (int i = 0; i < n; i += 2 * k) { // passo 2k: só o primeiro k de cada bloco é revertido
        int left = i;
        int right = Math.min(i + k - 1, n - 1); // cobre o caso de sobrar menos que k no final

        while (left < right) {
            char tmp = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp;
            left++;
            right--;
        }
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

- Calcular `right` como `i + k` em vez de `i + k - 1` — o bloco de `k` caracteres começando em `i` termina no índice `i + k - 1`; esquecer o `-1` reverte um caractere além do esperado.
- Esquecer o `Math.min(..., n - 1)` — quando sobra menos que `k` caracteres no final da string, sem esse limite o código acessa índice fora dos limites do array.
- Achar que a segunda metade de cada bloco de `2k` (os caracteres entre `k` e `2k`) precisa de algum tratamento especial — eles simplesmente ficam como estão; o loop com passo `2*k` já os pula automaticamente ao saltar pro próximo bloco.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Blocos completos de 2k | `s="abcdefg"`, `k=2` | `"bacdfeg"` | dois blocos completos + um caractere sobrando no fim |
| Entre k e 2k | `s="abcd"`, `k=2` | `"bacd"` | reverte só os primeiros k=2, o resto (`cd`) fica igual |
| Menos que k no final | `s="ab"`, `k=3` | `"ba"` | sobra menos que k, reverte tudo que existe |
| k maior que a string | `s="a"`, `k=5` | `"a"` | um único caractere, reversão não muda nada |

## 🔗 Conexões

- Problemas irmãos: [0344] Reverse String (mesma técnica de swap com dois ponteiros, mas aplicada à string inteira, sem blocos), [0151] Reverse Words in a String (também reorganiza blocos específicos preservando o resto)
- No backend: processamento de dados em blocos fixos (chunking), aplicando uma transformação só numa parte de cada bloco — por exemplo, calcular paridade/checksum sobre os primeiros k bytes de cada frame de um protocolo de rede.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
