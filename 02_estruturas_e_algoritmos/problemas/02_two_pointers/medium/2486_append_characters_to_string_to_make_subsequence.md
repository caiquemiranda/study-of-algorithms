# [2486] Append Characters to String to Make Subsequence

> 🔗 [LeetCode 2486](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Greedy` `#Medium`

## 📜 O Problema

Dadas `s` e `t`, retorne o número **mínimo** de caracteres que precisam ser anexados ao final de `s` para que `t` se torne uma **subsequência** de `s`.

**Exemplos:**
```
Input:  s = "coaching", t = "coding"
Output: 4
Explicação: anexa "ding" → "coachingding"; t = "coding" já é subsequência.

Input:  s = "abcde", t = "a"
Output: 0
Explicação: t já é subsequência de s.

Input:  s = "z", t = "abcde"
Output: 5
Explicação: nenhum caractere de t aparece em s, precisa anexar tudo.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length, t.length <= 10^5` → O(n+m) é o esperado
- "Anexar ao FINAL" → só interessa quanto de `t`, na ORDEM, já é encontrado em `s`; o resto vira anexo direto, sem precisar decidir onde inserir

## 🧭 Como reconhecer o padrão

Este problema é uma extensão direta de [0392] Is Subsequence: em vez de responder só "sim ou não", ele pede **quanto falta**. A mesma varredura greedy com dois ponteiros resolve — o que sobra de `t` sem ser casado é exatamente o que precisa ser anexado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada tamanho de sufixo `k` de `t` a ser descartado (começando em `0`), checar se o prefixo restante de `t` é subsequência de `s` usando a checagem completa de [0392], aumentando `k` até achar um que funcione.

- Tempo: O(t.length() × s.length()) — múltiplas checagens completas de subsequência · Espaço: O(1) por checagem
- **Por que não basta:** recalcula do zero, para cada tentativa de `k`, uma checagem que já tinha sido parcialmente feita antes; uma única passada greedy já encontra o maior prefixo de `t` que é subsequência de `s`, sem precisar tentar vários tamanhos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `i` em `s` e `j` em `t`, exatamente como em [0392] Is Subsequence: percorra `s` com `i`; sempre que `s[i] == t[j]`, avance `j` também (esse caractere de `t` foi "encontrado"). Ao final, `j` representa quantos caracteres de `t` já são cobertos por `s` na ordem certa — os que sobram (`t.length() - j`) são exatamente os que precisam ser anexados.

## 🎬 Exemplo passo a passo

`s = "coaching"`, `t = "coding"`

| Passo | i | s[i] | j (antes) | t[j] esperado | Match? | Ação |
|---|---|---|---|---|---|---|
| 1 | 0 | `c` | 0 | `c` | sim | avança `j` e `i` |
| 2 | 1 | `o` | 1 | `o` | sim | avança `j` e `i` |
| 3 | 2–7 | `a,c,h,i,n,g` | 2 | `d` | não (nenhum bate) | `i` avança até o fim de `s`, `j` permanece em 2 |

`j` final = 2 (só `"co"` casado); resposta = `t.length()(6) - j(2) = 4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — cada ponteiro percorre sua string uma única vez
- **Espaço:** O(1) — só os índices `i` e `j`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int appendCharacters(String s, String t) {
    int i = 0;
    int j = 0;
    int n = s.length();
    int m = t.length();

    while (i < n && j < m) {
        if (s.charAt(i) == t.charAt(j)) {
            j++; // esse caractere de t foi encontrado em s, na ordem certa
        }
        i++;
    }

    return m - j; // caracteres de t que não foram encontrados em s, precisam ser anexados
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

- Achar que é preciso REMOVER caracteres de `t` e testar — não é: a resposta é simplesmente `t.length() - (quantos de t já foram casados)`, sem precisar simular remoção nenhuma.
- Confundir este problema com [0392] Is Subsequence — aqui a pergunta não é "é subsequência?" (sim/não), é "quantos caracteres faltam pra virar subsequência?"; a técnica de dois ponteiros é a mesma, só a métrica final muda.
- Achar que precisa de um caso especial para "já é subsequência" — se `t` já é subsequência completa de `s`, `j` naturalmente chega a `m` durante o loop, dando resposta `0` sem nenhum tratamento extra.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Precisa anexar parte | `s="coaching"`, `t="coding"` | 4 | só `"co"` é casado, faltam 4 caracteres de `"ding"` |
| Já é subsequência | `s="abcde"`, `t="a"` | 0 | `t` inteiro já é encontrado em `s` |
| Nenhum caractere casa | `s="z"`, `t="abcde"` | 5 | nenhum caractere de `t` aparece em `s`, precisa anexar tudo |
| Casamento perfeito | `s="ab"`, `t="ab"` | 0 | `t` inteiro já casa, sem precisar anexar nada |

## 🔗 Conexões

- Problemas irmãos: [0392] Is Subsequence (a mesma técnica de dois ponteiros, mas respondendo sim/não em vez de quantificar o que falta), [1961] Check if String Is a Prefix of Array (mesma família de "consumir" uma sequência progressivamente)
- No backend: calcular quantos campos obrigatórios ainda faltam ser preenchidos ao final de um formulário/payload parcialmente compatível com um esquema esperado, processando o que já existe numa única passada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
