# [0575] Distribute Candies

> 🔗 [LeetCode 575](https://leetcode.com/problems/distribute-candies/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Easy`

## 📜 O Problema

Alice tem `n` doces, onde o `i`-ésimo doce é do tipo `candyType[i]`. Alice percebeu que começou a ganhar peso, então visitou um médico. O médico recomendou que ela coma apenas `n / 2` dos doces que tem (`n` é sempre par). Alice gosta muito dos seus doces e quer comer o máximo número de tipos diferentes enquanto segue a recomendação médica.

Dado o array de inteiros `candyType` de tamanho `n`, retorne **o número máximo de tipos diferentes de doces que ela pode comer, comendo apenas `n / 2` deles**.

**Exemplos:**
```
Input:  candyType = [1,1,2,2,3,3]
Output: 3
Explicação: ela pode comer 6/2 = 3 doces. Como só há 3 tipos, pode comer um de cada.

Input:  candyType = [1,1,2,3]
Output: 2
Explicação: ela pode comer 4/2 = 2 doces. Seja [1,2], [1,3] ou [2,3], ainda são só 2 tipos diferentes.

Input:  candyType = [6,6,6,6]
Output: 1
Explicação: ela pode comer 2 doces, mas só existe 1 tipo.
```

**Restrições (e o que elas denunciam):**
- `n == candyType.length`, `2 <= n <= 10^4`, `n` sempre par → a resposta é limitada tanto pelo número de tipos distintos quanto pelo limite de quantidade (`n/2`)
- `-10^5 <= candyType[i] <= 10^5` → valores podem ser negativos, então não dá pra usar o valor como índice direto de array; precisa de hash set

## 🧭 Como reconhecer o padrão

"Quantos tipos distintos" é sempre resolvido contando o tamanho de um conjunto (hash set) dos valores únicos — a "distribuição ótima" aqui se resume a comparar esse número de tipos distintos com o limite de quantidade que ela pode comer.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada doce, verificar se o tipo já apareceu antes percorrendo todos os doces anteriores (comparação par a par).

- Tempo: O(n²) — para cada doce, percorre os anteriores em busca de duplicata · Espaço: O(1) extra (fora a entrada)
- **Por que não basta:** com n até 10^4, dá 10^8 comparações — funciona mas é redundante; um hash set responde "já vi esse tipo?" em O(1) em vez de O(n).

## 💡 Solução 2 — A ideia otimizada (intuição)

Coloque todos os tipos em um `HashSet` (isso elimina duplicatas automaticamente e dá o número de tipos distintos em O(n)). A resposta é o menor valor entre `tiposDistintos` e `n/2` — ela nunca pode comer mais tipos diferentes do que existem, nem mais doces do que a metade permitida.

## 🎬 Exemplo passo a passo

`candyType = [1,1,2,2,3,3]`

| Passo | candy | set antes | Ação | set depois |
|---|---|---|---|---|
| 1 | 1 | {} | adiciona | {1} |
| 2 | 1 | {1} | já existe, ignora | {1} |
| 3 | 2 | {1} | adiciona | {1,2} |
| 4 | 2 | {1,2} | já existe, ignora | {1,2} |
| 5 | 3 | {1,2} | adiciona | {1,2,3} |
| 6 | 3 | {1,2,3} | já existe, ignora | {1,2,3} |

`tiposDistintos = 3`, `n/2 = 3` → `min(3,3) = 3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para construir o set
- **Espaço:** O(n) no pior caso — todos os tipos distintos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int distributeCandies(int[] candyType) {
    Set<Integer> tiposUnicos = new HashSet<>();
    for (int tipo : candyType) {
        tiposUnicos.add(tipo); // HashSet já ignora duplicatas automaticamente
    }
    int limiteDeComer = candyType.length / 2;
    return Math.min(tiposUnicos.size(), limiteDeComer); // não pode comer mais tipos do que existem, nem mais que a metade
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

- Usar um array de contagem fixo (`int[200001]`) em vez de `HashSet` — funciona (os valores cabem no intervalo `[-10^5, 10^5]` com deslocamento), mas gasta memória fixa grande desnecessariamente; o `HashSet` escala com o tamanho real da entrada.
- Esquecer de tirar o `min` com `n/2` — retornar só o número de tipos distintos falha quando há MUITOS tipos diferentes mas ela só pode comer poucos doces (ex.: `n=4` com 4 tipos distintos, ela só come 2).
- Confundir "tipos distintos" com "quantidade total de doces" — o tamanho do array `candyType` não é a resposta, é só o denominador para calcular quantos doces ela pode comer.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Tipos suficientes para todos | `[1,1,2,2,3,3]` | 3 | 3 tipos distintos, pode comer até 3 |
| Poucos tipos distintos | `[1,1,2,3]` | 2 | 3 tipos distintos mas só pode comer 2 |
| Um único tipo | `[6,6,6,6]` | 1 | só existe 1 tipo, mesmo podendo comer 2 doces |
| Todos distintos | `[1,2,3,4]` | 2 | 4 tipos distintos, mas o limite da metade (2) é o gargalo |

## 🔗 Conexões

- Problemas irmãos: [0217] Contains Duplicate (mesmo uso básico de HashSet), [0350] Intersection of Two Arrays II (contagem de elementos únicos/frequência com hash)
- No backend: cálculo de cardinalidade distinta em análises de dados (ex.: "quantos usuários únicos visitaram o site", "quantos produtos diferentes um cliente pode levar dado um limite de itens no carrinho") — o padrão hash set + min com um limite externo é recorrente em regras de negócio com cota.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
