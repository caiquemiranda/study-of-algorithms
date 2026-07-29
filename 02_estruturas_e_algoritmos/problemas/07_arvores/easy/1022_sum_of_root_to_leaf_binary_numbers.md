# [1022] Sum of Root To Leaf Binary Numbers

> 🔗 [LeetCode 1022](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária onde cada nó vale `0` ou `1`, cada caminho raiz-folha representa um número binário (bit mais significativo primeiro). Retorne a **soma** de todos esses números, considerando todas as folhas.

**Exemplos:**
```
Input:  root = [1,0,1,0,1,0,1]
Output: 22
Explicação: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Input:  root = [0]
Output: 0
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 1000]` → precisa de solução O(n)
- `Node.val` é `0` ou `1` → cada nó é literalmente um bit do número binário formado pelo caminho
- "a resposta cabe num inteiro de 32 bits" → não é preciso se preocupar com números arbitrariamente grandes, `int` (ou `long` por segurança) já basta

## 🧭 Como reconhecer o padrão

"Cada caminho raiz-folha representa um número (binário, decimal, etc.)" é a mesma estrutura de [0112] Path Sum e [0257] Binary Tree Paths: descer acumulando um estado conforme os nós são visitados, e "fechar a conta" só ao chegar numa folha. A diferença aqui é **como** o estado é acumulado: não é soma nem lista, é a construção de um número via deslocamento de bits.

## 🐢 Solução 1 — Força bruta (construir strings binárias e converter)

DFS que constrói o caminho como uma **string** de `'0'`s e `'1'`s, concatenando a cada nível (`caminho + no.val`). Ao chegar numa folha, converte a string acumulada para inteiro com `Integer.parseInt(caminho, 2)` e soma ao total.

- Tempo: O(n · h) no pior caso (concatenação de string custa proporcional ao tamanho atual, mais a conversão de string para inteiro por folha) · Espaço: O(n) para as strings
- **Por que não basta:** concatenar strings repetidamente e depois fazer parsing delas é trabalho totalmente desnecessário — o "número binário até aqui" pode ser mantido diretamente como um **inteiro**, atualizado com uma operação de bits O(1) a cada nível, sem nunca passar por texto.

## 💡 Solução 2 — A ideia otimizada (intuição)

Carregue o "número binário até aqui" como um `int`, atualizado a cada passo com `numeroAtual = numeroAtual * 2 + no.val` (equivalente a deslocar um bit para a esquerda e adicionar o novo bit — a mesma operação de `numeroAtual << 1 | no.val`). Ao chegar numa folha, esse `numeroAtual` já É o número completo do caminho; some-o direto ao total, sem nenhuma conversão.

## 🎬 Exemplo passo a passo

`root = [1,0,1,0,1,0,1]` — caminho da esquerda: `1 → 0 → 0` = binário `100` = 4

```
        1
       / \
      0   1
     / \ / \
    0  1 0  1
```

| Passo | Nó | numeroAtual ao entrar | É folha? | Ação |
|---|---|---|---|---|
| 1 | 1 (raiz) | 0*2+1 = 1 | não | desce |
| 2 | 0 (esquerda) | 1*2+0 = 2 | não | desce |
| 3 | 0 (folha) | 2*2+0 = 4 | sim | soma 4 (caminho `100`) |
| 4 | 1 (folha, irmão) | 2*2+1 = 5 | sim | soma 5 (caminho `101`) → total 9 |
| ... | (ramo direito, análogo) | — | — | soma 6 (`110`) e 7 (`111`) → total final 22 |

Resultado final: `22` ✔ (4+5+6+7, bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez, e a atualização do número é O(1) por nó
- **Espaço:** O(h) de pilha de recursão — nenhuma string intermediária

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int sumRootToLeaf(TreeNode root) {
    return dfs(root, 0);
}

private int dfs(TreeNode no, int numeroAtual) {
    if (no == null) return 0; // subárvore vazia não contribui à soma

    // desloca um bit para a esquerda e adiciona o bit deste nó (equivalente a numeroAtual << 1 | no.val)
    numeroAtual = numeroAtual * 2 + no.val;

    if (no.left == null && no.right == null) {
        return numeroAtual; // folha: o número do caminho está completo
    }

    return dfs(no.left, numeroAtual) + dfs(no.right, numeroAtual);
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

- Usar `numeroAtual + no.val` em vez de `numeroAtual * 2 + no.val` — sem o deslocamento (`* 2`), os bits anteriores não "empurram" para a esquerda, e o número final fica errado (é literalmente a diferença entre binário posicional e uma soma simples).
- Concatenar strings a cada nível (a força bruta) — funciona para 1000 nós, mas carrega o mesmo hábito ineficiente já visto em [0257] Binary Tree Paths.
- Esquecer o teste de folha (`no.left == null && no.right == null`) e somar em **todo** nó, não só nas folhas — o problema pede a soma dos números de caminhos **raiz-folha**, nós intermediários não representam um número completo.
- Testar `no == null` como se fosse folha — um nó nulo não existe, é só o sinal de "não desça mais aqui"; a checagem de folha é sobre `left == null && right == null` de um nó que **existe**.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só, valor 0 | `root = [0]` | `0` | caso base, cobre o exemplo 2 do enunciado |
| Um nó só, valor 1 | `root = [1]` | `1` | caso base positivo mínimo |
| Só filhos à esquerda (skew) | `root = [1,0,null,1]` | `5` (binário `101`) | testa o acúmulo numa corrente única, sem ramificação |
| Árvore completa de 3 níveis | exemplo 1 do enunciado | `22` | valida múltiplos caminhos somados corretamente |

## 🔗 Conexões

- Problemas irmãos: [0112] Path Sum (mesma estrutura de "acumular estado numérico durante a descida, fechar na folha"), [0257] Binary Tree Paths (mesma travessia raiz-folha, mas coletando strings em vez de calcular um número)
- No backend: acumular um valor via deslocamento de bits durante uma travessia hierárquica é o mesmo princípio usado na construção de identificadores hierárquicos codificados em bits (ex.: paths de árvores de decisão codificados como um único inteiro para lookup rápido em tabelas de roteamento ou em Trie compactadas em bitmask).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
