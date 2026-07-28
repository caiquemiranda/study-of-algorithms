# [2491] Divide Players Into Teams of Equal Skill

> 🔗 [LeetCode 2491](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Greedy` `#Sorting` `#Medium`

## 📜 O Problema

Dado `skill` (tamanho par), divida os jogadores em `n/2` times de 2, todos com a **mesma** soma de habilidade. A "química" de um time é o produto das habilidades. Retorne a soma das químicas de todos os times, ou `-1` se não for possível dividir com somas iguais.

**Exemplos:**
```
Input:  skill = [3,2,5,1,3,4]
Output: 22
Explicação: times (1,5),(2,4),(3,3), todos somando 6; química = 5+8+9 = 22.

Input:  skill = [3,4]
Output: 12

Input:  skill = [1,1,2,3]
Output: -1
```

**Restrições (e o que elas denunciam):**
- `2 <= skill.length <= 10^5`, tamanho sempre par → O(n²) é arriscado, O(n log n) é o esperado
- `1 <= skill[i] <= 1000` → o produto de dois valores pode chegar a `10^6`, e a soma acumulada de até `5×10^4` produtos pode passar de `2×10^9` — precisa de `long`
- Times de soma **igual** → sinaliza que só uma estratégia específica de emparelhamento (menor com maior) pode funcionar; se ela falhar, nenhuma outra tentativa resolveria

## 🧭 Como reconhecer o padrão

"Formar pares com soma igual entre todos" é resolvido ordenando o array e emparelhando o menor valor disponível com o maior — a mesma estrutura de [1877] Minimize Maximum Pair Sum in Array. A diferença aqui é que, em vez de minimizar o máximo, é preciso **verificar** se essa estratégia produz somas idênticas em TODOS os pares; se não produzir, nenhuma outra estratégia de emparelhamento conseguiria (é uma propriedade do multiconjunto de valores, não da ordem escolhida).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Testar todas as formas possíveis de agrupar o array em pares, verificando se TODOS os pares de algum agrupamento têm soma igual, e calculando a química só para agrupamentos válidos.

- Tempo: O(n!) — dupla-fatorial de agrupamentos possíveis
- **Por que não basta:** claramente inviável. Ordenar o array e verificar se o emparelhamento menor-com-maior produz somas consistentes já resolve o problema — se essa estratégia específica falhar, nenhum outro agrupamento poderia funcionar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `skill`. Use `left` no início e `right` no fim. A soma do primeiro par (`skill[left] + skill[right]`) define o **alvo** que todo par subsequente precisa igualar. Avance os dois ponteiros pra dentro, formando pares e checando a cada passo se a soma bate com o alvo — se não bater em algum momento, retorne `-1` imediatamente. Se todos baterem, acumule o produto (`skill[left] * skill[right]`) de cada par.

## 🎬 Exemplo passo a passo

`skill = [3,2,5,1,3,4]` → ordenado: `[1,2,3,3,4,5]`

| Passo | left (valor) | right (valor) | soma | Comparação com alvo | química acumulada |
|---|---|---|---|---|---|
| 1 | 0 (1) | 5 (5) | 6 | define o alvo = 6 | +1×5 = 5 |
| 2 | 1 (2) | 4 (4) | 6 | == alvo | +2×4 = 13 |
| 3 | 2 (3) | 3 (3) | 6 | == alvo | +3×3 = 22 |

`left(3) >= right(2)` → loop termina. Resultado final: `22` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação; a varredura com dois ponteiros depois é O(n)
- **Espaço:** O(log n) a O(n), dependendo do algoritmo de sort usado internamente

## 💻 Implementações

### Java (referência completa e comentada)
```java
public long dividePlayers(int[] skill) {
    Arrays.sort(skill);
    int n = skill.length;
    int left = 0;
    int right = n - 1;
    int target = skill[left] + skill[right]; // soma do primeiro par define o alvo pros demais
    long chemistry = 0;

    while (left < right) {
        if (skill[left] + skill[right] != target) {
            return -1; // esse par quebra a exigência de soma igual: divisão impossível
        }
        chemistry += (long) skill[left] * skill[right];
        left++;
        right--;
    }

    return chemistry;
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

- Esquecer de checar se TODOS os pares têm a mesma soma — só formar os pares (menor com maior) não basta; se algum tiver soma diferente do alvo, a resposta é `-1`.
- Usar `int` para acumular a química — o produto de dois valores até `1000` já dá até `10^6`, e a soma de vários desses produtos pode estourar `int`; `long` é obrigatório.
- Definir o alvo errado (ex.: usar a média da soma total, ou o primeiro elemento sozinho) — o alvo é especificamente a soma do PRIMEIRO par formado após ordenar (`skill[0] + skill[n-1]`).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Divisão válida | `[3,2,5,1,3,4]` | 22 | três pares, todos somando 6 |
| Par único | `[3,4]` | 12 | caso mínimo, um único par |
| Divisão impossível | `[1,1,2,3]` | -1 | nenhuma forma de emparelhar dá somas iguais |
| Todos os valores iguais | `[2,2,2,2]` | 8 | todo par soma 4, química = 2×2 + 2×2 = 8 |

## 🔗 Conexões

- Problemas irmãos: [1877] Minimize Maximum Pair Sum in Array (mesma técnica de ordenar e combinar menor-com-maior), [2465] Number of Distinct Averages (mesma família de processar repetidamente os extremos de um array ordenado)
- No backend: formar duplas de trabalho com carga total balanceada — por exemplo, parear tarefas pesadas e leves de forma que cada dupla tenha o mesmo esforço combinado, validando se a divisão é sequer possível antes de prosseguir.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
