# [0771] Jewels and Stones

> 🔗 [LeetCode 771](https://leetcode.com/problems/jewels-and-stones/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Você recebe as strings `jewels`, representando os tipos de pedras que são joias, e `stones`, representando as pedras que você tem. Cada caractere em `stones` é um tipo de pedra que você possui. Você quer saber quantas das suas pedras também são joias.

As letras são case sensitive, então `"a"` é considerado um tipo de pedra diferente de `"A"`.

**Exemplos:**
```
Input:  jewels = "aA", stones = "aAAbbbb"
Output: 3

Input:  jewels = "z", stones = "ZZ"
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= jewels.length, stones.length <= 50` → entrada minúscula, qualquer abordagem serve com folga
- letras case-sensitive, caracteres de `jewels` são únicos → dá pra usar hash set sem se preocupar com duplicatas dentro de `jewels`

## 🧭 Como reconhecer o padrão

"Quantos elementos de uma coleção pertencem a um conjunto de referência" é sempre resolvido colocando o conjunto de referência (`jewels`) num hash set, e depois contando quantos elementos da outra coleção (`stones`) estão presentes nesse set — troca busca linear repetida por consulta O(1).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada pedra em `stones`, percorrer `jewels` caractere por caractere procurando uma correspondência.

- Tempo: O(stones × jewels) — busca linear de cada pedra dentro da string de joias · Espaço: O(1)
- **Por que não basta:** com os limites dados (até 50×50=2500) nem chega a ser um problema de performance, mas o padrão correto (que escala) é não repetir a busca em `jewels` a cada pedra — um `HashSet` responde isso em O(1).

## 💡 Solução 2 — A ideia otimizada (intuição)

Coloque todos os caracteres de `jewels` num `HashSet<Character>`. Percorra `stones` contando quantos caracteres estão presentes nesse set.

## 🎬 Exemplo passo a passo

`jewels = "aA"`, `stones = "aAAbbbb"` — set de jewels: `{'a', 'A'}`

| Passo | i | stones[i] | está no set? | contador |
|---|---|---|---|---|
| 1 | 0 | a | sim | 1 |
| 2 | 1 | A | sim | 2 |
| 3 | 2 | A | sim | 3 |
| 4 | 3 | b | não | 3 |
| 5 | 4 | b | não | 3 |
| 6 | 5 | b | não | 3 |
| 7 | 6 | b | não | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(j + s) — j = tamanho de jewels, s = tamanho de stones
- **Espaço:** O(j) — para o hash set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numJewelsInStones(String jewels, String stones) {
    Set<Character> tiposDeJoia = new HashSet<>();
    for (char c : jewels.toCharArray()) {
        tiposDeJoia.add(c);
    }

    int contador = 0;
    for (char pedra : stones.toCharArray()) {
        if (tiposDeJoia.contains(pedra)) {
            contador++;
        }
    }
    return contador;
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

- Esquecer que a comparação é case-sensitive — `'a'` e `'A'` são tipos diferentes; misturar caixa ao construir o set ou ao comparar dá resultado errado.
- Usar `jewels.contains(String.valueOf(pedra))` dentro do loop de `stones` em vez de um `HashSet` — funciona, mas volta para busca linear repetida (O(stones × jewels)) em vez de O(1) por consulta.
- Assumir que `stones` não tem caracteres fora de `jewels` — o problema não garante isso; o contador só deve somar quando há correspondência real.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Case sensitive | `jewels="aA", stones="aAAbbbb"` | 3 | conta 'a' e 'A' como tipos diferentes de joia, ambos presentes |
| Sem correspondência de caixa | `jewels="z", stones="ZZ"` | 0 | 'Z' maiúsculo é diferente de 'z' minúsculo |
| Nenhuma pedra é joia | `jewels="ab", stones="cccc"` | 0 | nenhum caractere de stones está no set |
| Todas as pedras são joias | `jewels="abc", stones="abcabc"` | 6 | todos os caracteres de stones pertencem ao set |

## 🔗 Conexões

- Problemas irmãos: [0217] Contains Duplicate (mesmo uso básico de HashSet para consulta O(1)), [0349] Intersection of Two Arrays (mesma ideia de "quais elementos de uma coleção pertencem a outra")
- No backend: filtragem rápida de itens contra uma lista de permissões/categorias (ex.: verificar quantos itens de um pedido pertencem a uma categoria promocional), sempre que a checagem de pertencimento precisa ser O(1) em vez de busca linear repetida.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
