# [2269] Find the K-Beauty of a Number

> 🔗 [LeetCode 2269](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Math` `#Easy`

## 📜 O Problema

A **k-beauty** de um inteiro `num` é o número de substrings de `num` (lido como string) que atendem às condições: tem comprimento `k` **e** é um divisor de `num`. Zeros à esquerda são permitidos na substring; `0` nunca é divisor de nada. Retorne a k-beauty de `num`.

**Exemplos:**
```
Input:  num = 240, k = 2
Output: 2
Explicação: "24" (de "24"0) divide 240; "40" (de "2"40") divide 240. K-beauty = 2.

Input:  num = 430043, k = 2
Output: 2
Explicação: "43" aparece duas vezes e divide 430043; "30", "00" e "04" não dividem.
```

**Restrições (e o que elas denunciam):**
- `1 <= num <= 10^9` → como string, no máximo 10 dígitos; qualquer abordagem O(dígitos) é praticamente O(1)
- `1 <= k <= num.length` (tomando `num` como string) → `k` nunca excede o tamanho da string, sempre existe pelo menos uma janela

## 🧭 Como reconhecer o padrão

"Substrings de tamanho **fixo** `k` dentro da representação em string de um número" é janela deslizante de tamanho fixo: desliza-se uma janela de `k` dígitos sobre a string, mantendo o valor numérico da janela e testando se ele divide o número original.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, extrair a substring `numStr.substring(i, i+k)`, converter para inteiro e checar `num % valor == 0` (cuidando de não dividir por zero).

- Tempo: O(d) onde `d` é o número de dígitos (na prática O(1), já que `d <= 10`) · Espaço: O(d) para a string
- **Por que não basta (mesmo sendo rápido aqui):** recria uma nova `String` e reconverte para número a cada janela, quando o valor poderia ser atualizado incrementalmente — o padrão idiomático de janela deslizante que vale a pena internalizar para strings maiores.

## 💡 Solução 2 — A ideia otimizada (intuição)

Converta `num` para string uma vez. Mantenha o valor da janela atual como inteiro; ao deslizar, "remove" o dígito mais significativo (subtraindo `dígito_removido × 10^(k-1)`) e "adiciona" o novo dígito à direita (`valor × 10 + novo_dígito`), sem nunca re-parsear a substring inteira.

## 🎬 Exemplo passo a passo

`num = 240` (string `"240"`), `k = 2`

| i | Janela (string) | Valor da janela | num % valor == 0? | Divisor de num? | Contagem |
|---|---|---|---|---|---|
| 0 | "24" | 24 | 240%24=0 | sim | 1 |
| 1 | "40" | 24 - 2·10 = 4 → 4·10+0 = 40 | 240%40=0 | sim | 2 |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(d) — `d` = número de dígitos de `num` (no máximo 10)
- **Espaço:** O(d) para a string de dígitos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int divisorSubstrings(int num, int k) {
    String digits = String.valueOf(num);
    int windowValue = 0;
    for (int i = 0; i < k; i++) {
        windowValue = windowValue * 10 + (digits.charAt(i) - '0');
    }

    int pow = (int) Math.pow(10, k - 1); // peso do dígito mais significativo da janela
    int count = isDivisor(num, windowValue) ? 1 : 0;

    for (int i = k; i < digits.length(); i++) {
        int outDigit = digits.charAt(i - k) - '0';
        int inDigit = digits.charAt(i) - '0';
        windowValue = (windowValue - outDigit * pow) * 10 + inDigit; // desliza a janela de dígitos
        if (isDivisor(num, windowValue)) {
            count++;
        }
    }

    return count;
}

private boolean isDivisor(int num, int value) {
    return value != 0 && num % value == 0; // 0 nunca é divisor de nada
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

- `0` nunca é divisor de nenhum número (regra explícita do enunciado) — checar `value != 0` antes de fazer `num % value`, senão risco de divisão por zero.
- Zeros à esquerda são permitidos na substring (ex.: "04" vale 4) — não descartar janelas que começam com `'0'`.
- Atualizar o valor da janela na ordem errada (somar o novo dígito antes de remover o antigo, ou esquecer o peso `10^(k-1)` do dígito removido) produz um valor numérico incorreto silenciosamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k igual ao número de dígitos | `num=240`, `k=3` | 1 | única janela possível é o próprio número, que sempre se divide |
| Janela com zero (não divisor) | `num=430043`, `k=2` | 2 | "00" e "30" não dividem 430043; só "43" (duas vezes) divide |
| k=1, dígito zero presente | `num=105`, `k=1` | 2 | dígitos "1" e "5" dividem 105; "0" nunca conta |
| Número de um único dígito | `num=7`, `k=1` | 1 | único dígito, sempre divide a si mesmo |

## 🔗 Conexões

- Problemas irmãos: [1876] Substrings of Size Three with Distinct Characters (mesma técnica de janela de tamanho fixo, aqui sobre dígitos em vez de letras), [0187] Repeated DNA Sequences (mesma ideia de deslizar uma janela fixa mantendo um valor incremental em vez de reprocessar a substring inteira)
- No backend: validar códigos ou checksums onde sub-blocos de tamanho fixo dentro de um identificador precisam satisfazer uma propriedade aritmética — por exemplo, validação de dígitos verificadores em blocos de um número de documento.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
