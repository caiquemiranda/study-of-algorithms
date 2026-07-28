# [0503] Next Greater Element II

> 🔗 [LeetCode 503](https://leetcode.com/problems/next-greater-element-ii/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Array`

## 📜 O Problema

Dado um array circular de inteiros `nums` (ou seja, o próximo elemento de `nums[nums.length-1]` é `nums[0]`), retorne o **próximo elemento maior** para cada elemento de `nums`. O próximo maior de `x` é o primeiro elemento maior encontrado seguindo a ordem do array, buscando **circularmente** se necessário. Se não existir, retorne `-1` para esse elemento.

**Exemplos:**
```
Input:  nums = [1,2,1]
Output: [2,-1,2]
Explicação:
- O primeiro 1 tem próximo maior 2.
- O 2 não encontra um maior (nem circularmente).
- O segundo 1 precisa buscar circularmente, também encontra 2.

Input:  nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 10^4` → precisa de solução O(n); a busca circular ingênua para cada elemento seria O(n²)
- `-10^9 <= nums[i] <= 10^9` → valores grandes, mas sem impacto na técnica, só descarta truques de soma/produto

## 🧭 Como reconhecer o padrão

É a mesma técnica de [0496] Next Greater Element I (monotonic stack), com uma variação: a busca é **circular**. A sacada para lidar com a circularidade sem duplicar o array fisicamente é percorrer os índices **duas vezes** (de `0` a `2n-1`, usando `i % n` para mapear de volta ao índice real) — isso simula "dar a volta" no array uma vez, permitindo que qualquer elemento "veja" até quase todos os outros, incluindo os que vêm antes dele na ordem original.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i`, percorrer circularmente a partir de `i+1` (voltando ao início se ultrapassar o fim) até encontrar um valor maior que `nums[i]`, limitando a busca a no máximo `n-1` passos para não entrar em loop infinito.

- Tempo: O(n²) · Espaço: O(n) para a resposta
- **Por que não basta:** para cada elemento, a busca pode percorrer quase o array inteiro de novo, sem aproveitar nada do trabalho já feito para elementos processados anteriormente. Para `n=10^4`, isso já é 10^8 operações — arriscado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Simule a circularidade percorrendo os índices de `0` até `2n-1`, sempre usando `nums[i % n]` para acessar o valor real. Mantenha uma pilha monotônica decrescente de **índices reais** (`i % n`). Durante toda a passada (incluindo a segunda "volta"): enquanto o topo da pilha apontar para um valor menor que o atual, esse topo acabou de encontrar seu próximo maior — desempilhe e registre a resposta. Só **empilhe** novos índices durante a **primeira** volta (`i < n`) — a segunda volta serve só para resolver pendências antigas, não para introduzir novos candidatos (isso evitaria resolver o mesmo elemento duas vezes ou criar ciclos).

## 🎬 Exemplo passo a passo

`nums = [1,2,1]` (n=3), percorrendo i de 0 a 5, usando `nums[i % 3]`

| Passo | i | i%3 | valor | Ação do while (desempilha menores) | Pilha (índices) após | Empilha? (i<n) |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1 | pilha vazia | `[0]` | sim |
| 2 | 1 | 1 | 2 | 1 < 2 → pop idx 0, res[0]=2 | `[1]` | sim |
| 3 | 2 | 2 | 1 | 1 não < 2 (topo aponta valor 2), para | `[1, 2]` | sim |
| 4 | 3 | 0 | 1 | 1 não < 1 (topo aponta valor 1 do idx 2), para | `[1, 2]` | não (i=3 ≥ n) |
| 5 | 4 | 1 | 2 | 1(idx2) < 2 → pop idx2, res[2]=2 | `[1]` | não |
| 6 | 5 | 2 | 1 | 2(idx1) não < 1, para | `[1]` | não |

Sobrou índice 1 na pilha → `res[1] = -1` (nunca encontrou).

Resultado final: `[2, -1, 2]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — a passada é de tamanho `2n`, e cada índice real é empilhado no máximo uma vez (só na primeira volta) e desempilhado no máximo uma vez
- **Espaço:** O(n) — a pilha e o array de resposta têm tamanho proporcional a `n`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] nextGreaterElements(int[] nums) {
    int n = nums.length;
    int[] resposta = new int[n];
    Arrays.fill(resposta, -1); // default: nenhum próximo maior encontrado
    Deque<Integer> pilha = new ArrayDeque<>(); // índices reais, valores decrescentes

    for (int i = 0; i < 2 * n; i++) {
        int idxReal = i % n; // simula a circularidade sem duplicar o array
        while (!pilha.isEmpty() && nums[pilha.peek()] < nums[idxReal]) {
            resposta[pilha.pop()] = nums[idxReal];
        }
        if (i < n) {
            pilha.push(idxReal); // só introduz novos candidatos na primeira volta
        }
    }

    return resposta;
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

- Empilhar índices também na segunda volta (`i >= n`) — isso reintroduziria os mesmos elementos como candidatos, potencialmente causando resultados incorretos ou um número de operações maior que o necessário; a segunda volta deve **só resolver**, nunca **adicionar**.
- Esquecer o `% n` ao acessar `nums` ou ao empilhar/desempilhar — o índice de iteração `i` vai até `2n-1`, mas o índice **real** no array (para leitura de valor e para gravar a resposta) sempre precisa do módulo.
- Usar valores em vez de índices na pilha — como a resposta precisa ser gravada na posição `resposta[idx]`, é necessário saber o índice, não só o valor (mesmo que os valores não sejam garantidamente únicos aqui, ao contrário do 496).
- Achar que basta duplicar fisicamente o array (`nums + nums`) — funciona, mas gasta O(n) de espaço extra desnecessário; simular a circularidade com `% n` evita essa cópia.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Precisa buscar circularmente | `[1,2,1]` | `[2,-1,2]` | o último elemento só encontra seu maior "dando a volta" |
| Nenhum elemento encontra maior | `[5,4,3,2,1]` | `[-1,-1,-1,-1,-1]` | array estritamente decrescente, nem circularmente há maior |
| Valores repetidos no array | `[1,2,3,4,3]` | `[2,3,4,-1,4]` | o "3" duplicado no fim encontra seu próprio maior corretamente |
| Um único elemento | `[1]` | `[-1]` | sem ninguém mais no array, nem circularmente há candidato |

## 🔗 Conexões

- Problemas irmãos: [0496] Next Greater Element I (mesma técnica, mas sem circularidade e com consulta via mapa), [0739] Daily Temperatures (monotonic stack retornando distância em vez do valor)
- No backend: a técnica de "simular circularidade com módulo em vez de duplicar dados" aparece em processamento de buffers circulares (ring buffers) usados em filas de mensagens e em janelas deslizantes sobre dados cíclicos, como análise de padrões em séries temporais que se repetem periodicamente (ex.: tráfego por hora do dia).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
