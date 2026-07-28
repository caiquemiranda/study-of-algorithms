# [0880] Decoded String at Index

> 🔗 [LeetCode 880](https://leetcode.com/problems/decoded-string-at-index/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#Medium`

## 📜 O Problema

Você recebe uma string codificada `s`. Para decodificá-la numa fita, lê-se um caractere por vez: se for uma **letra**, ela é escrita na fita; se for um **dígito** `d`, a fita atual inteira é repetida `d-1` vezes a mais (totalizando `d` cópias). Dado um inteiro `k`, retorne a `k`-ésima letra (1-indexada) da string decodificada.

**Exemplos:**
```
Input:  s = "leet2code3", k = 10
Output: "o"
Explicação: a string decodificada é "leetleetcodeleetleetcodeleetleetcode". A 10ª letra é "o".

Input:  s = "ha22", k = 5
Output: "h"
Explicação: a string decodificada é "hahahaha". A 5ª letra é "h".

Input:  s = "a2345678999999999999999", k = 1
Output: "a"
Explicação: a string decodificada é "a" repetida um número astronômico de vezes. A 1ª letra é "a".
```

**Restrições (e o que elas denunciam):**
- `2 <= s.length <= 100`, `1 <= k <= 10^9`, string decodificada com menos de `2^63` letras → o tamanho real decodificado pode ser astronomicamente maior que qualquer estrutura de dados poderia armazenar; a solução **não pode materializar a string decodificada**, precisa calcular a resposta indiretamente
- `s` consiste de letras minúsculas e dígitos `2` a `9`, sempre começando com letra → não há dígito `0`/`1` (que não fariam sentido como multiplicador), simplificando a lógica de repetição
- É garantido que `k` é válido dentro do tamanho decodificado → não é preciso tratar `k` fora dos limites

## 🧭 Como reconhecer o padrão

Este problema é oficialmente tagueado como "stack" no LeetCode porque uma abordagem válida é construir a string com uma pilha explícita — mas isso só funciona para tamanhos pequenos. A observação que resolve o problema de verdade é que você não precisa **construir** a string: só precisa saber o **tamanho** que a fita teria em cada ponto, e então "desfazer" as repetições de trás para frente até reduzir `k` ao caractere exato original. Essa técnica de "rastrear tamanho acumulado e depois andar para trás" é a mesma ideia central de [0388] Longest Absolute File Path (rastrear comprimento por nível) e [0394] Decode String (mesma sintaxe `letra`/`dígito`, mas expandindo em vez de indexar).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar uma pilha (ou StringBuilder) para construir a string decodificada caractere a caractere, expandindo cada repetição literalmente, e depois indexar diretamente na posição `k-1`.

- Tempo: O(tamanho decodificado) · Espaço: O(tamanho decodificado)
- **Por que não basta:** o enunciado garante que a string decodificada pode ter **menos de 2^63 letras** — um número tão grande que nem toda a memória do planeta conseguiria armazenar essa string. Construir a fita de verdade é fisicamente impossível para entradas como `"a2345678999999999999999"`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça duas passadas. **Primeira passada (esquerda para direita):** calcule o `tamanho` final da fita, sem construí-la — para cada letra, `tamanho += 1`; para cada dígito `d`, `tamanho *= d`. **Segunda passada (direita para esquerda):** percorra `s` de trás para frente "desfazendo" a construção. Para cada caractere, primeiro reduza `k = k % tamanho` (isso "desfaz" o efeito de todas as repetições completas, mantendo só a posição relativa dentro do último ciclo). Se `k == 0` **e** o caractere atual é uma letra, essa letra É a resposta (posição `k=0` após o módulo significa "a última posição do ciclo", que corresponde exatamente ao caractere que está sendo processado agora). Caso contrário: se for dígito, `tamanho /= d` (desfaz a multiplicação); se for letra, `tamanho -= 1` (desfaz a adição).

## 🎬 Exemplo passo a passo

`s = "ha22"`, `k = 5`

**Primeira passada (calcula tamanho final):** `h`→1, `a`→2, `2`→2×2=4, `2`→4×2=8. Tamanho final: `8`.

**Segunda passada (de trás para frente, reduzindo k):**

| Passo | Caractere (índice) | k antes | k %= tamanho | k==0 e é letra? | Ação | tamanho após |
|---|---|---|---|---|---|---|
| 1 | `2` (índice 3) | 5 | `5 % 8 = 5` | não (k≠0) | é dígito → tamanho `8/2=4` | 4 |
| 2 | `2` (índice 2) | 5 | `5 % 4 = 1` | não (k≠0) | é dígito → tamanho `4/2=2` | 2 |
| 3 | `a` (índice 1) | 1 | `1 % 2 = 1` | não (k≠0) | é letra → tamanho `2-1=1` | 1 |
| 4 | `h` (índice 0) | 1 | `1 % 1 = 0` | **sim!** → retorna `'h'` | — | — |

Resultado final: `"h"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — duas passadas lineares pela string (`n` é o tamanho de `s`, não da string decodificada)
- **Espaço:** O(1) — só variáveis escalares (`tamanho`, `k`), independente de quão grande a string decodificada seria

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String decodeAtIndex(String s, int k) {
    long tamanho = 0; // long: o tamanho decodificado pode passar de Integer.MAX_VALUE facilmente

    // 1ª passada: calcula o tamanho final da fita, sem construí-la
    for (char c : s.toCharArray()) {
        if (Character.isDigit(c)) {
            tamanho *= (c - '0');
        } else {
            tamanho += 1;
        }
    }

    // 2ª passada: de trás para frente, desfaz a construção até achar o caractere exato
    for (int i = s.length() - 1; i >= 0; i--) {
        char c = s.charAt(i);
        k %= tamanho; // reduz k à posição relativa dentro do ciclo atual

        if (k == 0 && Character.isLetter(c)) {
            return String.valueOf(c); // achou: esta letra ocupa a posição k (0 após módulo = última do ciclo)
        }

        if (Character.isDigit(c)) {
            tamanho /= (c - '0'); // desfaz a multiplicação
        } else {
            tamanho -= 1; // desfaz a adição
        }
    }

    return ""; // inalcançável dado que a entrada é garantida válida
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

- Usar `int` em vez de `long`/`long long` para `tamanho` — o tamanho decodificado pode crescer rapidamente além de `2^31`, mesmo que o `k` pedido seja pequeno; sem um tipo de 64 bits, a multiplicação estoura (overflow) antes mesmo de você conseguir usar o módulo para conter o crescimento.
- Esquecer o `k %= tamanho` **antes** de checar `k == 0` a cada iteração — é esse módulo que "desfaz" retroativamente todas as repetições completas, sem ele a lógica não converge para a posição real.
- Confundir a condição de parada — a resposta é encontrada quando `k == 0` **e** o caractere atual é uma **letra** (não um dígito); um dígito nunca é a resposta, mesmo que `k` chegue a 0 nele (a lógica continua reduzindo `tamanho` e seguindo para trás).
- Tentar resolver construindo a string mesmo com um limite artificial (ex.: "só construir até 10^9 caracteres") — isso ainda seria inviável em tempo e memória para os casos extremos do enunciado (multiplicadores em cascata alcançando `2^63`); a técnica correta nunca constrói a fita.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Múltiplos blocos de repetição | `"leet2code3", k=10` | `"o"` | testa a redução de k através de vários níveis de multiplicação |
| Repetição simples | `"ha22", k=5` | `"h"` | caso do enunciado, testa duas multiplicações consecutivas |
| Multiplicadores em cascata astronômicos | `"a2345678999999999999999", k=1` | `"a"` | testa que o algoritmo nunca tenta materializar o tamanho gigantesco, resolvendo em O(n) mesmo assim |
| k no limite exato do tamanho | `s` cujo tamanho final é exatamente `k` (ex.: `"ab2"`, k=4, decodificado="abab") | `"b"` | testa a borda onde k=tamanho, garantindo que `k % tamanho` trata isso como a última posição corretamente |

## 🔗 Conexões

- Problemas irmãos: [0394] Decode String (mesma sintaxe de codificação `letra`/`dígito`, mas expandindo a string em vez de indexar sem construí-la), [0388] Longest Absolute File Path (mesma técnica de rastrear tamanho acumulado sem reconstruir a estrutura inteira)
- No backend: essa técnica de "calcular o tamanho de uma estrutura comprimida e navegar até uma posição sem descomprimir tudo" é o mesmo princípio usado em acesso aleatório (random access) a arquivos comprimidos com compressão run-length, e em estruturas de dados sucintas que respondem consultas de posição sem materializar a representação expandida completa.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
