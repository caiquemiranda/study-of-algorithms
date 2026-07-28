# [2149] Rearrange Array Elements by Sign

> 🔗 [LeetCode 2149](https://leetcode.com/problems/rearrange-array-elements-by-sign/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Medium`

## 📜 O Problema

Dado um array `nums` de tamanho par com quantidades iguais de positivos e negativos, reorganize-o de forma que: todo par consecutivo tenha sinais opostos; a ordem relativa dentro de cada sinal seja preservada; o array comece com um positivo.

**Exemplos:**
```
Input:  nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Input:  nums = [-1,1]
Output: [1,-1]
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 2 * 10^5`, tamanho sempre par → garante que a alternância perfeita (positivo, negativo, positivo, ...) sempre é possível
- Quantidade igual de positivos e negativos → cada grupo ocupa exatamente metade das posições finais
- Ordem relativa preservada dentro de cada sinal → a saída não pode reordenar por valor, só reagrupar por posição

## 🧭 Como reconhecer o padrão

"Intercalar dois grupos (por uma condição binária) numa saída de posições fixas alternadas, preservando a ordem de cada grupo" é dois ponteiros escrevendo direto no array de resultado: um cuida só das posições **pares** (positivos), o outro só das **ímpares** (negativos) — a mesma ideia de [0922] Sort Array By Parity II, mas aqui o "sinal" de cada posição já é fixo, não precisa ser descoberto.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição do array resultado, escanear `nums` do início até encontrar o próximo número do sinal esperado que ainda não foi usado (marcando como usado).

- Tempo: O(n²) · Espaço: O(n)
- **Por que não basta:** refaz a busca do início a cada posição, revisitando elementos já processados; dois ponteiros — um avançando só entre posições pares, outro só entre ímpares — já sabem exatamente onde escrever o próximo número de cada sinal, numa única passada por `nums`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `posIdx = 0` (próxima posição par livre) e `negIdx = 1` (próxima posição ímpar livre). Percorra `nums` uma única vez: se o número for positivo, escreva-o em `result[posIdx]` e avance `posIdx` em 2; se for negativo, escreva em `result[negIdx]` e avance `negIdx` em 2. Como `nums` é processado em ordem e cada sinal tem seu próprio ponteiro independente, a ordem relativa dentro de cada grupo é preservada automaticamente.

## 🎬 Exemplo passo a passo

`nums = [3,1,-2,-5,2,-4]`

| Passo | num | Sinal | Ação | posIdx depois | negIdx depois |
|---|---|---|---|---|---|
| 1 | 3 | + | `result[0]=3` | 2 | 1 |
| 2 | 1 | + | `result[2]=1` | 4 | 1 |
| 3 | -2 | − | `result[1]=-2` | 4 | 3 |
| 4 | -5 | − | `result[3]=-5` | 4 | 5 |
| 5 | 2 | + | `result[4]=2` | 6 | 5 |
| 6 | -4 | − | `result[5]=-4` | 6 | 7 |

Resultado final: `[3,-2,1,-5,2,-4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada por `nums`
- **Espaço:** O(n) para o array de resultado (exigido pelo problema)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] rearrangeArray(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    int posIdx = 0; // próxima posição PAR livre (positivos)
    int negIdx = 1; // próxima posição ÍMPAR livre (negativos)

    for (int num : nums) {
        if (num > 0) {
            result[posIdx] = num;
            posIdx += 2;
        } else {
            result[negIdx] = num;
            negIdx += 2;
        }
    }

    return result;
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

- Avançar `posIdx`/`negIdx` de 1 em 1 em vez de 2 em 2 — como positivos só ocupam posições PARES e negativos só ÍMPARES, cada ponteiro precisa pular a posição reservada ao outro sinal.
- Achar que a ordem relativa entre números do mesmo sinal precisa de tratamento especial — ela já é preservada naturalmente, porque `nums` é processado em ordem e cada sinal usa seu próprio ponteiro independente; tentar "otimizar" ordenando por valor quebraria essa garantia.
- Tentar fazer a reorganização in-place sobrescrevendo `nums` enquanto ainda lê dele — o próprio enunciado avisa que não é necessário in-place; escrever no array de resultado separado evita sobrescrever valores ainda não processados.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | `[3,1,-2,-5,2,-4]` | `[3,-2,1,-5,2,-4]` | intercalação simples preservando ordem relativa |
| Tamanho mínimo | `[-1,1]` | `[1,-1]` | um positivo, um negativo |
| Positivos primeiro no original | `[1,2,-1,-2]` | `[1,-1,2,-2]` | ordem original dos positivos e negativos preservada |
| Negativos intercalados desde o início | `[-1,2,-3,4]` | `[2,-1,4,-3]` | positivos e negativos mantêm sua ordem relativa original |

## 🔗 Conexões

- Problemas irmãos: [0922] Sort Array By Parity II (mesma técnica de escrever em posições pares/ímpares alternadas com ponteiros dedicados), [1768] Merge Strings Alternately (mesma ideia de intercalar duas fontes numa saída única)
- No backend: distribuir itens de duas categorias numa saída intercalada preservando a ordem de chegada de cada categoria — por exemplo, intercalar transações de crédito e débito num extrato, mantendo a ordem cronológica dentro de cada tipo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
