# [1598] Crawler Log Folder

> 🔗 [LeetCode 1598](https://leetcode.com/problems/crawler-log-folder/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Array` `#String`

## 📜 O Problema

O sistema de arquivos do LeetCode mantém um log toda vez que um usuário executa uma operação de **trocar de pasta**. As operações são:

- `"../"`: move para a pasta **pai** da pasta atual (se já estiver na pasta principal, **permanece** na mesma pasta).
- `"./"`: permanece na mesma pasta.
- `"x/"`: move para a pasta filha `x` (garantida existir).

Você recebe uma lista `logs` com as operações realizadas em ordem. O sistema começa na pasta principal. Retorne o **número mínimo de operações** necessárias para voltar à pasta principal depois de executar todas as operações do log.

**Exemplos:**
```
Input:  logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explicação: use "../" 2 vezes para voltar à pasta principal.

Input:  logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Input:  logs = ["d1/","../","../","../"]
Output: 0
Explicação: já estava (ou voltou) para a pasta principal antes do fim do log.
```

**Restrições (e o que elas denunciam):**
- `1 <= logs.length <= 10^3` → qualquer solução O(n) é rápida o bastante
- `2 <= logs[i].length <= 10` → cada operação é curta, não precisa de parsing complexo
- `logs[i]` segue exatamente um dos 3 formatos descritos → não há operações inválidas a tratar

## 🧭 Como reconhecer o padrão

"Rastrear a profundidade atual numa estrutura de pastas navegável, onde '..' volta um nível" é a mesma ideia de rastrear aninhamento que sustenta uma pilha: cada `"x/"` empilharia uma pasta, e cada `"../"` desempilharia. Como a pergunta final é só "quantos passos para voltar à raiz" (ou seja, a **profundidade** final), você nem precisa guardar os nomes das pastas — só a contagem de níveis, que é exatamente o **tamanho** que a pilha teria.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular o sistema de arquivos de verdade com uma pilha de nomes de pastas: `"x/"` empilha `x`, `"../"` desempilha (se não vazia), `"./"` não faz nada. No final, o número de operações para voltar à raiz é o tamanho da pilha.

- Tempo: O(n) · Espaço: O(n) — guarda todos os nomes de pastas empilhados
- **Por que não basta:** essa solução já é O(n) e correta, mas gasta espaço guardando os **nomes** das pastas (`String`), quando a pergunta só precisa da **contagem** de níveis. A solução ótima simplifica trocando a pilha de strings por um contador inteiro, sem perda de correção.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um contador `profundidade` começando em 0 (a pasta principal). Para cada operação: `"x/"` incrementa `profundidade`; `"../"` decrementa `profundidade`, mas nunca abaixo de 0 (já estar na raiz e tentar subir mantém na raiz); `"./"` não altera nada. No final, `profundidade` já é a resposta: o número mínimo de `"../"` necessários para voltar à raiz é exatamente quantos níveis abaixo da raiz você está.

## 🎬 Exemplo passo a passo

`logs = ["d1/","d2/","./","d3/","../","d31/"]`

| Passo | Operação | Ação | profundidade após |
|---|---|---|---|
| 1 | `"d1/"` | entra na pasta filha → incrementa | 1 |
| 2 | `"d2/"` | entra na pasta filha → incrementa | 2 |
| 3 | `"./"` | permanece → nada muda | 2 |
| 4 | `"d3/"` | entra na pasta filha → incrementa | 3 |
| 5 | `"../"` | sobe um nível → decrementa | 2 |
| 6 | `"d31/"` | entra na pasta filha → incrementa | 3 |

Resultado final: `3` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelo log, decisão O(1) por operação
- **Espaço:** O(1) — só um contador inteiro, sem guardar nomes de pastas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minOperations(String[] logs) {
    int profundidade = 0;

    for (String log : logs) {
        if (log.equals("../")) {
            profundidade = Math.max(0, profundidade - 1); // já na raiz: "subir" não faz nada
        } else if (!log.equals("./")) {
            profundidade++;                                 // qualquer outra coisa é "entrar em x/"
        }
        // "./" cai aqui e não altera profundidade
    }

    return profundidade; // distância até a raiz == nº mínimo de "../" para voltar
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

- Deixar `profundidade` ficar negativa ao processar `"../"` na raiz — o enunciado é explícito que tentar subir da pasta principal **não faz nada**; sem o `Math.max(0, ...)`, uma sequência como `["../","../","d1/"]` calcularia profundidade errada.
- Confundir a ordem das checagens no `if`/`else` — checar `"../"` primeiro e usar `else if` para as demais evita comparar a mesma string duas vezes e deixa claro que `"x/"` é o caso "sobra" (qualquer coisa que não seja os dois operadores especiais).
- Achar que precisa rastrear os **nomes** das pastas para responder a pergunta — como a pergunta só quer "quantas operações para voltar à raiz", a profundidade numérica já é suficiente; guardar nomes é trabalho desnecessário aqui (mas seria necessário se o problema pedisse o **caminho** final, não só a contagem).
- Tratar `"./"` como se fosse "subir um nível" por engano — `"./"` significa "permanecer", não deve alterar o contador.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Tentar subir da raiz repetidamente | `["../","../"]` | 0 | já está na raiz, `"../"` não pode deixar a profundidade negativa |
| Só operações "./" | `["./","./"]` | 0 | nunca sai da raiz |
| Volta exata à raiz no meio do log | `["d1/","../","../","../"]` | 0 | mesmo com "../" sobrando (tentando subir além da raiz), o resultado final é 0 |
| Descida profunda sem subir | `["d1/","d2/","d3/"]` | 3 | cada entrada incrementa, sem nenhuma saída |

## 🔗 Conexões

- Problemas irmãos: [0071] Simplify Path (mesmo domínio de navegação de sistema de arquivos, mas usando pilha de nomes reais porque a resposta é o caminho final, não só a profundidade), [1614] Maximum Nesting Depth of the Parentheses (mesma ideia de contador de profundidade sem pilha explícita)
- No backend: rastrear profundidade/nível sem guardar o conteúdo aparece em navegação de árvores de diretórios (breadcrumbs de UI), em contadores de indentação de parsers, e em qualquer sistema que precise saber "quantos níveis preciso subir para voltar à raiz" sem precisar materializar o caminho inteiro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
