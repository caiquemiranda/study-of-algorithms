# [1544] Make The String Great

> 🔗 [LeetCode 1544](https://leetcode.com/problems/make-the-string-great/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` de letras minúsculas e maiúsculas do inglês. Uma string é **boa** se ela não tem dois caracteres adjacentes `s[i]` e `s[i+1]` onde um é a versão minúscula e o outro é a versão maiúscula da **mesma** letra (em qualquer ordem).

Para tornar a string boa, você pode escolher dois caracteres adjacentes que a tornam ruim e removê-los. Repita até a string ficar boa. Retorne a string resultante (garantida ser única). Uma string vazia também é boa.

**Exemplos:**
```
Input:  s = "leEeetcode"
Output: "leetcode"
Explicação: escolhendo i=1 ou i=2 (o par "Ee"), o resultado se reduz a "leetcode".

Input:  s = "abBAcC"
Output: ""
Explicação: "abBAcC" → "aAcC" → "cC" → ""

Input:  s = "s"
Output: "s"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → tamanho minúsculo, qualquer solução O(n) ou até O(n²) passaria; o problema é sobre a técnica correta, não performance
- `s` contém só letras minúsculas e maiúsculas do inglês → a "mesma letra em cases opostos" é verificável comparando os caracteres após normalizar case, ou comparando a diferença de código ASCII (32)

## 🧭 Como reconhecer o padrão

Igual ao [1047] Remove All Adjacent Duplicates In String, "remover repetidamente um par adjacente que satisfaz uma condição, onde a remoção pode expor um **novo** par adjacente que também precisa ser avaliado" é a assinatura de stack: o candidato a formar par com o caractere atual é sempre o último ainda não cancelado — o topo da pilha.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Repetidamente varrer a string procurando o primeiro par adjacente "ruim" (mesma letra, cases opostos), remover esse par reconstruindo a string, e recomeçar a busca do zero até não sobrar nenhum par ruim.

- Tempo: O(n²) pior caso · Espaço: O(n) por cópia
- **Por que não basta:** cada remoção pode exigir uma nova varredura completa (ex.: `"aAbBcC"` colapsa em várias rodadas em cascata). Mesmo com `n <= 100` isso passaria no tempo, mas não generaliza — e a solução com pilha resolve em uma única passada, sem reconstruir a string repetidamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` uma única vez com uma pilha. Para cada caractere: se a pilha não estiver vazia e o caractere do topo for a **mesma letra em case oposto** ao atual (ex.: `'e'` e `'E'`), isso forma um par "ruim" adjacente — desempilhe (cancelando os dois, sem empilhar o atual). Caso contrário, empilhe o caractere atual. No final, o que sobrou na pilha, de baixo para cima, é a string boa resultante.

## 🎬 Exemplo passo a passo

`s = "leEeetcode"`

| Passo | Caractere | Compara com topo | Ação | Pilha após |
|---|---|---|---|---|
| 1 | `l` | pilha vazia | empilha | `[l]` |
| 2 | `e` | topo `l`, não é par com `e` | empilha | `[l, e]` |
| 3 | `E` | topo `e`, mesma letra em case oposto → par ruim | desempilha | `[l]` |
| 4 | `e` | topo `l`, não é par | empilha | `[l, e]` |
| 5 | `e` | topo `e`, mesma letra e mesmo case → **não** é par ruim (a regra exige cases opostos) | empilha | `[l, e, e]` |
| 6 | `t` | topo `e`, não é par | empilha | `[l, e, e, t]` |
| 7 | `c` | topo `t`, não é par | empilha | `[l, e, e, t, c]` |
| 8 | `o` | topo `c`, não é par | empilha | `[l, e, e, t, c, o]` |
| 9 | `d` | topo `o`, não é par | empilha | `[l, e, e, t, c, o, d]` |
| 10 | `e` | topo `d`, não é par | empilha | `[l, e, e, t, c, o, d, e]` |

Resultado final (pilha de baixo para cima): `"leetcode"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere é empilhado e desempilhado no máximo uma vez
- **Espaço:** O(n) — pior caso, string já boa (sem nenhum par ruim), todos os caracteres ficam na pilha

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String makeGood(String s) {
    Deque<Character> pilha = new ArrayDeque<>();

    for (char c : s.toCharArray()) {
        // "mesma letra, case oposto" == diferença de 32 no código ASCII entre maiúscula e minúscula
        if (!pilha.isEmpty() && Math.abs(pilha.peek() - c) == 32) {
            pilha.pop();               // cancela o par ruim
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

- Usar `Character.toLowerCase(a) == Character.toLowerCase(b)` sozinho para detectar o par — isso captura "mesma letra", mas não garante que os **cases são opostos**; `"ee"` (mesma letra, mesmo case) não é um par ruim e não deve ser removido, só `"eE"`/`"Ee"`.
- Esquecer de checar `pilha.isEmpty()` antes de comparar com o topo — no primeiro caractere, ou logo após um cancelamento que esvazia a pilha, comparar com uma pilha vazia lança exceção.
- Reconstruir a string na ordem errada — desempilhar devolve os caracteres de cima para baixo (ordem inversa da string final); é preciso reverter o resultado.
- Achar que a diferença de 32 no código ASCII funciona para qualquer par de letras diferentes — ela só é válida quando as duas letras já são a **mesma letra** em cases opostos; `'a'` e `'C'`, por exemplo, também têm diferença diferente de 32, então a checagem de diferença de 32 já implicitamente garante "mesma letra" (não precisa de uma segunda comparação).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Cancelamento total em cascata | `"abBAcC"` | `""` | cada cancelamento expõe o próximo par ruim, até esvaziar |
| Mesma letra, mesmo case (não cancela) | `"aa"` | `"aa"` | mesmo case não é considerado "ruim", só cases opostos |
| Já é uma string boa | `"abc"` | `"abc"` | nenhum par se cancela, string retorna intacta |
| Caractere único | `"s"` | `"s"` | pilha nunca tem par para comparar |

## 🔗 Conexões

- Problemas irmãos: [1047] Remove All Adjacent Duplicates In String (mesma técnica de cancelamento com pilha, mas a condição de par é igualdade exata em vez de case oposto), [2696] Minimum String Length After Removing Substrings (cancelamento em cascata removendo substrings fixas de 2 caracteres)
- No backend: normalização/sanitização de strings com regras de cancelamento em cascata aparece em parsers de markup que colapsam tags de toggle opostas adjacentes (ex.: `<b></b>` vazio em editores de texto rico), e em qualquer pipeline de limpeza de dados onde um valor "cancela" o anterior segundo uma regra de negócio.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
