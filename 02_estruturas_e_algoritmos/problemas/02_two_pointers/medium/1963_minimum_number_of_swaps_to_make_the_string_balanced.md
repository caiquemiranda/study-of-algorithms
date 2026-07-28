# [1963] Minimum Number of Swaps to Make the String Balanced

> 🔗 [LeetCode 1963](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Greedy` `#Medium`

## 📜 O Problema

Dada uma string `s` de tamanho par com `n/2` colchetes `'['` e `n/2` colchetes `']'`, você pode trocar os colchetes de **quaisquer** dois índices, quantas vezes quiser. Retorne o número **mínimo** de trocas para tornar `s` balanceada.

**Exemplos:**
```
Input:  s = "][]["
Output: 1
Explicação: troca índice 0 com 3 → "[[]]".

Input:  s = "]]][[["
Output: 2

Input:  s = "[]"
Output: 0
```

**Restrições (e o que elas denunciam):**
- `2 <= n <= 10^6` → O(n) é o único tempo viável nessa escala
- A troca pode ser entre **quaisquer** duas posições (não só adjacentes) → simplifica muito a resposta: não importa ONDE o `']'` desemparelhado está, só QUANTOS existem
- Quantidade de `'['` e `']'` sempre igual (`n/2` cada) → garante que sempre existe solução

## 🧭 Como reconhecer o padrão

"Contar o desequilíbrio mínimo que precisa ser corrigido, sem se importar com a posição exata" é resolvido com uma varredura da esquerda pra direita que acumula um **saldo** (`'['` soma, `']'` subtrai) — a mesma família de "passada única rastreando um estado acumulado" de [2511] Maximum Enemy Forts e [0821] Shortest Distance to a Character. Sempre que o saldo fica negativo, isso sinaliza um `']'` sem `'['` correspondente ainda "disponível" — e como a troca pode vir de QUALQUER lugar da string, basta contar esses momentos.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular repetidamente: encontrar o primeiro `']'` sem um `'['` correspondente ainda aberto, procurar à frente o próximo `'['` disponível, trocar os dois, e recomeçar a varredura do zero a cada troca.

- Tempo: O(n²) — cada troca pode exigir uma nova varredura completa da string
- **Por que não basta:** refaz a varredura inteira a cada troca; rastreando o desequilíbrio **acumulado** numa única passada, dá pra saber de antemão exatamente quantas trocas serão necessárias, sem precisar re-simular nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` mantendo um `balance` que soma `1` para cada `'['` e subtrai `1` para cada `']'`. Sempre que `balance` chegar a `-1`, significa que apareceu um `']'` sem nenhum `'['` "de sobra" pra casar com ele — conte uma troca e **reinicie** o `balance` para `1` (como se essa posição já tivesse sido virtualmente trocada por um `'['`, resolvendo o desequilíbrio local e permitindo que a contagem continue de um saldo positivo). O total de vezes que isso acontece é a resposta.

## 🎬 Exemplo passo a passo

`s = "]]][[["` (n=6)

| Passo | caractere | balance depois | Ação |
|---|---|---|---|
| 1 | `]` | -1 | desbalanceado! `swaps=1`, `balance` reinicia para 1 |
| 2 | `]` | 0 | — |
| 3 | `]` | -1 | desbalanceado! `swaps=2`, `balance` reinicia para 1 |
| 4 | `[` | 2 | — |
| 5 | `[` | 3 | — |
| 6 | `[` | 4 | — |

Resultado final: `swaps = 2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela string
- **Espaço:** O(1) — só o `balance` e o contador de trocas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int minSwaps(String s) {
    int balance = 0;
    int swaps = 0;

    for (char c : s.toCharArray()) {
        balance += (c == '[') ? 1 : -1;
        if (balance == -1) {
            // achou um ']' sem par ainda aberto: essa troca "conserta" o desequilíbrio local
            swaps++;
            balance = 1; // equivale a já ter trocado esse ']' virtualmente por um '['
        }
    }

    return swaps;
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

- Achar que é preciso simular as trocas de verdade (mover caracteres na string) — não é: o problema só pede a CONTAGEM mínima; rastrear o desequilíbrio numa passada já responde, sem tocar na string.
- Resetar `balance` para `0` em vez de `1` ao detectar o desequilíbrio — o reset pra `1` representa que a troca já "resolveu" esse `']'` (virando um `'['` efetivo); resetar pra `0` subestimaria o saldo real depois da correção.
- Confundir este problema com "trocas ADJACENTES" — aqui a troca pode ser entre QUAISQUER duas posições, o que simplifica muito a resposta comparado a um problema que só permitisse trocar vizinhos.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um desequilíbrio | `"][]["` | 1 | um `']'` desemparelhado logo no início |
| Dois desequilíbrios | `"]]][[["` | 2 | dois momentos de `balance=-1` durante a varredura |
| Já balanceada | `"[]"` | 0 | `balance` nunca fica negativo |
| Desequilíbrio duplo seguido | `"]][["` | 1 | `balance` vai a -1 na primeira posição, depois se recupera sem novo desequilíbrio |

## 🔗 Conexões

- Problemas irmãos: [0921] Minimum Add to Make Parentheses Valid (mesma ideia de rastrear desequilíbrio de parênteses numa passada), [0032] Longest Valid Parentheses (mesma família de análise de balanceamento de colchetes/parênteses)
- No backend: validar e "consertar" a estrutura de documentos aninhados (ex.: JSON ou XML malformado) contando o número mínimo de correções necessárias sem precisar simular cada correção individualmente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
