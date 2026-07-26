# [0345] Reverse Vowels of a String

> 🔗 [LeetCode 345](https://leetcode.com/problems/reverse-vowels-of-a-string/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s`, reverta **só as vogais** dentro dela e retorne o resultado. As vogais são `a, e, i, o, u`, em maiúscula ou minúscula, podendo repetir.

**Exemplos:**
```
Input:  s = "IceCreAm"
Output: "AceCreIm"
Explicação: as vogais são ['I','e','e','A']; revertidas, ficam ['A','e','e','I'].

Input:  s = "leetcode"
Output: "leotcede"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 3 * 10^5` → O(n) esperado
- Vogais em maiúscula OU minúscula, "mais de uma vez" → a detecção de vogal precisa cobrir os dois casos, e o mesmo caractere pode aparecer várias vezes

## 🧭 Como reconhecer o padrão

"Reverter só um subconjunto de posições de uma sequência, mantendo o resto fixo" ainda é dois ponteiros nas pontas — a diferença de [0344] Reverse String é que os ponteiros precisam **pular** (avançar/recuar) por cima de qualquer caractere que não pertença ao subconjunto de interesse (aqui, as consoantes), só trocando quando os dois estiverem sobre vogais.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Percorrer a string uma vez coletando todas as vogais encontradas numa lista, inverter essa lista, e percorrer a string de novo substituindo cada posição de vogal pelo próximo elemento da lista invertida.

- Tempo: O(n) · Espaço: O(k), onde k é a quantidade de vogais (pode chegar a O(n) se a string for só vogais)
- **Por que não basta:** exige **duas passadas completas** pela string e uma lista auxiliar guardando as vogais; dois ponteiros convergindo das pontas resolvem numa única passada, sem coletar nada — trocam direto quando encontram uma vogal de cada lado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no início e `right` no fim (sobre um `char[]`, já que strings em Java são imutáveis). Avance `left` enquanto o caractere não for vogal; recue `right` enquanto o dele também não for. Quando os dois pararem sobre vogais, troque-as e continue. Repita até `left` cruzar `right`.

## 🎬 Exemplo passo a passo

`s = "leetcode"` (índices 0 a 7: `l,e,e,t,c,o,d,e`)

| Passo | left | right | Ação |
|---|---|---|---|
| 1 | 0 → 1 | 7 | `s[0]='l'` não é vogal, avança; `s[1]='e'` é vogal, para |
| 2 | 1 | 7 | `s[7]='e'` já é vogal, mantém |
| 3 | 1 | 7 | troca `s[1]` com `s[7]` (ambos `'e'`, sem mudança visível); left=2, right=6 |
| 4 | 2 | 6 → 5 | `s[2]='e'` já é vogal; `s[6]='d'` não é vogal, recua; `s[5]='o'` é vogal, para |
| 5 | 2 | 5 | troca `s[2]` com `s[5]` (`'e'` ↔ `'o'`); left=3, right=4 |
| 6 | 3 → 5 | 4 | `s[3]='t'`, `s[4]='c'` não são vogais, `left` avança até 5 |
| 7 | 5 | 4 | `left(5) > right(4)` → loop termina |

Resultado final: `"leotcede"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — os dois ponteiros juntos percorrem a string no máximo uma vez
- **Espaço:** O(n) só para o `char[]` (necessário em Java por strings serem imutáveis); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
private static final Set<Character> VOGAIS = Set.of('a','e','i','o','u','A','E','I','O','U');

public String reverseVowels(String s) {
    char[] arr = s.toCharArray();
    int left = 0;
    int right = arr.length - 1;

    while (left < right) {
        // pula qualquer caractere que não seja vogal, dos dois lados
        while (left < right && !VOGAIS.contains(arr[left])) {
            left++;
        }
        while (left < right && !VOGAIS.contains(arr[right])) {
            right--;
        }
        if (left < right) {
            char tmp = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp;
            left++;
            right--;
        }
    }

    return new String(arr);
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

- Esquecer que vogais podem ser maiúsculas ou minúsculas — o conjunto de vogais precisa cobrir os dois casos; ignorar isso faz `"IceCreAm"` não reverter o `'I'`/`'A'` corretamente.
- Confundir "reverter as vogais" com "reverter a string toda e filtrar" — só o **conteúdo** das posições que são vogais é trocado entre si; a posição das consoantes nunca muda.
- Não checar `left < right` antes do swap final — depois dos dois `while` internos de pular caracteres, é possível que `left` já tenha alcançado ou passado `right` (quando não sobra nenhuma vogal pra comparar); trocar sem essa checagem faz um swap indevido.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Vogais maiúsculas e minúsculas | `"IceCreAm"` | `"AceCreIm"` | testa detecção case-insensitive |
| Caso padrão | `"leetcode"` | `"leotcede"` | mistura de vogal simétrica (sem mudança visível) e assimétrica |
| Sem vogais | `"xyz"` | `"xyz"` | os ponteiros se cruzam sem nunca achar uma vogal pra trocar |
| Só vogais | `"aeiou"` | `"uoiea"` | equivalente a reverter a string inteira |

## 🔗 Conexões

- Problemas irmãos: [0344] Reverse String (mesma técnica, mas reverte TODOS os caracteres, não só um subconjunto), [0151] Reverse Words in a String (também reorganiza partes específicas da string mantendo outras fixas)
- No backend: transformação seletiva de um subconjunto de caracteres/tokens dentro de um payload maior, preservando o restante do formato intacto (ex.: mascarar ou reordenar apenas certos campos de um texto sem afetar sua estrutura geral).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
