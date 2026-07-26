# [0748] Shortest Completing Word

> 🔗 [LeetCode 748](https://leetcode.com/problems/shortest-completing-word/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Dada uma string `licensePlate` e um array de strings `words`, encontre a **palavra completante mais curta** em `words`.

Uma palavra **completante** é uma palavra que **contém todas as letras** de `licensePlate`. Ignore números e espaços em `licensePlate`, e trate as letras de forma **case insensitive**. Se uma letra aparece mais de uma vez em `licensePlate`, ela precisa aparecer na palavra o mesmo número de vezes ou mais.

Retorne **a palavra completante mais curta** em `words`. É garantido que existe uma resposta. Se houver múltiplas palavras completantes mais curtas, retorne a **primeira** que aparece em `words`.

**Exemplos:**
```
Input:  licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explicação: licensePlate contém 's', 'p', 's' (ignorando caixa) e 't'.
"step" tem 't' e 'p', mas só 1 's'. "steps" tem 't', 'p' e os dois 's'.
"stripe" não tem 's' suficiente. "stepple" também não. "steps" é a resposta.

Input:  licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explicação: licensePlate só tem a letra 's'. Todas as palavras têm 's', mas "pest", "stew" e "show"
são as mais curtas. A resposta é "pest" por ser a que aparece primeiro entre elas.
```

**Restrições (e o que elas denunciam):**
- `1 <= licensePlate.length <= 7` → o mapa de requisitos é pequeno (poucas letras no máximo)
- `1 <= words.length <= 1000`, `1 <= words[i].length <= 15` → força bruta O(words × 26) é tranquila
- "ignore números e espaços", "case insensitive" → precisa filtrar e normalizar `licensePlate` antes de montar os requisitos
- garantido que existe resposta → não precisa tratar "nenhuma palavra serve"

## 🧭 Como reconhecer o padrão

"A palavra precisa CONTER pelo menos N ocorrências de cada letra exigida" é a mesma assinatura de Ransom Note ([0383]): construa um mapa de "quantas vezes cada letra é exigida" e depois, para cada candidato, verifique se ele cobre essas exigências contando suas próprias letras.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra, para cada letra exigida pela placa, contar quantas vezes essa letra aparece na palavra (percorrendo a palavra inteira de novo a cada letra exigida) e comparar com a exigência.

- Tempo: O(words × 26 × tamanho_palavra) se recontar a palavra inteira para cada uma das até 26 letras exigidas · Espaço: O(1)
- **Por que não basta:** não é assintoticamente ruim para os limites dados, mas repete a varredura da mesma palavra várias vezes (uma por letra exigida) quando um único array de contagem por palavra resolve tudo de uma vez.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa o array de requisitos (26 posições) a partir de `licensePlate`, ignorando dígitos/espaços e normalizando para minúsculo. Para cada palavra em `words`, construa o array de contagem dela (26 posições) numa única passada e verifique se ele "cobre" o array de requisitos posição a posição. Mantenha a menor palavra válida vista até agora.

## 🎬 Exemplo passo a passo

`licensePlate = "1s3 PSt"`, `words = ["step","steps","stripe","stepple"]`

Requisitos (ignorando dígitos/espaço, minúsculo): `s` aparece 2x ('s' e 'S'), `p` 1x, `t` 1x → `{s:2, p:1, t:1}`

| Passo | palavra | contagem relevante | cobre os requisitos? | melhor até agora |
|---|---|---|---|---|
| 1 | step | s:1,t:1,e:1,p:1 | não (só 1 's', precisa 2) | — |
| 2 | steps | s:2,t:1,e:1,p:1 | sim (cobre s:2,p:1,t:1) | "steps" (tamanho 5) |
| 3 | stripe | s:1,t:1,r:1,i:1,p:1,e:1 | não (só 1 's') | "steps" |
| 4 | stepple | s:1,t:1,e:2,p:2,l:1 | não (só 1 's') | "steps" |

Resultado final: `"steps"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(soma(len(words[i])) + len(licensePlate)) — uma passada por todos os caracteres de todas as palavras
- **Espaço:** O(1) extra — arrays fixos de 26 posições

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String shortestCompletingWord(String licensePlate, String[] words) {
    int[] requisitos = new int[26];
    for (char c : licensePlate.toCharArray()) {
        if (Character.isLetter(c)) {
            requisitos[Character.toLowerCase(c) - 'a']++;
        }
    }

    String melhor = null;
    for (String word : words) {
        int[] contagem = new int[26];
        for (char c : word.toCharArray()) {
            contagem[c - 'a']++; // words já são garantidas minúsculas pelo enunciado
        }

        if (cobreRequisitos(contagem, requisitos) &&
            (melhor == null || word.length() < melhor.length())) {
            melhor = word; // primeira ocorrência mais curta vence, empates preservam a ordem original
        }
    }
    return melhor;
}

private boolean cobreRequisitos(int[] contagem, int[] requisitos) {
    for (int i = 0; i < 26; i++) {
        if (contagem[i] < requisitos[i]) {
            return false; // faltou pelo menos uma ocorrência desta letra
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

- Esquecer de filtrar dígitos e espaços de `licensePlate` antes de contar — contá-los junto poderia gerar um índice inválido (`c - 'a'` para um dígito não é uma letra válida).
- Não usar `<` estrito na comparação de tamanho ao atualizar `melhor` — usar `<=` faria a última palavra válida do MESMO tamanho vencer, quando o enunciado pede a PRIMEIRA que aparece entre as mais curtas.
- Comparar strings letra a letra em vez de usar arrays de contagem de 26 posições — não captura corretamente exigências de letras repetidas (ex.: "s" duas vezes) sem uma lógica bem mais complicada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Letra repetida na placa | `licensePlate="1s3 PSt", words=["step","steps","stripe","stepple"]` | "steps" | só "steps" tem 2 's' |
| Só uma letra exigida | `licensePlate="1s3 456", words=["looks","pest","stew","show"]` | "pest" | várias servem, "pest" é a mais curta e primeira |
| Placa com todas maiúsculas | `licensePlate="AB", words=["ab","ba","abc"]` | "ab" (ou "ba", o que vier primeiro) | case insensitive, ambas de tamanho 2 cobrem |
| Palavra exatamente igual aos requisitos | `licensePlate="ab", words=["ba"]` | "ba" | ordem das letras na palavra não importa, só a contagem |

## 🔗 Conexões

- Problemas irmãos: [0383] Ransom Note (mesma técnica de comparação de arrays de contagem de 26 letras, "cobre os requisitos?"), [0242] Valid Anagram (mesma base de contagem, mas exige igualdade exata em vez de cobertura mínima)
- No backend: validação de requisitos de formulário (ex.: "a senha precisa ter pelo menos 2 dígitos e 1 símbolo"), busca de produtos que atendem a um conjunto mínimo de especificações (filtro por atributos com quantidade mínima).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
