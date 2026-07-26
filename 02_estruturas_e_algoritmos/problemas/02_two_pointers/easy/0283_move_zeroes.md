# [0283] Move Zeroes

> 🔗 [LeetCode 283](https://leetcode.com/problems/move-zeroes/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums`, mova todos os `0`s para o final, mantendo a **ordem relativa** dos elementos não-zero. A modificação deve ser **in-place**, sem copiar o array.

**Exemplos:**
```
Input:  nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input:  nums = [0]
Output: [0]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → O(n) esperado
- `-2^31 <= nums[i] <= 2^31 - 1` → inclui negativos; não dá pra usar "valor mínimo" como sentinela
- Exige modificação **in-place**, sem cópia → proíbe montar um array novo com os não-zero na frente
- Follow-up pede minimizar o número de operações → sugere que existe uma versão com menos escritas do que "sobrescrever tudo e depois zerar o resto"

## 🧭 Como reconhecer o padrão

"Empurrar um grupo de elementos pra um lado, mantendo a ordem dos demais, in-place" é resolvido com um ponteiro **lento** marcando a próxima posição livre para um valor não-zero, e um ponteiro **rápido** percorrendo o array — a diferença para [0027] Remove Element é que aqui, em vez de simplesmente descartar o valor "errado" (o zero), ele precisa ser **empurrado** para o final, o que é feito com **troca (swap)** em vez de sobrescrita simples.

## 🐢 Solução 1 — Força bruta (duas passadas)

Primeira passada: copiar (sobrescrever) todos os valores não-zero para o início do array, contando quantos são (`k`), igual ao LC 27. Segunda passada: preencher todas as posições de `k` até o fim com `0`.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** já é O(n) em tempo e O(1) em espaço, mas faz até **duas passadas de escrita** — sobrescreve valores não-zero mesmo quando já estão na posição certa, e ainda escreve `0` em toda posição restante. O follow-up pede minimizar o número de operações; a versão com `swap` faz isso numa passada só.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um ponteiro `lento` marcando a próxima posição onde um valor não-zero deve ficar. Percorra o array com um ponteiro `rápido`; toda vez que `nums[rápido] != 0`, **troque** `nums[lento]` com `nums[rápido]` e avance `lento`. A troca (em vez de cópia simples) garante que o zero que estava em `lento` seja empurrado para a posição de `rápido`, resolvendo "mover os zeros" como efeito colateral — sem precisar de uma segunda passada só para preenchê-los.

## 🎬 Exemplo passo a passo

`nums = [0,1,0,3,12]`, `lento` começa em 0

| Passo | rápido | nums[rápido] | Ação | Array depois |
|---|---|---|---|---|
| 1 | 0 | 0 | zero, ignora | `[0,1,0,3,12]` |
| 2 | 1 | 1 | troca(lento=0, rápido=1) → lento=1 | `[1,0,0,3,12]` |
| 3 | 2 | 0 | zero, ignora | `[1,0,0,3,12]` |
| 4 | 3 | 3 | troca(lento=1, rápido=3) → lento=2 | `[1,3,0,0,12]` |
| 5 | 4 | 12 | troca(lento=2, rápido=4) → lento=3 | `[1,3,12,0,0]` |

Resultado final: `[1,3,12,0,0]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada, cada troca é O(1)
- **Espaço:** O(1) — só os índices `lento` e `rápido`, mais uma variável temporária pra troca

## 💻 Implementações

### Java (referência completa e comentada)
```java
public void moveZeroes(int[] nums) {
    int lento = 0; // próxima posição onde um valor não-zero deve ficar

    for (int rapido = 0; rapido < nums.length; rapido++) {
        if (nums[rapido] != 0) {
            // troca em vez de sobrescrever: empurra o zero pra frente
            // como efeito colateral, sem precisar de um segundo passe
            int tmp = nums[lento];
            nums[lento] = nums[rapido];
            nums[rapido] = tmp;
            lento++;
        }
    }
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

- Usar sobrescrita simples (`nums[lento] = nums[rapido]`) e depois um segundo loop para zerar o resto — funciona, mas conta como duas passadas de escrita; o follow-up (minimizar operações) pede exatamente a versão com `swap`.
- Achar que precisa de uma checagem especial para o caso `lento == rapido` — não precisa: trocar um valor com ele mesmo é um no-op inofensivo.
- Pensar que a ordem relativa dos não-zero pode ser perdida com o swap — não é: `lento` nunca "pula na frente" de um valor não-zero ainda não visto, então a ordem entre eles é preservada.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Zero único | `[0]` | `[0]` | array de tamanho 1, nenhuma troca acontece |
| Sem zeros | `[1,2,3]` | `[1,2,3]` | `lento` sempre igual a `rápido`, trocas são no-op |
| Todos zeros | `[0,0,0]` | `[0,0,0]` | nenhum swap ocorre, `lento` nunca avança |
| Exemplo do enunciado | `[0,1,0,3,12]` | `[1,3,12,0,0]` | caso padrão com zeros intercalados |

## 🔗 Conexões

- Problemas irmãos: [0027] Remove Element (mesmo padrão lento/rápido, mas descarta o valor em vez de empurrá-lo pro fim), [0026] Remove Duplicates from Sorted Array (mesma família de reescrita in-place com dois ponteiros)
- No backend: reorganizar uma coleção in-place agrupando registros "vazios"/inválidos no final (ex.: compactar um buffer removendo entradas invalidadas), sem alocar estrutura nova e preservando a ordem dos registros válidos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
