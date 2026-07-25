# [0303] Range Sum Query - Immutable

> 🔗 [LeetCode 303](https://leetcode.com/problems/range-sum-query-immutable/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Design` `#PrefixSum` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums`, implemente a classe `NumArray` para responder **múltiplas** consultas do tipo: "qual a soma dos elementos entre os índices `left` e `right` (inclusive)?"

**Exemplos:**
```
NumArray([-2, 0, 3, -5, 2, -1])
sumRange(0, 2)  → (-2) + 0 + 3        = 1
sumRange(2, 5)  → 3 + (-5) + 2 + (-1) = -1
sumRange(0, 5)  → soma de tudo        = -3
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` e **"até 10^4 chamadas a `sumRange`"** → é a pista central do problema: com muitas consultas, **cada uma tem que ser O(1)**, senão o total vira O(n × q) ~ 10^8, arriscado
- O array é **imutável** (o nome da classe já avisa) → não há `update()`, então dá para **pré-computar tudo uma única vez** no construtor
- `-10^5 <= nums[i] <= 10^5` → soma pode chegar a ~10^9, ainda cabe em `int`, mas fique de olho se as constraints fossem maiores

## 🧭 Como reconhecer o padrão

"Múltiplas consultas de soma de intervalo" em uma estrutura que **não muda** é a definição de livro-texto de **prefix sum**: pague o custo de pré-processar uma vez (O(n)) para responder cada consulta depois em O(1).

## 🐢 Solução 1 — Força bruta

A cada chamada de `sumRange(left, right)`, percorrer o array do índice `left` até `right` somando os valores.

- Tempo: O(n) por consulta, O(n × q) no total para q consultas · Espaço: O(1) extra
- **Por que não basta:** com `q` podendo ser 10.000 e `n` podendo ser 10.000, o pior caso chega a 10^8 operações — no limite do aceitável, mas desperdiça a informação de que o array nunca muda entre as consultas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa, uma única vez, um array de **somas de prefixo**: `prefixo[i]` = soma de `nums[0]` até `nums[i-1]`. A partir daí, a soma de qualquer intervalo `[left, right]` é uma simples subtração: `prefixo[right+1] - prefixo[left]` — como "cortar um pedaço de uma régua" usando duas marcas já desenhadas.

## 🎬 Exemplo passo a passo

`nums = [-2, 0, 3, -5, 2, -1]` → construção do prefixo (tamanho n+1, começando em 0):

| i | nums[i-1] | prefixo[i] = prefixo[i-1] + nums[i-1] |
|---|---|---|
| 0 | — | 0 |
| 1 | -2 | 0 + (-2) = -2 |
| 2 | 0 | -2 + 0 = -2 |
| 3 | 3 | -2 + 3 = 1 |
| 4 | -5 | 1 + (-5) = -4 |
| 5 | 2 | -4 + 2 = -2 |
| 6 | -1 | -2 + (-1) = -3 |

Agora `sumRange(2, 5)` = `prefixo[6] - prefixo[2]` = `-3 - (-2)` = **-1** ✔ (bate com o exemplo do enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) para construir o prefixo (uma vez, no construtor); **O(1) por consulta** depois
- **Espaço:** O(n) — o array de prefixo tem um elemento a mais que `nums`

## 💻 Implementações

### Java (referência completa e comentada)
```java
class NumArray {
    private final int[] prefixo;

    public NumArray(int[] nums) {
        // prefixo[i] = soma de nums[0..i-1]; prefixo[0] = 0 é o caso base (soma vazia)
        prefixo = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefixo[i + 1] = prefixo[i] + nums[i];
        }
    }

    public int sumRange(int left, int right) {
        // soma[left..right] = tudo até 'right' MENOS tudo até antes de 'left'
        return prefixo[right + 1] - prefixo[left];
    }
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

- Esquecer o **deslocamento de +1** no array de prefixo — sem o `prefixo[0] = 0` inicial, a subtração para o intervalo que começa em `left = 0` fica errada.
- Fazer `prefixo[right] - prefixo[left]` (sem o `+1` no `right`) — erro de off-by-one clássico; sempre teste na régua: `prefixo[i]` cobre `nums[0..i-1]`, não `nums[0..i]`.
- Recalcular a soma do zero a cada chamada de `sumRange` (a força bruta) quando o enunciado já avisa "múltiplas consultas" — é o sinal para pré-computar.
- **Java**: se as constraints fossem maiores (arrays somando bilhões), `int` poderia estourar — use `long` para o array de prefixo nesse caso.

## 🧪 Casos de teste para validar

| Caso | Chamada | Esperado | Por quê |
|---|---|---|---|
| Intervalo de um elemento | `sumRange(0,0)` com `nums=[5]` | 5 | borda mínima |
| Intervalo = array inteiro | `sumRange(0, n-1)` | soma total | testa o prefixo completo |
| Intervalo no meio | `sumRange(2,2)` | `nums[2]` | intervalo de tamanho 1 no meio |
| Valores negativos | `nums=[-1,-1,-1]`, `sumRange(0,2)` | -3 | garante que a subtração lida bem com negativos |

## 🔗 Conexões

- Problemas irmãos: **[0304] Range Sum Query 2D - Immutable** (mesma ideia, mas com prefixo em matriz), **[0560] Subarray Sum Equals K** (prefix sum combinado com hash map para contar subarrays)
- No backend: métricas acumuladas (bytes transferidos até o minuto X), saldo de conta bancária em qualquer ponto do extrato, e paginação de contadores em dashboards são todos casos de "consulta de intervalo em dado imutável" resolvidos com prefix sum.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
