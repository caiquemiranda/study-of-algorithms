# [0917] Reverse Only Letters

> 🔗 [LeetCode 917](https://leetcode.com/problems/reverse-only-letters/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Dada uma string `s`, reverta-a seguindo estas regras: todo caractere que **não** é letra fica na mesma posição; todas as letras (maiúsculas ou minúsculas) devem ser revertidas entre si.

**Exemplos:**
```
Input:  s = "ab-cd"
Output: "dc-ba"

Input:  s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Input:  s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → entrada pequena, mas O(n) já é a solução natural
- ASCII entre `[33, 122]`, sem `"` ou `\` → inclui dígitos, pontuação e símbolos, todos tratados como "não-letra" e mantidos fixos
- "Maiúscula ou minúscula" contam como letra → a checagem de "é letra" precisa cobrir os dois casos

## 🧭 Como reconhecer o padrão

Este é o mesmo padrão de [0345] Reverse Vowels of a String: "reverter só um subconjunto de posições, mantendo o resto fixo" — dois ponteiros nas pontas que **pulam** qualquer caractere fora do subconjunto de interesse (aqui, tudo que não é letra), só trocando quando ambos estiverem sobre letras.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Percorrer a string coletando todas as letras numa lista, invertê-la, e percorrer a string de novo substituindo cada posição de letra pelo próximo elemento da lista invertida.

- Tempo: O(n) · Espaço: O(k), onde k é a quantidade de letras (pode chegar a O(n))
- **Por que não basta:** exige duas passadas completas e uma lista auxiliar guardando as letras; dois ponteiros convergindo das pontas resolvem numa única passada, sem coletar nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no início e `right` no fim (sobre um `char[]`). Avance `left` enquanto o caractere não for letra; recue `right` enquanto o dele também não for. Quando os dois pararem sobre letras, troque-as e continue até `left` cruzar `right`.

## 🎬 Exemplo passo a passo

`s = "ab-cd"` (índices 0 a 4: `a,b,-,c,d`)

| Passo | left | right | Ação |
|---|---|---|---|
| 1 | 0 (`a`) | 4 (`d`) | ambos são letras, troca → `[d,b,-,c,a]`; left=1, right=3 |
| 2 | 1 (`b`) | 3 (`c`) | ambos são letras, troca → `[d,c,-,b,a]`; left=2, right=2 |
| 3 | 2 | 2 | `left == right`, loop termina (posição do meio é `-`, nunca é tocada) |

Resultado final: `"dc-ba"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — os dois ponteiros juntos percorrem a string no máximo uma vez
- **Espaço:** O(n) para o `char[]` (necessário em Java por strings serem imutáveis); O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String reverseOnlyLetters(String s) {
    char[] arr = s.toCharArray();
    int left = 0;
    int right = arr.length - 1;

    while (left < right) {
        // pula qualquer caractere que não seja letra, dos dois lados
        while (left < right && !Character.isLetter(arr[left])) {
            left++;
        }
        while (left < right && !Character.isLetter(arr[right])) {
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

- Usar `Character.isLetterOrDigit` em vez de `Character.isLetter` — o problema pede reverter só LETRAS; dígitos e símbolos devem ficar fixos (diferente de [0125] Valid Palindrome, que trata letras e dígitos juntos).
- Implementar a checagem "é letra" manualmente comparando intervalos (`'a'-'z'`, `'A'-'Z'`) e esquecer um dos dois casos — `Character.isLetter` já cobre maiúsculas e minúsculas automaticamente.
- Não checar `left < right` antes do swap final — depois dos dois `while` internos de pular caracteres, é possível que `left` já tenha alcançado ou passado `right`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Símbolo no meio | `"ab-cd"` | `"dc-ba"` | o símbolo fica fixo, só as letras trocam de lado |
| Mistura de maiúsc/minúsc | `"a-bC-dEf-ghIj"` | `"j-Ih-gfE-dCba"` | testa que case não afeta a detecção de "é letra" |
| Vários símbolos e dígitos | `"Test1ng-Leet=code-Q!"` | `"Qedo1ct-eeLg=ntse-T!"` | dígitos e símbolos ficam fixos, só as letras se movem |
| Sem letras | `"123-456"` | `"123-456"` | nenhuma letra encontrada, string permanece igual |

## 🔗 Conexões

- Problemas irmãos: [0345] Reverse Vowels of a String (mesma técnica, mas filtrando por vogal em vez de letra), [0344] Reverse String (mesma técnica, revertendo TODOS os caracteres)
- No backend: transformação seletiva de um subconjunto de caracteres dentro de um payload, preservando pontuação/formatação fixa — por exemplo, normalizar só as letras de um identificador mantendo separadores no lugar.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
