# [0001] Two Sum

> 🔗 [LeetCode 1](https://leetcode.com/problems/two-sum/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-24 · Revisões: —

Tags: `#ArraysEHashing` `#Complemento` `#Easy`

## 📜 O Problema

Dado um array de inteiros `nums` e um inteiro `target`, retorne os **índices** dos dois números que somam exatamente `target`. Cada input tem **exatamente uma solução**, e você não pode usar o mesmo elemento duas vezes. A resposta pode vir em qualquer ordem.

**Exemplos:**
```
Input:  nums = [2,7,11,15], target = 9    Output: [0,1]   Explicação: nums[0] + nums[1] = 2 + 7 = 9
Input:  nums = [3,2,4], target = 6        Output: [1,2]
Input:  nums = [3,3], target = 6          Output: [0,1]
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 10^4` → O(n²) (10^8 operações) passaria no limite, mas é apertado; o enunciado já sugere no follow-up que existe algo melhor que O(n²)
- `-10^9 <= nums[i], target <= 10^9` → os valores cabem em `int` de 32 bits, mas a **soma de dois** (`nums[i] + nums[j]`) pode chegar a `2×10^9`, que estoura `int` em Java — cuidado ao comparar, prefira comparar por subtração (`target - nums[i]`) em vez de somar dois valores extremos
- "exatamente uma solução" → não precisa tratar empate/múltiplas respostas, simplifica a lógica de parada (pode retornar assim que achar o primeiro par)
- "não pode usar o mesmo elemento duas vezes" → `nums = [3,3]` funciona porque são dois **elementos distintos** com o mesmo valor, não o mesmo índice reutilizado
- Follow-up "menos que O(n²)" → é o convite explícito para trocar busca aninhada por hash map

## 🧭 Como reconhecer o padrão

"Encontre **dois** elementos que somam/combinam para um valor" é o caso canônico de troca de loop aninhado por hash map: para cada elemento, a pergunta "existe o complemento que falta?" vira uma busca O(1) em vez de um segundo `for`. Ver [fundamentos](../../../fundamentos/01_arrays_e_hashing.md), seção "chave-nº-1: elimine o loop interno com hash map".

## 🐢 Solução 1 — Força bruta

Para cada par `(i, j)` com `i < j`, testa se `nums[i] + nums[j] == target`. Dois loops aninhados.

- Tempo: O(n²) · Espaço: O(1)
- **Por que não basta:** o enunciado pede explicitamente algo melhor que O(n²) no follow-up. Além disso, a força bruta refaz o mesmo trabalho: para descobrir se existe um complemento de `nums[i]`, ela varre o array inteiro de novo, em vez de "lembrar" o que já viu.

## 💡 Solução 2 — A ideia otimizada (intuição)

Em vez de perguntar "existe algum `j` tal que `nums[i] + nums[j] == target`?" varrendo tudo de novo, vire a pergunta ao contrário: "**eu já vi** o número `target - nums[i]`?" Um hash map guarda **todo número já percorrido → seu índice**. Assim, a busca pelo complemento vira O(1) em vez de O(n).

Passa pelo array **uma única vez**: para cada `nums[i]`, primeiro checa se o complemento já está no mapa (não conta o próprio elemento contra si mesmo); se não estiver, guarda `nums[i]` no mapa e segue.

## 🎬 Exemplo passo a passo

`nums = [2, 7, 11, 15]`, `target = 9`

| Passo | i | nums[i] | complemento (target - nums[i]) | está no mapa? | Ação | mapa após |
|---|---|---|---|---|---|---|
| 1 | 0 | 2 | 7 | não | guarda 2 | `{2: 0}` |
| 2 | 1 | 7 | 2 | **sim** (índice 0) | retorna `[0, 1]` | — |

Resultado final: `[0, 1]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — um único passe pelo array, cada busca/inserção no hash map é O(1) em média
- **Espaço:** O(n) — no pior caso, guarda quase todos os elementos no mapa antes de achar o par

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] twoSum(int[] nums, int target) {
    // valor -> índice onde ele apareceu. Guardamos o que JÁ vimos,
    // nunca o elemento atual antes de checar o complemento dele.
    Map<Integer, Integer> vistos = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
        // Comparação por subtração, não soma: evita risco de overflow
        // se nums[i] e um valor futuro fossem ambos próximos do limite de int.
        int complemento = target - nums[i];

        if (vistos.containsKey(complemento)) {
            // Achou: o complemento já foi visto ANTES de i, então
            // nunca reutiliza o próprio índice i como par de si mesmo.
            return new int[] { vistos.get(complemento), i };
        }

        // Só guarda nums[i] DEPOIS de checar — garante que o par
        // encontrado usa dois índices distintos, mesmo com valores iguais
        // (ex.: nums = [3,3]: no i=1, o complemento 3 já está no mapa do i=0).
        vistos.put(nums[i], i);
    }

    // Inalcançável dado o enunciado ("exatamente uma solução" garantida),
    // mas o Java exige um retorno em todo caminho do método.
    throw new IllegalArgumentException("Nenhum par encontrado");
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

- **Guardar `nums[i]` no mapa antes de checar o complemento**: quebra o caso onde o próprio elemento seria seu "complemento" por engano (ex.: `nums = [3,5]`, `target = 6` não deveria casar o 3 consigo mesmo — mas isso só vira bug real quando o mesmo valor aparece em pares tipo `target = nums[i]*2`; ainda assim, checar antes de inserir é o hábito correto sempre).
- **Somar os dois extremos em vez de subtrair**: com valores próximos de `±10^9`, somar `nums[i] + nums[j]` diretamente para comparar pode estourar `int` em Java/C++; comparar via `target - nums[i]` evita a soma perigosa.
- **Usar valor como índice, ou vice-versa, na resposta final**: o retorno são **índices**, não os valores — fácil trocar sob pressão de entrevista.
- **Assumir array ordenado**: como o array **não está ordenado**, não dá para usar two pointers diretamente sem antes ordenar (e ordenar destruiria os índices originais, exigindo guardá-los à parte — mais trabalho que o hash map).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo básico | `nums=[2,7,11,15], target=9` | `[0,1]` | caso feliz do enunciado |
| Valores repetidos | `nums=[3,3], target=6` | `[0,1]` | mesmo valor, índices distintos — testa a ordem "checa antes de inserir" |
| Par no fim do array | `nums=[3,2,4], target=6` | `[1,2]` | força o hash map a guardar mais de um valor antes de achar |
| Números negativos | `nums=[-3,4,3,90], target=0` | `[0,2]` | complemento negativo, testa que a subtração funciona com sinais |
| Menor array possível | `nums=[1,2], target=3` | `[0,1]` | borda mínima (`n=2`) |

## 🔗 Conexões

- Problemas irmãos: **[0015] 3Sum** (mesma ideia de complemento, uma dimensão a mais, geralmente resolvido com two pointers após ordenar), **[0167] Two Sum II - Input Array Is Sorted** (mesmo problema, mas array ordenado permite two pointers em vez de hash map), **[0454] 4Sum II** (complemento entre quatro arrays usando hash map)
- No backend: "existe o complemento que eu preciso?" é o mesmo raciocínio de checar rapidamente se uma chave já existe num cache (Redis, `HashMap` em memória) antes de fazer uma segunda consulta cara — trocar uma varredura O(n) por uma busca O(1) é a otimização mais comum em código de produção que processa listas.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
