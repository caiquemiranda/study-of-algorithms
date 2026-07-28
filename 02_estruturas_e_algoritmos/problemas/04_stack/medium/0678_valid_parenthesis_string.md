# [0678] Valid Parenthesis String

> 🔗 [LeetCode 678](https://leetcode.com/problems/valid-parenthesis-string/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Greedy` `#String`

## 📜 O Problema

Dada uma string `s` contendo só `'('`, `')'` e `'*'`, retorne `true` se `s` for **válida**. Uma string válida obedece: todo `'('` deve ter um `')'` correspondente; todo `')'` deve ter um `'('` correspondente; `'('` deve vir antes do `')'` correspondente; e `'*'` pode ser tratado como `'('`, como `')'`, ou como string vazia `""`.

**Exemplos:**
```
Input:  s = "()"
Output: true

Input:  s = "(*)"
Output: true

Input:  s = "(*))"
Output: true
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → tamanho minúsculo, mas o número de combinações de interpretação de `'*'` cresce exponencialmente (3^(número de asteriscos)), então força bruta por combinação é inviável mesmo assim
- `s[i]` é `'('`, `')'` ou `'*'` → só três símbolos possíveis, cada um com um papel bem definido

## 🧭 Como reconhecer o padrão

Esta é uma variação de [0020] Valid Parentheses com um **coringa** (`'*'`) que pode assumir três papéis diferentes. A técnica de duas pilhas trata cada tipo de símbolo aberto separadamente: uma pilha de índices de `'('` e outra de índices de `'*'`. Quando um `')'` aparece, ele prefere fechar um `'('` real primeiro (preservando os `'*'` como coringas flexíveis para depois); só usa um `'*'` como fechamento se não houver `'('` disponível.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `'*'` na string, testar recursivamente as três interpretações possíveis (`'('`, `')'` ou vazio), validando a string resultante como parênteses simples ([0020]) em cada combinação.

- Tempo: O(3^k × n), onde `k` é o número de asteriscos · Espaço: O(k) pela recursão
- **Por que não basta:** o número de combinações cresce exponencialmente com a quantidade de `'*'` — uma string de 100 caracteres, quase todos asteriscos, geraria até 3^100 combinações. É preciso decidir o papel de cada `'*'` de forma gulosa, sem enumerar alternativas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use duas pilhas de **índices**: `abre` para `'('` e `estrela` para `'*'`. Percorra `s`: em `'('`, empilhe o índice em `abre`; em `'*'`, empilhe em `estrela`; em `')'`, primeiro tente fechar com um `'('` real (desempilhe de `abre`, se houver); se não houver, use um `'*'` como fechamento (desempilhe de `estrela`); se nenhum dos dois estiver disponível, a string é inválida (fechamento sem nada para casar). No final, todo `'('` que sobrou em `abre` precisa ser coberto por um `'*'` que esteja **à sua direita** (índice maior) em `estrela` (usado como `')'` virtual) — casando os dois de fora para dentro (do topo de cada pilha), tratando ambos como possíveis fechamentos.

## 🎬 Exemplo passo a passo

`s = "(*))"`

| Passo | i | Caractere | Ação | abre após | estrela após |
|---|---|---|---|---|---|
| 1 | 0 | `(` | empilha índice em `abre` | `[0]` | `[]` |
| 2 | 1 | `*` | empilha índice em `estrela` | `[0]` | `[1]` |
| 3 | 2 | `)` | tenta `abre` primeiro → desempilha `0` | `[]` | `[1]` |
| 4 | 3 | `)` | `abre` vazio → usa `estrela` → desempilha `1` | `[]` | `[]` |

Ao final, `abre` está vazio → não sobrou nenhum `'('` sem par.

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string, cada índice empilhado/desempilhado no máximo uma vez em cada pilha
- **Espaço:** O(n) — as duas pilhas guardam no máximo todos os índices de `'('` e `'*'`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean checkValidString(String s) {
    Deque<Integer> abre = new ArrayDeque<>();     // índices de '(' ainda não fechados
    Deque<Integer> estrela = new ArrayDeque<>();  // índices de '*' ainda não usados

    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(') {
            abre.push(i);
        } else if (c == '*') {
            estrela.push(i);
        } else { // c == ')'
            if (!abre.isEmpty()) {
                abre.pop();          // prefere fechar com um '(' real
            } else if (!estrela.isEmpty()) {
                estrela.pop();       // sem '(' disponível: usa um '*' como ')'
            } else {
                return false;        // fechamento sem nada para casar
            }
        }
    }

    // todo '(' que sobrou precisa de um '*' à sua DIREITA (índice maior) para virar ')'
    while (!abre.isEmpty()) {
        if (estrela.isEmpty() || estrela.peek() < abre.peek()) {
            return false; // não há '*' suficiente à direita para cobrir este '('
        }
        abre.pop();
        estrela.pop();
    }

    return true;
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

- Usar um `'*'` como fechamento antes de esgotar os `'('` reais disponíveis — isso desperdiça a flexibilidade do `'*'`; sempre prefira fechar com `'('` real primeiro, guardando os asteriscos para o caso de sobrarem `'('` sem par no final.
- Esquecer a checagem de **posição relativa** ao casar `'('` sobrando com `'*'` no final — um `'*'` só pode servir como `')'` se estiver **depois** do `'('` na string (índice maior); ignorar essa ordem permitiria casamentos que violam a regra "abre antes de fechar".
- Tentar resolver com uma única pilha misturando `'('` e `'*'` sem distinguir os tipos — perde a informação de qual símbolo pode ser reinterpretado como vazio, necessária para a validação final.
- Retornar `false` prematuramente ao encontrar `')'` sem `'('` nem `'*'` disponíveis **no momento**, mas esquecer que a checagem correta é justamente essa (não há como um fechamento "esperar" por uma abertura futura) — essa parte, na verdade, está certa por definição do problema (abertura sempre precisa vir antes).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Asterisco como vazio | `"(*)"` | true | o `*` pode ser interpretado como string vazia, deixando `"()"` |
| Mais fechamentos que aberturas, cobertos por asterisco | `"(*))"` | true | testa o uso de `*` tanto como abertura quanto como fechamento em contextos diferentes |
| Fechamento sem nada para casar | `")("` | false | o primeiro `)` não tem `(` nem `*` disponível antes dele |
| Só asteriscos | `"***"` | true | todos podem virar string vazia, resultando em string válida vazia |

## 🔗 Conexões

- Problemas irmãos: [0020] Valid Parentheses (a versão sem coringa, mesma técnica base de pilha), [0856] Score of Parentheses (outra manipulação de parênteses balanceados com pilha, mas calculando pontuação em vez de validade)
- No backend: validação de sintaxe com símbolos opcionais/curinga aparece em parsers tolerantes a erro (ex.: autocompletar de código que aceita parênteses não fechados temporariamente) e em validadores de templates onde certos delimitadores são opcionais dependendo do contexto.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
