# 03 — Sliding Window

> Uma janela `[esq, dir]` que desliza sobre o array/string, reaproveitando o cálculo em vez de recomputar. Problemas em [`../problemas/03_sliding_window/`](../problemas/03_sliding_window/).

## Conceito

Para problemas de **subarray/substring contígua**, em vez de testar todas as janelas (O(n²) ou O(n³)), mantenha uma janela e um **estado incremental** (soma, mapa de frequência, contador de distintos). Ao mover `dir`, adicione o elemento ao estado; ao mover `esq`, remova. Cada elemento entra e sai no máximo uma vez → O(n).

**Duas formas:**
1. **Janela fixa** (tamanho k dado): desliza somando o que entra e subtraindo o que sai.
2. **Janela variável**: expanda `dir` sempre; **encolha `esq` enquanto a janela violar a condição** (ou, para minimização, enquanto ela ainda for válida). A janela mantém um invariante — ex.: "sem caracteres repetidos".

## Como reconhecer no enunciado

- "maior/menor **subarray/substring contígua** que satisfaz X"
- "soma/média de todas as janelas de tamanho k"
- "no máximo K elementos distintos / no máximo K trocas"
- Palavras-chave: *longest*, *shortest*, *contiguous*, *substring*, *subarray*
- ⚠️ Se pede **subsequência** (não contígua), não é sliding window — provavelmente é DP

## Templates

```python
# Janela fixa de tamanho k — maior soma
def max_soma_k(nums, k):
    soma = sum(nums[:k])
    melhor = soma
    for dir in range(k, len(nums)):
        soma += nums[dir] - nums[dir - k]   # entra um, sai um
        melhor = max(melhor, soma)
    return melhor

# Janela variável — maior substring sem repetição
def longest_unique(s):
    janela = set()
    esq = melhor = 0
    for dir in range(len(s)):
        while s[dir] in janela:             # encolhe até restaurar o invariante
            janela.remove(s[esq])
            esq += 1
        janela.add(s[dir])
        melhor = max(melhor, dir - esq + 1)
    return melhor

# Minimização — menor janela que contém todos os chars de t (esqueleto)
from collections import Counter
def min_window(s, t):
    precisa = Counter(t); faltam = len(t)
    esq = 0; melhor = (float("inf"), 0, 0)
    for dir, ch in enumerate(s):
        if precisa[ch] > 0: faltam -= 1
        precisa[ch] -= 1
        while faltam == 0:                  # janela válida: tenta encolher
            if dir - esq + 1 < melhor[0]:
                melhor = (dir - esq + 1, esq, dir)
            precisa[s[esq]] += 1
            if precisa[s[esq]] > 0: faltam += 1
            esq += 1
    return "" if melhor[0] == float("inf") else s[melhor[1]:melhor[2] + 1]
```

## Complexidade típica

O(n) tempo — `esq` e `dir` só avançam. Espaço O(k) ou O(tamanho do alfabeto) para o estado da janela.

## Erros comuns

- Recalcular o estado da janela inteira a cada passo (vira O(n·k) — perde o propósito)
- Confundir a direção do encolhimento: **maximização** → encolhe enquanto *inválida*; **minimização** → encolhe enquanto *válida*
- Esquecer de atualizar o estado ao remover `s[esq]`
- Aplicar com números negativos em problema de "soma ≥ alvo" (a monotonicidade quebra — aí é prefix sum + deque)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 121. Best Time to Buy and Sell Stock | 🟢 easy |
| 3. Longest Substring Without Repeating Characters | 🟡 medium |
| 424. Longest Repeating Character Replacement | 🟡 medium |
| 567. Permutation in String | 🟡 medium |
| 76. Minimum Window Substring | 🔴 hard |
| 239. Sliding Window Maximum (deque monotônico) | 🔴 hard |

## Conexão com backend

Rate limiting por **Sliding Window** (Fase 6.5) é literalmente este padrão aplicado a timestamps de requisições. Janelas também aparecem em stream processing (tumbling/sliding windows do Kafka Streams/Flink — Vol. 2 Módulo D.5) e em cálculo de métricas móveis (p99 na última hora).
