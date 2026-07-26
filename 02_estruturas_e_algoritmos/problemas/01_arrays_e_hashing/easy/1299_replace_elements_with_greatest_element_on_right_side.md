# [1299] Replace Elements with Greatest Element on Right Side

> 🔗 [LeetCode 1299](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array `arr`, substitua cada elemento pelo maior elemento entre os elementos à sua direita, e substitua o último elemento por `-1`. Depois disso, retorne o array.

**Exemplos:**
```
Input:  arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explicação:
- índice 0 --> o maior à direita é o índice 1 (18).
- índice 1 --> o maior à direita é o índice 4 (6).
- índice 2 --> o maior à direita é o índice 4 (6).
- índice 3 --> o maior à direita é o índice 4 (6).
- índice 4 --> o maior à direita é o índice 5 (1).
- índice 5 --> não há elementos à direita, colocamos -1.

Input:  arr = [400]
Output: [-1]
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 10^4` → O(n) esperado
- `1 <= arr[i] <= 10^5` → valores positivos, sem complicação de sinal para o "-1" sentinela do último elemento

## 🧭 Como reconhecer o padrão

"Substitua cada elemento pelo máximo à direita dele" é resolvido percorrendo o array DE TRÁS PARA FRENTE, mantendo um "máximo visto até agora" que é atualizado DEPOIS de escrever o valor atual — assim cada posição usa o máximo dos elementos que ainda não foram sobrescritos.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, percorrer todo o subarray à direita (`i+1` até o fim) procurando o maior valor, e substituir `arr[i]` por esse máximo.

- Tempo: O(n²) — para cada posição, uma varredura completa do restante do array · Espaço: O(1) extra
- **Por que não basta:** recalcula o máximo do zero para cada posição, quando o máximo à direita de `i` é só `max(arr[i+1], máximo à direita de i+1)` — informação que já foi calculada ao processar a posição seguinte.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array de trás para frente com uma variável `maiorAteAgora` (inicializada em `-1`, o valor sentinela do último elemento). Para cada posição `i`, salve `arr[i]` temporariamente, sobrescreva `arr[i]` com `maiorAteAgora`, e então atualize `maiorAteAgora = max(maiorAteAgora, valor original salvo)`.

## 🎬 Exemplo passo a passo

`arr = [17,18,5,4,6,1]`

| Passo | i | arr[i] original | maiorAteAgora (antes) | novo arr[i] | maiorAteAgora (depois) |
|---|---|---|---|---|---|
| 1 | 5 | 1 | -1 | -1 | max(-1,1)=1 |
| 2 | 4 | 6 | 1 | 1 | max(1,6)=6 |
| 3 | 3 | 4 | 6 | 6 | max(6,4)=6 |
| 4 | 2 | 5 | 6 | 6 | max(6,5)=6 |
| 5 | 1 | 18 | 6 | 6 | max(6,18)=18 |
| 6 | 0 | 17 | 18 | 18 | max(18,17)=18 |

Array final: `[18,6,6,6,1,-1]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada de trás para frente
- **Espaço:** O(1) extra (in-place)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] replaceElements(int[] arr) {
    int maiorAteAgora = -1;
    for (int i = arr.length - 1; i >= 0; i--) {
        int original = arr[i];
        arr[i] = maiorAteAgora;                       // escreve o máximo já visto à direita
        maiorAteAgora = Math.max(maiorAteAgora, original); // atualiza DEPOIS de escrever, com o valor original
    }
    return arr;
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

- Atualizar `maiorAteAgora` ANTES de escrever `arr[i]` — isso faria o elemento incluir a si mesmo no cálculo do "máximo à direita", quando o enunciado pede só os elementos estritamente à direita.
- Esquecer de salvar o valor original de `arr[i]` antes de sobrescrevê-lo — como a substituição é in-place, sobrescrever primeiro perderia o valor necessário para atualizar `maiorAteAgora` depois.
- Inicializar `maiorAteAgora` como `0` em vez de `-1` — o enunciado exige explicitamente que o último elemento vire `-1`, não `0`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | `[17,18,5,4,6,1]` | [18,6,6,6,1,-1] | cada posição reflete o máximo estritamente à direita |
| Um único elemento | `[400]` | [-1] | não há elementos à direita, vira -1 direto |
| Array crescente | `[1,2,3,4]` | [4,4,4,-1] | cada posição reflete o maior elemento que ainda vem depois |
| Array decrescente | `[4,3,2,1]` | [3,2,1,-1] | máximo à direita é sempre o próximo elemento |

## 🔗 Conexões

- Problemas irmãos: [0238] Product of Array Except Self (mesma técnica de passada da direita para a esquerda mantendo um acumulador), [0739] Daily Temperatures (também processa de trás para frente, mas com uma pilha monotônica em vez de um único máximo)
- No backend: cálculo de "melhor oferta futura" em séries de preços (ex.: para cada dia, qual o maior preço de venda disponível em dias futuros) — a mesma passada reversa com acumulador aparece em análises financeiras simples.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
