# [0374] Guess Number Higher or Lower

> 🔗 [LeetCode 374](https://leetcode.com/problems/guess-number-higher-or-lower/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Interactive` `#Easy`

## 📜 O Problema

Alguém escolheu um número secreto entre `1` e `n`. Você chama a API `int guess(int num)`, que devolve:
- `-1` se seu palpite é **maior** que o número secreto,
- `1` se seu palpite é **menor**,
- `0` se você **acertou**.

Encontre o número secreto.

**Exemplos:**
```
Input:  n = 10, pick = 6    Output: 6
Input:  n = 1, pick = 1     Output: 1
Input:  n = 2, pick = 1     Output: 1
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 2^31 - 1` → `n` pode ser gigantesco; adivinhar sequencialmente (1, 2, 3, ...) até acertar é O(n), inviável
- `1 <= pick <= n` → o número secreto sempre existe dentro do intervalo, não precisa tratar "não existe"
- A API devolve exatamente 3 respostas ordenadas (`maior`, `menor`, `igual`) → é literalmente o oráculo de comparação que a busca binária precisa para descartar metade do espaço a cada chamada

## 🧭 Como reconhecer o padrão

Este é o problema mais didático de busca binária "pura": ao contrário de [0035] Search Insert Position (que compara com um array), aqui a comparação vem de uma função externa — mas a lógica é idêntica. Sempre que existe uma forma de perguntar "meu candidato é maior, menor ou igual ao alvo?" sobre um espaço ordenado, é busca binária.

## 🐢 Solução 1 — Força bruta

Chamar `guess(1)`, `guess(2)`, `guess(3)`, ... em ordem crescente até a resposta ser `0`.

- Tempo: O(n) chamadas de API · Espaço: O(1)
- **Por que não basta:** ignora a informação mais valiosa que cada chamada devolve — não é só "acertou ou não", é "para qual lado está o número secreto". Cada chamada poderia eliminar metade dos candidatos, não só um.

## 💡 Solução 2 — A ideia otimizada (intuição)

Trate `[1, n]` como o espaço de busca. A cada iteração, escolha o `mid` do intervalo atual e chame `guess(mid)`:
- Retorno `0` → achou, retorna `mid`.
- Retorno `-1` (mid é maior que o secreto) → o número está à **esquerda** → `right = mid - 1`.
- Retorno `1` (mid é menor que o secreto) → o número está à **direita** → `left = mid + 1`.

Repita até acertar. É a busca binária "de livro-texto" — sem casos especiais de fronteira, porque o número secreto **sempre existe** no intervalo.

## 🎬 Exemplo passo a passo

`n = 10`, `pick = 6`

| Passo | left | mid | right | guess(mid) | Decisão |
|---|---|---|---|---|---|
| 1 | 1 | 5 | 10 | 1 (mid menor que o secreto) | `left = 6` |
| 2 | 6 | 8 | 10 | -1 (mid maior que o secreto) | `right = 7` |
| 3 | 6 | 6 | 7 | 0 (acertou) | retorna 6 |

Resultado final: `6` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) chamadas de API — cada chamada descarta metade do intervalo restante
- **Espaço:** O(1) — dois/três ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
/* The guess API is defined in the parent class GuessGame.
   int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1, right = n;

        while (left <= right) {
            // left + (right-left)/2 evita overflow de int quando n chega perto de 2^31-1
            int mid = left + (right - left) / 2;
            int resposta = guess(mid);

            if (resposta == 0) {
                return mid;                 // acertou o número secreto
            } else if (resposta == -1) {
                right = mid - 1;             // mid é MAIOR que o secreto: descarta a metade direita
            } else {
                left = mid + 1;              // mid é MENOR que o secreto: descarta a metade esquerda
            }
        }
        return -1;                           // inalcançável dado que pick sempre existe em [1, n]
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

- **Inverter o sentido do retorno**: `-1` significa "meu palpite é maior" (não "o secreto é maior"), o que é contraintuitivo — trocar isso inverte toda a lógica de `left`/`right` e faz a busca divergir do alvo.
- **`(left + right) / 2` em vez de `left + (right - left) / 2`**: com `n` até `2^31 - 1`, a soma direta estoura `int` — mesmo cuidado que em [0278] First Bad Version.
- **Confundir com busca por fronteira** (como First Bad Version): aqui existe um valor exato a encontrar, então o template usa `left <= right` e retorna assim que `resposta == 0` — não é uma busca por "onde a condição muda".
- **Ignorar o custo de chamadas de API**: em cenários reais (rede, disco), cada chamada tem latência — é por isso que "minimizar chamadas" é o critério de qualidade da solução, não só o tempo de CPU.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| n=1 (borda mínima) | `n=1, pick=1` | 1 | único candidato possível |
| Secreto é o primeiro | `n=10, pick=1` | 1 | fronteira no início do intervalo |
| Secreto é o último | `n=10, pick=10` | 10 | fronteira no fim do intervalo |
| Secreto no meio | `n=10, pick=6` | 6 | trace acima |
| n grande (perto do limite) | `n=2147483647, pick=2147483647` | 2147483647 | testa overflow em `mid` |

## 🔗 Conexões

- Problemas irmãos: **[0278] First Bad Version** (mesma ideia de busca binária interativa, mas por fronteira booleana em vez de valor exato), **[0704] Binary Search** (a mesma lógica, mas comparando com um array em vez de uma API)
- No backend: é o modelo mental de qualquer protocolo de "negociação por intervalo" — por exemplo, ajustar um parâmetro de rate limiting via feedback binário (`"está alto/baixo demais"`) até convergir no valor ideal, minimizando o número de rodadas de ajuste.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
