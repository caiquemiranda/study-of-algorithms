# [3174] Clear Digits

> 🔗 [LeetCode 3174](https://leetcode.com/problems/clear-digits/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Simulation`

## 📜 O Problema

Você recebe uma string `s`. Sua tarefa é remover **todos** os dígitos repetindo esta operação:

- Delete o **primeiro** dígito e o caractere **não-dígito** mais próximo à sua **esquerda**.

Retorne a string resultante após remover todos os dígitos. A operação **não pode** ser feita num dígito que não tenha nenhum caractere não-dígito à esquerda (a entrada garante que sempre é possível remover todos os dígitos).

**Exemplos:**
```
Input:  s = "abc"
Output: "abc"
Explicação: não há dígito na string.

Input:  s = "cb34"
Output: ""
Explicação:
- Aplica a operação em s[2] ('3'): remove '3' e o não-dígito mais próximo à esquerda ('b') → s = "c4".
- Aplica a operação em s[1] ('4'): remove '4' e o não-dígito mais próximo à esquerda ('c') → s = "".
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → tamanho minúsculo, qualquer solução O(n) é folgada
- `s` consiste só de letras minúsculas e dígitos → só duas categorias de caractere a distinguir
- A entrada é garantida permitir deletar todos os dígitos → não é preciso tratar o caso "sobra um dígito sem letra à esquerda"

## 🧭 Como reconhecer o padrão

"Cada dígito cancela o caractere não-dígito **mais próximo à esquerda** (o mais recente ainda não cancelado)" é exatamente o comportamento LIFO de uma pilha: ao processar a string da esquerda para a direita, o "não-dígito mais próximo à esquerda" de um dígito é sempre o topo da pilha de não-dígitos ainda pendentes naquele momento.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Repetidamente encontrar o primeiro dígito na string, localizar o não-dígito mais próximo à sua esquerda, remover ambos (reconstruindo a string), e recomeçar a busca do zero até não sobrar nenhum dígito.

- Tempo: O(n²) pior caso · Espaço: O(n) por cópia
- **Por que não basta:** cada remoção pode exigir uma nova varredura completa da string à procura do próximo dígito e da letra mais próxima à esquerda. Mesmo com `n <= 100` isso passaria, mas a solução com pilha resolve tudo em uma única passada, sem refazer buscas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` uma vez com uma pilha. Para cada caractere: se for um **dígito**, ele cancela o não-dígito no topo da pilha — desempilhe (e não empilhe o dígito, já que ele também é removido pela operação). Se for uma **letra**, empilhe-a normalmente (ela é uma candidata a ser cancelada por um dígito futuro). No final, o que sobrar na pilha, de baixo para cima, é o resultado — porque cada cancelamento já considerou automaticamente as letras que "ficaram expostas" depois de cancelamentos anteriores.

## 🎬 Exemplo passo a passo

`s = "cb34"`

| Passo | Caractere | É dígito? | Ação | Pilha após |
|---|---|---|---|---|
| 1 | `c` | não | empilha | `[c]` |
| 2 | `b` | não | empilha | `[c, b]` |
| 3 | `3` | sim | cancela o topo (`b`) | `[c]` |
| 4 | `4` | sim | cancela o topo (`c`) | `[]` |

Resultado final: pilha vazia → `""` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string, cada caractere empilhado/desempilhado no máximo uma vez
- **Espaço:** O(n) — pior caso (nenhum dígito), todas as letras ficam na pilha

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String clearDigits(String s) {
    Deque<Character> pilha = new ArrayDeque<>();

    for (char c : s.toCharArray()) {
        if (Character.isDigit(c)) {
            pilha.pop();          // dígito cancela o não-dígito mais próximo à esquerda (topo)
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

- Empilhar o dígito por engano em vez de só desempilhar — o dígito também é removido pela operação, ele nunca deveria entrar na pilha.
- Reconstruir a string na ordem errada — desempilhar devolve os caracteres de cima para baixo (ordem inversa da string final); é preciso reverter o resultado.
- Achar que "o mais próximo à esquerda" exige buscar retroativamente na string original a cada dígito — como a pilha só contém as letras **ainda não canceladas**, o topo dela já É o não-dígito mais próximo à esquerda no estado atual, sem precisar buscar de novo.
- Confundir esta técnica com [1047]/[2696] (que cancelam **pares de caracteres iguais/específicos entre si**) — aqui o cancelamento é entre categorias diferentes (dígito cancela letra), não entre dois caracteres do mesmo tipo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem nenhum dígito | `"abc"` | `"abc"` | pilha nunca é afetada por cancelamento |
| Cancelamento total | `"cb34"` | `""` | cada dígito cancela a letra mais recente até esvaziar |
| Letra sobrevive entre dígitos distantes | `"a1b2"` | `""` | `1` cancela `a`, depois `b` empilha e `2` cancela `b` |
| Múltiplas letras seguidas de um só dígito | `"abc1"` | `"ab"` | só a letra mais próxima à esquerda (`c`) é cancelada, as demais permanecem |

## 🔗 Conexões

- Problemas irmãos: [1047] Remove All Adjacent Duplicates In String (mesma estrutura de pilha, mas cancelando pares idênticos adjacentes), [2696] Minimum String Length After Removing Substrings (cancelamento em cascata de substrings fixas com pilha)
- No backend: "o evento mais recente pendente é cancelado pelo próximo evento de tipo oposto" é o mesmo padrão de matching de eventos abre/fecha em parsers e em sistemas de log que casam eventos de início/fim (ex.: um evento de "erro" que cancela o alerta pendente mais recente daquele tipo).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
