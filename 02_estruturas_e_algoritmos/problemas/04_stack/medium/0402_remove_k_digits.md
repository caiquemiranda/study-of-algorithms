# [0402] Remove K Digits

> 🔗 [LeetCode 402](https://leetcode.com/problems/remove-k-digits/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Greedy`

## 📜 O Problema

Dada uma string `num` representando um inteiro não-negativo, e um inteiro `k`, retorne o **menor** inteiro possível após remover exatamente `k` dígitos de `num`.

**Exemplos:**
```
Input:  num = "1432219", k = 3
Output: "1219"
Explicação: remova os três dígitos 4, 3 e 2 para formar 1219, o menor possível.

Input:  num = "10200", k = 1
Output: "200"
Explicação: remove o "1" inicial; a saída não deve ter zeros à esquerda.

Input:  num = "10", k = 2
Output: "0"
Explicação: remove todos os dígitos, sobra "nada", que é representado como "0".
```

**Restrições (e o que elas denunciam):**
- `1 <= k <= num.length <= 10^5` → precisa de solução O(n); testar todas as combinações de remoção é inviável
- `num` consiste só de dígitos, sem zeros à esquerda (exceto o próprio zero) → a entrada já é "limpa", mas a **saída** precisa remover zeros à esquerda que surgirem após as remoções
- `k` sempre é removível (até o limite de `num.length`) → o caso extremo de remover tudo (sobra `"0"`) é possível e precisa ser tratado

## 🧭 Como reconhecer o padrão

"Remover exatamente k elementos para minimizar o valor resultante, preservando a ordem relativa dos que restam" é a assinatura de **monotonic stack greedy**: para minimizar um número, você quer que os dígitos mais significativos (mais à esquerda) sejam os menores possíveis — então, sempre que um dígito novo for **menor** que o topo da pilha, vale a pena remover o topo (ele está "atrapalhando" ao ser maior e mais significativo que o que vem depois).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar todas as combinações de `num.length - k` dígitos (preservando a ordem original) e escolher a que forma o menor número.

- Tempo: O(C(n, n-k)) — exponencial · Espaço: exponencial
- **Por que não basta:** o número de combinações cresce combinatorialmente com `n`; para `n=10^5` é completamente inviável. É preciso uma decisão gulosa que remova o dígito certo em cada passo, sem enumerar alternativas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `num` da esquerda para a direita, construindo o resultado numa pilha. Para cada dígito: enquanto ainda restarem remoções disponíveis (`k > 0`) **e** o topo da pilha for **maior** que o dígito atual, desempilhe (remova o topo) e decremente `k` — isso melhora o resultado, porque um dígito maior mais à esquerda vale mais que um dígito maior mais à direita. Empilhe o dígito atual. Se sobrar `k > 0` ao final (a string já estava em ordem crescente, nada foi removido no meio), remova os `k` últimos dígitos da pilha (eles são os mais insignificantes, à direita). Por fim, remova zeros à esquerda do resultado, e trate string vazia como `"0"`.

## 🎬 Exemplo passo a passo

`num = "1432219"`, `k = 3`

| Passo | Dígito | Ação do while (topo > dígito e k>0) | Pilha após | k restante |
|---|---|---|---|---|
| 1 | `1` | pilha vazia | `[1]` | 3 |
| 2 | `4` | topo `1` < `4`, não remove | `[1,4]` | 3 |
| 3 | `3` | topo `4` > `3` → pop, k-- | `[1,3]` | 2 |
| 4 | `2` | topo `3` > `2` → pop, k--; topo agora `1` < `2`, para | `[1,2]` | 1 |
| 5 | `2` | topo `2` não é > `2` (igual), não remove | `[1,2,2]` | 1 |
| 6 | `1` | topo `2` > `1` → pop, k--; agora k=0, para (mesmo que o novo topo ainda seja maior) | `[1,2,1]` | 0 |
| 7 | `9` | k=0, não remove mais | `[1,2,1,9]` | 0 |

Pilha final: `"1219"`. Sem zeros à esquerda para remover, `k=0` (nada mais a cortar do final).

Resultado final: `"1219"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada dígito é empilhado e desempilhado no máximo uma vez
- **Espaço:** O(n) — a pilha guarda no máximo todos os dígitos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String removeKdigits(String num, int k) {
    Deque<Character> pilha = new ArrayDeque<>();

    for (char c : num.toCharArray()) {
        // remove dígitos maiores no topo enquanto ainda houver remoções disponíveis
        while (k > 0 && !pilha.isEmpty() && pilha.peek() > c) {
            pilha.pop();
            k--;
        }
        pilha.push(c);
    }

    // se sobrou k > 0, a string já era crescente: remove os k últimos (mais insignificantes)
    while (k > 0) {
        pilha.pop();
        k--;
    }

    // reconstrói na ordem correta (pilha guarda de baixo pra cima o resultado)
    StringBuilder resultado = new StringBuilder();
    while (!pilha.isEmpty()) {
        resultado.append(pilha.pop());
    }
    resultado.reverse();

    // remove zeros à esquerda
    int i = 0;
    while (i < resultado.length() - 1 && resultado.charAt(i) == '0') {
        i++;
    }
    String semZeros = resultado.substring(i);

    return semZeros.isEmpty() ? "0" : semZeros;
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

- Esquecer o caso em que `k` ainda sobra depois de percorrer toda a string (quando `num` já é não-decrescente, ex.: `"12345"` com `k=2`) — nesse caso, nenhuma remoção acontece durante o loop principal, e os `k` últimos dígitos da pilha precisam ser removidos manualmente ao final.
- Esquecer de remover zeros à esquerda do resultado — remover dígitos pode expor zeros que agora ficam na frente (ex.: `"10200"` com `k=1` remove o `1`, expondo `"0200"`, que precisa virar `"200"`).
- Retornar string vazia em vez de `"0"` quando todos os dígitos são removidos — o enunciado exige que o resultado seja um inteiro válido, e "nada" se representa como `"0"`.
- Usar `>=` em vez de `>` na comparação do while — dígitos **iguais** ao topo não devem disparar remoção (remover um `2` para dar lugar a outro `2` não melhora nada e desperdiça uma remoção disponível).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Remove tudo | `"10", k=2` | `"0"` | caso extremo de string vazia, precisa virar "0" |
| Zeros expostos após remoção | `"10200", k=1` | `"200"` | testa a remoção de zeros à esquerda depois da remoção principal |
| String já crescente, remoções sobram para o final | `"12345", k=2` | `"123"` | nenhuma remoção ocorre no meio, sobra remover do fim |
| k igual ao tamanho da string | `"9", k=1` | `"0"` | remove o único dígito, resultado vazio vira "0" |

## 🔗 Conexões

- Problemas irmãos: [0316] Remove Duplicate Letters (mesma técnica de monotonic stack greedy, mas removendo duplicatas em vez de exatamente k elementos), [1475] Final Prices With a Special Discount in a Shop (outra aplicação de monotonic stack sobre um array numérico)
- No backend: essa técnica de "remover exatamente k elementos para minimizar/maximizar um resultado, preservando ordem relativa" aparece em otimização de sequências de operações (ex.: escolher quais k transações cancelar para minimizar impacto) e em problemas de seleção de subsequência ótima sob restrição de contagem fixa de remoções.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
