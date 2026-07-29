# [0441] Arranging Coins

> 🔗 [LeetCode 441](https://leetcode.com/problems/arranging-coins/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Math` `#Easy`

## 📜 O Problema

Você tem `n` moedas e quer montar uma escada: a linha `i` precisa de exatamente `i` moedas. A última linha **pode ficar incompleta**. Retorne quantas **linhas completas** você consegue montar.

**Exemplos:**
```
Input:  n = 5    Output: 2   (linha 1 usa 1, linha 2 usa 2, total 3; sobra 2, não dá pra completar a linha 3 que precisa de 3)
Input:  n = 8    Output: 3   (1+2+3=6 moedas usadas; sobram 2, não dá pra completar a linha 4 que precisa de 4)
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 2^31 - 1` → `n` pode ser gigantesco; simular linha por linha (somando 1, depois 2, depois 3...) até estourar `n` é O(√n) na prática, mas ainda é mais lento que necessário
- O total de moedas até a linha `k` é `k*(k+1)/2` (soma de PA) → é uma fórmula **monotonicamente crescente** em `k` — a condição "`k*(k+1)/2 <= n`" é verdadeira para k pequenos e falsa depois, sem alternar
- Existe uma fórmula fechada via Bhaskara (`k = (-1 + sqrt(1+8n)) / 2`), mas ela usa raiz de ponto flutuante — que sofre erro de precisão justamente nos valores grandes que o problema testa (`n` até ~2 bilhões)

## 🧭 Como reconhecer o padrão

"Ache o maior `k` tal que uma fórmula crescente em `k` seja `<= n`" é **busca binária na resposta**: em vez de calcular `k` direto com uma fórmula (que aqui tem risco de imprecisão numérica), buscamos `k` testando candidatos num intervalo `[0, n]`.

## 🐢 Solução 1 — Força bruta

Simular: comece com `linha = 1` e `moedasUsadas = 0`; enquanto `moedasUsadas + linha <= n`, some `linha` a `moedasUsadas`, incremente `linha`. Retorne `linha - 1`.

- Tempo: O(√n) — porque a linha completa cresce até aproximadamente `√(2n)` · Espaço: O(1)
- **Por que não basta:** embora O(√n) já não seja terrível, ele ainda testa candidato por candidato sequencialmente; como a condição `k*(k+1)/2 <= n` é monotônica, dá para descartar metade do espaço de busca a cada comparação em vez de andar de 1 em 1.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça busca binária no intervalo `[1, n]` de possíveis números de linhas completas `k`. Para cada `mid`, calcule o total de moedas necessário para `mid` linhas: `total = mid * (mid + 1) / 2`.
- Se `total <= n`, `mid` linhas cabem — é um candidato válido, mas talvez um `k` maior também caiba → guarda `mid` e busca à **direita**.
- Se `total > n`, `mid` linhas não cabem → busca à **esquerda**.

O melhor candidato guardado ao final é a resposta.

> Por que não usar a fórmula de Bhaskara direto? Ela é O(1), mas depende de `sqrt` em ponto flutuante — para `n` perto de `2^31 - 1`, o erro de arredondamento pode dar um `k` errado por 1 unidade. Busca binária com aritmética inteira é imune a esse problema.

## 🎬 Exemplo passo a passo

`n = 8`

| Passo | left | mid | right | total = mid*(mid+1)/2 | Comparação | Decisão |
|---|---|---|---|---|---|---|
| 1 | 1 | 4 | 8 | 10 | 10 > 8 → grande demais | `right = 3` |
| 2 | 1 | 2 | 3 | 3 | 3 <= 8 → candidato válido | guarda 2, `left = 3` |
| 3 | 3 | 3 | 3 | 6 | 6 <= 8 → candidato válido | guarda 3, `left = 4` |
| 4 | 4 | — | 3 | — | `left > right` → fim | retorna melhor candidato: 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do intervalo `[1, n]`
- **Espaço:** O(1) — só ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int arrangeCoins(int n) {
    long left = 1, right = n;             // long: n já é int grande, e "right" evita overflow em contas futuras
    long resultado = 0;

    while (left <= right) {
        long mid = left + (right - left) / 2;
        long totalNecessario = mid * (mid + 1) / 2;  // soma de PA: moedas para "mid" linhas completas

        if (totalNecessario <= n) {
            resultado = mid;              // mid linhas cabem: candidato válido, tenta um mid maior
            left = mid + 1;
        } else {
            right = mid - 1;              // mid linhas não cabem: precisa de menos linhas
        }
    }
    return (int) resultado;
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

- **Overflow em `mid * (mid + 1)`**: com `n` até `2^31 - 1`, `mid` pode passar de 65000, e `mid * (mid + 1)` em `int` de 32 bits estoura antes de comparar com `n`. Use `long`/`long long`.
- **Usar a fórmula de Bhaskara sem cuidado**: `(-1 + Math.sqrt(1 + 8.0*n)) / 2` funciona para a maioria dos casos, mas erro de ponto flutuante pode arredondar errado exatamente nos valores de `n` grandes que o LeetCode testa — é uma pegadinha clássica deste problema específico.
- **Confundir "linhas completas" com "moedas sobrando"**: o problema pede o número de linhas, não o resto — não esqueça de retornar `mid`/`resultado`, não `n - total`.
- **Esquecer que `n = 0` não é uma entrada válida aqui** (a restrição garante `n >= 1`), mas se fosse, o resultado seria 0 linhas — bom caso mental para validar a lógica de `left = 1`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| n=1 (borda mínima) | `n=1` | 1 | só dá para completar a linha 1 |
| Exatamente uma linha, sem sobra | `n=3` | 2 | 1+2=3, encaixa perfeito na linha 2 |
| Sobra sem completar a próxima | `n=5` | 2 | trace do enunciado |
| Triangular perfeito grande | `n=6` | 3 | 1+2+3=6, encaixa perfeito na linha 3 |
| Valor grande (perto do limite) | `n=2147483647` | 65535 | testa overflow em `mid*(mid+1)` |

## 🔗 Conexões

- Problemas irmãos: **[0069] Sqrt(x)** (mesmo padrão de busca binária sobre fórmula crescente), **[0367] Valid Perfect Square** (busca binária evitando `sqrt` de ponto flutuante), **[0704] Binary Search** (o padrão-base)
- No backend: buscar o maior `k` que satisfaz uma restrição de capacidade crescente (aqui, "quantas linhas cabem") é o mesmo raciocínio usado para calcular quantas páginas de resultado cabem num orçamento de memória, ou quantos itens cabem numa paginação com tamanho de página variável — sem depender de aritmética de ponto flutuante que poderia falhar em valores extremos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
