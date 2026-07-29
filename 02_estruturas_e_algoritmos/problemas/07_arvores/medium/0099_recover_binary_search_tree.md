# [0099] Recover Binary Search Tree

> 🔗 [LeetCode 99](https://leetcode.com/problems/recover-binary-search-tree/) · Dificuldade: 🟡 medium · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#TravessiaEmOrdem`

## 📜 O Problema

Dado o `root` de uma BST onde os valores de **exatamente dois** nós foram trocados por engano, recupere a árvore **sem mudar sua estrutura** (só corrigindo os valores).

**Exemplos:**
```
Input:  root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explicação: 3 não pode ser filho esquerdo de 1 (3 > 1); trocando 1 e 3 a BST fica válida

Input:  root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explicação: 2 não pode estar na subárvore direita de 3 (2 < 3); trocando 2 e 3 a BST fica válida
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[2, 1000]` → precisa de solução O(n); sempre há pelo menos 2 nós, então a troca sempre é possível
- `-2^31 <= Node.val <= 2^31 - 1` → mesmo cuidado de [0098] com sentinelas de limite, mas aqui não é necessário nenhum sentinela — a técnica usa comparação com o valor **anterior**, não limites de min/max
- Follow-up "O(1) espaço" → existe uma técnica avançada (Morris Traversal, que usa ponteiros temporários dentro da própria árvore em vez de pilha de recursão) para isso; a solução de referência aqui usa recursão O(h), que já é a resposta esperada na maioria dos contextos de estudo — o Morris fica como próximo passo avançado

## 🧭 Como reconhecer o padrão

"BST com exatamente 2 valores trocados" é uma variação de [0098] Validate Binary Search Tree: em vez de só detectar **que** a árvore é inválida, é preciso detectar **quais** dois nós especificamente causam a violação. A mesma travessia em-ordem (que deveria produzir uma sequência estritamente crescente) revela isso: cada "queda" na sequência (`anterior > atual`) aponta para um dos dois nós errados.

## 🐢 Solução 1 — Força bruta (coletar tudo, ordenar, reescrever)

Fazer uma travessia em-ordem coletando todos os valores numa lista. Ordenar essa lista. Fazer uma **segunda** travessia em-ordem, agora escrevendo de volta nos nós, na ordem visitada, os valores da lista já ordenada.

- Tempo: O(n log n) por causa do sort · Espaço: O(n) para a lista
- **Por que não basta:** paga por um sort completo (e duas travessias) quando só **dois** valores específicos estão fora de lugar — o resto da árvore já está correto. Ordenar a lista inteira para depois reescrever tudo é um exagero para um problema que é, na essência, "ache duas trocas e desfaça".

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça uma travessia em-ordem comparando cada valor com o **anterior** (sem lista, sem sort). Numa BST válida, a sequência é sempre crescente; com dois valores trocados, ocorrem uma ou duas "quedas" (`anterior > atual`):
- Se os dois nós trocados são **vizinhos** na sequência em-ordem, ocorre **uma única queda**, e os dois nós errados são exatamente esse par (anterior, atual).
- Se **não** são vizinhos, ocorrem **duas quedas**: na primeira, o nó errado é o `anterior` daquele momento; na segunda, o nó errado é o `atual` daquele momento (o `second` é atualizado a cada queda, mas o `first` só é fixado na primeira).

Depois de identificar os dois nós, basta **trocar os valores** deles (não a estrutura).

## 🎬 Exemplo passo a passo

`root = [3,1,4,null,null,2]` (raiz 3, filho esquerdo 1, filho direito 4 com filho esquerdo 2) — os nós `2` e `3` foram trocados por engano (a árvore correta seria `[2,1,4,null,null,3]`)

```
      3
     / \
    1   4
       /
      2
```

Travessia em-ordem (esquerda, nó, direita): `1, 3, 2, 4` (deveria ser `1, 2, 3, 4`)

| Passo | Valor visitado | anterior | Queda? (anterior > atual) | first | second |
|---|---|---|---|---|---|
| 1 | 1 | — | não (primeiro valor) | — | — |
| 2 | 3 | 1 | não (1 < 3) | — | — |
| 3 | 2 | 3 | **sim** (3 > 2) | nó de valor `3` (o anterior) | nó de valor `2` (o atual) |
| 4 | 4 | 2 | não (2 < 4) | nó de valor `3` | nó de valor `2` |

Só uma queda ocorreu (os dois nós errados são vizinhos na sequência em-ordem) → troca os valores dos nós `3` e `2` identificados. A raiz (que valia 3) passa a valer 2, e o nó que valia 2 passa a valer 3 — a travessia em-ordem volta a ser `1, 2, 3, 4`.

Resultado final: `[2,1,4,null,null,3]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única travessia em-ordem, sem sort
- **Espaço:** O(h) de pilha de recursão (O(1) seria possível com Morris Traversal, fora do escopo desta referência)

## 💻 Implementações

### Java (referência completa e comentada)
```java
private TreeNode primeiro = null;   // primeiro nó errado (fixado só na PRIMEIRA queda)
private TreeNode segundo = null;    // segundo nó errado (atualizado a cada queda encontrada)
private TreeNode anterior = null;   // último nó visitado na travessia em-ordem

public void recoverTree(TreeNode root) {
    emOrdem(root);
    // troca só os VALORES dos dois nós identificados — a estrutura da árvore não muda
    int temp = primeiro.val;
    primeiro.val = segundo.val;
    segundo.val = temp;
}

private void emOrdem(TreeNode no) {
    if (no == null) return;

    emOrdem(no.left);

    // queda: valor atual é menor que o anterior — não deveria acontecer numa BST válida
    if (anterior != null && anterior.val > no.val) {
        if (primeiro == null) primeiro = anterior; // só fixa na PRIMEIRA queda encontrada
        segundo = no; // sempre atualiza: se houver uma segunda queda, ela corrige para o nó certo
    }
    anterior = no;

    emOrdem(no.right);
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

- Atualizar `primeiro` em **toda** queda, não só na primeira — quando os dois nós trocados não são vizinhos na travessia (duas quedas), o `primeiro` correto é sempre o `anterior` da **primeira** queda; sobrescrevê-lo na segunda queda perde a referência certa.
- Esquecer de atualizar `segundo` em cada queda (não só na primeira) — no caso de duas quedas, o nó errado da **segunda** queda é o `atual` daquele momento, que só é capturado corretamente se `segundo` for reatribuído a cada ocorrência.
- Trocar a **estrutura** da árvore (mover nós, religar ponteiros) em vez de só trocar os `.val` dos dois nós — o enunciado exige explicitamente preservar a estrutura original.
- Coletar tudo numa lista e ordenar (a força bruta) — funciona, mas ignora que só 2 valores específicos precisam ser corrigidos, pagando um custo de sort desnecessário.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Dois nós (mínimo possível) | `root = [1,2]` (2 é filho esquerdo de 1, invertido) | `[2,1]` | caso mínimo garantido pela restrição `[2, 1000]` |
| Nós trocados são vizinhos na travessia | `root = [1,3,null,null,2]` | `[3,1,null,null,2]` | cobre o exemplo 1, testa o caso de **uma única queda** |
| Nós trocados não são vizinhos | `root = [3,1,4,null,null,2]` | `[2,1,4,null,null,3]` | cobre o exemplo 2, testa o caso de **duas quedas** |
| Troca envolvendo a raiz | `root = [2,3,1]` (hipotético, raiz e um filho trocados) | árvore corrigida | garante que a lógica funciona mesmo quando um dos nós errados é a própria raiz |

## 🔗 Conexões

- Problemas irmãos: [0098] Validate Binary Search Tree (a mesma travessia em-ordem, mas só detectando **que** há violação, sem corrigir), [0530] Minimum Absolute Difference in BST (mesma técnica de comparar com o valor anterior durante a em-ordem)
- No backend: detectar e corrigir exatamente os registros "fora de ordem" numa sequência que deveria ser monotônica (sem reordenar tudo) aparece em correção de dados corrompidos em índices ordenados e em auditoria de logs com timestamps quase sempre crescentes, onde só alguns poucos registros fora de ordem precisam ser identificados e realinhados.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
