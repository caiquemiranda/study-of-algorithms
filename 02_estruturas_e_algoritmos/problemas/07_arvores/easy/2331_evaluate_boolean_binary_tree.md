# [2331] Evaluate Boolean Binary Tree

> 🔗 [LeetCode 2331](https://leetcode.com/problems/evaluate-boolean-binary-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma **árvore binária cheia** (todo nó tem 0 ou 2 filhos) onde folhas valem `0` (falso) ou `1` (verdadeiro), e nós internos valem `2` (OR) ou `3` (AND), **avalie** a árvore como uma expressão booleana e retorne o resultado.

**Exemplos:**
```
Input:  root = [2,1,3,null,null,0,1]
Output: true
Explicação: o nó AND avalia False AND True = False; o nó OR avalia True OR False = True

Input:  root = [0]
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 1000]` → precisa de solução O(n)
- Todo nó tem exatamente `0` ou `2` filhos (árvore **cheia**) → nunca existe o caso de um nó ter só um filho; simplifica a lógica, pois um nó não-folha sempre tem os dois lados disponíveis para avaliar
- Folhas valem só `0`/`1`, internos só `2`/`3` → os dois "tipos" de nó nunca se confundem; o valor do nó já diz o que fazer com ele

## 🧭 Como reconhecer o padrão

"Árvore onde folhas são valores e nós internos são operadores" é a estrutura de uma **árvore de expressão**: cada nó interno precisa da resposta dos dois filhos (avaliados recursivamente) antes de poder calcular a própria resposta — é o mesmo padrão pós-ordem de "o pai precisa do resultado dos filhos" já visto em [0543] Diameter e [0563] Binary Tree Tilt, mas aqui o "resultado" é um booleano combinado por AND/OR em vez de um número.

## 🐢 Solução 1 — Força bruta (converter para expressão em texto e usar um parser)

Percorrer a árvore construindo uma **string** de expressão booleana totalmente parentizada (ex.: `"(true OR (false AND true))"`), e depois usar um parser/avaliador de expressões genérico (do tipo usado em calculadoras, como em LC 224/227) para interpretar e avaliar essa string.

- Tempo: O(n) para construir a string, mais O(n) para o parser reprocessá-la — dobra o trabalho · Espaço: O(n) para a string, mais a estrutura interna do parser (pilhas de operadores/operandos)
- **Por que não basta:** a árvore **já é** a estrutura de uma expressão pronta para ser avaliada diretamente por recursão — textualizar tudo em string e depois escrever (ou reaproveitar) um parser inteiro para reinterpretar essa string é resolver o mesmo problema duas vezes, com uma camada de complexidade (parsing de texto) que nunca precisava existir.

## 💡 Solução 2 — A ideia otimizada (intuição)

DFS que avalia diretamente: se o nó é **folha** (`val` é 0 ou 1), o resultado é simplesmente esse valor como booleano. Se é **interno** (`val` é 2 ou 3), avalie recursivamente os dois filhos primeiro, e combine os resultados com `OR` (se `val == 2`) ou `AND` (se `val == 3`).

## 🎬 Exemplo passo a passo

`root = [2,1,3,null,null,0,1]` → raiz `2` (OR) tem filho esquerdo `1` (folha=true) e filho direito `3` (AND, com filhos `0` e `1`)

```
        2 (OR)
       /      \
      1        3 (AND)
   (true)     /      \
             0        1
          (false)   (true)
```

| Passo | Nó | Tipo | Avaliação |
|---|---|---|---|
| 1 | 1 (folha) | folha | `true` |
| 2 | 0 (folha) | folha | `false` |
| 3 | 1 (folha) | folha | `true` |
| 4 | 3 (AND) | interno | `false AND true = false` |
| 5 | 2 (OR, raiz) | interno | `true OR false = true` |

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado e avaliado exatamente uma vez
- **Espaço:** O(h) de pilha de recursão — nenhuma string ou estrutura de parser auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean evaluateTree(TreeNode root) {
    // folha: o próprio valor (0 ou 1) já é a resposta booleana
    if (root.left == null && root.right == null) {
        return root.val == 1;
    }

    // interno: SEMPRE tem os dois filhos (árvore cheia garantida pelo enunciado)
    boolean esquerda = evaluateTree(root.left);
    boolean direita = evaluateTree(root.right);

    // val == 2 é OR, val == 3 é AND — únicos dois valores possíveis para nó interno
    return (root.val == 2) ? (esquerda || direita) : (esquerda && direita);
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

- Avaliar os filhos com curto-circuito do próprio operador Java (`||`/`&&`) achando que isso evita a recursão do outro lado — **não** evita: as chamadas `evaluateTree(root.left)` e `evaluateTree(root.right)` já são calculadas **antes** de aplicar o operador (guardadas em variáveis), então ambas sempre são avaliadas; isso é necessário aqui, diferente de outros problemas onde short-circuit evita trabalho.
- Confundir os códigos: `2` é OR, `3` é AND — fácil de trocar, já que não há relação intuitiva óbvia entre o número e a operação; vale a pena fixar isso explicitamente no código com nomes claros (ou comentário) em vez de confiar na memória.
- Tentar tratar um nó com valor `0` ou `1` como se pudesse ser interno — a estrutura garante que folhas só têm esses dois valores e nós internos só têm `2`/`3`, então checar `root.left == null` já é suficiente para decidir; não precisa também checar o valor para saber se é folha.
- Construir a árvore de expressão em texto (a força bruta) quando a estrutura já está pronta para avaliação direta — funciona, mas duplica trabalho sem necessidade.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só, falso | `root = [0]` | `false` | caso base, cobre o exemplo 2 do enunciado |
| Um nó só, verdadeiro | `root = [1]` | `true` | caso base positivo mínimo |
| OR simples | `root = [2,0,1]` | `true` | `false OR true = true`, testa o operador OR isoladamente |
| AND simples | `root = [3,1,0]` | `false` | `true AND false = false`, testa o operador AND isoladamente |

## 🔗 Conexões

- Problemas irmãos: [0224]/[0227] Basic Calculator (avaliação de expressões, mas a partir de string em vez de árvore já estruturada), [0543] Diameter of Binary Tree (mesmo padrão pós-ordem de "combinar resultados dos filhos no nó pai")
- No backend: árvores de expressão booleana avaliadas recursivamente são exatamente como motores de regras de negócio avaliam condições compostas (ex.: "(região == 'BR' OR vip == true) AND ativo == true" representado como árvore de AST) sem nunca precisar reprocessar texto em tempo de execução.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
