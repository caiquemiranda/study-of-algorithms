# [0098] Validate Binary Search Tree

> 🔗 [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#TravessiaEmOrdem`

## 📜 O Problema

Dado o `root` de uma árvore binária, determine se ela é uma **BST válida**: para todo nó, a subárvore esquerda **inteira** contém só valores estritamente menores, e a subárvore direita **inteira** contém só valores estritamente maiores.

**Exemplos:**
```
Input:  root = [2,1,3]
Output: true

Input:  root = [5,1,4,null,null,3,6]
Output: false
Explicação: o valor da raiz é 5, mas o filho direito dela tem valor 4
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^4]` → precisa de solução O(n)
- `-2^31 <= Node.val <= 2^31 - 1` → valores cobrem o range **inteiro** de `int`, incluindo os extremos — usar `int` como sentinela de limite inicial ("infinito") vai falhar exatamente nesses extremos
- "**estritamente** menor / maior" → BST aqui não aceita valores repetidos em posições ambíguas; `no.val <= limite` ou `no.val >= limite` já invalida

## 🧭 Como reconhecer o padrão

"É uma BST válida?" parece simples ("compara com o pai"), mas a regra vale para a subárvore **inteira**, não só o vizinho imediato — é o erro nº 1 documentado nos fundamentos da categoria. A forma correta é propagar **limites** (mínimo e máximo permitidos) descendo pela árvore: cada nó herda os limites de todos os seus ancestrais, não só do pai direto.

## 🐢 Solução 1 — Força bruta (travessia em-ordem completa, coletando numa lista)

Fazer uma travessia em-ordem coletando todos os valores numa `List<Integer>`. No final, percorrer a lista checando se ela está estritamente crescente (`lista[i] < lista[i+1]` para todo `i`).

- Tempo: O(n) · Espaço: O(n) para a lista completa
- **Por que não basta:** funciona corretamente (é uma solução válida), mas guarda **todos** os n valores numa lista quando só o valor **anterior** visitado precisa ser lembrado a cada passo — o mesmo padrão de desperdício de memória já visto em [0530]/[0783].

## 💡 Solução 2 — A ideia otimizada (intuição)

Duas formas equivalentes, ambas evitando a lista completa:
1. **Limites descendo:** cada chamada recursiva recebe um `(mínimo, máximo)` permitido, herdado dos ancestrais. Ao descer para a esquerda, o `máximo` vira o valor do nó atual; ao descer para a direita, o `mínimo` vira o valor do nó atual.
2. **Em-ordem com valor anterior:** faça a travessia em-ordem comparando cada novo valor só com o **anterior** visitado (sem lista), retornando `false` assim que encontrar um valor não estritamente maior que o anterior.

A referência abaixo usa a técnica de limites, por deixar mais explícito **por que** o erro clássico de comparar só com o pai está errado.

## 🎬 Exemplo passo a passo

`root = [5,1,4,null,null,3,6]` (a raiz é 5, filho esquerdo 1, filho direito 4 com filhos 3 e 6)

```
      5
     / \
    1   4
       / \
      3   6
```

| Passo | Nó | limites herdados (min, max) | Comparação | Ação |
|---|---|---|---|---|
| 1 | 5 (raiz) | (-∞, +∞) | dentro dos limites | desce: esquerda com max=5, direita com min=5 |
| 2 | 1 (esquerda) | (-∞, 5) | 1 < 5, válido | folha, ok |
| 3 | 4 (direita) | (5, +∞) | **4 não é > 5** | **inválido** → retorna `false` imediatamente |

Se a checagem fosse só "comparar com o pai imediato" (o erro clássico), o nó `4` seria comparado só com seu próprio pai (`4` mesmo, na posição), e a violação contra o **avô** (`5`) passaria despercebida — é exatamente esse tipo de caso que os limites descendo capturam corretamente.

Resultado final: `false` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez, com short-circuit assim que uma violação é encontrada
- **Espaço:** O(h) de pilha de recursão — nenhuma lista guardando todos os valores

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isValidBST(TreeNode root) {
    return valida(root, Long.MIN_VALUE, Long.MAX_VALUE); // long: Node.val pode chegar a Integer.MIN/MAX_VALUE
}

private boolean valida(TreeNode no, long minimo, long maximo) {
    if (no == null) return true; // subárvore vazia não viola nada

    // a regra vale para TODOS os ancestrais, não só o pai imediato — por isso os limites
    if (no.val <= minimo || no.val >= maximo) return false;

    return valida(no.left, minimo, no.val)   // à esquerda, o teto agora é o valor deste nó
        && valida(no.right, no.val, maximo); // à direita, o piso agora é o valor deste nó
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

- **O erro nº 1 do problema:** comparar cada nó só com o **pai** imediato (`no.val > pai.val` para a direita, `no.val < pai.val` para a esquerda) — passa em casos simples, mas falha em árvores como `[5,1,4,null,null,3,6]`, onde a violação está contra um **avô**, não o pai direto.
- Usar `int` como sentinela de "infinito" (`Integer.MIN_VALUE`/`MAX_VALUE`) em vez de `long` — se algum nó realmente valer `Integer.MIN_VALUE` ou `Integer.MAX_VALUE` (permitido pela restrição), a comparação `no.val <= minimo` com `minimo = Integer.MIN_VALUE` nunca dispararia corretamente, porque não existe valor menor que `Integer.MIN_VALUE` dentro do próprio tipo `int`.
- Usar `<` e `>` em vez de `<=` e `>=` na checagem de violação — a regra é **estritamente** menor/maior; um nó com valor igual ao limite herdado já invalida a árvore.
- Guardar todos os valores numa lista (a força bruta) para depois checar se está ordenada — funciona, mas gasta memória à toa quando dá para validar durante a própria descida.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| BST válida simples | `root = [2,1,3]` | `true` | caso base positivo |
| Violação contra o avô, não o pai | `root = [5,1,4,null,null,3,6]` | `false` | cobre o exemplo 2 do enunciado, o caso clássico que "comparar só com o pai" erra |
| Valores nos extremos de `int` | `root = [2147483647]` | `true` | valida que o sentinela `long` funciona corretamente no limite superior |
| Valores duplicados (violação de "estritamente") | `root = [2,2,2]` | `false` | testa que igualdade também invalida, não só inversão de ordem |

## 🔗 Conexões

- Problemas irmãos: [0099] Recover Binary Search Tree (usa a mesma travessia em-ordem para **detectar** onde a BST foi corrompida, em vez de só validar), [0530] Minimum Absolute Difference in BST (mesma travessia em-ordem comparando com o valor anterior)
- No backend: validar invariantes que valem para toda uma subestrutura (não só o vizinho imediato) é o mesmo tipo de checagem usada em validação de hierarquias de permissões (um usuário não pode ter um nível de acesso maior que **nenhum** ancestral na cadeia, não só o pai direto) e em verificação de integridade de índices B-Tree após operações de balanceamento.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
