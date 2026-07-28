# [0718] Maximum Length of Repeated Subarray

> 🔗 [LeetCode 718](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#DynamicProgramming` `#Medium`

## 📜 O Problema

Dados dois arrays de inteiros `nums1` e `nums2`, retorne o comprimento máximo de um subarray que aparece em **ambos** os arrays.

**Exemplos:**
```
Input:  nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explicação: o subarray repetido de tamanho máximo é [3,2,1].

Input:  nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
```

**Restrições (e o que elas denunciam):**
- `1 <= nums1.length, nums2.length <= 1000` → O(n·m·min(n,m)) força bruta ingênua pode chegar a ~10^9; uma técnica O((n+m)·min(n,m)) já é bem mais segura
- `0 <= nums1[i], nums2[i] <= 100` → valores pequenos, sem necessidade de tratamento especial de overflow

## 🧭 Como reconhecer o padrão

"Maior trecho contíguo compartilhado entre DOIS arrays" é resolvido **deslizando** um array sobre o outro em cada alinhamento possível (cada "deslocamento" relativo entre os índices de `nums1` e `nums2`) e, para cada alinhamento fixo, percorrendo a região sobreposta uma única vez em busca do maior trecho de correspondência consecutiva — a mesma ideia de "janela" aplicada entre duas sequências em vez de uma só.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de posições iniciais `(i, j)` (uma em cada array), estender um comprimento de correspondência a partir dali, comparando elemento a elemento.

- Tempo: O(n · m · min(n,m)) · Espaço: O(1)
- **Por que não basta:** refaz a extensão do zero para CADA par `(i,j)` independentemente, mesmo quando pares vizinhos compartilham o mesmo "alinhamento" e poderiam ser resolvidos numa única varredura.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de testar todo par `(i,j)` separadamente, itere sobre todo **deslocamento** possível entre os dois arrays (a diferença `i - j`, que efetivamente "desliza" `nums2` sobre `nums1`). Para cada deslocamento fixo, uma única passada pela região sobreposta encontra o maior trecho de valores iguais consecutivos (resetando um contador de `run` a cada divergência), sem precisar reiniciar para cada par de índices dentro daquele alinhamento.

## 🎬 Exemplo passo a passo

`nums1 = [1,2,3,2,1]`, `nums2 = [3,2,1,4,7]` — mostrando o deslocamento vencedor (`offset = 2`, alinhando `nums1[2]` com `nums2[0]`):

| Deslocamento (offset) | i inicial | j inicial | Percurso (run a cada passo) | Melhor run neste offset |
|---|---|---|---|---|
| ... outros deslocamentos não mostrados (nenhum supera 3) | | | | ≤3 |
| 2 | 2 | 0 | nums1[2]=3=nums2[0]=3→run1; nums1[3]=2=nums2[1]=2→run2; nums1[4]=1=nums2[2]=1→run3 | 3 |

Resultado final (maior run entre todos os deslocamentos): `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O((n+m) · min(n,m)) — cada um dos `n+m-1` deslocamentos possíveis percorre até `min(n,m)` posições
- **Espaço:** O(1) além da entrada

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findLength(int[] nums1, int[] nums2) {
    int n = nums1.length;
    int m = nums2.length;
    int best = 0;

    // offset varia de -(m-1) a (n-1): alinha nums1[i] com nums2[i-offset]
    for (int offset = -(m - 1); offset <= n - 1; offset++) {
        int i = Math.max(0, offset);
        int j = Math.max(0, -offset);
        int run = 0;

        while (i < n && j < m) {
            if (nums1[i] == nums2[j]) {
                run++;
                best = Math.max(best, run);
            } else {
                run = 0; // a correspondência consecutiva quebrou, reinicia
            }
            i++;
            j++;
        }
    }

    return best;
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

- Confundir "deslocamento" (offset) com índice absoluto — o alinhamento correto usa `i = max(0, offset)` e `j = max(0, -offset)` para nunca acessar índice negativo em nenhum dos dois arrays.
- Resetar o `run` para `0` a cada divergência é essencial — sem isso, a contagem mistura posições não consecutivas.
- Essa técnica de "deslizar" um array sobre o outro é mais simples de implementar que programação dinâmica, mas para arrays muito maiores (`>10^4`), DP O(n·m) ou busca binária + rolling hash O((n+m)log(min(n,m))) escalam melhor.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhuma sobreposição | `nums1=[1,2]`, `nums2=[3,4]` | 0 | nenhum valor em comum |
| Arrays idênticos | `nums1=[0,0,0,0,0]`, `nums2=[0,0,0,0,0]` | 5 | o array inteiro é um subarray repetido |
| Match de tamanho 1 | `nums1=[1,2,3]`, `nums2=[9,1,9]` | 1 | só o valor 1 coincide, isoladamente |
| Exemplo do enunciado | `nums1=[1,2,3,2,1]`, `nums2=[3,2,1,4,7]` | 3 | [3,2,1] aparece em ambos |

## 🔗 Conexões

- Problemas irmãos: [1143] Longest Common Subsequence (mesmo objetivo de "maior trecho compartilhado" entre duas sequências, mas permitindo lacunas — não precisa ser contíguo, resolvido com DP em vez de deslizamento), [0003] Longest Substring Without Repeating Characters (mesma família de manipulação de janelas sobre sequências)
- No backend: encontrar o maior trecho idêntico entre duas versões de um arquivo ou payload (diffing), útil para detectar blocos de dados duplicados ou não alterados entre duas revisões.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
