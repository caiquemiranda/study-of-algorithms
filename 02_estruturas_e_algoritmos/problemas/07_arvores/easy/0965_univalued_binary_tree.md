# [0965] Univalued Binary Tree

> 🔗 [LeetCode 965](https://leetcode.com/problems/univalued-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne `true` se **todo** nó da árvore tiver o mesmo valor.

**Exemplos:**
```
Input:  root = [1,1,1,1,1,null,1]
Output: true

Input:  root = [2,2,2,5,2]
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 100]` → entrada pequena, qualquer O(n) resolve
- `0 <= Node.val < 100` → valores não-negativos, cabem em `int`
- Não há follow-up nem pegadinha estrutural — o desafio real aqui é implementar o **short-circuit** corretamente, não a complexidade em si

## 🧭 Como reconhecer o padrão

"Todo nó tem o mesmo valor?" é uma checagem simples de DFS: cada nó só precisa ser comparado com o valor da **raiz** (fixo, conhecido desde o início), não com o pai imediato — porque a pergunta é sobre um único valor válido para a árvore inteira, não sobre relações locais entre vizinhos.

## 🐢 Solução 1 — Força bruta (coletar todos os valores num set)

Percorrer a árvore inteira com DFS ou BFS, adicionando cada `no.val` a um `HashSet<Integer>`, sempre até o fim. No final, checar se o set tem exatamente 1 elemento.

- Tempo: O(n) · Espaço: O(k), onde k é o número de valores distintos (até O(n) no pior caso)
- **Por que não basta:** continua visitando a árvore inteira mesmo depois de já ter encontrado dois valores diferentes (o que já basta para responder `false`) — não há necessidade de terminar a travessia nem de guardar nada num set quando a resposta já está decidida.

## 💡 Solução 2 — A ideia otimizada (intuição)

DFS que compara `no.val` diretamente com `root.val` (guardado uma vez, no início). Assim que encontrar **qualquer** nó com valor diferente, retorne `false` imediatamente (short-circuit), sem continuar descendo no resto da árvore. Só chega ao fim da travessia sem interrupção se todos os valores realmente baterem.

## 🎬 Exemplo passo a passo

`root = [2,2,2,5,2]` (raiz 2, filhos 2 e 2; o filho esquerdo do primeiro `2` é `5`)

```
      2
     / \
    2   2
   /
  5
```

| Passo | Nó visitado | no.val == root.val (2)? | Ação |
|---|---|---|---|
| 1 | 2 (filho esquerdo da raiz) | sim | continua descendo |
| 2 | 5 (neto) | **não** | retorna `false` imediatamente — nem chega a visitar o outro filho da raiz |

Resultado final: `false` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no pior caso (árvore realmente uni-valorada, precisa confirmar todos os nós), mas termina muito antes quando encontra uma diferença cedo
- **Espaço:** O(h) de pilha de recursão — nenhuma estrutura auxiliar como set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isUnivalTree(TreeNode root) {
    return dfs(root, root.val);
}

private boolean dfs(TreeNode no, int valorEsperado) {
    if (no == null) return true; // subárvore vazia não quebra a uniformidade

    if (no.val != valorEsperado) return false; // achou diferença: short-circuit imediato

    // só continua se AMBOS os lados também baterem (curto-circuito do && já evita trabalho extra)
    return dfs(no.left, valorEsperado) && dfs(no.right, valorEsperado);
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

- Comparar cada nó só com o **pai** em vez de com a raiz — tecnicamente funciona aqui (se todo par pai-filho é igual, transitivamente todos são iguais), mas é um raciocínio mais frágil de generalizar; comparar direto com `root.val` é mais direto e menos sujeito a erro conceitual.
- Continuar percorrendo a árvore inteira depois de já ter achado uma diferença (a força bruta com set) — desperdiça tempo e memória numa resposta que já estava decidida.
- Esquecer o caso base `no == null` retornando `true` — sem ele, folhas (que têm filhos nulos) quebram a recursão com `NullPointerException` ao tentar comparar `null.val`.
- Usar `||` em vez de `&&` ao combinar os resultados da esquerda e da direita — a árvore só é uni-valorada se **ambos** os lados forem uniformes, não se **pelo menos um** for.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [5]` | `true` | caso base, nada para comparar além da própria raiz |
| Todos iguais, árvore maior | `root = [1,1,1,1,1,null,1]` | `true` | cobre o exemplo 1 do enunciado, testa short-circuit "nunca dispara" |
| Diferença rasa | `root = [1,2]` | `false` | diferença no primeiro nível já resolve |
| Diferença funda | `root = [2,2,2,5,2]` | `false` | cobre o exemplo 2, valida que a busca desce até achar a diferença, mas para assim que acha |

## 🔗 Conexões

- Problemas irmãos: [0100] Same Tree (mesma ideia de comparação recursiva com short-circuit, mas entre duas árvores em vez de contra um valor fixo), [0671] Second Minimum Node In a Binary Tree (também compara cada nó contra o valor da raiz para decidir a ação)
- No backend: verificar se todos os registros de uma hierarquia compartilham o mesmo valor (ex.: todos os nós de uma árvore de permissões pertencem ao mesmo tenant/organização) usa exatamente esse padrão de comparação contra um valor de referência fixo, com saída antecipada assim que uma violação é encontrada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
