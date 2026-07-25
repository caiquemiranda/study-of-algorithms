# 10 — Backtracking

> Explorar todas as possibilidades construindo a solução passo a passo — e desfazendo o passo quando ele leva a um beco. Problemas em [`../problemas/10_backtracking/`](../problemas/10_backtracking/).

## Conceito

Backtracking é DFS no **espaço de decisões**: em cada nível você faz uma escolha, recursa, e **desfaz** a escolha (o "back") para tentar a próxima. É a técnica para problemas de enumeração onde não há atalho polinomial: subconjuntos, permutações, combinações, tabuleiros.

**O molde universal:**
```
def backtrack(estado, escolhas):
    if solucao_completa(estado): registra(estado); return
    for escolha in escolhas_validas(estado):
        aplica(escolha)          # escolher
        backtrack(...)           # explorar
        desfaz(escolha)          # desescolher  ← o coração do padrão
```

**Poda (pruning)** é o que separa força bruta inviável de solução aceita: aborte o ramo assim que ele se torna inválido (soma estourou, rainha atacada, prefixo não existe na trie).

**As três famílias:**
- **Subsets**: cada elemento entra ou não entra (2ⁿ folhas)
- **Combinações**: subsets com tamanho/critério fixo; use índice `start` para não repetir ordem
- **Permutações**: ordem importa; use vetor `usado[]` (n! folhas)

## Como reconhecer no enunciado

- "**todas** as combinações/permutações/subconjuntos/soluções"
- "gere todas as formas válidas de..." (parênteses, partições palindrômicas)
- Tabuleiro/grade com restrições (N-Queens, Sudoku, Word Search)
- n pequeno no enunciado (n ≤ ~20) — o custo exponencial é esperado

## Templates

```python
# Subsets — decisão binária por elemento
def subsets(nums):
    res, atual = [], []
    def bt(i):
        if i == len(nums):
            res.append(atual[:])          # cópia!
            return
        atual.append(nums[i]); bt(i + 1); atual.pop()   # com nums[i]
        bt(i + 1)                                        # sem nums[i]
    bt(0)
    return res

# Combination Sum — reuso permitido, poda por soma
def combination_sum(cands, alvo):
    res, atual = [], []
    cands.sort()
    def bt(start, resto):
        if resto == 0:
            res.append(atual[:]); return
        for i in range(start, len(cands)):
            if cands[i] > resto:
                break                     # poda: ordenado, ninguém à frente serve
            atual.append(cands[i])
            bt(i, resto - cands[i])       # i (não i+1): pode reusar
            atual.pop()
    bt(0, alvo)
    return res

# Permutações com duplicatas — ordenar + pular repetido no mesmo nível
def permute_unique(nums):
    nums.sort()
    res, atual, usado = [], [], [False] * len(nums)
    def bt():
        if len(atual) == len(nums):
            res.append(atual[:]); return
        for i in range(len(nums)):
            if usado[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not usado[i-1]:
                continue                  # duplicata no mesmo nível
            usado[i] = True; atual.append(nums[i])
            bt()
            atual.pop(); usado[i] = False
    bt()
    return res
```

## Complexidade típica

Subsets O(2ⁿ·n) · permutações O(n!·n) · com poda, muito menos na prática — mas o pior caso continua exponencial. Espaço O(profundidade).

## Erros comuns

- `res.append(atual)` sem copiar (`atual[:]`) — todas as respostas viram a mesma lista mutável
- Esquecer o `pop()`/desfazer (estado vaza entre ramos)
- Duplicatas: não ordenar + não pular `nums[i] == nums[i-1]` no mesmo nível
- Em grade: não marcar/desmarcar a célula visitada
- Podar de menos (TLE) ou podar errado (perde soluções) — justifique cada poda

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 78. Subsets | 🟡 medium |
| 39. Combination Sum | 🟡 medium |
| 46. Permutations | 🟡 medium |
| 90. Subsets II | 🟡 medium |
| 40. Combination Sum II | 🟡 medium |
| 131. Palindrome Partitioning | 🟡 medium |
| 17. Letter Combinations of a Phone Number | 🟡 medium |
| 79. Word Search | 🟡 medium |
| 51. N-Queens | 🔴 hard |

## Conexão com backend

Resolvedores de dependências (Maven escolhendo versões compatíveis), planejadores de query em bancos, alocação de recursos com restrições e geradores de teste (property-based testing) usam busca com backtracking e poda. Se a memoization elimina o recálculo de subproblemas repetidos, o backtracking virou DP — ver [13](13_programacao_dinamica_1d.md).
