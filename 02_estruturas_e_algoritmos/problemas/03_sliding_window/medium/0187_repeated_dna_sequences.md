# [0187] Repeated DNA Sequences

> 🔗 [LeetCode 187](https://leetcode.com/problems/repeated-dna-sequences/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#BitManipulation` `#RollingHash` `#Medium`

## 📜 O Problema

Uma sequência de DNA é composta por nucleotídeos abreviados como `'A'`, `'C'`, `'G'` e `'T'`. Dada uma string `s` representando uma sequência de DNA, retorne todas as sequências (substrings) de **10 letras** que ocorrem mais de uma vez na molécula. A resposta pode ser retornada em qualquer ordem.

**Exemplos:**
```
Input:  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Input:  s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → O(n²) comparando todo par de substrings de 10 caracteres estoura; O(n) é o esperado
- `s[i]` é `'A'`, `'C'`, `'G'` ou `'T'` → alfabeto de só 4 símbolos, então cada base cabe em 2 bits — uma substring de 10 bases cabe inteira num inteiro de 20 bits, permitindo hashing rápido sem manipular `String`s pesadas

## 🧭 Como reconhecer o padrão

"Substrings de tamanho **fixo** 10, achar as que se repetem" é janela deslizante de tamanho fixo combinada com contagem via hashmap: desliza-se uma janela de 10 caracteres, usando uma codificação numérica dela como chave num mapa de contagem; quando a contagem de uma chave chega a exatamente 2, a sequência correspondente entra no resultado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, extrair `s.substring(i, i+10)` (uma nova `String` a cada passo) e usar um `HashMap<String, Integer>` para contar ocorrências.

- Tempo: O(10n) — ainda O(n) assintoticamente, mas com constante mais alta · Espaço: O(n) para as strings armazenadas
- **Por que não basta (mesmo sendo O(n)):** aloca uma nova `String` de 10 caracteres a cada janela e recalcula seu hash do zero, quando um inteiro atualizado incrementalmente evita toda essa alocação.

## 💡 Solução 2 — A ideia otimizada (intuição)

Codifique cada base (`A`, `C`, `G`, `T`) em 2 bits. Mantenha um inteiro `hash` representando os últimos 10 caracteres: ao deslizar, `hash = ((hash << 2) | novoBit) & mask`, onde `mask` mantém só os 20 bits mais recentes. Use um `HashMap<Integer, Integer>` de hash → contagem; quando a contagem de um hash chegar a exatamente 2, adicione a substring correspondente ao resultado (evitando duplicar entradas se ela aparecer 3 vezes ou mais).

## 🎬 Exemplo passo a passo

`s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"` (32 caracteres, 23 janelas de tamanho 10) — destacando os pontos-chave da varredura, onde as repetições acontecem:

| i (início da janela) | Substring | Contagem no mapa (após incluir) | Ação |
|---|---|---|---|
| 0 | AAAAACCCCC | 1 | primeira vez, só registra |
| 5 | CCCCCAAAAA | 1 | primeira vez, só registra |
| 10 | AAAAACCCCC | 2 | repetiu! adiciona ao resultado |
| 16 | CCCCCAAAAA | 2 | repetiu! adiciona ao resultado |

Resultado final: `["AAAAACCCCC", "CCCCCAAAAA"]` ✔ (ordem pode variar)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada, cada posição faz O(1) trabalho de bitmask
- **Espaço:** O(n) no pior caso para o mapa de hashes

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<String> findRepeatedDnaSequences(String s) {
    Map<Character, Integer> baseCode = Map.of('A', 0, 'C', 1, 'G', 2, 'T', 3);
    int n = s.length();
    List<String> result = new ArrayList<>();
    if (n < 10) {
        return result;
    }

    int mask = (1 << 20) - 1; // mantém só os 20 bits mais recentes (10 bases x 2 bits)
    int hash = 0;
    for (int i = 0; i < 9; i++) {
        hash = ((hash << 2) | baseCode.get(s.charAt(i))) & mask;
    }

    Map<Integer, Integer> count = new HashMap<>();
    for (int i = 9; i < n; i++) {
        hash = ((hash << 2) | baseCode.get(s.charAt(i))) & mask;
        int seen = count.merge(hash, 1, Integer::sum);
        if (seen == 2) {
            result.add(s.substring(i - 9, i + 1)); // só adiciona na 2a ocorrência, evita duplicar no resultado
        }
    }

    return result;
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

- Adicionar a substring ao resultado toda vez que ela é vista (em vez de só na **segunda** ocorrência) duplica entradas no resultado se a sequência aparecer 3+ vezes — checar `seen == 2` exatamente evita isso.
- A janela representada pelo hash termina em `i`, então a substring correspondente é `s.substring(i-9, i+1)`, não `s.substring(i, i+10)` — fácil de errar o índice inicial ao trabalhar "de trás pra frente" a partir do fim da janela.
- Usar `String` como chave do mapa funciona, mas cada chave de 10 caracteres custa mais para hashear e comparar do que um `int` — a codificação em bits é o que torna a solução genuinamente O(n) com baixa constante.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| String menor que 10 | `"ACGT"` | [] | nenhuma janela de tamanho 10 cabe |
| Só uma janela possível | `"ACGTACGTAC"` (exatamente 10 chars) | [] | só uma janela existe, não pode repetir sozinha |
| Repetição tripla (não duplicar no resultado) | `"AAAAAAAAAAAAA"` | ["AAAAAAAAAA"] | a sequência aparece 4 vezes, mas entra só uma vez no resultado |
| Exemplo do enunciado | `"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"` | ["AAAAACCCCC","CCCCCAAAAA"] | as duas sequências de 10 bases que se repetem |

## 🔗 Conexões

- Problemas irmãos: [0028] Find the Index of the First Occurrence in a String (mesma família de buscar padrões dentro de uma string, aqui generalizado para achar TODAS as repetições de tamanho fixo), [2269] Find the K-Beauty of a Number (mesma técnica de manter um valor numérico da janela atualizado incrementalmente em vez de reprocessar a substring inteira)
- No backend: detectar sequências repetidas em dados estruturados — por exemplo, encontrar blocos de 10 caracteres duplicados num arquivo de log ou num identificador de tamanho fixo, usando hashing incremental para performance.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
