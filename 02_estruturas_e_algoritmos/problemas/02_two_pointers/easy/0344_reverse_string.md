# [0344] Reverse String

> 🔗 [LeetCode 344](https://leetcode.com/problems/reverse-string/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Easy`

## 📜 O Problema

Escreva uma função que reverte uma string, dada como um array de caracteres `s`. A modificação deve ser **in-place**, com **O(1)** de memória extra.

**Exemplos:**
```
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n) esperado
- Exige **in-place** com **O(1)** de memória extra → proíbe criar uma nova string/array reverso, e desaconselha recursão (cada chamada empilha um frame, custando espaço proporcional a n na pilha)

## 🧭 Como reconhecer o padrão

"Reverter uma sequência in-place" é o exemplo mais direto de dois ponteiros nas pontas: um no início, outro no fim, trocando de lugar e andando um em direção ao outro até se cruzarem.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Criar um array novo, preenchendo-o de trás para frente com os caracteres de `s` (ou usar `StringBuilder`/`new String(s).reverse()` em linguagens que oferecem isso), e depois copiar de volta.

- Tempo: O(n) · Espaço: O(n) — precisa de um array/estrutura auxiliar do mesmo tamanho
- **Por que não basta:** o enunciado exige explicitamente O(1) de memória extra; qualquer cópia do array viola essa restrição, mesmo com tempo já linear.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `left` no índice 0 e `right` no último índice. Troque `s[left]` com `s[right]`, depois avance `left` e recue `right`, repetindo até eles se cruzarem (`left >= right`). Cada par de posições simétricas troca de lugar exatamente uma vez.

## 🎬 Exemplo passo a passo

`s = ["h","e","l","l","o"]` (índices 0 a 4)

| Passo | left | right | Ação | Array depois |
|---|---|---|---|---|
| 1 | 0 (`h`) | 4 (`o`) | troca | `[o,e,l,l,h]` |
| 2 | 1 (`e`) | 3 (`l`) | troca | `[o,l,l,e,h]` |
| 3 | 2 | 2 | `left == right`, para | `[o,l,l,e,h]` |

Resultado final: `["o","l","l","e","h"]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada posição é tocada uma única vez, o loop dá `n/2` iterações
- **Espaço:** O(1) — só os índices `left`/`right` e uma variável temporária pra troca

## 💻 Implementações

### Java (referência completa e comentada)
```java
public void reverseString(char[] s) {
    int left = 0;
    int right = s.length - 1;

    while (left < right) { // "<" evita trocar o elemento do meio com ele mesmo
        char tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
        left++;
        right--;
    }
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

- Usar `new String(s).reverse()`/`StringBuilder` ou concatenar num array novo — qualquer uma dessas cria uma cópia, violando o requisito explícito de O(1) de memória extra.
- Resolver com recursão — funciona, mas cada chamada empilha um frame na pilha de execução, custando espaço O(n); é uma forma "escondida" de gastar memória extra mesmo sem alocar um array visível.
- Usar `left <= right` em vez de `left < right` — com array de tamanho ímpar, isso trocaria o elemento do meio consigo mesmo (inofensivo, mas desnecessário) e, dependendo de como o código está escrito, pode causar um passo extra incorreto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Tamanho ímpar | `["h","e","l","l","o"]` | `["o","l","l","e","h"]` | elemento do meio (índice 2) não precisa de troca |
| Tamanho par | `["H","a","n","n","a","h"]` | `["h","a","n","n","a","H"]` | `left` e `right` se cruzam sem sobrar elemento do meio |
| Um único caractere | `["a"]` | `["a"]` | `left == right` desde o início, loop não executa |
| Dois caracteres | `["a","b"]` | `["b","a"]` | caso mínimo, um único swap |

## 🔗 Conexões

- Problemas irmãos: [0541] Reverse String II (mesma técnica, mas aplicada só em blocos alternados da string), [0151] Reverse Words in a String (reverte a ordem das palavras, não dos caracteres, mas mesma família de manipulação in-place)
- No backend: reverter buffers de bytes in-place é comum em parsers binários e protocolos de rede (ex.: converter a ordem de bytes entre big-endian e little-endian).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
