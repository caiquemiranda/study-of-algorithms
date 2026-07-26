# [1460] Make Two Arrays Equal by Reversing Subarrays

> 🔗 [LeetCode 1460](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#HashTable` `#Sorting` `#Easy`

## 📜 O Problema

Você recebe dois arrays de inteiros de mesmo tamanho, `target` e `arr`. Em um passo, você pode selecionar qualquer **subarray não vazio** de `arr` e revertê-lo. Você pode fazer quantos passos quiser.

Retorne `true` se você pode tornar `arr` igual a `target`, ou `false` caso contrário.

**Exemplos:**
```
Input:  target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explicação: é possível reverter subarrays sucessivamente até transformar arr em target.

Input:  target = [7], arr = [7]
Output: true

Input:  target = [3,7,9], arr = [3,7,11]
Output: false
Explicação: arr não tem o valor 9, nunca pode virar target.
```

**Restrições (e o que elas denunciam):**
- `1 <= target.length <= 1000` → O(n log n) resolve com folga
- reversão de subarray pode ser aplicada QUANTAS VEZES quiser, em QUALQUER subarray → isso significa que qualquer permutação é alcançável
- valores entre 1 e 1000 → pequeno o suficiente para array de contagem fixo

## 🧭 Como reconhecer o padrão

Quando a operação permitida (reverter subarrays arbitrariamente, quantas vezes quiser) é poderosa o suficiente para alcançar QUALQUER permutação, o problema deixa de ser sobre a ORDEM e vira sobre o MULTICONJUNTO — basta checar se os dois arrays têm exatamente os mesmos elementos com as mesmas frequências.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Ordenar os dois arrays e compará-los elemento a elemento.

- Tempo: O(n log n) · Espaço: O(n)
- **Por que não basta:** já é razoável, mas dá pra fazer O(n) com contagem, já que os valores são limitados a um intervalo pequeno (1 a 1000).

## 💡 Solução 2 — A ideia otimizada (intuição)

Array de contagem (frequência) para `target`, decrementar para cada elemento de `arr`; se alguma contagem ficar negativa, `false`; no final, todas as contagens precisam ser zero.

## 🎬 Exemplo passo a passo

`target = [1,2,3,4]`, `arr = [2,4,1,3]` — contagem inicial de target: `{1:1,2:1,3:1,4:1}`

| Passo | elemento de arr | contagem[elemento] antes | Ação | contagem[elemento] depois |
|---|---|---|---|---|
| 1 | 2 | 1 | decrementa | 0 |
| 2 | 4 | 1 | decrementa | 0 |
| 3 | 1 | 1 | decrementa | 0 |
| 4 | 3 | 1 | decrementa | 0 |

Todas as contagens zeraram, nenhuma ficou negativa → **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — array de contagem fixo de 1001 posições
- **Espaço:** O(1) extra

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean canBeEqual(int[] target, int[] arr) {
    int[] contagem = new int[1001];
    for (int v : target) {
        contagem[v]++;
    }
    for (int v : arr) {
        contagem[v]--;
        if (contagem[v] < 0) {
            return false; // arr tem mais ocorrências deste valor do que target
        }
    }
    return true; // se chegou aqui, as contagens batem (soma zero e nunca negativa)
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

- Tentar simular reversões de verdade — completamente desnecessário; a operação permitida é poderosa o suficiente para tornar a ORDEM irrelevante.
- Esquecer de checar se alguma contagem fica negativa durante o processo — só checar no final (`soma == 0`) não pega o caso em que `arr` tem um valor a MAIS de algo compensado por outro valor faltando.
- Comparar os arrays diretamente (elemento a elemento, sem ordenar/contar) — a ordem NÃO importa aqui, graças à operação de reversão livre.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Mesmos elementos, ordem diferente | target=[1,2,3,4], arr=[2,4,1,3] | true | mesmo multiconjunto |
| Já iguais | target=[7], arr=[7] | true | sem necessidade de nenhuma reversão |
| Elemento faltando | target=[3,7,9], arr=[3,7,11] | false | arr não tem o valor 9 |
| Duplicatas com contagens diferentes | target=[1,1,2], arr=[1,2,2] | false | target tem dois 1's, arr só tem um |

## 🔗 Conexões

- Problemas irmãos: [0242] Valid Anagram (exatamente a mesma técnica de comparação por contagem), [1122] Relative Sort Array (mesmo domínio de contagem + reconstrução)
- No backend: validação de que dois lotes de dados contêm exatamente os mesmos registros, independente da ordem de chegada (ex.: reconciliação de duas fontes de dados).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
