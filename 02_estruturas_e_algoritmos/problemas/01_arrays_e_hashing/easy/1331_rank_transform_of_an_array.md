# [1331] Rank Transform of an Array

> 🔗 [LeetCode 1331](https://leetcode.com/problems/rank-transform-of-an-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Sorting` `#Easy`

## 📜 O Problema

Dado um array de inteiros `arr`, substitua cada elemento pelo seu rank. O rank representa o quão grande é o elemento, seguindo as regras:
- O rank é um inteiro começando de 1.
- Quanto maior o elemento, maior o rank. Se dois elementos são iguais, seu rank deve ser o mesmo.
- O rank deve ser o menor possível.

**Exemplos:**
```
Input:  arr = [40,10,20,30]
Output: [4,1,2,3]
Explicação: 40 é o maior. 10 é o menor. 20 é o segundo menor. 30 é o terceiro menor.

Input:  arr = [100,100,100]
Output: [1,1,1]
Explicação: elementos iguais compartilham o mesmo rank.

Input:  arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
```

**Restrições (e o que elas denunciam):**
- `0 <= arr.length <= 10^5` → precisa O(n log n), array pode ser vazio
- `-10^9 <= arr[i] <= 10^9` → valores muito grandes e possivelmente negativos, não cabe em array de contagem fixo — precisa de hash map + sort

## 🧭 Como reconhecer o padrão

"Substitua cada valor pelo seu rank (posição relativa entre os valores distintos, sem 'buracos')" é resolvido ordenando uma CÓPIA dos valores distintos, atribuindo ranks 1, 2, 3... a cada valor distinto na ordem, e depois usando um hash map para "traduzir" cada elemento do array original para o rank correspondente.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada elemento `arr[i]`, contar quantos valores DISTINTOS no array são menores ou iguais a ele.

- Tempo: O(n²) — para cada elemento, uma varredura completa do array · Espaço: O(n)
- **Por que não basta:** recalcula a mesma informação de "quantos valores distintos são menores que X" repetidamente, quando ordenar uma vez já revela essa relação para TODOS os valores de uma vez.

## 💡 Solução 2 — A ideia otimizada (intuição)

Copie os valores para um novo array e ordene. Atribua a cada valor distinto seu rank (posição na ordem, começando em 1) num hash map `valor → rank`. Percorra o array original, substituindo cada elemento pelo rank correspondente no mapa.

## 🎬 Exemplo passo a passo

`arr = [40,10,20,30]` — valores distintos ordenados: `[10,20,30,40]`, mapa de rank: `{10:1, 20:2, 30:3, 40:4}`

| Passo | i | arr[i] | rank[arr[i]] |
|---|---|---|---|
| 1 | 0 | 40 | 4 |
| 2 | 1 | 10 | 1 |
| 3 | 2 | 20 | 2 |
| 4 | 3 | 30 | 3 |

Resultado final: `[4,1,2,3]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n log n) — dominado pela ordenação dos valores
- **Espaço:** O(n) — para o hash map e o array de valores distintos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] arrayRankTransform(int[] arr) {
    int[] ordenado = arr.clone();
    Arrays.sort(ordenado);

    Map<Integer, Integer> rankPorValor = new HashMap<>();
    int rankAtual = 0;
    for (int valor : ordenado) {
        if (!rankPorValor.containsKey(valor)) {
            rankAtual++;
            rankPorValor.put(valor, rankAtual); // só atribui um novo rank a valores ainda não vistos
        }
    }

    int[] resultado = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
        resultado[i] = rankPorValor.get(arr[i]);
    }
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

- Atribuir um rank novo para CADA elemento ordenado, mesmo quando repetido — sem a checagem `containsKey`, elementos iguais receberiam ranks diferentes, violando "se dois elementos são iguais, seu rank deve ser igual".
- Ordenar o array ORIGINAL diretamente (em vez de uma cópia) — perderia a ordem original necessária para montar o resultado na posição correta.
- Não tratar o array vazio (`arr.length == 0`) — o enunciado permite essa entrada; o código já lida com isso naturalmente (os loops simplesmente não executam), mas vale ter o caso em mente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ranks distintos | `[40,10,20,30]` | [4,1,2,3] | caso padrão do enunciado |
| Todos iguais | `[100,100,100]` | [1,1,1] | elementos iguais compartilham o mesmo rank |
| Vários valores repetidos | `[37,12,28,9,100,56,80,5,12]` | [5,3,4,2,8,6,7,1,3] | "12" aparece duas vezes e recebe o mesmo rank (3) nas duas ocorrências |
| Array vazio | `[]` | [] | caso de borda permitido pela restrição |

## 🔗 Conexões

- Problemas irmãos: [1365] How Many Numbers Are Smaller Than the Current Number (mesma ideia de "posição relativa" entre elementos, mas com contagem em vez de rank sem buracos), [0347] Top K Frequent Elements (mesma técnica de combinar ordenação com hash map)
- No backend: normalização de dados para machine learning (ex.: converter valores contínuos em ranks ordinais antes de treinar um modelo), ou geração de rankings de competição onde empates compartilham a mesma posição.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
