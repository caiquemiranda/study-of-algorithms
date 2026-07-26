# [1422] Maximum Score After Splitting a String

> 🔗 [LeetCode 1422](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#PrefixSum` `#Easy`

## 📜 O Problema

Dada uma string `s` de zeros e uns, retorne a pontuação máxima após dividir a string em duas substrings **não vazias** (substring esquerda e substring direita).

A pontuação de uma divisão é o número de **zeros** na substring **esquerda** mais o número de **uns** na substring **direita**.

**Exemplos:**
```
Input:  s = "011101"
Output: 5
Explicação: todas as formas de dividir s em duas substrings não vazias:
left = "0" e right = "11101", score = 1 + 4 = 5
left = "01" e right = "1101", score = 1 + 3 = 4
left = "011" e right = "101", score = 1 + 2 = 3
left = "0111" e right = "01", score = 1 + 1 = 2
left = "01110" e right = "1", score = 2 + 1 = 3

Input:  s = "00111"
Output: 5
Explicação: com left = "00" e right = "111", score máximo = 2 + 3 = 5

Input:  s = "1111"
Output: 3
```

**Restrições (e o que elas denunciam):**
- `2 <= s.length <= 500` → pequeno, O(n) ou O(n²) resolvem com folga
- string só de '0' e '1' → contagem simples, sem complicação
- "dividir em duas substrings NÃO VAZIAS" → o ponto de corte nunca pode ser antes do primeiro ou depois do último caractere

## 🧭 Como reconhecer o padrão

"Maximizar uma soma que depende de contagens em duas metades opostas de uma string, variando o ponto de corte" é resolvido com prefix sum: pré-compute o total de "1"s na string inteira, e percorra os pontos de corte possíveis mantendo a contagem de "0"s à esquerda (que cresce) e derivando a contagem de "1"s à direita (total - 1s à esquerda), sem recontar nada do zero a cada corte.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada ponto de corte possível, dividir a string em duas partes e contar do zero quantos "0"s tem a esquerda e quantos "1"s tem a direita, somando os dois.

- Tempo: O(n²) — n pontos de corte possíveis, cada um exigindo O(n) para recontar as duas partes · Espaço: O(n) para as substrings geradas
- **Por que não basta:** recontagem completa das duas metades a cada ponto de corte é redundante, já que mover o ponto de corte em 1 posição só muda a contribuição de UM caractere (ele sai da direita e entra na esquerda).

## 💡 Solução 2 — A ideia otimizada (intuição)

Pré-compute `totalUns` (quantidade de "1"s na string toda). Percorra os pontos de corte de `i=0` até `n-2` (garantindo que ambos os lados fiquem não vazios), mantendo `zerosEsquerda` (incrementado a cada '0' visto) e `unsDireita = totalUns - unsEsquerda` (derivado, sem recontagem). Calcule o score a cada ponto e mantenha o máximo.

## 🎬 Exemplo passo a passo

`s = "011101"` — `totalUns = 4` (posições 1,2,3,5)

| Passo | i (corte após este índice) | s[i] | zerosEsquerda | unsEsquerda (acumulado) | unsDireita = totalUns-unsEsquerda | score |
|---|---|---|---|---|---|---|
| 1 | 0 | '0' | 1 | 0 | 4 | 1+4=5 |
| 2 | 1 | '1' | 1 | 1 | 3 | 1+3=4 |
| 3 | 2 | '1' | 1 | 2 | 2 | 1+2=3 |
| 4 | 3 | '1' | 1 | 3 | 1 | 1+1=2 |
| 5 | 4 | '0' | 2 | 3 | 1 | 2+1=3 |

(o corte no índice 5, o último caractere, não é permitido, pois a parte direita ficaria vazia)

Máximo entre os scores calculados: `5` ✔ (no primeiro ponto de corte, left="0", right="11101")

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para pré-computar `totalUns`, outra para percorrer os cortes
- **Espaço:** O(1) extra

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxScore(String s) {
    int totalUns = 0;
    for (char c : s.toCharArray()) {
        if (c == '1') {
            totalUns++;
        }
    }

    int zerosEsquerda = 0;
    int unsEsquerda = 0;
    int melhorScore = Integer.MIN_VALUE;

    // o corte acontece DEPOIS do índice i; i vai de 0 até n-2 para garantir os dois lados não vazios
    for (int i = 0; i < s.length() - 1; i++) {
        if (s.charAt(i) == '0') {
            zerosEsquerda++;
        } else {
            unsEsquerda++;
        }
        int unsDireita = totalUns - unsEsquerda;
        melhorScore = Math.max(melhorScore, zerosEsquerda + unsDireita);
    }
    return melhorScore;
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

- Permitir o corte no último índice (`i = s.length() - 1`) — isso deixaria o lado direito vazio, violando a exigência de substrings NÃO VAZIAS; o loop precisa ir só até `s.length() - 2`.
- Recontar `zeros` e `uns` do zero para cada ponto de corte (força bruta) em vez de acumular incrementalmente — funciona, mas é O(n²) desnecessário.
- Esquecer de pré-computar `totalUns` ANTES do loop principal — sem esse total, não há como derivar `unsDireita` sem recontar a parte direita a cada iteração.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Melhor corte logo no início | `"011101"` | 5 | left="0" (1 zero), right="11101" (4 uns) |
| Corte no meio | `"00111"` | 5 | left="00" (2 zeros), right="111" (3 uns) |
| Só uns | `"1111"` | 3 | melhor corte deixa 3 uns de um lado, 0 zeros do outro |
| Tamanho mínimo | `"01"` | 2 | único corte possível: left="0" (1), right="1" (1) |

## 🔗 Conexões

- Problemas irmãos: [0724] Find Pivot Index (mesma técnica de prefix sum com total pré-computado), [0053] Maximum Subarray (mesmo domínio de maximizar uma métrica variando um ponto de corte/janela)
- No backend: otimização de pontos de corte em séries de dados binários (ex.: dividir um turno de trabalho em dois períodos para maximizar uma métrica de eficiência combinada dos dois lados).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
