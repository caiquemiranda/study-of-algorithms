# [0027] Remove Element

> 🔗 [LeetCode 27](https://leetcode.com/problems/remove-element/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums` e um inteiro `val`, remova **in-place** todas as ocorrências de `val`. A ordem dos elementos pode mudar. Retorne `k`, a quantidade de elementos que **não** são iguais a `val`; os primeiros `k` elementos de `nums` devem conter esses valores (em qualquer ordem), e o que estiver depois de `k - 1` não importa.

**Exemplos:**
```
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
```

**Restrições (e o que elas denunciam):**
- `0 <= nums.length <= 100` → inclui array **vazio**, caso de borda que o loop precisa aguentar sem checagem extra
- `0 <= nums[i], val <= 100` → intervalo pequeno, não abre atalho por contagem, pois a ordem dos elementos mantidos pode ser qualquer uma
- Julgamento customizado lê `nums` diretamente após a chamada → exige alteração **in-place**, sem array auxiliar

## 🧭 Como reconhecer o padrão

"Filtrar um array in-place, sem se importar com a ordem final" é resolvido com dois ponteiros andando na mesma direção: um ponteiro de **leitura** (`i`) visita cada posição, e um ponteiro de **escrita** (`k`) marca onde o próximo valor válido deve ser gravado. Diferente do LC 26, aqui o array **não precisa estar ordenado** — a decisão de manter ou não um valor depende só de ele ser igual a `val`, não de comparação com o vizinho.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Construir uma lista nova só com os elementos diferentes de `val`, e depois copiar essa lista de volta para `nums`.

- Tempo: O(n) · Espaço: O(n) — a lista auxiliar guarda até n elementos
- **Por que não basta:** o judge confere `nums` diretamente após a chamada, exigindo modificação in-place; uma estrutura auxiliar de tamanho O(n) viola essa exigência mesmo com tempo já linear.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um ponteiro `k` começando em 0. Percorra o array com um ponteiro `i`: sempre que `nums[i] != val`, esse valor é "válido" — copie-o para `nums[k]` e avance `k`. Quando `nums[i] == val`, simplesmente ignore (não avança `k`, deixando esse valor ser sobrescrito depois). Ao final, `k` é a resposta.

## 🎬 Exemplo passo a passo

`nums = [0,1,2,2,3,0,4,2]`, `val = 2`, `k` começa em 0

| Passo | i | nums[i] | == val? | Ação | k depois |
|---|---|---|---|---|---|
| 1 | 0 | 0 | não | nums[0]=0 (sem mudança) | 1 |
| 2 | 1 | 1 | não | nums[1]=1 (sem mudança) | 2 |
| 3 | 2 | 2 | sim | ignora | 2 |
| 4 | 3 | 2 | sim | ignora | 2 |
| 5 | 4 | 3 | não | nums[2]=3 | 3 |
| 6 | 5 | 0 | não | nums[3]=0 | 4 |
| 7 | 6 | 4 | não | nums[4]=4 | 5 |
| 8 | 7 | 2 | sim | ignora | 5 |

Array final (primeiros k): `[0,1,3,0,4]` — mesmo multiconjunto de `{0,0,1,3,4}` do enunciado, `k = 5` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada ponteiro percorre o array uma única vez
- **Espaço:** O(1) — só duas variáveis inteiras, modificação in-place

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int removeElement(int[] nums, int val) {
    int k = 0; // ponteiro de escrita: próxima posição livre para um valor válido

    for (int i = 0; i < nums.length; i++) {
        // como a ordem final não importa, basta comparar com "val" direto,
        // sem depender de o array estar ordenado (diferente do LC 26)
        if (nums[i] != val) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
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

- Tentar reaproveitar a lógica do LC 26 (comparar com o vizinho/último único) — aqui o critério é comparar com `val`, um valor fixo, não com o elemento anterior; o array nem precisa estar ordenado.
- Usar `i` e `k` como se fossem sempre a mesma posição — nas primeiras iterações eles coincidem (por isso "sem mudança"), mas divergem assim que o primeiro `val` é encontrado; é aí que a escrita em `nums[k]` passa a sobrescrever de fato.
- Não tratar `nums.length == 0` — a constraint permite array vazio; o loop `for` simplesmente não executa e `k` retorna 0 corretamente, mas vale checar mentalmente esse caso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Array vazio | `nums = []`, `val = 1` | k=0 | loop não executa, `k` permanece 0 |
| Todos iguais a val | `nums = [2,2,2]`, `val = 2` | k=0 | `i` nunca avança `k`, todos são ignorados |
| Nenhum igual a val | `nums = [1,3,5]`, `val = 2` | k=3, `[1,3,5]` | `k` avança em todo passo, array não muda |
| Exemplo do enunciado | `nums = [3,2,2,3]`, `val = 3` | k=2, `[2,2,_,_]` | caso padrão com valor repetido nas pontas |

## 🔗 Conexões

- Problemas irmãos: [0026] Remove Duplicates from Sorted Array (mesmo padrão leitura/escrita, mas depende de o array estar ordenado), [0283] Move Zeroes (mesma técnica de "compactar mantendo só o que interessa", aqui filtrando por valor)
- No backend: filtrar registros de uma lista em memória sem alocar buffer novo (ex.: remover entradas marcadas como "deletadas" de um array antes de persistir), processando tudo em uma única passada in-place.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
