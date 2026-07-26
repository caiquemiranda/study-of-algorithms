# [1313] Decompress Run-Length Encoded List

> 🔗 [LeetCode 1313](https://leetcode.com/problems/decompress-run-length-encoded-list/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Recebemos uma lista `nums` de inteiros representando uma lista comprimida com run-length encoding. Considere cada par adjacente de elementos `[freq, val] = [nums[2*i], nums[2*i+1]]` (com `i >= 0`). Para cada par, existem `freq` elementos com valor `val` concatenados numa sublista. Concatene todas as sublistas da esquerda para a direita para gerar a lista descomprimida.

Retorne a lista descomprimida.

**Exemplos:**
```
Input:  nums = [1,2,3,4]
Output: [2,4,4,4]
Explicação: o primeiro par [1,2] significa freq=1, val=2, gerando [2]. O segundo par [3,4] significa
freq=3, val=4, gerando [4,4,4]. Concatenando: [2] + [4,4,4] = [2,4,4,4].

Input:  nums = [1,1,2,3]
Output: [1,3,3]
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 100`, `nums.length % 2 == 0` → array sempre vem em pares [freq, val]
- `1 <= nums[i] <= 100` → frequências e valores pequenos, saída no máximo 100×50=5000 elementos

## 🧭 Como reconhecer o padrão

"Descompactar uma lista codificada por pares [frequência, valor]" é resolvido percorrendo os pares consecutivos e, para cada um, adicionando `valor` repetido `frequência` vezes na lista de saída — simulação direta, sem nenhum truque especial.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Percorrer `nums` de 2 em 2, extraindo `freq = nums[2i]` e `val = nums[2i+1]`, e adicionar `val` à saída `freq` vezes — na prática, já é essencialmente a solução ótima, pois a descompactação é inerentemente sequencial.

- Tempo: O(soma das frequências) — o tamanho da própria saída, inevitável de percorrer inteiramente · Espaço: O(soma das frequências) para a saída
- **Por que vale nomear mesmo assim:** não há uma versão "pior" real aqui; a única armadilha é confundir a ordem dos elementos do par (`[freq, val]`, frequência vem PRIMEIRO).

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Percorra `nums` com um passo de 2 em 2 (`i += 2`). Para cada par, use um loop interno para adicionar `nums[i+1]` (`val`) repetido `nums[i]` (`freq`) vezes à lista de resultado.

## 🎬 Exemplo passo a passo

`nums = [1,2,3,4]`

| Passo | i | freq=nums[i] | val=nums[i+1] | emissões | resultado parcial |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 2 | 2 | [2] |
| 2 | 2 | 3 | 4 | 4,4,4 | [2,4,4,4] |

Resultado final: `[2,4,4,4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(soma das frequências) — dominado pelo tamanho da saída
- **Espaço:** O(soma das frequências)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] decompressRLElist(int[] nums) {
    int tamanhoTotal = 0;
    for (int i = 0; i < nums.length; i += 2) {
        tamanhoTotal += nums[i]; // soma todas as frequências para saber o tamanho final
    }

    int[] resultado = new int[tamanhoTotal];
    int pos = 0;
    for (int i = 0; i < nums.length; i += 2) {
        int freq = nums[i];
        int val = nums[i + 1];
        for (int k = 0; k < freq; k++) {
            resultado[pos++] = val; // repete o valor 'freq' vezes
        }
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

- Inverter a ordem do par (tratar `nums[i]` como valor e `nums[i+1]` como frequência) — o enunciado é explícito: o par é `[freq, val]`, frequência sempre vem primeiro.
- Usar uma `List<Integer>` dinâmica sem pré-calcular o tamanho, quando um array de tamanho fixo pré-calculado é mais direto (evita overhead de boxing/unboxing e resize da lista).
- Esquecer que o índice do loop externo precisa avançar de 2 em 2 (`i += 2`), não de 1 em 1 — senão o mesmo par seria processado (ou interpretado errado) mais de uma vez.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Dois pares | `[1,2,3,4]` | [2,4,4,4] | caso padrão do enunciado |
| Frequência 1 em ambos os pares | `[1,1,2,3]` | [1,3,3] | primeiro par gera só 1 elemento |
| Um único par | `[5,7]` | [7,7,7,7,7] | menor entrada possível (2 elementos) |
| Frequência alta | `[3,1]` | [1,1,1] | mesmo valor repetido várias vezes |

## 🔗 Conexões

- Problemas irmãos: [1309] Decrypt String from Alphabet to Integer Mapping (mesma família de decodificação de formato compacto), [0443] String Compression (operação "inversa": compactar em vez de descompactar)
- No backend: descompactação de dados em formatos de serialização eficientes (ex.: run-length encoding é usado em compressão de imagens simples como BMP ou em protocolos de telemetria que enviam "valor + repetições" para economizar banda).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
