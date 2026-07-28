# [1813] Sentence Similarity III

> 🔗 [LeetCode 1813](https://leetcode.com/problems/sentence-similarity-iii/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#String` `#Medium`

## 📜 O Problema

Dadas duas sentenças (palavras separadas por um único espaço), elas são **similares** se for possível inserir uma sentença arbitrária (possivelmente vazia) dentro de uma delas para torná-las iguais — a inserção precisa ficar separada das palavras existentes por espaço. Retorne se as sentenças são similares.

**Exemplos:**
```
Input:  sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explicação: insere "name is" entre "My" e "Haley" em sentence2.

Input:  sentence1 = "of", sentence2 = "A lot of words"
Output: false

Input:  sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explicação: insere "right now" no final de sentence2.
```

**Restrições (e o que elas denunciam):**
- `1 <= sentence1.length, sentence2.length <= 100` → entrada pequena, O(n) já é natural
- A inserção precisa ser um bloco **contíguo** de palavras → o que sobra fora desse bloco tem que ser exatamente um prefixo em comum e um sufixo em comum entre as duas sentenças
- A sentença inserida pode ser **vazia** → sentenças idênticas também contam como similares

## 🧭 Como reconhecer o padrão

"Verificar se uma sequência é a outra com um bloco inserido no meio" é resolvido com dois ponteiros convergindo de fora pra dentro: um conta quantas palavras batem a partir do **início** das duas sentenças (prefixo comum), outro conta quantas batem a partir do **fim** (sufixo comum). Se a soma dessas duas contagens cobrir todas as palavras da sentença mais curta, o "buraco" no meio da mais longa é exatamente a sentença inserida.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar todas as possíveis "sentenças inseridas" (todo intervalo contíguo de palavras da sentença mais longa) e testar se removê-las resulta exatamente na sentença mais curta.

- Tempo: O(n²) tentativas (todo par início/fim de intervalo de palavras), cada teste de igualdade O(n) · Espaço: O(n) por tentativa
- **Por que não basta:** testa posições de inserção que já poderiam ser descartadas cedo — o prefixo comum e o sufixo comum entre as duas sentenças já delimitam exatamente ONDE a inserção poderia ter acontecido; não é preciso testar todo intervalo possível.

## 💡 Solução 2 — A ideia otimizada (intuição)

Divida as duas sentenças em arrays de palavras. Conte quantas palavras batem a partir do início (`frontMatch`), avançando enquanto `words1[i] == words2[i]`. Depois, conte quantas batem a partir do fim (`backMatch`), recuando enquanto `words1[n1-1-j] == words2[n2-1-j]` — limitando esse segundo loop para nunca reusar uma palavra já contada pelo primeiro. Se `frontMatch + backMatch` cobrir todas as palavras da sentença **mais curta**, as sentenças são similares.

## 🎬 Exemplo passo a passo

`sentence1 = "My name is Haley"` (4 palavras), `sentence2 = "My Haley"` (2 palavras) → `minLen = 2`

| Passo | Direção | Comparação | Ação |
|---|---|---|---|
| 1 | prefixo | `words1[0]="My"` == `words2[0]="My"` | `frontMatch=1` |
| 2 | prefixo | `words1[1]="name"` ≠ `words2[1]="Haley"` | para o prefixo |
| 3 | sufixo | `words1[3]="Haley"` == `words2[1]="Haley"` | `backMatch=1` |
| 4 | sufixo | `backMatch(1) >= minLen-frontMatch(1)` | para o sufixo |

`frontMatch + backMatch = 1 + 1 = 2 >= minLen(2)` → **true** ✔ (o "buraco" no meio de `sentence1`, `"name is"`, é a sentença inserida)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada ponteiro percorre no máximo `min(n1, n2)` palavras
- **Espaço:** O(n1 + n2) para os arrays de palavras resultantes do `split`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean areSentencesSimilar(String sentence1, String sentence2) {
    String[] words1 = sentence1.split(" ");
    String[] words2 = sentence2.split(" ");
    int n1 = words1.length;
    int n2 = words2.length;
    int minLen = Math.min(n1, n2);

    int frontMatch = 0;
    while (frontMatch < minLen && words1[frontMatch].equals(words2[frontMatch])) {
        frontMatch++;
    }

    int backMatch = 0;
    // limite (minLen - frontMatch) evita contar de novo uma palavra já usada pelo prefixo
    while (backMatch < minLen - frontMatch
           && words1[n1 - 1 - backMatch].equals(words2[n2 - 1 - backMatch])) {
        backMatch++;
    }

    return frontMatch + backMatch >= minLen;
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

- Deixar `frontMatch` e `backMatch` se sobreporem — sem o limite `minLen - frontMatch` no loop do sufixo, as duas contagens poderiam contar a MESMA palavra da sentença mais curta duas vezes.
- Esquecer que a sentença inserida pode ser vazia — se as duas sentenças já forem idênticas, `frontMatch` sozinho cobre `minLen` inteiro, e o resultado ainda deve ser `true`.
- Assumir que a maior sentença é sempre uma delas especificamente — usar `Math.min`/`Math.max` explicitamente evita essa suposição, já que qualquer uma das duas pode ser a mais curta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Inserção no meio | `sentence1="My name is Haley"`, `sentence2="My Haley"` | true | `"name is"` inserido entre `"My"` e `"Haley"` |
| Sem cobertura suficiente | `sentence1="of"`, `sentence2="A lot of words"` | false | nenhuma combinação de prefixo+sufixo cobre a palavra única de sentence1 |
| Inserção só no final | `sentence1="Eating right now"`, `sentence2="Eating"` | true | `"right now"` inserido no final |
| Sentenças idênticas | `sentence1="a b c"`, `sentence2="a b c"` | true | inserção vazia, `frontMatch` já cobre tudo |

## 🔗 Conexões

- Problemas irmãos: [1961] Check if String Is a Prefix of Array (mesma ideia de casar uma sequência com um prefixo/sufixo de outra), [0392] Is Subsequence (mesma família de comparar duas sequências avançando ponteiros de forma greedy)
- No backend: comparar duas versões de um texto/configuração pra detectar se uma é a outra com um bloco inserido no meio — por exemplo, diffing simplificado de arquivos de configuração, detectando se a mudança entre duas versões foi só uma inserção contígua.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
