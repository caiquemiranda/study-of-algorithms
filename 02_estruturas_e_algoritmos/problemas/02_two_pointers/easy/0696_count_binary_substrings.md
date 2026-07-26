# [0696] Count Binary Substrings

> 🔗 [LeetCode 696](https://leetcode.com/problems/count-binary-substrings/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string binária `s`, retorne o número de substrings não-vazias que têm a mesma quantidade de `0`s e `1`s, com todos os `0`s e todos os `1`s **agrupados consecutivamente**. Substrings repetidas contam cada vez que aparecem.

**Exemplos:**
```
Input:  s = "00110011"
Output: 6
Explicação: "0011", "01", "1100", "10", "0011", "01" (algumas repetem)

Input:  s = "10101"
Output: 4
Explicação: "10", "01", "10", "01"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n²) ou pior (checar substring por substring) é arriscado; O(n) é o esperado
- `s[i]` é `'0'` ou `'1'` → só dois valores possíveis, o que faz a string naturalmente se dividir em **grupos** de caracteres repetidos (ex.: `"00110011"` → grupos `00`, `11`, `00`, `11`)

## 🧭 Como reconhecer o padrão

"Contar algo que depende de blocos consecutivos iguais, comparados com o bloco vizinho" aponta pra percorrer a string marcando o início e o fim de cada **grupo** de caracteres repetidos (um ponteiro fixa o início do grupo, outro avança enquanto o caractere não muda) e comparar o tamanho de cada grupo com o do grupo **anterior** — uma substring válida só pode ser formada por dois grupos vizinhos de valores diferentes.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de índices `(i, j)` com `i <= j`, extrair a substring `s[i..j]` e verificar diretamente se os `0`s e os `1`s dentro dela aparecem agrupados e em quantidades iguais.

- Tempo: O(n³) (O(n²) substrings, O(n) para validar cada uma) · Espaço: O(1) além da substring temporária
- **Por que não basta:** verifica substrings que nunca poderiam ser válidas (qualquer uma que não seja exatamente "metade de um grupo + metade do grupo vizinho"); a estrutura de grupos consecutivos permite calcular a resposta com uma única passada pela string.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra a string agrupando caracteres iguais consecutivos, medindo o tamanho de cada grupo (ex.: em `"00110011"`, os grupos são `00`(2), `11`(2), `00`(2), `11`(2)). Toda substring válida é formada por um grupo e o grupo **imediatamente anterior** — e a quantidade de substrings válidas que esse par de grupos produz é exatamente `min(tamanho do grupo anterior, tamanho do grupo atual)` (você pode "puxar" de 1 a esse mínimo de caracteres de cada lado da fronteira, sempre balanceado). Some esse mínimo a cada nova fronteira entre grupos.

## 🎬 Exemplo passo a passo

`s = "10101"` (grupos: `1`, `0`, `1`, `0`, `1`, todos de tamanho 1)

| Passo | grupo (valor, posição) | curLen | prevLen (antes) | min adicionado | total acumulado |
|---|---|---|---|---|---|
| 1 | `'1'` [0,0] | 1 | 0 | 0 | 0 |
| 2 | `'0'` [1,1] | 1 | 1 | 1 | 1 |
| 3 | `'1'` [2,2] | 1 | 1 | 1 | 2 |
| 4 | `'0'` [3,3] | 1 | 1 | 1 | 3 |
| 5 | `'1'` [4,4] | 1 | 1 | 1 | 4 |

Resultado final: `4` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere é visitado exatamente uma vez, seja marcando início de grupo ou avançando dentro dele
- **Espaço:** O(1) — só o tamanho do grupo atual e do grupo anterior, sem guardar todos os grupos numa lista

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countBinarySubstrings(String s) {
    int n = s.length();
    int i = 0;
    int prevLen = 0; // tamanho do grupo anterior
    int total = 0;

    while (i < n) {
        char atual = s.charAt(i);
        int curLen = 0;
        // conta o tamanho do grupo atual (caracteres iguais consecutivos)
        while (i < n && s.charAt(i) == atual) {
            i++;
            curLen++;
        }
        // toda substring válida vem de combinar o grupo anterior com o atual
        total += Math.min(prevLen, curLen);
        prevLen = curLen;
    }

    return total;
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

- Contar substrings comparando caractere a caractere sem pensar em grupos — leva a soluções O(n²) ou piores, quando o padrão de "grupos consecutivos" permite resolver em uma única passada.
- Esquecer de atualizar `prevLen` a cada novo grupo — ele precisa sempre refletir o tamanho do **último** grupo processado, não do primeiro grupo da string inteira.
- Confundir "grupo" com "substring válida" — um grupo é uma sequência de caracteres IGUAIS (ex.: `"00"`); a substring válida é formada por DOIS grupos ADJACENTES (ex.: `"0011"` ou `"01"`), nunca um grupo isolado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Grupos parelhos | `"00110011"` | 6 | 3 fronteiras entre grupos, cada uma contribuindo 2 |
| Alternado | `"10101"` | 4 | 4 fronteiras, cada uma contribuindo 1 |
| Só um caractere repetido | `"0000"` | 0 | existe só 1 grupo, nenhuma fronteira pra combinar |
| Caso mínimo | `"01"` | 1 | única fronteira, grupos de tamanho 1 cada |

## 🔗 Conexões

- Problemas irmãos: [0485] Max Consecutive Ones (mesma técnica de contar runs consecutivos), [1446] Consecutive Characters (mesma ideia de agrupar por runs de caracteres iguais)
- No backend: compressão RLE (Run-Length Encoding) de dados repetitivos usa exatamente essa contagem de grupos consecutivos — comum em compactação de imagens simples ou logs com valores repetidos em sequência.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
