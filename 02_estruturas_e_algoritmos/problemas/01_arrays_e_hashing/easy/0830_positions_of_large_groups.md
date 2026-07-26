# [0830] Positions of Large Groups

> 🔗 [LeetCode 830](https://leetcode.com/problems/positions-of-large-groups/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Numa string `s` de letras minúsculas, letras iguais consecutivas formam grupos. Por exemplo, `s = "abbxxxxzyy"` tem os grupos `"a"`, `"bb"`, `"xxxx"`, `"z"` e `"yy"`.

Um grupo é identificado por um intervalo `[start, end]` (índices inclusivos). Um grupo é considerado **grande** se tem 3 ou mais caracteres. Retorne os intervalos de todo grupo grande, ordenados por índice inicial crescente.

**Exemplos:**
```
Input:  s = "abbxxxxzzy"
Output: [[3,6]]
Explicação: "xxxx" é o único grupo grande, com índice inicial 3 e final 6.

Input:  s = "abc"
Output: []
Explicação: os grupos são "a", "b", "c", nenhum grande.

Input:  s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explicação: os grupos grandes são "ddd", "eeee" e "bbb".
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 1000` → O(n) resolve com folga
- só letras minúsculas → sem complicação de caixa
- grupo "grande" = 3+ caracteres → threshold fixo simples

## 🧭 Como reconhecer o padrão

"Identifique grupos consecutivos do mesmo caractere e reporte os intervalos que satisfazem uma condição de tamanho" é resolvido rastreando o início do grupo atual e comparando com o caractere anterior — quando o caractere muda (ou a string acaba), fecha o grupo e verifica o tamanho.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, expandir para a direita enquanto `s[j] == s[i]`, redescobrindo o grupo inteiro a cada nova posição inicial testada.

- Tempo: O(n²) — repete a expansão a partir de cada índice dentro do mesmo grupo já visitado · Espaço: O(1) fora a lista de resultado
- **Por que não basta:** se um grupo tem 100 caracteres iguais, testar cada uma das 100 posições internas como "possível início" refaz o mesmo trabalho de expansão repetidamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma única passada com um ponteiro `inicioGrupo`. Sempre que `s[i] != s[i-1]` (ou `i` chega ao fim da string), o grupo que vai de `inicioGrupo` até `i-1` terminou; se seu tamanho é ≥ 3, registre o intervalo. Atualize `inicioGrupo = i` para o próximo grupo.

## 🎬 Exemplo passo a passo

`s = "abcdddeeeeaabbbcd"`

| Passo | grupo (char) | intervalo | tamanho | é grande (>=3)? | registra? |
|---|---|---|---|---|---|
| 1 | a | [0,0] | 1 | não | — |
| 2 | b | [1,1] | 1 | não | — |
| 3 | c | [2,2] | 1 | não | — |
| 4 | d | [3,5] | 3 | sim | [3,5] |
| 5 | e | [6,9] | 4 | sim | [6,9] |
| 6 | a | [10,11] | 2 | não | — |
| 7 | b | [12,14] | 3 | sim | [12,14] |
| 8 | c | [15,15] | 1 | não | — |
| 9 | d | [16,16] | 1 | não | — |

Resultado final: `[[3,5],[6,9],[12,14]]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) extra (fora a lista de resultado, proporcional ao número de grupos grandes)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<List<Integer>> largeGroupPositions(String s) {
    List<List<Integer>> resultado = new ArrayList<>();
    int inicioGrupo = 0;

    for (int i = 1; i <= s.length(); i++) {
        // grupo termina quando o caractere muda, ou quando a string acaba
        if (i == s.length() || s.charAt(i) != s.charAt(inicioGrupo)) {
            int fimGrupo = i - 1;
            if (fimGrupo - inicioGrupo + 1 >= 3) {
                resultado.add(Arrays.asList(inicioGrupo, fimGrupo));
            }
            inicioGrupo = i; // começa o próximo grupo a partir daqui
        }
    }
    return resultado;
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

- Esquecer de fechar o ÚLTIMO grupo quando a string termina — o loop precisa ir até `i == s.length()` (não só `s.length() - 1`) para capturar o grupo final, senão um grupo grande no fim da string é perdido.
- Usar `> 3` em vez de `>= 3` — o enunciado define grupo grande como "3 ou mais caracteres", então tamanho exatamente 3 já conta.
- Calcular o tamanho do grupo como `fimGrupo - inicioGrupo` sem o `+ 1` — erro clássico de off-by-one ao converter índices em tamanho de intervalo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Grupo grande no meio | `"abbxxxxzzy"` | [[3,6]] | só "xxxx" tem 4+ caracteres |
| Sem grupos grandes | `"abc"` | [] | todos os grupos têm tamanho 1 |
| Vários grupos grandes | `"abcdddeeeeaabbbcd"` | [[3,5],[6,9],[12,14]] | caso padrão do enunciado |
| Grupo grande no final | `"aabbb"` | [[2,4]] | precisa fechar o grupo ao terminar a string |

## 🔗 Conexões

- Problemas irmãos: [0551] Student Attendance Record I (mesmo padrão de contar sequências consecutivas), [0443] String Compression (mesma técnica de agrupar caracteres consecutivos, mas para compactar em vez de filtrar)
- No backend: detecção de rajadas em sequências de eventos (ex.: identificar períodos de 3+ falhas consecutivas em um log de status, ou sequências longas repetidas em dados de sensores).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
