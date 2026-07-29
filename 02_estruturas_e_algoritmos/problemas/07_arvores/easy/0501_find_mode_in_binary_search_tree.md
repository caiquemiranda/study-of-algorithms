# [0501] Find Mode in Binary Search Tree

> 🔗 [LeetCode 501](https://leetcode.com/problems/find-mode-in-binary-search-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BST` `#DFS` `#TravessiaEmOrdem`

## 📜 O Problema

Dado o `root` de uma BST **com duplicatas permitidas**, retorne todos os valores que são **moda** (o(s) valor(es) que mais se repete(m)). Se houver mais de uma moda, retorne em qualquer ordem.

**Exemplos:**
```
Input:  root = [1,null,2,2]
Output: [2]

Input:  root = [0]
Output: [0]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^4]` → precisa de solução O(n), não O(n log n)
- `-10^5 <= Node.val <= 10^5` → valores cabem em `int`
- "BST com duplicatas": esquerda ≤ nó ≤ direita → essa regra é o que garante que **valores iguais ficam adjacentes** numa travessia em-ordem, mesmo estando em nós diferentes da árvore
- Follow-up "sem espaço extra (fora da pilha de recursão)" → descarta usar `HashMap` de contagem como solução final, mesmo sendo O(n) tempo

## 🧭 Como reconhecer o padrão

"BST + valor mais frequente" é sinal de aproveitar a propriedade da BST em vez de tratar como árvore genérica: numa travessia **em-ordem**, todos os nós com o mesmo valor aparecem **em sequência** (nunca intercalados com outro valor), porque a regra "esquerda ≤ nó ≤ direita" força isso. Isso transforma "contar frequências numa árvore" em "contar streaks (sequências) consecutivas numa lista ordenada" — o mesmo problema de [0530] Minimum Absolute Difference, só que contando repetições em vez de diferenças.

## 🐢 Solução 1 — Força bruta (HashMap de contagem)

Percorrer a árvore com qualquer travessia (nem precisa ser em-ordem), contando a frequência de cada valor num `HashMap<Integer, Integer>`. No final, achar o(s) valor(es) com a contagem máxima.

- Tempo: O(n) · Espaço: O(n) para o mapa de contagem
- **Por que não basta:** ignora completamente a propriedade de BST — funcionaria até numa árvore binária qualquer, sem ordem nenhuma. O enunciado explicitamente cobra (no follow-up) uma solução sem espaço extra, que só é possível **porque** é uma BST: sem essa garantia estrutural, não haveria como saber quais nós têm o mesmo valor sem armazenar contagens em algum lugar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça uma travessia em-ordem, mas em vez de guardar todos os valores, mantenha só o **valor anterior visitado** e uma contagem da sequência atual (`streakAtual`). Ao visitar um novo nó: se o valor é igual ao anterior, incrementa a sequência; se é diferente, reinicia a sequência em 1. Toda vez que a sequência atual **bate ou supera** o recorde de sequência máxima já visto, atualiza a lista de modas (bate = adiciona à lista; supera = zera a lista e recomeça só com esse valor).

## 🎬 Exemplo passo a passo

`root = [1,null,2,2]` (1 é raiz, filho direito 2, que tem filho esquerdo 2)

```
1
 \
  2
 /
2
```

Travessia em-ordem: `1, 2, 2`

| Passo | Valor visitado | valorAnterior | streakAtual | maxStreak | modas |
|---|---|---|---|---|---|
| 1 | 1 | — | 1 | 1 | `[1]` |
| 2 | 2 | 1 | 1 (reinicia, valor mudou) | 1 (empatou) | `[1,2]` |
| 3 | 2 | 2 | 2 (incrementa, valor igual) | **2** (superou) | `[2]` (zera e recomeça só com 2) |

Resultado final: `[2]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — travessia em-ordem visita cada nó exatamente uma vez
- **Espaço:** O(h) de pilha de recursão (o follow-up considera isso "sem espaço extra", já que é inerente a qualquer travessia recursiva) — a lista de resultado não conta como espaço extra porque é a própria saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
private Integer valorAnterior = null;
private int streakAtual = 0;
private int maxStreak = 0;
private List<Integer> modas = new ArrayList<>();

public int[] findMode(TreeNode root) {
    emOrdem(root);
    // converte List<Integer> para int[] só no final, para a assinatura de retorno pedida
    int[] resultado = new int[modas.size()];
    for (int i = 0; i < modas.size(); i++) resultado[i] = modas.get(i);
    return resultado;
}

private void emOrdem(TreeNode no) {
    if (no == null) return;

    emOrdem(no.left);

    // valores iguais ficam ADJACENTES na travessia em-ordem de uma BST — é essa garantia que usamos
    if (valorAnterior != null && no.val == valorAnterior) {
        streakAtual++;
    } else {
        streakAtual = 1;
    }

    if (streakAtual > maxStreak) {
        maxStreak = streakAtual;
        modas.clear();     // achou um recorde novo: descarta as modas antigas
        modas.add(no.val);
    } else if (streakAtual == maxStreak) {
        modas.add(no.val); // empatou o recorde: mais uma moda válida
    }

    valorAnterior = no.val;
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

- Comparar com `valorAnterior == null` usando `==` num tipo primitivo `int` — precisa ser `Integer` (boxed, nullable) para representar "ainda não visitei nenhum valor"; com `int` primitivo não existe um "vazio" seguro (usar `Integer.MIN_VALUE` como sentinela quebraria se um nó realmente valesse `-10^5` próximo desse limite).
- Esquecer de **limpar** a lista de modas (`modas.clear()`) ao encontrar um novo recorde — sem isso, a lista final mistura valores do recorde antigo com o novo.
- Usar `HashMap` (a força bruta) quando o follow-up pede explicitamente para não gastar espaço extra — passa nos testes, mas não atende ao que o problema realmente está cobrando.
- Tentar comparar `no.val` direto com o **pai** na árvore, em vez de com o valor anterior na **travessia em-ordem** — a estrutura da árvore (quem é pai de quem) não tem relação direta com "quem foi visitado por último"; são conceitos diferentes.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó só | `root = [0]` | `[0]` | caso base, streak de 1 já é o máximo |
| Duas modas empatadas | `root = [1,1,2]` (hipotético, valores repetidos em ramos diferentes) | `[1,2]` (ordem pode variar) | valida o ramo `streakAtual == maxStreak` |
| Todos os valores iguais | `root = [5,5,5]` | `[5]` | streak cresce continuamente sem nunca reiniciar |
| Todos os valores distintos | `root = [2,1,3]` | `[1,2,3]` (ordem pode variar) | cada streak é 1, todos empatam como moda |

## 🔗 Conexões

- Problemas irmãos: [0530] Minimum Absolute Difference in BST (mesma travessia em-ordem comparando com o valor anterior, mas calculando diferença mínima em vez de contagem), [0230] Kth Smallest Element in a BST (mesma técnica de em-ordem aproveitando a propriedade de BST)
- No backend: a ideia de "detectar sequências consecutivas iguais numa passada só, sem estrutura auxiliar" é a mesma técnica usada em compressão run-length (RLE) e em análise de logs ordenados por timestamp para detectar rajadas (bursts) do mesmo evento sem precisar de contagem em memória separada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
