# [0520] Detect Capital

> 🔗 [LeetCode 520](https://leetcode.com/problems/detect-capital/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Definimos que o uso de maiúsculas numa palavra está certo quando um destes casos vale:
- Todas as letras da palavra são maiúsculas, como `"USA"`.
- Todas as letras da palavra não são maiúsculas, como `"leetcode"`.
- Só a primeira letra da palavra é maiúscula, como `"Google"`.

Dada uma string `word`, retorne `true` se o uso de maiúsculas nela está certo.

**Exemplos:**
```
Input:  word = "USA"
Output: true

Input:  word = "FlaG"
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= word.length <= 100` → entrada minúscula, qualquer O(n) resolve tranquilamente
- `word` consiste de letras minúsculas e maiúsculas do inglês → não precisa tratar caracteres não alfabéticos

## 🧭 Como reconhecer o padrão

"Validar se a entrada segue um de N padrões fixos" é sempre resolvido enumerando exatamente essas condições — aqui, três casos possíveis — sem precisar de estrutura de dados extra, só contagem ou comparação direta.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Comparar `word` contra as três formas possíveis: `word.toUpperCase()`, `word.toLowerCase()`, e a versão "capitalizada" (primeira maiúscula + resto minúsculo) construída manualmente.

- Tempo: O(n) — gera até 3 novas strings de tamanho n para comparar · Espaço: O(n) para as strings intermediárias
- **Por que não basta:** não é ineficiente de verdade (ainda é O(n)), mas gera até 3 strings novas quando dá para decidir em uma única passada contando maiúsculas, sem nenhuma alocação de string extra.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte quantas letras maiúsculas existem **depois** do primeiro caractere. Só há 3 casos válidos: 0 maiúsculas depois do índice 0 (tudo minúsculo, ou só a primeira é maiúscula), OU todas as letras depois do índice 0 são maiúsculas E a primeira também é (tudo maiúsculo).

## 🎬 Exemplo passo a passo

`word = "FlaG"`

| Passo | i | char | é maiúscula? | contagem de maiúsculas (i>=1) |
|---|---|---|---|---|
| 1 | 0 | F | sim (ignorado na contagem, é o primeiro) | 0 |
| 2 | 1 | l | não | 0 |
| 3 | 2 | a | não | 0 |
| 4 | 3 | G | sim | 1 |

Contagem final de maiúsculas após o índice 0: 1 (nem 0, nem "todas as 3 restantes") → não bate com nenhum dos 3 padrões válidos → **false** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) — só um contador inteiro

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean detectCapitalUse(String word) {
    int maiusculasAposPrimeira = 0;
    for (int i = 1; i < word.length(); i++) {
        if (Character.isUpperCase(word.charAt(i))) {
            maiusculasAposPrimeira++;
        }
    }

    // caso A: nenhuma maiúscula depois da primeira letra (ex.: "leetcode" ou "Google")
    if (maiusculasAposPrimeira == 0) {
        return true;
    }
    // caso B: todas as letras depois da primeira são maiúsculas E a primeira também é (ex.: "USA")
    boolean primeiraEhMaiuscula = Character.isUpperCase(word.charAt(0));
    return primeiraEhMaiuscula && maiusculasAposPrimeira == word.length() - 1;
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

- Esquecer o caso "USA" (tudo maiúsculo) e só checar "0 maiúsculas depois da primeira" — cobre "leetcode" e "Google", mas rejeita erroneamente "USA".
- Contar a primeira letra junto com as demais na mesma contagem — mistura os dois casos (tudo maiúsculo vs. só a primeira) e complica a lógica; separar a primeira letra deixa a checagem direta.
- Palavra de um único caractere (ex.: `"A"` ou `"a"`) — o loop não executa (não há índice 1), `maiusculasAposPrimeira` fica 0, cai no caso A e retorna `true` corretamente (qualquer letra sozinha é válida).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Tudo maiúsculo | `"USA"` | true | caso "tudo maiúsculo" |
| Só primeira maiúscula | `"Google"` | true | caso "capitalizado" |
| Tudo minúsculo | `"leetcode"` | true | caso "tudo minúsculo" |
| Maiúscula no meio | `"FlaG"` | false | maiúscula fora de qualquer um dos 3 padrões válidos |
| Uma letra | `"A"` | true | caso trivial, sempre válido |

## 🔗 Conexões

- Problemas irmãos: [0709] To Lower Case (mesma manipulação básica de caixa de caracteres), [0784] Letter Case Permutation (mesmo domínio de maiúsculas/minúsculas, mas gerando combinações)
- No backend: validação de formato de campos de entrada (ex.: siglas de país sempre em maiúsculo, nomes próprios capitalizados) antes de persistir dados de cadastro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
