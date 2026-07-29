# [0563] Binary Tree Tilt

> 🔗 [LeetCode 563](https://leetcode.com/problems/binary-tree-tilt/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dado o `root` de uma árvore binária, retorne a **soma da inclinação (tilt)** de todos os nós. A inclinação de um nó é a diferença absoluta entre a soma dos valores da subárvore esquerda e a soma dos valores da subárvore direita (subárvore ausente conta como soma 0).

**Exemplos:**
```
Input:  root = [1,2,3]
Output: 1

Input:  root = [4,2,9,3,5,null,7]
Output: 15
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[0, 10^4]` → precisa de solução O(n); recalcular soma de subárvore por nó (O(n²)) fica arriscado no limite superior
- `-1000 <= Node.val <= 1000` → valores podem ser negativos, então a soma de uma subárvore não é necessariamente "quanto maior, mais nós" — precisa somar de verdade, não estimar pelo tamanho
- A definição diz "soma de **todo** nó" (não só a raiz) → é preciso acumular um total, um valor por nó, igual ao padrão de [0543] Diameter

## 🧭 Como reconhecer o padrão

"Soma da subárvore esquerda vs direita, em **todo** nó" é outro caso do molde "duas perguntas numa passada pós-ordem só": cada nó precisa saber a soma da própria subárvore (informação que o pai vai usar) e, ao mesmo tempo, calcular sua inclinação usando as somas que os filhos acabaram de devolver — acumulando um total à parte.

## 🐢 Solução 1 — Força bruta (soma recalculada por nó)

Para cada nó da árvore, chamar uma função `soma()` separada para a subárvore esquerda e para a direita, calcular `|somaEsq - somaDir|`, somar ao acumulador total, e repetir recursivamente para todos os nós.

- Tempo: O(n²) no pior caso · Espaço: O(h)
- **Por que não basta:** a soma de cada subárvore é recalculada do zero múltiplas vezes conforme a recursão sobe pela árvore — o mesmo padrão de recomputação redundante já visto em [0110] Balanced Binary Tree e [0543] Diameter of Binary Tree. Numa árvore degenerada de 10^4 nós, isso vira O(n²).

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única função recursiva que **retorna a soma** da subárvore (o contrato que o pai precisa), mas que **também** acumula `|somaEsquerda - somaDireita|` num total global toda vez que processa um nó — a soma de cada subárvore é calculada exatamente uma vez e reaproveitada tanto para responder ao pai quanto para calcular a própria inclinação do nó atual.

## 🎬 Exemplo passo a passo

`root = [4,2,9,3,5,null,7]`

```
        4
       / \
      2   9
     / \    \
    3   5    7
```

| Chamada | somaEsq | somaDir | tilt deste nó | total acumulado | retorna (soma da subárvore) |
|---|---|---|---|---|---|
| soma(3) | 0 | 0 | \|0-0\|=0 | 0 | 3 |
| soma(5) | 0 | 0 | \|0-0\|=0 | 0 | 5 |
| soma(7) | 0 | 0 | \|0-0\|=0 | 0 | 7 |
| soma(2) | 3 | 5 | \|3-5\|=2 | 2 | 2+3+5=10 |
| soma(9) | 0 | 7 | \|0-7\|=7 | 9 | 9+0+7=16 |
| soma(4) | 10 | 16 | \|10-16\|=6 | **15** | 4+10+16=30 |

Resultado final: `15` ✔ (0+0+0+2+7+6 = 15, bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada nó é visitado exatamente uma vez, e sua soma é calculada uma única vez
- **Espaço:** O(h) — pilha de recursão proporcional à altura da árvore

## 💻 Implementações

### Java (referência completa e comentada)
```java
private int tiltTotal = 0; // acumulador global, atualizado como efeito colateral

public int findTilt(TreeNode root) {
    soma(root);
    return tiltTotal;
}

private int soma(TreeNode no) {
    if (no == null) return 0; // subárvore ausente: soma 0, conforme a definição do problema

    int somaEsq = soma(no.left);
    int somaDir = soma(no.right);

    // inclinação DESTE nó: usa as somas que os filhos acabaram de devolver, sem recalcular nada
    tiltTotal += Math.abs(somaEsq - somaDir);

    // contrato: devolve a soma desta subárvore (incluindo o próprio nó) para o pai usar
    return no.val + somaEsq + somaDir;
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

- Recalcular a soma da subárvore esquerda e direita em funções separadas por nó (a força bruta) — funciona, mas é a diferença entre O(n) e O(n²) que a restrição de 10^4 nós está testando.
- Esquecer de somar o `tiltTotal` de **todo** nó, e não só da raiz — o enunciado pede a soma de todas as inclinações da árvore, não só a inclinação do nó raiz.
- Confundir "soma da subárvore" (usada para calcular inclinação) com "inclinação em si" — são dois valores diferentes: a função retorna a soma (para o pai usar), mas acumula a inclinação num lugar separado.
- Não tratar valores negativos corretamente — como `Node.val` pode ser negativo, a soma de uma subárvore pode ser menor que a soma de uma subárvore com menos nós; `Math.abs` é essencial e não pode ser trocado por uma subtração simples sem o valor absoluto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Árvore vazia | `root = []` | `0` | caso base, nenhum nó para inclinar |
| Um nó só | `root = [1]` | `0` | sem filhos, `\|0-0\| = 0` |
| Árvore simples de 3 nós | `root = [1,2,3]` | `1` | cobre o exemplo 1 do enunciado |
| Árvore assimétrica com valores negativos | `root = [1,-2,3]` | testa soma com negativo | garante que `Math.abs` trata corretamente subárvores com soma negativa |

## 🔗 Conexões

- Problemas irmãos: [0543] Diameter of Binary Tree (mesmo molde de "duas perguntas numa passada pós-ordem, acumulando um total à parte"), [0104] Maximum Depth of Binary Tree (a versão mais simples do mesmo padrão de retorno pós-ordem)
- No backend: acumular um total global enquanto cada nó devolve um valor ao pai é o mesmo princípio usado em relatórios financeiros hierárquicos (cada filial soma seus números e reporta consolidado para a matriz, enquanto o sistema também rastreia desequilíbrios/outliers por nível) e em auditoria de árvores de orçamento organizacional.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
