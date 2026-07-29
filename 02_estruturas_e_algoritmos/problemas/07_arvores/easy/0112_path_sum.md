# [0112] Path Sum

> 🔗 [LeetCode 112](https://leetcode.com/problems/path-sum/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Backtracking`

## 📜 O Problema

Dado o `root` de uma árvore binária e um inteiro `targetSum`, retorne `true` se existir um caminho **raiz-até-folha** cuja soma dos valores seja igual a `targetSum`.

**Exemplos:**
```
Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Input:  root = [1,2,3], targetSum = 5
Output: false

Input:  root = [], targetSum = 0
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 5000]` → O(n) resolve com folga
- `-1000 <= Node.val <= 1000` e `-1000 <= targetSum <= 1000` → valores podem ser negativos, então "a soma passou do alvo" **não** significa que o caminho pode ser descartado cedo (diferente de um problema com só valores positivos)
- Árvore vazia sempre retorna `false`, mesmo se `targetSum = 0` → não existe caminho algum numa árvore vazia, então não há "soma vazia que bate com zero" aqui

## 🧭 Como reconhecer o padrão

"Existe um caminho raiz-folha com soma X?" é DFS clássico carregando um estado (soma parcial) enquanto desce, e testando a condição só quando chega numa **folha real** — mistura a ideia de acumular estado durante a descida com a mesma exigência de "folha real" já vista em [0111] Minimum Depth.

## 🐢 Solução 1 — Força bruta (gerar todos os caminhos e depois somar)

DFS que constrói e guarda **todos** os caminhos raiz-folha como listas de valores; depois de coletar tudo, percorrer a lista de caminhos e somar cada um para comparar com `targetSum`.

- Tempo: O(n) · Espaço: O(n²) no pior caso — cada um dos até O(n) caminhos pode ter até O(n) nós, numa árvore degenerada isso vira uma lista de listas quadrática
- **Por que não basta:** guardar todos os caminhos por completo antes de somar desperdiça memória — a soma de cada caminho pode ser calculada **durante** a descida, sem nunca precisar materializar a lista de valores visitados.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de carregar "a soma até aqui", subtraia o valor do nó atual do `targetSum` restante conforme desce (`restante -= node.val`). Ao chegar numa folha, a pergunta vira simplesmente "o que sobrou é zero?". Isso evita guardar qualquer lista — só um número (o alvo restante) viaja pela recursão.

## 🎬 Exemplo passo a passo

`root = [1,2,3]`, `targetSum = 5`

```
    1
   / \
  2   3
```

| Passo | Nó | restante ao entrar | É folha? | Decisão |
|---|---|---|---|---|
| 1 | 1 | 5 - 1 = 4 | não | desce para os dois filhos |
| 2 | 2 (esquerda) | 4 - 2 = 2 | sim, mas restante ≠ 0 | `false` neste ramo |
| 3 | 3 (direita) | 4 - 3 = 1 | sim, mas restante ≠ 0 | `false` neste ramo |
| 4 | volta à raiz | — | — | nenhum ramo bateu → `false` |

Resultado final: `false` ✔ (bate com o enunciado — os únicos caminhos são `1→2` soma 3 e `1→3` soma 4, nenhum é 5)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado no máximo uma vez, e a recursão para cedo (short-circuit com `||`) assim que encontra um caminho válido
- **Espaço:** O(h) — só a pilha de recursão; nenhuma estrutura auxiliar guardando caminhos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) return false; // árvore vazia: nenhum caminho existe, mesmo se targetSum for 0

    int restante = targetSum - root.val;

    // folha real: só aqui a pergunta "restante é zero?" faz sentido
    if (root.left == null && root.right == null) {
        return restante == 0;
    }

    // short-circuit: se o lado esquerdo já achou um caminho válido, nem avalia o direito
    return hasPathSum(root.left, restante) || hasPathSum(root.right, restante);
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

- Testar `restante == 0` num nó que **não** é folha — um nó intermediário pode ter soma parcial zero por coincidência (especialmente com valores negativos) sem que o caminho até uma folha real feche em zero.
- Cortar a busca cedo assumindo "se restante já é negativo, pode parar" — só é seguro fazer esse corte se todos os valores forem garantidamente não-negativos; como `Node.val` pode ser negativo aqui, um ramo aparentemente "estourado" ainda pode se corrigir mais abaixo.
- Esquecer o caso `root == null` retornando `false` diretamente — sem ele, uma árvore vazia com `targetSum = 0` erraria para `true` se a checagem de folha fosse feita antes da checagem de nulo.
- Confundir com [0113] Path Sum II, que pede para **retornar os caminhos**, não só `true`/`false` — a versão II não pode usar o truque de descartar a lista de valores, porque a lista É a resposta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = [], targetSum = 0` | `false` | nenhum caminho existe numa árvore vazia, independente do alvo |
| Um nó igual ao alvo | `root = [5], targetSum = 5` | `true` | a própria raiz já é a folha, caso mínimo não-vazio |
| Valores negativos no caminho | `root = [1,-2,-3], targetSum = -1` | `true` (`1 + -2 = -1`) | garante que não há corte prematuro por "soma ficou negativa" |
| Soma bate num nó intermediário, não numa folha | `root = [1,2], targetSum = 1` | `false` | a raiz sozinha soma 1, mas não é folha (tem filho 2); só o caminho `1→2` (soma 3) conta |

## 🔗 Conexões

- Problemas irmãos: [0113] Path Sum II (mesma ideia, mas precisa retornar todos os caminhos válidos, não só um booleano), [0437] Path Sum III (caminhos não precisam começar na raiz nem terminar numa folha, usa prefix sum com hash map)
- No backend: acumular um "orçamento restante" enquanto desce numa estrutura hierárquica aparece em validação de limites de gasto por departamento numa árvore organizacional, e em roteamento de mensagens onde cada nó intermediário consome parte de um "TTL"/budget antes de repassar adiante.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
