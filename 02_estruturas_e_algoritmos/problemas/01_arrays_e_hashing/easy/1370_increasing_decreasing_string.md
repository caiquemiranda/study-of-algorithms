# [1370] Increasing Decreasing String

> 🔗 [LeetCode 1370](https://leetcode.com/problems/increasing-decreasing-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Counting` `#Easy`

## 📜 O Problema

Você recebe uma string `s`. Reordene a string usando o seguinte algoritmo:
- Remova o caractere **menor** de `s` e anexe-o ao resultado.
- Remova o caractere **menor** de `s` que seja maior que o último caractere anexado, e anexe-o. Repita até não ser mais possível.
- Remova o caractere **maior** de `s` e anexe-o ao resultado.
- Remova o caractere **maior** de `s` que seja menor que o último caractere anexado, e anexe-o. Repita até não ser mais possível.
- Repita os passos anteriores até que todos os caracteres de `s` tenham sido removidos.

Retorne a string resultante após reordenar `s` com esse algoritmo.

**Exemplos:**
```
Input:  s = "aaaabbbbcccc"
Output: "abccbaabccba"

Input:  s = "rat"
Output: "art"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 500` → pequeno, O(n) ou até O(26×n) resolve com folga
- só letras minúsculas → array fixo de 26 posições
- o algoritmo alterna entre "menor disponível crescente" e "maior disponível decrescente" repetidamente até esgotar a string

## 🧭 Como reconhecer o padrão

"Construa a string seguindo uma ordem alternada de menor→maior→menor..." usando as letras disponíveis é resolvido contando a frequência de cada letra (array de 26 posições) e simulando o algoritmo diretamente sobre esse array, sem nunca precisar remover caracteres de uma string de verdade — só decrementar contadores.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Manter a string `s` como uma lista mutável, e a cada passo do algoritmo, PROCURAR (busca linear) o menor ou maior caractere restante na lista, removê-lo, e repetir.

- Tempo: O(n × 26) na melhor implementação ingênua, podendo chegar a O(n²) se a busca varrer a lista inteira · Espaço: O(n)
- **Por que não basta:** buscar o "menor caractere restante" numa lista de até 500 caracteres é mais lento do que verificar 26 posições fixas de um array de contagem, que já está ordenado por natureza (índice = letra).

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte a frequência de cada letra (array de 26 posições). Simule o algoritmo repetidamente: percorra de 'a' a 'z' anexando cada letra com contagem > 0 (decrementando-a) — fase "crescente"; depois percorra de 'z' a 'a' fazendo o mesmo — fase "decrescente". Repita até que todas as contagens estejam zeradas.

## 🎬 Exemplo passo a passo

`s = "rat"` (contagem: a:1, r:1, t:1)

| Passo | Fase | letra | contagem antes | Ação | resultado parcial |
|---|---|---|---|---|---|
| 1 | crescente (a→z) | a | 1 | anexa, decrementa | a |
| 2 | crescente (a→z) | r | 1 | anexa, decrementa | ar |
| 3 | crescente (a→z) | t | 1 | anexa, decrementa | art |
| 4 | decrescente (z→a) | (todas zeradas) | 0 | nada a fazer | art |

Todas as contagens zeraram após a primeira fase crescente → o algoritmo termina.

Resultado final: `"art"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada letra é anexada uma única vez no total, ao longo de todos os ciclos
- **Espaço:** O(1) extra (array fixo de 26 posições) + O(n) para o resultado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String sortString(String s) {
    int[] contagem = new int[26];
    for (char c : s.toCharArray()) {
        contagem[c - 'a']++;
    }

    StringBuilder resultado = new StringBuilder();
    while (resultado.length() < s.length()) {
        // fase crescente: de 'a' até 'z', anexa cada letra disponível
        for (int i = 0; i < 26; i++) {
            if (contagem[i] > 0) {
                resultado.append((char) ('a' + i));
                contagem[i]--;
            }
        }
        // fase decrescente: de 'z' até 'a', anexa cada letra disponível
        for (int i = 25; i >= 0; i--) {
            if (contagem[i] > 0) {
                resultado.append((char) ('a' + i));
                contagem[i]--;
            }
        }
    }
    return resultado.toString();
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

- Tentar remover caracteres de uma `String`/lista de verdade a cada passo, em vez de decrementar um array de contagem — funciona, mas é mais lento e mais propenso a erro de índice.
- Esquecer a condição de parada correta (`resultado.length() < s.length()`) — sem ela, o loop `while` continuaria rodando indefinidamente mesmo depois de todas as contagens zerarem.
- Assumir que cada ciclo (crescente + decrescente) sempre usa TODAS as 26 letras — na prática, cada ciclo só usa as letras que ainda têm contagem > 0, então ciclos posteriores processam cada vez menos letras.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Palavra simples | `"rat"` | "art" | uma única fase crescente já esgota as letras |
| Múltiplos ciclos | `"aaaabbbbcccc"` | "abccbaabccba" | precisa de 2 ciclos completos (crescente+decrescente) para esgotar |
| Uma única letra repetida | `"aaa"` | "aaa" | cada ciclo crescente emite um 'a', repete 3 vezes |
| Letras já alternadas | `"ba"` | "ab" | fase crescente reordena para a forma correta |

## 🔗 Conexões

- Problemas irmãos: [1636] Sort Array by Increasing Frequency (mesma base de contagem seguida de reconstrução ordenada), [0451] Sort Characters By Frequency (mesmo domínio de reordenar uma string usando um array de contagem)
- No backend: geração de sequências balanceadas a partir de um estoque de itens categorizados (ex.: distribuir tarefas de prioridades diferentes numa ordem alternada crescente/decrescente para balancear carga), aplicando repetidamente o mesmo padrão de "consumir do estoque disponível".

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
