# [0100] Same Tree

> 🔗 [LeetCode 100](https://leetcode.com/problems/same-tree/) · Dificuldade: 🟢 easy · Categoria: [`07_arvores`](../../../fundamentos/07_arvores.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArvoreBinaria` `#DFS` `#Easy`

## 📜 O Problema

Dadas as raízes `p` e `q` de duas árvores binárias, verifique se elas são **iguais**: mesma estrutura (mesmo formato de nós e nulos nas mesmas posições) e mesmo valor em cada nó correspondente.

**Exemplos:**
```
Input:  p = [1,2,3], q = [1,2,3]
Output: true

Input:  p = [1,2], q = [1,null,2]
Output: false

Input:  p = [1,2,1], q = [1,1,2]
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em ambas as árvores em `[0, 100]` → entrada pequena, qualquer solução O(n) serve
- `-10^4 <= Node.val <= 10^4` → valores cabem em `int` sem overflow
- O segundo exemplo (`[1,2]` vs `[1,null,2]`) é a pista mais importante: **estrutura importa tanto quanto valor** — um `2` no filho esquerdo não é o mesmo que um `2` no filho direito

## 🧭 Como reconhecer o padrão

"Duas árvores são iguais/idênticas?" é comparação estrutural par a par: para cada posição, os dois nós têm que existir (ou os dois serem nulos) e ter o mesmo valor. É a base de outros problemas de árvore ("é subárvore?", "é simétrica?") que reaproveitam essa mesma checagem internamente.

## 🐢 Solução 1 — Força bruta (serializar e comparar strings)

Serializar cada árvore em uma string via pré-ordem (ex.: `"1,2,3"`) e comparar as duas strings.

- Tempo: O(n) · Espaço: O(n) para as duas strings
- **Por que não basta:** sem um marcador explícito para "filho ausente", a serialização fica ambígua. `p = [1,2]` (2 é filho esquerdo) serializaria como `"1,2"`, e `q = [1,null,2]` (2 é filho direito) **também** serializaria como `"1,2"` se você só concatenar valores sem marcar os nulos — o algoritmo diria "iguais" quando o gabarito é `false`. Corrigir isso exige inserir marcadores de nulo em toda posição ausente, o que já é tanto trabalho quanto comparar as árvores diretamente, sem ganhar nada em troca.

## 💡 Solução 2 — A ideia otimizada (intuição)

Compare os dois nós recursivamente, sem serializar nada: se os dois são `null`, são iguais (caso base); se só um é `null`, são diferentes; se os valores diferem, são diferentes; senão, a resposta é "os dois lados esquerdos são iguais **e** os dois lados direitos são iguais" — a recursão já lida com a ambiguidade estrutural porque compara os nós na mesma posição da árvore, não uma sequência linear de valores.

## 🎬 Exemplo passo a passo

`p = [1,2,3]`, `q = [1,2,3]`

| Passo | Chamada | p.val vs q.val | Ação | Resultado parcial |
|---|---|---|---|---|
| 1 | isSameTree(1, 1) | 1 == 1 | compara filhos esquerdos e direitos | aguardando |
| 2 | isSameTree(2, 2) | 2 == 2 | ambos sem filhos → `true` | esquerda ✔ |
| 3 | isSameTree(3, 3) | 3 == 3 | ambos sem filhos → `true` | direita ✔ |
| 4 | volta ao passo 1 | — | esquerda ✔ **e** direita ✔ → `true` | `true` |

Resultado final: `true` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(min(n, m)) — a recursão para assim que encontra a primeira diferença; no pior caso (árvores iguais ou só diferentes na última folha), percorre todos os nós de uma delas
- **Espaço:** O(min(h_p, h_q)) — pilha de recursão limitada pela altura da árvore mais rasa entre as duas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isSameTree(TreeNode p, TreeNode q) {
    // ambos nulos na mesma posição: estrutura bate aqui, não há mais nada a comparar
    if (p == null && q == null) return true;

    // só um dos dois é nulo: estrutura diverge (um tem nó, o outro não)
    if (p == null || q == null) return false;

    // valores diferentes no mesmo nó: não são iguais, nem adianta olhar os filhos
    if (p.val != q.val) return false;

    // só são iguais se AMBOS os lados (esquerdo e direito) forem iguais
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
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

- Serializar sem marcador de nulo (o erro da força bruta acima) — produz falsos positivos quando a mesma sequência de valores corresponde a formatos diferentes de árvore.
- Esquecer o caso `p == null && q == null` antes do `p == null || q == null` — na ordem errada, `null == null` cairia incorretamente no ramo de "diferentes".
- Comparar só os valores em uma travessia (ex.: duas listas em-ordem) sem checar estrutura — duas árvores diferentes podem ter a mesma sequência em-ordem (ex.: rotações de BST).
- Usar `==` para comparar `Integer` boxed em vez de `.equals()` ou `int` primitivo — fora da faixa de cache do Java (-128 a 127), `==` entre `Integer` compara referência, não valor, e pode dar falso negativo silencioso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Duas árvores vazias | `p = [], q = []` | `true` | ambos `null` já no primeiro caso base |
| Uma vazia, outra não | `p = [], q = [1]` | `false` | cobre o ramo "só um é null" |
| Mesma estrutura, valor diferente | `p = [1,2], q = [1,3]` | `false` | testa a comparação de `val` |
| Mesmos valores, estrutura diferente | `p = [1,2], q = [1,null,2]` | `false` | o caso clássico que a serialização ingênua erra |

## 🔗 Conexões

- Problemas irmãos: [0101] Symmetric Tree (compara uma árvore com o espelho dela mesma, reaproveitando essa mesma lógica de "comparar dois nós"), [0572] Subtree of Another Tree (chama `isSameTree` repetidamente para cada nó de uma árvore maior)
- No backend: comparação estrutural de árvores aparece em diffs de AST (compiladores, linters) para detectar se duas expressões de código são semanticamente idênticas, e em comparação de documentos JSON/XML aninhados campo a campo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
