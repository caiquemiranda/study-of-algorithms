# 05 — Busca Binária

> Descarta metade do espaço de busca por passo: O(log n). Soluções em [`../problemas/05_busca_binaria/`](../problemas/05_busca_binaria/).

## 1. Conceito Central e Analogia Didática

- Exige espaço de busca **monotônico**: existe um ponto de virada único onde a resposta muda de "não" para "sim" (array ordenado é o caso óbvio).
- Cada comparação com o meio **elimina metade** dos candidatos — 1 bilhão de itens cai em ~30 passos.
- Formas que caem: busca clássica, **lower/upper bound**, array **rotacionado**, e ⭐ **busca binária na resposta** (buscar no espaço de soluções, não num array).

**Analogia:** adivinhar um número de 1 a 100 com respostas "maior/menor": ninguém chuta 1, 2, 3... — você chuta 50 e joga fora metade. O dicionário físico é igual: abre no meio, decide o lado, repete.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se o array está **ordenado** (ou rotacionado) e pede busca → binária.
- Se o enunciado exige **O(log n)** explicitamente → binária, sem discussão.
- Se pede "**minimize o máximo**" ou "**maximize o mínimo**" → busca binária **na resposta**.
- Se pergunta "menor valor X tal que `consigo(X)` é verdadeiro" e `consigo()` é monotônica (velocidade, capacidade, dias) → binária na resposta.
- Se pede "primeira/última ocorrência" → lower/upper bound, não busca comum.

## 3. Templates de Código

### Lower bound (primeira posição com `nums[i] >= alvo`)

```java
// Java — convenção [esq, dir): dir EXCLUSIVO evita loop infinito por construção
public int lowerBound(int[] nums, int alvo) {
    int esq = 0, dir = nums.length;              // dir fora do array: pode retornar n (inserir no fim)
    while (esq < dir) {
        int meio = esq + (dir - esq) / 2;        // forma anti-overflow de (esq+dir)/2
        if (nums[meio] < alvo) {
            esq = meio + 1;                      // meio é pequeno demais: descarta ele e tudo à esquerda
        } else {
            dir = meio;                          // meio serve: mantém como candidato, descarta o resto à direita
        }
    }
    return esq;                                  // esq == dir: fronteira exata do "primeiro >= alvo"
}
```

```python
def lower_bound(nums, alvo):
    esq, dir = 0, len(nums)          # dir exclusivo
    while esq < dir:
        meio = (esq + dir) // 2      # Python não estoura int; em Java use a forma anti-overflow
        if nums[meio] < alvo:
            esq = meio + 1           # descarta meio: ele não satisfaz
        else:
            dir = meio               # meio ainda pode ser a resposta: não pule ele
    return esq
```

### Busca binária NA RESPOSTA (Koko Eating Bananas)

```java
// Java — buscamos a MENOR velocidade viável; viável(v) é monotônica: se v serve, v+1 serve
public int minEatingSpeed(int[] piles, int h) {
    int esq = 1, dir = Arrays.stream(piles).max().getAsInt();
    while (esq < dir) {
        int meio = esq + (dir - esq) / 2;
        if (viavel(piles, meio, h)) dir = meio;   // serve: tenta velocidade menor (mantém meio)
        else esq = meio + 1;                      // não serve: precisa comer mais rápido
    }
    return esq;
}

private boolean viavel(int[] piles, int vel, int h) {
    long horas = 0;
    for (int p : piles) horas += (p + vel - 1L) / vel; // teto da divisão sem Math.ceil em double
    return horas <= h;
}
```

```python
import math

def min_eating_speed(piles, h):
    def viavel(vel):                              # função monotônica: o coração do padrão
        return sum(math.ceil(p / vel) for p in piles) <= h
    esq, dir = 1, max(piles)
    while esq < dir:
        meio = (esq + dir) // 2
        if viavel(meio):
            dir = meio                            # serve: aperta para baixo
        else:
            esq = meio + 1
    return esq
```

## 4. Walkthrough Visual (Teste de Mesa)

`lowerBound(nums=[1, 3, 3, 5, 8], alvo=3)`

| Iteração | esq | dir | meio | nums[meio] | Decisão |
|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 3 | `3 >= 3` → `dir = 2` |
| 2 | 0 | 2 | 1 | 3 | `3 >= 3` → `dir = 1` |
| 3 | 0 | 1 | 0 | 1 | `1 < 3` → `esq = 1` |
| fim | 1 | 1 | — | — | retorna **1** (primeira ocorrência de 3) ✔ |

## 5. Complexidade (Tempo e Espaço)

| Forma | Tempo | Espaço |
|---|---|---|
| Busca em array | O(log n) | O(1) |
| Na resposta | O(n · log(intervalo)) | O(1) |

- Log porque o espaço de busca **divide por 2 a cada passo**; o `viavel()` de O(n) roda uma vez por passo.

## 6. Pegadinhas e Erros Comuns

- **Loop infinito**: `esq = meio` (sem `+1`) com divisão truncando para baixo. No template `[esq, dir)`: sempre `esq = meio + 1` ou `dir = meio`.
- **Java/C++**: `(esq + dir) / 2` estoura int com índices grandes → `esq + (dir - esq) / 2`.
- Misturar convenções (dir inclusivo vs exclusivo) no mesmo código — padronize UM template para a vida.
- Retornar `meio` na primeira igualdade quando o problema pede **primeira ocorrência** → lower bound.
- Na busca na resposta: aplicar sem verificar que `viavel()` é **monotônica** — sem isso o descarte é inválido.
- **Java**: `Math.ceil(a / b)` com ints faz divisão inteira ANTES do ceil — use `(a + b - 1) / b`.
- **Python**: `//` arredonda para baixo até com negativos (`-3 // 2 == -2`) — cuidado em variantes com índices negativos.

## 7. Aplicações no Mundo Real (Backend)

- **PostgreSQL**: dentro de cada página do índice **B-Tree**, a busca pela chave é binária.
- **Kafka**: consumidor localiza offset por timestamp via busca binária no índice do segmento de log.
- **Git**: `git bisect` é busca binária na história de commits para achar a regressão.
- **Capacity planning**: "menor número de instâncias que sustenta a carga" = busca binária na resposta com teste de carga como `viavel()`.
- JVM/GC: busca de faixas em tabelas ordenadas (card tables, free lists) usa a mesma ideia.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟢 Easy |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | 🟡 Medium |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 🟡 Medium |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟡 Medium |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟡 Medium |
| 981 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | 🟡 Medium |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard |
