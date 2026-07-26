# [0697] Degree of an Array

> 🔗 [LeetCode 697](https://leetcode.com/problems/degree-of-an-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Easy`

## 📜 O Problema

Dado um array não vazio de inteiros não negativos `nums`, o **grau** desse array é definido como a frequência máxima de qualquer um dos seus elementos. Sua tarefa é encontrar o menor comprimento possível de um subarray (contíguo) de `nums` que tenha o mesmo grau do array inteiro.

**Exemplos:**
```
Input:  nums = [1,2,2,3,1]
Output: 2
Explicação: o array tem grau 2, pois tanto 1 quanto 2 aparecem duas vezes.
Dos subarrays com o mesmo grau: [1,2,2,3,1], [1,2,2,3], [2,2,3,1], [1,2,2], [2,2,3], [2,2]
O menor comprimento é 2.

Input:  nums = [1,2,2,3,1,4,2]
Output: 6
Explicação: o grau é 3, porque o elemento 2 se repete 3 vezes.
Então [2,2,3,1,4,2] é o menor subarray, retornando 6.
```

**Restrições (e o que elas denunciam):**
- `nums.length` entre 1 e 50.000 → precisa O(n), não O(n²) ou pior
- `nums[i]` entre 0 e 49.999 → não negativo, poderia usar array de contagem fixo, mas um mapa de hash funciona igual e é mais direto de explicar

## 🧭 Como reconhecer o padrão

"Subarray mais curto com a mesma propriedade de frequência máxima do array inteiro" pede que, para o(s) elemento(s) mais frequente(s), você saiba exatamente onde é a primeira e a última ocorrência — isso é sempre resolvido guardando, para cada valor, `primeira_ocorrencia`, `ultima_ocorrencia` e `contagem` num único passe.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de índices `(i, j)` com `i <= j`, verificar se o subarray `nums[i..j]` tem o mesmo grau (mesma frequência máxima) que o array inteiro, guardando o menor comprimento válido.

- Tempo: O(n³) — O(n²) pares de índices, cada um exigindo O(n) para calcular as frequências do subarray · Espaço: O(n) para as contagens do subarray
- **Por que não basta:** recalcula frequências do zero para cada subarray candidato, quando a informação necessária (primeira/última ocorrência de cada valor) pode ser coletada em uma única passada pelo array inteiro.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma passada guardando três mapas: `primeiraOcorrencia[valor]`, `ultimaOcorrencia[valor]`, `frequencia[valor]`. Depois, encontre o `grau` (frequência máxima) e, entre todos os valores com essa frequência máxima, retorne o menor `ultimaOcorrencia - primeiraOcorrencia + 1`.

## 🎬 Exemplo passo a passo

`nums = [1,2,2,3,1]`

| Passo | i | valor | primeira[valor] | ultima[valor] | frequencia[valor] |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 1 |
| 2 | 1 | 2 | 1 | 1 | 1 |
| 3 | 2 | 2 | 1 (mantém) | 2 | 2 |
| 4 | 3 | 3 | 3 | 3 | 1 |
| 5 | 4 | 1 | 0 (mantém) | 4 | 2 |

`grau = max(frequencia) = 2` (valores 1 e 2 empatam). Comprimento(1) = 4-0+1 = 5. Comprimento(2) = 2-1+1 = 2. Menor entre os que têm grau máximo: **2** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para coletar + uma passada para achar o mínimo entre os candidatos
- **Espaço:** O(n) — para os três mapas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findShortestSubArray(int[] nums) {
    Map<Integer, Integer> primeira = new HashMap<>();
    Map<Integer, Integer> ultima = new HashMap<>();
    Map<Integer, Integer> frequencia = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
        int valor = nums[i];
        primeira.putIfAbsent(valor, i);              // só grava na primeira vez que aparece
        ultima.put(valor, i);                          // sempre sobrescreve com a ocorrência mais recente
        frequencia.merge(valor, 1, Integer::sum);       // incrementa a contagem
    }

    int grau = Collections.max(frequencia.values());
    int menorComprimento = nums.length;

    for (int valor : frequencia.keySet()) {
        if (frequencia.get(valor) == grau) {
            int comprimento = ultima.get(valor) - primeira.get(valor) + 1;
            menorComprimento = Math.min(menorComprimento, comprimento);
        }
    }
    return menorComprimento;
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

- Usar `put` em vez de `putIfAbsent` para `primeira` — sobrescreveria com a última ocorrência em vez de manter a primeira, quebrando o cálculo do comprimento.
- Esquecer que pode haver EMPATE no grau (múltiplos valores com a mesma frequência máxima) — precisa checar todos eles e pegar o menor comprimento entre todos, não só o primeiro encontrado.
- Calcular o comprimento como `ultima - primeira` sem o `+ 1` — erro clássico de off-by-one ao converter índices em tamanho de intervalo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Empate no grau | `[1,2,2,3,1]` | 2 | valores 1 e 2 empatam com frequência 2, mas o subarray de 2 é mais curto |
| Grau único e mais espalhado | `[1,2,2,3,1,4,2]` | 6 | valor 2 domina com frequência 3, subarray precisa cobrir do índice 1 ao 6 |
| Array de um elemento | `[5]` | 1 | grau 1, subarray mínimo é o próprio elemento |
| Todos elementos distintos | `[1,2,3,4]` | 1 | grau 1, qualquer elemento sozinho já serve |

## 🔗 Conexões

- Problemas irmãos: [0448] Find All Numbers Disappeared in an Array (mesma família de aproveitar índices/posições), [0169] Majority Element (também gira em torno de "qual elemento é mais frequente")
- No backend: análise de logs para achar a janela mínima de tempo que contém todas as ocorrências do evento mais frequente (ex.: identificar o menor intervalo de tempo em que um erro recorrente se concentrou).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
