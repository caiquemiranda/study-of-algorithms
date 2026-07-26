# [1446] Consecutive Characters

> 🔗 [LeetCode 1446](https://leetcode.com/problems/consecutive-characters/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

A **potência** de uma string é o comprimento máximo de uma substring não vazia que contém apenas um único caractere distinto. Dada uma string `s`, retorne a potência de `s`.

**Exemplos:**
```
Input:  s = "leetcode"
Output: 2
Explicação: a substring "ee" tem comprimento 2 usando só o caractere 'e'.

Input:  s = "abbcccddddeeeeedcba"
Output: 5
Explicação: a substring "eeeee" tem comprimento 5 usando só o caractere 'e'.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 500` → O(n) resolve com folga
- só letras minúsculas → sem complicação de caixa

## 🧭 Como reconhecer o padrão

"Maior substring formada por um único caractere repetido" é o mesmo padrão de contador de streak já visto em [0485] Max Consecutive Ones e [0830] Positions of Large Groups: cresce enquanto o caractere se repete, reseta ao mudar.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada posição `i`, expandir para a direita enquanto `s[j] == s[i]`, redescobrindo o mesmo trecho repetidamente.

- Tempo: O(n²) — repete a expansão de posições já cobertas pelo mesmo grupo · Espaço: O(1)
- **Por que não basta:** recalcula o tamanho de um grupo de caracteres repetidos a cada posição interna dele, quando um contador de streak já resolve tudo numa única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Uma passada com um contador `atual` que incrementa quando `s[i] == s[i-1]`, reseta a 1 caso contrário; atualiza `maximo` a cada passo.

## 🎬 Exemplo passo a passo

`s = "abbcccddddeeeeedcba"` (trecho ilustrativo até o grupo máximo)

| Passo | i | s[i] | s[i-1] | atual | maximo |
|---|---|---|---|---|---|
| 1 | 0 | a | — | 1 | 1 |
| 2 | 1 | b | a | 1 (reset) | 1 |
| 3 | 2 | b | b | 2 | 2 |
| 4 | 3 | c | b | 1 (reset) | 2 |
| 5 | 4-5 | c,c | c,c | 3 | 3 |
| 6 | 6-9 | dddd | (grupo de 4 d's) | 4 | 4 |
| 7 | 10-14 | eeeee | (grupo de 5 e's) | 5 | **5** |
| 8 | 15-19 | dcba | (todos diferentes do anterior) | 1 | 5 |

Resultado final: `5` ✔ ("eeeee")

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1) — dois contadores inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int maxPower(String s) {
    int atual = 1;
    int maximo = 1;
    for (int i = 1; i < s.length(); i++) {
        if (s.charAt(i) == s.charAt(i - 1)) {
            atual++;
        } else {
            atual = 1; // caractere mudou, reinicia contando o elemento atual
        }
        maximo = Math.max(maximo, atual);
    }
    return maximo;
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

- Inicializar `atual` e `maximo` como `0` em vez de `1` — uma string de um único caractere sempre tem potência pelo menos 1.
- Resetar `atual` para `0` em vez de `1` ao mudar de caractere — o próprio caractere que quebrou a sequência já inicia um novo grupo de tamanho 1.
- Confundir "substring" com "subsequência" — tem que ser CONTÍGUO, não vale pular caracteres para achar um grupo maior.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Repetição no meio | "leetcode" | 2 | "ee" é o maior grupo |
| Vários grupos | "abbcccddddeeeeedcba" | 5 | "eeeee" é o maior |
| Sem repetição | "abcdef" | 1 | nenhum caractere se repete |
| Toda a string igual | "aaaa" | 4 | string inteira é um único grupo |

## 🔗 Conexões

- Problemas irmãos: [0485] Max Consecutive Ones, [0830] Positions of Large Groups (mesma técnica de contador de streak)
- No backend: detecção de rajadas em logs (ex.: maior sequência de status idêntico consecutivo, como "OK OK OK" antes de uma falha).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
