# 18 — Bit Manipulation

> Operar direto nos bits: o último nível antes do hardware. Soluções em [`../problemas/18_bit_manipulation/`](../problemas/18_bit_manipulation/).

## 1. Conceito Central e Analogia Didática

- Inteiros são vetores de bits (complemento de dois — Fase 1.1); operadores: `&` `|` `^` `~` `<<` `>>`.
- Identidades que resolvem problemas: `x ^ x = 0` (XOR cancela pares), `x & (x-1)` apaga o bit 1 mais baixo, `x & (-x)` isola-o, `x | (1<<k)` liga o bit k.
- **Bitmask como conjunto**: um int de 32 bits representa 32 flags booleanas — base de permissões e DP com bitmask.

**Analogia:** painel de 32 interruptores numa placa: `|` liga um interruptor específico, `&` testa se está ligado, `^` inverte, e a "mágica" do XOR em par é que ligar e desligar o mesmo interruptor duas vezes volta ao estado inicial — sobra aceso só o que foi tocado uma vez.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se diz "todos aparecem **duas vezes, exceto um**" → XOR de tudo (os pares se cancelam).
- Se pede "**conte os bits 1**" / "é potência de 2?" → `x & (x-1)`.
- Se pede "some **sem usar +**" → XOR (soma sem carry) + AND<<1 (carry), repetir até zerar.
- Se pede "número **faltando** em 0..n" → XOR de índices com valores.
- Se o estado é pequeno (n ≤ 20) e precisa marcar subconjuntos → bitmask.

## 3. Templates de Código

### XOR para achar o único (Single Number / Missing Number)

```java
// Java — XOR é comutativo e associativo: a ordem não importa, os pares somem
public int singleNumber(int[] nums) {
    int res = 0;                 // 0 é neutro do XOR: x ^ 0 = x
    for (int n : nums) {
        res ^= n;                // cada par a^a vira 0; sobra exatamente o ímpar
    }
    return res;
}

public int missingNumber(int[] nums) {
    int res = nums.length;               // começa com o índice n (que não tem par no loop)
    for (int i = 0; i < nums.length; i++) {
        res ^= i ^ nums[i];              // índices 0..n e valores 0..n (menos o faltante) se cancelam
    }
    return res;                          // sobra o número que nunca apareceu
}
```

```python
def single_number(nums):
    res = 0
    for n in nums:
        res ^= n         # pares se anulam; o solitário sobrevive
    return res
```

### Contar bits (Hamming Weight + Counting Bits com DP)

```java
// Java — n & (n-1) apaga o 1 mais baixo: itera só o nº de bits ligados, não 32 vezes
public int hammingWeight(int n) {
    int cont = 0;
    while (n != 0) {
        n &= (n - 1);    // cada passada elimina exatamente um bit 1
        cont++;
    }
    return cont;
}

// dp[i] = dp[i >> 1] + (i & 1): o nº de bits de i é o de i/2 mais o bit que caiu fora
public int[] countBits(int n) {
    int[] dp = new int[n + 1];
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i >> 1] + (i & 1);   // reaproveita o resultado já calculado (DP + bits)
    }
    return dp;
}
```

```python
def hamming_weight(n):
    cont = 0
    while n:
        n &= n - 1       # apaga o bit 1 mais baixo por iteração
        cont += 1
    return cont

def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)   # i>>1 já foi resolvido: transição O(1)
    return dp
```

### Soma sem `+` (o mecanismo do somador da CPU)

```python
def get_sum(a, b):
    MASK = 0xFFFFFFFF                     # Python tem int infinito: simula 32 bits na mão
    while b & MASK:
        carry = (a & b) << 1              # AND acha as posições que geram "vai um"
        a = (a ^ b) & MASK                # XOR soma ignorando o carry
        b = carry & MASK                  # o carry vira a nova parcela, até se esgotar
    return (a & MASK) if a <= 0x7FFFFFFF else ~((a ^ MASK) & MASK)  # reinterpreta negativo
```

## 4. Walkthrough Visual (Teste de Mesa)

`singleNumber([4, 1, 2, 1, 2])`

| n | res (binário) antes | res ^= n | res após |
|---|---|---|---|
| 4 | 000 | 000 ^ 100 | 100 (4) |
| 1 | 100 | 100 ^ 001 | 101 (5) |
| 2 | 101 | 101 ^ 010 | 111 (7) |
| 1 | 111 | 111 ^ 001 | 110 (6) |
| 2 | 110 | 110 ^ 010 | 100 (**4**) ✔ |

- Os pares 1^1 e 2^2 se cancelaram em qualquer ordem; sobrou o 4 — sem set, sem espaço extra.

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade | Motivo |
|---|---|---|
| Operador bit a bit | O(1) | instrução única de CPU |
| Varredura com XOR | O(n), espaço O(1) | uma passada, um acumulador |
| Hamming weight | O(bits ligados) | `n & (n-1)` pula os zeros |
| DP bitmask | O(2ⁿ · n) | viável até n ≈ 20 |

## 6. Pegadinhas e Erros Comuns

- **Precedência**: `x & 1 == 0` avalia `1 == 0` primeiro (Java e Python!) → sempre `(x & 1) == 0`.
- **Java**: `>>` é aritmético (propaga o sinal); `>>>` é o shift lógico — em números negativos a diferença é abismal.
- **Python**: int é infinito → algoritmos de 32 bits (soma sem `+`, reverse bits) exigem máscara `& 0xFFFFFFFF` e reinterpretação do negativo.
- Confundir `&`/`|` (bit a bit) com `&&`/`||` (lógico) em Java — compila em `boolean` e muda semântica (sem curto-circuito).
- `x << 1` estoura int silenciosamente em Java — para contagens grandes, `long`.
- Esquecer que `~x = -x - 1` (complemento de dois) ao "inverter flags" — para limpar um bit use `x & ~(1 << k)`, não `~`.

## 7. Aplicações no Mundo Real (Backend)

- **Permissões**: `chmod 755` é bitmask pura (rwx = 3 bits); flags de feature compactas e `EnumSet` do Java.
- **Redes**: máscara de sub-rede/CIDR é AND bit a bit (Fase 1.4); o frame do WebSocket carrega opcode e mask em bits (pilar 4.14).
- **Bancos**: bitmap indexes (Postgres usa bitmap scans para combinar índices com AND/OR de bitmaps).
- **Bloom filter**: k bits ligados por hash — dedup e cache negativo (Fase 2.2, Vol. 2 E.2).
- Quem lê bitmask lê **protocolo binário no Wireshark** — a ponte direta com seu mundo de automação (Modbus/BACnet são campos de bits).

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | 🟢 Easy |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | 🟢 Easy |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | 🟢 Easy |
| 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | 🟢 Easy |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | 🟢 Easy |
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | 🟡 Medium |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | 🟡 Medium |
