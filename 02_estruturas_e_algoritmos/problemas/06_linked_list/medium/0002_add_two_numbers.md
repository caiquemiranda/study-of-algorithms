# [0002] Add Two Numbers

> 🔗 [LeetCode 2](https://leetcode.com/problems/add-two-numbers/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Matematica` `#Medium`

## 📜 O Problema

Você recebe duas linked lists não vazias representando dois inteiros não negativos. Os dígitos são armazenados em **ordem inversa** (o dígito das unidades vem primeiro), e cada nó guarda um único dígito. Some os dois números e retorne a soma como uma linked list, também em ordem inversa. Os números não têm zero à esquerda (exceto o próprio 0).

**Exemplos:**
```
Input:  l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explicação: 342 + 465 = 807.

Input:  l1 = [0], l2 = [0]
Output: [0]

Input:  l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

**Restrições (e o que elas denunciam):**
- Número de nós em cada lista em `[1, 100]` → O(máx(m, n)) é o esperado, uma única passada pelas duas listas
- `0 <= Node.val <= 9` → cada nó é literalmente um dígito, então a soma de dois dígitos + carry nunca passa de `9+9+1=19` — cabe folgado em `int`
- "os números não têm zero à esquerda, exceto o 0 em si" → garante que não é preciso lidar com dígitos de preenchimento artificiais; mas o **resultado** pode ter um dígito a mais que as duas entradas (por causa do carry final), como no 3º exemplo

## 🧭 Como reconhecer o padrão

Duas linked lists representando números em ordem inversa (dígito menos significativo primeiro) é o cenário perfeito para somar como se faz **na mão, papel e caneta**: a ordem inversa já é exatamente a ordem em que se soma (unidades primeiro, propagando o "vai um"). É uma travessia simples combinada com aritmética de carry — o mesmo padrão do template "Merge com sentinela" da categoria (ver [fundamentos](../../../fundamentos/06_linked_list.md)), usado aqui para construir a lista resultado nó a nó.

## 🐢 Solução 1 — Força bruta (converter para inteiro, somar, reconverter)

Percorre cada lista construindo o número inteiro correspondente (multiplicando por potências de 10), soma os dois inteiros, e converte o resultado de volta para uma linked list.

- Tempo: O(m + n) · Espaço: O(1) extra (fora a lista de saída)
- **Por que não basta:** parece simples, mas não é seguro em geral — não há limite de quantos dígitos os números podem ter (até 100 dígitos cada), o que estoura qualquer tipo numérico fixo (`int`, `long`, até `double`). Precisaria de aritmética de precisão arbitrária (`BigInteger`), o que é mais pesado do que necessário quando dá para somar dígito a dígito diretamente, do jeito que a lista já apresenta os dados.

## 💡 Solução 2 — A ideia otimizada (intuição)

Como os dígitos já vêm em ordem de unidades primeiro, basta percorrer as duas listas **em paralelo**, somando os dígitos correspondentes mais o `carry` ("vai um") da soma anterior, e criando um novo nó com `soma % 10` (o dígito) enquanto guarda `soma / 10` como o novo carry. Continua enquanto houver dígitos em qualquer uma das listas **ou** ainda sobrar carry — é assim que aparece o dígito extra no 3º exemplo.

## 🎬 Exemplo passo a passo

`l1 = [2,4,3]`, `l2 = [5,6,4]` (representam 342 e 465)

| Passo | d1 | d2 | carry (entra) | soma | dígito criado | carry (sai) |
|---|---|---|---|---|---|---|
| 1 | 2 | 5 | 0 | 7 | 7 | 0 |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 |
| 3 | 3 | 4 | 1 | 8 | 8 | 0 |
| fim | — | — | 0 | — | (nenhum, carry zerou) | — |

Resultado final: `7 → 0 → 8` ✔ — bate com o esperado no enunciado (342 + 465 = 807).

## ⚡ Complexidade da solução ótima

- **Tempo:** O(max(m, n)) — percorre as duas listas em paralelo até a mais longa terminar (mais possivelmente um dígito extra do carry final)
- **Espaço:** O(max(m, n)) para a lista de saída (não conta como espaço extra, é o resultado exigido)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0); // sentinela: elimina o caso especial "1º dígito do resultado"
    ListNode cur = dummy;
    int carry = 0;

    // Continua enquanto sobrar dígito em QUALQUER lista OU ainda houver carry a propagar —
    // é essa 3ª condição que gera o dígito extra quando as somas "estouram" 9 no final.
    while (l1 != null || l2 != null || carry != 0) {
        int d1 = (l1 != null) ? l1.val : 0; // lista mais curta contribui com 0 quando já acabou
        int d2 = (l2 != null) ? l2.val : 0;

        int soma = d1 + d2 + carry;
        carry = soma / 10;       // "vai um" para o próximo dígito
        cur.next = new ListNode(soma % 10);
        cur = cur.next;

        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;
    }

    return dummy.next;
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

- **Esquecer o carry final**: se a última soma gerar `carry = 1` (ex.: `9+9`) e o loop parar assim que as duas listas terminarem, falta criar o dígito extra — é por isso que a condição do loop inclui `|| carry != 0`, não só `l1 != null || l2 != null`.
- **Tratar listas de tamanhos diferentes sem o `d1`/`d2` default para 0**: acessar `l1.val` depois que `l1` já virou `null` lança `NullPointerException` — sempre checar antes de ler o valor.
- **Confundir com "número na ordem normal"**: se os dígitos viessem na ordem usual (mais significativo primeiro, como no LC 445 "Add Two Numbers II"), somar diretamente da esquerda não funciona sem inverter as listas ou usar pilhas primeiro — a ordem invertida deste problema é o que torna a soma direta possível.
- **Não usar sentinela**: sem ele, é preciso tratar "qual nó é a cabeça do resultado" como caso especial antes do loop.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ambos zero | `l1=[0], l2=[0]` | `[0]` | menor caso possível, sem carry |
| Carry propaga até o fim | `l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]` | `[8,9,9,9,0,0,0,1]` | testa o dígito extra criado pelo carry final, exemplo do enunciado |
| Listas de tamanhos diferentes | `l1=[9,9], l2=[1]` | `[0,0,1]` | valida o default `0` para a lista mais curta, combinado com carry |
| Sem nenhum carry | `l1=[1,2], l2=[3,4]` | `[4,6]` | garante que a soma simples funciona sem propagação |
| Um único carry no início | `l1=[5], l2=[5]` | `[0,1]` | menor caso onde o carry cria um dígito extra |

## 🔗 Conexões

- Problemas irmãos: **[0445] Add Two Numbers II** (mesmo problema, mas dígitos em ordem normal — exige inverter as listas ou usar pilhas antes de somar), **[1290] Convert Binary Number in a Linked List to Integer** (também interpreta uma linked list como número, mas em base 2 e com o dígito mais significativo primeiro)
- No backend: propagar um "carry" ao longo de uma sequência processada em ordem é o mesmo padrão usado em **checksums acumulativos** e em bibliotecas de **aritmética de precisão arbitrária** (BigInteger/BigDecimal), que somam números maiores que qualquer tipo primitivo dígito a dígito, exatamente como aqui.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
