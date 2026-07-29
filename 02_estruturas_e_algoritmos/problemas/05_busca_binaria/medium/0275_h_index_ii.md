# [0275] H-Index II

> 🔗 [LeetCode 275](https://leetcode.com/problems/h-index-ii/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Você recebe `citations`, um array **ordenado ascendente** onde `citations[i]` é o número de citações do `i`-ésimo artigo de um pesquisador. Retorne o **h-index**: o maior valor `h` tal que o pesquisador tem **pelo menos `h` artigos** com **pelo menos `h` citações** cada.

**Exemplos:**
```
Input:  citations = [0,1,3,5,6]    Output: 3
        (3 artigos com >= 3 citações cada: os valores 3, 5, 6; os outros dois têm <= 3)
Input:  citations = [1,2,100]      Output: 2
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^5` → O(n) passaria, mas o enunciado exige explicitamente tempo logarítmico
- "You must write an algorithm that runs in logarithmic time" → busca binária obrigatória — este é o "follow-up" direto do H-Index original (LC 274, que resolve em O(n) com array não ordenado)
- "citations is sorted in ascending order" → é essa ordenação que habilita a versão O(log n): para qualquer índice `i`, o número de artigos com citações `>= citations[i]` é sempre `n - i` (todos os artigos a partir de `i`, já que o array é ascendente)

## 🧭 Como reconhecer o padrão

Para cada índice `i` do array ordenado, `n - i` é exatamente "quantos artigos têm pelo menos `citations[i]` citações". A pergunta "existe um `h` que se auto-sustenta" (h artigos com pelo menos h citações) vira: **ache o menor índice `i` onde `citations[i] >= n - i`** — porque, como `citations` só cresce, esse `i` marca o ponto de virada entre "poucos artigos citados o bastante" e "artigos citados o bastante". A resposta final é `n - i` nesse ponto.

## 🐢 Solução 1 — Força bruta

Para cada candidato `h` de `n` até `0`, contar quantos elementos de `citations` são `>= h`; retornar o primeiro `h` que se auto-sustenta (ou percorrer o array uma vez comparando `citations[i]` com `n - i`, que já é O(n)).

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** o enunciado exige tempo logarítmico — e ignora que a condição `citations[i] >= n - i` é monotônica ao longo do array ordenado (falsa nos índices baixos, verdadeira nos altos), o convite direto para busca binária pela fronteira.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça busca binária pelo **menor índice `mid`** onde `citations[mid] >= n - mid`:
- Se essa condição for verdadeira em `mid`, ele é um candidato válido (`h = n - mid`) — mas talvez exista um índice ainda menor que também sirva (dando um `h` ainda maior) → guarda o candidato e busca à **esquerda**.
- Se for falsa, esse índice tem citações insuficientes para o número de artigos que o sustentariam → busca à **direita**.

O melhor candidato guardado ao final é o h-index.

## 🎬 Exemplo passo a passo

`citations = [0, 1, 3, 5, 6]` (n = 5)

| Passo | left | mid | right | citations[mid] vs n-mid | Decisão |
|---|---|---|---|---|---|
| 1 | 0 | 2 (val 3) | 4 | 3 >= 5-2=3 → candidato válido (h=3) | guarda h=3, `right = 1` |
| 2 | 0 | 0 (val 0) | 1 | 0 >= 5-0=5? não | `left = 1` |
| 3 | 1 | 1 (val 1) | 1 | 1 >= 5-1=4? não | `left = 2` |
| 4 | 2 | — | 1 | `left > right` → fim | melhor candidato: h=3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do espaço de busca
- **Espaço:** O(1) — só ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int hIndex(int[] citations) {
    int n = citations.length;
    int left = 0, right = n - 1;
    int melhorH = 0;                     // se nenhum índice satisfizer, h-index é 0

    while (left <= right) {
        int mid = left + (right - left) / 2;
        int artigosComPeloMenos = n - mid;   // quantos artigos têm citações >= citations[mid]

        if (citations[mid] >= artigosComPeloMenos) {
            melhorH = artigosComPeloMenos;   // candidato válido: h = n - mid
            right = mid - 1;                 // tenta achar um índice ainda menor (h ainda maior)
        } else {
            left = mid + 1;                  // citations[mid] insuficiente para sustentar h = n-mid
        }
    }
    return melhorH;
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

- **Confundir `n - mid` com `n - mid - 1`**: `n - mid` conta corretamente os artigos do índice `mid` até o fim (inclusive), que são `n - mid` elementos — um erro de off-by-one aqui desloca toda a resposta.
- **Buscar o maior índice em vez do menor**: queremos o índice mais à **esquerda** que satisfaz a condição, porque índices menores correspondem a `h` **maiores** (`n - mid` cresce conforme `mid` diminui) — inverter a direção da busca dá o `h` errado.
- **Esquecer o caso h-index = 0**: se nenhum artigo tiver citações suficientes (ex.: `citations = [0,0,0]`), a resposta é `0` — o valor inicial de `melhorH` já cobre isso, mas é bom testar explicitamente.
- **Aplicar a versão O(n) do H-Index original (LC 274) aqui**: funciona corretamente, mas não atende ao requisito de tempo logarítmico deste problema — a diferença entre os dois é exatamente a ordenação do array e a exigência de complexidade.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhuma citação | `citations=[0,0,0]` | 0 | h-index mínimo |
| Um artigo só | `citations=[100]` | 1 | borda mínima, h-index é 1 (1 artigo com >=1 citação) |
| H-index é o próprio n | `citations=[5,6,7,8,9]` | 5 | todos os 5 artigos têm pelo menos 5 citações |
| Citação alta isolada | `citations=[1,2,100]` | 2 | trace do segundo exemplo, só 2 artigos sustentam h=2 |
| Exemplo do enunciado | `citations=[0,1,3,5,6]` | 3 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **H-Index (LC 274)** (o mesmo problema sem a garantia de ordenação, resolvido em O(n)), **[2529] Maximum Count of Positive Integer and Negative Integer** (busca binária por fronteira monotônica em array ordenado), **[1608] Special Array With X Elements Greater Than or Equal X** (mesma estrutura: contar elementos que "sustentam" um valor de índice)
- No backend: calcular métricas de "auto-sustentação" (ex.: quantos servidores de um cluster suportam pelo menos X% da carga, ou o "índice de qualidade" mínimo garantido por pelo menos N itens de um catálogo) usa a mesma técnica de busca binária sobre uma condição de contagem monotônica.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
