# [0367] Valid Perfect Square

> 🔗 [LeetCode 367](https://leetcode.com/problems/valid-perfect-square/) · Dificuldade: 🟢 easy · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Math` `#Easy`

## 📜 O Problema

Dado um inteiro positivo `num`, retorne `true` se ele é um **quadrado perfeito** (é o produto de algum inteiro por ele mesmo). Não é permitido usar função de biblioteca pronta como `sqrt`.

**Exemplos:**
```
Input:  num = 16    Output: true    (4 * 4 = 16)
Input:  num = 14    Output: false   (3.742... não é inteiro)
```

**Restrições (e o que elas denunciam):**
- `1 <= num <= 2^31 - 1` → `num` pode ser bem grande; testar `1*1, 2*2, 3*3, ...` até passar é O(√num), inviável para o teto do intervalo
- "must not use any built-in library function, such as sqrt" → proíbe o atalho óbvio, exige construir a verificação manualmente
- A pergunta é **binária** (é ou não é quadrado perfeito) sobre um espaço de candidatos **ordenado e monotônico** (`k*k` cresce estritamente com `k`) → sinal claro de busca binária

## 🧭 Como reconhecer o padrão

É irmão gêmeo do [0069] Sqrt(x): a condição `k*k <= num` é verdadeira para valores pequenos de `k` e falsa a partir de um certo ponto, sem alternar — isso é **monotonicidade**, e sempre que uma condição assim existe sobre um intervalo de candidatos, dá para buscar binariamente a fronteira em vez de testar um por um.

## 🐢 Solução 1 — Força bruta

Testar `k = 1, 2, 3, ...` incrementando até que `k*k >= num`; se `k*k == num`, é quadrado perfeito.

- Tempo: O(√num) · Espaço: O(1)
- **Por que não basta:** com `num` até `2^31 - 1`, `√num` chega perto de 46341 testes sequenciais — funciona, mas desperdiça a mesma oportunidade que Sqrt(x): a condição é monotônica, então cada teste poderia eliminar metade dos candidatos em vez de andar um a um.

## 💡 Solução 2 — A ideia otimizada (intuição)

Faça busca binária no intervalo `[1, num]` (ou `[1, num/2 + 1]` como otimização, já que a raiz nunca passa da metade para `num >= 2`). Para cada `mid`, compare `mid * mid` com `num`:
- Se forem iguais, achou — é quadrado perfeito.
- Se `mid * mid < num`, o candidato certo está mais à direita.
- Se `mid * mid > num`, está mais à esquerda.

Se a busca terminar sem encontrar igualdade exata, `num` não é quadrado perfeito.

## 🎬 Exemplo passo a passo

`num = 14`

| Passo | left | mid | right | mid*mid vs num | Decisão |
|---|---|---|---|---|---|
| 1 | 1 | 7 | 14 | 49 > 14 → grande demais | `right = 6` |
| 2 | 1 | 3 | 6 | 9 < 14 → pequeno demais | `left = 4` |
| 3 | 4 | 5 | 6 | 25 > 14 → grande demais | `right = 4` |
| 4 | 4 | 4 | 4 | 16 > 14 → grande demais | `right = 3` |
| 5 | 4 | — | 3 | `left > right` → fim, nunca achou igualdade | retorna `false` |

Resultado final: `false` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log num) — cada iteração descarta metade do intervalo de busca
- **Espaço:** O(1) — só ponteiros inteiros

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isPerfectSquare(int num) {
    if (num < 2) return true;             // 1 é sempre quadrado perfeito (1*1); 0 não entra pela restrição num>=1

    long left = 2, right = num / 2;       // a raiz de num nunca passa de num/2 quando num >= 2

    while (left <= right) {
        long mid = left + (right - left) / 2;
        long quadrado = mid * mid;        // long evita overflow: mid pode chegar perto de 2^15/2^16

        if (quadrado == num) {
            return true;                  // achou a raiz exata
        } else if (quadrado < num) {
            left = mid + 1;               // mid pequeno demais, busca à direita
        } else {
            right = mid - 1;              // mid grande demais, busca à esquerda
        }
    }
    // Esgotou o intervalo sem achar igualdade exata: num não é quadrado perfeito.
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

- **Overflow em `mid * mid`**: assim como em Sqrt(x), `mid` pode se aproximar de 46340 e `mid*mid` estourar `int` de 32 bits — use `long`/`long long`.
- **Esquecer o caso `num = 1`**: é quadrado perfeito (`1*1`), mas o intervalo `[2, num/2]` ficaria vazio (`right = 0 < left = 2`) sem o tratamento especial.
- **Trocar `==` por `<=`**: aqui a busca exige **igualdade exata** para retornar `true` — diferente de Sqrt(x), que aceita o maior candidato que ainda satisfaz `<=`. Confundir os dois templates é o erro mais comum entre esses dois problemas irmãos.
- **Achar que basta comparar com `Math.sqrt(num)`**: o enunciado proíbe função de raiz pronta — mesmo que funcionasse na prática, viola a regra do problema (e converter double para int perto de limites grandes traz erro de precisão).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um (borda mínima) | `num=1` | true | quadrado perfeito trivial, intervalo especial |
| Dois | `num=2` | false | menor caso não trivial que falha |
| Quadrado perfeito comum | `num=16` | true | 4*4=16 |
| Não é quadrado perfeito | `num=14` | false | trace acima |
| Valor grande perto do limite | `num=2147483647` | false | testa overflow em `mid*mid` |

## 🔗 Conexões

- Problemas irmãos: **[0069] Sqrt(x)** (mesmíssima busca binária, só muda o critério de parada), **[0441] Arranging Coins** (busca binária em cima de outra fórmula quadrática), **[0704] Binary Search** (o padrão-base)
- No backend: validar se um valor é "exato" dentro de uma fórmula monotônica (sem usar operações caras como raiz de ponto flutuante) aparece em sistemas de hashing/particionamento que precisam checar propriedades numéricas exatas com determinismo total, sem depender de arredondamento de float.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
