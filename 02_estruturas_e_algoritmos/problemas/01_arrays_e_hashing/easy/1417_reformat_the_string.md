# [1417] Reformat The String

> 🔗 [LeetCode 1417](https://leetcode.com/problems/reformat-the-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Você recebe uma string alfanumérica `s` (formada por letras minúsculas e dígitos). Encontre uma permutação da string onde nenhuma letra é seguida por outra letra e nenhum dígito é seguido por outro dígito — ou seja, dois caracteres adjacentes nunca têm o mesmo tipo.

Retorne a string reformatada, ou uma string vazia se for impossível reformatar.

**Exemplos:**
```
Input:  s = "a0b1c2"
Output: "0a1b2c"
Explicação: nenhum caractere adjacente tem o mesmo tipo em "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b"
também são permutações válidas.

Input:  s = "leetcode"
Output: ""
Explicação: "leetcode" só tem letras, então não dá para separá-las com dígitos.

Input:  s = "1229857369"
Output: ""
Explicação: "1229857369" só tem dígitos, então não dá para separá-los com letras.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 500` → pequeno, O(n) resolve com folga
- caracteres são só letras minúsculas e dígitos → só 2 "tipos" possíveis, simplifica a lógica de alternância
- "impossível" precisa ser detectado quando as contagens dos dois tipos diferem em mais de 1

## 🧭 Como reconhecer o padrão

"Intercalar dois tipos de caracteres sem dois do mesmo tipo adjacentes" é resolvido separando os caracteres em dois grupos (letras e dígitos), e verificando se a diferença de tamanho entre os grupos é no máximo 1 — se for, intercale-os começando pelo grupo maior (ou qualquer um, se os tamanhos forem iguais).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Tentar todas as permutações possíveis da string, verificando para cada uma se ela satisfaz "nenhum tipo igual adjacente".

- Tempo: O(n!) — todas as permutações da string · Espaço: O(n!) no pior caso
- **Por que não basta:** astronomicamente inviável mesmo para n pequeno; o problema tem uma estrutura muito mais simples do que "testar todas as ordens possíveis" sugere.

## 💡 Solução 2 — A ideia otimizada (intuição)

Separe os caracteres de `s` em duas listas: `letras` e `digitos`. Se `|letras.length - digitos.length| > 1`, é impossível, retorne `""`. Caso contrário, intercale os dois grupos, colocando o grupo MAIOR primeiro (ou qualquer um, se forem do mesmo tamanho).

## 🎬 Exemplo passo a passo

`s = "a0b1c2"` — `letras = [a,b,c]`, `digitos = [0,1,2]` (ambos tamanho 3, diferença 0, válido)

| Passo | Fonte | caractere | resultado parcial |
|---|---|---|---|
| 1 | digitos[0] | 0 | 0 |
| 2 | letras[0] | a | 0a |
| 3 | digitos[1] | 1 | 0a1 |
| 4 | letras[1] | b | 0a1b |
| 5 | digitos[2] | 2 | 0a1b2 |
| 6 | letras[2] | c | 0a1b2c |

Resultado final: `"0a1b2c"` ✔ (uma das permutações válidas aceitas pelo enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para separar + uma passada para intercalar
- **Espaço:** O(n) — para as duas listas e o resultado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String reformat(String s) {
    StringBuilder letras = new StringBuilder();
    StringBuilder digitos = new StringBuilder();
    for (char c : s.toCharArray()) {
        if (Character.isDigit(c)) {
            digitos.append(c);
        } else {
            letras.append(c);
        }
    }

    if (Math.abs(letras.length() - digitos.length()) > 1) {
        return ""; // impossível intercalar sem dois do mesmo tipo adjacentes
    }

    // garante que 'maior' seja o grupo com mais (ou igual) elementos, para começar por ele
    StringBuilder maior = letras.length() >= digitos.length() ? letras : digitos;
    StringBuilder menor = letras.length() >= digitos.length() ? digitos : letras;

    StringBuilder resultado = new StringBuilder();
    for (int i = 0; i < menor.length(); i++) {
        resultado.append(maior.charAt(i));
        resultado.append(menor.charAt(i));
    }
    if (maior.length() > menor.length()) {
        resultado.append(maior.charAt(maior.length() - 1)); // sobra 1 caractere do grupo maior no final
    }
    return resultado.toString();
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

- Esquecer de verificar `|letras.length - digitos.length| > 1` antes de tentar intercalar — sem essa checagem, o código poderia gerar uma string com dois caracteres do mesmo tipo adjacentes no final, ou lançar exceção de índice.
- Sempre começar pelas letras (ou sempre pelos dígitos) sem checar qual grupo é maior — se o grupo menor for usado primeiro quando os tamanhos diferem em 1, sobra um caractere do grupo maior que não tem "parceiro" para intercalar corretamente no início.
- Confundir "impossível" com "resultado vazio por entrada vazia" — `""` como retorno é o sinal específico de impossibilidade, não uma entrada vazia (o enunciado garante `s.length >= 1`).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado (uma resposta válida) | Por quê |
|---|---|---|---|
| Grupos de tamanho igual | `"a0b1c2"` | "0a1b2c" | 3 letras e 3 dígitos, intercalação perfeita |
| Só letras | `"leetcode"` | "" | nenhum dígito para intercalar, impossível |
| Só dígitos | `"1229857369"` | "" | nenhuma letra para intercalar, impossível |
| Diferença de 1 no tamanho | `"ab123"` | uma intercalação como "1a2b3" | 2 letras e 3 dígitos, o grupo maior (dígitos) começa e termina |

## 🔗 Conexões

- Problemas irmãos: [1370] Increasing Decreasing String (mesmo domínio de reconstruir string com regras de alternância a partir de contagens), [0767] Reorganize String (mesma ideia de "nenhum tipo igual adjacente", mas com múltiplos tipos de caracteres em vez de só 2)
- No backend: geração de senhas ou códigos que exigem alternância entre categorias de caracteres (ex.: "não pode ter dois dígitos seguidos") como parte de uma política de formatação de identificadores.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
