# [0500] Keyboard Row

> 🔗 [LeetCode 500](https://leetcode.com/problems/keyboard-row/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Dado um array de strings `words`, retorne **as palavras que podem ser digitadas usando letras de apenas uma linha do teclado americano**.

As strings são **case-insensitive**: tanto a versão minúscula quanto a maiúscula da mesma letra são tratadas como se estivessem na mesma linha.

No **teclado americano**:
- a primeira linha é `"qwertyuiop"`,
- a segunda linha é `"asdfghjkl"`,
- a terceira linha é `"zxcvbnm"`.

**Exemplos:**
```
Input:  words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explicação: 'a' e 'A' estão na 2ª linha do teclado, independente da caixa.

Input:  words = ["omk"]
Output: []

Input:  words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
```

**Restrições (e o que elas denunciam):**
- `1 <= words.length <= 20`, `1 <= words[i].length <= 100` → entrada pequena, qualquer O(n·m) resolve tranquilamente
- case-insensitive → precisa normalizar caixa antes de comparar
- só 3 linhas possíveis de teclado → dá pra pré-computar um mapa fixo letra→linha (26 entradas), como um array de contagem fixo

## 🧭 Como reconhecer o padrão

"Pertence ao mesmo grupo" com um conjunto fixo e pequeno de grupos (aqui, 3 linhas do teclado) é sempre resolvido com um mapa de "elemento → grupo" pré-computado, e depois checando se todos os elementos de cada palavra caem no mesmo grupo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra, para cada uma das 3 linhas do teclado, verificar se TODOS os caracteres da palavra pertencem àquela linha (usando `contains` na string da linha).

- Tempo: O(palavras × linhas × tamanho_palavra × tamanho_linha) · Espaço: O(1)
- **Por que não basta:** não é proibitivo aqui (entrada pequena), mas repete a busca "qual linha tem esta letra" letra por letra, quando dá para responder isso em O(1) com um mapa pré-computado uma única vez.

## 💡 Solução 2 — A ideia otimizada (intuição)

Crie um mapa (array de 26 posições) que responde "em qual linha (0, 1 ou 2) está esta letra" — computado uma única vez fora do loop principal. Para cada palavra, pegue a linha do primeiro caractere e confirme que todos os outros caracteres têm a mesma linha.

## 🎬 Exemplo passo a passo

`words = ["Hello","Alaska","Dad","Peace"]` — linha0 tem `qwertyuiop`, linha1 tem `asdfghjkl`, linha2 tem `zxcvbnm`

| Passo | palavra | linha do 1º char | todas as letras na mesma linha? | resultado |
|---|---|---|---|---|
| 1 | Hello | h→linha1 | e→linha0 (diferente!) | descarta |
| 2 | Alaska | a→linha1 | l,a,s,k,a→todas linha1 | mantém |
| 3 | Dad | d→linha1 | a,d→todas linha1 | mantém |
| 4 | Peace | p→linha0 | e,a→linha1 (diferente!) | descarta |

Resultado final: `["Alaska","Dad"]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(total de caracteres em `words`) — pré-computação O(1) fixa + uma passada por palavra
- **Espaço:** O(1) extra — o mapa de 26 letras tem tamanho fixo

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String[] findWords(String[] words) {
    int[] linhaDaLetra = new int[26];
    String[] linhas = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
    for (int linha = 0; linha < linhas.length; linha++) {
        for (char c : linhas[linha].toCharArray()) {
            linhaDaLetra[c - 'a'] = linha; // pré-computa: letra -> linha do teclado
        }
    }

    List<String> resultado = new ArrayList<>();
    for (String word : words) {
        String lower = word.toLowerCase();
        int linhaEsperada = linhaDaLetra[lower.charAt(0) - 'a'];
        boolean valido = true;
        for (char c : lower.toCharArray()) {
            if (linhaDaLetra[c - 'a'] != linhaEsperada) {
                valido = false;
                break; // já achou uma letra fora da linha, não precisa continuar
            }
        }
        if (valido) {
            resultado.add(word); // guarda a palavra ORIGINAL (com a caixa original)
        }
    }
    return resultado.toArray(new String[0]);
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

- Esquecer de normalizar a caixa antes de indexar no array (`'A' - 'a'` daria índice negativo) — sempre converta para minúsculo (ou maiúsculo) antes de usar como índice.
- Adicionar a palavra em minúsculo no resultado em vez da palavra original — o enunciado espera a palavra como veio na entrada, preservando a caixa original.
- Comparar contra as 3 strings de linha com `contains` letra por letra dentro do loop de palavras, recomputando a mesma informação repetidamente em vez de pré-computar o mapa uma única vez fora do loop.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Palavra cruzando linhas | `["omk"]` | `[]` | 'o' está na linha 0, 'm' e 'k' em outras linhas |
| Palavra válida com maiúsculas | `["Alaska"]` | `["Alaska"]` | case-insensitive, mas preserva a caixa original na saída |
| Todas as letras na mesma linha | `["adsdf","sfd"]` | `["adsdf","sfd"]` | ambas ficam inteiramente na linha 1 |
| Palavra de uma letra | `["a"]` | `["a"]` | trivialmente válida, só uma linha envolvida |

## 🔗 Conexões

- Problemas irmãos: [0242] Valid Anagram (mesmo uso de mapa fixo de 26 posições), [0205] Isomorphic Strings (mapa letra→grupo, mas com regra de correspondência diferente)
- No backend: validação de dados contra grupos pré-definidos (ex.: verificar se todos os itens de um pedido pertencem ao mesmo centro de distribuição), roteamento de mensagens por categoria fixa usando lookup table em vez de busca linear repetida.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
