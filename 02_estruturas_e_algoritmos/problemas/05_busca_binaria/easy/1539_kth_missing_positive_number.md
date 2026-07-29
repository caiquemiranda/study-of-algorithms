# [1539] Kth Missing Positive Number

> 🔗 [LeetCode 1539](https://leetcode.com/problems/kth-missing-positive-number/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Easy`

## 📜 O Problema

Você recebe um array `arr` de inteiros positivos, ordenado **estritamente crescente**, e um inteiro `k`. Retorne o **k-ésimo número positivo que está faltando** na sequência (contando os "buracos" entre os valores presentes, na ordem em que apareceriam).

**Exemplos:**
```
Input:  arr = [2,3,4,7,11], k = 5    Output: 9
        (faltantes: 1,5,6,8,9,10,12,... → o 5º é 9)
Input:  arr = [1,2,3,4], k = 2       Output: 6
        (faltantes: 5,6,7,... → o 2º é 6)
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length, arr[i], k <= 1000` → array pequeno, O(n) ou até O(n+k) passariam tranquilo
- **Follow up:** "Could you solve this problem in less than O(n) complexity?" → é o convite explícito para O(log n), ou seja, busca binária
- `arr` estritamente crescente → cada posição `i` "deveria" conter o valor `i+1` se nada estivesse faltando; a diferença entre o valor real e o esperado é **monotonicamente não decrescente**, o que habilita busca binária

## 🧭 Como reconhecer o padrão

A sacada é notar que, numa posição `i` (0-indexada), se nada estivesse faltando, `arr[i]` valeria `i + 1`. A diferença `arr[i] - (i + 1)` conta **quantos números já faltaram até aquela posição** — e essa contagem só cresce (ou se mantém) conforme `i` avança. Uma contagem monotônica que cresce com o índice é exatamente o sinal de busca binária pela fronteira onde ela atinge `k`.

## 🐢 Solução 1 — Força bruta

Percorrer os números positivos `1, 2, 3, ...` e, para cada um, verificar se está em `arr` (usando um ponteiro que avança junto); contar quantos "faltam" até chegar ao k-ésimo.

- Tempo: O(n + k) — no pior caso, k pode ser maior que o maior elemento de arr · Espaço: O(1)
- **Por que não basta:** o follow-up pede menos que O(n) — e a contagem de faltantes por posição é monotônica, então dá para pular direto para a região certa via busca binária em vez de caminhar número a número.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada índice `i`, `faltantes_ate_aqui = arr[i] - (i + 1)` (quantos números já faltaram até e incluindo essa posição). Faça busca binária pelo **primeiro índice onde `faltantes_ate_aqui >= k`**:
- Se `faltantes_ate_aqui < k`, ainda não faltou o suficiente → busca à **direita** (`left = mid + 1`).
- Se `faltantes_ate_aqui >= k`, já faltou o bastante (ou mais) → busca à **esquerda** (`right = mid - 1`).

Quando a busca termina, `left` é o número de elementos de `arr` que ficam **antes** do k-ésimo faltante. A resposta final é `left + k` — porque antes da posição `left`, exatamente `left` números de `arr` já foram "consumidos", então o k-ésimo faltante está `k` posições à frente disso.

## 🎬 Exemplo passo a passo

`arr = [2, 3, 4, 7, 11]`, `k = 5`

| Passo | left | mid | right | arr[mid] - (mid+1) | Comparação com k=5 | Decisão |
|---|---|---|---|---|---|---|
| 1 | 0 | 2 (val 4) | 4 | 4 - 3 = 1 | 1 < 5 | `left = 3` |
| 2 | 3 | 3 (val 7) | 4 | 7 - 4 = 3 | 3 < 5 | `left = 4` |
| 3 | 4 | 4 (val 11) | 4 | 11 - 5 = 6 | 6 >= 5 | `right = 3` |
| 4 | 4 | — | 3 | `left > right` → fim | — | retorna `left + k = 4 + 5` |

Resultado final: `9` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — cada iteração descarta metade do array
- **Espaço:** O(1) — só ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findKthPositive(int[] arr, int k) {
    int left = 0, right = arr.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        // Quantos números positivos já faltaram até (e incluindo) a posição mid,
        // assumindo que sem buracos arr[mid] valeria mid+1.
        int faltantesAteAqui = arr[mid] - (mid + 1);

        if (faltantesAteAqui < k) {
            left = mid + 1;              // faltou pouco até aqui: avança
        } else {
            right = mid - 1;             // já faltou o suficiente (ou mais): recua
        }
    }
    // "left" é quantos elementos de arr ficam antes do k-ésimo faltante.
    // Somar k desloca para o valor exato do faltante procurado.
    return left + k;
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

- **Esquecer o `+1` no índice**: a fórmula é `arr[i] - (i + 1)`, não `arr[i] - i` — arrays são 0-indexados, mas a sequência de positivos começa em 1, então é fácil errar esse deslocamento.
- **Retornar `left` em vez de `left + k`**: `left` sozinho é só "quantos elementos de arr vieram antes"; a resposta pede o **valor** do k-ésimo faltante, que exige somar `k`.
- **`k` maior que qualquer faltante dentro do array**: quando `faltantesAteAqui` nunca atinge `k` dentro do array (ex.: `arr=[1,2,3,4], k=2`), a busca termina com `left = arr.length`, e a fórmula `left + k` ainda funciona (`4 + 2 = 6`), porque considera "todo o array já foi consumido, sobra contar direto a partir do fim".
- **Tentar aplicar força bruta pensando que O(n+k) é suficiente**: passa nas restrições pequenas deste problema, mas não atende ao follow-up de menos que O(n) — vale treinar a versão binária mesmo que a bruta "passe".

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem buracos no começo | `arr=[1,2,3,4], k=2` | 6 | testa quando left chega ao fim do array |
| k=1, primeiro faltante | `arr=[2,3,4,7,11], k=1` | 1 | menor faltante possível |
| Array de um elemento | `arr=[1], k=1` | 2 | borda mínima, primeiro faltante logo após |
| Todos os faltantes antes do array | `arr=[5,6,7], k=3` | 3 | 1,2,3 faltam antes de o array sequer começar |
| Exemplo do enunciado | `arr=[2,3,4,7,11], k=5` | 9 | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0268] Missing Number** (também sobre números faltantes, mas com técnica diferente pois o array não vem ordenado), **[2529] Maximum Count of Positive Integer and Negative Integer** (busca binária por fronteira em array ordenado), **[0035] Search Insert Position** (mesmo template de busca por posição)
- No backend: contar/localizar "buracos" numa sequência esperada de IDs (ex.: números de fatura ou de pedido faltando num lote) usando a diferença entre posição esperada e valor real é o mesmo raciocínio usado em auditoria de sequências numéricas sem precisar enumerar todos os IDs.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
