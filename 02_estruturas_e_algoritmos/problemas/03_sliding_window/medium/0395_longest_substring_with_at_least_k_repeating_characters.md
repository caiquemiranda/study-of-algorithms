# [0395] Longest Substring with At Least K Repeating Characters

> 🔗 [LeetCode 395](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#DivideAndConquer` `#Medium`

## 📜 O Problema

Dada uma string `s` e um inteiro `k`, retorne o comprimento da maior substring de `s` tal que a frequência de cada caractere nessa substring seja **maior ou igual** a `k`. Se não existir tal substring, retorne `0`.

**Exemplos:**
```
Input:  s = "aaabb", k = 3
Output: 3
Explicação: a maior substring é "aaa", já que 'a' se repete 3 vezes.

Input:  s = "ababbc", k = 2
Output: 5
Explicação: a maior substring é "ababb", já que 'a' se repete 2 vezes e 'b' se repete 3 vezes.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^4` → O(n³) força bruta é arriscado; o esperado é algo próximo de O(n) ou O(26n)
- `s` consiste só em letras minúsculas → no máximo 26 caracteres distintos, o que limita a profundidade de qualquer recursão baseada em "eliminar um caractere por vez"
- `1 <= k <= 10^5` → `k` pode ser maior que o próprio comprimento de `s`, tornando a resposta `0` em muitos casos

## 🧭 Como reconhecer o padrão

"Maior substring onde cada caractere presente atinge uma contagem mínima" não permite o encolhimento clássico de janela: remover um elemento pela esquerda não necessariamente resolve o problema, porque o caractere "insuficiente" pode estar em qualquer posição da janela. A saída é uma variação do princípio de janela: em vez de mover dois ponteiros, **divide-se** a busca ao redor do primeiro caractere que provadamente não pode pertencer a nenhuma substring válida, reduzindo o problema original a subproblemas menores e independentes.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada substring `[left, right]`, contar a frequência de cada caractere e checar se todas são `>= k`.

- Tempo: O(n³) (O(n²) substrings, O(n) para contar cada uma) · Espaço: O(26) por substring
- **Por que não basta:** revalida a contagem de caracteres do zero a cada substring candidata, mesmo quando ela é apenas a anterior estendida em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte a frequência de cada caractere no trecho inteiro. Se algum caractere aparece MENOS de `k` vezes, ele nunca pode fazer parte de nenhuma substring válida que o contenha (removê-lo do trecho só reduziria ainda mais sua contagem em qualquer subtrecho). Corte a string nesse caractere e resolva recursivamente cada metade, pegando o maior resultado. Se todo caractere já aparece `>= k` vezes, o trecho inteiro é a resposta.

## 🎬 Exemplo passo a passo

`s = "ababbc"`, `k = 2`

| Chamada | Substring | Frequências | Caractere que quebra (freq<k)? | Ação |
|---|---|---|---|---|
| 1 | "ababbc" (string inteira) | a:2, b:3, c:1 | 'c' (freq1<2) | divide em "ababb" e "" ao redor de 'c' |
| 2 | "ababb" | a:2, b:3 | nenhum (todos ≥2) | válida! retorna comprimento 5 |
| 3 | "" (depois de 'c') | — | — | vazia, retorna 0 |

Resultado final: `max(5, 0) = 5` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(26n) = O(n) — cada nível de recursão "elimina" pelo menos um caractere distinto (no máximo 26 no total), então a recursão nunca é mais profunda que 26 níveis, e o trabalho total por nível é O(n)
- **Espaço:** O(n) para a pilha de recursão e as substrings criadas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int longestSubstring(String s, int k) {
    return longestSubstring(s, 0, s.length(), k);
}

private int longestSubstring(String s, int start, int end, int k) {
    if (end - start < k) {
        return 0; // nem dá pra um único caractere atingir k ocorrências aqui
    }

    int[] freq = new int[26];
    for (int i = start; i < end; i++) {
        freq[s.charAt(i) - 'a']++;
    }

    for (int i = start; i < end; i++) {
        if (freq[s.charAt(i) - 'a'] < k) {
            // esse caractere nunca pode aparecer numa substring válida: divide em torno dele
            int left = longestSubstring(s, start, i, k);
            int right = longestSubstring(s, i + 1, end, k);
            return Math.max(left, right);
        }
    }

    return end - start; // todo caractere já aparece >= k vezes: o trecho inteiro é válido
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

- A "janela" aqui não desliza com dois ponteiros — ela é **dividida** recursivamente ao redor de um caractere que provadamente nunca pode participar de uma substring válida.
- Recalcular as frequências do zero a cada chamada recursiva parece caro, mas como cada nível elimina pelo menos um caractere distinto (no máximo 26 no total), o custo total continua O(26n) = O(n).
- Esquecer o caso base `end - start < k` — um trecho menor que `k` caracteres nunca pode ter nenhum caractere repetido `k` vezes, então recursar nele é desnecessário (embora não incorreto, é um corte de eficiência).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| String menor que k | `s="a"`, `k=2` | 0 | nem o único caractere presente atinge k ocorrências |
| String inteira já válida | `s="aaa"`, `k=3` | 3 | "aaa" já tem 'a' repetido 3 vezes |
| Múltiplos caracteres "ruins" | `s="aabbcc"`, `k=3` | 0 | nenhum caractere isolado chega a 3 ocorrências |
| Exemplo do enunciado | `s="ababbc"`, `k=2` | 5 | "ababb" tem 'a' e 'b' cada um com pelo menos 2 ocorrências |

## 🔗 Conexões

- Problemas irmãos: [1763] Longest Nice Substring (mesma família de dividir a busca ao redor de um caractere que invalida qualquer substring que o contenha), [0904] Fruit Into Baskets (mesma categoria de janela, mas resolvido por encolhimento clássico em vez de divisão)
- No backend: filtrar tokens raros de um vocabulário (um caractere ou palavra que aparece poucas vezes num corpus) antes de processar blocos de texto, dividindo o texto original nos pontos onde tokens abaixo do limiar de frequência aparecem.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
