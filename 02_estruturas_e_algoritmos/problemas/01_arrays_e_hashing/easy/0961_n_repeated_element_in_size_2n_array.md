# [0961] N-Repeated Element in Size 2N Array

> 🔗 [LeetCode 961](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array de inteiros `nums` com as seguintes propriedades:
- `nums.length == 2 * n`
- `nums` contém `n + 1` valores **únicos**, `n` dos quais aparecem **exatamente uma vez** no array
- Exatamente um elemento de `nums` está repetido `n` vezes

Retorne **o elemento que está repetido `n` vezes**.

**Exemplos:**
```
Input:  nums = [1,2,3,3]
Output: 3

Input:  nums = [2,1,2,5,3,2]
Output: 2

Input:  nums = [5,1,5,2,5,3,5,4]
Output: 5
```

**Restrições (e o que elas denunciam):**
- `2 <= n <= 5000`, `nums.length == 2n` → array de tamanho par, precisa O(n)
- `n+1` valores únicos, exatamente um repetido `n` vezes → garante que existe exatamente uma resposta

## 🧭 Como reconhecer o padrão

"Encontre o único elemento repetido" é sempre resolvido com um hash set: percorra o array, e a primeira vez que tentar inserir um valor que já está no set, esse é o elemento repetido — não precisa nem terminar de percorrer o array inteiro.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada elemento, contar quantas vezes ele aparece no array inteiro percorrendo tudo de novo, até achar o que aparece mais de uma vez.

- Tempo: O(n²) — recontagem completa do array para cada elemento candidato · Espaço: O(1) extra
- **Por que não basta:** repete a mesma varredura do array várias vezes quando um hash set decide "já vi este valor?" em O(1) por elemento, numa única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array com um `HashSet`. Para cada valor, tente adicioná-lo ao set; se a inserção falhar (o valor já estava lá), esse é o elemento repetido — retorne na hora, sem precisar terminar a passada.

## 🎬 Exemplo passo a passo

`nums = [2,1,2,5,3,2]`

| Passo | i | valor | já está no set? | Ação |
|---|---|---|---|---|
| 1 | 0 | 2 | não | adiciona {2} |
| 2 | 1 | 1 | não | adiciona {1,2} |
| 3 | 2 | 2 | **sim** | achou o repetido, retorna |

Resultado final: `2` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) no pior caso (frequentemente para antes, já que o valor repetido aparece `n` vezes entre `2n` posições)
- **Espaço:** O(n) no pior caso, para o set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int repeatedNTimes(int[] nums) {
    Set<Integer> vistos = new HashSet<>();
    for (int num : nums) {
        if (!vistos.add(num)) {
            return num; // add() retorna false se o valor já estava no set -> achou o repetido
        }
    }
    throw new IllegalStateException("nunca deveria chegar aqui, dado que o enunciado garante uma resposta");
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

- Continuar percorrendo o array depois de já ter encontrado o elemento repetido — desperdício desnecessário; a garantia do enunciado ("exatamente um elemento repetido n vezes") significa que a primeira repetição encontrada já é a resposta final.
- Usar `contains()` seguido de `add()` como duas operações separadas — funciona, mas `add()` sozinho já retorna `false` quando o elemento já existe, economizando uma consulta extra ao set.
- Achar que precisa contar quantas vezes cada elemento aparece antes de decidir — não precisa; o enunciado garante que só existe UM elemento repetido, então a primeira duplicata encontrada já resolve o problema.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Repetição no final | `[1,2,3,3]` | 3 | menor entrada válida (n=2) |
| Repetição no meio | `[2,1,2,5,3,2]` | 2 | repetição não está nas bordas do array |
| Repetição espalhada | `[5,1,5,2,5,3,5,4]` | 5 | elemento repetido aparece em posições bem distantes |
| Repetição não adjacente | `[2,3,1,3]` | 3 | detecção funciona mesmo sem as duplicatas estarem coladas |

## 🔗 Conexões

- Problemas irmãos: [0217] Contains Duplicate (mesmo uso básico de HashSet para detectar repetição), [0287] Find the Duplicate Number (mesmo objetivo, mas com restrição de espaço O(1) que exige uma técnica diferente)
- No backend: detecção rápida de registros duplicados num lote de dados (ex.: IDs de transação processados duas vezes por engano) — parar assim que a primeira duplicata é encontrada evita processamento desnecessário do restante do lote.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
