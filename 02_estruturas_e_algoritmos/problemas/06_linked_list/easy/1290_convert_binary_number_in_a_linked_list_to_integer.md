# [1290] Convert Binary Number in a Linked List to Integer

> 🔗 [LeetCode 1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Matematica` `#Easy`

## 📜 O Problema

Dado `head`, uma linked list onde cada nó vale `0` ou `1` e representa, em conjunto, a representação binária de um número (bit mais significativo na cabeça), retorne o **valor decimal** desse número.

**Exemplos:**
```
Input:  head = [1,0,1]
Output: 5
Explicação: (101) em base 2 = 5 em base 10

Input:  head = [0]
Output: 0
```

**Restrições (e o que elas denunciam):**
- Lista nunca vazia → não é preciso tratar `head == null`
- Número de nós não passa de 30 → o resultado cabe folgado num `int` (2^30 é bem menor que `Integer.MAX_VALUE`); não há risco de overflow mesmo com todos os bits em 1
- Cada nó vale 0 ou 1 → não é preciso validar o valor, só interpretá-lo como bit

## 🧭 Como reconhecer o padrão

O input é `ListNode`, mas a operação central é **matemática**: converter uma sequência de bits (mais significativo primeiro) em decimal. É um problema de "percorrer a lista uma vez, acumulando um valor" — não usa fast & slow nem reversão, é a travessia mais simples da categoria combinada com uma conta de base 2.

## 🐢 Solução 1 — Força bruta (contar bits, depois somar potências de 2)

Primeira passada: percorre a lista para contar quantos bits ela tem (`n`). Segunda passada: para cada nó, se o valor for `1`, soma `2^(posição a partir do fim)` ao resultado, usando `Math.pow` ou um laço de potência.

- Tempo: O(n) · Espaço: O(1)
- **Por que não basta:** funciona, mas exige duas passadas pela lista e recalcula potências de 2 (`2^k`) a cada bit — quando existe uma forma de acumular o resultado em **uma única passada**, sem nunca calcular potência explicitamente.

## 💡 Solução 2 — A ideia otimizada (intuição)

Converter binário para decimal, bit a bit da esquerda para a direita, é a mesma conta que "ler um número em voz alta": a cada novo dígito, o valor acumulado até agora **dobra** (desloca uma casa para a esquerda) e **soma** o novo dígito. Em fórmula: `resultado = resultado * 2 + bitAtual`. Isso elimina a necessidade de saber o tamanho da lista ou calcular potências — uma passada só, acumulando.

## 🎬 Exemplo passo a passo

`head = [1,0,1]`

| Passo | bit atual | resultado antes | resultado = resultado*2 + bit |
|---|---|---|---|
| 1 | 1 | 0 | 0*2 + 1 = 1 |
| 2 | 0 | 1 | 1*2 + 0 = 2 |
| 3 | 1 | 2 | 2*2 + 1 = 5 |

Resultado final: `5` ✔ — bate com o esperado no enunciado (`101` em binário = `5`).

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pela lista
- **Espaço:** O(1) — só um acumulador inteiro

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int getDecimalValue(ListNode head) {
    int resultado = 0;

    while (head != null) {
        // Cada novo bit desloca o resultado acumulado uma casa binária p/ a esquerda
        // (multiplica por 2) e soma o bit atual — a mesma lógica de "ler um número em voz alta".
        resultado = resultado * 2 + head.val;
        head = head.next;
    }

    return resultado;
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

- **Deslocar na ordem errada** (`resultado + resultado * 2 + head.val` ou esquecer o `* 2`): sem multiplicar por 2 a cada passo, os bits anteriores não são "empurrados" para a posição certa, e o resultado vira uma simples soma de 0s e 1s em vez do valor binário correto.
- **Calcular a posição de cada bit a partir do fim (`2^k`) sem saber o tamanho da lista de antemão**: obriga a uma passada extra só para contar os nós — desnecessário com a técnica de acumulação.
- **Achar que precisa de `long` ou `BigInteger`**: com no máximo 30 bits, o maior valor possível é `2^30 - 1`, que cabe folgado num `int` de 32 bits — não há necessidade de tipos maiores aqui (diferente de problemas com listas de tamanho maior).
- **Esquecer que o bit mais significativo vem primeiro (na cabeça)**: diferente do LC 2 (Add Two Numbers), onde os dígitos vêm em ordem **inversa** — aqui a ordem de leitura já é a natural, da esquerda para a direita.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um único nó, zero | `head = [0]` | `0` | menor caso possível, testa o acumulador partindo de 0 |
| Um único nó, um | `head = [1]` | `1` | garante que a fórmula funciona com 1 bit só |
| Todos zeros | `head = [0,0,0]` | `0` | garante que multiplicar por 2 repetidamente em 0 continua 0 |
| Todos uns (máximo de bits) | `head = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]` (30 bits) | `2^30 - 1 = 1073741823` | valida que não há overflow no limite da restrição |
| Exemplo do enunciado | `head = [1,0,1]` | `5` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0067] Add Binary** (mesma conversão binário-decimal, mas com strings em vez de linked list), **[0002] Add Two Numbers** (também interpreta uma linked list como número, mas em ordem inversa e em base 10)
- No backend: acumular um valor numa única passada, sem estrutura auxiliar, é o mesmo padrão de **parsers de protocolo binário** (ler um stream de bits/bytes e montar um valor incrementalmente) e de **checksums/hashes rolantes** que processam dados sequencialmente sem armazenar tudo em memória.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
