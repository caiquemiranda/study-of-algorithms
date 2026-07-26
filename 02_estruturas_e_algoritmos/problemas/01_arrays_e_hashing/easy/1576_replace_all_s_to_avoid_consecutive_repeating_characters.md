# [1576] Replace All ?'s to Avoid Consecutive Repeating Characters

> 🔗 [LeetCode 1576](https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Dada uma string `s` contendo apenas letras minúsculas do inglês e o caractere `'?'`, converta todos os caracteres `'?'` em letras minúsculas de forma que a string final não contenha caracteres repetidos consecutivos. Você **não pode** modificar os caracteres que não são `'?'`.

É garantido que não há caracteres repetidos consecutivos na string dada, exceto por `'?'`.

Retorne a string final após todas as conversões. Se houver mais de uma solução, retorne qualquer uma delas.

**Exemplos:**
```
Input:  s = "?zs"
Output: "azs"
Explicação: há 25 soluções para este problema. De "azs" até "yzs", todas são válidas.
Só "z" é uma modificação inválida, pois geraria "zzs" (repetição consecutiva).

Input:  s = "ubv?w"
Output: "ubvaw"
Explicação: há 24 soluções. Só "v" e "w" são modificações inválidas, pois gerariam
"ubvvw" e "ubvww".
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → pequeno, O(n) resolve com folga
- garantido que não há repetição consecutiva EXCETO por causa de '?' → simplifica a lógica, só precisa se preocupar com os vizinhos do '?' atual
- "se houver múltiplas soluções, retorne qualquer uma" → não precisa de uma escolha ótima, só uma válida

## 🧭 Como reconhecer o padrão

"Substituir um caractere curinga evitando um conflito local com os vizinhos" é resolvido gulosamente, caractere por caractere: para cada '?', escolha qualquer letra entre um pequeno conjunto fixo (ex.: 'a', 'b', 'c') que não seja igual ao vizinho da esquerda nem ao da direita — como só 2 vizinhos existem, e há 3 letras candidatas, sempre existe pelo menos uma opção livre.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada '?', testar as 26 letras do alfabeto até achar uma que não conflite com os vizinhos.

- Tempo: O(n × 26) · Espaço: O(n) para o resultado
- **Por que não basta:** testar as 26 letras é desnecessário quando um conjunto fixo de só 3 letras (`'a', 'b', 'c'`) já garante matematicamente que sempre há uma opção livre.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra a string caractere por caractere. Para cada `'?'`, teste 'a', 'b', 'c' nessa ordem; escolha a primeira que for diferente do caractere anterior (já processado) E do caractere seguinte original (se existir). Substitua e continue.

## 🎬 Exemplo passo a passo

`s = "ubv?w"`

| Passo | i | s[i] | vizinho esquerdo (já processado) | vizinho direito (original) | letra escolhida |
|---|---|---|---|---|---|
| 1 | 0 | u | — | b | u (não é '?', mantém) |
| 2 | 1 | b | u | v | b (mantém) |
| 3 | 2 | v | b | ? | v (mantém) |
| 4 | 3 | ? | v | w | testa 'a': 'a'≠v e 'a'≠w → escolhe 'a' |
| 5 | 4 | w | a | — | w (mantém) |

Resultado final: `"ubvaw"` ✔ (uma das respostas válidas aceitas pelo enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — no máximo 3 tentativas de letra por '?'
- **Espaço:** O(n) — para o resultado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String modifyString(String s) {
    char[] chars = s.toCharArray();

    for (int i = 0; i < chars.length; i++) {
        if (chars[i] != '?') {
            continue;
        }
        for (char candidata = 'a'; candidata <= 'c'; candidata++) {
            boolean conflitaEsquerda = i > 0 && chars[i - 1] == candidata;
            boolean conflitaDireita = i < chars.length - 1 && chars[i + 1] == candidata;
            if (!conflitaEsquerda && !conflitaDireita) {
                chars[i] = candidata; // achou uma letra livre, substitui e para de testar
                break;
            }
        }
    }
    return new String(chars);
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

- Testar só 2 letras candidatas em vez de 3 — com só 2 vizinhos a evitar e 2 letras candidatas, pode acontecer de as duas conflitarem simultaneamente; 3 letras garantem matematicamente que sobra pelo menos uma livre.
- Esquecer de atualizar `chars[i]` ANTES de processar o próximo `'?'` — se dois `'?'` forem adjacentes, o segundo precisa "ver" a escolha já feita para o primeiro (por isso o array é modificado in-place, não uma cópia separada).
- Comparar o `'?'` atual com o caractere ORIGINAL à direita quando esse também é `'?'` — nesse caso, comparar com `'?'` nunca gera conflito de verdade (já que `'?'` não é uma letra candidata), então a lógica funciona mesmo sem tratamento especial.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado (uma resposta válida) | Por quê |
|---|---|---|---|
| Um '?' na borda | "?zs" | "azs" | 'a' não conflita com 'z' (não há vizinho esquerdo) |
| Um '?' no meio | "ubv?w" | "ubvaw" | 'a' não conflita nem com 'v' nem com 'w' |
| Múltiplos '?' adjacentes | "??" | "ab" | primeiro '?' vira 'a', segundo precisa ser diferente de 'a', vira 'b' |
| '?' cercado por letras iguais entre si | "a?a" | "aba" | 'b' não conflita com nenhum dos dois 'a's |

## 🔗 Conexões

- Problemas irmãos: [0767] Reorganize String (mesmo domínio de evitar repetição consecutiva, mas reorganizando em vez de substituir curingas), [1370] Increasing Decreasing String (mesma família de reconstrução de string sob restrições locais)
- No backend: preenchimento de campos "coringa" em templates de configuração respeitando restrições de adjacência (ex.: gerar identificadores onde certos padrões consecutivos são proibidos por regra de negócio).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
