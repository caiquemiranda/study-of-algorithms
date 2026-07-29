# [1346] Check If N and Its Double Exist

> 🔗 [LeetCode 1346](https://leetcode.com/problems/check-if-n-and-its-double-exist/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#ArraysEHashing` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Dado um array `arr` de inteiros, verifique se existem dois índices **diferentes** `i` e `j` tais que `arr[i] == 2 * arr[j]` (um número é o dobro exato do outro).

**Exemplos:**
```
Input:  arr = [10,2,5,3]    Output: true    (10 == 2*5, com i=0, j=2)
Input:  arr = [3,1,7,11]    Output: false   (nenhum par satisfaz a condição)
```

**Restrições (e o que elas denunciam):**
- `2 <= arr.length <= 500` → array pequeno, força bruta O(n²) já passaria tranquilo, mas o padrão certo é O(n)
- `-10^3 <= arr[i] <= 10^3` → inclui **negativos e zero** — atenção especial ao dobro de zero (`2*0 = 0`, precisa de dois zeros distintos no array) e ao dobro de negativos (`2 * -5 = -10`)
- "existem `i != j`" → precisamos de índices diferentes mesmo que os valores sejam iguais (caso do zero)

## 🧭 Como reconhecer o padrão

"Existe um par onde um elemento é uma função direta do outro (dobro, complemento, soma fixa)" é a assinatura clássica de **hash set com busca de complemento**, igual ao Two Sum: para cada elemento, calcule o valor "parceiro" que resolveria a condição e pergunte a um set se ele já apareceu.

## 🐢 Solução 1 — Força bruta

Para cada par `(i, j)` com `i != j`, verificar se `arr[i] == 2 * arr[j]`.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** mesmo passando dentro do limite de tempo com `n <= 500`, refaz a mesma verificação repetidamente; um hash set resolve com uma única passada, sem comparar todos os pares.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada número `x` do array, ele forma um par válido com outro número já visto se **o dobro dele (`2x`) já apareceu** OU **a metade dele (`x/2`, quando `x` é par) já apareceu**. Guarde os números já processados num hash set e, para cada novo `x`, cheque as duas condições antes de adicionar `x` ao set.

Checar as duas direções (dobro e metade) numa única passada evita ter que decidir de antemão "quem é o maior" — cobre `arr[i] == 2*arr[j]` para qualquer ordem em que `i` e `j` apareçam no array.

## 🎬 Exemplo passo a passo

`arr = [10, 2, 5, 3]`

| Passo | x atual | 2x visto? | x/2 visto? (se x par) | Decisão | seen (depois) |
|---|---|---|---|---|---|
| 1 | 10 | 20 não está em seen (vazio) | 5 não está em seen | segue | `{10}` |
| 2 | 2 | 4 não está em seen | 1 não está em seen | segue | `{10, 2}` |
| 3 | 5 | 10 está em seen! | — | **retorna true** | — |

Resultado final: `true` ✔ (5 é a metade de 10, que já tinha sido visto)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada, com consultas O(1) ao hash set
- **Espaço:** O(n) — o hash set guarda até todos os elementos do array

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean checkIfExist(int[] arr) {
    Set<Integer> visto = new HashSet<>();

    for (int x : arr) {
        // Checa as duas direções: x pode ser o "arr[i]" (dobro de algo já visto)
        // ou o "arr[j]" (algo já visto é o dobro de x).
        if (visto.contains(2 * x) || (x % 2 == 0 && visto.contains(x / 2))) {
            return true;
        }
        visto.add(x);                     // só adiciona DEPOIS de checar, evita usar o próprio x como par dele mesmo
    }
    return false;
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

- **Adicionar `x` ao set antes de checar**: isso permitiria que um número servisse de par dele mesmo indevidamente em alguns casos — a ordem certa é checar primeiro, adicionar depois.
- **Esquecer o caso de dois zeros**: `arr = [0, 0]` deve retornar `true` (`0 == 2*0`, com `i != j`), mas `arr = [0]` sozinho não conta (só um índice). Como o set já teria `0` da primeira ocorrência, checar `2*0=0` na segunda ocorrência funciona corretamente — só falha se você tentar otimizar removendo essa checagem por achar "redundante".
- **`x / 2` com `x` ímpar**: dividir inteiro arredonda errado (`5/2=2`, mas `2*2=4 != 5`) — por isso o `x % 2 == 0` é obrigatório antes de checar a metade.
- **Números negativos**: `2 * -5 = -10` é válido matematicamente; não há necessidade de tratamento especial além de garantir que a aritmética funciona igual para negativos (que funciona nativamente em Java/Python/C++).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Par de zeros | `arr=[0,0]` | true | zero é o dobro de si mesmo, mas precisa de dois índices |
| Zero único | `arr=[0,1]` | false | um só zero não forma par válido |
| Negativos | `arr=[-10,12,-20,-8,15]` | true | -20 é o dobro de -10 (`2 * -10 = -20`), confirma que a aritmética funciona igual com valores negativos |
| Sem par, com negativos e zero | `arr=[-2,0,10,-19,4,6,-8]` | false | nenhum valor é exatamente o dobro de outro presente, mesmo com negativos e zero no meio |
| Sem par | `arr=[3,1,7,11]` | false | nenhuma combinação satisfaz |
| Exemplo do enunciado | `arr=[10,2,5,3]` | true | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0001] Two Sum** (mesmo padrão raiz de complemento via hash set), **[0349] Intersection of Two Arrays** (hash set para consulta O(1) em vez de comparação par a par)
- No backend: detectar relações "um valor é função direta de outro já visto" via set aparece em deduplicação de eventos (ex.: detectar se um evento é um "eco" de outro já processado, aplicando uma transformação conhecida) sem precisar comparar cada novo evento com todo o histórico.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode, referente a ordenar+buscar o dobro/metade), mas a técnica ótima é hash set com checagem de complemento (O(n), sem ordenar), então o documento foi classificado em `01_arrays_e_hashing`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
