# [0394] Decode String

> 🔗 [LeetCode 394](https://leetcode.com/problems/decode-string/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Recursion`

## 📜 O Problema

Dada uma string codificada, retorne sua string decodificada. A regra de codificação é `k[string_codificada]`, onde `string_codificada` dentro dos colchetes é repetida exatamente `k` vezes. A entrada é sempre válida (colchetes bem formados, `k` sempre inteiro positivo, e os dados originais não contêm dígitos).

**Exemplos:**
```
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"

Input:  s = "3[a2[c]]"
Output: "accaccacc"

Input:  s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 30` → tamanho de entrada minúsculo, mas o resultado pode crescer exponencialmente com aninhamento (`k`s multiplicativos); a saída é garantida não passar de `10^5`
- `s` consiste de letras minúsculas, dígitos e colchetes → dígitos só aparecem como multiplicadores `k`, nunca como dado literal
- Todos os inteiros em `s` estão em `[1, 300]` → `k` pode ter múltiplos dígitos (ex.: "300"), então é preciso acumular dígitos, não tratar cada um isoladamente

## 🧭 Como reconhecer o padrão

"Expandir uma estrutura aninhada `k[...]` onde o conteúdo dentro dos colchetes pode ele mesmo conter outra estrutura `k[...]`" é a assinatura de stack para aninhamento: cada `'['` abre um novo "contexto" de construção (uma nova substring sendo montada, com seu próprio multiplicador pendente), e cada `']'` fecha esse contexto, multiplicando o que foi construído e devolvendo o controle ao contexto pai — exatamente como [0385] Mini Parser e [0388] Longest Absolute File Path rastreiam níveis de aninhamento.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar recursão: uma função que processa a string a partir de um índice, e ao encontrar `'['`, chama a si mesma recursivamente para decodificar o conteúdo interno até o `']'` correspondente, multiplicando o resultado pelo `k` local.

- Tempo: O(n × tamanho_máximo_de_saída) · Espaço: O(profundidade de aninhamento) na call stack
- **Por que não basta:** funciona e tem a mesma complexidade da solução iterativa, mas depende da call stack da linguagem para rastrear os níveis — para entradas muito aninhadas (mesmo dentro de `n<=30`, aninhamentos profundos como `"2[2[2[2[...]]]]"` são possíveis), isso arrisca estouro de pilha de chamadas em linguagens com limites baixos de recursão. Uma pilha explícita evita essa dependência.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use duas pilhas em paralelo (ou uma pilha de pares): uma para os **números** pendentes (`k` acumulado) e outra para as **strings parciais** já construídas em cada nível. Percorra `s` acumulando dígitos num número, e caracteres normais numa string "atual". Ao encontrar `'['`: empilhe o número acumulado e a string atual construída até agora (o contexto do nível pai), depois zere ambos para começar um novo nível. Ao encontrar `']'`: o nível atual terminou — desempilhe o número `k` e a string do pai, e atualize a string atual para `stringPai + (stringAtual repetida k vezes)`. Caracteres normais só se acumulam na string atual.

## 🎬 Exemplo passo a passo

`s = "3[a2[c]]"`

| Passo | Caractere | Ação | numAtual | strAtual | Pilha (num, str) |
|---|---|---|---|---|---|
| 1 | `3` | acumula dígito | 3 | `""` | `[]` |
| 2 | `[` | empilha (3, `""`); zera | 0 | `""` | `[(3, "")]` |
| 3 | `a` | acumula letra | 0 | `"a"` | `[(3, "")]` |
| 4 | `2` | acumula dígito | 2 | `"a"` | `[(3, "")]` |
| 5 | `[` | empilha (2, `"a"`); zera | 0 | `""` | `[(3,""), (2,"a")]` |
| 6 | `c` | acumula letra | 0 | `"c"` | `[(3,""), (2,"a")]` |
| 7 | `]` | desempilha (2, `"a"`): strAtual = `"a" + "c"*2 = "acc"` | — | `"acc"` | `[(3,"")]` |
| 8 | `]` | desempilha (3, `""`): strAtual = `"" + "acc"*3 = "accaccacc"` | — | `"accaccacc"` | `[]` |

Resultado final: `"accaccacc"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n × maxK) no pior caso, onde a expansão total é limitada pela garantia do enunciado de que a saída não excede `10^5` caracteres
- **Espaço:** O(n + tamanho da saída) — as pilhas guardam contextos pendentes proporcionais à profundidade de aninhamento, e a string final ocupa o espaço da saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String decodeString(String s) {
    Deque<Integer> numeros = new ArrayDeque<>();
    Deque<StringBuilder> strings = new ArrayDeque<>();
    StringBuilder atual = new StringBuilder();
    int num = 0;

    for (char c : s.toCharArray()) {
        if (Character.isDigit(c)) {
            num = num * 10 + (c - '0'); // acumula multiplicadores de múltiplos dígitos (ex.: "300")
        } else if (c == '[') {
            numeros.push(num);
            strings.push(atual);
            num = 0;
            atual = new StringBuilder(); // novo contexto começa vazio
        } else if (c == ']') {
            int k = numeros.pop();
            StringBuilder anterior = strings.pop();
            for (int i = 0; i < k; i++) {
                anterior.append(atual);   // repete o conteúdo do nível que acabou de fechar
            }
            atual = anterior;             // o contexto pai retoma, já com o conteúdo expandido anexado
        } else {
            atual.append(c);              // letra comum: só acumula
        }
    }

    return atual.toString();
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

- Tratar `k` como um único dígito, ignorando números multi-dígito — a restrição garante `k` até 300, então `num = num*10 + digito` é obrigatório, não basta `num = digito`.
- Esquecer de zerar `num` e criar uma nova string ao abrir `'['` — sem isso, o multiplicador e o conteúdo de um nível vazam para o próximo, misturando contextos.
- Inverter a ordem em `']'`: fazer `atual + anterior*k` em vez de `anterior + atual*k` — o conteúdo do nível interno (`atual`) é o que se repete `k` vezes, e o resultado se **anexa** ao que já existia no nível pai (`anterior`), não o contrário.
- Esquecer que caracteres fora de qualquer `[...]` (como o `"ef"` no exemplo `"2[abc]3[cd]ef"`) também precisam ser acumulados em `atual` normalmente — eles não pertencem a nenhuma repetição, só ficam anexados ao final.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Múltiplos grupos independentes | `"3[a]2[bc]"` | `"aaabcbc"` | dois níveis irmãos (não aninhados), testa reinício de contexto |
| Aninhamento de dois níveis | `"3[a2[c]]"` | `"accaccacc"` | testa multiplicação em cascata entre níveis |
| Caracteres soltos fora de colchetes | `"2[abc]3[cd]ef"` | `"abcabccdcdcdef"` | testa que texto fora de `[...]` é preservado ao final |
| Multiplicador com múltiplos dígitos | `"10[a]"` (dentro do limite k<=300) | `"aaaaaaaaaa"` | testa que dígitos multi-caractere são acumulados corretamente antes do `[` |

## 🔗 Conexões

- Problemas irmãos: [0385] Mini Parser (mesma técnica de pilha para parsear estruturas aninhadas com colchetes), [0071] Simplify Path (outra pilha rastreando contexto por nível, aplicada a caminhos de arquivo)
- No backend: expansão de estruturas comprimidas com repetição aninhada é o mesmo princípio de algoritmos de compressão run-length com aninhamento (formatos de arquivo comprimido), e de templates de geração de conteúdo com repetição parametrizada (ex.: gerar HTML repetindo blocos aninhados N vezes a partir de uma definição compacta).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
