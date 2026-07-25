# 02 — Two Pointers

> Dois índices coordenados eliminam o loop aninhado. Soluções em [`../problemas/02_two_pointers/`](../problemas/02_two_pointers/).

## 1. Conceito Central e Analogia Didática

- Dois ponteiros se movem segundo uma **regra de descarte**: cada movimento elimina candidatos com segurança, sem testar todos os pares.
- Só funciona com **monotonicidade**: mover o ponteiro numa direção só melhora (ou só piora) o critério — geralmente porque o array está **ordenado**.
- Três variantes: **pontas opostas** (convergem), **leitor/escritor** (mesma direção), **fast & slow** (velocidades diferentes — ver [06_linked_list](06_linked_list.md)).

**Analogia:** dois seguranças fechando um corredor pelas duas pontas. A cada passo, um deles decide avançar sabendo que ninguém ficou para trás sem ser checado — no fim, se encontraram e o corredor inteiro foi coberto numa única passada.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se o problema dá **array ordenado** e pede "par/tripla com soma X" → pontas opostas.
- Se exige **"in-place, O(1) de espaço extra"** → leitor/escritor.
- Se envolve **palíndromo** ou comparação simétrica → pontas opostas.
- Se pede "remova/compacte elementos mantendo a ordem" → leitor/escritor.
- Se o array não está ordenado e a posição original não importa → **ordene primeiro** e reavalie.

## 3. Templates de Código

### Pontas opostas (par com soma alvo em array ordenado)

```java
// Java — cada comparação descarta uma ponta inteira de candidatos
public int[] parComSoma(int[] nums, int alvo) {
    int esq = 0, dir = nums.length - 1;
    while (esq < dir) {
        int soma = nums[esq] + nums[dir];
        if (soma == alvo) return new int[]{esq, dir};
        if (soma < alvo) esq++;  // soma pequena: só cresce se avançarmos o menor lado
        else dir--;              // soma grande: só diminui se recuarmos o maior lado
    }
    return new int[]{};
}
```

```python
def par_com_soma(nums, alvo):
    esq, dir = 0, len(nums) - 1
    while esq < dir:
        soma = nums[esq] + nums[dir]
        if soma == alvo:
            return [esq, dir]
        if soma < alvo:
            esq += 1             # precisa de soma maior: avança a ponta pequena
        else:
            dir -= 1             # precisa de soma menor: recua a ponta grande
    return []
```

### Leitor/escritor (compactar in-place)

```java
// Java — 'escreve' marca a fronteira do array "limpo"; 'le' varre tudo
public int removeDuplicates(int[] nums) {
    int escreve = 1;                              // posição 0 já é única por definição
    for (int le = 1; le < nums.length; le++) {
        if (nums[le] != nums[escreve - 1]) {      // só copia o que é novo em relação ao último aceito
            nums[escreve++] = nums[le];
        }
    }
    return escreve;                               // novo tamanho lógico do array
}
```

```python
def remove_duplicates(nums):
    escreve = 1
    for le in range(1, len(nums)):
        if nums[le] != nums[escreve - 1]:   # compara com o último ACEITO, não com o vizinho
            nums[escreve] = nums[le]
            escreve += 1
    return escreve
```

## 4. Walkthrough Visual (Teste de Mesa)

`parComSoma(nums=[1, 3, 4, 6, 9], alvo=10)`

| Iteração | esq | dir | nums[esq]+nums[dir] | Decisão |
|---|---|---|---|---|
| 1 | 0 (1) | 4 (9) | 10 | **== alvo → retorna [0, 4]** ✔ |

`parComSoma(nums=[1, 3, 4, 6, 9], alvo=9)`

| Iteração | esq | dir | soma | Decisão |
|---|---|---|---|---|
| 1 | 0 (1) | 4 (9) | 10 | > 9 → `dir--` |
| 2 | 0 (1) | 3 (6) | 7 | < 9 → `esq++` |
| 3 | 1 (3) | 3 (6) | 9 | **== alvo → retorna [1, 3]** ✔ |

## 5. Complexidade (Tempo e Espaço)

| Cenário | Tempo | Espaço |
|---|---|---|
| Array já ordenado | O(n) | O(1) |
| Precisa ordenar antes | O(n log n) | O(1)–O(n) conforme o sort |
| 3Sum (fixa 1 + two pointers) | O(n²) | O(1) |

- O(n) porque **cada ponteiro atravessa o array no máximo uma vez** — nunca voltam.

## 6. Pegadinhas e Erros Comuns

- Aplicar em array **não ordenado**: a regra de descarte perde a garantia e a resposta some silenciosamente.
- `esq < dir` vs `esq <= dir`: pergunte se os ponteiros **podem** apontar para o mesmo elemento; no par com soma, não podem.
- 3Sum sem pular duplicatas (`nums[i] == nums[i-1]`) → triplas repetidas na resposta.
- **Java**: em arrays de `String`, comparar com `==` em vez de `.equals()` no critério do ponteiro.
- **Python**: `dir` sombreia a built-in `dir()` — aceitável em entrevista, evite em produção.
- Não saber **justificar o descarte** em voz alta = o padrão provavelmente não se aplica ao problema.

## 7. Aplicações no Mundo Real (Backend)

- **Merge de arquivos ordenados**: dois cursores avançando é a base do merge externo e da **compactação de SSTables** (LSM — Cassandra/RocksDB).
- **PostgreSQL**: merge join usa exatamente dois cursores em relações ordenadas.
- **Streams**: reconciliação de dois extratos ordenados por data (conciliação bancária) é two pointers puro.
- Leitor/escritor é o padrão de **compactação de buffers** em parsers e protocolos binários.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | 🟢 Easy |
| 167 | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟡 Medium |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 Hard |
