# [0316] Remove Duplicate Letters

> 🔗 [LeetCode 316](https://leetcode.com/problems/remove-duplicate-letters/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Greedy`

## 📜 O Problema

Dada uma string `s`, remova letras duplicadas de forma que cada letra apareça exatamente uma vez. O resultado deve ser o **menor em ordem lexicográfica** entre todos os resultados possíveis.

**Exemplos:**
```
Input:  s = "bcabc"
Output: "abc"

Input:  s = "cbacdcbc"
Output: "acdb"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^4` → precisa de solução O(n) ou O(26n); qualquer coisa quadrática arriscaria no limite
- `s` consiste só de letras minúsculas do inglês → alfabeto fixo de 26, permite usar arrays de tamanho fixo para "última ocorrência" e "já usado", em vez de hash maps genéricos

## 🧭 Como reconhecer o padrão

"Construir a menor sequência possível respeitando que cada elemento aparece uma vez, decidindo greedily se descarta um elemento anterior para dar lugar a um menor" é o padrão de **monotonic stack greedy**: você quer manter a pilha crescente (lexicograficamente), e só desempilha o topo se ele for maior que o caractere atual **E** ainda existir outra chance de reempilhá-lo mais tarde (ou seja, ele ainda ocorre depois na string).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Gerar todas as subsequências possíveis que contêm cada letra distinta exatamente uma vez, e escolher a lexicograficamente menor entre as válidas.

- Tempo: exponencial (combinatório) · Espaço: exponencial
- **Por que não basta:** o número de subsequências candidatas explode combinatorialmente; para `n=10^4` isso é completamente inviável. É preciso uma decisão gulosa, caractere a caractere, que garanta otimalidade sem enumerar alternativas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pré-processe a **última ocorrência** de cada letra na string (um array de 26 posições). Percorra `s` com uma pilha que representa o resultado sendo construído. Para cada caractere `c`: se `c` já está na pilha (rastreado por um `seen` de 26 posições), pule-o — ele já está representado, e mover sua posição pioraria a ordem. Caso contrário, enquanto o topo da pilha for **maior** que `c` **e** esse topo ainda ocorrer novamente mais adiante na string (segundo a última ocorrência pré-computada), desempilhe-o (ele será reinserido depois, numa posição melhor). Empilhe `c`. No final, a pilha é a resposta.

## 🎬 Exemplo passo a passo

`s = "cbacdcbc"`, últimas ocorrências: `c→7, b→6, a→2, d→4`

| Passo | i | c | Já na pilha? | Ação do while (topo > c e topo reaparece depois) | Pilha após |
|---|---|---|---|---|---|
| 1 | 0 | `c` | não | pilha vazia | `[c]` |
| 2 | 1 | `b` | não | topo `c` > `b`, e `c` reaparece depois (última em 7 > 1) → pop `c` | `[b]` |
| 3 | 2 | `a` | não | topo `b` > `a`, `b` reaparece depois (última em 6 > 2) → pop `b` | `[a]` |
| 4 | 3 | `c` | não | topo `a` < `c`, para | `[a, c]` |
| 5 | 4 | `d` | não | topo `c` < `d`, para | `[a, c, d]` |
| 6 | 5 | `c` | sim (já na pilha) | pula | `[a, c, d]` |
| 7 | 6 | `b` | não | topo `d` > `b`, mas `d` NÃO reaparece depois (última ocorrência de `d` é 4, já passamos) → não desempilha | `[a, c, d, b]` |
| 8 | 7 | `c` | sim (já na pilha) | pula | `[a, c, d, b]` |

Resultado final: `"acdb"` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere é empilhado e desempilhado no máximo uma vez; o pré-processamento das últimas ocorrências é O(n)
- **Espaço:** O(1) extra além da pilha — os arrays de "última ocorrência" e "já visto" têm tamanho fixo 26; a pilha em si guarda no máximo 26 caracteres (um de cada letra)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String removeDuplicateLetters(String s) {
    int[] ultimaOcorrencia = new int[26];
    for (int i = 0; i < s.length(); i++) {
        ultimaOcorrencia[s.charAt(i) - 'a'] = i; // sobrescreve: fica com o ÚLTIMO índice de cada letra
    }

    boolean[] naPilha = new boolean[26];
    Deque<Character> pilha = new ArrayDeque<>();

    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (naPilha[c - 'a']) {
            continue; // já representado no resultado, mover pioraria a ordem
        }
        // desempilha enquanto o topo for maior E ainda tiver outra chance mais à frente
        while (!pilha.isEmpty() && pilha.peek() > c && ultimaOcorrencia[pilha.peek() - 'a'] > i) {
            naPilha[pilha.pop() - 'a'] = false;
        }
        pilha.push(c);
        naPilha[c - 'a'] = true;
    }

    StringBuilder resultado = new StringBuilder();
    while (!pilha.isEmpty()) {
        resultado.append(pilha.pop());
    }
    return resultado.reverse().toString();
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

- Desempilhar o topo mesmo quando ele **não reaparece mais** na string à frente — isso perderia a letra para sempre (ela nunca mais poderia ser reinserida), violando a regra de "cada letra aparece exatamente uma vez". A condição `ultimaOcorrencia[topo] > i` é essencial.
- Esquecer de pular caracteres que já estão na pilha (`naPilha[c]`) — sem isso, a mesma letra poderia ser empilhada de novo, quebrando a garantia de unicidade.
- Confundir "primeira ocorrência" com "última ocorrência" ao pré-computar — o array precisa da **última** posição de cada letra, porque é isso que determina se ainda há uma "próxima chance" de reinserir o caractere desempilhado.
- Achar que a ordem gulosa por si só garante o menor resultado sem a checagem de última ocorrência — sem essa checagem, o algoritmo se comportaria como o problema mais simples "menor subsequência mantendo k caracteres" ([0402] Remove K Digits), que tem uma regra diferente (remover até k, não até garantir unicidade).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já em ordem crescente com duplicatas | `"abcabc"` | `"abc"` | cada letra distinta já está na melhor posição possível |
| Ordem decrescente forçando trocas | `"cba"` | `"cba"` | nenhuma letra reaparece depois, então nada pode ser desempilhado (única ocorrência de cada) |
| Letra repetida no início bloqueando otimização | `"cbacdcbc"` | `"acdb"` | caso do enunciado, testa a interação completa entre desempilhar e a checagem de última ocorrência |
| Um único caractere repetido várias vezes | `"aaaa"` | `"a"` | todas as ocorrências extras são puladas por já estar na pilha |

## 🔗 Conexões

- Problemas irmãos: [0402] Remove K Digits (mesma técnica de monotonic stack greedy, mas removendo exatamente k caracteres em vez de garantir unicidade), [1081] Smallest Subsequence of Distinct Characters (o mesmo problema, com outro número no LeetCode)
- No backend: essa técnica de "manter a menor sequência possível, descartando elementos anteriores quando ainda há chance de reinserção futura" aparece em deduplicação de listas ordenadas preservando a menor representação canônica, e em otimização de sequências de eventos onde cada tipo de evento só pode aparecer uma vez no resultado final.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
