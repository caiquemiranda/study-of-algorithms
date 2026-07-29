# [0888] Fair Candy Swap

> 🔗 [LeetCode 888](https://leetcode.com/problems/fair-candy-swap/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArraysEHashing` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Alice e Bob têm quantidades diferentes de doces, divididas em caixas: `aliceSizes[i]` é o tamanho da caixa `i` de Alice, `bobSizes[j]` o de Bob. Eles querem trocar **uma caixa cada um** de forma que, depois da troca, os dois fiquem com a **mesma quantidade total** de doces. Retorne um par `[caixaDeAlice, caixaDeBob]` que resolve a troca (garantido que existe pelo menos uma solução).

**Exemplos:**
```
Input:  aliceSizes = [1,2], bobSizes = [2,3]    Output: [1,2]
Input:  aliceSizes = [2], bobSizes = [1,3]      Output: [2,3]
```

**Restrições (e o que elas denunciam):**
- `1 <= aliceSizes.length, bobSizes.length <= 10^4` → O(n×m) força bruta (10^8) é arriscado; existe algo em O(n+m)
- "there will be at least one valid answer" → não precisamos tratar o caso "sem solução" — simplifica a busca
- A equação da troca (`sumA - x + y == sumB - y + x`) é **uma equação linear com uma incógnita** depois de fixar `x` → para cada `x` de Alice, o `y` de Bob necessário é único e calculável diretamente, o que pede uma estrutura de consulta O(1): **hash set**

## 🧭 Como reconhecer o padrão

Isolando a equação da troca, para cada caixa `x` de Alice existe **exatamente um** valor `y` de Bob que resolveria o problema. Isso é a mesma assinatura de "complemento" do Two Sum: fixe um lado, calcule o que o outro lado precisa ser, e consulte um hash set em O(1) para ver se esse valor existe.

## 🐢 Solução 1 — Força bruta

Para cada caixa `x` de Alice, para cada caixa `y` de Bob, verificar se trocá-las equilibra os totais (`sumA - x + y == sumB - y + x`).

- Tempo: O(n × m) · Espaço: O(1)
- **Por que não basta:** com `n` e `m` até 10^4, o produto chega a 10^8 comparações — funciona, mas desperdiça a estrutura da equação: dado `x`, o `y` certo é conhecido de antemão, não precisa testar todos os `y`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Isole a equação: se Alice troca a caixa `x` pela caixa `y` de Bob, o novo total de Alice é `sumA - x + y`, e o de Bob é `sumB - y + x`. Para ficarem iguais:

```
sumA - x + y = sumB - y + x
2y = sumB - sumA + 2x
y = x + (sumB - sumA) / 2
```

Ou seja, para cada `x` em `aliceSizes`, existe **um único** `y` candidato — basta calculá-lo e verificar se ele está em `bobSizes`. Colocando `bobSizes` num hash set, essa verificação vira O(1), e a busca inteira vira uma única passada por `aliceSizes`.

`diff = (sumB - sumA) / 2` é constante para todo o problema (calculado uma vez fora do laço).

## 🎬 Exemplo passo a passo

`aliceSizes = [1, 2]`, `bobSizes = [2, 3]` → `sumA = 3`, `sumB = 5`, `diff = (5-3)/2 = 1`

| Passo | Estrutura | x (de Alice) | y = x + diff | y está em setBob? | Decisão |
|---|---|---|---|---|---|
| 1 | setBob = `{2, 3}` | (construção) | — | — | setBob pronto |
| 2 | — | 1 | 1 + 1 = 2 | sim (2 está no set) | retorna `[1, 2]` |

Resultado final: `[1, 2]` ✔ (Alice troca a caixa de 1 doce pela caixa de 2 doces de Bob: Alice fica com 3-1+2=4, Bob fica com 5-2+1=4)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — uma passada para somar e montar o set, outra para procurar o par
- **Espaço:** O(m) — o hash set com as caixas de Bob

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
    int sumA = 0, sumB = 0;
    for (int a : aliceSizes) sumA += a;
    for (int b : bobSizes) sumB += b;

    // diff é quanto cada "y" precisa exceder o "x" correspondente para equilibrar os totais.
    int diff = (sumB - sumA) / 2;

    Set<Integer> setBob = new HashSet<>();
    for (int b : bobSizes) {
        setBob.add(b);                     // consulta O(1) na busca abaixo
    }

    for (int x : aliceSizes) {
        int y = x + diff;                  // único candidato de Bob que resolveria a troca com este x
        if (setBob.contains(y)) {
            return new int[]{x, y};
        }
    }
    return new int[]{};                    // inalcançável: o enunciado garante que existe solução
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

- **Erro de sinal na fórmula do `diff`**: é fácil trocar `(sumB - sumA)` por `(sumA - sumB)` e inverter a direção da busca — sempre reconferir com um exemplo pequeno antes de codar.
- **`diff` ímpar**: se `(sumB - sumA)` fosse ímpar, `y` nunca seria um inteiro válido para equilibrar — na prática o enunciado garante solução, então isso não acontece, mas é bom entender por quê (a divisão inteira arredondaria errado silenciosamente).
- **Somar com `int` em vez de `long` para arrays gigantes**: aqui os valores são pequenos (`1 <= size <= 10^5`, até `10^4` caixas), então `int` cabe, mas é o tipo de suposição que quebra em variações do problema com limites maiores.
- **Confundir com busca binária**: ordenar e buscar `y` via binary search também funciona (O((n+m) log m)), mas é estritamente pior que o hash set O(n+m) — por isso a categoria final é hashing, não busca binária.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Uma caixa cada | `aliceSizes=[2], bobSizes=[1,3]` | `[2,3]` | borda mínima em ambos os arrays |
| Já quase equilibrado | `aliceSizes=[1,2], bobSizes=[2,3]` | `[1,2]` | trace acima |
| Diferença grande | `aliceSizes=[1,1], bobSizes=[2,2]` | `[1,2]` | testa diff positivo simples |
| Alice tem mais doces que Bob | `aliceSizes=[35,17,4,24,10], bobSizes=[13,20,73,71,34]` | qualquer par válido (ex. `[24,73]`) | testa diff negativo (sumA > sumB) |
| Arrays de tamanho 1 cada | `aliceSizes=[2], bobSizes=[4]` | `[2,4]` | menor caso possível de troca válida |

## 🔗 Conexões

- Problemas irmãos: **[1346] Check If N and Its Double Exist** (mesmo padrão de "calcule o complemento e procure no set"), **[0001] Two Sum** (a raiz de todo esse padrão de complemento via hashing)
- No backend: resolver "qual registro do outro lado equilibra uma equação" via hash set é o mesmo padrão de casamento de transações em sistemas de conciliação financeira — dado um débito, procurar em O(1) o crédito exato que zera a diferença, sem comparar todos os pares.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente a ordenar+buscar o `y` candidato), mas a técnica ótima é hash set com cálculo direto do complemento (O(n+m), sem ordenar), então o documento foi classificado em `01_arrays_e_hashing`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
