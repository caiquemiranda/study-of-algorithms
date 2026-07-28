# [2024] Maximize the Confusion of an Exam

> 🔗 [LeetCode 2024](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Um professor escreve uma prova de `n` questões verdadeiro/falso (`'T'`/`'F'`) e quer maximizar o número de questões **consecutivas** com a **mesma** resposta. Dada `answerKey` e um inteiro `k` (o número máximo de vezes que você pode trocar a resposta de qualquer questão), retorne o número máximo de `'T'`s ou `'F'`s consecutivos possível.

**Exemplos:**
```
Input:  answerKey = "TTFF", k = 2
Output: 4
Explicação: trocar os dois 'F's por 'T's dá "TTTT".

Input:  answerKey = "TFFT", k = 1
Output: 3

Input:  answerKey = "TTFTTFTT", k = 1
Output: 5
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 5 * 10^4` → O(n²) força bruta é arriscado; O(n) é o esperado
- `1 <= k <= n` → `k` pode cobrir a string inteira

## 🧭 Como reconhecer o padrão

Esse é EXATAMENTE o mesmo problema de [0424] Longest Repeating Character Replacement, com um alfabeto reduzido a 2 símbolos (`T`/`F`) em vez de 26 letras: maior janela onde `tamanho - contagem_do_caractere_mais_comum <= k`. Como a resposta pode ser de 'T's ou de 'F's, roda-se a mesma lógica duas vezes.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, contar a frequência de 'T' e 'F' na janela e checar se `tamanho - max(freqT,freqF) <= k`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** revalida a contagem do zero a cada substring candidata, mesmo quando ela é apenas a anterior estendida em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Rode a técnica de [0424] duas vezes: uma maximizando a contagem de 'T' na janela (`maxCount`), outra maximizando 'F'. Em cada passada, expanda `right`; se `tamanho - maxCount > k`, encolha `left` em 1 (sem recalcular `maxCount` pra baixo, pois isso é seguro). O resultado final é o maior entre as duas passadas.

## 🎬 Exemplo passo a passo

`answerKey = "TTFF"`, `k = 2` (passada maximizando 'T')

| right | char | freqT | maxCount | len-maxCount | ação | comprimento | melhor |
|---|---|---|---|---|---|---|---|
| 0 | T | 1 | 1 | 0 | ok | 1 | 1 |
| 1 | T | 2 | 2 | 0 | ok | 2 | 2 |
| 2 | F | 2 | 2 | 1 | ok | 3 | 3 |
| 3 | F | 2 | 2 | 2 | ok | 4 | 4 |

Resultado final (maximizando 'T'; a passada para 'F' não supera este): `4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas O(n)
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxConsecutiveAnswers(String answerKey, int k) {
    return Math.max(maxWindow(answerKey, k, 'T'), maxWindow(answerKey, k, 'F'));
}

private int maxWindow(String answerKey, int k, char target) {
    int left = 0;
    int maxCount = 0;
    int best = 0;

    for (int right = 0; right < answerKey.length(); right++) {
        if (answerKey.charAt(right) == target) {
            maxCount++;
        }

        if (right - left + 1 - maxCount > k) {
            if (answerKey.charAt(left) == target) {
                maxCount--;
            }
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
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

- É preciso rodar a mesma lógica DUAS vezes — uma maximizando sequências de 'T', outra de 'F' — porque a melhor janela pode ser de qualquer um dos dois tipos; esquecer uma das duas passadas perde metade dos casos.
- Esse é EXATAMENTE o mesmo algoritmo de [0424] Longest Repeating Character Replacement, só que aplicado a um alfabeto de 2 símbolos em vez de 26 — reconhecer essa equivalência evita reinventar a lógica do zero.
- `maxCount` não é recalculado para baixo ao encolher a janela (mesma pegadinha de 424) — isso é intencional e seguro, pois o objetivo é só o maior comprimento válido.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k cobre a string inteira | `"TTFF"`, `k=2` | 4 | dá pra uniformizar tudo pra 'T' (ou 'F') |
| k=0 (sem trocas) | `"TFFT"`, `k=0` | 2 | sem trocas, a maior sequência já repetida tem tamanho 2 ("FF") |
| Já uniforme | `"TTTT"`, `k=1` | 4 | nenhuma troca necessária |
| Exemplo do enunciado | `"TTFTTFTT"`, `k=1` | 5 | trocar um 'F' cria uma sequência de 5 'T's |

## 🔗 Conexões

- Problemas irmãos: [0424] Longest Repeating Character Replacement (praticamente o mesmo problema, com alfabeto reduzido a 2 símbolos), [1004] Max Consecutive Ones III (mesma técnica de janela variável com contagem de "exceções" permitidas)
- No backend: calcular o maior trecho de um log binário (sucesso/falha) que pode ser "normalizado" para um único valor dentro de um orçamento limitado de correções manuais.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
