# [0278] First Bad Version

> 🔗 [LeetCode 278](https://leetcode.com/problems/first-bad-version/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Interactive` `#Easy`

## 📜 O Problema

Você é gerente de produto e tem `n` versões `[1, 2, ..., n]`. A partir de uma versão ruim, **todas as versões seguintes também são ruins** (uma vez que quebra, fica quebrado). Você recebe uma API `bool isBadVersion(version)` e precisa achar a **primeira** versão ruim, **minimizando o número de chamadas** à API.

**Exemplos:**
```
Input:  n = 5, bad = 4    Output: 4
        (isBadVersion(3) -> false, isBadVersion(5) -> true, isBadVersion(4) -> true)
Input:  n = 1, bad = 1    Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= bad <= n <= 2^31 - 1` → `n` pode ser gigantesco; testar versão por versão (1, 2, 3, ...) até achar a ruim é O(n), inviável
- "minimize the number of calls to the API" → é o pedido explícito por eficiência: cada chamada tem "custo", então o algoritmo precisa descartar o máximo de candidatos por chamada
- "all versions after a bad version are also bad" → a sequência de respostas é `false, false, ..., false, true, true, ..., true` — **monotônica**, a condição ideal para busca binária

## 🧭 Como reconhecer o padrão

Sempre que a resposta de uma pergunta booleana muda de `false` para `true` exatamente uma vez ao longo de um intervalo ordenado (nunca volta a `false`), é **busca binária na fronteira**: em vez de procurar um valor específico, procuramos o ponto exato onde a condição vira de `false` para `true`.

## 🐢 Solução 1 — Força bruta

Chamar `isBadVersion(1)`, `isBadVersion(2)`, `isBadVersion(3)`, ... em ordem crescente até achar a primeira que retorna `true`.

- Tempo: O(n) chamadas de API · Espaço: O(1)
- **Por que não basta:** o enunciado pede para **minimizar chamadas**, e testar sequencialmente ignora que a resposta é monotônica — cada chamada devolve muito mais informação do que "essa versão específica é ruim ou não": ela também elimina metade dos candidatos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Trate `[1, n]` como o espaço de busca. Para cada `mid`, chame `isBadVersion(mid)`:
- Se `true`, `mid` é ruim (ou é a primeira ruim, ou existe uma ruim antes dela) → a resposta está em `mid` ou **à esquerda** → guarda `mid` como candidato e `right = mid - 1`.
- Se `false`, `mid` é boa → a primeira ruim está estritamente **à direita** → `left = mid + 1`.

Quando o intervalo se esgota, `left` aponta exatamente para a primeira versão ruim — é o mesmo "lower bound" de [0035] Search Insert Position, só que a condição vem de uma chamada de API em vez de comparação de array.

## 🎬 Exemplo passo a passo

`n = 5`, `bad = 4`

| Passo | left | mid | right | isBadVersion(mid) | Decisão |
|---|---|---|---|---|---|
| 1 | 1 | 3 | 5 | false | `left = 4` |
| 2 | 4 | 4 | 5 | true | guarda 4, `right = 3` |
| 3 | 4 | — | 3 | `left > right` → fim | retorna `left = 4` |

Resultado final: `4` ✔ (só 2 chamadas de API, contra até 4 na força bruta)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) chamadas de API — cada chamada descarta metade do intervalo restante
- **Espaço:** O(1) — dois/três ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1, right = n;

        while (left < right) {
            // left + (right-left)/2 evita overflow de int quando n chega perto de 2^31-1
            int mid = left + (right - left) / 2;

            if (isBadVersion(mid)) {
                // mid é ruim: a primeira ruim é mid ou está antes dele.
                // NÃO descartamos mid (right = mid, não mid - 1).
                right = mid;
            } else {
                // mid é boa: a primeira ruim com certeza está depois de mid.
                left = mid + 1;
            }
        }
        // Invariante: quando left == right, esse índice é a primeira versão ruim.
        return left;
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

- **`(left + right) / 2` em vez de `left + (right - left) / 2`**: com `n` até `2^31 - 1`, a soma direta estoura `int` — clássico bug de overflow neste problema específico, já que o enunciado escolhe deliberadamente esse limite.
- **`right = mid - 1` quando `isBadVersion(mid)` é `true`**: erra porque `mid` PODE ser a própria primeira versão ruim — descartá-lo perde a resposta correta. O padrão certo aqui é `right = mid` (mantém mid como candidato).
- **Confundir com busca por valor exato**: não existe "o valor que estou procurando" no array — a busca é pela **fronteira** entre `false` e `true`, então o template de busca binária muda (usa `left < right` em vez de `left <= right`).
- **Testar `n = 1`**: com só uma versão, ela precisa ser automaticamente a resposta se for ruim — bom caso de borda para verificar que o laço nem entra e retorna `left` direto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Só uma versão, ruim | `n=1, bad=1` | 1 | borda mínima |
| Primeira é a ruim | `n=5, bad=1` | 1 | fronteira no início, sem "boas" antes |
| Última é a ruim | `n=5, bad=5` | 5 | fronteira no fim, todas as anteriores são boas |
| Fronteira no meio | `n=5, bad=4` | 4 | trace acima |
| n grande (perto do limite) | `n=2147483647, bad=2147483647` | 2147483647 | testa overflow em `mid` |

## 🔗 Conexões

- Problemas irmãos: **[0035] Search Insert Position** (mesmo template de "lower bound", mas em array em vez de API), **[0374] Guess Number Higher or Lower** (busca binária interativa com API de 3 respostas), **[0704] Binary Search** (o padrão-base)
- No backend: é literalmente o algoritmo do `git bisect` — achar o primeiro commit "ruim" (que quebrou um teste) numa sequência onde tudo depois dele também está quebrado, minimizando quantos commits você precisa testar manualmente.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
