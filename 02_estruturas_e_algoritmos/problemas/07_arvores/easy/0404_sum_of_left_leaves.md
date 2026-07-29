# [0404] Sum of Left Leaves

> 🔗 [LeetCode 404](https://leetcode.com/problems/sum-of-left-leaves/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne a **soma de todas as folhas esquerdas**. Uma folha é um nó sem filhos; uma folha esquerda é uma folha que é filho **esquerdo** de outro nó.

**Exemplos:**
```
Input:  root = [3,9,20,null,null,15,7]
Output: 24
Explicação: as folhas esquerdas são 9 e 15 (24 = 9 + 15)

Input:  root = [1]
Output: 0
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 1000]` → entrada pequena, O(n) resolve com folga
- `-1000 <= Node.val <= 1000` → valores cabem em `int`, mas a soma pode ser negativa (não assumir que o resultado é sempre ≥ 0)
- O exemplo 2 (`[1]`, output `0`) é a pegadinha: a raiz sozinha **é** folha, mas não é filho esquerdo de ninguém (não tem pai), então não conta

## 🧭 Como reconhecer o padrão

"Folha esquerda" exige saber **duas** coisas sobre um nó ao mesmo tempo: (1) ele é folha (sem filhos) e (2) ele chegou até aqui como filho esquerdo do nó anterior. Isso é diferente da maioria dos problemas de árvore, que só perguntam sobre a subárvore de um nó — aqui é preciso também saber "de onde eu vim", ou seja, informação vinda do **pai**, não só dos filhos.

## 🐢 Solução 1 — Força bruta (mapa de pais em duas passadas)

Primeira passada: percorrer a árvore inteira construindo um `Map<TreeNode, TreeNode>` (filho → pai). Segunda passada: percorrer de novo, e para cada folha, consultar o mapa para descobrir se o pai dela a tem como `left`.

- Tempo: O(n) · Espaço: O(n) para o mapa de pais
- **Por que não basta:** não está errado, mas gasta uma estrutura auxiliar inteira (o mapa) e duas passadas pela árvore para responder uma pergunta que já está disponível "de graça" durante uma única descida: quando você está no nó pai decidindo se desce para `left` ou para `right`, você já sabe, naquele exato momento, qual dos dois é qual — não precisa perguntar depois.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de perguntar "de onde eu vim?" depois, **carregue essa informação durante a descida**: ao chamar a recursão para `no.left`, passe um parâmetro `ehEsquerda = true`; ao chamar para `no.right`, passe `ehEsquerda = false`. Quando a recursão encontrar uma folha, ela já sabe (porque recebeu como parâmetro) se deve somar aquele valor ou não — sem precisar consultar nada extra.

## 🎬 Exemplo passo a passo

`root = [3,9,20,null,null,15,7]`

```
      3
     / \
    9  20
      /  \
    15    7
```

| Chamada | ehEsquerda | É folha? | Soma parcial acumulada |
|---|---|---|---|
| dfs(9, ehEsquerda=true) | true | sim | +9 → soma = 9 |
| dfs(20, ehEsquerda=false) | false | não | desce para 15 e 7 |
| dfs(15, ehEsquerda=true) | true | sim | +15 → soma = 24 |
| dfs(7, ehEsquerda=false) | false | sim, mas não é esquerda | não soma |

Resultado final: `24` ✔ (9 + 15, bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez
- **Espaço:** O(h) — só a pilha de recursão, nenhuma estrutura auxiliar como mapa de pais

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int sumOfLeftLeaves(TreeNode root) {
    return dfs(root, false); // a raiz nunca é "filho esquerdo de alguém", então começa com false
}

private int dfs(TreeNode no, boolean ehEsquerda) {
    if (no == null) return 0;

    // folha + chegou aqui vindo de um ponteiro "left": é exatamente o que procuramos
    if (no.left == null && no.right == null) {
        return ehEsquerda ? no.val : 0;
    }

    // a informação "sou filho esquerdo?" é passada NA CHAMADA, não descoberta depois
    return dfs(no.left, true) + dfs(no.right, false);
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

- Somar qualquer nó cujo `left != null` seja folha, sem checar se o próprio nó atual **é** folha — o erro clássico é confundir "eu tenho um filho esquerdo que é folha" (correto, é isso que queremos) com "eu sou o filho esquerdo e sou folha" (também precisa das duas condições, mas testado no nível certo da recursão).
- Contar a raiz como folha esquerda quando ela é o único nó (`root = [1]`) — a raiz nunca é filho esquerdo de ninguém, por isso o parâmetro inicial precisa ser `false`, não `true`.
- Usar um nó com **um filho apenas** (não é folha) como se fosse folha — `no.left == null && no.right == null` precisa checar **ambos**, um nó com só o direito presente não conta.
- Construir o mapa de pais (a força bruta) quando a informação já está disponível de graça durante a própria descida — funciona, mas é trabalho e memória desnecessários.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1]` | `0` | a raiz é folha, mas não é filho esquerdo de ninguém — cobre o exemplo 2 |
| Só folha à direita | `root = [1,null,2]` | `0` | a única folha existe, mas é filha direita, não conta |
| Só folha à esquerda | `root = [1,2]` | `2` | caso mínimo positivo, uma única folha esquerda |
| Múltiplas folhas esquerdas em níveis diferentes | `root = [3,9,20,null,null,15,7]` | `24` | cobre o exemplo 1 do enunciado, valida a soma através de múltiplos ramos |

## 🔗 Conexões

- Problemas irmãos: [0257] Binary Tree Paths (também carrega estado durante a descida, mas o caminho inteiro em vez de um booleano), [0111] Minimum Depth of Binary Tree (mesma exigência de "só conta se for folha real")
- No backend: carregar contexto do pai durante uma travessia (em vez de reconsultar depois) é o mesmo princípio de passar parâmetros de contexto/autorização "descendo" numa árvore de permissões hierárquicas, evitando releituras redundantes do nó ancestral em cada verificação.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
