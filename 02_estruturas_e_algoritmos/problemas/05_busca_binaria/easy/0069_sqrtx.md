# [0069] Sqrt(x)

> 🔗 [LeetCode 69](https://leetcode.com/problems/sqrtx/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Math` `#Easy`

## 📜 O Problema

Dado um inteiro não negativo `x`, retorne a **raiz quadrada de `x` arredondada para baixo**. Não é permitido usar função/operador de potência pronto (nada de `pow(x, 0.5)` ou `x ** 0.5`).

**Exemplos:**
```
Input:  x = 4    Output: 2   (raiz exata)
Input:  x = 8    Output: 2   (raiz real é 2.828..., arredonda para baixo)
```

**Restrições (e o que elas denunciam):**
- `0 <= x <= 2^31 - 1` → x pode ser bem grande; testar candidato a candidato (1, 2, 3, ...) é O(√x), inviável para x perto de 2 bilhões
- "must not use any built-in exponent function" → proíbe o atalho óbvio, forçando a construir a busca manualmente
- "rounded down to the nearest integer" → não é "achar o valor exato", é achar o **maior inteiro k tal que k² <= x** — uma busca por fronteira, não por igualdade

## 🧭 Como reconhecer o padrão

Sempre que a pergunta é "qual é o maior/menor valor que satisfaz uma condição monotônica?" (aqui: `k*k <= x` é verdadeiro para k pequenos e falso para k grandes, sem alternar), é **busca binária na resposta**: em vez de buscar num array, buscamos num intervalo de inteiros candidatos `[0, x]`.

## 🐢 Solução 1 — Força bruta

Testar `k = 0, 1, 2, 3, ...` até que `k*k > x`; o resultado é `k - 1`.

- Tempo: O(√x) · Espaço: O(1)
- **Por que não basta:** com `x` até `2^31 - 1` (~2.1 bilhões), `√x` chega perto de 46341 — passa, mas é um desperdício: a condição `k*k <= x` é monotônica (verdadeira até um ponto, depois sempre falsa), e isso é exatamente o sinal para descartar metade do espaço a cada passo em vez de testar candidato por candidato.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de testar cada candidato em sequência, faça busca binária no intervalo `[0, x]`: para cada `mid`, verifique se `mid * mid <= x`.
- Se for verdadeiro, `mid` é um candidato válido, mas talvez exista um `mid` maior que também sirva → guarda `mid` como melhor resposta até agora e busca à **direita**.
- Se for falso, `mid` é grande demais → busca à **esquerda**.

Quando a busca termina, o melhor candidato guardado é a resposta.

> Cuidado com overflow: `mid * mid` pode estourar `int` quando `mid` chega perto de `2^16`. Use `long` na multiplicação (Java) ou compare via divisão (`mid <= x / mid`).

## 🎬 Exemplo passo a passo

`x = 8`

| Passo | left | mid | right | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 | 4 | 8 | 4*4=16 > 8 → grande demais | `right = 3` |
| 2 | 0 | 1 | 3 | 1*1=1 <= 8 → candidato válido | guarda 1, `left = 2` |
| 3 | 2 | 2 | 3 | 2*2=4 <= 8 → candidato válido | guarda 2, `left = 3` |
| 4 | 3 | 3 | 3 | 3*3=9 > 8 → grande demais | `right = 2` |
| 5 | 3 | — | 2 | `left > right` → fim | retorna melhor candidato: 2 |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log x) — cada iteração descarta metade do intervalo `[0, x]`
- **Espaço:** O(1) — só ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int mySqrt(int x) {
    if (x < 2) return x;                 // raiz de 0 é 0, raiz de 1 é 1 (caso trivial evita loop desnecessário)

    long left = 1, right = x;            // a resposta nunca passa de x/2 para x >= 2, mas x é limite seguro
    long resultado = 1;

    while (left <= right) {
        long mid = left + (right - left) / 2;
        long quadrado = mid * mid;       // long evita overflow: mid pode chegar perto de 2^16

        if (quadrado == x) {
            return (int) mid;            // raiz exata
        } else if (quadrado < x) {
            resultado = mid;             // candidato válido: guarda e tenta um mid maior
            left = mid + 1;
        } else {
            right = mid - 1;             // mid grande demais
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

- **Overflow em `mid * mid`**: com `x` até `2^31 - 1`, `mid` pode passar de 46000, e `mid * mid` em `int` (32 bits) estoura antes de chegar no teto. Use `long`/`long long`.
- **Esquecer o caso `x = 0` ou `x = 1`**: raiz de 0 é 0, raiz de 1 é 1 — sem tratamento especial, alguns intervalos iniciais (`left=1, right=x`) quebram para `x=0`.
- **Confundir "menor k com k*k >= x" com "maior k com k*k <= x"**: são buscas de fronteira diferentes; aqui queremos o maior k que ainda satisfaz `k*k <= x` (arredondar para baixo), não o primeiro que ultrapassa.
- **Achar que basta arredondar `(int)Math.sqrt(x)`**: o enunciado proíbe função de raiz/potência pronta — é a regra do problema, não só estilo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Zero | `x=0` | 0 | borda mínima |
| Um | `x=1` | 1 | raiz exata do menor caso não trivial |
| Quadrado perfeito | `x=4` | 2 | raiz exata |
| Não é quadrado perfeito | `x=8` | 2 | precisa arredondar para baixo |
| Valor grande (perto do limite) | `x=2147395599` | 46339 | testa overflow em `mid*mid` |

## 🔗 Conexões

- Problemas irmãos: **[0367] Valid Perfect Square** (mesma ideia, só que verifica igualdade em vez de arredondar), **[0441] Arranging Coins** (busca binária em cima de uma fórmula quadrática também), **[0704] Binary Search** (o padrão-base)
- No backend: "busca binária na resposta" é o mesmo raciocínio usado para achar o menor tamanho de buffer/página que satisfaz uma restrição de capacidade, ou para calibrar um parâmetro numérico (ex.: throttling) testando valores candidatos de forma monotônica em vez de força bruta.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
