# [0234] Palindrome Linked List

> 🔗 [LeetCode 234](https://leetcode.com/problems/palindrome-linked-list/) · Dificuldade: 🟢 easy · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#FastSlow` `#ReversaoDePonteiros` `#Easy`

## 📜 O Problema

Dado o `head` de uma linked list simples, retorne `true` se ela é um **palíndromo** (lê-se igual de trás para frente) ou `false` caso contrário.

**Exemplos:**
```
Input:  head = [1,2,2,1]
Output: true

Input:  head = [1,2]
Output: false
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^5]` → O(n) é o esperado; `10^5` também é um sinal de que soluções O(n²) (comparar cada nó com todos os outros) não passam
- `0 <= Node.val <= 9` → valores pequenos, sem risco de overflow; não há truque numérico aqui
- Follow-up "O(n) tempo e O(1) espaço" → descarta copiar a lista para um array (O(n) espaço) como solução final; empurra para achar o meio + inverter a segunda metade in-place

## 🧭 Como reconhecer o padrão

"Verifique se é palíndromo" numa estrutura sem acesso por índice (não dá para comparar `lista[i]` com `lista[n-1-i]` direto, como num array) combina duas técnicas da categoria: **fast & slow** para achar o meio sem contar o tamanho antes, e **reversão de ponteiros** para inverter a segunda metade — ver [fundamentos](../../../fundamentos/06_linked_list.md).

## 🐢 Solução 1 — Força bruta (copiar valores para um array)

Percorre a lista copiando cada valor para um array (ou `ArrayList`), depois compara o array com dois ponteiros a partir das pontas (`i=0` e `j=n-1`), como um palíndromo comum de array.

- Tempo: O(n) · Espaço: O(n)
- **Por que não basta:** o tempo já é ótimo, mas o follow-up pede O(1) de espaço — copiar todos os valores para um array joga fora a chance de resolver in-place usando a própria estrutura da lista.

## 💡 Solução 2 — A ideia otimizada (intuição)

Um palíndromo lido em linked list não permite "andar para trás" — mas dá para **inverter a segunda metade** e comparar as duas metades andando para frente nas duas ao mesmo tempo. Passos:
1. Achar o **meio** da lista com fast & slow (fast anda 2, slow anda 1; quando fast acaba, slow está no meio).
2. **Inverter** a segunda metade (a partir de `slow`), usando a técnica de reversão de ponteiros.
3. Comparar a primeira metade com a segunda metade (agora invertida), nó a nó, ponteiro a ponteiro.

## 🎬 Exemplo passo a passo

`head = [1,2,2,1]`

**Fase 1 — achar o meio (fast & slow):**

| Passo | slow | fast |
|---|---|---|
| início | 1 (1º) | 1 (1º) |
| 1 | 2 (2º) | 2 (3º) |
| 2 | 2 (3º) | null → loop encerra |

`slow` parou no 3º nó (valor 2) — início da segunda metade.

**Fase 2 — inverter a segunda metade** (`2 → 1`, a partir de `slow`): vira `1 → 2` (agora começando pelo antigo último nó).

**Fase 3 — comparar as duas metades:**

| Passo | 1ª metade | 2ª metade invertida | Iguais? |
|---|---|---|---|
| 1 | 1 | 1 | sim |
| 2 | 2 | 2 | sim |

Resultado final: `true` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — achar o meio é O(n/2), inverter a metade é O(n/2), comparar é O(n/2); soma continua O(n)
- **Espaço:** O(1) — só ponteiros; a inversão é feita in-place, sem estrutura auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isPalindrome(ListNode head) {
    if (head == null || head.next == null) return true; // 0 ou 1 nó é sempre palíndromo

    // Fase 1: acha o início da 2ª metade com fast & slow.
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Fase 2: inverte a 2ª metade (a partir de slow) — mesma técnica do LC 206.
    ListNode segundaMetadeInvertida = reverse(slow);

    // Fase 3: compara a 1ª metade (a partir de head) com a 2ª metade invertida.
    // Se a lista tem tamanho ímpar, a 1ª metade é "mais curta" e para de comparar primeiro
    // naturalmente, porque o laço para quando p2 chega em null.
    ListNode p1 = head, p2 = segundaMetadeInvertida;
    boolean resultado = true;
    while (p2 != null) {
        if (p1.val != p2.val) {
            resultado = false;
            break;
        }
        p1 = p1.next;
        p2 = p2.next;
    }

    return resultado;
    // Nota: o enunciado não exige restaurar a lista ao estado original; se exigisse,
    // bastaria inverter a 2ª metade de novo antes de retornar.
}

private ListNode reverse(ListNode head) {
    ListNode prev = null;
    while (head != null) {
        ListNode nxt = head.next;
        head.next = prev;
        prev = head;
        head = nxt;
    }
    return prev;
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

- **Errar o ponto de corte em listas de tamanho ímpar**: com `fast != null && fast.next != null`, `slow` para no nó do **meio exato** em listas ímpares (esse nó não precisa ter par para comparar — ele acaba ficando de fora da comparação porque a 2ª metade invertida é sempre menor ou igual à 1ª). Testar com `[1,2,3,2,1]` ajuda a validar isso.
- **Comparar por referência (`p1 == p2`) em vez de por valor (`p1.val == p2.val`)**: aqui o objetivo é comparar **conteúdo**, não identidade — é o oposto da pegadinha de detecção de ciclo.
- **Esquecer o caso base de 0 ou 1 nó**: uma lista com 1 nó (ou vazia) é trivialmente um palíndromo; sem esse caso base, o fast & slow ainda funciona, mas é mais seguro tratar explicitamente.
- **Modificar a lista original sem necessidade em contextos onde ela precisa ser preservada**: a inversão da 2ª metade altera os ponteiros originais — se o enunciado (ou uma variação dele) exigir manter a lista intacta, é preciso desfazer a inversão no final.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um nó | `head = [1]` | `true` | caso base, sem nada para comparar |
| Dois nós, não palíndromo | `head = [1,2]` | `false` | exemplo do enunciado, menor caso "falso" |
| Tamanho par, palíndromo | `head = [1,2,2,1]` | `true` | exemplo do enunciado, trace acima |
| Tamanho ímpar, palíndromo | `head = [1,2,3,2,1]` | `true` | valida que o nó do meio não atrapalha a comparação |
| Tamanho ímpar, não palíndromo | `head = [1,2,3,4,1]` | `false` | garante que a comparação nó a nó realmente pega a diferença |

## 🔗 Conexões

- Problemas irmãos: **[0206] Reverse Linked List** (a sub-rotina de reversão usada na fase 2), **[0876] Middle of the Linked List** (a sub-rotina de achar o meio usada na fase 1), **[0143] Reorder List** (combina as mesmas duas sub-rotinas — achar meio + inverter — para um objetivo diferente)
- No backend: comparar uma sequência com sua própria reversão sem espaço extra é o mesmo raciocínio usado em **verificação de integridade de streams** (checar simetria de um payload sem materializar tudo em memória) e em testes de **estruturas de dados persistentes** onde criar uma cópia completa para comparação seria caro demais.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
