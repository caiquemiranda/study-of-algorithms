# [1078] Occurrences After Bigram

> 🔗 [LeetCode 1078](https://leetcode.com/problems/occurrences-after-bigram/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#String` `#Easy`

## 📜 O Problema

Dadas duas strings `first` e `second`, considere ocorrências num texto da forma `"first second third"`, onde `second` vem logo depois de `first`, e `third` vem logo depois de `second`.

Retorne **um array com todas as palavras `third`** para cada ocorrência de `"first second third"`.

**Exemplos:**
```
Input:  text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Input:  text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
```

**Restrições (e o que elas denunciam):**
- `1 <= text.length <= 1000` → pequeno, O(n) resolve com folga
- palavras separadas por um único espaço, sem espaços nas bordas → tokenização simples com split
- `first` e `second` sempre têm entre 1 e 10 caracteres → comparação de string curta, O(1) efetivo por comparação

## 🧭 Como reconhecer o padrão

"Encontre o padrão X Y Z na sequência de tokens e reporte todos os Z" é resolvido tokenizando o texto e percorrendo com uma janela de 3 posições consecutivas (`i-2, i-1, i`), verificando se as duas primeiras batem com `first` e `second`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Tokenizar o texto e, para cada posição `i` a partir do índice 2, checar se `palavras[i-2] == first` e `palavras[i-1] == second`; se sim, adicionar `palavras[i]` ao resultado — na prática, já é a solução ótima, pois o problema é inerentemente sequencial.

- Tempo: O(n) — cada palavra é visitada uma única vez como parte da janela de 3 · Espaço: O(n) para o array de palavras tokenizadas
- **Por que vale nomear mesmo assim:** a solução "ingênua" e a "ótima" aqui são praticamente a mesma coisa; a única armadilha é indexar a janela de 3 palavras corretamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Tokenize `text` com `split(" ")`. Percorra os índices de `2` até o final, comparando `palavras[i-2]` com `first` e `palavras[i-1]` com `second`; se ambos baterem, adicione `palavras[i]` ao resultado.

## 🎬 Exemplo passo a passo

`text = "alice is a good girl she is a good student"`, `first = "a"`, `second = "good"`

palavras: alice, is, a, good, girl, she, is, a, good, student

| Passo | i | palavras[i-2] | palavras[i-1] | palavras[i] | bate com "a good"? | Ação |
|---|---|---|---|---|---|---|
| 1 | 2 | alice | is | a | não | ignora |
| 2 | 3 | is | a | good | não | ignora |
| 3 | 4 | a | good | girl | **sim** | adiciona "girl" |
| 4 | 5 | good | girl | she | não | ignora |
| 5 | 6 | girl | she | is | não | ignora |
| 6 | 7 | she | is | a | não | ignora |
| 7 | 8 | is | a | good | não | ignora |
| 8 | 9 | a | good | student | **sim** | adiciona "student" |

Resultado final: `["girl","student"]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — n = número de palavras
- **Espaço:** O(n) — para o array tokenizado e o resultado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String[] findOcurrences(String text, String first, String second) {
    String[] palavras = text.split(" ");
    List<String> resultado = new ArrayList<>();

    for (int i = 2; i < palavras.length; i++) {
        if (palavras[i - 2].equals(first) && palavras[i - 1].equals(second)) {
            resultado.add(palavras[i]); // achou o padrão "first second", captura o terceiro
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

- Começar o loop em `i = 0` sem checar limites — acessar `palavras[i-2]` com `i < 2` gera `ArrayIndexOutOfBoundsException`; o loop precisa começar em `i = 2`.
- Usar `==` em vez de `.equals()` para comparar Strings em Java — `==` compara referências, não conteúdo, e pode falhar de forma inconsistente dependendo do pool de strings da JVM.
- Não considerar padrões sobrepostos (ex.: `"a a a"` com `first="a", second="a"`) — o algoritmo já trata isso corretamente, pois cada janela de 3 é avaliada independentemente, incluindo janelas que compartilham palavras com a anterior.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Padrão repetido | `text="alice is a good girl she is a good student", first="a", second="good"` | ["girl","student"] | caso padrão do enunciado |
| Padrões sobrepostos | `text="we will we will rock you", first="we", second="will"` | ["we","rock"] | a segunda ocorrência de "we will" também é capturada |
| Padrão nunca ocorre | `text="a b c", first="x", second="y"` | [] | nenhuma janela bate com first/second |
| Texto mínimo com padrão | `text="a b c", first="a", second="b"` | ["c"] | exatamente uma janela de 3 palavras |

## 🔗 Conexões

- Problemas irmãos: [0187] Repeated DNA Sequences (mesma técnica de janela fixa percorrendo tokens/caracteres), [0459] Repeated Substring Pattern (mesmo domínio de reconhecer padrões numa sequência)
- No backend: extração de trigramas ou N-gramas em processamento de linguagem natural (ex.: identificar palavras que seguem uma sequência específica de duas palavras em análise de texto, base de modelos simples de linguagem).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
