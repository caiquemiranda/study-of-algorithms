# [0617] Merge Two Binary Trees

> 🔗 [LeetCode 617](https://leetcode.com/problems/merge-two-binary-trees/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dadas as raízes de duas árvores binárias `root1` e `root2`, mescle-as numa árvore nova: onde os dois nós se sobrepõem, some os valores; onde só um dos dois existe, use o nó que **não** é nulo.

**Exemplos:**
```
Input:  root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input:  root1 = [1], root2 = [1,2]
Output: [2,2]
```

**Restrições (e o que elas denunciam):**
- Número de nós em ambas as árvores em `[0, 2000]` → precisa de solução O(n), onde n é o total combinado das duas árvores
- `-10^4 <= Node.val <= 10^4` → valores cabem em `int` (a soma de dois valores nesse range ainda cabe sem overflow)
- "a mesclagem deve começar pelas raízes de ambas" → a comparação é sempre posição a posição, igual a [0100] Same Tree, não uma busca livre por valores parecidos

## 🧭 Como reconhecer o padrão

"Mesclar duas árvores, posição a posição" é DFS simultâneo nas duas árvores ao mesmo tempo — o mesmo esqueleto de recursão de [0100] Same Tree e [0101] Symmetric Tree, só que em vez de **comparar** os dois nós, você **combina** eles (soma valores, escolhe o não-nulo).

## 🐢 Solução 1 — Força bruta (clonar uma árvore, depois mesclar a outra)

Primeiro clonar `root1` inteira, alocando um nó novo para cada nó existente (uma travessia completa só para copiar). Depois, numa segunda passada, percorrer `root2` mesclando seus valores dentro da cópia recém-criada — inclusive alocando nós novos na cópia sempre que `root2` tiver um nó numa posição onde a cópia (originada de `root1`) não tinha nada.

- Tempo: O(n1 + n2) · Espaço: O(n1 + n2) para a árvore clonada, mesmo nas partes que não se sobrepõem
- **Por que não basta:** funciona, mas clona nós que, no fim das contas, muitas vezes vão simplesmente ser **reaproveitados por referência** sem nenhuma modificação (as partes de `root1` ou `root2` que não se sobrepõem). Fazer uma passada completa de clonagem antes de sequer olhar a segunda árvore é trabalho redundante quando dá para decidir "clonar ou reaproveitar" nó a nó, numa única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única recursão simultânea nas duas árvores: se **ambos** `t1` e `t2` existem no nó atual, some os valores (mutando `t1` em vez de alocar um nó novo) e continue recursivamente para os filhos de ambos. Se só um dos dois existe, **retorne aquele nó diretamente por referência** — a subárvore inteira dele já está pronta, não precisa ser reconstruída nó a nó.

## 🎬 Exemplo passo a passo

`root1 = [1], root2 = [1,2]` (root2 tem um filho esquerdo `2`)

```
t1:   1        t2:   1
                     /
                    2
```

| Passo | Chamada | t1 existe? | t2 existe? | Ação |
|---|---|---|---|---|
| 1 | merge(1, 1) | sim | sim | soma: `t1.val = 1+1 = 2`; recursa para os filhos |
| 2 | merge(null, 2) [filho esquerdo] | não | sim | retorna `t2` (o nó `2`) diretamente, por referência |
| 3 | merge(null, null) [filho direito] | não | não | retorna `null` |

Resultado: raiz com valor `2`, filho esquerdo é o nó `2` original de `root2` (reaproveitado), sem filho direito.

Resultado final: `[2,2]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(min(n1, n2)) — a recursão só continua descendo enquanto **ambas** as árvores tiverem nós na mesma posição; assim que uma delas acaba, a subárvore restante da outra é anexada por referência sem visitar seus nós individualmente
- **Espaço:** O(min(h1, h2)) de pilha de recursão — nenhuma estrutura extra é alocada além da mutação de `t1`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
    if (t1 == null) return t2; // reaproveita t2 (ou null) diretamente, sem clonar
    if (t2 == null) return t1; // idem para t1: a subárvore já está pronta, não precisa recriar

    // ambos existem: muta t1 no lugar, somando os valores (evita alocar um nó novo)
    t1.val += t2.val;
    t1.left = mergeTrees(t1.left, t2.left);
    t1.right = mergeTrees(t1.right, t2.right);

    return t1;
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

- Alocar um nó novo mesmo quando só uma das duas árvores tem algo naquela posição — desperdiça memória e trabalho; basta devolver a subárvore existente por referência.
- Mutar `root1` quando o enunciado (ou os testes) espera que as árvores originais permaneçam intactas — a solução de referência aqui **muta `t1`**, o que é aceito pelo LeetCode (a resposta é o retorno, não a preservação de `root1`), mas é importante estar ciente dessa mutação em código de produção, onde efeitos colaterais em estruturas de entrada costumam ser indesejados.
- Esquecer que a ordem dos parâmetros importa para a leitura, mas não para o resultado — a soma é comutativa (`t1.val + t2.val`), então trocar a ordem dos argumentos não muda a resposta, só a legibilidade.
- Tratar `t1 == null && t2 == null` como um caso especial separado — não é necessário: o primeiro `if (t1 == null) return t2` já cobre esse caso corretamente, retornando `null`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ambas vazias | `root1 = [], root2 = []` | `[]` (`null`) | caso base, primeiro `if` já resolve |
| Uma vazia, outra não | `root1 = [], root2 = [1,2]` | `[1,2]` | testa o reaproveitamento por referência de uma árvore inteira |
| Sobreposição total | `root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]` | `[3,4,5,5,4,null,7]` | cobre o exemplo 1 do enunciado, mistura sobreposição parcial e total |
| Valores negativos | `root1 = [-1], root2 = [1]` | `[0]` | garante que a soma funciona corretamente com valores negativos que se cancelam |

## 🔗 Conexões

- Problemas irmãos: [0100] Same Tree (o mesmo esqueleto de recursão simultânea em duas árvores, mas comparando em vez de combinar), [0226] Invert Binary Tree (mesma ideia de mutar a árvore existente em vez de reconstruir do zero)
- No backend: mesclar duas estruturas hierárquicas nó a nó, reaproveitando por referência as partes que não colidem, é o mesmo padrão usado em merge de configurações em cascata (ex.: config padrão + overrides específicos de ambiente formando uma árvore de configuração final) e em resolução de conflitos em merges de documentos JSON aninhados.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
