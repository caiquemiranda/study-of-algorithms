# [0872] Leaf-Similar Trees

> 🔗 [LeetCode 872](https://leetcode.com/problems/leaf-similar-trees/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dadas as raízes de duas árvores binárias `root1` e `root2`, retorne `true` se a **sequência de valores das folhas**, lida da esquerda para a direita, for igual nas duas árvores.

**Exemplos:**
```
Input:  root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Input:  root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em cada árvore em `[1, 200]` → entrada pequena, qualquer O(n) resolve
- Valores em `[0, 200]` → cabem em `int`
- "sequência de valores das folhas, da esquerda para a direita" → a **estrutura interna** das duas árvores pode ser completamente diferente (como no exemplo 1, onde as árvores têm formatos distintos); só a sequência final de folhas importa

## 🧭 Como reconhecer o padrão

"Comparar apenas as folhas, ignorando a estrutura interna" é diferente de [0100] Same Tree: aqui não interessa se os nós internos batem, só a sequência de valores nas pontas. A técnica é: extrair a sequência de folhas de cada árvore via DFS (que naturalmente visita da esquerda para a direita), e comparar as duas sequências no final.

## 🐢 Solução 1 — Força bruta (coletar todos os nós, filtrar depois)

DFS que adiciona **todo** nó visitado (folha ou não) numa lista, junto com uma marcação de "é folha?". Só no final, filtrar a lista mantendo apenas os valores marcados como folha.

- Tempo: O(n1 + n2) · Espaço: O(n1 + n2) para as listas completas, antes da filtragem
- **Por que não basta:** guarda e depois descarta informação sobre nós que nunca precisavam ter sido guardados — o teste "é folha?" (`no.left == null && no.right == null`) já está disponível no momento da visita; adicionar só as folhas diretamente elimina a etapa de filtrar depois e o espaço gasto com os nós internos.

## 💡 Solução 2 — A ideia otimizada (intuição)

DFS que, ao visitar um nó, só adiciona o valor à lista de saída **se** o nó for folha — não guarda nada sobre nós internos. Faça isso para as duas árvores separadamente (gerando duas listas só de folhas) e compare as duas listas no final com `.equals()`.

## 🎬 Exemplo passo a passo

`root1 = [1,2,3]`, `root2 = [1,3,2]`

```
t1:    1        t2:    1
      / \             / \
     2   3           3   2
```

| Passo | Árvore | DFS visita | É folha? | Lista de folhas |
|---|---|---|---|---|
| 1 | t1 | 2 | sim | `[2]` |
| 2 | t1 | 3 | sim | `[2,3]` |
| 3 | t2 | 3 | sim | `[3]` |
| 4 | t2 | 2 | sim | `[3,2]` |

Comparação final: `[2,3]` vs `[3,2]` → diferentes.

Resultado final: `false` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n1 + n2) — cada nó de cada árvore é visitado exatamente uma vez
- **Espaço:** O(folhas1 + folhas2) — só os valores das folhas são guardados, não todos os nós

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean leafSimilar(TreeNode root1, TreeNode root2) {
    List<Integer> folhas1 = new ArrayList<>();
    List<Integer> folhas2 = new ArrayList<>();

    coletarFolhas(root1, folhas1);
    coletarFolhas(root2, folhas2);

    return folhas1.equals(folhas2); // List.equals já compara elemento a elemento, na ordem
}

private void coletarFolhas(TreeNode no, List<Integer> folhas) {
    if (no == null) return;

    // só adiciona se for folha: DFS naturalmente visita da esquerda para a direita
    if (no.left == null && no.right == null) {
        folhas.add(no.val);
        return;
    }

    coletarFolhas(no.left, folhas);
    coletarFolhas(no.right, folhas);
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

- Usar BFS para coletar as folhas em vez de DFS — BFS visita por **nível**, não da esquerda para a direita "estrutural"; uma folha rasa (num nível baixo) pode aparecer antes de uma folha mais profunda que deveria vir primeiro na ordem esquerda-para-direita real da árvore, produzindo uma sequência errada.
- Comparar o **tamanho** das duas árvores (número de nós) achando que precisa ser igual — o exemplo 1 do enunciado mostra árvores com formatos e tamanhos de estrutura interna completamente diferentes, mas com a mesma sequência de folhas.
- Guardar nós internos na lista e filtrar depois (a força bruta) — funciona, mas gasta memória guardando informação que já era descartável no momento da visita.
- Comparar as listas com `==` em vez de `.equals()` em Java — `==` entre objetos `List` compara referência, não conteúdo; sempre daria `false` mesmo quando as listas têm os mesmos valores.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvores com uma folha cada | `root1 = [1], root2 = [1]` | `true` | a própria raiz é a única folha em ambas |
| Mesma sequência, estrutura diferente | exemplo 1 do enunciado | `true` | valida que a estrutura interna não importa, só a sequência final |
| Mesmos valores, ordem diferente | `root1 = [1,2,3], root2 = [1,3,2]` | `false` | cobre o exemplo 2, a ordem esquerda-direita importa |
| Quantidade de folhas diferente | `root1 = [1,2], root2 = [1,2,3]` | `false` | listas de tamanhos diferentes nunca são iguais, `.equals()` já cobre isso |

## 🔗 Conexões

- Problemas irmãos: [0100] Same Tree (compara toda a estrutura, não só as folhas), [0404] Sum of Left Leaves (também filtra por "é folha?" durante a descida, mas soma em vez de coletar sequência)
- No backend: comparar apenas os elementos "terminais" de duas estruturas hierárquicas (ignorando a organização interna) aparece em comparação de resultados finais de pipelines de processamento em árvore com implementações internas diferentes, e em testes de regressão que validam só a saída observável, não os passos intermediários.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
