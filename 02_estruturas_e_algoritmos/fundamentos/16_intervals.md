# 16 — Intervals (Intervalos)

> Sobreposição, mesclagem e agendamento de intervalos `[início, fim]`. Problemas em [`../problemas/16_intervals/`](../problemas/16_intervals/).

## Conceito

O insight que resolve 90% da categoria: **ordene** (por início para mesclar; por fim para selecionar o máximo de intervalos compatíveis) e varra uma vez comparando cada intervalo com o "estado atual".

**As operações fundamentais:**
- **Sobreposição**: `a` e `b` sobrepõem ⇔ `a.inicio <= b.fim and b.inicio <= a.fim` (decore; errar esse teste custa o problema inteiro)
- **Merge**: ordenar por início; se o atual começa antes do fim do acumulado, funda (`fim = max(fins)`); senão, fecha e recomeça
- **Seleção máxima de não sobrepostos** (= mínimo de remoções): ordenar por **fim** e escolher gulosamente o que termina primeiro
- **Contagem de sobreposições simultâneas** (Meeting Rooms II): eventos de +1/−1 ordenados (sweep line) ou min-heap de fins

## Como reconhecer no enunciado

- "mescle / insira intervalo"
- "quantas salas/recursos simultâneos são necessários" → sweep line ou heap
- "número mínimo de remoções para não sobrepor" → guloso por fim
- Reservas, agendas, alocação de faixas de tempo/IPs

## Templates

```python
# Merge Intervals — O(n log n)
def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    for ini, fim in intervals[1:]:
        if ini <= res[-1][1]:                 # sobrepõe o acumulado
            res[-1][1] = max(res[-1][1], fim)
        else:
            res.append([ini, fim])
    return res

# Non-overlapping Intervals — guloso por FIM, O(n log n)
def erase_overlap(intervals):
    intervals.sort(key=lambda x: x[1])
    removidos, fim_atual = 0, float("-inf")
    for ini, fim in intervals:
        if ini >= fim_atual:
            fim_atual = fim                   # compatível: mantém
        else:
            removidos += 1                    # sobrepõe: remove este
    return removidos

# Meeting Rooms II — sweep line, O(n log n)
def min_meeting_rooms(intervals):
    eventos = []
    for ini, fim in intervals:
        eventos.append((ini, 1))              # reunião começa
        eventos.append((fim, -1))             # reunião termina
    eventos.sort()                            # empate: -1 antes de +1 ✓
    salas = pico = 0
    for _, delta in eventos:
        salas += delta
        pico = max(pico, salas)
    return pico
```

## Complexidade típica

O(n log n) pela ordenação; a varredura é O(n).

## Erros comuns

- Teste de sobreposição errado nos limites (fechado vs aberto: `[1,2]` e `[2,3]` sobrepõem? depende do enunciado — **leia**)
- Ordenar por início quando o problema pede seleção máxima (o guloso correto é por **fim**)
- No sweep line, desempate errado entre fim e início no mesmo ponto (fim deve processar antes se tocar não conta como sobrepor)
- Esquecer `max` no merge (intervalo contido: `[1,10], [2,3]`)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 57. Insert Interval | 🟡 medium |
| 56. Merge Intervals | 🟡 medium |
| 435. Non-overlapping Intervals | 🟡 medium |
| 252 / 253. Meeting Rooms I e II | 🟢/🟡 |
| 1851. Minimum Interval to Include Each Query | 🔴 hard |

## Conexão com backend

Intervalos são onipresentes: janelas de manutenção, reservas de recursos, leases de DHCP, TTLs, compactação de ranges em índices, detecção de conflito de agendamento (o Meeting Rooms II é literalmente o dimensionamento de pool de conexões: quantas conexões simultâneas no pico? — Lei de Little, Vol. 2 Módulo B.2).
