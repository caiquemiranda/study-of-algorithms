# 18 — Bit Manipulation

> Operar diretamente nos bits: o nível mais baixo antes do hardware. Problemas em [`../problemas/18_bit_manipulation/`](../problemas/18_bit_manipulation/).

## Conceito

Inteiros são vetores de bits (Fase 1.1: binário, complemento de dois). Os operadores: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<`/`>>` (shifts).

**As identidades que resolvem problemas:**
- `x ^ x = 0` e `x ^ 0 = x` → XOR de tudo cancela os pares e **sobra o ímpar** (Single Number)
- XOR é comutativo/associativo → a ordem não importa
- `x & (x - 1)` **apaga o bit 1 mais baixo** → contar bits, testar potência de 2 (`x & (x-1) == 0`)
- `x & (-x)` **isola o bit 1 mais baixo**
- `x >> k & 1` lê o k-ésimo bit; `x | (1 << k)` liga; `x & ~(1 << k)` desliga
- Soma sem `+`: `a ^ b` é a soma sem carry; `(a & b) << 1` é o carry — repita até o carry zerar
- **Bitmask como conjunto**: um int de n bits representa um subconjunto de n itens — base da DP com bitmask e de flags de permissão

**Complemento de dois** (por que `-x = ~x + 1`): o negativo é o complemento que faz a soma dar zero com overflow. É por isso que `x & (-x)` isola o último bit.

## Como reconhecer no enunciado

- "todos aparecem duas vezes, exceto um" → XOR
- "conte os bits 1", "potência de dois", "sem usar +/-" → identidades acima
- "sem espaço extra" em problema de paridade/duplicata → pense em XOR
- Estados pequenos (n ≤ 20) para marcar visitados/subconjuntos → bitmask

## Templates

```python
# Single Number — XOR cancela pares, O(n)/O(1)
def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

# Contar bits 1 (Hamming weight) — apaga o mais baixo por iteração
def hamming_weight(n):
    cont = 0
    while n:
        n &= n - 1
        cont += 1
    return cont

# Counting Bits 0..n — DP com offset: bits(i) = bits(i >> 1) + (i & 1)
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

# Missing Number — XOR dos índices com os valores
def missing_number(nums):
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res

# Reverse Bits (32 bits)
def reverse_bits(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res
```

## Complexidade típica

O(1) por operação; O(n) para varrer. Bitmask DP: O(2ⁿ·n) — viável até n ≈ 20.

## Erros comuns

- Precedência: `x & 1 == 0` em Python/Java é `x & (1 == 0)` — **use parênteses** `(x & 1) == 0`
- Python tem inteiros infinitos: algoritmos que dependem de 32 bits (reverse bits, soma sem `+` com negativos) precisam de máscara `& 0xFFFFFFFF`
- `>>` em Java é aritmético (propaga sinal); `>>>` é o lógico — em C++ depende do tipo
- Confundir `&` com `&&` (bit a bit vs lógico)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 136. Single Number | 🟢 easy |
| 191. Number of 1 Bits | 🟢 easy |
| 338. Counting Bits | 🟢 easy |
| 190. Reverse Bits | 🟢 easy |
| 268. Missing Number | 🟢 easy |
| 371. Sum of Two Integers | 🟡 medium |
| 7. Reverse Integer | 🟡 medium |

## Conexão com backend

Bits estão em todo lugar do backend real: **flags de permissão** (`chmod 755` é uma bitmask — Fase 0.1), máscaras de sub-rede/CIDR (Fase 1.4), headers de protocolo binário (o frame do WebSocket tem bits de opcode e mask — Fase 4.14), Bloom filters, `EnumSet` do Java, e feature flags compactas. Quem lê bitmask lê protocolo de rede no Wireshark.
