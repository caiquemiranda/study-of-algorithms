# [0071] Simplify Path

> 🔗 [LeetCode 71](https://leetcode.com/problems/simplify-path/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Medium`

## 📜 O Problema

Você recebe um caminho **absoluto** de um sistema de arquivos estilo Unix, que sempre começa com uma barra `'/'`. Transforme esse caminho no seu **caminho canônico simplificado**.

Regras do sistema de arquivos:
- `'.'` representa o diretório atual.
- `'..'` representa o diretório pai/anterior.
- Múltiplas barras consecutivas (`'//'`, `'///'`) são tratadas como uma única barra.
- Qualquer sequência de pontos que **não** casa com as regras acima é um nome válido de diretório/arquivo (ex.: `'...'` e `'....'` são nomes válidos).

O caminho simplificado deve: começar com uma única barra; ter diretórios separados por exatamente uma barra; não terminar com barra (exceto se for a raiz); não conter `'.'`/`'..'` como componentes.

**Exemplos:**
```
Input:  path = "/home/"
Output: "/home"
Explicação: a barra final é removida.

Input:  path = "/home//foo/"
Output: "/home/foo"
Explicação: barras consecutivas viram uma só.

Input:  path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explicação: ".." sobe um nível (volta para o diretório pai).

Input:  path = "/../"
Output: "/"
Explicação: subir a partir da raiz não é possível.

Input:  path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explicação: "..." é um nome de diretório válido neste problema.
```

**Restrições (e o que elas denunciam):**
- `1 <= path.length <= 3000` → precisa de solução O(n); reconstruções ingênuas repetidas seriam arriscadas
- `path` consiste de letras, dígitos, `'.'`, `'/'` ou `'_'` → conjunto de caracteres restrito, sem necessidade de tratar símbolos especiais adicionais
- `path` é um caminho absoluto Unix válido → sempre começa com `'/'`, não é preciso validar formato

## 🧭 Como reconhecer o padrão

"Navegar por componentes de caminho onde `'..'` volta um nível" é a mesma ideia de [1598] Crawler Log Folder, mas aqui a resposta precisa do **caminho final completo**, não só a contagem de níveis — por isso, em vez de um contador, você precisa de uma **pilha de nomes de diretórios**: cada componente válido empilha, cada `'..'` desempilha (voltando ao pai), e `'.'`/componentes vazios são ignorados.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar expressões regulares ou parsing manual caractere a caractere para processar barras, pontos e nomes simultaneamente, construindo o resultado incrementalmente com lógica condicional complexa embutida no laço principal.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** tecnicamente já seria O(n), mas misturar toda a lógica de parsing (detectar barras duplicadas, identificar `'.'` vs `'..'` vs nome válido) num único laço caractere a caractere é propenso a bugs sutis de índice. Dividir o problema em "quebrar por `/`" + "processar cada componente com uma pilha" é mais simples e menos sujeito a erro — é essa divisão que caracteriza a solução ótima.

## 💡 Solução 2 — A ideia otimizada (intuição)

Divida `path` pelo caractere `/` (isso já resolve barras consecutivas, já que dividir por `/` produz strings vazias entre barras duplicadas, que são fáceis de ignorar). Para cada componente resultante: se for vazio ou `"."`, ignore (não afeta o caminho). Se for `".."`, desempilhe o último diretório da pilha, se houver algum (subir do topo é um no-op se a pilha já estiver vazia — equivalente a já estar na raiz). Caso contrário (nome de diretório/arquivo válido, incluindo sequências como `"..."`), empilhe-o. No final, junte os componentes da pilha com `/` entre eles, prefixados por uma barra inicial.

## 🎬 Exemplo passo a passo

`path = "/.../a/../b/c/../d/./"`, componentes após dividir por `/`: `["", "...", "a", "..", "b", "c", "..", "d", ".", ""]`

| Passo | Componente | Ação | Pilha após |
|---|---|---|---|
| 1 | `""` | vazio → ignora | `[]` |
| 2 | `"..."` | nome válido (não é "." nem "..") → empilha | `[...]` |
| 3 | `"a"` | nome válido → empilha | `[..., a]` |
| 4 | `".."` | sobe → desempilha topo (`a`) | `[...]` |
| 5 | `"b"` | nome válido → empilha | `[..., b]` |
| 6 | `"c"` | nome válido → empilha | `[..., b, c]` |
| 7 | `".."` | sobe → desempilha topo (`c`) | `[..., b]` |
| 8 | `"d"` | nome válido → empilha | `[..., b, d]` |
| 9 | `"."` | diretório atual → ignora | `[..., b, d]` |
| 10 | `""` | vazio → ignora | `[..., b, d]` |

Junta a pilha com `/`: `"/.../b/d"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — dividir a string é O(n), e cada componente é processado em O(1) amortizado
- **Espaço:** O(n) — a pilha guarda no máximo todos os componentes do caminho

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String simplifyPath(String path) {
    Deque<String> pilha = new ArrayDeque<>();

    // split por "/" já resolve barras consecutivas: elas geram strings vazias, ignoradas abaixo
    for (String componente : path.split("/")) {
        if (componente.isEmpty() || componente.equals(".")) {
            continue;                              // não afeta o caminho
        } else if (componente.equals("..")) {
            if (!pilha.isEmpty()) {
                pilha.removeLast();                 // sobe um nível (no-op se já na raiz)
            }
        } else {
            pilha.addLast(componente);              // nome de diretório/arquivo válido
        }
    }

    return "/" + String.join("/", pilha); // pilha vazia gera exatamente "/" (a raiz)
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

- Desempilhar em `".."` sem checar se a pilha está vazia — tentar subir a partir da raiz (`"/../"`) deve ser um no-op, não um erro; `pilha.isEmpty()` precisa ser checado antes de remover.
- Esquecer que `split("/")` numa string começando com `/` gera uma string vazia como primeiro elemento, e que barras duplicadas também geram vazios no meio — ambos os casos precisam ser ignorados da mesma forma, sem lógica especial separada.
- Tratar `"..."` (três pontos) ou `"...."` como se fossem `".."` — a regra é uma comparação **exata** de string: só `"."` exatamente e `".."` exatamente têm significado especial; qualquer outra sequência de pontos é um nome de diretório válido.
- Adicionar uma barra extra ao juntar a pilha — usar `"/" + String.join("/", pilha)` gera o formato correto (raiz sozinha quando a pilha está vazia, ou `/comp1/comp2/...` quando não está), sem barra dupla ou barra final indevida.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Subir além da raiz | `"/../"` | `"/"` | tentar subir da raiz não pode gerar erro nem caminho negativo |
| Barras consecutivas | `"/home//foo/"` | `"/home/foo"` | split por "/" já absorve isso, sem lógica extra |
| Nome de diretório parecido com ".." | `"/.../a/../b/c/../d/./"` | `"/.../b/d"` | "..." não é tratado como operador de navegação |
| Caminho já canônico | `"/a/b/c"` | `"/a/b/c"` | nenhuma simplificação necessária, cada componente só empilha |

## 🔗 Conexões

- Problemas irmãos: [1598] Crawler Log Folder (mesmo domínio de navegação de sistema de arquivos, mas só precisa da profundidade/contagem, não do caminho completo), [0150] Evaluate Reverse Polish Notation (outra pilha processando tokens sequenciais para produzir um resultado final)
- No backend: normalização de caminhos é usada em toda validação de path traversal (segurança — impedir `"../"` maliciosos em uploads/downloads de arquivos), em roteadores de URL que resolvem caminhos relativos, e em sistemas de build que resolvem imports com caminhos relativos (`import "../utils"`).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
