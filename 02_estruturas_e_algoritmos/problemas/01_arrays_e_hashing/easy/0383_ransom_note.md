# [0383] Ransom Note

> 🔗 [LeetCode 383](https://leetcode.com/problems/ransom-note/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Counting` `#Easy`

## 📜 O Problema

Dadas as strings `ransomNote` e `magazine`, retorne `true` se `ransomNote` pode ser construída usando as letras de `magazine` — cada letra da revista só pode ser usada **uma vez**.

**Exemplos:**
```
Input:  ransomNote = "a",  magazine = "b"    Output: false
Input:  ransomNote = "aa", magazine = "ab"   Output: false (só há um 'a' na revista)
Input:  ransomNote = "aa", magazine = "aab"  Output: true
```

**Restrições (e o que elas denunciam):**
- `1 <= ransomNote.length, magazine.length <= 10^5` → precisa de O(n+m); comparação letra a letra com remoção ingênua de string seria custosa demais
- "letras minúsculas do inglês" → só 26 possibilidades, habilita array de contagem fixo (mais rápido que hash map genérico)
- "cada letra só pode ser usada uma vez" → é essencialmente perguntar se a **contagem** de cada letra em `magazine` é suficiente para cobrir a contagem exigida por `ransomNote`

## 🧭 Como reconhecer o padrão

"Posso formar X usando as letras de Y (cada letra uma vez)?" é sempre um problema de **comparação de frequências**: conte as letras disponíveis, conte as letras necessárias, e verifique se a disponibilidade cobre a necessidade em cada posição do alfabeto.

## 🐢 Solução 1 — Força bruta

Para cada caractere de `ransomNote`, procurar e "consumir" (marcar como usado) uma ocorrência correspondente em `magazine`, evitando reutilizar a mesma posição.

- Tempo: O(n × m) — para cada letra do bilhete, varre a revista procurando uma letra livre · Espaço: O(m) para marcar posições usadas
- **Por que não basta:** com n e m em torno de 100.000, o produto chega a 10 bilhões — inviável. E toda a informação necessária é só "quantas vezes cada letra aparece", não "onde".

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte quantas vezes cada letra aparece em `magazine` (o "estoque disponível"). Depois, percorra `ransomNote` **descontando** do estoque cada letra usada. Se alguma letra precisar ser usada mas o estoque já estiver zerado (ou negativo), a resposta é `false` na hora.

## 🎬 Exemplo passo a passo

`ransomNote = "aab"`, `magazine = "aabb"`

**Fase 1 — construir o estoque de `magazine`:** `{a: 2, b: 2}`

| Passo | letra de ransomNote | estoque[letra] antes | Ação | estoque[letra] depois |
|---|---|---|---|---|
| 1 | a | 2 | decrementa | 1 |
| 2 | a | 1 | decrementa | 0 |
| 3 | b | 2 | decrementa | 1 |

Nenhuma letra ficou negativa durante o processo → **true** ✔ (a revista tinha estoque suficiente)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — uma passada para contar `magazine`, outra para descontar com `ransomNote`
- **Espaço:** O(1) — o array de contagem tem tamanho fixo (26), independente do tamanho das strings

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean canConstruct(String ransomNote, String magazine) {
    // atalho: se o bilhete for maior que a revista, é matematicamente impossível
    if (ransomNote.length() > magazine.length()) {
        return false;
    }

    int[] estoque = new int[26];
    for (char c : magazine.toCharArray()) {
        estoque[c - 'a']++;  // conta o "material disponível" na revista
    }

    for (char c : ransomNote.toCharArray()) {
        estoque[c - 'a']--;               // consome uma unidade do estoque
        if (estoque[c - 'a'] < 0) {
            return false;                 // faltou material para esta letra
        }
    }
    return true;
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

- Esquecer o atalho `ransomNote.length() > magazine.length()` — não é obrigatório (o algoritmo funciona sem ele), mas evita processamento desnecessário quando já dá para saber a resposta de cara.
- Contar as letras de **ambas** as strings em arrays separados e comparar no final — funciona, mas gasta o dobro de memória e um loop extra comparado a decrementar direto no mesmo array.
- **Java**: `c - 'a'` pressupõe letras minúsculas garantidas pelo enunciado — não generalize esse truque para entradas com maiúsculas ou Unicode sem ajustar.
- Confundir com **Valid Anagram** ([242]): aqui `magazine` pode ter letras **sobrando** (não precisa ser anagrama exato, só precisa "conter o suficiente").

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Bilhete maior que a revista | `ransomNote="ab", magazine="a"` | false | pega no atalho de tamanho |
| Letra insuficiente | `ransomNote="aa", magazine="ab"` | false | só 1 'a' disponível, precisa de 2 |
| Exatamente suficiente | `ransomNote="aa", magazine="aab"` | true | caso do enunciado |
| Revista com sobra | `ransomNote="a", magazine="aaaa"` | true | garante que sobra não atrapalha |

## 🔗 Conexões

- Problemas irmãos: **[0242] Valid Anagram** (mesma técnica de contagem, mas exige igualdade exata, não "conter o suficiente"), **[0387] First Unique Character in a String** (também usa array de contagem de 26 posições)
- No backend: verificar se um pedido pode ser atendido com o estoque disponível (inventário), validar se os componentes necessários para montar um pacote de software existem no repositório local, e checar cotas de recursos (ex.: "tenho memória/CPU suficiente para esta alocação?") seguem essa mesma lógica de contagem e desconto.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
