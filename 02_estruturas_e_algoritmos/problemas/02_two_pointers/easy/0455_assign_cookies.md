# [0455] Assign Cookies

> 🔗 [LeetCode 455](https://leetcode.com/problems/assign-cookies/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Greedy` `#Sorting` `#Easy`

## 📜 O Problema

Cada criança `i` tem um fator de gula `g[i]` (o tamanho mínimo de biscoito que a satisfaz), e cada biscoito `j` tem um tamanho `s[j]`. Um biscoito `j` satisfaz a criança `i` se `s[j] >= g[i]`. Cada criança recebe no máximo um biscoito. Retorne o número **máximo** de crianças que podem ficar satisfeitas.

**Exemplos:**
```
Input:  g = [1,2,3], s = [1,1]
Output: 1
Explicação: só dá pra satisfazer a criança de gula 1; os dois biscoitos são de tamanho 1.

Input:  g = [1,2], s = [1,2,3]
Output: 2
Explicação: há biscoitos suficientes pra satisfazer as duas crianças.
```

**Restrições (e o que elas denunciam):**
- `1 <= g.length <= 3 * 10^4`, `0 <= s.length <= 3 * 10^4` → força bruta O(g×s) pode chegar a 9×10^8; O((g+s) log(g+s)) (sort) é o esperado
- `s.length` pode ser `0` → caso de borda sem nenhum biscoito, resposta sempre 0
- `1 <= g[i], s[j] <= 2^31 - 1` → sem casos negativos ou zero pra tratar

## 🧭 Como reconhecer o padrão

"Combinar dois grupos por um critério de limiar (`>=`), maximizando o número de pares" é resolvido ordenando os dois arrays e usando dois ponteiros que avançam de forma greedy: sempre tente satisfazer a criança **menos** gulosa restante com o biscoito **menor** disponível que já sirva para ela — se um biscoito pequeno não serve nem pra essa criança, ele não serve pra nenhuma outra (todas as outras são mais ou igualmente gulosas).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada criança (em qualquer ordem), percorrer todos os biscoitos ainda não usados procurando algum que a satisfaça, e marcá-lo como usado se encontrar.

- Tempo: O(g.length × s.length) — no pior caso, cada criança escaneia todos os biscoitos restantes · Espaço: O(1) além do controle de "usado"
- **Por que não basta:** ignora a estrutura que a ordenação oferece; sem processar crianças e biscoitos do menor para o maior, não há garantia de estar fazendo a escolha ótima em cada passo, e o tempo vira quadrático.

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `g` e `s` em ordem crescente. Use um ponteiro `i` na criança menos gulosa ainda não satisfeita, e `j` no menor biscoito ainda não usado. Se `s[j] >= g[i]`, esse biscoito satisfaz essa criança — conte e avance os dois ponteiros. Se não satisfizer, esse biscoito é pequeno demais até para a criança menos gulosa de todas as restantes, então ele não serve pra ninguém — descarte-o avançando só `j`.

## 🎬 Exemplo passo a passo

`g = [1,2,3]` (já ordenado), `s = [1,1]` (já ordenado)

| Passo | i | j | g[i] | s[j] | Suficiente? | Ação |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1 | 1 | sim | satisfaz: i=1, j=1 |
| 2 | 1 | 1 | 2 | 1 | não | descarta o biscoito: j=2 |
| 3 | 1 | 2 (esgotado) | — | — | — | `j == s.length`, loop termina |

Crianças satisfeitas: `i = 1` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(g log g + s log s) — dominado pela ordenação dos dois arrays; o scan com dois ponteiros depois é O(g + s)
- **Espaço:** O(log g + log s) — só o espaço interno do sort (ou O(1) extra se usar um algoritmo de sort in-place)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findContentChildren(int[] g, int[] s) {
    Arrays.sort(g);
    Arrays.sort(s);

    int i = 0; // criança menos gulosa ainda não satisfeita
    int j = 0; // menor biscoito ainda não usado

    while (i < g.length && j < s.length) {
        if (s[j] >= g[i]) {
            // biscoito atual satisfaz a criança menos gulosa restante: usa e avança os dois
            i++;
        }
        // se não satisfizer, esse biscoito não serve pra ninguém mais (todos os outros são mais gulosos)
        j++;
    }

    return i; // quantidade de crianças satisfeitas
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

- Não ordenar os dois arrays antes — sem ordenação, a escolha greedy "usa o menor biscoito suficiente" não tem garantia de ser ótima; a prova de corretude depende de processar ambos do menor pro maior.
- Avançar `i` e `j` juntos mesmo quando `s[j] < g[i]` — isso descartaria uma criança que ainda poderia ser satisfeita por um biscoito maior; só avance `i` quando de fato satisfizer.
- Esquecer que `s.length` pode ser `0` (constraint permite) — o `while` já trata isso naturalmente, nunca entrando no loop e retornando 0.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Poucos biscoitos | `g=[1,2,3]`, `s=[1,1]` | 1 | só o biscoito de tamanho 1 serve, e só pra criança de gula 1 |
| Biscoitos suficientes | `g=[1,2]`, `s=[1,2,3]` | 2 | sobra biscoito, mas todas as crianças são satisfeitas |
| Sem biscoitos | `g=[1]`, `s=[]` | 0 | loop nem executa, `j` já começa fora dos limites |
| Nenhum biscoito serve | `g=[5]`, `s=[1,2,3]` | 0 | nenhum biscoito atinge o tamanho mínimo exigido |

## 🔗 Conexões

- Problemas irmãos: [2410] Maximum Matching of Players With Trainers (o mesmo problema, com nomes diferentes — citado no próprio enunciado), [0016] 3Sum Closest (mesma família de "ordenar e usar dois ponteiros com decisão greedy" sobre arrays)
- No backend: alocação greedy de recursos limitados a demandas com requisito mínimo — por exemplo, atribuir servidores com capacidade mínima a tarefas que exigem um limiar de CPU/memória, maximizando quantas tarefas são atendidas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
