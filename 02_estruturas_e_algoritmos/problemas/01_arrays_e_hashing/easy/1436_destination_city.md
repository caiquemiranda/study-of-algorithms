# [1436] Destination City

> 🔗 [LeetCode 1436](https://leetcode.com/problems/destination-city/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#String` `#Easy`

## 📜 O Problema

Você recebe o array `paths`, onde `paths[i] = [cityAi, cityBi]` significa que existe um caminho direto de `cityAi` para `cityBi`. Retorne a cidade de destino, ou seja, a cidade sem nenhum caminho de saída para outra cidade.

É garantido que o grafo de caminhos forma uma linha sem nenhum ciclo, portanto existirá exatamente uma cidade de destino.

**Exemplos:**
```
Input:  paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explicação: começando em "London" você chega em "Sao Paulo", a cidade de destino. A viagem é:
"London" -> "New York" -> "Lima" -> "Sao Paulo".

Input:  paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"

Input:  paths = [["A","Z"]]
Output: "Z"
```

**Restrições (e o que elas denunciam):**
- `1 <= paths.length <= 100` → pequeno, O(n) resolve com folga
- garantido que os caminhos formam uma LINHA (sem ciclos) → existe exatamente uma cidade de destino, sem ambiguidade
- nomes de cidades podem ter espaços → comparação de string padrão já lida com isso naturalmente

## 🧭 Como reconhecer o padrão

"Encontre o nó final de uma cadeia linear de conexões" é resolvido sem precisar de um grafo de verdade (BFS/DFS): basta colocar todas as cidades de PARTIDA num hash set, e a cidade de destino é a única cidade que aparece como CHEGADA em algum caminho mas nunca aparece como PARTIDA em nenhum outro.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada cidade que aparece como destino em algum caminho, verificar se ela aparece como origem em ALGUM outro caminho, percorrendo a lista inteira de `paths` a cada checagem.

- Tempo: O(n²) — para cada destino candidato, uma varredura completa de `paths` · Espaço: O(1) extra
- **Por que não basta:** repete a busca "esta cidade é origem de algum caminho?" várias vezes, quando um hash set de todas as origens responde isso em O(1) por consulta.

## 💡 Solução 2 — A ideia otimizada (intuição)

Construa um hash set com todas as cidades de ORIGEM (`cityA` de cada par). Percorra os pares novamente; a cidade de DESTINO (`cityB`) que NÃO estiver nesse set de origens é a resposta.

## 🎬 Exemplo passo a passo

`paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`

set de origens: `{London, New York, Lima}`

| Passo | par | cityB | está no set de origens? | Ação |
|---|---|---|---|---|
| 1 | [London,New York] | New York | sim | não é a resposta |
| 2 | [New York,Lima] | Lima | sim | não é a resposta |
| 3 | [Lima,Sao Paulo] | Sao Paulo | **não** | é a resposta |

Resultado final: `"Sao Paulo"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para construir o set + uma passada para achar o destino
- **Espaço:** O(n) — para o set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String destCity(List<List<String>> paths) {
    Set<String> origens = new HashSet<>();
    for (List<String> par : paths) {
        origens.add(par.get(0)); // cityA, a origem de cada caminho
    }

    for (List<String> par : paths) {
        String cityB = par.get(1);
        if (!origens.contains(cityB)) {
            return cityB; // esta cidade nunca é origem de nenhum caminho -> é o destino final
        }
    }
    throw new IllegalStateException("nunca deveria chegar aqui, dado que o enunciado garante um destino");
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

- Tentar resolver com BFS/DFS completo, tratando o problema como um grafo genérico — funciona, mas é over-engineering; a garantia de que o grafo é uma LINHA (sem ramificações nem ciclos) permite a solução direta com hash set, sem nenhuma travessia real.
- Esquecer de percorrer TODOS os caminhos para popular o set de origens antes de procurar o destino — se você tentar decidir "é destino?" numa única passada combinada, pode concluir errado antes de ter visto todas as origens possíveis.
- Confundir `cityA` com `cityB` na leitura dos pares — a origem é sempre o primeiro elemento do par (`par.get(0)`), o destino candidato é o segundo (`par.get(1)`).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Cadeia de 3 caminhos | `[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]` | "Sao Paulo" | último elo da cadeia |
| Ordem embaralhada | `[["B","C"],["D","B"],["C","A"]]` | "A" | a ordem dos pares na lista não importa, só a estrutura da cadeia |
| Um único caminho | `[["A","Z"]]` | "Z" | caso mínimo, cadeia de 1 elo |
| Cidade com espaço no nome | `[["San Francisco","Sao Paulo"]]` | "Sao Paulo" | nomes com espaço são tratados como strings normais |

## 🔗 Conexões

- Problemas irmãos: [0207] Course Schedule (também modela dependências como grafo, mas exige detecção de ciclo de verdade), [0997] Find the Town Judge (mesma ideia de achar o "nó" com uma propriedade única usando contagem/set em vez de travessia)
- No backend: identificação do "nó final" numa cadeia de processamento ou pipeline de dados (ex.: rastrear a etapa final de um workflow representado como uma sequência de transições entre estados).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
