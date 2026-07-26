# [0125] Valid Palindrome

> 🔗 [LeetCode 125](https://leetcode.com/problems/valid-palindrome/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Uma frase é um **palíndromo** se, depois de converter todas as letras maiúsculas em minúsculas e remover todos os caracteres não alfanuméricos, ela lê igual de trás para frente. Dada uma string `s`, retorne `true` se ela for um palíndromo.

**Exemplos:**
```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
Explicação: "amanaplanacanalpanama" é palíndromo.

Input:  s = "race a car"
Output: false
Explicação: "raceacar" não é palíndromo.

Input:  s = " "
Output: true
Explicação: fica string vazia após a limpeza; vazia é palíndromo por vacuidade.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 2 * 10^5` → O(n²) (comparar tudo com tudo) é arriscado; O(n) é o esperado
- `s` consiste só de caracteres ASCII imprimíveis → inclui pontuação, espaços e símbolos que precisam ser ignorados, não só letras/dígitos
- Definição explícita de "ignorar case e caracteres não alfanuméricos" → a comparação nunca é direta, sempre passa por uma normalização por caractere

## 🧭 Como reconhecer o padrão

"Verificar se algo lê igual de trás para frente" é a assinatura mais clássica de dois ponteiros nas pontas: um ponteiro `left` no início, outro `right` no fim, andando um em direção ao outro até se cruzarem. Aqui, com o adicional de pular caracteres inválidos antes de cada comparação.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Construir uma nova string só com os caracteres alfanuméricos em minúsculas, e depois comparar essa string com sua própria versão invertida (ou reverter e comparar caractere a caractere).

- Tempo: O(n) · Espaço: O(n) — precisa guardar a string limpa (e possivelmente sua reversa)
- **Por que não basta:** funciona, mas gasta O(n) de espaço extra construindo uma cópia limpa da string; dois ponteiros conseguem fazer a mesma verificação em uma única passada sobre a string **original**, sem alocar nada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` começando no índice 0 e `right` no último índice. Antes de comparar, avance `left` enquanto o caractere não for alfanumérico, e recue `right` enquanto o dele também não for. Quando ambos apontarem para caracteres válidos, compare-os (ignorando case); se forem diferentes, não é palíndromo. Se forem iguais, avance `left` e recue `right`, repetindo até eles se cruzarem.

## 🎬 Exemplo passo a passo

`s = "race a car"` (índices 0 a 9: `r,a,c,e,' ',a,' ',c,a,r`)

| Passo | left | right | Ação/Comparação |
|---|---|---|---|
| 1 | 0 (`r`) | 9 (`r`) | ambos alfanuméricos, iguais → avança: left=1, right=8 |
| 2 | 1 (`a`) | 8 (`a`) | iguais → left=2, right=7 |
| 3 | 2 (`c`) | 7 (`c`) | iguais → left=3, right=6 |
| 4 | 3 (`e`) | 6 (`' '`) | `right` não é alfanumérico → recua: right=5 |
| 5 | 3 (`e`) | 5 (`a`) | `e` ≠ `a` → **retorna false** |

Resultado final: `false` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — os dois ponteiros juntos percorrem a string no máximo uma vez
- **Espaço:** O(1) — só os índices `left` e `right`, sem string nova

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isPalindrome(String s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        // pula caracteres que não são letra nem dígito, dos dois lados
        while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
            left++;
        }
        while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
            right--;
        }
        // compara ignorando maiúscula/minúscula, conforme a definição do problema
        if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
            return false;
        }
        left++;
        right--;
    }

    return true; // ponteiros se cruzaram sem nenhum mismatch
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

- Esquecer de normalizar case antes de comparar — comparar `'A'` com `'a'` sem `toLowerCase` faz uma frase válida ser rejeitada incorretamente.
- Pular caracteres inválidos de só um lado antes de comparar — os dois ponteiros precisam estar cada um sobre um caractere alfanumérico **antes** da comparação, senão eles desalinham.
- Achar que uma string sem nenhuma letra/dígito (ex.: `" "` ou `",,,"`) deveria dar erro — pela definição do problema, ela fica vazia após a limpeza, e string vazia é palíndromo por vacuidade (`true`); a condição `left < right` do loop já cobre isso automaticamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Frase clássica | `"A man, a plan, a canal: Panama"` | true | ignora espaços, pontuação e case |
| Quase palíndromo | `"race a car"` | false | mismatch no meio depois de ignorar espaços |
| Só espaço | `" "` | true | fica vazia após limpeza, vazio é palíndromo |
| Um único caractere | `"a"` | true | `left == right`, o loop nem chega a comparar |

## 🔗 Conexões

- Problemas irmãos: [0680] Valid Palindrome II (mesma técnica, mas permite remover até 1 caractere para virar palíndromo), [0009] Palindrome Number (mesmo conceito, aplicado a número em vez de string)
- No backend: validação de dados "canônicos" ignorando formatação — por exemplo, comparar dois números de documento ou telefone digitados com pontuação/espaços diferentes usa a mesma ideia de normalizar e comparar de fora para dentro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
