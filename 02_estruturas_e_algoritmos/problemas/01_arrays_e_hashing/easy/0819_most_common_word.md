# [0819] Most Common Word

> 🔗 [LeetCode 819](https://leetcode.com/problems/most-common-word/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Counting` `#Easy`

## 📜 O Problema

Dado um `paragraph` e um array de strings `banned` com palavras banidas, retorne **a palavra mais frequente que não está banida**. É garantido que existe pelo menos uma palavra não banida, e que a resposta é única.

As palavras em `paragraph` são **case-insensitive**, e a resposta deve ser retornada em **minúsculas**. Palavras não podem conter símbolos de pontuação.

**Exemplos:**
```
Input:  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explicação: "hit" ocorre 3 vezes, mas é banida. "ball" ocorre 2 vezes (e nenhuma outra palavra
mais), então é a mais frequente não banida. Note que a comparação ignora caixa e pontuação.

Input:  paragraph = "a.", banned = []
Output: "a"
```

**Restrições (e o que elas denunciam):**
- `1 <= paragraph.length <= 1000` → pequeno, O(n) resolve com folga
- pontuação deve ser ignorada, case-insensitive → precisa normalizar (remover pontuação, minúsculo) antes de tokenizar
- `0 <= banned.length <= 100` → lista de banidas pequena, hash set resolve consulta O(1)
- garantido que existe resposta única → não precisa tratar empate/sem resposta

## 🧭 Como reconhecer o padrão

"Palavra mais frequente, excluindo algumas" é sempre resolvido tokenizando o texto, normalizando cada palavra, contando frequências num hash map, e ignorando (ou pulando) as que estão num hash set de exclusão.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra do parágrafo, contar manualmente quantas vezes ela aparece percorrendo o parágrafo inteiro de novo, e checar se está na lista banida com busca linear em `banned`.

- Tempo: O(n²) — recontagem completa do parágrafo para cada palavra, mais busca linear em `banned` por palavra · Espaço: O(n)
- **Por que não basta:** recontagem repetida da mesma palavra e busca linear na lista banida são redundantes quando um hash map de frequência e um hash set de banidas resolvem ambos em O(1) por consulta.

## 💡 Solução 2 — A ideia otimizada (intuição)

Normalize o parágrafo trocando todo caractere não-letra por espaço e tudo para minúsculo, depois `split` por espaço para tokenizar. Construa um hash set com as palavras banidas. Percorra as palavras tokenizadas, contando frequência num hash map só para as que não estão banidas, e rastreie a de maior frequência.

## 🎬 Exemplo passo a passo

`paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."`, `banned = ["hit"]`

Normalizado e tokenizado: `bob hit a ball the hit ball flew far after it was hit`

| Passo | palavra | banida? | frequencia[palavra] | maisFrequente até agora |
|---|---|---|---|---|
| 1 | bob | não | bob:1 | bob (1) |
| 2 | hit | sim | (ignorada) | bob (1) |
| 3 | a | não | a:1 | bob (1) |
| 4 | ball | não | ball:1 | bob (1) |
| 5 | the | não | the:1 | bob (1) |
| 6 | hit | sim | (ignorada) | bob (1) |
| 7 | ball | não | ball:2 | **ball (2)** |
| 8+ | (demais palavras, frequência 1) | — | — | ball (2) |

Resultado final: `"ball"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — n = tamanho do parágrafo, tokenização + contagem
- **Espaço:** O(n) — para o hash map e o set de banidas

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String mostCommonWord(String paragraph, String[] banned) {
    Set<String> banidas = new HashSet<>(Arrays.asList(banned));

    // troca qualquer caractere que não seja letra por espaço, e normaliza para minúsculo
    String normalizado = paragraph.toLowerCase().replaceAll("[^a-z]", " ");
    String[] palavras = normalizado.split("\\s+");

    Map<String, Integer> frequencia = new HashMap<>();
    String maisFrequente = "";
    int maiorContagem = 0;

    for (String palavra : palavras) {
        if (palavra.isEmpty() || banidas.contains(palavra)) {
            continue; // pula tokens vazios (de espaços múltiplos) e palavras banidas
        }
        int contagem = frequencia.merge(palavra, 1, Integer::sum);
        if (contagem > maiorContagem) {
            maiorContagem = contagem;
            maisFrequente = palavra;
        }
    }
    return maisFrequente;
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

- Esquecer de normalizar a caixa antes de comparar com `banned` (que vem sempre em minúsculo) — "Hit" e "hit" precisam ser tratados como a mesma palavra.
- Não remover pontuação grudada ("ball," vira "ball") — sem essa limpeza, "ball," e "ball" seriam tratadas como palavras diferentes.
- Usar `split(" ")` em vez de `split("\\s+")` depois de substituir pontuação por espaço — a substituição pode gerar espaços duplicados, criando tokens vazios que precisam ser ignorados.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Palavra banida mais frequente | `paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]` | "ball" | "hit" aparece mais, mas está banida |
| Sem palavras banidas | `paragraph="a.", banned=[]` | "a" | caso trivial de uma única palavra |
| Pontuação grudada em várias palavras | `paragraph="a, a, a, b!", banned=["b"]` | "a" | pontuação não deve fragmentar a contagem |
| Maiúsculas misturadas | `paragraph="Bob bob BOB", banned=[]` | "bob" | case-insensitive, resposta sempre em minúsculo |

## 🔗 Conexões

- Problemas irmãos: [0692] Top K Frequent Words (mesma base de contagem de frequência de palavras, mas retornando os k mais frequentes), [0242] Valid Anagram (mesmo uso de hash map de contagem)
- No backend: análise de texto/logs para encontrar termos mais frequentes excluindo stop words ou termos de uma lista de bloqueio — base de qualquer pipeline simples de word count com filtro.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
