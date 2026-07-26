# [0026] Remove Duplicates from Sorted Array

> 🔗 [LeetCode 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums` ordenado em ordem **não decrescente**, remova as duplicatas **in-place** (sem alocar outro array) de forma que cada elemento único apareça só **uma vez**, mantendo a **ordem relativa** dos elementos.

Considere `k` o número de elementos únicos. Depois de remover as duplicatas, os primeiros `k` elementos de `nums` devem conter os valores únicos em ordem; o que estiver depois do índice `k - 1` pode ser lixo (não importa). A função deve **retornar `k`**.

**Exemplos:**
```
Input:  nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 3 * 10^4` → força bruta O(n²) (comparar cada elemento com todos) estoura; O(n) é esperado
- `-100 <= nums[i] <= 100` → intervalo pequeno, mas isso não abre atalho por contagem porque a ordem relativa importa
- `nums` já vem **ordenado em não decrescente** → é a peça-chave: duplicatas são sempre **vizinhas**, nunca espalhadas pelo array
- Julgamento customizado exige alterar `nums` **in-place** → proíbe alocar um segundo array/lista para montar a resposta

## 🧭 Como reconhecer o padrão

"Array já ordenado + operação in-place O(1) de espaço extra" é a assinatura de dois ponteiros andando na mesma direção: um ponteiro **lento** marca a última posição confirmada como única, e um ponteiro **rápido** varre o array procurando o próximo valor diferente.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Percorrer o array coletando os valores únicos numa lista auxiliar (ou `Set`, já que está ordenado basta comparar com o último inserido) e depois copiar essa lista de volta para `nums`.

- Tempo: O(n) · Espaço: O(n) — a lista auxiliar guarda até n elementos
- **Por que não basta:** o enunciado exige modificação **in-place**, com o custom judge conferindo diretamente o conteúdo de `nums`; alocar uma estrutura auxiliar de tamanho O(n) viola essa exigência mesmo que o tempo já seja linear.

## 💡 Solução 2 — A ideia otimizada (intuição)

Como o array já está ordenado, todo valor duplicado fica **colado** no seu igual. Basta manter um ponteiro `lento` apontando pro fim do trecho já "limpo" (só únicos). Um ponteiro `rapido` percorre o resto do array; toda vez que `nums[rapido]` for **diferente** de `nums[lento]`, é um valor novo — avança `lento` e copia `nums[rapido]` para lá. Valores iguais a `nums[lento]` são simplesmente ignorados (o ponteiro rápido passa por cima).

## 🎬 Exemplo passo a passo

`nums = [0,0,1,1,1,2,2,3,3,4]` (índices 0 a 9), `lento` começa em 0

| Passo | rápido | nums[rápido] | nums[lento] | Igual? | Ação |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | sim | ignora |
| 2 | 2 | 1 | 0 | não | lento=1, nums[1]=1 |
| 3 | 3 | 1 | 1 | sim | ignora |
| 4 | 4 | 1 | 1 | sim | ignora |
| 5 | 5 | 2 | 1 | não | lento=2, nums[2]=2 |
| 6 | 6 | 2 | 2 | sim | ignora |
| 7 | 7 | 3 | 2 | não | lento=3, nums[3]=3 |
| 8 | 8 | 3 | 3 | sim | ignora |
| 9 | 9 | 4 | 3 | não | lento=4, nums[4]=4 |

Array final (primeiros k): `[0,1,2,3,4]`, `k = lento + 1 = 5` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada ponteiro percorre o array uma única vez
- **Espaço:** O(1) — só duas variáveis inteiras, a modificação é in-place

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int removeDuplicates(int[] nums) {
    int lento = 0; // índice do último valor único já confirmado

    for (int rapido = 1; rapido < nums.length; rapido++) {
        // array já ordenado: se é diferente do último único, é um valor novo
        if (nums[rapido] != nums[lento]) {
            lento++;
            nums[lento] = nums[rapido];
        }
        // se for igual, "rapido" simplesmente pula esse valor repetido
    }

    return lento + 1; // k = quantidade de elementos únicos
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

- Retornar `lento` em vez de `lento + 1` — `lento` é um **índice** (base 0), mas `k` é uma **contagem**; esse off-by-one é o erro mais comum do problema.
- Achar que precisa de uma estrutura auxiliar (`Set`, lista) para "não repetir" — o fato de o array já estar ordenado elimina essa necessidade; duplicatas nunca aparecem longe uma da outra.
- Comparar `nums[rapido]` com `nums[rapido - 1]` em vez de `nums[lento]` — funciona por coincidência aqui, mas quebra em variantes como "Remove Duplicates II" (permite até 2 repetições), onde só comparar com o último valor **escrito** (`lento`) dá a resposta certa.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único elemento | `[1]` | k=1, `[1]` | não há duplicata; `lento` nunca avança no loop |
| Todos iguais | `[2,2,2,2]` | k=1, `[2,_,_,_]` | todo o resto é ignorado por `rapido` |
| Sem duplicatas | `[1,2,3]` | k=3, `[1,2,3]` | `lento` avança em todo passo, array não muda |
| Exemplo do enunciado | `[0,0,1,1,1,2,2,3,3,4]` | k=5, `[0,1,2,3,4,...]` | caso com múltiplos grupos de duplicatas |

## 🔗 Conexões

- Problemas irmãos: [0080] Remove Duplicates from Sorted Array II (mesma técnica, mas permite até 2 ocorrências por valor — precisa de um contador junto com os ponteiros), [0283] Move Zeroes (mesmo padrão de ponteiro lento/rápido reescrevendo o array in-place)
- No backend: compactar um stream já ordenado (ex.: eventos de log ordenados por timestamp) removendo entradas repetidas sem alocar um buffer extra, processando o array/stream em uma única passada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
