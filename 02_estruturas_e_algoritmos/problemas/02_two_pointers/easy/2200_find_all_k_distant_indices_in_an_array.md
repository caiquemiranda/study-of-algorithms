# [2200] Find All K-Distant Indices in an Array

> 🔗 [LeetCode 2200](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums` (0-indexado) e dois inteiros `key` e `k`, um índice `i` é **k-distante** se existe algum índice `j` tal que `|i - j| <= k` e `nums[j] == key`. Retorne a lista de todos os índices k-distantes, em ordem crescente.

**Exemplos:**
```
Input:  nums = [3,4,9,1,3,9,5], key = 9, k = 1
Output: [1,2,3,4,5,6]

Input:  nums = [2,2,2,2,2], key = 2, k = 2
Output: [0,1,2,3,4]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums.length <= 1000`, `1 <= k <= nums.length` → uma solução O(n×k) já passaria, mas O(n) é alcançável
- `key` garantido existir em `nums` → sempre há pelo menos uma ocorrência de referência
- A resposta precisa vir **ordenada crescente** → como percorremos `nums` da esquerda pra direita, a ordem já sai naturalmente correta

## 🧭 Como reconhecer o padrão

"Para cada posição, verificar se existe uma ocorrência de referência dentro de uma distância `k`" é resolvido com dois ponteiros que só avançam: um percorre `nums` normalmente (`i`), o outro percorre a lista de posições onde `key` aparece (`p`) — como ambos são crescentes, `p` nunca precisa voltar, só descarta ocorrências que já ficaram longe demais à esquerda.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada índice `i`, percorrer TODO o array procurando algum `j` com `nums[j] == key` e `|i - j| <= k`.

- Tempo: O(n²) no pior caso — cada `i` pode escanear até `n` posições · Espaço: O(1) além do resultado
- **Por que não basta:** recalcula do zero, para cada `i`, uma busca que já tinha sido parcialmente feita para o `i` anterior; como as posições de `key` são fixas e ordenadas, um ponteiro que só avança resolve tudo numa única passada combinada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, colete todas as posições onde `nums[j] == key` numa lista `keyIdx` (já sai ordenada, pois percorremos `nums` em ordem). Depois, percorra `nums` com `i`, mantendo um ponteiro `p` em `keyIdx`: antes de checar `i`, avance `p` enquanto a ocorrência atual estiver longe demais à esquerda (`keyIdx[p] < i - k`) — ela nunca mais vai servir para nenhum `i` futuro, então pode ser descartada de vez. Se, depois disso, a ocorrência em `keyIdx[p]` ainda estiver dentro do alcance à direita (`keyIdx[p] <= i + k`), `i` é k-distante.

## 🎬 Exemplo passo a passo

`nums = [3,4,9,1,3,9,5]`, `key = 9`, `k = 1` → `keyIdx = [2, 5]`

| Passo | i | p | keyIdx[p] | Ação | Resultado |
|---|---|---|---|---|---|
| 1 | 0 | 0 | 2 | `\|0-2\|=2 > 1` | não adiciona |
| 2 | 1 | 0 | 2 | `\|1-2\|=1 <= 1` | adiciona 1 |
| 3 | 2 | 0 | 2 | `\|2-2\|=0 <= 1` | adiciona 2 |
| 4 | 3 | 0 | 2 | `\|3-2\|=1 <= 1` | adiciona 3 |
| 5 | 4 | 0→1 | 2 ficou longe (`2 < 4-1`) → avança p=1 (keyIdx=5) | `\|4-5\|=1 <= 1` | adiciona 4 |
| 6 | 5 | 1 | 5 | `\|5-5\|=0 <= 1` | adiciona 5 |
| 7 | 6 | 1 | 5 | `\|6-5\|=1 <= 1` | adiciona 6 |

Resultado final: `[1,2,3,4,5,6]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `i` percorre `nums` uma vez, e `p` percorre `keyIdx` no total no máximo uma vez (nunca recua)
- **Espaço:** O(n) para `keyIdx` e o resultado; O(1) de espaço extra além disso

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
    List<Integer> keyIdx = new ArrayList<>();
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] == key) {
            keyIdx.add(j);
        }
    }

    List<Integer> result = new ArrayList<>();
    int p = 0; // ponteiro em keyIdx: só avança, nunca volta
    for (int i = 0; i < nums.length; i++) {
        // descarta ocorrências de key que já ficaram longe demais à esquerda
        while (p < keyIdx.size() && keyIdx.get(p) < i - k) {
            p++;
        }
        if (p < keyIdx.size() && keyIdx.get(p) <= i + k) {
            result.add(i);
        }
    }

    return result;
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

- Reiniciar a busca do zero (ou voltar `p` pra trás) a cada novo `i` — como tanto `i` quanto `keyIdx` são crescentes, o ponteiro `p` NUNCA precisa recuar.
- Confundir a condição de descarte (`keyIdx[p] < i - k`) com a de aceitação (`keyIdx[p] <= i + k`) — a primeira decide se o ponteiro avança (ocorrência ficou pra trás), a segunda se o índice atual entra no resultado.
- Esquecer a checagem `p < keyIdx.size()` antes de acessar `keyIdx.get(p)` — quando todas as ocorrências de `key` já foram "usadas", acessar um índice além do fim da lista quebra o código.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Duas ocorrências separadas | `nums=[3,4,9,1,3,9,5]`, `key=9`, `k=1` | `[1,2,3,4,5,6]` | união dos alcances das duas ocorrências, com sobreposição no meio |
| k cobre tudo | `nums=[2,2,2,2,2]`, `key=2`, `k=2` | `[0,1,2,3,4]` | toda posição tem alguma ocorrência dentro do alcance |
| k pequeno, uma única ocorrência | `nums=[1,2,3,4,5]`, `key=3`, `k=1` | `[1,2,3]` | só os vizinhos imediatos do índice 2 entram |
| Índices isolados fora de alcance | `nums=[9,1,1,1,1]`, `key=9`, `k=1` | `[0,1]` | índices 2,3,4 estão longe demais da única ocorrência (índice 0) |

## 🔗 Conexões

- Problemas irmãos: [0821] Shortest Distance to a Character (mesma família de "calcular alcance/distância até a ocorrência mais próxima de um valor"), [0239] Sliding Window Maximum (mesma técnica de ponteiro que só avança, nunca recua, sobre uma janela)
- No backend: marcar registros "próximos" de um evento de referência dentro de uma janela de tempo/distância — por exemplo, sinalizar todas as métricas coletadas dentro de k minutos de um evento de erro conhecido, aproveitando que tanto os registros quanto os eventos de referência já vêm ordenados no tempo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
