# [0169] Majority Element

> 🔗 [LeetCode 169](https://leetcode.com/problems/majority-element/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#HashTable` `#Easy`

## 📜 O Problema

Dado um array `nums` de tamanho `n`, retorne **o elemento majoritário**: aquele que aparece mais de `⌊n / 2⌋` vezes. Pode assumir que ele sempre existe.

**Exemplos:**
```
Input:  nums = [3,2,3]              Output: 3
Input:  nums = [2,2,1,1,1,2,2]      Output: 2
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 5 * 10^4` → O(n log n) (ordenar) já passaria, mas o **follow-up pede O(n) tempo e O(1) espaço** — isso aponta direto para o Voto de Boyer-Moore
- "é garantido que o elemento majoritário existe" → você não precisa validar a resposta no final, só encontrá-la
- Majoritário = mais que **metade** dos elementos → essa garantia é o que torna o algoritmo de votação seguro

## 🧭 Como reconhecer o padrão

"Contar ocorrências de cada elemento" grita hash map de frequência — mas quando a pergunta é especificamente sobre **maioria absoluta (> n/2)** e o enunciado cobra O(1) de espaço, é o gatilho para o algoritmo de **votação de Boyer-Moore**: candidato + contador que se cancelam.

## 🐢 Solução 1 — Força bruta

Para cada elemento candidato, percorrer o array inteiro contando quantas vezes ele aparece; se passar de `n/2`, é a resposta.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** com n = 50.000, são até 2,5 bilhões de comparações — inviável. E ainda existe a alternativa intermediária de hash map de frequência, O(n) tempo mas O(n) espaço — o follow-up pede melhor que isso.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pense em uma eleição: cada vez que você vê o candidato atual, ele ganha +1 voto; cada vez que vê outro diferente, ele perde 1 voto — os votos se **cancelam par a par**. Se o contador zera, troque de candidato.

Como o majoritário aparece mais que todo o resto somado, ele nunca pode ser completamente cancelado — ele sobrevive como candidato final, mesmo que o contador oscile no meio do caminho.

## 🎬 Exemplo passo a passo

`nums = [2, 2, 1, 1, 1, 2, 2]`

| Passo | num | candidato antes | contador antes | Ação | candidato depois | contador depois |
|---|---|---|---|---|---|---|
| 1 | 2 | — | 0 | contador=0 → troca candidato | 2 | 1 |
| 2 | 2 | 2 | 1 | igual ao candidato: +1 | 2 | 2 |
| 3 | 1 | 2 | 2 | diferente: -1 | 2 | 1 |
| 4 | 1 | 2 | 1 | diferente: -1 | 2 | 0 |
| 5 | 1 | 2 | 0 | contador=0 → troca candidato | 1 | 1 |
| 6 | 2 | 1 | 1 | diferente: -1 | 1 | 0 |
| 7 | 2 | 1 | 0 | contador=0 → troca candidato | 2 | 1 |

Resultado final: candidato = **2** ✔ (2 aparece 4 vezes em 7 elementos — é maioria)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelo array
- **Espaço:** O(1) — apenas duas variáveis (candidato e contador)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int majorityElement(int[] nums) {
    int candidato = 0;
    int contador = 0;

    for (int n : nums) {
        if (contador == 0) {
            // sem "crédito" de votos: o próximo elemento vira o novo candidato
            candidato = n;
        }
        // vota +1 se concorda com o candidato atual, -1 se discorda
        contador += (n == candidato) ? 1 : -1;
    }

    // não precisamos verificar o resultado: o enunciado GARANTE que existe maioria
    return candidato;
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

- Achar que o **candidato durante o processo** já é a resposta a qualquer momento — só o candidato **final**, após percorrer tudo, é garantido correto.
- Esquecer que o algoritmo **depende da garantia do enunciado** (maioria existe); sem essa garantia, seria preciso uma segunda passada para confirmar a contagem.
- **Java**: comparar `Integer` com `==` funciona aqui porque `nums` é `int[]` primitivo — cuidado se o array fosse `Integer[]` (autoboxing pode comparar referência em vez de valor para números > 127).
- Confundir "maioria" (> n/2) com "moda" (o mais frequente, sem garantia de ultrapassar a metade) — são problemas diferentes (a moda sem garantia de maioria não tem solução O(1) espaço garantida).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um elemento só | `[7]` | 7 | borda mínima, sempre maioria |
| Maioria no início | `[5,5,5,1,2]` | 5 | candidato certo desde cedo |
| Maioria intercalada | `[1,2,1,2,1]` | 1 | testa as trocas de candidato no meio |
| Exatamente na borda | `[1,1,2,2,1]` | 1 | n=5, precisa aparecer > 2 vezes (aparece 3) |

## 🔗 Conexões

- Problemas irmãos: **[0229] Majority Element II** (agora com até 2 majoritários, > n/3 — exige 2 candidatos e 2 contadores), **[0refresh] Boyer-Moore** é a mesma ideia usada em streaming de dados
- No backend: detectar o "valor dominante" em um stream de eventos (ex.: qual código de erro domina os últimos N logs) sem guardar histograma completo é aplicação direta deste algoritmo com memória O(1).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
