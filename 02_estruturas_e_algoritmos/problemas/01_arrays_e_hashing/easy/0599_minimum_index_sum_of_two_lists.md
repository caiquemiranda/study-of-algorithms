# [0599] Minimum Index Sum of Two Lists

> 🔗 [LeetCode 599](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#String` `#Easy`

## 📜 O Problema

Dados dois arrays de strings `list1` e `list2`, encontre as **strings comuns com a menor soma de índices**.

Uma **string comum** é uma string que aparece em ambas as listas. Uma **string comum com a menor soma de índices** é uma string comum tal que, se ela aparece em `list1[i]` e `list2[j]`, então `i + j` deve ser o menor valor entre todas as outras strings comuns.

Retorne **todas as strings comuns com a menor soma de índices**, em qualquer ordem.

**Exemplos:**
```
Input:  list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]

Input:  list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explicação: soma de índices = (0 + 1) = 1.

Input:  list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explicação: "happy" soma 1, "sad" soma 1, "good" soma 4. As duas com soma mínima empatam.
```

**Restrições (e o que elas denunciam):**
- `1 <= list1.length, list2.length <= 1000` → força bruta O(n·m) = até 10^6, ainda passa, mas hash map O(n+m) é bem mais direto
- todas as strings de cada lista são **únicas** dentro dela mesma → não precisa se preocupar com duplicatas dentro da mesma lista
- garantido que existe pelo menos uma string comum → não precisa tratar "sem resposta"

## 🧭 Como reconhecer o padrão

"Encontrar elementos comuns entre duas coleções, com algum critério de otimização" é sempre resolvido guardando um índice num hash map (`valor → posição`) para uma das listas, e depois consultando esse mapa em O(1) enquanto percorre a outra.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada string de `list1`, procurar essa mesma string em `list2` com um laço interno, calculando a soma de índices quando encontrar.

- Tempo: O(n × m) — busca linear de cada string de `list1` dentro de `list2` · Espaço: O(1) extra
- **Por que não basta:** repete a busca "onde está esta string em list2" para cada item de list1, quando um mapa pré-computado responde isso em O(1).

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um mapa `string → índice` a partir de `list1`. Percorra `list2`, e para cada string presente no mapa, calcule `i + j`; mantenha a lista de strings com a menor soma vista até agora (reiniciando a lista se encontrar uma soma menor, ou adicionando se empatar com a menor soma atual).

## 🎬 Exemplo passo a passo

`list1 = ["Shogun","Tapioca Express","Burger King","KFC"]`, `list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]`

Mapa de `list1`: `{Shogun:0, "Tapioca Express":1, "Burger King":2, KFC:3}`

| Passo | j | list2[j] | está no mapa? | i (de list1) | soma i+j | melhorSoma | resultado |
|---|---|---|---|---|---|---|---|
| 1 | 0 | Piatti | não | — | — | ∞ | [] |
| 2 | 1 | The Grill... | não | — | — | ∞ | [] |
| 3 | 2 | Hungry Hunter... | não | — | — | ∞ | [] |
| 4 | 3 | Shogun | sim | 0 | 3 | 3 (melhorou) | [Shogun] |

Resultado final: `["Shogun"]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — construir o mapa (n) + uma passada em list2 (m)
- **Espaço:** O(n) — para o mapa de `list1`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String[] findRestaurant(String[] list1, String[] list2) {
    Map<String, Integer> indiceEmList1 = new HashMap<>();
    for (int i = 0; i < list1.length; i++) {
        indiceEmList1.put(list1[i], i);
    }

    List<String> melhores = new ArrayList<>();
    int melhorSoma = Integer.MAX_VALUE;

    for (int j = 0; j < list2.length; j++) {
        Integer i = indiceEmList1.get(list2[j]);
        if (i == null) {
            continue; // não é uma string comum
        }
        int soma = i + j;
        if (soma < melhorSoma) {
            melhorSoma = soma;
            melhores.clear();      // achou uma soma melhor, descarta os candidatos anteriores
            melhores.add(list2[j]);
        } else if (soma == melhorSoma) {
            melhores.add(list2[j]); // empate na melhor soma, mantém ambos
        }
    }
    return melhores.toArray(new String[0]);
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

- Esquecer de tratar o caso de empate (`soma == melhorSoma`) — o enunciado pede TODAS as strings com a soma mínima, não só a primeira encontrada.
- Não limpar a lista `melhores` ao encontrar uma soma estritamente menor — sem o `clear()`, candidatos de somas piores ficariam misturados com o resultado final.
- Percorrer `list2` procurando em `list1` com `indexOf` (busca linear) em vez de usar o hash map — funciona, mas volta para O(n×m).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Única string comum | `list1=["Shogun","Tapioca Express","Burger King","KFC"], list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]` | `["Shogun"]` | só há uma coincidência possível |
| Empate na soma mínima | `list1=["happy","sad","good"], list2=["sad","happy","good"]` | `["sad","happy"]` (ordem qualquer) | duas strings empatam com soma 1 |
| Mesmo índice nas duas listas | `list1=["a","b"], list2=["a","b"]` | `["a"]` | soma 0 é a menor possível, só "a" bate no índice 0 |
| Uma única entrada em cada lista | `list1=["KFC"], list2=["KFC"]` | `["KFC"]` | caso mínimo trivial |

## 🔗 Conexões

- Problemas irmãos: [0349] Intersection of Two Arrays (interseção básica com hash set), [0350] Intersection of Two Arrays II (interseção com contagem de frequência)
- No backend: sistemas de recomendação que cruzam duas listas de preferências (ex.: restaurantes favoritos de dois usuários) buscando a melhor coincidência por algum critério de prioridade/rank combinado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
