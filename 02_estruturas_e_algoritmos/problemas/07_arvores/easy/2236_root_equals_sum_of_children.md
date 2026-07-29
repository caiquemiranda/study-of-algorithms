# [2236] Root Equals Sum of Children

> 🔗 [LeetCode 2236](https://leetcode.com/problems/root-equals-sum-of-children/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária que tem **exatamente 3 nós** (raiz, filho esquerdo, filho direito), retorne `true` se o valor da raiz for igual à soma dos valores dos dois filhos.

**Exemplos:**
```
Input:  root = [10,4,6]
Output: true
Explicação: 10 = 4 + 6

Input:  root = [5,3,1]
Output: false
Explicação: 5 ≠ 3 + 1
```

**Restrições (e o que elas denunciam):**
- "A árvore consiste **exatamente** em raiz, filho esquerdo e filho direito" → não há caso de árvore vazia, com um filho só, ou com mais de 3 nós; a estrutura é **fixa**, não genérica
- `-100 <= Node.val <= 100` → valores cabem em `int`, soma de dois valores nesse range não estoura

## 🧭 Como reconhecer o padrão

Diferente da maioria dos problemas de árvore, aqui **não há generalização nenhuma para fazer**: a estrutura é sempre a mesma (3 nós fixos), então a resposta é simplesmente ler três campos e comparar — não é preciso recursão, DFS, nem qualquer travessia.

## 🐢 Solução 1 — Força bruta (tratar como árvore genérica)

Escrever uma função recursiva genérica de "soma de todos os nós da árvore" (que funcionaria para uma árvore de qualquer tamanho), aplicá-la nos dois filhos separadamente, e comparar o resultado com `root.val`.

- Tempo: O(1) de qualquer forma, já que só existem 3 nós · Espaço: O(1) a O(h) dependendo de como a recursão genérica é escrita
- **Por que não basta:** não é uma questão de complexidade assintótica (ambas as soluções são O(1) aqui), e sim de **complexidade desnecessária**: escrever e chamar uma função recursiva genérica de árvore para um caso que o próprio enunciado já garante como fixo é over-engineering — três acessos de campo resolvem tudo.

## 💡 Solução 2 — A ideia otimizada (intuição)

Acesse diretamente os três valores garantidos pela estrutura fixa: `root.val`, `root.left.val`, `root.right.val`. Compare o primeiro com a soma dos outros dois.

## 🎬 Exemplo passo a passo

`root = [10,4,6]`

```
    10
   /  \
  4    6
```

| Campo acessado | Valor |
|---|---|
| `root.val` | 10 |
| `root.left.val` | 4 |
| `root.right.val` | 6 |
| `root.left.val + root.right.val` | 10 |
| `root.val == soma`? | `10 == 10` → `true` |

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) — sempre exatamente 3 acessos de campo e uma comparação, independente de qualquer coisa
- **Espaço:** O(1) — nenhuma estrutura auxiliar, nenhuma recursão

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean checkTree(TreeNode root) {
    // estrutura garantida pelo enunciado: sempre existem left e right, sem precisar checar null
    return root.val == root.left.val + root.right.val;
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

- Adicionar checagens de `null` para `root.left`/`root.right` — o enunciado **garante** que a árvore sempre tem exatamente esses 3 nós; checagens defensivas aqui são código morto que nunca vai disparar, mas ainda assim poluem a solução.
- Escrever uma função recursiva genérica (a força bruta) para um problema que é, na prática, aritmética de 3 números — reconhecer quando a generalização é desnecessária é tão importante quanto saber generalizar quando é preciso.
- Inverter a comparação (`root.left.val == root.val + root.right.val`) — a soma tem que ser dos **dois filhos**, comparada com a **raiz**, não qualquer outra combinação dos três valores.
- Assumir que existe algum caso de borda como árvore vazia ou com um filho só — a restrição do enunciado elimina esses casos por definição; não há necessidade (nem seria coerente com o enunciado) de tratá-los.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Soma correta | `root = [10,4,6]` | `true` | cobre o exemplo 1 do enunciado |
| Soma incorreta | `root = [5,3,1]` | `false` | cobre o exemplo 2 do enunciado |
| Valores negativos que se cancelam | `root = [0,-5,5]` | `true` | garante que a soma funciona corretamente com negativos |
| Filhos com valor zero | `root = [0,0,0]` | `true` | caso extremo, soma de zeros ainda bate com raiz zero |

## 🔗 Conexões

- Problemas irmãos: [0563] Binary Tree Tilt (soma de subárvores esquerda/direita, mas generalizada para qualquer tamanho de árvore, não só 3 nós), [0112] Path Sum (também compara uma soma com um valor-alvo, mas numa árvore de tamanho arbitrário)
- No backend: esse tipo de checagem de "consistência local" com estrutura fixa e conhecida aparece em validação de registros de dados com esquema rígido (ex.: um registro contábil onde um campo "total" deve sempre bater com a soma de exatamente dois campos relacionados), onde generalizar demais o código de validação só adicionaria complexidade sem necessidade real.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
