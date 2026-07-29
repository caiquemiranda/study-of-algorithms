# [0528] Random Pick with Weight

> 🔗 [LeetCode 528](https://leetcode.com/problems/random-pick-with-weight/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-29 · Revisões: —

Tags: `#BuscaBinaria` `#PrefixSum` `#Medium`

## 📜 O Problema

Você recebe um array `w` (0-indexado) de inteiros positivos, onde `w[i]` é o **peso** do índice `i`. Implemente `pickIndex()`, que sorteia aleatoriamente um índice de `[0, w.length-1]`, de forma que a **probabilidade de escolher o índice `i`** seja `w[i] / soma(w)`.

**Exemplo:**
```
w = [1, 3]
P(escolher índice 0) = 1/4 = 25%
P(escolher índice 1) = 3/4 = 75%
```

**Restrições (e o que elas denunciam):**
- `1 <= w.length <= 10^4`, `pickIndex` chamado até `10^4` vezes → cada chamada precisa ser rápida (O(log n)), já que o pré-processamento acontece uma vez só no construtor
- "probabilidade de escolher `i` é `w[i] / soma(w)`" → índices com peso maior precisam ter mais chance — não é um sorteio uniforme entre índices, é ponderado
- `1 <= w[i] <= 10^5` → pesos sempre positivos, então a soma prefixada é sempre estritamente crescente (sem "empates" que atrapalhem a busca binária)

## 🧭 Como reconhecer o padrão

"Sortear um item de uma lista onde cada item tem um **peso**/probabilidade diferente" é o padrão de **soma prefixada + busca binária**: transforme os pesos numa reta numérica acumulada (soma prefixada), sorteie um ponto uniforme nessa reta, e ache — via busca binária — em qual "fatia" (índice) esse ponto caiu. Fatias maiores (pesos maiores) ocupam mais espaço na reta, logo têm mais chance de serem sorteadas.

## 🐢 Solução 1 — Força bruta

A cada chamada de `pickIndex()`, construir uma lista "expandida" onde cada índice `i` aparece `w[i]` vezes, e sortear um elemento uniformemente dessa lista.

- Tempo: O(∑w) por chamada (ou de pré-processamento, se feita uma vez) · Espaço: O(∑w)
- **Por que não basta:** com pesos até 10^5 e até 10^4 índices, a lista expandida pode ter até 10^9 elementos — inviável em memória. A soma prefixada representa a mesma informação em O(n) de espaço, sem precisar "expandir" nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

No construtor, monte o array de **soma prefixada** dos pesos: `prefixo[i] = w[0] + w[1] + ... + w[i]`. A soma total é `prefixo[n-1]`.

A cada chamada de `pickIndex()`:
1. Sorteie um inteiro `r` uniforme em `[1, somaTotal]` (ou `[0, somaTotal-1]`, dependendo da convenção).
2. Faça busca binária (lower bound) no array de soma prefixada pela primeira posição `i` onde `prefixo[i] >= r`. Esse `i` é o índice sorteado.

Índices com peso maior ocupam uma faixa maior de valores possíveis de `r` na soma prefixada, então são proporcionalmente mais prováveis de serem escolhidos.

## 🎬 Exemplo passo a passo

`w = [1, 3]` → soma prefixada: `[1, 4]` (soma total = 4)

Suponha que o sorteio devolveu `r = 3` (dentro de `[1, 4]`):

| Passo | left | mid | right | prefixo[mid] | Comparação | Decisão |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 (val 1) | 1 | 1 | 1 >= 3? não | `left = 1` |
| 2 | 1 | 1 (val 4) | 1 | 4 | `left==right` → fim | idx = 1 |

Resultado: índice `1` escolhido ✔ (consistente com a probabilidade de 75% do índice 1 — a faixa `[2,4]` de `r`, tamanho 3, pertence a ele; só `r=1` pertence ao índice 0)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no construtor para montar a soma prefixada; O(log n) por chamada de `pickIndex()`
- **Espaço:** O(n) para a soma prefixada

## 💻 Implementações

### Java (referência completa e comentada)
```java
class Solution {
    private final int[] somaPrefixada;
    private final int somaTotal;
    private final Random random = new Random();

    public Solution(int[] w) {
        somaPrefixada = new int[w.length];
        int acumulado = 0;
        for (int i = 0; i < w.length; i++) {
            acumulado += w[i];
            somaPrefixada[i] = acumulado;
        }
        somaTotal = acumulado;
    }

    public int pickIndex() {
        // Sorteio uniforme em [1, somaTotal]: nextInt(somaTotal) dá [0, somaTotal-1], +1 ajusta.
        int r = random.nextInt(somaTotal) + 1;
        return lowerBound(r);
    }

    // Busca binária: primeiro índice onde somaPrefixada[idx] >= alvo.
    private int lowerBound(int alvo) {
        int left = 0, right = somaPrefixada.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (somaPrefixada[mid] < alvo) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
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

- **Sortear índice uniformemente em vez de por peso**: ignoraria completamente a proporção `w[i]/soma(w)` — é o erro mais direto de não entender o problema.
- **Off-by-one no intervalo do sorteio**: usar `[1, somaTotal]` (inclusivo nos dois lados) exige `random.nextInt(somaTotal) + 1`; usar `[0, somaTotal-1]` exige trocar a busca para "primeiro índice onde `prefixo[idx] > r`" (upper bound) em vez de `>=`. Misturar as duas convenções é a fonte mais comum de bug neste problema.
- **Recalcular a soma prefixada a cada chamada de `pickIndex()`**: desperdiça O(n) por chamada — o pré-processamento deve acontecer **uma vez só**, no construtor.
- **Overflow em `int` para pesos muito grandes**: com `w[i]` até 10^5 e até 10^4 índices, a soma total pode chegar a 10^9 — ainda cabe em `int` (limite ~2.1×10^9), mas é um caso limítrofe que merece atenção se as restrições mudarem.

## 🧪 Casos de teste para validar

| Caso | Input | Comportamento esperado | Por quê |
|---|---|---|---|
| Um único peso | `w=[1]` | sempre retorna 0 | borda mínima, única opção possível |
| Pesos iguais | `w=[5,5,5]` | cada índice ~1/3 das vezes | testa distribuição uniforme quando pesos empatam |
| Peso dominante | `w=[1,1,1,1000]` | índice 3 escolhido quase sempre | testa peso muito maior que os outros |
| Exemplo do enunciado | `w=[1,3]` | índice 1 ~75%, índice 0 ~25% | trace acima |
| Dois pesos, extremos do sorteio | `w=[2,2]` | `r=1` ou `r=2` → índice 0; `r=3` ou `r=4` → índice 1 | testa a fronteira exata da busca binária |

## 🔗 Conexões

- Problemas irmãos: **[0497] Random Point in Non-overlapping Rectangles** (mesmo padrão, mas o "peso" é a área de um retângulo 2D), **[0035] Search Insert Position** (o lower bound usado como bloco de construção aqui)
- No backend: escolher um servidor/réplica proporcionalmente à sua capacidade disponível (balanceamento de carga ponderado), ou sortear um item de um leilão/loteria onde cada participante tem "bilhetes" proporcionais ao valor investido, usa exatamente essa técnica de soma prefixada + busca binária.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
