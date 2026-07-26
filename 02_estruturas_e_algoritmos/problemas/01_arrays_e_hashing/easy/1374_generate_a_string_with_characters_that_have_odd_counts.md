# [1374] Generate a String With Characters That Have Odd Counts

> 🔗 [LeetCode 1374](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Math` `#Easy`

## 📜 O Problema

Dado um inteiro `n`, retorne uma string com `n` caracteres tal que cada caractere na string ocorra um número **ímpar** de vezes. A string retornada deve conter só letras minúsculas do inglês. Se houver múltiplas strings válidas, retorne qualquer uma delas.

**Exemplos:**
```
Input:  n = 4
Output: "pppz"
Explicação: "pppz" é válida pois 'p' ocorre três vezes e 'z' ocorre uma vez. Há muitas outras
strings válidas, como "ohhh" e "love".

Input:  n = 2
Output: "xy"
Explicação: "xy" é válida pois 'x' e 'y' ocorrem uma vez cada. Há muitas outras strings válidas.

Input:  n = 7
Output: "holasss"
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 500` → tamanho pequeno, qualquer O(n) resolve com folga
- só letras minúsculas → só precisa de no máximo 2 letras distintas para resolver qualquer `n`
- "se houver múltiplas strings válidas, retorne qualquer uma" → não precisa de uma construção única, só uma que funcione

## 🧭 Como reconhecer o padrão

Quando o enunciado permite "qualquer resposta válida" e a restrição é sobre PARIDADE de contagens, geralmente existe uma construção direta e determinística (sem busca ou simulação) baseada na paridade do próprio `n` — pense primeiro na resposta matemática antes de tentar simular algo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar candidatos aleatórios ou testar combinações de letras até achar uma cujas contagens sejam todas ímpares — não existe uma versão "eficiente-mas-ingênua" real aqui, pois a resposta correta é uma construção direta O(n).

- Tempo: indefinido/ineficiente se feito por tentativa e erro · Espaço: O(n)
- **Por que não basta:** gerar e testar candidatos é desnecessário quando existe uma fórmula direta baseada só na paridade de `n`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Se `n` é ímpar, a string `"a"` repetida `n` vezes já tem uma única letra com contagem `n` (ímpar) — resolve sozinha. Se `n` é par, use `"a"` repetida `n-1` vezes (contagem par-1 = ímpar) mais um único `"b"` no final (contagem 1, ímpar) — duas letras, ambas com contagem ímpar, somando `n` caracteres.

## 🎬 Exemplo passo a passo

`n = 4` (par)

| Passo | Verificação | Construção |
|---|---|---|
| 1 | n é par? | sim |
| 2 | 'a' repetido (n-1)=3 vezes | "aaa" |
| 3 | + 'b' uma vez | "aaab" |

Resultado final: `"aaab"` ✔ (contagem de 'a' = 3, ímpar; contagem de 'b' = 1, ímpar)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — construção da string de tamanho n
- **Espaço:** O(n) — para a string resultante

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String generateTheString(int n) {
    StringBuilder resultado = new StringBuilder();
    if (n % 2 == 1) {
        // n ímpar: uma única letra repetida n vezes já tem contagem ímpar
        for (int i = 0; i < n; i++) {
            resultado.append('a');
        }
    } else {
        // n par: (n-1) 'a's (contagem ímpar, pois n-1 é ímpar) + 1 'b' (contagem 1, ímpar)
        for (int i = 0; i < n - 1; i++) {
            resultado.append('a');
        }
        resultado.append('b');
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

- Tentar usar sempre a mesma letra independente da paridade de `n` — se `n` é par e você usa só `"a"` repetido `n` vezes, a contagem de 'a' seria PAR, violando a condição.
- Superengenhar a solução tentando distribuir várias letras diferentes quando só 1 ou 2 letras já resolvem qualquer valor de `n` — o problema aceita qualquer resposta válida, não precisa de diversidade de letras.
- Esquecer que `n=1` já é ímpar e cai no caso simples (uma letra só) — não precisa de tratamento especial separado do caso "n ímpar" geral.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado (uma resposta válida) | Por quê |
|---|---|---|---|
| n par | `n=4` | "aaab" | contagens 3 e 1, ambas ímpares |
| n par pequeno | `n=2` | "ab" | contagens 1 e 1, ambas ímpares |
| n ímpar | `n=7` | "aaaaaaa" | contagem 7, ímpar, uma única letra basta |
| n mínimo | `n=1` | "a" | contagem 1, ímpar, caso trivial |

## 🔗 Conexões

- Problemas irmãos: [0409] Longest Palindrome (mesmo domínio de raciocinar sobre paridade de contagens de caracteres), [0242] Valid Anagram (mesma base de contagem de caracteres, embora com objetivo diferente)
- No backend: geração de identificadores ou tokens sintéticos que precisam satisfazer uma propriedade estrutural simples (ex.: checksums baseados em paridade) sem precisar de aleatoriedade nem busca.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
