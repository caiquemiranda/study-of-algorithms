# [0824] Goat Latin

> 🔗 [LeetCode 824](https://leetcode.com/problems/goat-latin/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Você recebe uma string `sentence` com palavras separadas por espaços, cada uma contendo só letras minúsculas e maiúsculas. Converta a frase para "Goat Latin" seguindo as regras:

- Se a palavra começa com vogal (`'a','e','i','o','u'`), adicione `"ma"` ao final.
- Se a palavra começa com consoante, remova a primeira letra, adicione-a ao final, depois adicione `"ma"`.
- Adicione a letra `'a'` ao final de cada palavra, repetida conforme o índice da palavra na frase (começando em 1): a primeira palavra recebe `"a"`, a segunda `"aa"`, e assim por diante.

Retorne a frase final convertida.

**Exemplos:**
```
Input:  sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Input:  sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
```

**Restrições (e o que elas denunciam):**
- `1 <= sentence.length <= 150` → pequeno, O(n²) na saída ainda é tranquilo
- sem espaços extras nas bordas, palavras separadas por um único espaço → tokenização simples com split
- vogal = a,e,i,o,u — a primeira letra pode ser maiúscula (como em "I"), então a checagem precisa cobrir ambos os casos

## 🧭 Como reconhecer o padrão

"Aplicar uma transformação diferente por palavra, dependendo de uma condição local (primeira letra) e do índice da palavra na frase" é sempre resolvido tokenizando a frase, processando palavra por palavra com um índice, e juntando o resultado no final — não precisa de nenhuma estrutura de dados além de um `StringBuilder`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada palavra, checar a primeira letra, mover se for consoante, adicionar "ma", e adicionar "a" repetido `índice+1` vezes; juntar tudo com espaço.

- Tempo: O(n²) se usar concatenação de `String` repetida no loop externo em vez de `StringBuilder` · Espaço: O(n²) (inerente ao tamanho da própria saída)
- **Por que não basta:** concatenar `String` dentro do loop principal é O(n) por operação; usar `StringBuilder` para acumular o resultado final evita esse custo evitável (o custo quadrático da saída em si é inerente ao problema, não um desperdício).

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça `split(" ")` na frase. Para cada palavra no índice `i` (1-based), verifique se a primeira letra é vogal; se não for, mova a primeira letra para o final. Anexe `"ma"` e depois `"a"` repetido `i` vezes. Junte todas as palavras processadas com espaço usando `StringBuilder`.

## 🎬 Exemplo passo a passo

`sentence = "I speak Goat Latin"`

| Passo | índice(1-based) | palavra | primeira letra é vogal? | após mover consoante | + "ma" + "a"×índice |
|---|---|---|---|---|---|
| 1 | 1 | I | sim | I | "I"+"ma"+"a" = "Imaa" |
| 2 | 2 | speak | não | "peaks" | "peaks"+"ma"+"aa" = "peaksmaaa" |
| 3 | 3 | Goat | não | "oatG" | "oatG"+"ma"+"aaa" = "oatGmaaaa" |
| 4 | 4 | Latin | não | "atinL" | "atinL"+"ma"+"aaaa" = "atinLmaaaaa" |

Resultado final: `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) no pior caso — dominado pelo tamanho da própria saída (a quantidade de 'a's cresce a cada palavra), inerente ao problema
- **Espaço:** O(n²) — para a string de saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String toGoatLatin(String sentence) {
    String[] palavras = sentence.split(" ");
    StringBuilder resultado = new StringBuilder();
    String vogais = "aeiouAEIOU";

    for (int i = 0; i < palavras.length; i++) {
        String palavra = palavras[i];
        StringBuilder atual = new StringBuilder();

        if (vogais.indexOf(palavra.charAt(0)) >= 0) {
            atual.append(palavra); // já começa com vogal, mantém como está
        } else {
            atual.append(palavra.substring(1)).append(palavra.charAt(0)); // move a 1ª letra pro fim
        }
        atual.append("ma");
        atual.append("a".repeat(i + 1)); // "a" repetido (índice + 1) vezes, já que i é 0-based

        if (i > 0) {
            resultado.append(' '); // espaço entre palavras, exceto antes da primeira
        }
        resultado.append(atual);
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

- Esquecer que o índice do enunciado é 1-based ("a" para a primeira palavra, "aa" para a segunda) enquanto o loop em Java geralmente é 0-based — usar `i` em vez de `i + 1` no `repeat()` erra a contagem de "a"s.
- Checar só vogais minúsculas (`"aeiou"`) — a primeira letra da palavra pode vir em maiúsculo (ex.: "I" no exemplo), então a checagem precisa cobrir ambos os casos.
- Concatenar strings dentro de loops sem `StringBuilder` — desperdício de performance evitável, mesmo que o limite de entrada seja pequeno.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Primeira palavra é vogal | `"I speak Goat Latin"` | "Imaa peaksmaaa oatGmaaaa atinLmaaaaa" | caso padrão do enunciado |
| Todas consoantes | `"The quick brown fox jumped over the lazy dog"` | "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa" | nenhuma palavra começa com vogal |
| Uma única palavra | `"apple"` | "applemaa" | vogal no início, mantém a palavra e soma "ma"+"a" (índice 1) |
| Palavra de uma letra | `"a"` | "amaa" | vogal isolada, ainda recebe "ma" + "a" |

## 🔗 Conexões

- Problemas irmãos: [0345] Reverse Vowels of a String (mesma checagem de conjunto fixo de vogais), [0006] Zigzag Conversion (mesma ideia de processar índice a índice com regra dependente de posição)
- No backend: geração de identificadores ou codinomes ofuscados a partir de uma regra de transformação fixa por posição — o mesmo padrão de "regra determinística aplicada token a token" aparece em pipelines de anonimização leve de dados.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
