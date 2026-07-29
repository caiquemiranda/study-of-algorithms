# [0400] Nth Digit

> 🔗 [LeetCode 400](https://leetcode.com/problems/nth-digit/) · Dificuldade: 🟡 medium · Categoria: [`17_matematica_e_geometria`](../../../fundamentos/17_matematica_e_geometria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#MatematicaEGeometria` `#BuscaBinaria` `#Medium`

## 📜 O Problema

Dado um inteiro `n`, retorne o `n`-ésimo dígito da sequência infinita `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]` (os números escritos um atrás do outro, sem separador).

**Exemplos:**
```
Input:  n = 3     Output: 3    (o 3º dígito da sequência "123456789..." é '3')
Input:  n = 11    Output: 0    (a sequência "1234567891011..." tem '0' na posição 11, parte do número 10)
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 2^31 - 1` → `n` pode passar de 2 bilhões; **construir a sequência de dígitos até chegar em `n`** é completamente inviável (geraria uma string de ~2 bilhões de caracteres)
- O tamanho do intervalo `[1, n]` cresce em blocos previsíveis: 9 números de 1 dígito, 90 números de 2 dígitos, 900 de 3 dígitos, e assim por diante (`9 * 10^(k-1)` números com `k` dígitos) → é uma progressão que permite "pular" blocos inteiros por aritmética direta, sem escanear dígito por dígito

## 🧭 Como reconhecer o padrão

Quando um problema pede "o n-ésimo elemento de uma sequência gerada por um padrão matemático previsível" (aqui, blocos de números com a mesma quantidade de dígitos), a resposta geralmente vem de **decompor `n` em blocos** usando aritmética (divisão e módulo), em vez de gerar a sequência inteira. É uma técnica de matemática/contagem, não de comparação com um ponto médio como a busca binária clássica.

## 🐢 Solução 1 — Força bruta

Construir a string `"123456789101112..."` concatenando números crescentes até que ela tenha pelo menos `n` caracteres, e retornar o caractere na posição `n-1`.

- Tempo: O(n) · Espaço: O(n) para a string gerada
- **Por que não basta:** com `n` até `2^31 - 1` (~2.1 bilhões), gerar uma string desse tamanho estoura qualquer limite razoável de tempo e memória — é preciso "pular" direto para o número certo sem construir tudo antes dele.

## 💡 Solução 2 — A ideia otimizada (intuição)

Os números com `k` dígitos formam um bloco de `9 * 10^(k-1)` números, contribuindo `k * 9 * 10^(k-1)` dígitos ao total. Percorra esses blocos (`k = 1, 2, 3, ...`) subtraindo o tamanho de cada bloco de `n`, até que `n` caiba dentro do bloco atual — isso identifica quantos **dígitos** o número procurado tem.

Uma vez sabendo `k` (o tamanho em dígitos) e quanto sobrou de `n` dentro desse bloco, calcule:
- **Qual número**: o primeiro número com `k` dígitos (`10^(k-1)`) mais `(n-1) / k` (quantos números completos "cabem" antes do procurado).
- **Qual dígito dentro desse número**: a posição `(n-1) % k` (0-indexada) na representação em string do número.

## 🎬 Exemplo passo a passo

`n = 11`

| Passo | Bloco (k dígitos) | Tamanho do bloco (9×10^(k-1) × k) | n cabe aqui? | Ação |
|---|---|---|---|---|
| 1 | k=1 (números 1-9) | 9×1 = 9 dígitos | 11 > 9 → não cabe | `n -= 9` → n=2, avança para k=2 |
| 2 | k=2 (números 10-99) | 90×2 = 180 dígitos | 2 <= 180 → cabe aqui! | para aqui |

Com `k=2` e `n=2` (restante dentro do bloco):
- Número: `10^(2-1) + (2-1)/2 = 10 + 0 = 10`
- Dígito dentro do número: posição `(2-1) % 2 = 1` (0-indexada) na string "10" → caractere `'0'`

Resultado final: `0` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(log n) — o número de blocos percorridos é proporcional à quantidade de dígitos do maior número envolvido (no máximo ~10 blocos, já que `n` cabe em 10 dígitos)
- **Espaço:** O(log n) para converter o número final em string (ou O(1) se extrair o dígito por aritmética pura, sem conversão)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findNthDigit(int n) {
    long digitos = 1;             // quantidade de dígitos dos números do bloco atual
    long contagem = 9;            // quantos números existem nesse bloco (9, 90, 900, ...)
    long inicioDoBloco = 1;       // primeiro número do bloco atual (1, 10, 100, ...)

    // "Pula" blocos inteiros de números com a mesma quantidade de dígitos
    // até que n caiba dentro do bloco atual.
    while (n > digitos * contagem) {
        n -= digitos * contagem;
        digitos++;
        contagem *= 10;
        inicioDoBloco *= 10;
    }

    // Dentro do bloco atual, acha o número exato e o dígito dentro dele.
    long numero = inicioDoBloco + (n - 1) / digitos;
    int posicaoDoDigito = (int) ((n - 1) % digitos);

    String comoTexto = Long.toString(numero);
    return comoTexto.charAt(posicaoDoDigito) - '0';
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

- **Overflow em `digitos * contagem`**: com blocos avançando (9, 90, 900, ..., até 9 dígitos), o produto pode passar do limite de `int` — usar `long` nas variáveis de contagem evita esse problema, mesmo `n` cabendo em `int`.
- **Esquecer o `-1` nos cálculos de índice**: tanto `(n-1)/digitos` quanto `(n-1)%digitos` usam `n-1` porque `n` é 1-indexado (o "1º dígito"), mas aritmética de posição é naturalmente 0-indexada.
- **Confundir "quantos números" com "quantos dígitos"**: o tamanho do bloco em **dígitos** é `contagem * digitos` (não só `contagem`) — um erro comum é comparar `n` só com a quantidade de números do bloco, ignorando que cada um contribui `digitos` caracteres.
- **Achar que este problema é busca binária "de verdade"**: como o número de blocos é pequeno (no máximo ~10, já que `n` tem no máximo 10 dígitos), não há ganho real em fazer busca binária sobre os blocos — a varredura sequencial já é O(log n) na prática.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Primeiro dígito | `n=1` | 1 | borda mínima |
| Último dígito de 1 dígito | `n=9` | 9 | fronteira do bloco k=1 |
| Primeiro dígito do bloco de 2 dígitos | `n=10` | 1 | primeiro caractere de "10" |
| Segundo dígito do bloco de 2 dígitos | `n=11` | 0 | trace acima |
| Valor grande (perto do limite) | `n=2147483647` | 2 | testa overflow nas variáveis de contagem |

## 🔗 Conexões

- Problemas irmãos: **[0009] Palindrome Number** (também manipula dígitos de números via aritmética, sem converter para string), **[0069] Sqrt(x)** (outro problema de busca binária "na resposta" para contraste com este, que é puramente aritmético)
- No backend: calcular diretamente a posição de um registro numa sequência gerada por um padrão (ex.: paginação de IDs sequenciais com blocos de tamanho variável) sem materializar a sequência inteira usa o mesmo raciocínio de decomposição aritmética em blocos.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tag do LeetCode), mas a técnica ótima é decomposição aritmética direta em blocos de dígitos (divisão e módulo), sem nenhuma comparação de ponto médio ou descarte de metade de um espaço de busca — por isso o documento foi classificado em `17_matematica_e_geometria`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
