# [0009] Palindrome Number

> 🔗 [LeetCode 9](https://leetcode.com/problems/palindrome-number/) · Dificuldade: 🟢 easy · Categoria: [`17_matematica_e_geometria`](../../../fundamentos/17_matematica_e_geometria.md)
> 📅 Resolvido em: 2026-07-24 · Revisões: —

Tags: `#Matematica` `#ManipulacaoDeDigitos` `#Easy`

## 📜 O Problema

Dado um inteiro `x`, retorne `true` se `x` é um **palíndromo** (lê-se igual de trás para frente) e `false` caso contrário.

**Exemplos:**
```
Input:  x = 121     Output: true    Explicação: lido da esquerda ou da direita, dá "121"
Input:  x = -121    Output: false   Explicação: da direita para esquerda vira "121-", o sinal quebra a simetria
Input:  x = 10       Output: false   Explicação: da direita para esquerda vira "01", o zero à esquerda não existe em número
```

**Restrições (e o que elas denunciam):**
- `-2^31 <= x <= 2^31 - 1` → `x` cabe num `int` de 32 bits; isso é o aviso de que **reverter o número inteiro pode estourar** (ex.: `x = 1534236469` reverte para `9646324351`, que já não cabe em `int`). A solução precisa lidar com isso sem simplesmente reverter tudo.
- Não há restrição de tempo/espaço explícita, mas o próprio enunciado convida a uma pergunta: "dá para resolver sem converter para string?" — é o sinal de que a solução elegante é puramente aritmética.

## 🧭 Como reconhecer o padrão

"Verificar simetria de dígitos de um número" é manipulação numérica pura — mesma família de "reverter inteiro" (LC 7) e "Pow(x,n)" (divisão do problema em metades). Não é array nem string: é aritmética com `%` e `/`, e por isso mora em [matemática e geometria](../../../fundamentos/17_matematica_e_geometria.md), não em two pointers (mesmo que a ideia de "comparar pontas" seja parecida).

## 🐢 Solução 1 — Força bruta (converter para string)

Converte `x` para string e compara com o seu reverso (dois ponteiros nas pontas, ou `s == s[::-1]`).

- Tempo: O(log₁₀ x) · Espaço: O(log₁₀ x) — para guardar a string
- **Por que não basta:** funciona e passa, mas o problema convida explicitamente a resolver **sem converter para string** (é a pergunta clássica de follow-up em entrevista). Usar string gasta espaço extra que a versão numérica não precisa.

## 💡 Solução 2 — A ideia otimizada (intuição)

Negativos nunca são palíndromos (o sinal `-` só existe no início, nunca no fim) — descarta na hora. Números terminados em `0` (exceto o próprio `0`) também nunca são, porque um palíndromo não pode começar com `0`.

Para o resto: em vez de reverter o número **inteiro** (que pode estourar `int`), reverta só a **metade de trás** e pare quando ela alcançar ou ultrapassar a metade da frente. Nesse ponto:
- se `x` tem número par de dígitos, a metade da frente (`x` restante) deve ser igual à metade reversa;
- se tem número ímpar, sobra um dígito do meio a mais na metade reversa — descarte-o dividindo por 10.

Isso evita overflow (a metade reversa nunca cresce além do próprio `x` original) e evita alocar string.

## 🎬 Exemplo passo a passo

`x = 12321` (ímpar, 5 dígitos)

| Passo | x (restante) | reversed (acumulado) | Comparação `x <= reversed`? | Ação |
|---|---|---|---|---|
| 1 | 12321 | 0 | não | `reversed = 0*10 + 1 = 1`; `x = 1232` |
| 2 | 1232 | 1 | não | `reversed = 1*10 + 2 = 12`; `x = 123` |
| 3 | 123 | 12 | não | `reversed = 12*10 + 3 = 123`; `x = 12` |
| 4 | 12 | 123 | sim (`12 <= 123`) | para o loop |

Dígitos ímpares: descarta o do meio → `reversed / 10 = 12`. Compara `x (12) == reversed/10 (12)` → igual.

Resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log₁₀ x) — processa metade dos dígitos de `x`, e o número de dígitos é proporcional a `log₁₀ x`
- **Espaço:** O(1) — só duas variáveis inteiras, nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isPalindrome(int x) {
    // Negativo nunca é palíndromo: o '-' só apareceria no início.
    // Terminado em 0 (e diferente de 0) nunca é: um número não pode
    // começar com 0, então não pode "terminar igual ao início" nesse caso.
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    int reversedHalf = 0;
    // Reverte só a metade de trás. Parar quando x <= reversedHalf
    // garante que nunca reconstruímos o número inteiro -> sem overflow.
    while (x > reversedHalf) {
        reversedHalf = reversedHalf * 10 + x % 10;
        x /= 10;
    }

    // Dígitos pares: x == reversedHalf (as duas metades se encontraram).
    // Dígitos ímpares: sobra o dígito do meio em reversedHalf;
    // descartar dividindo por 10 (ex.: 12321 -> x=12, reversedHalf=123 -> 123/10=12).
    return x == reversedHalf || x == reversedHalf / 10;
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

- **Reverter o número inteiro e comparar**: funciona na maioria dos casos, mas **estoura `int`** em Java/C++ para entradas grandes (ex.: `1563847412` reverte para `2147483651`, que passa de `Integer.MAX_VALUE`). Reverter só a metade evita isso por construção.
- **Esquecer o caso `x == 0`**: `0` é palíndromo (`true`), mas a regra "termina em 0 é sempre false" pegaria ele por engano se não excluir `x != 0` explicitamente.
- **Esquecer negativos**: `-121` "parece" palíndromo se você só olhar os dígitos `121`, mas o sinal quebra a leitura da direita para a esquerda — sempre `false`.
- **Confundir dígitos pares e ímpares na comparação final**: comparar sempre `x == reversedHalf` falha para quantidade ímpar de dígitos (sobra o dígito do meio); é preciso o `|| x == reversedHalf / 10`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Zero | `0` | `true` | borda: termina em 0, mas é o único caso válido disso |
| Negativo simétrico | `-121` | `false` | o sinal invalida antes mesmo de olhar os dígitos |
| Termina em zero (não-zero) | `10` | `false` | reverso teria "01", que não é número válido |
| Dígitos pares | `1221` | `true` | as duas metades se encontram exatamente |
| Dígitos ímpares | `12321` | `true` | precisa descartar o dígito do meio (`reversedHalf / 10`) |
| Um dígito | `7` | `true` | caso trivial, x == reversedHalf logo na 1ª iteração |
| Quase estoura int se revertido inteiro | `1563847412` | `false` | mostra por que reverter só a metade importa |

## 🔗 Conexões

- Problemas irmãos: **[0007] Reverse Integer** (mesma mecânica de `% 10` / `/ 10`, mas precisa checar overflow explicitamente), **[0008] String to Integer (atoi)** (outra manipulação numérica dígito a dígito com casos de borda chatos), **[0125] Valid Palindrome** (mesma ideia de simetria, agora em string)
- No backend: checagem dígito a dígito sem alocar estrutura auxiliar é o mesmo raciocínio por trás de validar checksums (dígito verificador de CPF, cartão de crédito via algoritmo de Luhn) processando um número por vez, sem transformar tudo em string antes.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
