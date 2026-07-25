# 15 — Greedy (Algoritmos Gulosos)

> A melhor escolha local, quando comprovadamente leva ao ótimo global. Soluções em [`../problemas/15_greedy/`](../problemas/15_greedy/).

## 1. Conceito Central e Analogia Didática

- O guloso decide **sem olhar o futuro** e nunca volta atrás — por isso é O(n) ou O(n log n).
- Só funciona com duas propriedades: **escolha gulosa** (o ótimo local estende-se ao global) + **subestrutura ótima** (o que sobra é o mesmo problema, menor).
- Validação obrigatória: **argumento de troca** ("trocar a escolha ótima pela gulosa nunca piora") OU um contraexemplo — sem prova, greedy é aposta.

**Analogia:** caixa dando troco com moedas de 100/50/25/10/5/1: pegar sempre a maior moeda possível funciona **neste** sistema de moedas. Mas com moedas {1, 3, 4} para dar 6, o guloso dá 4+1+1 (3 moedas) e o ótimo é 3+3 (2) — o mesmo instinto, em outro sistema, falha. Greedy é isso: certo no sistema certo, armadilha no errado.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "número **mínimo** de saltos/intervalos/remoções" em estrutura sequencial → candidato a greedy.
- Se é **agendamento/seleção de atividades** → ordenar pelo critério certo (geralmente pelo FIM) e varrer.
- Se n é grande demais para DP (10⁵–10⁶) e a decisão parece local → o autor espera greedy.
- Se envolve "alcance máximo" (até onde chego?) → manter fronteira e estendê-la.
- Antes de confiar: **tente montar um contraexemplo**; se achar, caia para DP.

## 3. Templates de Código

### Alcance máximo (Jump Game)

```java
// Java — 'alcance' é a fronteira do atingível; um índice além dela é ilha inalcançável
public boolean canJump(int[] nums) {
    int alcance = 0;
    for (int i = 0; i < nums.length; i++) {
        if (i > alcance) return false;             // buraco: ninguém chega aqui
        alcance = Math.max(alcance, i + nums[i]);  // estende a fronteira com o salto deste índice
    }
    return true;                                    // percorreu tudo dentro da fronteira
}
```

```python
def can_jump(nums):
    alcance = 0
    for i, salto in enumerate(nums):
        if i > alcance:
            return False          # a fronteira nunca alcançou i: impossível
        alcance = max(alcance, i + salto)
    return True
```

### Balanço com reinício (Gas Station)

```python
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1                        # globalmente impossível: nem adianta procurar início
    tanque = inicio = 0
    for i in range(len(gas)):
        tanque += gas[i] - cost[i]
        if tanque < 0:                   # quebrou aqui partindo de 'inicio'...
            inicio, tanque = i + 1, 0    # ...então NENHUM posto entre eles serve: pule todos
    return inicio                        # a prova de que este início fecha o circuito vem da soma total
```

### Seleção por fim (Non-overlapping Intervals)

```java
// Java — ordenar pelo FIM: quem termina cedo deixa mais espaço para os próximos
public int eraseOverlapIntervals(int[][] intervals) {
    Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));  // critério certo = fim, não início
    int removidos = 0;
    int fimAtual = Integer.MIN_VALUE;
    for (int[] it : intervals) {
        if (it[0] >= fimAtual) {
            fimAtual = it[1];      // compatível: adota este intervalo (termina o mais cedo possível)
        } else {
            removidos++;           // sobrepõe o escolhido: remover ESTE é sempre >= remover o outro
        }
    }
    return removidos;
}
```

## 4. Walkthrough Visual (Teste de Mesa)

`canJump(nums=[2, 3, 1, 1, 4])`

| i | nums[i] | i > alcance? | alcance = max(alcance, i+nums[i]) |
|---|---|---|---|
| 0 | 2 | 0 > 0? não | max(0, 2) = 2 |
| 1 | 3 | 1 > 2? não | max(2, 4) = 4 |
| 2 | 1 | 2 > 4? não | max(4, 3) = 4 |
| 3 | 1 | 3 > 4? não | max(4, 4) = 4 |
| 4 | 4 | 4 > 4? não | chegou ao fim → **true** ✔ |

- Contraste com `[3, 2, 1, 0, 4]`: em i=4, `4 > alcance=3` → **false** (o zero no índice 3 criou o buraco).

## 5. Complexidade (Tempo e Espaço)

| Padrão | Tempo | Espaço |
|---|---|---|
| Varredura com fronteira/balanço | O(n) | O(1) |
| Com ordenação prévia | O(n log n) | O(1)–O(n) do sort |
| vs. DP equivalente | — | DP paga O(n·estados) para GARANTIR o ótimo |

- Greedy é rápido porque **nunca reconsidera** — a mesma razão pela qual precisa de prova.

## 6. Pegadinhas e Erros Comuns

- Aplicar sem justificar: passa nos exemplos do enunciado e falha no caso oculto — o erro nº 1 da categoria.
- Ordenar pelo critério errado: agendamento é por **fim**; por início ou duração há contraexemplos clássicos.
- Gas Station sem o teste da soma total antes → retorna início "válido" em circuito impossível.
- Troco com moedas arbitrárias: guloso NÃO serve (use Coin Change/DP) — só funciona em sistemas canônicos.
- **Java**: `Comparator.comparingInt(a -> a[1])` — esquecer o comparator e ordenar `int[][]` pela referência.
- **Python**: `sort(key=lambda x: x[1])` — ordenar tuplas sem key compara o elemento 0 (início), o critério errado.
- Se a escolha atual pode precisar ser **desfeita** à luz do futuro → não é greedy, é DP/backtracking.

## 7. Aplicações no Mundo Real (Backend)

- **Escalonadores**: shortest-job-first, earliest-deadline-first (SO, Fase 1.3) — gulosos com prova.
- **Load balancing**: least-connections escolhe o servidor menos carregado AGORA — decisão local contínua.
- **Huffman coding** (gzip/brotli, Fase 6.10): guloso ótimo provado — junta sempre as duas frequências menores.
- **Kubernetes**: bin packing de pods usa heurísticas gulosas (first-fit/best-fit) porque o ótimo é NP-difícil.
- Lição de arquitetura: greedy sem prova = otimização sem medição — parece certo até o caso que derruba (Vol. 2, Módulo G).

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 53 | [Maximum Subarray (Kadane)](https://leetcode.com/problems/maximum-subarray/) | 🟡 Medium |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | 🟡 Medium |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | 🟡 Medium |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | 🟡 Medium |
| 846 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | 🟡 Medium |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | 🟡 Medium |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | 🟡 Medium |
