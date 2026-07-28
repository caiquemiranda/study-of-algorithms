# [0219] Contains Duplicate II

> 🔗 [LeetCode 219](https://leetcode.com/problems/contains-duplicate-ii/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#HashTable` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums` e um inteiro `k`, retorne `true` se existirem dois índices **distintos** `i` e `j` tais que `nums[i] == nums[j]` e `abs(i - j) <= k`.

**Exemplos:**
```
Input:  nums = [1,2,3,1], k = 3
Output: true

Input:  nums = [1,0,1,1], k = 1
Output: true

Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^5` → O(n²) comparando todos os pares estoura; a solução esperada é O(n)
- `-10^9 <= nums[i] <= 10^9` → o intervalo de valores é enorme, então não dá pra usar um array de contagem indexado pelo valor; precisa de hash table
- `0 <= k <= 10^5` → `k` pode ser `0` (nenhuma janela útil, resposta sempre `false`) ou até maior que o array inteiro

## 🧭 Como reconhecer o padrão

"Duplicata dentro de uma distância máxima `k` entre índices" é uma janela deslizante de **tamanho fixo**: em vez de comparar todo par de índices, basta manter um conjunto com os últimos `k` valores vistos — se o valor atual já está lá dentro, achou a duplicata; senão, insere e descarta o valor que saiu do alcance.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `i`, olhar todo `j` no intervalo `[i+1, min(i+k, n-1)]` comparando `nums[i] == nums[j]` diretamente.

- Tempo: O(n·k), que no pior caso (`k` próximo de `n`) vira O(n²) · Espaço: O(1)
- **Por que não basta:** recompara elementos que a janela do `i` anterior já tinha processado — nada é reaproveitado entre iterações consecutivas.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha um `HashSet` representando os últimos `k` valores vistos (a "janela" de índices `[i-k, i-1]`). Ao processar `nums[i]`: se o valor já está no set, os dois índices estão a distância `<= k` — retorna `true`. Senão, adiciona `nums[i]` ao set; se o set passar de `k` elementos, remove o valor mais antigo (`nums[i-k]`), porque ele já saiu do alcance permitido.

## 🎬 Exemplo passo a passo

`nums = [1,2,3,1,2,3]`, `k = 2`

| i | nums[i] | window antes | contém? | window depois |
|---|---|---|---|---|
| 0 | 1 | {} | não | {1} |
| 1 | 2 | {1} | não | {1,2} |
| 2 | 3 | {1,2} | não | {2,3} (remove 1) |
| 3 | 1 | {2,3} | não | {3,1} (remove 2) |
| 4 | 2 | {3,1} | não | {1,2} (remove 3) |
| 5 | 3 | {1,2} | não | {2,3} (remove 1) |

Resultado final: `false` ✔ (nenhum valor repetido dentro da distância `k=2`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada elemento entra e sai do set no máximo uma vez
- **Espaço:** O(min(n, k)) — o set nunca guarda mais que `k` elementos

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean containsNearbyDuplicate(int[] nums, int k) {
    Set<Integer> window = new HashSet<>();

    for (int i = 0; i < nums.length; i++) {
        if (window.contains(nums[i])) {
            return true; // achou o mesmo valor dentro da distância k
        }
        window.add(nums[i]);
        if (window.size() > k) {
            window.remove(nums[i - k]); // desliza a janela: remove quem saiu do alcance
        }
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

- Confundir "distância `k`" com "janela de `k+1` elementos" — o set deve guardar apenas os `k` valores **anteriores** ao atual (sem contar o próprio), senão a comparação fica errada.
- `k = 0` é um valor válido nas restrições e a resposta correta é sempre `false` (índices distintos nunca têm distância `<= 0`); o algoritmo já trata isso naturalmente, sem precisar de caso especial.
- Usar uma lista em vez de `HashSet` e fazer `contains` linear: funciona, mas vira O(n·k) no pior caso, perdendo a vantagem do hash.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| k=0 | `nums=[1,1]`, `k=0` | false | distância mínima entre índices distintos é 1, maior que 0 |
| Duplicata na borda exata da janela | `nums=[1,2,1]`, `k=2` | true | `abs(0-2)=2<=2` |
| Duplicata fora da janela | `nums=[1,2,3,1]`, `k=2` | false | `abs(0-3)=3>2` |
| Array sem duplicatas | `nums=[1,2,3,4]`, `k=3` | false | nenhum valor se repete |

## 🔗 Conexões

- Problemas irmãos: [0217] Contains Duplicate (mesma checagem, sem restrição de distância — resolvido só com hashset simples), [0003] Longest Substring Without Repeating Characters (mesma ideia de janela que expulsa elementos antigos ao ultrapassar um limite)
- No backend: detectar eventos duplicados dentro de uma janela de tempo — por exemplo, garantir idempotência descartando uma requisição repetida se um identificador igual já apareceu nos últimos `k` registros processados.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
