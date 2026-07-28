# [1047] Remove All Adjacent Duplicates In String

> 🔗 [LeetCode 1047](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#String` `#Easy`

## 📜 O Problema

Você recebe uma string `s` de letras minúsculas do inglês. Uma **remoção de duplicata** consiste em escolher duas letras **adjacentes e iguais** e removê-las. Você aplica remoções repetidamente até não conseguir mais. Retorne a string final.

**Exemplos:**
```
Input:  s = "abbaca"
Output: "ca"
Explicação: removendo "bb" → "aaca"; removendo "aa" → "ca". Resultado final: "ca".

Input:  s = "azxxzy"
Output: "ay"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → precisa de O(n); simular remoções repetidas com reconstrução de string a cada passo seria caro
- `s` consiste só de letras minúsculas do inglês → não há outros caracteres a considerar

## 🧭 Como reconhecer o padrão

"Remover repetidamente um par adjacente e igual, e a remoção pode criar um **novo** par adjacente" é a assinatura de stack: ao processar caractere por caractere, o candidato a formar par com o atual é sempre o **último caractere ainda não cancelado** — exatamente o topo de uma pilha. Quando um par cancela, o próximo caractere pode formar par com quem ficou por baixo, o que a pilha resolve naturalmente ao continuar o processo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Repetidamente varrer a string procurando o primeiro par de caracteres adjacentes iguais, remover esse par (reconstruindo a string), e recomeçar a busca do zero até nenhuma remoção ser mais possível.

- Tempo: O(n²) pior caso · Espaço: O(n) por cópia
- **Por que não basta:** cada remoção pode exigir uma nova varredura completa da string (por exemplo, `"aaaaaa"` colapsa em várias rodadas), e strings em Java/Python são imutáveis, então cada "remoção" na prática recria uma string inteira nova — para `n = 10^5`, isso explode.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` uma única vez com uma pilha. Para cada caractere: se ele for igual ao topo da pilha, isso significa que ele forma um par adjacente com o topo — desempilhe (cancelando os dois). Caso contrário, empilhe o caractere. No final, o que sobrou na pilha, na ordem de baixo para cima, é a string resultante — porque cada cancelamento já considerou automaticamente os caracteres que "ficaram expostos" depois de cancelamentos anteriores.

## 🎬 Exemplo passo a passo

`s = "azxxzy"`

| Passo | Caractere | Compara com topo | Ação | Pilha após |
|---|---|---|---|---|
| 1 | `a` | pilha vazia | empilha | `[a]` |
| 2 | `z` | topo é `a`, diferente | empilha | `[a, z]` |
| 3 | `x` | topo é `z`, diferente | empilha | `[a, z, x]` |
| 4 | `x` | topo é `x`, **igual** | desempilha (cancela par) | `[a, z]` |
| 5 | `z` | topo é `z`, **igual** | desempilha (cancela par) | `[a]` |
| 6 | `y` | topo é `a`, diferente | empilha | `[a, y]` |

Resultado final: `"ay"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere é empilhado e desempilhado no máximo uma vez
- **Espaço:** O(n) — pior caso (nenhuma duplicata adjacente), todos os caracteres ficam na pilha

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String removeDuplicates(String s) {
    Deque<Character> pilha = new ArrayDeque<>();

    for (char c : s.toCharArray()) {
        if (!pilha.isEmpty() && pilha.peek() == c) {
            pilha.pop();              // cancela o par: o atual e o topo se anulam
        } else {
            pilha.push(c);
        }
    }

    // a pilha guarda o resultado de baixo pra cima; reconstrua na ordem certa
    StringBuilder resultado = new StringBuilder();
    while (!pilha.isEmpty()) {
        resultado.append(pilha.pop());
    }
    return resultado.reverse().toString(); // desempilhar inverte a ordem, então reverte de volta
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

- Esquecer de checar `pilha.isEmpty()` antes de `pilha.peek()` — no primeiro caractere (ou logo após um cancelamento que esvazia a pilha), comparar com o topo de uma pilha vazia lança exceção.
- Reconstruir a string na ordem errada — desempilhar (`pop`) devolve os caracteres de cima para baixo, que é a ordem **inversa** da string final; é preciso reverter o resultado (ou usar uma estrutura que permita iterar de baixo para cima, como um `Deque` com `addFirst`).
- Achar que basta uma passada "olhando só para trás" sem estrutura de pilha, comparando `s[i]` com `s[i-1]` diretamente no array original — isso falha quando um cancelamento expõe um novo par que não era adjacente originalmente (ex.: `"abba"`: comparar índices fixos não captura que, depois de cancelar `"bb"`, sobra `"aa"` adjacente).
- Confundir "remover duplicatas adjacentes" com "remover todas as ocorrências de caracteres duplicados" (como em problemas de deduplicação geral) — aqui só pares **adjacentes e consecutivos** contam.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Cancelamento em cascata | `"abbaca"` | `"ca"` | um cancelamento expõe outro par, que também precisa cancelar |
| Toda a string cancela | `"aabbcc"` | `""` | todos os pares se anulam, sobra pilha vazia |
| Nenhuma duplicata adjacente | `"abcde"` | `"abcde"` | nada é cancelado, string retorna intacta |
| Caractere único | `"z"` | `"z"` | pilha nunca tem par para comparar |

## 🔗 Conexões

- Problemas irmãos: [1544] Make The String Great (mesma técnica, mas o "par" é definido por case diferente da mesma letra em vez de igualdade exata), [2696] Minimum String Length After Removing Substrings (mesma ideia de cancelamento em cascata com pilha, mas removendo substrings de 2 caracteres específicas)
- No backend: cancelamento em cascata com pilha aparece em parsers de expressões que simplificam sequências (ex.: `"++"` e `"--"` em compressão de path, ou simplificação de expressões matemáticas com termos que se cancelam), e em qualquer processamento de stream onde eventos consecutivos e opostos se anulam (like/unlike, ação/desfazer em sequência).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
