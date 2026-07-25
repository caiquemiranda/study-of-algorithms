# 16 — Intervals (Intervalos)

> Sobreposição, mesclagem e agendamento de `[início, fim]`. Soluções em [`../problemas/16_intervals/`](../problemas/16_intervals/).

## 1. Conceito Central e Analogia Didática

- O insight de 90% da categoria: **ordene** e varra uma vez comparando cada intervalo com o estado acumulado.
- Critério de ordenação define o problema: por **início** → mesclar; por **fim** → selecionar o máximo de compatíveis.
- Teste de sobreposição (decore): `a` e `b` sobrepõem ⇔ `a.inicio <= b.fim && b.inicio <= a.fim`.
- **Sweep line**: transforme intervalos em eventos `+1` (abre) e `−1` (fecha), ordene e acumule — o pico é a concorrência máxima.

**Analogia:** agenda de reuniões: para saber quantas **salas** precisa, não importa quem reúne com quem — importa quantas reuniões estão abertas **ao mesmo tempo**. Cada início acende uma luz, cada fim apaga; o número máximo de luzes acesas é a resposta.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "**mescle / insira** intervalos" → ordenar por início + fundir com o acumulado.
- Se pergunta "quantas **salas/recursos simultâneos**" → sweep line (ou min-heap de fins).
- Se pede "mínimo de **remoções** para não sobrepor" → guloso por FIM (ver [15_greedy](15_greedy.md)).
- Se envolve reservas, agendas, faixas de tempo/IP → é esta categoria.
- Atenção ao enunciado: `[1,2]` e `[2,3]` se tocam — **conta como sobreposição ou não?** A resposta muda o `<=` vs `<`.

## 3. Templates de Código

### Merge Intervals

```java
// Java — ordenado por início, o acumulado só cresce pelo fim
public int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, Comparator.comparingInt(a -> a[0])); // sem isso, nada funciona
    List<int[]> res = new ArrayList<>();
    int[] atual = intervals[0];
    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i][0] <= atual[1]) {                     // começa antes do acumulado terminar: funde
            atual[1] = Math.max(atual[1], intervals[i][1]);    // max protege contra intervalo CONTIDO
        } else {
            res.add(atual);                                    // buraco entre eles: fecha o acumulado
            atual = intervals[i];
        }
    }
    res.add(atual);                                            // não esqueça o último em aberto
    return res.toArray(new int[0][]);
}
```

```python
def merge(intervals):
    intervals.sort()                       # por início (tuplas/listas comparam pelo 1º elemento)
    res = [intervals[0]]
    for ini, fim in intervals[1:]:
        if ini <= res[-1][1]:              # sobrepõe/toca o acumulado
            res[-1][1] = max(res[-1][1], fim)   # max: [1,10] engole [2,3] sem encolher
        else:
            res.append([ini, fim])
    return res
```

### Meeting Rooms II (sweep line)

```java
// Java — eventos +1/-1; empate resolve o FIM antes (sala liberada pode ser reusada no mesmo instante)
public int minMeetingRooms(int[][] intervals) {
    int n = intervals.length;
    int[] inicios = new int[n], fins = new int[n];
    for (int i = 0; i < n; i++) { inicios[i] = intervals[i][0]; fins[i] = intervals[i][1]; }
    Arrays.sort(inicios);
    Arrays.sort(fins);
    int salas = 0, pico = 0, f = 0;
    for (int inicio : inicios) {
        if (inicio >= fins[f]) f++;   // alguém já terminou até este início: reusa a sala dele
        else salas = ++pico;          // ninguém liberou: precisa de sala nova (pico cresce)
    }
    return pico == 0 ? Math.min(n, 1) : pico;
}
```

```python
def min_meeting_rooms(intervals):
    eventos = []
    for ini, fim in intervals:
        eventos.append((ini, 1))       # reunião abre: +1 sala em uso
        eventos.append((fim, -1))      # reunião fecha: -1
    eventos.sort()                     # empate: (t,-1) vem antes de (t,1) => liberar antes de ocupar
    salas = pico = 0
    for _, delta in eventos:
        salas += delta
        pico = max(pico, salas)        # o pico de simultaneidade é a resposta
    return pico
```

## 4. Walkthrough Visual (Teste de Mesa)

`merge([[1,3], [2,6], [8,10], [9,12]])` (já ordenado por início)

| Intervalo | ini <= fim do acumulado? | acumulado após | res |
|---|---|---|---|
| [1,3] | — (semente) | [1,3] | `[]` |
| [2,6] | 2 <= 3 → funde | [1, max(3,6)] = [1,6] | `[]` |
| [8,10] | 8 <= 6? não → fecha | [8,10] | `[[1,6]]` |
| [9,12] | 9 <= 10 → funde | [8, max(10,12)] = [8,12] | `[[1,6]]` |
| flush | — | — | `[[1,6], [8,12]]` ✔ |

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade | Motivo |
|---|---|---|
| Merge / seleção / sweep | O(n log n) | a ordenação domina |
| Varredura em si | O(n) | uma passada |
| Espaço | O(n) | saída/eventos |

## 6. Pegadinhas e Erros Comuns

- Limites fechados vs abertos: `[1,2]` e `[2,3]` — **leia o enunciado** antes de escolher `<=` ou `<`.
- Esquecer o `max` no merge → `[1,10], [2,3]` encolhe o acumulado para fim=3 (intervalo contido é o teste que pega).
- Esquecer de adicionar o **último acumulado** após o loop (flush).
- Sweep line com desempate errado: no mesmo instante, o `-1` (fim) deve processar **antes** do `+1` se tocar não conta como sobrepor.
- Seleção máxima ordenando por **início** em vez de fim → guloso errado (ver contraexemplos no [15_greedy](15_greedy.md)).
- **Java**: ordenar `int[][]` sem `Comparator` explícito não compila/ordena por referência.
- **Python**: `eventos.sort()` com tuplas `(t, delta)` já resolve o desempate correto porque `-1 < 1` — entenda POR QUE funciona antes de confiar.

## 7. Aplicações no Mundo Real (Backend)

- **Dimensionamento de pool**: Meeting Rooms II é literalmente "quantas conexões simultâneas no pico?" — Lei de Little na prática (Vol. 2, B.2).
- **Agendamento**: conflito de reservas, janelas de manutenção, escalas de turno (seu domínio industrial).
- **PostgreSQL**: tipos `tsrange`/`daterange` com **exclusion constraints** impedem reservas sobrepostas no próprio banco.
- **Rate limiting/leases**: TTLs e janelas de validade são intervalos gerenciados com estas operações.
- Compactação de ranges em índices e merges de arquivos por faixa de chave (LSM) usam merge de intervalos.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | 🟢 Easy |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | 🟡 Medium |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟡 Medium |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | 🟡 Medium |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | 🟡 Medium |
| 1851 | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | 🔴 Hard |
