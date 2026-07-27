# [0925] Long Pressed Name

> 🔗 [LeetCode 925](https://leetcode.com/problems/long-pressed-name/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Seu amigo está digitando `name` num teclado. Às vezes, ao digitar um caractere `c`, a tecla fica **pressionada demais** e o caractere é digitado 1 ou mais vezes além do esperado. Você observa o resultado `typed`. Retorne `true` se `typed` pode ser `name` com alguns caracteres (possivelmente nenhum) pressionados a mais.

**Exemplos:**
```
Input:  name = "alex", typed = "aaleex"
Output: true
Explicação: 'a' e 'e' foram pressionados a mais.

Input:  name = "saeed", typed = "ssaaedd"
Output: false
Explicação: faltaria um 'e' extra em typed pra bater com os dois 'e' de name.
```

**Restrições (e o que elas denunciam):**
- `1 <= name.length, typed.length <= 1000` → O(n) esperado
- Só letras minúsculas → sem normalização de case
- A ordem dos caracteres é preservada, só a **quantidade** de repetições pode crescer → sinaliza que a comparação precisa respeitar a sequência, não só as frequências de cada letra

## 🧭 Como reconhecer o padrão

"Verificar se uma sequência é outra com alguns elementos repetidos a mais, na mesma ordem" é resolvido com dois ponteiros andando juntos por `name` e `typed`: quando os caracteres batem, os dois avançam; quando não batem, `typed` só pode estar tendo uma repetição extra do caractere **anterior** — senão, é inválido.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Comparar frequência de cada letra em `name` e em `typed` (contando ocorrências com um mapa), e checar se toda letra de `typed` aparece pelo menos tantas vezes quanto em `name`.

- Tempo: O(n + m) · Espaço: O(26) para os mapas de frequência
- **Por que não basta:** frequência sozinha ignora a **ordem**. `name = "abb"` e `typed = "bba"` têm as mesmas frequências de letras, mas não são compatíveis como long press — a sequência de caracteres importa, não só a contagem total de cada um.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `i` em `name` e `j` em `typed`. Se `name[i] == typed[j]`, é um caractere legítimo — avance os dois. Se forem diferentes, só existe uma explicação válida: `typed[j]` é uma repetição extra do caractere anterior (`typed[j] == typed[j-1]`) — nesse caso, avance só `j`. Qualquer outra situação é inválida. No final, `name` precisa ter sido totalmente consumido (`i == name.length()`).

## 🎬 Exemplo passo a passo

`name = "alex"`, `typed = "aaleex"`

| Passo | i | j | name[i] | typed[j] | Ação |
|---|---|---|---|---|---|
| 1 | 0 | 0 | `a` | `a` | iguais → i=1, j=1 |
| 2 | 1 | 1 | `l` | `a` | diferentes; `typed[1] == typed[0]`? sim → j=2 (repetição extra) |
| 3 | 1 | 2 | `l` | `l` | iguais → i=2, j=3 |
| 4 | 2 | 3 | `e` | `e` | iguais → i=3, j=4 |
| 5 | 3 | 4 | `x` | `e` | diferentes; `typed[4] == typed[3]`? sim → j=5 (repetição extra) |
| 6 | 3 | 5 | `x` | `x` | iguais → i=4, j=6 |

`j` chega ao fim de `typed` (6); `i = 4 == name.length()` → **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — cada ponteiro percorre sua string uma única vez
- **Espaço:** O(1) — só os índices `i` e `j`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isLongPressedName(String name, String typed) {
    int i = 0;
    int j = 0;

    while (j < typed.length()) {
        if (i < name.length() && name.charAt(i) == typed.charAt(j)) {
            i++;
            j++;
        } else if (j > 0 && typed.charAt(j) == typed.charAt(j - 1)) {
            j++; // repetição extra causada pela tecla pressionada demais
        } else {
            return false; // não casa com name, nem é repetição do caractere anterior
        }
    }

    return i == name.length(); // precisa ter consumido "name" inteiro
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

- Esquecer o `j > 0` antes de comparar `typed[j]` com `typed[j-1]` — no primeiro caractere (`j=0`) não existe "anterior"; sem essa checagem, um mismatch logo no início acessa índice inválido.
- Comparar só as frequências de cada letra — ignora a ordem; `name="abb"` e `typed="bba"` têm as mesmas contagens mas não são um long press válido.
- Esquecer de checar `i == name.length()` no final — se `typed` acabar mas `name` ainda tiver caracteres sobrando (ex.: `name="alexx"`, `typed="aaleex"`), a resposta deveria ser `false`; sem essa checagem final, o algoritmo aceitaria incorretamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Long press válido | `name="alex"`, `typed="aaleex"` | true | `'a'` e `'e'` pressionados a mais, ordem preservada |
| Caractere faltando | `name="saeed"`, `typed="ssaaedd"` | false | falta um `'e'` extra em typed pra bater com os dois `'e'` de name |
| Name maior que o consumido | `name="alexx"`, `typed="aaleex"` | false | `typed` acaba mas `name` ainda tem um `'x'` sobrando |
| Idênticas | `name="leelee"`, `typed="leelee"` | true | nenhum long press, casamento exato caractere a caractere |

## 🔗 Conexões

- Problemas irmãos: [0844] Backspace String Compare (mesma família de comparar duas strings processando caractere a caractere com lógica de "consumo condicional"), [0696] Count Binary Substrings (mesma ideia de trabalhar com grupos/runs de caracteres repetidos)
- No backend: validar se um payload recebido é uma versão "com ruído" (retransmissão duplicada) de um payload esperado — comum em protocolos que toleram repetição de bytes por retransmissão de rede.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
