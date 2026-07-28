# [0856] Score of Parentheses

> 🔗 [LeetCode 856](https://leetcode.com/problems/score-of-parentheses/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Medium`

## 📜 O Problema

Dada uma string de parênteses balanceada `s`, retorne a **pontuação** da string, segundo as regras: `"()"` tem pontuação `1`; `AB` tem pontuação `A + B`, onde `A` e `B` são strings balanceadas; `(A)` tem pontuação `2 * A`, onde `A` é uma string balanceada.

**Exemplos:**
```
Input:  s = "()"
Output: 1

Input:  s = "(())"
Output: 2

Input:  s = "()()"
Output: 2
```

**Restrições (e o que elas denunciam):**
- `2 <= s.length <= 50` → tamanho minúsculo, qualquer solução O(n) é folgada
- `s` consiste só de `'('` e `')'`, garantidamente balanceada → não é preciso validar a string, só calcular a pontuação

## 🧭 Como reconhecer o padrão

"Calcular uma pontuação que depende do nível de aninhamento, onde cada nível **dobra** a pontuação do que está dentro dele" é a assinatura de stack: cada `'('` abre um novo "escopo de pontuação" que começa em zero, e cada `')'` fecha esse escopo, aplicando a regra `max(2 × pontuação_interna, 1)` e somando o resultado ao escopo pai — exatamente o comportamento de acumular e propagar valores por nível que uma pilha resolve naturalmente.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar recursão: encontrar o par de parênteses mais externo e seu conteúdo interno, calcular recursivamente a pontuação do conteúdo, multiplicar por 2 (ou usar 1 se vazio), e somar com a pontuação do restante da string ao lado.

- Tempo: O(n²) no pior caso (encontrar o parêntese correspondente a cada nível pode exigir varrer a string) · Espaço: O(n) pela recursão
- **Por que não basta:** localizar repetidamente o parêntese de fechamento correspondente a cada `'('` externo (para separar "dentro" de "fora") pode degradar para O(n²) se feito ingenuamente a cada chamada recursiva. Uma pilha processa a string numa única passada O(n), sem precisar localizar pares correspondentes explicitamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use uma pilha de inteiros, começando com um `0` (representando a pontuação do escopo mais externo, "fora" de qualquer parêntese). Para cada `'('`: empilhe um novo `0` — um novo escopo de pontuação começa vazio. Para cada `')'`: desempilhe o valor do escopo que acabou de fechar (`v`), calcule sua contribuição como `max(2*v, 1)` (a regra `"()"` = 1 é o caso especial de escopo vazio, onde `2*0=0` não seria válido), e **some** essa contribuição ao novo topo da pilha (o escopo pai, que agora recebe esse valor como parte do seu próprio conteúdo). No final, o único valor que sobra na pilha é a pontuação total.

## 🎬 Exemplo passo a passo

`s = "(())"`

| Passo | Caractere | Ação | Pilha após |
|---|---|---|---|
| 1 | (início) | pilha começa com escopo externo | `[0]` |
| 2 | `(` | novo escopo (nível 1) | `[0, 0]` |
| 3 | `(` | novo escopo (nível 2) | `[0, 0, 0]` |
| 4 | `)` | fecha nível 2: `v=0` → contribuição `max(0,1)=1`; soma ao pai (nível 1) | `[0, 1]` |
| 5 | `)` | fecha nível 1: `v=1` → contribuição `max(2,1)=2`; soma ao pai (nível 0) | `[2]` |

Resultado final: `2` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string, cada caractere processado em O(1)
- **Espaço:** O(n) — pilha, pior caso proporcional ao nível máximo de aninhamento (até n/2 níveis)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int scoreOfParentheses(String s) {
    Deque<Integer> pilha = new ArrayDeque<>();
    pilha.push(0); // escopo externo, pontuação acumulada começa em 0

    for (char c : s.toCharArray()) {
        if (c == '(') {
            pilha.push(0); // novo escopo, começa vazio
        } else {
            int v = pilha.pop();               // pontuação do escopo que acabou de fechar
            int contribuicao = Math.max(2 * v, 1); // "()" vazio vale 1; senão, dobra o conteúdo
            pilha.push(pilha.pop() + contribuicao); // soma ao escopo pai (novo topo)
        }
    }

    return pilha.pop(); // sobra só a pontuação total do escopo externo
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

- Usar `2 * v` sem o `max(..., 1)` — quando `v=0` (escopo vazio, ou seja, `"()"`  puro), `2*0=0` daria pontuação zero para o caso base, mas a regra do enunciado define explicitamente `"()"` como pontuação `1`; o `max` captura esse caso especial.
- Esquecer de **somar** (em vez de sobrescrever) a contribuição ao escopo pai — múltiplos grupos irmãos dentro do mesmo escopo (ex.: `"()()"`, onde ambos os `"()"` estão no escopo externo) precisam ter suas pontuações **somadas**, não substituídas uma pela outra.
- Inicializar a pilha vazia em vez de já com um `0` — sem esse escopo externo inicial, o primeiro `')'` da string não teria um "pai" para receber sua contribuição, causando erro de pilha vazia.
- Confundir a ordem de operações em `')'`: primeiro desempilhar o valor do escopo que fechou, calcular a contribuição, **depois** somar ao novo topo (que já é o escopo pai) — inverter a ordem mistura os valores.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso base único | `"()"` | 1 | escopo vazio, testa a regra especial `max(0,1)=1` |
| Aninhamento duplo | `"(())"` | 2 | um nível de aninhamento dobra a pontuação do caso base |
| Grupos irmãos somados | `"()()"` | 2 | dois grupos independentes no mesmo escopo, pontuações somadas (1+1) |
| Aninhamento profundo misto | `"(()(()))"` | 6 | combina aninhamento e soma de irmãos dentro de níveis diferentes, testando a interação completa da regra |

## 🔗 Conexões

- Problemas irmãos: [0020] Valid Parentheses (mesma estrutura de dados base, mas validando em vez de pontuar), [1021] Remove Outermost Parentheses (mesma ideia de rastrear níveis de parênteses, mas filtrando caracteres em vez de acumular pontuação)
- No backend: acumular valores por escopo aninhado, propagando para o escopo pai ao fechar, é o mesmo padrão usado em avaliadores de expressões aninhadas (calculadoras com parênteses), em cálculo de custo agregado de operações aninhadas em query planners de bancos de dados, e em contadores de complexidade ciclomática que somam a complexidade de blocos aninhados de código.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
