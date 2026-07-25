# 10 — Backtracking

> Construir a solução passo a passo e desfazer o passo que leva a beco sem saída. Soluções em [`../problemas/10_backtracking/`](../problemas/10_backtracking/).

## 1. Conceito Central e Analogia Didática

- É DFS no **espaço de decisões**: em cada nível, faça uma escolha → recurse → **desfaça** (o "back") → tente a próxima.
- O molde universal tem 3 verbos: **escolher, explorar, desescolher** — o `pop()`/desmarcar é o coração do padrão.
- **Poda (pruning)** separa força bruta inviável de solução aceita: aborte o ramo assim que ele se tornar inválido.

**Analogia:** labirinto com giz: em cada bifurcação você marca o corredor escolhido; deu em parede, **volta apagando a marca** e tenta o próximo corredor. O giz apagado é o estado desfeito — sem ele, os caminhos se contaminam.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "**TODAS** as combinações/permutações/subconjuntos/soluções" → backtracking.
- Se pede "gere todas as formas **válidas** de..." (parênteses, partições) → backtracking com poda de validade.
- Se é tabuleiro/grade com restrições (N-Queens, Sudoku, Word Search) → backtracking com marcação de visitados.
- Se `n ≤ ~20` nas constraints → o custo exponencial é esperado; pode enumerar.
- Ordem importa? **Permutação** (vetor `usado[]`). Ordem não importa? **Combinação** (índice `start`).

## 3. Templates de Código

### Subsets (decisão binária por elemento)

```java
// Java — cada elemento tem 2 destinos: entra ou não entra; 2^n folhas
public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();
    backtrack(nums, 0, new ArrayList<>(), res);
    return res;
}

private void backtrack(int[] nums, int i, List<Integer> atual, List<List<Integer>> res) {
    if (i == nums.length) {
        res.add(new ArrayList<>(atual));   // CÓPIA: 'atual' será mutada pelos próximos ramos
        return;
    }
    atual.add(nums[i]);                    // ramo 1: escolhe nums[i]
    backtrack(nums, i + 1, atual, res);
    atual.remove(atual.size() - 1);        // DESFAZ: sem isso o ramo 2 herda a escolha do ramo 1
    backtrack(nums, i + 1, atual, res);    // ramo 2: não escolhe nums[i]
}
```

```python
def subsets(nums):
    res, atual = [], []
    def bt(i):
        if i == len(nums):
            res.append(atual[:])       # atual[:] copia — guardar 'atual' direto quebraria tudo
            return
        atual.append(nums[i])          # escolher
        bt(i + 1)                      # explorar
        atual.pop()                    # desescolher (o "back" do backtracking)
        bt(i + 1)                      # ramo sem nums[i]
    bt(0)
    return res
```

### Combination Sum (reuso permitido + poda por ordenação)

```python
def combination_sum(cands, alvo):
    cands.sort()                               # ordenar habilita a poda por break
    res, atual = [], []
    def bt(start, resto):
        if resto == 0:
            res.append(atual[:])
            return
        for i in range(start, len(cands)):
            if cands[i] > resto:
                break                          # poda: ordenado, todos à frente também estouram
            atual.append(cands[i])
            bt(i, resto - cands[i])            # 'i' (não i+1): o MESMO número pode repetir
            atual.pop()
    bt(0, alvo)
    return res
```

### Permutações com duplicatas

```java
// Java — ordenar + pular repetido no MESMO nível elimina permutações idênticas
public List<List<Integer>> permuteUnique(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> res = new ArrayList<>();
    backtrack(nums, new boolean[nums.length], new ArrayList<>(), res);
    return res;
}

private void backtrack(int[] nums, boolean[] usado, List<Integer> atual, List<List<Integer>> res) {
    if (atual.size() == nums.length) {
        res.add(new ArrayList<>(atual));
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        if (usado[i]) continue;
        // duplicata no mesmo nível: só permite a 1ª cópia livre (a anterior precisa estar em uso)
        if (i > 0 && nums[i] == nums[i - 1] && !usado[i - 1]) continue;
        usado[i] = true;  atual.add(nums[i]);
        backtrack(nums, usado, atual, res);
        atual.remove(atual.size() - 1);  usado[i] = false;   // desfaz o par de marcações
    }
}
```

## 4. Walkthrough Visual (Teste de Mesa)

`subsets([1, 2])` — árvore de decisões:

| Passo | i | decisão | atual | ação |
|---|---|---|---|---|
| 1 | 0 | escolhe 1 | `[1]` | desce |
| 2 | 1 | escolhe 2 | `[1,2]` | i==2 → grava `[1,2]` |
| 3 | 1 | pop 2, não escolhe | `[1]` | i==2 → grava `[1]` |
| 4 | 0 | pop 1, não escolhe | `[]` | desce |
| 5 | 1 | escolhe 2 | `[2]` | grava `[2]` |
| 6 | 1 | pop 2, não escolhe | `[]` | grava `[]` |

- Resultado: `[[1,2], [1], [2], []]` — 2² = 4 subconjuntos ✔ — repare no `pop` antes de cada ramo alternativo.

## 5. Complexidade (Tempo e Espaço)

| Família | Tempo | Motivo |
|---|---|---|
| Subsets | O(2ⁿ · n) | 2ⁿ folhas × custo de copiar |
| Permutações | O(n! · n) | n! ordens possíveis |
| Combinações | O(C(n,k) · k) | escolhas sem ordem |
| Espaço | O(profundidade) | pilha + caminho atual |

- Poda reduz o caso médio drasticamente, mas o **pior caso continua exponencial** — é a natureza do problema, não defeito seu.

## 6. Pegadinhas e Erros Comuns

- `res.add(atual)` **sem copiar** → todas as respostas apontam para a mesma lista mutável (Java e Python).
- Esquecer o `pop()`/`usado[i] = false` → estado vaza entre ramos e as respostas saem contaminadas.
- Duplicatas: não ordenar + não pular `nums[i] == nums[i-1]` no mesmo nível → respostas repetidas.
- Word Search: esquecer de **desmarcar** a célula da grade ao retornar.
- **Java**: `atual.remove(valor)` faz autoboxing e remove por OBJETO — use `remove(atual.size() - 1)` por índice.
- **Python**: passar `atual` como default mutável de parâmetro (`def bt(atual=[])`) — o default é compartilhado entre chamadas.
- Podar de menos → TLE; podar "de mais" sem justificar → perde soluções. Toda poda precisa de argumento.

## 7. Aplicações no Mundo Real (Backend)

- **Resolvedores de dependência**: Maven/pip escolhendo versões compatíveis exploram e retrocedem exatamente assim.
- **Planejador de queries (PostgreSQL)**: enumeração de ordens de join com poda por custo estimado.
- **Alocação com restrições**: escala de turnos, agendamento de recursos, configuração válida de infraestrutura.
- **Property-based testing**: geração e encolhimento (shrinking) de casos de teste percorre espaço de estados com retrocesso.
- Se subproblemas se repetem, memoize e vira **DP** — ver [13_programacao_dinamica_1d](13_programacao_dinamica_1d.md).

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | 🟡 Medium |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟡 Medium |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | 🟡 Medium |
| 90 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | 🟡 Medium |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | 🟡 Medium |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | 🟡 Medium |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens/) | 🔴 Hard |
