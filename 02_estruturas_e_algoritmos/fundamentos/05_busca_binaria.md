# 05 — Busca Binária

> Descartar metade do espaço de busca a cada passo: O(log n). Problemas em [`../problemas/05_busca_binaria/`](../problemas/05_busca_binaria/).

## Conceito

Requisito único: o espaço de busca precisa ser **monotônico** — existe um ponto de virada onde a resposta muda de "não" para "sim" (ou o array está ordenado). A busca binária encontra esse ponto em O(log n).

**As formas que caem:**
1. **Busca clássica** em array ordenado
2. **Lower / Upper bound**: primeira posição ≥ x / primeira posição > x (a forma mais útil e menos propensa a bug)
3. **Array rotacionado**: uma das metades sempre está ordenada — descubra qual e decida onde continuar
4. ⭐ **Busca binária na resposta**: quando a pergunta é "qual o menor/maior valor X tal que consigo(X)?" e `consigo()` é monotônica — você não busca num array, busca no **espaço de respostas** (velocidade mínima, capacidade mínima, tempo mínimo)

## Como reconhecer no enunciado

- Array ordenado (ou "quase ordenado" / rotacionado)
- "O(log n)" explícito no enunciado
- **"minimize o máximo" / "maximize o mínimo"** → busca binária na resposta
- "menor valor que satisfaz uma condição verificável" onde verificar custa O(n)

## Templates

```python
# Lower bound — primeira posição com nums[i] >= alvo (template universal)
def lower_bound(nums, alvo):
    esq, dir = 0, len(nums)          # dir é EXCLUSIVO
    while esq < dir:
        meio = (esq + dir) // 2
        if nums[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio
    return esq                        # posição de inserção; cheque limites ao usar

# Mínimo em array rotacionado — O(log n)
def find_min(nums):
    esq, dir = 0, len(nums) - 1
    while esq < dir:
        meio = (esq + dir) // 2
        if nums[meio] > nums[dir]:    # mínimo está à direita do meio
            esq = meio + 1
        else:
            dir = meio
    return nums[esq]

# Busca binária NA RESPOSTA — Koko Eating Bananas
import math
def min_eating_speed(piles, h):
    def consegue(vel):                # monotônica: se consegue com v, consegue com v+1
        return sum(math.ceil(p / vel) for p in piles) <= h
    esq, dir = 1, max(piles)
    while esq < dir:
        meio = (esq + dir) // 2
        if consegue(meio):
            dir = meio                # tenta menor
        else:
            esq = meio + 1
    return esq
```

## Complexidade típica

O(log n); na resposta: O(n · log(intervalo de respostas)).

## Erros comuns

- **Loop infinito**: com `esq = meio` sem `+1` e divisão truncando para baixo. Regra: no template `esq < dir` exclusivo, sempre `esq = meio + 1` ou `dir = meio`
- Misturar convenções (dir inclusivo vs exclusivo) no meio do código — escolha UMA e padronize todos os seus templates
- Em Java/C++: overflow em `(esq + dir) / 2` — use `esq + (dir - esq) / 2`
- Na busca na resposta: função `consegue()` não monotônica (o padrão não se aplica)
- Devolver `meio` quando a pergunta pedia lower bound (primeira ocorrência, não qualquer uma)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 704. Binary Search | 🟢 easy |
| 74. Search a 2D Matrix | 🟡 medium |
| 875. Koko Eating Bananas | 🟡 medium |
| 153. Find Minimum in Rotated Sorted Array | 🟡 medium |
| 33. Search in Rotated Sorted Array | 🟡 medium |
| 981. Time Based Key-Value Store | 🟡 medium |
| 4. Median of Two Sorted Arrays | 🔴 hard |

## Conexão com backend

Índices B-Tree fazem busca binária dentro de cada página (Fase 5.3). O Time-Based KV Store (LC 981) é literalmente o modelo de leitura de um banco versionado por timestamp (MVCC, Fase 5.4). Busca binária na resposta = capacity planning ("qual o menor número de servidores que aguenta a carga?").
