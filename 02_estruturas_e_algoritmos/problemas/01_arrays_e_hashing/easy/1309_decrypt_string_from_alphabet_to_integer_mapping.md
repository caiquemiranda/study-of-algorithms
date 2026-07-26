# [1309] Decrypt String from Alphabet to Integer Mapping

> 🔗 [LeetCode 1309](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Você recebe uma string `s` formada por dígitos e `'#'`. Queremos mapear `s` para caracteres minúsculos do inglês assim:
- Caracteres (`'a'` a `'i'`) são representados por (`'1'` a `'9'`) respectivamente.
- Caracteres (`'j'` a `'z'`) são representados por (`'10#'` a `'26#'`) respectivamente.

Retorne a string formada após o mapeamento. Os casos de teste garantem que sempre existe um mapeamento único.

**Exemplos:**
```
Input:  s = "10#11#12"
Output: "jkab"
Explicação: "j" -> "10#", "k" -> "11#", "a" -> "1", "b" -> "2".

Input:  s = "1326#"
Output: "acz"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 1000` → O(n) resolve com folga
- mapeamento ambíguo por tamanho variável (1 dígito para a-i, "NN#" para j-z) → precisa OLHAR À FRENTE (lookahead) para decidir se os próximos caracteres formam um código de 2 dígitos + '#'
- "mapeamento único sempre existe" → não precisa tratar ambiguidade real

## 🧭 Como reconhecer o padrão

"Decodificar símbolos de tamanho variável, onde o tamanho é decidido por um marcador (aqui, o '#')" é resolvido processando a string DA DIREITA PARA A ESQUERDA, verificando se os 2 caracteres antes de um possível '#' formam um código de 2 dígitos.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Percorrer a string da esquerda para a direita, e para cada posição, tentar todos os tamanhos possíveis de "próximo token" verificando qual delimitação é válida — sem aproveitar que o '#' sempre aparece 2 posições à frente quando existe.

- Tempo: O(n) na prática, mas com mais ramificações condicionais do que necessário · Espaço: O(n) para o resultado
- **Por que vale nomear mesmo assim:** a armadilha não é de complexidade (ambas são O(n)), é de organização: processar da DIREITA para a ESQUERDA simplifica a decisão, porque ao ver um '#', você já sabe que os 2 caracteres anteriores fazem parte do mesmo código.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` de trás para frente com um índice `i` começando no último caractere. Se `s[i] == '#'`, os caracteres em `s[i-2..i-1]` formam um número de 2 dígitos — decodifique como letra e recue `i` em 3. Caso contrário, `s[i]` sozinho é um número de 1 dígito — decodifique e recue `i` em 1.

## 🎬 Exemplo passo a passo

`s = "10#11#12"` — índices: 1(0) 0(1) #(2) 1(3) 1(4) #(5) 1(6) 2(7)

| Passo | i | s[i] | é '#'? | código extraído | letra | novo i |
|---|---|---|---|---|---|---|
| 1 | 7 | 2 | não | "2" | 'b' | 6 |
| 2 | 6 | 1 | não | "1" | 'a' | 5 |
| 3 | 5 | # | sim | s[3..4]="11" | 'k' | 2 |
| 4 | 2 | # | sim | s[0..1]="10" | 'j' | -1 |

Construindo de trás para frente e invertendo: letras coletadas na ordem processada = b, a, k, j → invertido = j, k, a, b → `"jkab"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada
- **Espaço:** O(n) — para o resultado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String freqAlphabets(String s) {
    StringBuilder resultado = new StringBuilder();
    int i = s.length() - 1;

    while (i >= 0) {
        if (s.charAt(i) == '#') {
            // os 2 caracteres antes do '#' formam um código de 2 dígitos (10 a 26)
            int codigo = Integer.parseInt(s.substring(i - 2, i));
            resultado.append((char) ('a' + codigo - 1));
            i -= 3; // pula os 2 dígitos + o '#'
        } else {
            // um único dígito (1 a 9) mapeia direto para 'a' a 'i'
            int codigo = s.charAt(i) - '0';
            resultado.append((char) ('a' + codigo - 1));
            i -= 1;
        }
    }
    return resultado.reverse().toString(); // foi construído de trás para frente, precisa inverter
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

- Processar da esquerda para a direita sem lookahead correto — decidir se um dígito é parte de um código de 1 ou 2 dígitos exige olhar 2 posições à frente para checar se há um '#'; processar de trás para frente evita esse lookahead complicado.
- Errar a conversão código→letra: `'a' + codigo - 1`, não `'a' + codigo` — como 'a' corresponde ao código 1 (não 0), é preciso subtrair 1 no deslocamento.
- Esquecer de inverter o `StringBuilder` no final, já que ele foi construído de trás para frente durante o processamento.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Mistura de códigos de 1 e 2 dígitos | `"10#11#12"` | "jkab" | caso padrão do enunciado |
| Só código de 2 dígitos no final | `"1326#"` | "acz" | "1","3","26#" -> 'a','c','z' |
| Só códigos de 1 dígito | `"123456789"` | "abcdefghi" | mapeamento direto, sem nenhum '#' |
| Um único código de 2 dígitos | `"10#"` | "j" | menor caso possível de código de 2 dígitos |

## 🔗 Conexões

- Problemas irmãos: [1313] Decompress Run-Length Encoded List (mesma família de decodificação de um formato compacto), [0038] Count and Say (também processa string com lógica de "grupos" e reconstrução)
- No backend: parsing de formatos de codificação compactos (ex.: decodificar identificadores curtos que usam marcadores especiais para valores "estendidos", como códigos de país de 1 vs 2 dígitos em sistemas de telefonia).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
