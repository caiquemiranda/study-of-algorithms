# 17 — Matemática e Geometria

> Matrizes, aritmética e os truques numéricos de entrevista. Soluções em [`../problemas/17_matematica_e_geometria/`](../problemas/17_matematica_e_geometria/).

## 1. Conceito Central e Analogia Didática

- Categoria "caixa de ferramentas": **manipulação de matriz** (rotação, espiral, zerar in-place), **aritmética eficiente** (exponenciação rápida, GCD, módulo) e **detecção de ciclo numérico**.
- Rotação 90° in-place = **transpor + inverter cada linha** — decore a decomposição, nunca mova os 4 cantos de cabeça.
- Exponenciação rápida: `x^n = (x²)^(n/2)` → O(log n); Euclides: `gcd(a,b) = gcd(b, a % b)`.

**Analogia (rotação):** girar uma foto 90° = **espelhar na diagonal** (transpor) e depois **espelhar horizontalmente** (inverter linhas). Duas operações simples e seguras substituem uma coreografia de 4 cantos propensa a erro.

## 2. Como Reconhecer (Padrões de Enunciado)

- Se pede "**rotacione / percorra em espiral / zere linhas e colunas** in-place" → simulação de matriz com fronteiras.
- Se pede "implemente `pow` / cálculo com expoente gigante" → exponenciação rápida O(log n).
- Se pergunta "a sequência **entra em loop**?" (Happy Number) → fast & slow em estado numérico.
- Se o resultado "deve ser retornado **módulo 10⁹+7**" → aritmética modular em cada passo (não só no fim).
- Se envolve frações/proporções exatas → GCD para normalizar (nunca compare floats).

## 3. Templates de Código

### Rotação 90° horária in-place

```java
// Java — transposta troca m[i][j] com m[j][i] SÓ acima da diagonal (senão desfaz)
public void rotate(int[][] m) {
    int n = m.length;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {      // j começa em i+1: metade superior apenas
            int tmp = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = tmp;
        }
    }
    for (int[] linha : m) {                     // inverter cada linha completa a rotação horária
        for (int e = 0, d = linha.length - 1; e < d; e++, d--) {
            int tmp = linha[e]; linha[e] = linha[d]; linha[d] = tmp;
        }
    }
}
```

```python
def rotate(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):          # só acima da diagonal: trocar tudo desfaria a transposta
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for linha in m:
        linha.reverse()                    # transpor + inverter linhas = 90° horário
```

### Exponenciação rápida

```java
// Java — processa o expoente BIT a BIT: cada bit 1 multiplica a base acumulada
public double myPow(double x, int n) {
    long e = n;                       // long ANTES de negar: -(-2^31) estoura int
    if (e < 0) { x = 1 / x; e = -e; }
    double res = 1.0;
    while (e > 0) {
        if ((e & 1) == 1) res *= x;   // bit ligado: esta potência de x entra no resultado
        x *= x;                       // x, x², x⁴, x⁸... uma quadratura por bit
        e >>= 1;
    }
    return res;
}
```

```python
def my_pow(x, n):
    if n < 0:
        x, n = 1 / x, -n              # Python não estoura int: negação segura
    res = 1.0
    while n:
        if n & 1:
            res *= x                  # consome o bit menos significativo do expoente
        x *= x
        n >>= 1
    return res
```

### GCD (Euclides) + Happy Number (ciclo com fast & slow)

```python
def gcd(a, b):
    while b:
        a, b = b, a % b               # o resto carrega toda a informação de divisibilidade
    return a

def is_happy(n):
    def prox(x):
        return sum(int(d) ** 2 for d in str(x))
    slow, fast = n, prox(n)
    while fast != 1 and slow != fast:  # sequência determinística de estado finito: ou chega em 1, ou cicla
        slow = prox(slow)
        fast = prox(prox(fast))        # Floyd: se há ciclo, fast alcança slow
    return fast == 1
```

## 4. Walkthrough Visual (Teste de Mesa)

`myPow(2, 10)` — expoente 10 em binário: `1010`

| Iteração | e (binário) | bit atual | res | x após quadratura |
|---|---|---|---|---|
| 1 | 1010 | 0 | 1 | 4 (2²) |
| 2 | 101 | 1 | 1×4 = 4 | 16 (2⁴) |
| 3 | 10 | 0 | 4 | 256 (2⁸) |
| 4 | 1 | 1 | 4×256 = **1024** | — |

- `2^10 = 1024` em **4 iterações** em vez de 10 multiplicações ✔ — o expoente foi consumido bit a bit (10 = 8 + 2).

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade | Motivo |
|---|---|---|
| Rotação / espiral / zerar | O(n·m), espaço O(1) | toca cada célula ~1 vez, in-place |
| Exponenciação rápida | O(log n) | um bit do expoente por iteração |
| GCD de Euclides | O(log min(a,b)) | o resto encolhe exponencialmente |
| Detecção de ciclo | O(tamanho do ciclo) | Floyd sem memória extra |

## 6. Pegadinhas e Erros Comuns

- Transpor a matriz **inteira** (i,j e j,i nos dois sentidos) → desfaz a própria troca; o loop interno começa em `j = i+1`.
- Espiral: não rechecar `topo <= base` / `esq <= dir` nas duas últimas passadas → linha/coluna única duplicada.
- **Java**: `-n` com `n = Integer.MIN_VALUE` estoura → converta para `long` ANTES de negar.
- **Java**: `%` devolve o sinal do dividendo (`-7 % 3 == -1`); **Python** devolve não negativo (`-7 % 3 == 2`) — portar código entre as duas muda resultados.
- Módulo 10⁹+7: aplicar só no fim → overflow no meio; aplique a cada soma/multiplicação (em Java, com `long`).
- Comparar floats com `==` → IEEE 754 (`0.1 + 0.2 != 0.3`, Fase 1.1); use epsilon ou inteiros/frações normalizadas por GCD.
- **Python**: `str(x)` para dígitos é aceitável; em Java, prefira aritmética (`x % 10`, `x / 10`) — conversão de String é cara.

## 7. Aplicações no Mundo Real (Backend)

- **Sharding**: `hash(chave) % n_shards` é aritmética modular — e o motivo de consistent hashing existir quando n muda (Vol. 2, D.3).
- **Criptografia**: RSA/Diffie-Hellman são exponenciação modular com números gigantes (Fase 4.9, TLS).
- **Dinheiro NUNCA em float**: IEEE 754 é o motivo de `DECIMAL`/`BigDecimal` em bancos e APIs de pagamento (Fase 5.1).
- **Backoff exponencial**: retry `2^tentativa` com jitter — a exponenciação do dia a dia (Fase 6.10).
- IDs e hashing distribuído (Snowflake, consistent hash rings) vivem de aritmética modular e bits.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | 🟢 Easy |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | 🟢 Easy |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | 🟡 Medium |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | 🟡 Medium |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | 🟡 Medium |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | 🟡 Medium |
| 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | 🟡 Medium |
| 2013 | [Detect Squares](https://leetcode.com/problems/detect-squares/) | 🟡 Medium |
