# [1394] Find Lucky Integer in an Array

> 🔗 [LeetCode 1394](https://leetcode.com/problems/find-lucky-integer-in-an-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Counting` `#Easy`

## 📜 O Problema

Dado um array de inteiros `arr`, um **inteiro sortudo** é um inteiro cuja frequência no array é igual ao seu próprio valor. Retorne o maior **inteiro sortudo** do array. Se não existir nenhum, retorne `-1`.

**Exemplos:**
```
Input:  arr = [2,2,3,4]
Output: 2
Explicação: o único número sortudo é 2, porque frequência[2] == 2.

Input:  arr = [1,2,2,3,3,3]
Output: 3
Explicação: 1, 2 e 3 são todos sortudos, retorne o maior deles.

Input:  arr = [2,2,2,3,3]
Output: -1
Explicação: não há números sortudos.
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 500`, `1 <= arr[i] <= 500` → pequeno, O(n) resolve com folga
- "lucky" = frequência do valor é IGUAL ao próprio valor → precisa contar frequências e comparar cada valor com sua própria contagem
- pode não existir nenhum lucky integer → precisa tratar o caso de retorno -1

## 🧭 Como reconhecer o padrão

"Um valor cuja frequência é igual a ele mesmo" é sempre resolvido contando frequências num hash map, e depois percorrendo as chaves do mapa verificando `chave == frequencia[chave]`, mantendo a maior chave que satisfizer.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada elemento distinto do array, contar manualmente (com um loop aninhado) quantas vezes ele aparece, e comparar essa contagem com o próprio valor.

- Tempo: O(n²) — para cada valor distinto, uma varredura completa do array para contar · Espaço: O(1) extra
- **Por que não basta:** recalcula a mesma contagem repetidamente para valores distintos, quando um hash map de frequência calcula tudo em uma única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um hash map `valor → frequência` percorrendo o array uma vez. Percorra as chaves do mapa; para cada uma onde `chave == frequencia[chave]`, atualize a resposta com o MAIOR valor de chave encontrado (ou `-1` se nenhuma satisfizer).

## 🎬 Exemplo passo a passo

`arr = [1,2,2,3,3,3]` — frequência: `{1:1, 2:2, 3:3}`

| Passo | valor | frequencia[valor] | valor == frequencia[valor]? | maiorLucky até agora |
|---|---|---|---|---|
| 1 | 1 | 1 | sim (1==1) | 1 |
| 2 | 2 | 2 | sim (2==2) | 2 |
| 3 | 3 | 3 | sim (3==3) | 3 |

Resultado final: `3` ✔ (o maior entre os lucky integers encontrados)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para contar + uma passada sobre as chaves
- **Espaço:** O(k), k = valores distintos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findLucky(int[] arr) {
    Map<Integer, Integer> frequencia = new HashMap<>();
    for (int num : arr) {
        frequencia.merge(num, 1, Integer::sum);
    }

    int maiorLucky = -1;
    for (Map.Entry<Integer, Integer> entry : frequencia.entrySet()) {
        int valor = entry.getKey();
        int freq = entry.getValue();
        if (valor == freq) {
            maiorLucky = Math.max(maiorLucky, valor); // mantém o maior lucky integer encontrado
        }
    }
    return maiorLucky;
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

- Retornar o PRIMEIRO lucky integer encontrado em vez do MAIOR — a ordem de iteração de um `HashMap` não é garantida, então "primeiro encontrado" pode não ser o maior; é preciso comparar explicitamente com `Math.max`.
- Confundir "frequência do valor" com "o próprio valor como índice" — não é sobre POSIÇÃO no array, é sobre quantas vezes aquele número aparece.
- Esquecer de inicializar a resposta como `-1` — se nenhum valor satisfizer `valor == frequência`, o enunciado exige retornar `-1` explicitamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único lucky integer | `[2,2,3,4]` | 2 | só o valor 2 tem frequência igual a ele mesmo |
| Múltiplos lucky integers | `[1,2,2,3,3,3]` | 3 | 1, 2 e 3 são todos lucky, retorna o maior |
| Nenhum lucky integer | `[2,2,2,3,3]` | -1 | 2 aparece 3 vezes (não 2), 3 aparece 2 vezes (não 3) |
| Array de um elemento | `[1]` | 1 | frequência de 1 é 1, bate exatamente |

## 🔗 Conexões

- Problemas irmãos: [1207] Unique Number of Occurrences (mesma base de hash map de frequência), [0169] Majority Element (mesmo domínio de comparar frequência com um critério específico)
- No backend: detecção de "coincidências estruturais" em dados categorizados (ex.: um código de erro que ocorre exatamente N vezes onde N é parte do próprio código, sinalizando um padrão suspeito digno de investigação).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
