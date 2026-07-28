# [2109] Adding Spaces to a String

> 🔗 [LeetCode 2109](https://leetcode.com/problems/adding-spaces-to-a-string/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Simulation` `#Medium`

## 📜 O Problema

Dada uma string `s` e um array `spaces` (índices estritamente crescentes), insira um espaço **antes** do caractere em cada índice de `spaces`. Retorne a string resultante.

**Exemplos:**
```
Input:  s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"

Input:  s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length, spaces.length <= 3 * 10^5` → O(n+m) é o esperado, qualquer deslocamento repetido de caracteres seria caro demais
- `spaces` já vem **estritamente crescente** → permite processar as posições de espaço em ordem, sem precisar ordenar nem revisitar
- Espaço vai **antes** do caractere no índice indicado → define exatamente o ponto de inserção em cada posição

## 🧭 Como reconhecer o padrão

"Mesclar uma sequência de caracteres com uma lista ordenada de posições de inserção" é o mesmo padrão de merge de [2570] Merge Two 2D Arrays by Summing Values: dois ponteiros avançam juntos — um percorre `s` caractere por caractere, o outro acompanha `spaces` verificando se a posição atual é onde um espaço deve entrar.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição em `spaces`, inserir um espaço na string usando `StringBuilder.insert(indice, ' ')`, processando os índices do MAIOR para o MENOR (para não invalidar os índices seguintes conforme a string cresce).

- Tempo: O(n×m) no pior caso — cada `insert` desloca todos os caracteres depois da posição inserida · Espaço: O(n) para a string em construção
- **Por que não basta:** cada inserção individual custa O(n) por deslocar o restante da string; construir o resultado numa única passada com um `StringBuilder` que só faz `append` (nunca desloca nada) resolve em tempo linear.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `i` percorrendo `s` do início ao fim e `j` acompanhando `spaces`. A cada posição `i`, se `spaces[j] == i`, anexe um espaço ao resultado ANTES do caractere, e avance `j`. Sempre anexe `s.charAt(i)` em seguida. Como `spaces` já está ordenado, `j` nunca precisa voltar — ele só avança conforme os espaços vão sendo "usados".

## 🎬 Exemplo passo a passo

`s = "icodeinpython"`, `spaces = [1,5,7,9]`

| Passo | i | Evento | Resultado parcial |
|---|---|---|---|
| 1 | 0 | sem espaço, anexa `'i'` | `"i"` |
| 2 | 1 | `spaces[0]=1` bate → anexa `' '` + `'c'` | `"i c"` |
| 3 | 2–4 | sem espaço, anexa `'o'`,`'d'`,`'e'` | `"i code"` |
| 4 | 5 | `spaces[1]=5` bate → anexa `' '` + `'i'` | `"i code i"` |
| 5 | 6 | sem espaço, anexa `'n'` | `"i code in"` |
| 6 | 7 | `spaces[2]=7` bate → anexa `' '` + `'p'` | `"i code in p"` |
| 7 | 8 | sem espaço, anexa `'y'` | `"i code in py"` |
| 8 | 9 | `spaces[3]=9` bate → anexa `' '` + `'t'` | `"i code in py t"` |
| 9 | 10–12 | sem espaço, anexa `'h'`,`'o'`,`'n'` | `"i code in py thon"` |

Resultado final: `"i code in py thon"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — `i` percorre `s` uma vez, `j` percorre `spaces` uma vez, juntos
- **Espaço:** O(n + m) para o resultado (exigido pelo problema)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String addSpaces(String s, int[] spaces) {
    StringBuilder sb = new StringBuilder();
    int j = 0; // ponteiro no array de posições de espaço
    int m = spaces.length;

    for (int i = 0; i < s.length(); i++) {
        if (j < m && spaces[j] == i) {
            sb.append(' ');
            j++;
        }
        sb.append(s.charAt(i));
    }

    return sb.toString();
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

- Inserir espaços diretamente na string original do início pro fim sem ajustar os índices — cada espaço inserido desloca todos os índices seguintes em 1 posição; construir o resultado do zero com dois ponteiros evita esse problema por completo.
- Esquecer de checar `j < m` antes de acessar `spaces[j]` — depois que todos os espaços já foram inseridos, continuar acessando o array de posições fora dos limites quebra o código.
- Adicionar o espaço DEPOIS do caractere em vez de ANTES — o enunciado é explícito: o espaço vai antes do caractere na posição indicada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Múltiplos espaços | `s="LeetcodeHelpsMeLearn"`, `spaces=[8,13,15]` | `"Leetcode Helps Me Learn"` | três espaços inseridos em posições distintas |
| Espaço no início | `s="spacing"`, `spaces=[0,1,2,3,4,5,6]` | `" s p a c i n g"` | espaço antes de CADA caractere, incluindo o primeiro |
| Um único espaço | `s="ab"`, `spaces=[1]` | `"a b"` | caso mínimo |
| Espaço só no final | `s="hello"`, `spaces=[4]` | `"hell o"` | espaço só antes do último caractere |

## 🔗 Conexões

- Problemas irmãos: [2570] Merge Two 2D Arrays by Summing Values (mesma técnica de mesclar duas sequências ordenadas com dois ponteiros), [0088] Merge Sorted Array (mesma família de merge guiado por posição)
- No backend: formatação de texto/templates inserindo delimitadores em posições pré-calculadas — por exemplo, inserir separadores de milhar num número grande, ou tags de marcação em posições específicas de um texto, tudo numa única passada sem deslocar dados repetidamente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
