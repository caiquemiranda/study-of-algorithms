# [3206] Alternating Groups I

> 🔗 [LeetCode 3206](https://leetcode.com/problems/alternating-groups-i/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Array` `#Easy`

## 📜 O Problema

Existe um círculo de ladrilhos vermelhos e azuis, representado por um array `colors` onde `colors[i] == 0` significa vermelho e `colors[i] == 1` significa azul. Toda trinca de 3 ladrilhos **contíguos** no círculo com cores **alternadas** (o ladrilho do meio tem cor diferente dos dois vizinhos) é chamada de **grupo alternado**. Retorne o número de grupos alternados. Como `colors` representa um círculo, o primeiro e o último ladrilho são considerados vizinhos.

**Exemplos:**
```
Input:  colors = [1,1,1]
Output: 0

Input:  colors = [0,1,0,0,1]
Output: 3
```

**Restrições (e o que elas denunciam):**
- `3 <= colors.length <= 100` → entrada pequena, O(n) já é folgado
- `0 <= colors[i] <= 1` → só duas cores possíveis, simplifica a checagem de alternância
- É um **círculo** → o primeiro e o último elemento são vizinhos, exigindo aritmética modular nos índices

## 🧭 Como reconhecer o padrão

"Trincas de 3 elementos **contíguos** num array circular satisfazendo uma condição local" é janela deslizante de tamanho **fixo** 3: percorre-se cada posição `i` do círculo tratando-a como o início de uma trinca `(i, i+1, i+2)`, usando índice módulo `n` para tratar a circularidade.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada `i`, extrair explicitamente os 3 ladrilhos `(colors[i], colors[(i+1)%n], colors[(i+2)%n])` numa estrutura auxiliar e comparar todos os pares.

- Tempo: O(n) já no total (a janela tem tamanho fixo 3), mas com overhead de alocação por trinca · Espaço: O(1) por iteração, descartado a cada passo
- **Por que não basta:** aloca uma estrutura temporária a cada uma das `n` trincas quando bastam 3 comparações diretas de inteiros.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada `i`, compare diretamente `colors[(i+1)%n]` (o meio) com `colors[i]` (esquerda) e `colors[(i+2)%n]` (direita). A trinca é um grupo alternado exatamente quando o meio é diferente dos dois vizinhos.

## 🎬 Exemplo passo a passo

`colors = [0,1,0,0,1]` (n=5)

| i | Trinca (índices) | Valores | Alterna (meio ≠ ambos vizinhos)? | Contagem |
|---|---|---|---|---|
| 0 | 0,1,2 | 0,1,0 | sim | 1 |
| 1 | 1,2,3 | 1,0,0 | não | 1 |
| 2 | 2,3,4 | 0,0,1 | não | 1 |
| 3 | 3,4,0 | 0,1,0 | sim | 2 |
| 4 | 4,0,1 | 1,0,1 | sim | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `n` trincas, checagem O(1) cada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numberOfAlternatingGroups(int[] colors) {
    int n = colors.length;
    int count = 0;

    for (int i = 0; i < n; i++) {
        int left = colors[i];
        int mid = colors[(i + 1) % n];
        int right = colors[(i + 2) % n];
        if (mid != left && mid != right) {
            count++;
        }
    }

    return count;
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

- Esquecer a circularidade: as trincas que "dão a volta" (envolvendo os últimos índices e o índice 0) exigem `% n`, senão faltam grupos válidos na contagem.
- Como só existem 2 cores, "meio diferente dos dois vizinhos" implica que os dois vizinhos são iguais entre si — mas a checagem direta `mid != left && mid != right` já cobre a condição sem precisar comparar `left == right` explicitamente.
- Cada trinca de 3 ladrilhos consecutivos conta uma vez, mesmo se sobrepor com a trinca vizinha — não há necessidade (nem seria correto) "pular" ladrilhos já usados em outro grupo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem nenhuma alternância | `[1,1,1]` | 0 | toda trinca tem o meio igual a algum vizinho |
| Tamanho mínimo, só uma trinca alterna | `[0,1,0]` | 1 | a trinca (0,1,2) alterna; as outras duas (que cruzam a borda) repetem um vizinho |
| Alternância perfeita, tamanho par | `[0,1,0,1]` | 4 | com período par, toda trinca circular alterna, incluindo as que cruzam a borda |
| Exemplo do enunciado | `[0,1,0,0,1]` | 3 | 3 das 5 trincas circulares alternam |

## 🔗 Conexões

- Problemas irmãos: [1876] Substrings of Size Three with Distinct Characters (mesmo padrão de janela fixa de tamanho 3, sem a circularidade), [3208] Alternating Groups II (mesmo problema generalizado para tamanho de grupo variável, exigindo janela deslizante genuína em vez de checagem fixa)
- No backend: detectar padrões cíclicos válidos em sequências circulares de eventos — por exemplo, validar que turnos de trabalho alternam corretamente entre dois times numa escala circular de plantões.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
