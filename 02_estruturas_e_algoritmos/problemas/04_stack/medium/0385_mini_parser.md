# [0385] Mini Parser

> 🔗 [LeetCode 385](https://leetcode.com/problems/mini-parser/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#DFS`

## 📜 O Problema

Uma string `s` representa a serialização de uma lista aninhada. Implemente um parser para desserializá-la e retornar o `NestedInteger` correspondente. Cada elemento é um inteiro ou uma lista cujos elementos também podem ser inteiros ou outras listas.

O LeetCode fornece a interface `NestedInteger` já pronta (não é você quem a define), com os métodos: `isInteger()`, `getInteger()`, `setInteger(int)`, `add(NestedInteger)` e `getList()`.

**Exemplos:**
```
Input:  s = "324"
Output: 324
Explicação: um único NestedInteger contendo o inteiro 324.

Input:  s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explicação: uma lista aninhada com um inteiro (123) e outra lista aninhada,
que por sua vez tem um inteiro (456) e mais uma lista com um inteiro (789).
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 5 * 10^4` → precisa de solução O(n), uma única passada pela string
- `s` consiste de dígitos, colchetes `'[]'`, sinal de negativo `'-'` e vírgulas `','` → o parsing precisa distinguir números (possivelmente negativos e multi-dígito) de estrutura (colchetes/vírgulas)
- `s` é garantidamente a serialização de um `NestedInteger` válido → não é preciso validar formato, só interpretá-lo

## 🧭 Como reconhecer o padrão

"Parsear uma estrutura aninhada com colchetes, onde cada nível de aninhamento representa uma sublista" é a assinatura de stack: cada `'['` abre um novo nível (uma nova lista sendo construída), e cada `']'` fecha o nível atual, entregando-o de volta ao nível pai — exatamente o comportamento LIFO necessário para "lembrar" em qual lista você estava antes de descer um nível.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar recursão com um índice mutável (ou uma referência de posição) compartilhado entre chamadas: uma função que, ao encontrar `'['`, chama a si mesma recursivamente para processar a sublista, e ao encontrar `']'`, retorna o controle para quem chamou.

- Tempo: O(n) · Espaço: O(n) — profundidade da recursão proporcional ao nível de aninhamento, mais a pilha de chamadas do sistema
- **Por que não basta:** essa abordagem funciona e é O(n), mas a recursão usa a **call stack** implícita da linguagem para rastrear os níveis — o que pode estourar (`StackOverflowError`) em entradas muito aninhadas dentro do limite de 5*10^4 caracteres. Uma pilha explícita (iterativa) tem o mesmo comportamento lógico sem depender da profundidade de recursão da linguagem.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se `s` não começa com `'['`, é só um número — retorne-o direto, sem pilha. Caso contrário, percorra `s` com uma pilha explícita de `NestedInteger` (cada elemento da pilha é uma lista sendo construída). Acumule dígitos (e o sinal `'-'`) num buffer de número. A cada `'['`, empilhe uma nova lista vazia (a lista pai anterior, se existir, "aguarda" no nível abaixo). A cada `','` ou `']'`: se havia um número acumulado no buffer, adicione-o à lista do topo da pilha e limpe o buffer. Além disso, em `']'`: a lista do topo terminou — desempilhe-a e, se ainda sobrar algo na pilha, adicione essa lista completa como elemento da nova lista do topo (o pai).

## 🎬 Exemplo passo a passo

`s = "[123,[456,[789]]]"`

| Passo | Caractere | Ação | Pilha (níveis) após |
|---|---|---|---|
| 1 | `[` | empilha lista vazia (nível 1) | `[ [] ]` |
| 2 | `1`,`2`,`3` | acumula no buffer `num="123"` | `[ [] ]` |
| 3 | `,` | fecha número: adiciona 123 à lista do topo | `[ [123] ]` |
| 4 | `[` | empilha lista vazia (nível 2) | `[ [123], [] ]` |
| 5 | `4`,`5`,`6` | acumula `num="456"` | `[ [123], [] ]` |
| 6 | `,` | fecha número: adiciona 456 ao topo (nível 2) | `[ [123], [456] ]` |
| 7 | `[` | empilha lista vazia (nível 3) | `[ [123], [456], [] ]` |
| 8 | `7`,`8`,`9` | acumula `num="789"` | `[ [123], [456], [] ]` |
| 9 | `]` | fecha número (789 no topo); desempilha nível 3 completo `[789]`; adiciona ao novo topo (nível 2) | `[ [123], [456, [789]] ]` |
| 10 | `]` | sem número pendente; desempilha nível 2 completo `[456,[789]]`; adiciona ao novo topo (nível 1) | `[ [123, [456,[789]]] ]` |
| 11 | `]` | sem número pendente; desempilha nível 1 completo; pilha vazia → esse é o resultado final | — |

Resultado final: `[123, [456, [789]]]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string
- **Espaço:** O(n) — pilha explícita cuja profundidade máxima é o nível de aninhamento máximo da entrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
// NestedInteger é fornecida pelo LeetCode como interface pronta (não a implementamos aqui).
public NestedInteger deserialize(String s) {
    if (s.charAt(0) != '[') {
        return new NestedInteger(Integer.parseInt(s)); // caso base: string é só um número
    }

    Deque<NestedInteger> pilha = new ArrayDeque<>();
    NestedInteger atual = null;
    int num = 0;
    boolean temNumero = false;
    boolean negativo = false;

    for (char c : s.toCharArray()) {
        if (c == '[') {
            NestedInteger novaLista = new NestedInteger();
            if (atual != null) {
                pilha.push(atual); // o nível anterior "aguarda" empilhado
            }
            atual = novaLista;
        } else if (c == '-') {
            negativo = true;
        } else if (Character.isDigit(c)) {
            num = num * 10 + (c - '0');
            temNumero = true;
        } else if (c == ',' || c == ']') {
            if (temNumero) {
                atual.add(new NestedInteger(negativo ? -num : num));
                num = 0;
                temNumero = false;
                negativo = false;
            }
            if (c == ']' && !pilha.isEmpty()) {
                NestedInteger filhaCompleta = atual;
                atual = pilha.pop();          // volta para o nível pai
                atual.add(filhaCompleta);     // anexa a lista recém-fechada como elemento do pai
            }
        }
    }

    return atual; // quando a pilha esvazia, "atual" já é o NestedInteger raiz completo
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

- Esquecer de tratar números **negativos** — o sinal `'-'` aparece antes dos dígitos e precisa ser capturado num flag separado, já que não é um dígito nem um caractere de estrutura.
- Não tratar o caso base "a string inteira é só um número" (`"324"`, sem colchetes) — testar `s.charAt(0) != '['` antes de entrar na lógica de pilha evita processamento desnecessário e um bug sutil (a lógica de pilha assume que sempre existe um `'['` inicial).
- Esquecer de "fechar" o número pendente também no caractere `']'`, não só na `','` — o último número de uma lista (ex.: o `789` antes do primeiro `]` no exemplo) não é seguido por vírgula, só pelo fechamento direto.
- Confundir a ordem de "desempilhar o nível atual" com "anexar ao pai" — primeiro você precisa guardar a lista recém-fechada (`atual`), DEPOIS trocar `atual` para o pai (`pilha.pop()`), e só então anexar a lista guardada ao novo `atual`; inverter a ordem perde a referência.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só um número (sem colchetes) | `"324"` | `324` | caso base, sem nenhuma estrutura de lista |
| Número negativo | `"-123"` | `-123` | testa o tratamento do sinal antes dos dígitos |
| Lista vazia | `"[]"` | `[]` | nenhum número é adicionado, mas a lista existe |
| Aninhamento profundo | `"[123,[456,[789]]]"` | `[123,[456,[789]]]` | testa múltiplos níveis de empilhar/desempilhar em sequência |

## 🔗 Conexões

- Problemas irmãos: [0341] Flatten Nested List Iterator (mesma estrutura `NestedInteger`, mas percorrendo em vez de construindo), [0394] Decode String (mesma técnica de pilha para estruturas aninhadas com colchetes, mas para repetição de substrings em vez de listas de números)
- No backend: parsing de estruturas aninhadas com pilha é a base de parsers de JSON/YAML feitos à mão, de árvores de sintaxe abstrata (AST) de compiladores, e de qualquer formato de serialização hierárquico onde a profundidade não é conhecida de antemão.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
