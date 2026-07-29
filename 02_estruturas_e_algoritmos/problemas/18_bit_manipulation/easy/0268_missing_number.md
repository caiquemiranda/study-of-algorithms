# [0268] Missing Number

> 🔗 [LeetCode 268](https://leetcode.com/problems/missing-number/) · Dificuldade: 🟢 easy · Categoria: [`18_bit_manipulation`](../../../fundamentos/18_bit_manipulation.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BitManipulation` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array `nums` com `n` números **distintos**, todos no intervalo `[0, n]`. Como o intervalo tem `n+1` valores possíveis (`0` até `n`) mas o array só tem `n` posições, **exatamente um número está faltando**. Encontre esse número.

**Exemplos:**
```
Input:  nums = [3,0,1]              Output: 2   (n=3, faltam checar 0..3, falta o 2)
Input:  nums = [0,1]                Output: 2   (n=2, faltam checar 0..2, falta o 2)
Input:  nums = [9,6,4,2,3,5,7,0,1]  Output: 8   (n=9, falta o 8)
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^4` → O(n log n) (sort) ou até O(n²) passariam no tempo, mas existe algo melhor
- `0 <= nums[i] <= n`, todos **únicos** → o array **não vem ordenado**, então busca binária exigiria pagar O(n log n) só para ordenar antes de buscar
- **Follow up:** "Could you implement a solution using only O(1) extra space and O(n) runtime?" → esse é o convite explícito para a solução ótima: nada de hash set (O(n) espaço) nem sort (O(n log n) tempo)

## 🧭 Como reconhecer o padrão

"Encontre o único número faltando/duplicado/sem-par num intervalo conhecido" é a assinatura clássica de **XOR**: XOR entre um número e ele mesmo é zero, e XOR é comutativo/associativo — então "cancelar" pares é natural. Aqui pensamos: se eu tivesse TODOS os números de `0` a `n` (o índice completo) e XORasse com todos os números do array (que tem um faltando), tudo que aparece nos dois lados se cancela e sobra exatamente o que falta.

## 🐢 Solução 1 — Força bruta

Para cada `i` de `0` a `n`, verificar se `i` existe em `nums` (busca linear); parar no primeiro que não existir.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** para cada um dos `n+1` candidatos, faz uma varredura O(n) no array — puro desperdício, já que dá pra descobrir o valor faltante numa única passada.

Uma alternativa intermediária, mas ainda não ótima: **ordenar** o array (O(n log n)) e depois comparar cada índice `i` com `nums[i]` — o primeiro índice onde eles divergem é a resposta (isso já seria busca binária pura, O(log n) *depois* de ordenar). Só que ordenar já custa mais do que o necessário: dá pra resolver em O(n) sem nem tocar em sort.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pense em dois "sacos" de números: um saco teórico com `0, 1, 2, ..., n` (todos os índices possíveis) e o saco real, que é o array `nums`. Todo número que existe nos dois sacos aparece duas vezes ao todo; o único que sobra sozinho é o que falta.

XOR tem a propriedade `a ^ a = 0` e `a ^ 0 = a`. Se eu fizer XOR de **todos os índices `0..n`** com **todos os valores do array**, cada número presente em ambos se cancela (`x ^ x = 0`), e o único número que não tem par — o que falta — sobra intacto no resultado final.

Na prática, dá pra fazer isso numa única passada: comece `resultado = n` (o maior índice) e para cada posição `i` de `0` a `n-1`, faça `resultado ^= i ^ nums[i]`.

## 🎬 Exemplo passo a passo

`nums = [3, 0, 1]` (n = 3)

| Passo | i | nums[i] | resultado (antes) | Operação | resultado (depois) |
|---|---|---|---|---|---|
| init | — | — | — | `resultado = n = 3` | 3 |
| 1 | 0 | 3 | 3 | `3 ^ 0 ^ 3` | 0 |
| 2 | 1 | 0 | 0 | `0 ^ 1 ^ 0` | 1 |
| 3 | 2 | 1 | 1 | `1 ^ 2 ^ 1` | 2 |

Resultado final: `2` ✔ (todo número de 0 a 3 exceto o 2 apareceu duas vezes e se cancelou)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelo array
- **Espaço:** O(1) — só uma variável acumuladora, sem sort e sem hash set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int missingNumber(int[] nums) {
    int n = nums.length;
    int resultado = n;                       // "n" é o único índice de 0..n que não tem posição no array

    for (int i = 0; i < n; i++) {
        // XOR do índice "i" com o valor "nums[i]": todo número que aparece
        // tanto como índice quanto como valor se cancela ao longo do laço.
        resultado ^= i ^ nums[i];
    }
    // O que sobrou é o único número sem par: o que está faltando.
    return resultado;
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

- **Usar soma (`n*(n+1)/2 - soma(nums)`) sem cuidar de overflow**: é uma alternativa igualmente O(n)/O(1) válida, mas em linguagens com inteiro de tamanho fixo, `n*(n+1)/2` pode estourar `int` para `n` grande — XOR nunca tem esse problema porque não cresce.
- **Inicializar `resultado = 0` em vez de `resultado = n`**: esquecer de incluir o índice extra `n` (o array só tem índices `0..n-1`, mas o intervalo de valores vai até `n`) faz o XOR cancelar tudo errado.
- **Tentar aplicar busca binária diretamente**: só funciona se o array estiver ordenado primeiro — e ordenar já custa mais (O(n log n)) do que a solução XOR (O(n)). É por isso que este problema muda de categoria: "busca binária" aparece nas tags do LeetCode, mas não é a técnica ótima aqui.
- **Confundir com "Find the Duplicate Number" (LC 287)**: lá o array tem um número **repetido** em vez de um faltando, e o intervalo é `[1, n]` — XOR simples não resolve, é preciso outra estratégia (Floyd's cycle detection).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Menor caso possível | `nums=[1]` | 0 | falta o menor valor do intervalo |
| Falta o maior valor | `nums=[0,1]` | 2 | falta o valor extra fora dos índices do array |
| Falta o primeiro | `nums=[1,2,3]` | 0 | zero nunca aparece no array |
| Array já "completo" exceto o meio | `nums=[9,6,4,2,3,5,7,0,1]` | 8 | trace acima, número faltando no meio da faixa |
| Um único elemento igual a zero | `nums=[0]` | 1 | n=1, falta o 1 |

## 🔗 Conexões

- Problemas irmãos: **[0136] Single Number** (mesma técnica de XOR para achar o "sem par"), **[0287] Find the Duplicate Number** (problema irmão na intenção, mas com repetido em vez de faltante — técnica diferente), **[0035] Search Insert Position** (usa busca binária de verdade, para contraste)
- No backend: XOR para achar "o que está faltando" aparece em checksums e detecção de corrupção de dados (paridade), e em reconciliação de conjuntos onde comparar dois grandes lotes de IDs sem usar memória extra é essencial (ex.: verificar se um lote de mensagens processadas bate com o esperado).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
