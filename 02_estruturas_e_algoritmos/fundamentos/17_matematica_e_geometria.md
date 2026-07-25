# 17 — Matemática e Geometria

> Manipulação de matrizes, aritmética e os truques numéricos que caem em entrevista. Problemas em [`../problemas/17_matematica_e_geometria/`](../problemas/17_matematica_e_geometria/).

## Conceito

Categoria "caixa de ferramentas" — menos um padrão único, mais um conjunto de técnicas:

**Matrizes:**
- **Rotação 90° in-place** = transpor + inverter cada linha (decore essa decomposição)
- **Espiral**: quatro fronteiras (`topo, base, esq, dir`) que se contraem
- **Set Matrix Zeroes in-place**: usar a primeira linha/coluna como marcador (O(1) de espaço)

**Aritmética:**
- **Detecção de ciclo em sequências numéricas** (Happy Number): fast & slow de novo — ciclos aparecem em qualquer iteração determinística de estado finito
- **Exponenciação rápida**: `x^n = (x²)^(n/2)` → O(log n)
- **GCD (Euclides)**: `gcd(a, b) = gcd(b, a % b)`; LCM = `a*b // gcd`
- **Aritmética modular**: `(a + b) % m`, `(a * b) % m` distribuem — essencial quando o resultado estoura (e em hashing, criptografia)
- Overflow: Python não estoura, **Java/C++ sim** — em entrevista Java, mencione `long` e os limites de `int` (2³¹−1)

## Como reconhecer no enunciado

- "rotacione / percorra em espiral / zere linhas e colunas" → simulação cuidadosa de matriz
- "sem usar operador de multiplicação/divisão", "implemente pow" → exponenciação rápida / bits
- "a sequência entra em loop?" → fast & slow
- Contagem com módulo 10⁹+7 → aritmética modular (comum em DP de contagem)

## Templates

```python
# Rotação 90° horária in-place — transpõe + inverte linhas
def rotate(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]   # transposta
    for linha in m:
        linha.reverse()

# Espiral — quatro fronteiras
def spiral_order(m):
    res = []
    topo, base, esq, dir = 0, len(m) - 1, 0, len(m[0]) - 1
    while topo <= base and esq <= dir:
        res += [m[topo][j] for j in range(esq, dir + 1)]; topo += 1
        res += [m[i][dir] for i in range(topo, base + 1)]; dir -= 1
        if topo <= base:
            res += [m[base][j] for j in range(dir, esq - 1, -1)]; base -= 1
        if esq <= dir:
            res += [m[i][esq] for i in range(base, topo - 1, -1)]; esq += 1
    return res

# Exponenciação rápida — O(log n)
def my_pow(x, n):
    if n < 0:
        x, n = 1 / x, -n
    res = 1.0
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res

# GCD de Euclides
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

## Complexidade típica

Matrizes: O(n·m) tempo, alvo comum de "O(1) espaço extra". Exponenciação/GCD: O(log n).

## Erros comuns

- Rotação: tentar mover os 4 cantos em ciclo sem desenhar antes (a decomposição transpor+inverter é à prova de erro)
- Espiral: não rechecar as fronteiras nas duas últimas passadas (linha/coluna única duplica elementos)
- `%` com negativos: Python devolve não-negativo, Java/C++ devolvem sinal do dividendo — cuidado ao portar
- Comparar floats com `==` (IEEE 754 — Fase 1.1: `0.1 + 0.2 != 0.3`)

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 66. Plus One | 🟢 easy |
| 202. Happy Number | 🟢 easy |
| 48. Rotate Image | 🟡 medium |
| 54. Spiral Matrix | 🟡 medium |
| 73. Set Matrix Zeroes | 🟡 medium |
| 50. Pow(x, n) | 🟡 medium |
| 43. Multiply Strings | 🟡 medium |
| 2013. Detect Squares | 🟡 medium |

## Conexão com backend

Aritmética modular sustenta hashing, sharding (`hash(chave) % n_shards` — e por que consistent hashing existe, Vol. 2 D.3), criptografia (RSA é exponenciação modular — Fase 4.9). Exponenciação rápida é o backoff exponencial calculado direito. E IEEE 754 é o motivo de **dinheiro nunca ser float** (`DECIMAL` no banco — Fase 5.1).
