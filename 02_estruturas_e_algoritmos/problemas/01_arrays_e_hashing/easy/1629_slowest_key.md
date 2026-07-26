# [1629] Slowest Key

> 🔗 [LeetCode 1629](https://leetcode.com/problems/slowest-key/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#String` `#Easy`

## 📜 O Problema

Um teclado recém-projetado foi testado, onde um testador pressionou uma sequência de `n` teclas, uma de cada vez. Você recebe uma string `keysPressed` de tamanho `n`, onde `keysPressed[i]` foi a `i`-ésima tecla pressionada, e uma lista ordenada `releaseTimes`, onde `releaseTimes[i]` foi o tempo em que a `i`-ésima tecla foi solta.

A `0`-ésima tecla foi pressionada no tempo `0`, e cada tecla subsequente foi pressionada exatamente no tempo em que a anterior foi solta. O testador quer saber qual tecla teve a **maior duração**. A `i`-ésima pressão teve duração `releaseTimes[i] - releaseTimes[i-1]`, e a `0`-ésima teve duração `releaseTimes[0]`.

Retorne a tecla da pressão com a maior duração. Se houver múltiplas, retorne a tecla lexicograficamente maior.

**Exemplos:**
```
Input:  releaseTimes = [9,29,49,50], keysPressed = "cbcd"
Output: "c"
Explicação: 'c' teve duração 9 (0 a 9). 'b' teve duração 29-9=20. 'c' (2ª vez) teve
duração 49-29=20. 'd' teve duração 50-49=1. 'b' e o segundo 'c' empatam em 20,
mas 'c' é lexicograficamente maior.

Input:  releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"
Explicação: 'a' tem a maior duração isolada (62-46=16).
```

**Restrições (e o que elas denunciam):**
- `2 <= n <= 1000` → O(n) resolve com folga
- `releaseTimes` estritamente crescente → cada duração é sempre positiva
- em caso de empate na duração, retornar a tecla lexicograficamente MAIOR → precisa de critério de desempate explícito

## 🧭 Como reconhecer o padrão

"Encontrar o elemento com o maior valor calculado, com desempate por outro critério" é resolvido numa única passada, calculando a duração de cada tecla (diferença de tempos consecutivos, com caso especial para a primeira) e comparando com um critério composto: maior duração primeiro, desempate por maior caractere.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Já é a solução direta aqui (não existe uma versão mais lenta relevante): percorrer as teclas, calculando a duração de cada uma, e manter a "melhor" tecla vista até agora segundo o critério composto.

- Tempo: O(n) · Espaço: O(1)
- **Por que vale nomear mesmo assim:** a única armadilha é tratar corretamente a duração da PRIMEIRA tecla (que não tem "tempo anterior" para subtrair, é só `releaseTimes[0]`).

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Mantenha `melhorTecla` e `maiorDuracao` atualizados numa única passada. Para cada tecla `i >= 1`, calcule `duracao = releaseTimes[i] - releaseTimes[i-1]`; se essa duração for maior que `maiorDuracao`, ou empatar e a tecla atual for lexicograficamente maior que `melhorTecla`, atualize os dois.

## 🎬 Exemplo passo a passo

`releaseTimes = [9,29,49,50]`, `keysPressed = "cbcd"`

| Passo | i | tecla | duração | maior duração até agora | melhor tecla até agora |
|---|---|---|---|---|---|
| 1 | 0 | c | 9 (releaseTimes[0]) | 9 | c |
| 2 | 1 | b | 29-9=20 | 20 (maior) | b |
| 3 | 2 | c | 49-29=20 | empate em 20, 'c' > 'b' | c |
| 4 | 3 | d | 50-49=1 | 20 continua maior | c |

Resultado final: `"c"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public char slowestKey(int[] releaseTimes, String keysPressed) {
    char melhorTecla = keysPressed.charAt(0);
    int maiorDuracao = releaseTimes[0];

    for (int i = 1; i < releaseTimes.length; i++) {
        int duracao = releaseTimes[i] - releaseTimes[i - 1];
        char teclaAtual = keysPressed.charAt(i);

        if (duracao > maiorDuracao || (duracao == maiorDuracao && teclaAtual > melhorTecla)) {
            maiorDuracao = duracao;
            melhorTecla = teclaAtual;
        }
    }
    return melhorTecla;
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

- Esquecer o caso especial da PRIMEIRA tecla — sua duração é simplesmente `releaseTimes[0]`, diferente de todas as outras que usam a diferença entre releases consecutivos.
- Esquecer o critério de DESEMPATE — sem ele, a primeira tecla com a duração máxima venceria, mesmo que uma tecla posterior com a MESMA duração fosse lexicograficamente maior.
- Inverter a condição do desempate (`<` em vez de `>`) — o enunciado pede a tecla lexicograficamente MAIOR entre as empatadas, não a menor.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Empate resolvido por desempate | releaseTimes=[9,29,49,50], keysPressed="cbcd" | "c" | 'b' e 'c' empatam em duração 20, 'c' é lexicograficamente maior |
| Sem empate | releaseTimes=[12,23,36,46,62], keysPressed="spuda" | "a" | 'a' tem a maior duração isolada (16) |
| Duas teclas apenas | releaseTimes=[1,10], keysPressed="ab" | "b" | segunda tecla tem duração 9, maior que a primeira (1) |
| Primeira tecla vence | releaseTimes=[100,101], keysPressed="ab" | "a" | primeira tecla tem duração 100, muito maior que a segunda (1) |

## 🔗 Conexões

- Problemas irmãos: [1200] Minimum Absolute Difference (mesmo domínio de rastrear extremos numa passada), [1636] Sort Array by Increasing Frequency (mesma ideia de critério de desempate composto)
- No backend: análise de telemetria de digitação (ex.: identificar qual tecla teve maior tempo de resposta num teste de usabilidade de teclado), ou métricas de performance com critério de desempate definido por regra de negócio.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
