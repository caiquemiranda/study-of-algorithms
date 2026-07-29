# [0572] Subtree of Another Tree

> 🔗 [LeetCode 572](https://leetcode.com/problems/subtree-of-another-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dadas as raízes de duas árvores binárias `root` e `subRoot`, retorne `true` se existir um nó em `root` tal que a subárvore enraizada ali seja **idêntica** (mesma estrutura e valores) a `subRoot`. Uma árvore é considerada subárvore de si mesma.

**Exemplos:**
```
Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

**Restrições (e o que elas denunciam):**
- Nós de `root` em `[1, 2000]`, nós de `subRoot` em `[1, 1000]` → o produto `n * m` chega a 2 milhões no pior caso, ainda tratável em O(n·m), mas é o tipo de restrição que sinaliza "cuidado para não ficar pior que isso"
- `-10^4 <= root.val, subRoot.val <= 10^4` → valores cabem em `int`
- O exemplo 2 é a pegadinha central: `subRoot = [4,1,2]` aparece "quase igual" dentro de `root`, mas o nó `4` de `root` tem um filho extra (`0`) que `subRoot` não tem — **subárvore precisa bater exatamente**, incluindo a ausência de filhos extras

## 🧭 Como reconhecer o padrão

"Existe uma subárvore idêntica a outra árvore menor?" é [0100] Same Tree aplicada repetidamente: para cada nó de `root`, pergunte "a subárvore que começa aqui é exatamente igual a `subRoot`?". Basta reaproveitar a lógica de comparação estrutural nó a nó já usada lá, só que agora testando em **todos** os pontos de partida possíveis de `root`, não só na raiz.

## 🐢 Solução 1 — Força bruta (serializar cada subárvore candidata e comparar)

Para cada nó de `root` (visitado via DFS), construir uma **lista nova** com todos os valores da subárvore que começa ali (uma travessia completa, sempre até o fim, mesmo que os primeiros valores já não batam com `subRoot`), e só depois comparar essa lista com a serialização de `subRoot`.

- Tempo: O(n · m) no pior caso, com uma constante pior na prática · Espaço: O(m) por comparação, refeito a cada nó testado (alocação repetida)
- **Por que não basta:** duas fontes de desperdício. Primeiro, aloca uma lista nova a cada nó candidato, mesmo para candidatos que claramente não vão bater. Segundo, sempre percorre a subárvore **inteira** antes de comparar, mesmo quando os dois primeiros valores já divergem — não existe short-circuit, porque a comparação só acontece depois que a lista inteira foi montada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `root` com DFS. Em cada nó visitado, chame a mesma função de "são exatamente iguais?" de [0100] Same Tree, comparando a subárvore que começa **naquele nó** com `subRoot` diretamente nó a nó — sem alocar nenhuma estrutura auxiliar, e com **curto-circuito**: assim que um valor diverge, a comparação para imediatamente, sem terminar de visitar o resto da subárvore. (Existe uma solução ainda mais rápida, O(n+m), serializando as duas árvores com marcadores de nulo únicos e buscando `subRoot` como substring de `root` via KMP — mas ela troca o problema de árvores por um problema de string matching, fora do escopo didático deste nível.)

## 🎬 Exemplo passo a passo

`root = [3,4,5,1,2]`, `subRoot = [4,1,2]`

```
root:        3           subRoot:   4
            / \                    / \
           4   5                  1   2
          / \
         1   2
```

| Passo | Nó de root visitado | isSameTree(nó, subRoot)? | Ação |
|---|---|---|---|
| 1 | 3 | 3 ≠ 4, `false` de cara | continua a busca nos filhos |
| 2 | 4 | 4==4, 1==1, 2==2, ambos sem mais filhos → `true` | encontrou! para aqui |

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n · m) — no pior caso, tenta a comparação completa em cada um dos n nós de `root`, e cada comparação pode custar até m
- **Espaço:** O(altura de root + altura de subRoot) — pilha de recursão do DFS externo somada à pilha da comparação `isSameTree`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isSubtree(TreeNode root, TreeNode subRoot) {
    if (root == null) return false; // acabou root sem achar bate-igual: não existe mais onde procurar

    // tenta bater exatamente A PARTIR deste nó; se bater, já resolve
    if (isSameTree(root, subRoot)) return true;

    // senão, procura recursivamente nos filhos de root (subRoot continua o mesmo)
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}

// mesma lógica de [0100] Same Tree: comparação estrutural nó a nó
private boolean isSameTree(TreeNode a, TreeNode b) {
    if (a == null && b == null) return true;
    if (a == null || b == null) return false;
    if (a.val != b.val) return false;
    return isSameTree(a.left, b.left) && isSameTree(a.right, b.right);
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

- Verificar só se os **valores** de `subRoot` aparecem em algum lugar de `root`, sem checar estrutura — o exemplo 2 do enunciado existe exatamente para pegar esse erro: `4,1,2` aparece nos valores de `root`, mas com um filho extra (`0`) que quebra a igualdade estrutural exata.
- Usar `isSameTree` para comparar `root` inteira com `subRoot` (sem tentar a partir de cada nó) — isso só checaria se `subRoot` é a árvore **inteira**, não uma subárvore em qualquer posição.
- Esquecer o caso base `root == null` no `isSubtree` — sem ele, a recursão que desce pelos filhos de `root` quebra com `NullPointerException` ao tentar comparar contra um nó ausente.
- Achar que basta parar na primeira vez que `root.val == subRoot.val` sem chamar `isSameTree` completo — um valor de raiz igual não garante que os filhos também batem; é preciso a comparação estrutural inteira.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore igual a ela mesma | `root = [1,2,3], subRoot = [1,2,3]` | `true` | "uma árvore é subárvore de si mesma", conforme o enunciado |
| subRoot é uma folha só | `root = [1,2,3], subRoot = [2]` | `true` | subárvore de tamanho 1 também é válida |
| Valores batem mas estrutura não (filho extra) | `root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]` | `false` | cobre o exemplo 2 do enunciado, o caso clássico da pegadinha |
| subRoot maior que qualquer subárvore de root | `root = [1], subRoot = [1,2]` | `false` | garante que o algoritmo não afirma falsamente quando subRoot não cabe em nenhum lugar |

## 🔗 Conexões

- Problemas irmãos: [0100] Same Tree (a função de comparação reaproveitada integralmente aqui), [0101] Symmetric Tree (outra variação de comparação estrutural entre nós)
- No backend: detectar se uma estrutura menor aparece dentro de uma maior é o mesmo padrão usado para achar padrões de fraude repetidos dentro de árvores de transações, ou para verificar se um fragmento de configuração (subárvore de um JSON/YAML) já existe dentro de uma configuração maior antes de mesclar.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
