# [0226] Invert Binary Tree

> 🔗 [LeetCode 226](https://leetcode.com/problems/invert-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, **inverta** a árvore (espelhe left/right em todo nó) e retorne a raiz.

**Exemplos:**
```
Input:  root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input:  root = [2,1,3]
Output: [2,3,1]

Input:  root = []
Output: []
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 100]` → entrada pequena, qualquer solução O(n) serve
- `-100 <= Node.val <= 100` → valores não importam para este problema, só a estrutura
- Não há follow-up pedindo iterativo aqui, mas ambas as travessias (DFS e BFS) resolvem igualmente bem — a escolha de qual usar é livre

## 🧭 Como reconhecer o padrão

"Inverter/espelhar uma árvore" é sempre "trocar `left` com `right` em **todo** nó, recursivamente". Não é preciso pensar em nenhuma ordem específica de travessia (pré, em ou pós-ordem funcionam igualmente) — o que importa é visitar cada nó exatamente uma vez e trocar seus dois ponteiros de filho.

## 🐢 Solução 1 — Força bruta (construir uma árvore nova invertida)

Recursivamente, construir uma **cópia** da árvore, alocando um `TreeNode` novo em cada posição, mas montando `left` da cópia a partir da inversão da subárvore `right` original (e vice-versa) — em vez de reaproveitar os nós que já existem.

- Tempo: O(n) · Espaço: O(n) para os nós novos alocados, além de O(h) de pilha de recursão
- **Por que não basta:** funciona, mas desperdiça memória alocando uma árvore paralela inteira quando o enunciado só pede para inverter a árvore **existente** — os nós originais já têm exatamente os ponteiros certos, só precisam ser trocados de lugar, não recriados.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em cada nó, apenas **troque os ponteiros** `left` e `right` que já existem (sem alocar nada novo), e desça recursivamente para continuar trocando nos filhos. Como a troca já reposiciona as subárvores inteiras de uma vez (o ponteiro carrega tudo que está pendurado nele), não é preciso "reconstruir" nada — só reatribuir referências.

## 🎬 Exemplo passo a passo

`root = [2,1,3]`

```
    2               2
   / \      →      / \
  1   3            3   1
```

| Passo | Nó | left antes | right antes | Ação | left depois | right depois |
|---|---|---|---|---|---|---|
| 1 | 1 | null | null | troca (nada muda, ambos nulos) | null | null |
| 2 | 3 | null | null | troca (nada muda, ambos nulos) | null | null |
| 3 | 2 | nó 1 | nó 3 | troca `left`↔`right` | nó 3 | nó 1 |

Resultado final: raiz `2` com `left = 3` e `right = 1` → `[2,3,1]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez, a troca é O(1) por nó
- **Espaço:** O(h) — só a pilha de recursão, nenhum nó novo é alocado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public TreeNode invertTree(TreeNode root) {
    if (root == null) return null; // caso base: nada para inverter

    // troca os ponteiros existentes — cada um já carrega a subárvore inteira pendurada nele
    TreeNode temp = root.left;
    root.left = root.right;
    root.right = temp;

    // continua invertendo recursivamente dentro de cada subárvore já trocada
    invertTree(root.left);
    invertTree(root.right);

    return root;
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

- Trocar os ponteiros **depois** de já ter chamado a recursão nos filhos originais (ordem errada de operações) — não quebra a corretude neste problema específico (a troca é local por nó), mas é fácil confundir se a lógica exigisse alguma ordem; o mais seguro é trocar primeiro, recursar depois (ou vice-versa, contanto que seja consistente).
- Usar uma variável temporária mal nomeada ou esquecer de guardar `root.left` **antes** de sobrescrevê-lo — sem a variável `temp`, `root.right = root.left` seguido de `root.left = root.right` acabaria copiando o mesmo valor duas vezes, perdendo a subárvore original da direita.
- Achar que precisa alocar nós novos (a força bruta) — o problema pede para inverter a árvore, não criar uma cópia invertida; reaproveitar os nós existentes é mais simples e mais barato em memória.
- Esquecer o caso base `root == null` — sem ele, chamar `invertTree` num filho ausente lança `NullPointerException` ao tentar acessar `.left`/`.right` de `null`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `[]` | caso base, retorna `null` imediatamente |
| Um nó só | `root = [1]` | `[1]` | trocar `null` com `null` não muda nada |
| Só filhos de um lado (skew) | `root = [1,2]` (2 é filho esquerdo) | `[1,null,2]` | valida que a inversão move um ramo inteiro de um lado para o outro |
| Árvore com múltiplos níveis | `root = [4,2,7,1,3,6,9]` | `[4,7,2,9,6,3,1]` | cobre o exemplo do enunciado, garante que a troca se propaga em todos os níveis, não só na raiz |

## 🔗 Conexões

- Problemas irmãos: [0100] Same Tree (a comparação de dois nós reaproveitada aqui seria útil para validar o resultado da inversão), [0101] Symmetric Tree (uma árvore simétrica é, por definição, igual à sua própria inversão)
- No backend: espelhar uma estrutura hierárquica aparece em suporte a layouts RTL (right-to-left) de interfaces (espelhar uma árvore de componentes de UI) e em transformações de árvores de sintaxe (AST) que trocam a ordem de avaliação de operandos em otimizadores de compiladores.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
