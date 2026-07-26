# [1128] Number of Equivalent Domino Pairs

> 🔗 [LeetCode 1128](https://leetcode.com/problems/number-of-equivalent-domino-pairs/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#Counting` `#Easy`

## 📜 O Problema

Dada uma lista de `dominoes`, `dominoes[i] = [a, b]` é **equivalente a** `dominoes[j] = [c, d]` se e somente se (`a == c` e `b == d`), ou (`a == d` e `b == c`) — ou seja, um dominó pode ser rotacionado para ficar igual ao outro.

Retorne **o número de pares `(i, j)`** para os quais `0 <= i < j < dominoes.length`, e `dominoes[i]` é equivalente a `dominoes[j]`.

**Exemplos:**
```
Input:  dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Input:  dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
```

**Restrições (e o que elas denunciam):**
- `1 <= dominoes.length <= 4×10^4` → precisa O(n); O(n²) (todos os pares) seria 1.6×10^9 — inviável
- `1 <= dominoes[i][j] <= 9` → só 9 valores possíveis por metade da peça, permitindo uma chave canônica compacta

## 🧭 Como reconhecer o padrão

"Conte pares equivalentes sob uma relação de simetria (aqui, rotação)" é resolvido normalizando cada elemento para uma forma canônica (que ignora a simetria) e contando quantos pares se formam entre elementos com a MESMA forma canônica.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par de índices `(i, j)` com `i < j`, verificar se `dominoes[i]` é equivalente a `dominoes[j]` (nas duas orientações possíveis) e contar.

- Tempo: O(n²) — todos os pares possíveis, cada checagem O(1) · Espaço: O(1) extra
- **Por que não basta:** com n até 4×10^4, n² chega a 1.6 bilhões de comparações — inviável dentro de um tempo razoável.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada dominó `[a,b]`, construa uma chave canônica que trate `[a,b]` e `[b,a]` como iguais (ex.: `min(a,b)*10 + max(a,b)`). Conte quantas vezes cada chave canônica aparece num hash map, acumulando os pares incrementalmente: cada dominó já visto com a mesma chave forma um novo par com o dominó atual.

## 🎬 Exemplo passo a passo

`dominoes = [[1,2],[2,1],[3,4],[5,6]]`

| Passo | dominó | chave canônica (min×10+max) | vistosAntes com essa chave | pares acumulados | contagem[chave] depois |
|---|---|---|---|---|---|
| 1 | [1,2] | 12 | 0 | 0 | 1 |
| 2 | [2,1] | 12 (min=1,max=2, mesma chave) | 1 | 0+1=1 | 2 |
| 3 | [3,4] | 34 | 0 | 1 | 1 |
| 4 | [5,6] | 56 | 0 | 1 | 1 |

Resultado final: `1` ✔ (o par formado por `[1,2]` e `[2,1]`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada acumulando contagem e pares
- **Espaço:** O(n) — para o mapa de contagem (no máximo 100 chaves possíveis, já que os valores vão de 1 a 9)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numEquivDominoPairs(int[][] dominoes) {
    Map<Integer, Integer> contagem = new HashMap<>();
    int pares = 0;

    for (int[] domino : dominoes) {
        int a = Math.min(domino[0], domino[1]);
        int b = Math.max(domino[0], domino[1]);
        int chave = a * 10 + b; // canoniza [a,b] e [b,a] para a mesma chave

        int vistosAntes = contagem.getOrDefault(chave, 0);
        pares += vistosAntes; // cada dominó já visto com a mesma chave forma um novo par com este
        contagem.put(chave, vistosAntes + 1);
    }
    return pares;
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

- Esquecer de normalizar a ordem (`min`/`max`) antes de formar a chave — sem isso, `[1,2]` e `[2,1]` gerariam chaves diferentes (`12` e `21`), quando deveriam ser tratadas como equivalentes.
- Calcular todos os pares de uma vez no final com `k×(k-1)/2` em vez de acumular incrementalmente (`pares += vistosAntes` a cada dominó) — as duas abordagens funcionam, mas a incremental evita uma segunda passada pelo mapa.
- Usar `a + "," + b` como chave String em vez de uma chave numérica compacta (`a*10+b`) — funciona, mas é menos eficiente (hash de String é mais caro que hash de Integer).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um par equivalente | `[[1,2],[2,1],[3,4],[5,6]]` | 1 | só `[1,2]` e `[2,1]` formam um par |
| Múltiplos pares na mesma chave | `[[1,2],[1,2],[1,1],[1,2],[2,2]]` | 3 | três dominós `[1,2]` formam `3 escolhe 2 = 3` pares |
| Nenhum par equivalente | `[[1,2],[3,4],[5,6]]` | 0 | todas as chaves são únicas |
| Todos equivalentes | `[[1,1],[1,1],[1,1]]` | 3 | dominó "duplo" (`a==b`) também segue a mesma regra, `3 escolhe 2 = 3` |

## 🔗 Conexões

- Problemas irmãos: [0001] Two Sum (mesma técnica de acumular contagem num hash map enquanto percorre, somando pares incrementalmente), [0049] Group Anagrams (mesma ideia de canonicalizar antes de agrupar)
- No backend: contagem de pares equivalentes sob alguma relação de simetria (ex.: pares de coordenadas `(x,y)` e `(y,x)` tratadas como a mesma conexão numa rede não direcionada, ou detecção de registros duplicados que diferem só na ordem dos campos).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
