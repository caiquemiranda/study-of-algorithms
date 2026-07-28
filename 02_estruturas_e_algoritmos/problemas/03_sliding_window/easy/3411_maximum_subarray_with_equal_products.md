# [3411] Maximum Subarray With Equal Products

> 🔗 [LeetCode 3411](https://leetcode.com/problems/maximum-subarray-with-equal-products/) · Dificuldade: 🟢 easy · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Math` `#Easy`

## 📜 O Problema

Dado um array de inteiros **positivos** `nums`, um array `arr` é **produto-equivalente** se `prod(arr) == lcm(arr) * gcd(arr)`, onde `prod` é o produto de todos os elementos, `gcd` é o máximo divisor comum, e `lcm` é o mínimo múltiplo comum. Retorne o comprimento do **maior** subarray produto-equivalente de `nums`.

**Exemplos:**
```
Input:  nums = [1,2,1,2,1,1,1]
Output: 5
Explicação: [1,2,1,1,1] tem prod=2, gcd=1, lcm=2, e gcd*lcm=2=prod.

Input:  nums = [2,3,4,5,6]
Output: 3
Explicação: o subarray [3,4,5] é o mais longo produto-equivalente.

Input:  nums = [1,2,3,1,4,5,1]
Output: 5
```

**Restrições (e o que elas denunciam):**
- `2 <= nums.length <= 100` → entrada pequena; O(n²) com trabalho extra por passo é totalmente viável
- `1 <= nums[i] <= 10` → os valores são pequenos, mas o **produto** de vários deles cresce exponencialmente com o tamanho da janela — um sinal de que aritmética de precisão arbitrária (`BigInteger`) é mais segura que `long`

## 🧭 Como reconhecer o padrão

"Maior subarray contíguo satisfazendo uma condição aritmética (produto, mdc e mmc)" é resolvido expandindo uma janela a partir de cada início, mantendo produto/gcd/lcm atualizados **incrementalmente** em vez de recalculá-los do zero a cada subarray candidato — a marca registrada de uma técnica de janela deslizante, mesmo aqui, onde cada início reinicia a expansão em vez de encolher pela esquerda.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada subarray `[left, right]`, calcular `prod`, `gcd` e `lcm` do zero, percorrendo o subarray inteiro a cada checagem.

- Tempo: O(n³) (O(n²) subarrays, O(n) para recalcular cada um) · Espaço: O(1) além da entrada
- **Por que não basta:** refaz o cálculo de produto/gcd/lcm inteiro a cada subarray candidato, mesmo que ele seja apenas o anterior estendido em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada início `left`, expanda `right` mantendo `product`, `gcd` e `lcm` **incrementalmente**: a cada novo elemento, `product *= num`, `gcd = gcd(gcd, num)`, `lcm = lcm(lcm, num)`. A cada passo, compare `product == gcd * lcm` e atualize o maior comprimento encontrado.

## 🎬 Exemplo passo a passo

`nums = [2,3,4,5,6]` — mostrando a expansão a partir de `left = 1` (valor 3), que produz o melhor resultado:

| right | num | product | gcd | lcm | product == gcd·lcm? | comprimento | melhor |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 3 | 3 | 3≠9, não | — | — |
| 2 | 4 | 12 | 1 | 12 | 12=12, sim | 2 | 2 |
| 3 | 5 | 60 | 1 | 60 | 60=60, sim | 3 | 3 |
| 4 | 6 | 360 | 1 | 60 | 360≠60, não | — | 3 |

Resultado final (considerando todos os `left`): `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n²) — `n` valores de `left`, cada um expandindo `right` com trabalho O(log(valor)) por passo (cálculo de gcd)
- **Espaço:** O(1) além do armazenamento interno de `BigInteger`

## 💻 Implementações

### Java (referência completa e comentada)
```java
import java.math.BigInteger;

public int maxLength(int[] nums) {
    int n = nums.length;
    int best = 0;

    for (int left = 0; left < n; left++) {
        BigInteger product = BigInteger.ONE;
        BigInteger gcd = BigInteger.ZERO; // gcd(0, x) = x, base correta para o primeiro elemento
        BigInteger lcm = BigInteger.ONE;

        for (int right = left; right < n; right++) {
            BigInteger num = BigInteger.valueOf(nums[right]);
            product = product.multiply(num);
            gcd = gcd.gcd(num);
            lcm = lcm.divide(lcm.gcd(num)).multiply(num);

            if (product.equals(gcd.multiply(lcm))) {
                best = Math.max(best, right - left + 1);
            }
        }
    }

    return best;
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

- Para **qualquer par** de dois números `a` e `b`, vale a identidade `a·b = gcd(a,b)·lcm(a,b)` — todo subarray de tamanho 2 automaticamente satisfaz a condição. Isso significa que a resposta nunca é menor que 2 (dado `n >= 2` nas restrições); o desafio real é achar janelas MAIORES que 2 que ainda mantenham a igualdade.
- O produto de vários números de até 10 cresce rapidíssimo (exponencialmente com o tamanho da janela) — usar `long` sem cuidado pode estourar silenciosamente; `BigInteger` remove esse risco, com performance irrelevante aqui (`n<=100`).
- `gcd` inicial deve começar em `0` (não `1`) ao expandir a janela, porque `gcd(0, x) = x` — usar `1` como valor inicial calcularia o `gcd` incorretamente para o primeiro elemento.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Tamanho mínimo (2 elementos) | `[9,4]` | 2 | para QUALQUER par de números, prod = gcd·lcm é uma identidade sempre verdadeira |
| Sequência maior que quebra a igualdade | `[2,3,4,5,6]` | 3 | [3,4,5] é o subarray produto-equivalente mais longo; estender para 6 quebra a igualdade |
| Muitos 1's ao redor de um valor | `[1,2,1,1,1]` | 5 | multiplicar por 1 não afeta produto, gcd nem lcm, então a igualdade se mantém pro array inteiro |
| Trio que quebra, mas o par ainda serve | `[5,5,5]` | 2 | o trio inteiro falha (125≠25), mas qualquer par [5,5] satisfaz pela identidade de 2 elementos |

## 🔗 Conexões

- Problemas irmãos: [3411] variações com GCD/LCM aparecem em [1071] Greatest Common Divisor of Strings (mesma ideia de propriedade aritmética compartilhada por todos os elementos de um conjunto), [3298] Maximum Product Substring (mesma família de expandir uma janela mantendo um produto incrementalmente)
- No backend: identificar o maior lote de valores de configuração (ex.: fatores de escala, multiplicadores de taxa) cuja combinação satisfaz uma invariante aritmética exigida por um sistema de faturamento ou licenciamento.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
