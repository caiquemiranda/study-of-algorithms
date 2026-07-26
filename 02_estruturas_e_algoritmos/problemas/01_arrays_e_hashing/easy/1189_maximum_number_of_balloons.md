# [1189] Maximum Number of Balloons

> 🔗 [LeetCode 1189](https://leetcode.com/problems/maximum-number-of-balloons/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Counting` `#Easy`

## 📜 O Problema

Dada uma string `text`, você quer usar os caracteres de `text` para formar o máximo de instâncias possíveis da palavra **"balloon"**. Cada caractere de `text` pode ser usado **no máximo uma vez**. Retorne o número máximo de instâncias que podem ser formadas.

**Exemplos:**
```
Input:  text = "nlaebolko"
Output: 1

Input:  text = "loonbalxballpoon"
Output: 2

Input:  text = "leetcode"
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= text.length <= 10^4` → O(n) resolve com folga
- letras minúsculas apenas → array fixo de 26 posições
- "cada caractere usado no máximo uma vez" → é uma contagem de "quantas vezes cabe o multiconjunto de letras de 'balloon'" dentro do estoque de `text`

## 🧭 Como reconhecer o padrão

"Quantas cópias de uma palavra-alvo você consegue formar com o estoque de letras disponível" é resolvido contando a frequência de cada letra no estoque e na palavra-alvo, e pegando o MENOR valor de `estoque[letra] / necessario[letra]` entre as letras da palavra-alvo — o "gargalo" limita quantas cópias completas dá pra formar.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada possível número de cópias `k` (começando de um valor grande e diminuindo), verificar se `text` tem letras suficientes para formar `k` cópias de "balloon", parando na primeira que funcionar.

- Tempo: O(k × 26) no pior caso, testando vários valores de `k` até achar o correto · Espaço: O(1)
- **Por que não basta:** testa vários candidatos de `k` quando o valor exato já pode ser calculado diretamente dividindo a contagem disponível pela contagem necessária de cada letra.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte a frequência de cada letra em `text` (array de 26 posições). "balloon" precisa de: b:1, a:1, l:2, o:2, n:1. Para cada uma dessas 5 letras, calcule `contagem[letra] / necessario[letra]` (divisão inteira); a resposta é o MENOR desses valores.

## 🎬 Exemplo passo a passo

`text = "nlaebolko"` — contagem: n:1, l:2, a:1, e:1, b:1, o:2, k:1

| Passo | letra | contagem[letra] | necessario[letra] | contagem/necessario |
|---|---|---|---|---|
| 1 | b | 1 | 1 | 1 |
| 2 | a | 1 | 1 | 1 |
| 3 | l | 2 | 2 | 1 |
| 4 | o | 2 | 2 | 1 |
| 5 | n | 1 | 1 | 1 |

Menor valor entre todos: `1` ✔ (todas as letras dão exatamente para 1 "balloon")

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — contagem em uma passada + checagem O(1) das 5 letras fixas
- **Espaço:** O(1) — array fixo de 26 posições

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxNumberOfBalloons(String text) {
    int[] contagem = new int[26];
    for (char c : text.toCharArray()) {
        contagem[c - 'a']++;
    }

    // "balloon" precisa de: b(1), a(1), l(2), o(2), n(1)
    int b = contagem['b' - 'a'];
    int a = contagem['a' - 'a'];
    int l = contagem['l' - 'a'] / 2; // 'l' aparece 2x em "balloon"
    int o = contagem['o' - 'a'] / 2; // 'o' aparece 2x em "balloon"
    int n = contagem['n' - 'a'];

    return Math.min(b, Math.min(a, Math.min(l, Math.min(o, n))));
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

- Esquecer que 'l' e 'o' aparecem DUAS vezes em "balloon" — sem dividir a contagem dessas letras por 2, o cálculo superestima quantas cópias são possíveis.
- Contar letras que não fazem parte de "balloon" (ex.: 'k', 'e' no exemplo) como se importassem — elas são irrelevantes, só as 5 letras de "balloon" limitam o resultado.
- Usar divisão de ponto flutuante em vez de divisão inteira — a divisão inteira (arredondando pra baixo) é exatamente o comportamento desejado, já que só cópias completas contam.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exatamente uma cópia | `"nlaebolko"` | 1 | todas as letras dão para exatamente 1 "balloon" |
| Duas cópias possíveis | `"loonbalxballpoon"` | 2 | letras suficientes para 2 cópias completas |
| Sem letras suficientes | `"leetcode"` | 0 | faltam letras como 'b' e o dobro de 'l'/'o' |
| Estoque exato sem sobra | `"balloon"` | 1 | usa exatamente as letras de uma cópia, nada sobra |

## 🔗 Conexões

- Problemas irmãos: [0383] Ransom Note (mesma base de comparação de contagem, mas binária em vez de "quantas vezes cabe"), [1160] Find Words That Can Be Formed by Characters (mesma técnica de array de contagem fixo comparando com um estoque)
- No backend: cálculo de quantas unidades de um produto composto podem ser montadas dado o estoque de componentes (ex.: "quantos kits de montagem posso formar com as peças que tenho"), onde cada kit exige quantidades específicas de cada peça.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
