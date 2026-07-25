# 15 — Greedy (Algoritmos Gulosos)

> Fazer a melhor escolha local em cada passo — quando isso comprovadamente leva ao ótimo global. Problemas em [`../problemas/15_greedy/`](../problemas/15_greedy/).

## Conceito

Um algoritmo guloso decide sem olhar o futuro. Só funciona quando o problema tem:
1. **Propriedade da escolha gulosa**: uma escolha ótima local pode ser estendida a uma solução ótima global
2. **Subestrutura ótima**: o que sobra após a escolha é o mesmo problema, menor

**A diferença para DP**: DP explora todas as opções e escolhe depois; greedy compromete-se já. Por isso greedy é O(n) ou O(n log n) — e por isso **falha silenciosamente** quando a propriedade não vale (o contraexemplo clássico: troco com moedas {1, 3, 4} para 6 — guloso dá 4+1+1, ótimo é 3+3 → precisa de DP).

**Como validar um greedy (em entrevista, verbalize):**
- **Argumento de troca (exchange argument)**: "se a solução ótima difere da gulosa, posso trocar um elemento pelo escolhido pelo guloso sem piorar"
- Ou encontre um **contraexemplo** e caia para DP

**Padrões gulosos recorrentes:**
- **Ordenar por critério certo e varrer** (fim mais cedo, razão, deadline)
- **Alcance máximo**: manter "até onde consigo chegar" (Jump Game)
- **Balanço/prefixo**: se o acumulado ficou negativo, recomece do próximo (Gas Station, Kadane)

## Como reconhecer no enunciado

- "número mínimo de intervalos/saltos/remoções" com estrutura sequencial
- Agendamento/seleção de atividades
- A versão DP existiria mas os limites são grandes demais (n ~ 10⁵/10⁶) → o autor espera greedy
- ⚠️ Sempre pergunte: "consigo montar um contraexemplo?" antes de confiar

## Templates

```python
# Alcance máximo — Jump Game, O(n)
def can_jump(nums):
    alcance = 0
    for i, salto in enumerate(nums):
        if i > alcance:
            return False              # buraco inalcançável
        alcance = max(alcance, i + salto)
    return True

# Gas Station — balanço com reinício, O(n)
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1                     # impossível globalmente
    tanque = inicio = 0
    for i in range(len(gas)):
        tanque += gas[i] - cost[i]
        if tanque < 0:                # não chega em i+1 partindo de 'inicio'
            inicio, tanque = i + 1, 0 # nenhum ponto entre eles serve — pule
    return inicio

# Partition Labels — última ocorrência define o corte, O(n)
def partition_labels(s):
    ultima = {ch: i for i, ch in enumerate(s)}
    res, fim, inicio = [], 0, 0
    for i, ch in enumerate(s):
        fim = max(fim, ultima[ch])
        if i == fim:                  # ninguém desta janela aparece depois
            res.append(i - inicio + 1)
            inicio = i + 1
    return res
```

## Complexidade típica

O(n) ou O(n log n) (quando exige ordenação prévia) — a recompensa por abrir mão da exploração exaustiva.

## Erros comuns

- Aplicar greedy sem justificar (funciona nos exemplos, falha no caso oculto)
- Ordenar pelo critério errado (agendamento: ordene por **fim**, não por início nem duração)
- Não tratar o caso "impossível" antes do loop (Gas Station sem o teste da soma)
- Confundir com DP: se a escolha atual pode precisar ser desfeita à luz do futuro, não é greedy

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 53. Maximum Subarray (Kadane) | 🟡 medium |
| 55 / 45. Jump Game I e II | 🟡 medium |
| 134. Gas Station | 🟡 medium |
| 846. Hand of Straights | 🟡 medium |
| 763. Partition Labels | 🟡 medium |
| 678. Valid Parenthesis String | 🟡 medium |
| 1899. Merge Triplets | 🟡 medium |

## Conexão com backend

Escalonadores usam greedy o tempo todo: shortest-job-first, earliest-deadline-first (SO — Fase 1.3), bin packing de pods, balanceamento least-connections (Fase 14.2). Huffman coding (compressão gzip — Fase 6.10) é um greedy com prova formal. E a lição de arquitetura: greedy sem prova é como otimização sem medição — parece certo até o caso que derruba.
