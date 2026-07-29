# [0671] Second Minimum Node In a Binary Tree

> 🔗 [LeetCode 671](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dada uma árvore binária especial onde todo nó tem **dois ou zero** filhos, e onde `root.val = min(root.left.val, root.right.val)` vale sempre que existem filhos, retorne o **segundo menor valor** distinto na árvore. Se não existir, retorne `-1`.

**Exemplos:**
```
Input:  root = [2,2,5,null,null,5,7]
Output: 5

Input:  root = [2,2,2]
Output: -1
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 25]` → entrada minúscula; a otimização aqui não é sobre reduzir complexidade assintótica, e sim sobre entender e usar a propriedade estrutural da árvore
- `1 <= Node.val <= 2^31 - 1` → valores sempre positivos, então `-1` é um sentinela seguro para "não existe"
- `root.val = min(root.left.val, root.right.val)` **sempre** que há filhos → é a pista central: **o valor da raiz de qualquer subárvore é sempre o menor valor daquela subárvore inteira** — isso permite podar buscas

## 🧭 Como reconhecer o padrão

A propriedade "`root.val` é sempre o mínimo da subárvore" é parecida com uma BST, mas mais restritiva: aqui **ambos** os filhos são ≥ ao pai (não só um lado). Isso significa que qualquer nó com valor **maior** que o "segundo menor" candidato atual não pode conter, na sua subárvore, um valor **entre** o mínimo global e esse candidato — pode-se **parar de descer** ali, cortando ramos inteiros da busca.

## 🐢 Solução 1 — Força bruta (coletar tudo e ordenar)

Percorrer a árvore inteira com DFS ou BFS, guardando cada valor distinto num `HashSet` (para eliminar duplicatas automaticamente). No final, se o set tiver menos de 2 elementos, retornar `-1`; senão, ordenar os valores e retornar o segundo menor.

- Tempo: O(n log n) por causa do sort · Espaço: O(n) para o set
- **Por que não basta:** ignora completamente a propriedade estrutural do problema. Sempre visita **todos** os n nós e ainda paga um sort no final, quando a estrutura garante que dá para podar subárvores inteiras sem nunca descer nelas — a única razão de visitar um nó é para eventualmente atualizar o candidato a segundo menor, e muitos nós nem precisam ser visitados.

## 💡 Solução 2 — A ideia otimizada (intuição)

O valor da raiz já é o mínimo global (dado pelo enunciado). Faça DFS mantendo um `segundoMinimo` (inicialmente "infinito"/inexistente). Em cada nó: se `no.val > root.val` (ele é candidato a segundo menor, diferente do mínimo), atualize `segundoMinimo` se for menor que o atual — **e não precisa descer mais fundo** nessa subárvore, porque, pela propriedade do problema, nada ali embaixo pode ser menor que `no.val`. Se `no.val == root.val`, continue descendo (pode haver um valor menor que o candidato atual escondido mais fundo).

## 🎬 Exemplo passo a passo

`root = [2,2,5,null,null,5,7]` (raiz 2, filho esquerdo 2 — folha —, filho direito 5, com filhos 5 e 7)

```
      2
     / \
    2   5
       / \
      5   7
```

Mínimo global = `root.val` = 2

| Passo | Nó | no.val > 2? | Ação | segundoMinimo após |
|---|---|---|---|---|
| 1 | 2 (filho esquerdo) | não (igual) | é folha, nada a fazer | ∞ (ainda não achou) |
| 2 | 5 (filho direito) | sim | candidato: 5 < ∞ → atualiza; **poda**, não desce mais aqui | 5 |

Como o nó `5` (filho direito da raiz) já tem valor maior que o mínimo, a poda evita descer até os netos `5` e `7` — eles não poderiam trazer nada menor que `5` de qualquer forma.

Resultado final: `5` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no pior caso (árvore onde todo nó vale o mesmo, forçando descer até o fim), mas frequentemente muito menor graças à poda
- **Espaço:** O(h) de pilha de recursão — nenhuma estrutura auxiliar como set ou lista

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findSecondMinimumValue(TreeNode root) {
    return dfs(root, root.val);
}

private int dfs(TreeNode no, int minimoGlobal) {
    if (no == null) return -1;

    // valor maior que o mínimo global: é candidato a segundo menor, e a subárvore
    // inteira daqui pra baixo só tem valores >= no.val (propriedade do problema) — pode podar
    if (no.val > minimoGlobal) return no.val;

    // valor igual ao mínimo: ainda pode haver algo menor escondido mais fundo, continua descendo
    int esquerda = dfs(no.left, minimoGlobal);
    int direita = dfs(no.right, minimoGlobal);

    if (esquerda == -1) return direita; // só a direita achou candidato (ou nenhuma achou)
    if (direita == -1) return esquerda; // só a esquerda achou candidato

    return Math.min(esquerda, direita); // ambas acharam: o segundo menor é o menor dos dois candidatos
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

- Continuar descendo numa subárvore mesmo depois de `no.val > minimoGlobal` — desperdiça trabalho: a propriedade do problema garante que nada mais fundo será menor que `no.val`, então a poda é sempre segura, não é uma otimização arriscada.
- Esquecer que `no.val == minimoGlobal` **não** significa "ignorar este nó" — é exatamente o oposto: só faz sentido continuar buscando quando o valor é igual ao mínimo, porque um valor **maior** já travou o candidato ali.
- Retornar `0` como sentinela de "não achei" em vez de `-1` — como `Node.val >= 1` sempre, `0` seria um sentinela seguro tecnicamente, mas o enunciado já define `-1` como a resposta esperada para "não existe segundo mínimo".
- Usar `HashSet` (a força bruta) numa árvore de até 25 nós achando que a otimização "não importa" pelo tamanho pequeno — o valor didático do problema está exatamente em reconhecer e aplicar a propriedade estrutural, não no ganho de performance em si.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [1]` | `-1` | sem filhos, não existe segundo valor |
| Todos os valores iguais | `root = [2,2,2]` | `-1` | cobre o exemplo 2 do enunciado, testa "nunca encontrar candidato" |
| Segundo mínimo raso | `root = [2,2,5,null,null,5,7]` | `5` | cobre o exemplo 1, valida a poda logo no primeiro nível maior que o mínimo |
| Segundo mínimo só aparece fundo | `root = [1,1,1,1,1,1,2]` (hipotético, 2 escondido no último nível) | `2` | garante que a busca continua descendo enquanto os valores forem iguais ao mínimo |

## 🔗 Conexões

- Problemas irmãos: [0530] Minimum Absolute Difference in BST (também aproveita uma propriedade estrutural específica para evitar comparar todos os pares), [0965] Univalued Binary Tree (mesma ideia de comparar cada nó com o valor da raiz, aqui usada de forma mais simples)
- No backend: podar buscas em subárvores que já não podem melhorar o resultado atual (branch and bound) é o mesmo princípio usado em otimização de consultas hierárquicas (parar de explorar um ramo de índice quando ele já não pode conter um resultado melhor que o candidato atual) e em algoritmos de busca em árvores de decisão com limites conhecidos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
