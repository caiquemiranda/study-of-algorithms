# [1624] Largest Substring Between Two Equal Characters

> 🔗 [LeetCode 1624](https://leetcode.com/problems/largest-substring-between-two-equal-characters/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s`, retorne o comprimento da maior substring entre dois caracteres iguais, excluindo os dois caracteres. Se não existir tal substring, retorne `-1`.

**Exemplos:**
```
Input:  s = "aa"
Output: 0
Explicação: a substring ótima aqui é uma substring vazia entre os dois 'a's.

Input:  s = "abca"
Output: 2
Explicação: a substring ótima aqui é "bc".

Input:  s = "cbzxy"
Output: -1
Explicação: não há caracteres que aparecem duas vezes em s.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 300` → pequeno, O(n) resolve com folga
- só letras minúsculas → mapa fixo de 26 posições possível, mas hash map genérico também funciona bem

## 🧭 Como reconhecer o padrão

"Maior distância entre duas ocorrências do MESMO caractere" é resolvido guardando a PRIMEIRA ocorrência de cada caractere num hash map; ao encontrar uma ocorrência REPETIDA, calcule a distância até a primeira e atualize o máximo — não precisa comparar todos os pares de ocorrências, só a primeira contra a mais distante é suficiente.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de índices `(i,j)` com `i<j` e `s[i]==s[j]`, calcular `j-i-1` e manter o máximo.

- Tempo: O(n²) — todos os pares de índices possíveis · Espaço: O(1) extra
- **Por que não basta:** para maximizar a distância entre duas ocorrências do MESMO caractere, só a primeira e a última ocorrência interessam; comparar todos os pares intermediários é redundante.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `s` guardando num hash map `caractere → primeiro índice visto`. Ao encontrar um caractere que JÁ está no mapa, calcule `i - primeiraOcorrencia[caractere] - 1` e atualize o máximo (sem nunca atualizar a primeira ocorrência registrada).

## 🎬 Exemplo passo a passo

`s = "abca"`

| Passo | i | s[i] | já no mapa? | Ação | maximo |
|---|---|---|---|---|---|
| 1 | 0 | a | não | registra primeira[a]=0 | -1 |
| 2 | 1 | b | não | registra primeira[b]=1 | -1 |
| 3 | 2 | c | não | registra primeira[c]=2 | -1 |
| 4 | 3 | a | sim (primeira[a]=0) | distância = 3-0-1=2 | 2 |

Resultado final: `2` ✔ ("bc" entre os dois 'a's)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) extra (mapa de no máximo 26 letras)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxLengthBetweenEqualCharacters(String s) {
    Map<Character, Integer> primeiraOcorrencia = new HashMap<>();
    int maximo = -1;

    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (primeiraOcorrencia.containsKey(c)) {
            int distancia = i - primeiraOcorrencia.get(c) - 1;
            maximo = Math.max(maximo, distancia);
        } else {
            primeiraOcorrencia.put(c, i); // só registra a PRIMEIRA vez que vê este caractere
        }
    }
    return maximo;
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

- Atualizar `primeiraOcorrencia[c]` toda vez que o caractere reaparece (em vez de só na primeira vez) — isso perderia a referência à ocorrência mais ANTIGA, que é justamente a que maximiza a distância.
- Esquecer o `- 1` no cálculo da distância — a pergunta é sobre o tamanho da substring ENTRE os dois caracteres, excluindo-os, não a diferença bruta de índices.
- Inicializar `maximo` como `0` em vez de `-1` — o enunciado pede retornar `-1` se nenhum caractere se repetir; usar `0` esconderia esse caso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caracteres adjacentes | "aa" | 0 | substring vazia entre os dois 'a's |
| Caso padrão | "abca" | 2 | "bc" entre os dois 'a's |
| Sem repetição | "cbzxy" | -1 | nenhum caractere aparece duas vezes |
| Múltiplas repetições, mesma letra | "abcaa" | 3 | usa a PRIMEIRA (índice 0) e a ÚLTIMA ocorrência processada (índice 4) de 'a' |

## 🔗 Conexões

- Problemas irmãos: [0387] First Unique Character in a String (mesmo uso de mapa de primeira ocorrência), [0003] Longest Substring Without Repeating Characters (mesmo domínio de rastrear posições de caracteres com hash map)
- No backend: análise de logs para medir o intervalo entre duas ocorrências do mesmo evento (ex.: tempo entre duas requisições do mesmo usuário, ou distância entre duas menções do mesmo identificador num fluxo de dados).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
