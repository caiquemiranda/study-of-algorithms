# [1016] Binary String With Substrings Representing 1 To N

> 🔗 [LeetCode 1016](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/) · Dificuldade: 🟡 medium · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#ArraysEHashing` `#HashTable` `#BitManipulation` `#Medium`

## 📜 O Problema

Dada uma string binária `s` e um inteiro positivo `n`, retorne `true` se a representação binária de todos os inteiros no intervalo `[1, n]` forem **substrings** de `s`, ou `false` caso contrário.

**Exemplos:**
```
Input:  s = "0110", n = 3
Output: true

Input:  s = "0110", n = 4
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 1000` → o tamanho de `s` é pequeno, mas...
- `1 <= n <= 10^9` → `n` pode ser gigantesco. Testar `n` números um a um está fora de cogitação sem um corte — a chave é perceber que uma string de comprimento `L` só tem `L·(L+1)/2` substrings no total (contando repetições por posição), então se `n` exceder esse número, é **impossível** cobrir `1..n` e a resposta já é `false`

## 🧭 Como reconhecer o padrão

"Checar se um conjunto de valores existe como substrings de uma string" é resolvido pré-computando um **conjunto de substrings** (hashset) e consultando cada valor nele em O(1) — a marca registrada de arrays/hashing. Um argumento de contagem (princípio da casa dos pombos) permite podar `n` para um limite seguro antes de gerar qualquer substring, evitando trabalho proporcional ao `n` original (que pode ser até `10^9`).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `i` de `1` a `n`, converter `i` para binário e checar `s.contains(binario)` diretamente (busca de substring O(L) a cada checagem, sem pré-processamento).

- Tempo: O(n · L) — inviável quando `n` chega a `10^9` · Espaço: O(1)
- **Por que não basta:** nem sequer tenta limitar `n` a um valor razoável antes de iterar, e refaz uma busca de substring completa em `s` para cada um dos até `10^9` valores.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, aplique o corte: se `n > L·(L+1)/2` (o número máximo de substrings distintas que uma string de comprimento `L` pode ter), retorne `false` de cara — não há substrings suficientes para cobrir `1..n`. Isso garante que o `n` relevante nunca passa de `L·(L+1)/2`, cujas representações binárias nunca passam de `~log2(L²)` bits. Gere só as substrings de `s` com comprimento até esse limite de bits (guardando num `HashSet`), e então cheque cada `i` de `1` a `n` nesse conjunto.

## 🎬 Exemplo passo a passo

`s = "0110"` (L=4, limite = 4·5/2 = 10), `n = 3` — nenhum dos dois exemplos do enunciado excede o limite

| i | binário(i) | presente em s="0110"? | Resultado parcial |
|---|---|---|---|
| 1 | "1" | sim | continua |
| 2 | "10" | sim | continua |
| 3 | "11" | sim | continua |

Resultado final (n=3): `true` ✔ (todos os binários de 1 a 3 são substrings de "0110")

Para `n = 4` (contraste, segundo exemplo do enunciado): binário(4)="100" **não** é substring de "0110" → resultado: `false`

## ⚡ Complexidade da solução ótima

- **Tempo:** O(L · log n + n · log n) — geração das substrings limitada em comprimento a O(L · log n); verificação de cada um dos (no máximo O(L²)) valores custa O(log n) por consulta hash
- **Espaço:** O(L · log n) para o conjunto de substrings

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean queryString(String s, int n) {
    int len = s.length();
    if ((long) n > (long) len * (len + 1) / 2) {
        return false; // pigeonhole: não há substrings suficientes para cobrir 1..n
    }

    int maxBits = Integer.toBinaryString(n).length(); // nenhum binário de 1..n é mais longo que isso
    Set<String> substrings = new HashSet<>();
    for (int start = 0; start < len; start++) {
        int maxLen = Math.min(maxBits, len - start);
        for (int length = 1; length <= maxLen; length++) {
            substrings.add(s.substring(start, start + length));
        }
    }

    for (int i = 1; i <= n; i++) {
        if (!substrings.contains(Integer.toBinaryString(i))) {
            return false;
        }
    }

    return true;
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

- Gerar TODAS as substrings de `s` (até comprimento `L`, não só até `maxBits`) desperdiça memória absurdamente: o total de caracteres armazenados cresce O(L³), que para `L=1000` significa centenas de milhões de caracteres — limitar o comprimento das substrings geradas a `maxBits` (o tamanho do binário de `n`, tipicamente < 20 bits) é o que torna a solução viável.
- Esquecer o corte inicial (`n > L·(L+1)/2 → false`) faz o algoritmo tentar iterar até um `n` de `10^9`, mesmo quando a resposta já está decidida.
- `(long) n > (long) len * (len+1) / 2` precisa do cast pra `long` antes da multiplicação — para `len` perto de `1000`, `len*(len+1)` já cabe em `int`, mas é hábito seguro sempre que se multiplica limites de entrada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| n excede o limite de substrings possíveis | `s="0"`, `n=10^9` | false | corte pelo princípio da casa dos pombos decide na hora, sem gerar nada |
| n=1 (caso mínimo) | `s="1"`, `n=1` | true | "1" é substring de si mesma |
| Falta uma representação específica | `s="0110"`, `n=4` | false | "100" (binário de 4) não é substring de "0110" |
| Exemplo do enunciado | `s="0110"`, `n=3` | true | "1", "10" e "11" são todas substrings de "0110" |

## 🔗 Conexões

- Problemas irmãos: [0187] Repeated DNA Sequences (mesma técnica-base de usar um HashSet para checar substrings de tamanho controlado, ali com janela deslizante de tamanho fixo), [0187] variações de contagem por princípio da casa dos pombos aparecem em problemas de "existe espaço suficiente para todos os itens?"
- No backend: validar se um identificador (ex.: um código de barras ou hash) contém, como substring, todas as representações de uma faixa de IDs esperada — útil em sistemas de auditoria de sequenciamento onde a faixa de valores é conhecida, mas a codificação pode ser compacta.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
