# [0202] Happy Number

> 🔗 [LeetCode 202](https://leetcode.com/problems/happy-number/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#HashTable` `#Math` `#Easy`

## 📜 O Problema

Um **número feliz** é definido por este processo: substitua o número pela soma dos quadrados dos seus dígitos, e repita. Se o processo terminar em `1` (onde ele fica preso para sempre), o número é feliz. Se em vez disso ele entrar num **ciclo infinito que não inclui o 1**, o número não é feliz. Dado `n`, retorne `true` se ele for feliz.

**Exemplos:**
```
Input:  n = 19
Output: true
Explicação:
1²+9² = 82
8²+2² = 68
6²+8² = 100
1²+0²+0² = 1

Input:  n = 2
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 2^31 - 1` → até 10 dígitos; a soma dos quadrados dos dígitos de qualquer número de 10 dígitos cabe tranquilamente em `int` (máximo teórico 10 × 9² = 810), então não há risco de overflow
- Não há garantia de quando o processo "termina" → é preciso detectar um **ciclo**, não só contar iterações até um limite arbitrário

## 🧭 Como reconhecer o padrão

"Uma sequência gerada por uma função que se aplica sobre o próprio resultado anterior, e que pode ou não entrar em loop" é resolvido com o mesmo truque de ponteiro lento/rápido (Floyd) usado para detectar ciclo em lista encadeada — só que aqui o "próximo nó" é o resultado de `soma dos quadrados dos dígitos`, em vez de um `next` explícito.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Guardar cada valor já visto num `HashSet`. A cada iteração, calcule o próximo valor; se ele já estiver no set, é um ciclo sem chegar em 1 → não feliz. Se chegar em 1, é feliz.

- Tempo: O(k) onde k é o número de passos até repetir um valor · Espaço: O(k) — o set guarda todo valor intermediário visto
- **Por que não basta:** funciona corretamente, mas usa espaço proporcional ao tamanho da sequência até o ciclo se repetir; a versão com dois ponteiros detecta o mesmo ciclo com espaço **constante**, sem guardar histórico nenhum.

## 💡 Solução 2 — A ideia otimizada (intuição)

Trate a sequência de valores como se fosse uma lista encadeada implícita, onde `next(x)` é a soma dos quadrados dos dígitos de `x`. Use um ponteiro `lento` que avança um passo (`next`) por vez, e um ponteiro `rápido` que avança dois passos (`next(next(...))`) por vez. Se a sequência tiver um ciclo, os dois ponteiros eventualmente se encontram no mesmo valor — exatamente como na detecção de ciclo em lista encadeada. Se esse valor de encontro for `1`, o número é feliz; se for outro, é um ciclo sem 1.

## 🎬 Exemplo passo a passo

`n = 19` — `lento` e `rápido` começam ambos em 19 (rápido já dá seu primeiro passo antes do loop)

| Passo | lento (antes) | rápido (antes) | lento (1 passo) | rápido (2 passos) | lento == rápido? |
|---|---|---|---|---|---|
| 1 | 19 | 19 | 82 | 68 | não |
| 2 | 82 | 68 | 68 | 1 | não |
| 3 | 68 | 1 | 100 | 1 | não |
| 4 | 100 | 1 | 1 | 1 | sim |

`rápido == 1` no encontro → **true** ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) por chamada de `next` (número de dígitos) vezes o número de passos até o ciclo se fechar — na prática, a sequência encolhe rápido e converge em poucas iterações
- **Espaço:** O(1) — só os dois ponteiros `lento` e `rápido`, sem estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isHappy(int n) {
    int lento = n;
    int rapido = proximo(n);

    // rápido avança duas vezes mais rápido que lento; se houver ciclo,
    // os dois eventualmente coincidem no mesmo valor (Floyd)
    while (rapido != 1 && lento != rapido) {
        lento = proximo(lento);
        rapido = proximo(proximo(rapido));
    }

    return rapido == 1; // convergiu em 1 → feliz; convergiu em outro valor → ciclo sem 1
}

private int proximo(int n) {
    int soma = 0;
    while (n > 0) {
        int digito = n % 10;
        soma += digito * digito;
        n /= 10;
    }
    return soma;
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

- Achar que "detectar valor repetido com um Set" é a única forma de resolver — funciona, mas gasta espaço O(k); a versão com dois ponteiros aplica a mesma ideia de Floyd usada em [0141]/[0142], com O(1) de espaço.
- Confundir "não feliz" com "nunca termina" — está matematicamente provado que toda sequência desse processo cai em 1 ou no ciclo fixo `4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4`; não existe um terceiro destino, então o loop com dois ponteiros sempre termina.
- Inverter a ordem dos passos do `rápido` — ele precisa aplicar `proximo` **duas vezes** por iteração (`proximo(proximo(rapido))`), não uma; se avançar só uma vez, ele se torna igual ao `lento` e nunca detecta o ciclo corretamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Feliz clássico | `19` | true | converge em 1 depois de poucas iterações |
| Não feliz | `2` | false | cai no ciclo fixo `4→16→37→58→89→145→42→20→4` |
| Já é 1 | `1` | true | `rápido` já começa em `proximo(1) = 1`, loop nem executa |
| Converge devagar | `7` | true | precisa de mais iterações (7→49→97→130→10→1) antes de estabilizar |

## 🔗 Conexões

- Problemas irmãos: [0141] Linked List Cycle (mesma técnica de ponteiro lento/rápido para detectar ciclo, mas em lista encadeada explícita), [0142] Linked List Cycle II (mesma ideia, e ainda encontra o nó de início do ciclo)
- No backend: detecção de ciclo em qualquer processo iterativo determinístico — por exemplo, verificar se uma cadeia de redirecionamentos de URL entra em loop, ou se uma máquina de estados nunca alcança um estado final; sempre que o próximo estado é função pura do anterior, dois ponteiros detectam ciclo sem guardar histórico.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
