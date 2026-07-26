# [0551] Student Attendance Record I

> 🔗 [LeetCode 551](https://leetcode.com/problems/student-attendance-record-i/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Você recebe uma string `s` representando o registro de presença de um estudante, onde cada caractere indica se o estudante faltou, chegou atrasado ou esteve presente naquele dia:
- `'A'`: Ausente.
- `'L'`: Atrasado (Late).
- `'P'`: Presente.

O estudante é elegível para um prêmio de assiduidade se atender **ambos** os critérios:
- Faltou (`'A'`) por **estritamente** menos de 2 dias no total.
- **Nunca** chegou atrasado (`'L'`) por 3 ou mais dias **consecutivos**.

Retorne `true` se o estudante é elegível para o prêmio, ou `false` caso contrário.

**Exemplos:**
```
Input:  s = "PPALLP"
Output: true
Explicação: menos de 2 faltas e nunca atrasado 3+ dias seguidos.

Input:  s = "PPALLL"
Output: false
Explicação: atrasado 3 dias consecutivos nos últimos 3 dias, não é elegível.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 1000` → qualquer O(n) resolve tranquilamente
- `s[i]` é `'A'`, `'L'` ou `'P'` → só 3 caracteres possíveis, sem necessidade de validação extra

## 🧭 Como reconhecer o padrão

"Conte ocorrências totais de X" + "verifique se não existe uma sequência de 3+ Y consecutivos" são duas checagens independentes que cabem numa única passada: um contador acumulado (para `'A'`) e um contador que reseta (para sequências de `'L'`).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Contar todas as ocorrências de `'A'` com uma passada, e separadamente, para cada posição, verificar com um laço aninhado se há 3 `'L'`s consecutivos a partir dali.

- Tempo: O(n²) por causa do laço aninhado para checar sequências de `'L'` a partir de cada posição · Espaço: O(1)
- **Por que não basta:** verificar sequências consecutivas de `'L'` não precisa reiniciar a busca a cada posição — um contador que reseta ao encontrar um caractere diferente de `'L'` já captura isso em uma única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única passada pela string, mantendo dois contadores: `totalAusencias` (incrementa a cada `'A'`) e `atrasosConsecutivos` (incrementa a cada `'L'`, reseta a 0 em qualquer outro caractere). Se `totalAusencias >= 2` ou `atrasosConsecutivos >= 3` em qualquer momento, já pode retornar `false` imediatamente.

## 🎬 Exemplo passo a passo

`s = "PPALLL"`

| Passo | i | char | totalAusencias | atrasosConsecutivos | condição violada? |
|---|---|---|---|---|---|
| 1 | 0 | P | 0 | 0 | não |
| 2 | 1 | P | 0 | 0 | não |
| 3 | 2 | A | 1 | 0 | não (ainda < 2) |
| 4 | 3 | L | 1 | 1 | não |
| 5 | 4 | L | 1 | 2 | não |
| 6 | 5 | L | 1 | 3 | **sim** (3 atrasos consecutivos) |

Resultado final: `false` ✔ (para no passo 6, assim que `atrasosConsecutivos` chega a 3)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada, com possível saída antecipada
- **Espaço:** O(1) — só dois contadores inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean checkRecord(String s) {
    int totalAusencias = 0;
    int atrasosConsecutivos = 0;

    for (char c : s.toCharArray()) {
        if (c == 'A') {
            totalAusencias++;
            atrasosConsecutivos = 0; // 'A' quebra qualquer sequência de atrasos em andamento
        } else if (c == 'L') {
            atrasosConsecutivos++;
        } else { // 'P'
            atrasosConsecutivos = 0;
        }

        if (totalAusencias >= 2 || atrasosConsecutivos >= 3) {
            return false; // já não há como ser elegível, corta cedo
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

- Esquecer de resetar `atrasosConsecutivos` quando encontra `'A'` ou `'P'` — sem o reset, atrasos separados por outros caracteres seriam contados como se fossem consecutivos.
- Usar `>` em vez de `>=` nas condições — o enunciado é claro: "estritamente menos que 2 ausências" (ou seja, 2 já desqualifica) e "3 ou mais atrasos consecutivos" (3 já desqualifica).
- Não cortar a execução cedo (`return false` assim que a condição é violada) — não é um erro de correção, só uma otimização perdida; funciona igual sem o corte, só percorre caracteres desnecessários depois que já sabe a resposta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Elegível no limite | `"PPALLP"` | true | 1 ausência, no máximo 2 atrasos consecutivos |
| Atrasos consecutivos demais | `"PPALLL"` | false | 3 atrasos seguidos no final |
| Duas ausências | `"PAAP"` | false | 2 ausências totais, viola o limite |
| Atrasos separados | `"LLPLL"` | true | 2+2 atrasos, mas nunca 3 seguidos (o 'P' quebra a sequência) |

## 🔗 Conexões

- Problemas irmãos: [1207] Unique Number of Occurrences (mesma família de "contar e validar num único loop"), [0485] Max Consecutive Ones (mesmo padrão de contador que reseta ao quebrar a sequência)
- No backend: validação de regras de negócio sobre um histórico de eventos (ex.: bloquear conta após N falhas de login consecutivas, ou após um total de M tentativas inválidas) — o mesmo par "contador total + contador de sequência" aparece direto em regras de rate limiting.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
