# [0744] Find Smallest Letter Greater Than Target

> 🔗 [LeetCode 744](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array `letters` de caracteres, ordenado de forma **não decrescente**, com **pelo menos duas letras diferentes**, e um caractere `target`. Retorne a **menor letra** de `letters` que é lexicograficamente **maior** que `target`. Se não existir nenhuma (target é maior ou igual a todas), retorne a **primeira letra** do array (comportamento circular).

**Exemplos:**
```
Input:  letters = ["c","f","j"], target = "a"    Output: "c"
Input:  letters = ["c","f","j"], target = "c"    Output: "f"   (não pode ser igual, precisa ser MAIOR)
Input:  letters = ["x","x","y","y"], target = "z" Output: "x"   (nada é maior que 'z' -> volta pro início)
```

**Restrições (e o que elas denunciam):**
- `2 <= letters.length <= 10^4` → O(n) passaria, mas existe algo melhor dado que o array já está ordenado
- "letters is sorted in non-decreasing order" → sinal direto de busca binária
- "contains at least two different characters" → garante que sempre existe uma "próxima" letra distinta possível, simplificando a lógica de fallback
- Precisa ser **estritamente maior**, não `>=` → muda a busca de "lower bound" para **"upper bound"**

## 🧭 Como reconhecer o padrão

"Array ordenado" + "ache o menor elemento estritamente maior que X" é a busca binária por **upper bound** (fronteira superior): a primeira posição onde a condição `letters[i] > target` passa a ser verdadeira.

## 🐢 Solução 1 — Força bruta

Percorrer o array da esquerda para a direita e retornar o primeiro caractere `> target`; se chegar ao fim sem achar, retornar `letters[0]`.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** funciona, mas ignora que o array está ordenado — a mesma resposta pode ser encontrada descartando metade dos candidatos a cada comparação em vez de andar um por um.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça busca binária pela primeira posição onde `letters[mid] > target`:
- Se `letters[mid] > target`, `mid` é um candidato válido, mas pode existir um candidato melhor (mais à esquerda) → guarda `mid` e busca à **esquerda** (`right = mid - 1`).
- Se `letters[mid] <= target` (menor OU igual — repare que aqui igual não serve, diferente de "lower bound"), descarta `mid` e tudo antes dele → busca à **direita** (`left = mid + 1`).

Se, ao final, nenhum candidato foi guardado (ou seja, `left` ultrapassou o array), o comportamento circular manda retornar `letters[0]`.

## 🎬 Exemplo passo a passo

`letters = ["c","f","j"]`, `target = "c"`

| Passo | left | mid | right | Comparação | Decisão |
|---|---|---|---|---|---|
| 1 | 0 ('c') | 1 ('f') | 2 ('j') | 'f' > 'c' → candidato válido | guarda 'f', `right = 0` |
| 2 | 0 ('c') | 0 ('c') | 0 ('c') | 'c' <= 'c' → não serve | `left = 1` |
| 3 | 1 | — | 0 | `left > right` → fim | retorna candidato guardado: 'f' |

Resultado final: `"f"` ✔ (repare que 'c' não conta mesmo sendo igual ao target)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do espaço de busca
- **Espaço:** O(1) — dois/três ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public char nextGreatestLetter(char[] letters, char target) {
    int left = 0, right = letters.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (letters[mid] > target) {
            // mid é candidato (estritamente maior), mas pode existir um menor à esquerda
            right = mid - 1;
        } else {
            // letters[mid] <= target: mid não serve (precisa ser ESTRITAMENTE maior)
            left = mid + 1;
        }
    }
    // "left" aponta para a primeira posição > target. Se passou do fim do array,
    // o comportamento circular exige voltar para letters[0].
    return letters[left % letters.length];
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

- **Usar `>=` em vez de `>` na comparação**: o problema pede estritamente maior — se `letters[mid] == target`, ele NÃO serve como resposta (ver exemplo 2, onde `target = 'c'` e a resposta é `'f'`, não `'c'`).
- **Esquecer o comportamento circular**: se `target` é maior ou igual a todas as letras, a resposta correta é voltar para `letters[0]` — o `% letters.length` no índice final resolve isso de forma elegante sem `if` extra.
- **Achar que precisa tratar duplicatas de forma especial**: duplicatas (`["x","x","y","y"]`) não quebram a busca binária por upper bound — o algoritmo naturalmente pula por cima delas.
- **Comparar `char` como se fosse necessário conversão manual**: em Java, `char` já compara como número (código ASCII) com os operadores `<`, `>`, `==` diretamente — não precisa de `.compareTo()`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Target menor que tudo | `letters=["c","f","j"], target="a"` | "c" | primeiro elemento já serve |
| Target igual a um elemento | `letters=["c","f","j"], target="c"` | "f" | 'c' não conta, precisa ser estritamente maior |
| Target maior que tudo (circular) | `letters=["x","x","y","y"], target="z"` | "x" | fallback para o início |
| Todas iguais exceto uma | `letters=["a","a","a","b"], target="a"` | "b" | testa pular sobre duplicatas |
| Duas letras, borda mínima | `letters=["a","b"], target="a"` | "b" | menor array válido pela restrição |

## 🔗 Conexões

- Problemas irmãos: **[0035] Search Insert Position** (busca por lower bound, contraste direto com este upper bound), **[2529] Maximum Count of Positive Integer and Negative Integer** (mesma técnica de fronteira aplicada a números)
- No backend: "ache o próximo valor válido maior que X, com wraparound" é o mesmo padrão de agendadores circulares (round-robin) e de estruturas como relógios/hash rings consistentes, onde você busca o próximo nó no anel que vem depois de uma chave, voltando ao início se necessário.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
