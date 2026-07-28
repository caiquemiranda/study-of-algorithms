# [1871] Jump Game VII

> 🔗 [LeetCode 1871](https://leetcode.com/problems/jump-game-vii/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#DynamicProgramming` `#Medium`

## 📜 O Problema

Dada uma string binária `s` (0-indexada) e dois inteiros `minJump` e `maxJump`. Você começa no índice `0`, que é `'0'`. Você pode se mover do índice `i` para o índice `j` se: `i + minJump <= j <= min(i + maxJump, s.length - 1)` e `s[j] == '0'`. Retorne `true` se você consegue alcançar o índice `s.length - 1`.

**Exemplos:**
```
Input:  s = "0110101", minJump = 2, maxJump = 3
Output: true
Explicação: move de 0 para 3, depois de 3 para 5.

Input:  s = "01101110", minJump = 2, maxJump = 3
Output: false
```

**Restrições (e o que elas denunciam):**
- `2 <= s.length <= 10^5` → O(n · maxJump) recalculando do zero pode chegar a `10^10`; O(n) é o esperado
- `s[0] == '0'` → o ponto de partida sempre é um índice válido

## 🧭 Como reconhecer o padrão

Esse é um problema de DP sobre alcançabilidade (`dp[i]` = consigo chegar em `i`?), onde `dp[i]` depende de existir algum `dp[j]` verdadeiro no intervalo `[i-maxJump, i-minJump]`. Recalcular essa checagem do zero é O(maxJump) por índice; manter uma **contagem de janela deslizante** de quantos `dp[j]` verdadeiros existem nesse intervalo reduz cada passo a O(1) — a mesma ideia de [0837] New 21 Game.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `i`, verificar diretamente se algum `j` em `[i-maxJump, i-minJump]` tem `dp[j]` verdadeiro, percorrendo esse intervalo do zero.

- Tempo: O(n · maxJump) · Espaço: O(n)
- **Por que não basta:** recheca o mesmo intervalo repetidamente, quando apenas um índice entra e um sai da faixa relevante a cada incremento de `i`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha `count`: quantos `dp[j]` verdadeiros existem na janela `[i-maxJump, i-minJump]`. Ao avançar `i`: quando `i-minJump` se torna elegível como fonte, adicione `dp[i-minJump]` a `count`; quando `i-maxJump-1` sai de alcance, subtraia `dp[i-maxJump-1]`. `dp[i]` é verdadeiro se `s[i]=='0'` e `count > 0`.

## 🎬 Exemplo passo a passo

`s = "011010"`, `minJump = 2`, `maxJump = 3` (índices: 0₀ 1₁ 1₂ 0₃ 1₄ 0₅). `dp[0]=true`.

| i | i-minJump (adiciona) | i-maxJump-1 (remove) | count | s[i] | dp[i] |
|---|---|---|---|---|---|
| 1 | — (i<minJump) | — | 0 | '1' | false |
| 2 | dp[0]=true → count=1 | — | 1 | '1' | false |
| 3 | dp[1]=false → count=1 | — (3>maxJump falso) | 1 | '0' | true |
| 4 | dp[2]=false → count=1 | dp[0]=true → count=0 | 0 | '1' | false |
| 5 | dp[3]=true → count=1 | dp[1]=false → count=1 | 1 | '0' | true |

Resultado final: `dp[5] = true` ✔ (alcança o último índice)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n) para o array `dp`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean canReach(String s, int minJump, int maxJump) {
    int n = s.length();
    if (s.charAt(n - 1) != '0') {
        return false;
    }

    boolean[] dp = new boolean[n];
    dp[0] = true;
    int count = 0; // quantos dp[j] verdadeiros existem na janela [i-maxJump, i-minJump]

    for (int i = 1; i < n; i++) {
        if (i >= minJump) {
            count += dp[i - minJump] ? 1 : 0; // esse índice acabou de virar uma fonte elegível
        }
        if (i > maxJump) {
            count -= dp[i - maxJump - 1] ? 1 : 0; // esse índice saiu do alcance
        }
        dp[i] = s.charAt(i) == '0' && count > 0;
    }

    return dp[n - 1];
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

- A "janela" aqui é sobre o próprio array `dp` sendo construído, exatamente como em [0837] New 21 Game — manter uma contagem incremental evita somar do zero a cada `i`.
- A adição (`i >= minJump`) e a remoção (`i > maxJump`) acontecem em momentos DIFERENTES do loop, defasadas propositalmente: um índice só se torna uma fonte válida depois de `minJump` passos, e só sai de alcance depois de `maxJump` passos.
- `s[i] == '0'` é uma condição OBRIGATÓRIA além de `count > 0` — não basta existir uma fonte alcançável, o próprio destino precisa ser um `'0'`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Último índice é '1' | `s="0111"`, `minJump=1`, `maxJump=1` | false | atalho: se `s[n-1] != '0'`, nunca dá pra parar ali |
| minJump igual a maxJump | `s="000"`, `minJump=1`, `maxJump=1` | true | salto fixo de 1, todos '0' |
| Bloco de 1s bloqueando | `s="01101110"`, `minJump=2`, `maxJump=3` | false | nenhuma sequência de saltos alcança o fim |
| Exemplo do enunciado | `s="011010"`, `minJump=2`, `maxJump=3` | true | 0→3→5 alcança o fim |

## 🔗 Conexões

- Problemas irmãos: [0837] New 21 Game (mesmíssima técnica de manter uma contagem de janela sobre um array de DP sendo construído), [0055] Jump Game (mesma família de alcançabilidade, mas sem restrição de salto mínimo)
- No backend: modelar alcançabilidade em grafos de estados onde transições só são permitidas dentro de uma faixa de "distância" (replicação de dados que só pode saltar entre nós dentro de um intervalo de latência aceitável).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
