# [1876] Substrings of Size Three with Distinct Characters

> 🔗 [LeetCode 1876](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#String` `#Easy`

## 📜 O Problema

Uma string é **boa** se não tem caracteres repetidos. Dado `s`, retorne o número de substrings **boas** de comprimento **três** em `s`. Se a mesma substring aparecer mais de uma vez, cada ocorrência conta.

**Exemplos:**
```
Input:  s = "xyzzaz"
Output: 1
Explicação: das 4 substrings de tamanho 3 ("xyz","yzz","zza","zaz"), só "xyz" é boa.

Input:  s = "aababcabc"
Output: 4
Explicação: das 7 substrings de tamanho 3, "abc" (duas vezes), "bca" e "cab" são boas.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → entrada pequena; qualquer abordagem O(n) é folgadamente suficiente
- `s` consiste só em letras minúsculas → no máximo 26 caracteres distintos possíveis (relevante para variações do problema com janelas maiores)

## 🧭 Como reconhecer o padrão

"Substrings de tamanho **fixo** 3" é o sinal mais direto de janela deslizante de tamanho fixo: em vez de gerar cada substring e processá-la do zero, desliza-se uma janela de 3 caracteres pela string, comparando diretamente os elementos da janela atual.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, extrair a substring `s.substring(i, i+3)` e usar um `Set` para checar se os 3 caracteres são distintos.

- Tempo: O(n) no total (a janela já é de tamanho fixo 3), mas com constante alta · Espaço: O(1) por iteração, descartado a cada passo
- **Por que não basta:** mesmo sendo O(n) assintoticamente, aloca uma nova `String` e um novo `Set` a cada uma das até 98 janelas — overhead de alocação e hashing desnecessário quando "tamanho 3" permite comparação direta trivial.

## 💡 Solução 2 — A ideia otimizada (intuição)

Compare diretamente os 3 caracteres da janela dois a dois (`s[i] != s[i+1]`, `s[i] != s[i+2]`, `s[i+1] != s[i+2]`), sem alocar nenhuma estrutura auxiliar. Como a janela tem tamanho fixo, basta deslizar `i` de `0` até `n-3` e fazer essa checagem O(1) em cada posição.

## 🎬 Exemplo passo a passo

`s = "xyzzaz"` (índices: x0 y1 z2 z3 a4 z5)

| i | Janela | x[i]==x[i+1]? | x[i]==x[i+2]? | x[i+1]==x[i+2]? | Boa? | Contagem |
|---|---|---|---|---|---|---|
| 0 | xyz | não | não | não | sim | 1 |
| 1 | yzz | não | não | sim | não | 1 |
| 2 | zza | sim | não | não | não | 1 |
| 3 | zaz | não | sim | não | não | 1 |

Resultado final: `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `n-2` janelas, checagem O(1) cada
- **Espaço:** O(1) — nenhuma estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countGoodSubstrings(String s) {
    int count = 0;
    for (int i = 0; i + 2 < s.length(); i++) {
        char a = s.charAt(i);
        char b = s.charAt(i + 1);
        char c = s.charAt(i + 2);
        if (a != b && a != c && b != c) {
            count++;
        }
    }
    return count;
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

- Esquecer o limite do loop (`i + 2 < s.length()`) e estourar índice ao acessar `s.charAt(i+2)` perto do fim da string.
- Usar uma estrutura auxiliar (`Set`, mapa de contagem) para checar 3 caracteres é desnecessário e mais lento — com janela de tamanho fixo tão pequeno, comparação direta par a par é mais simples e eficiente.
- Confundir "substring" com "subsequência": os 3 caracteres precisam ser **consecutivos** na string original, não apenas aparecer em qualquer ordem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só uma janela, todos distintos | `"xyz"` | 1 | único trio possível, sem repetição |
| Só uma janela, com repetição | `"zza"` | 0 | 'z' aparece duas vezes no trio |
| Exemplo do enunciado (várias janelas) | `"aababcabc"` | 4 | várias janelas de 3 caracteres distintos ao longo da string |
| Tamanho abaixo do mínimo útil | `"ab"` | 0 | nenhuma janela de tamanho 3 cabe (n < 3) |

## 🔗 Conexões

- Problemas irmãos: [0567] Permutation in String (mesma família de janela fixa comparando composição de caracteres, mas checando permutação em vez de distinção), [0643] Maximum Average Subarray I (mesma técnica de janela de tamanho fixo deslizando por um array/string)
- No backend: detectar sequências anômalas em eventos consecutivos — por exemplo, alertar quando os últimos 3 status de um pipeline se repetem de forma inesperada (o oposto: aqui queremos identificar os trios "sem repetição").

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
