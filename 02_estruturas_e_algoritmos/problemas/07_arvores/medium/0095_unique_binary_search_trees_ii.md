# [0095] Unique Binary Search Trees II

> 🔗 [LeetCode 95](https://leetcode.com/problems/unique-binary-search-trees-ii/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DivideEConquista` `#Backtracking`

## 📜 O Problema

Dado um inteiro `n`, retorne **todas** as BSTs estruturalmente diferentes que têm exatamente `n` nós com valores únicos de `1` a `n`. Retorne em qualquer ordem.

**Exemplos:**
```
Input:  n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Input:  n = 1
Output: [[1]]
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 8` → o limite é bem pequeno de propósito: o número de BSTs distintas cresce exponencialmente (é o número de Catalan de `n`), então `n = 8` já produz 1430 árvores — o problema não pede performance extrema, pede gerar tudo **sem duplicar trabalho**
- Valores **de 1 a n**, sempre os mesmos → não é preciso escolher quais valores usar, só como estruturá-los

## 🧭 Como reconhecer o padrão

"Gere **todas** as estruturas possíveis" com uma faixa contígua de valores (`1..n`) é o sinal de **divide e conquista recursivo**: para cada valor `i` escolhido como raiz, os valores `1..i-1` só podem formar a subárvore esquerda e `i+1..n` só podem formar a direita (propriedade de BST). O problema se quebra em "todas as formas possíveis da esquerda" combinadas com "todas as formas possíveis da direita" — um produto cartesiano de subproblemas menores e idênticos em formato.

## 🐢 Solução 1 — Força bruta (gerar todas as permutações de inserção)

Gerar todas as `n!` permutações da sequência `1..n`, inserir cada permutação numa BST vazia (usando inserção normal de BST), e coletar as árvores resultantes — descartando as que já apareceram (comparando estrutura com todas as já coletadas).

- Tempo: O(n! · n) só para gerar e inserir, mais o custo de deduplicação comparando árvores — extremamente mais caro que o necessário · Espaço: proporcional a `n!`
- **Por que não basta:** a maioria das `n!` permutações de inserção produz **a mesma** árvore final (várias ordens de inserção diferentes levam à mesma estrutura), então a maior parte do trabalho é jogado fora na deduplicação. Além disso, comparar estruturas de árvore repetidamente para achar duplicatas é caro e desnecessário quando dá para gerar cada estrutura **exatamente uma vez**, por construção.

## 💡 Solução 2 — A ideia otimizada (intuição)

Escreva uma função `gerar(inicio, fim)` que retorna a lista de todas as BSTs possíveis usando os valores `inicio..fim`. Para cada valor `i` nesse intervalo, escolhido como raiz: gere recursivamente **todas** as subárvores esquerdas possíveis (`gerar(inicio, i-1)`) e **todas** as direitas possíveis (`gerar(i+1, fim)`). Combine **cada** subárvore esquerda com **cada** subárvore direita (produto cartesiano), criando um novo nó raiz `i` para cada combinação. Caso base: intervalo vazio (`inicio > fim`) retorna uma lista com um único elemento `null` (representa "nenhuma subárvore aqui", mas ainda participa do produto cartesiano).

## 🎬 Exemplo passo a passo

`n = 3` → `gerar(1, 3)`

| Raiz escolhida (i) | Subárvores esquerdas (gerar(1,i-1)) | Subárvores direitas (gerar(i+1,3)) | Combinações geradas |
|---|---|---|---|
| 1 | `[null]` (intervalo vazio) | `gerar(2,3)` → 2 árvores possíveis com {2,3} | 1 × 2 = 2 árvores com raiz 1 |
| 2 | `gerar(1,1)` → `[1]` (só uma forma) | `gerar(3,3)` → `[3]` (só uma forma) | 1 × 1 = 1 árvore com raiz 2 |
| 3 | `gerar(1,2)` → 2 árvores possíveis com {1,2} | `[null]` (intervalo vazio) | 2 × 1 = 2 árvores com raiz 3 |

Total: 2 + 1 + 2 = **5 árvores** distintas ✔ (bate com o enunciado, que lista exatamente 5 estruturas para `n=3`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(Catalan(n) · n) — o número de Catalan de `n` é a quantidade de BSTs distintas, e cada uma custa O(n) para ser montada/copiada nas combinações
- **Espaço:** O(Catalan(n) · n) para armazenar todas as árvores geradas na resposta final

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<TreeNode> generateTrees(int n) {
    if (n == 0) return new ArrayList<>();
    return gerar(1, n);
}

private List<TreeNode> gerar(int inicio, int fim) {
    List<TreeNode> resultado = new ArrayList<>();

    if (inicio > fim) {
        // intervalo vazio: "nenhuma subárvore aqui" ainda participa do produto cartesiano
        resultado.add(null);
        return resultado;
    }

    for (int i = inicio; i <= fim; i++) {
        // tudo à esquerda de i vira subárvore esquerda; tudo à direita vira subárvore direita
        List<TreeNode> esquerdas = gerar(inicio, i - 1);
        List<TreeNode> direitas = gerar(i + 1, fim);

        // produto cartesiano: cada combinação (esquerda, direita) forma uma árvore distinta com raiz i
        for (TreeNode esq : esquerdas) {
            for (TreeNode dir : direitas) {
                TreeNode raiz = new TreeNode(i);
                raiz.left = esq;
                raiz.right = dir;
                resultado.add(raiz);
            }
        }
    }

    return resultado;
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

- Esquecer o caso base `inicio > fim` retornando uma lista com `null` (e não uma lista **vazia**) — se a lista voltar vazia, o produto cartesiano (`for esq : esquerdas`) nunca executa, e nenhuma árvore é gerada para aquele lado, mesmo quando o lado deveria contribuir com "nenhum filho" como opção válida.
- Reaproveitar o **mesmo nó** `TreeNode` em várias árvores da resposta (compartilhar referências entre combinações) — cada combinação do produto cartesiano precisa de um nó raiz **novo**, mesmo que os filhos (`esq`/`dir`) sejam reaproveitados de listas já geradas (isso é seguro, porque cada subárvore de `esquerdas`/`direitas` nunca é modificada depois de criada).
- Gerar por permutações de inserção (a força bruta) — funciona para `n` pequeno, mas desperdiça um fator enorme de trabalho redundante e de deduplicação cara.
- Confundir este problema com [0096] Unique Binary Search Trees — aqui é preciso **construir e retornar** as árvores; lá, só contar quantas existem (sem nunca alocar um nó).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| n = 1 | `n = 1` | `[[1]]` | caso base, uma única árvore possível (um nó só) |
| n = 0 (fora do range oficial, mas didático) | `n = 0` | `[]` | testa o tratamento explícito de entrada mínima antes do range garantido |
| n = 2 | `n = 2` | 2 árvores: `[1,null,2]` e `[2,1]` | menor caso com mais de uma estrutura possível, valida a recursão em ambos os sentidos |
| n = 3 | `n = 3` | 5 árvores | cobre o exemplo do enunciado, valida o produto cartesiano completo |

## 🔗 Conexões

- Problemas irmãos: [0096] Unique Binary Search Trees (a versão que só conta, sem construir), [0108] Convert Sorted Array to Binary Search Tree (mesma ideia de "escolher um valor como raiz e dividir o resto entre esquerda e direita", mas com uma única escolha ótima em vez de todas as possíveis)
- No backend: gerar todas as estruturas possíveis de um espaço combinatório respeitando uma restrição de ordem é o mesmo princípio usado em geração de todos os planos de execução possíveis de uma consulta SQL (diferentes ordens de junção de tabelas) antes do otimizador escolher o mais barato.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
