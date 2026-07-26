# [1184] Distance Between Bus Stops

> 🔗 [LeetCode 1184](https://leetcode.com/problems/distance-between-bus-stops/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#PrefixSum` `#Easy`

## 📜 O Problema

Um ônibus tem `n` paradas numeradas de `0` a `n-1` que formam um círculo. Conhecemos a distância entre todos os pares de paradas vizinhas, onde `distance[i]` é a distância entre as paradas `i` e `(i+1) % n`. O ônibus anda nos dois sentidos (horário e anti-horário).

Retorne a menor distância entre as paradas `start` e `destination`.

**Exemplos:**
```
Input:  distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explicação: a distância entre 0 e 1 é 1 ou 9, o mínimo é 1.

Input:  distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explicação: a distância entre 0 e 2 é 3 ou 7, o mínimo é 3.

Input:  distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explicação: a distância entre 0 e 3 é 6 ou 4, o mínimo é 4.
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^4` → O(n) resolve com folga
- `distance.length == n`, `0 <= start, destination < n` → paradas formam um círculo fechado
- `0 <= distance[i] <= 10^4` → soma total cabe em `int` sem overflow

## 🧭 Como reconhecer o padrão

"Menor distância num circuito fechado, podendo andar nos dois sentidos" é resolvido calculando a soma total do circuito e a soma do trecho direto entre os dois pontos (num sentido); a resposta é o menor entre esse trecho direto e "o resto do círculo" (total - trecho direto).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular o percurso célula a célula em ambos os sentidos (horário e anti-horário) a partir de `start` até `destination`, somando as distâncias percorridas em cada simulação, e retornar o menor total.

- Tempo: O(n) (na prática já é O(n), mas fazendo duas simulações completas em vez de uma soma direta) · Espaço: O(1)
- **Por que não basta:** simula passo a passo quando a soma do trecho pode ser calculada diretamente somando o intervalo `[min(start,destination), max(start,destination))`, sem precisar "andar" célula por célula com lógica de direção.

## 💡 Solução 2 — A ideia otimizada (intuição)

Garanta `start < destination` (troque se necessário, já que a distância é simétrica). Some `distance[start..destination-1]` para obter a distância "direta" num sentido. Some todo o array para obter o `total`. A resposta é `min(direta, total - direta)`.

## 🎬 Exemplo passo a passo

`distance = [1,2,3,4]`, `start = 0`, `destination = 2`

| Passo | Cálculo | Valor |
|---|---|---|
| 1 | soma total | 10 |
| 2 | soma direta (índices 0 a 1) | 3 |
| 3 | outro sentido (total - direta) | 7 |
| 4 | min(direta, outro sentido) | 3 |

Resultado final: `3` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para somar o intervalo direto e o array inteiro
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int distanceBetweenBusStops(int[] distance, int start, int destination) {
    int menor = Math.min(start, destination);
    int maior = Math.max(start, destination);

    int somaDireta = 0;
    int somaTotal = 0;
    for (int i = 0; i < distance.length; i++) {
        somaTotal += distance[i];
        if (i >= menor && i < maior) {
            somaDireta += distance[i]; // soma só o trecho entre as duas paradas, num sentido
        }
    }

    return Math.min(somaDireta, somaTotal - somaDireta);
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

- Esquecer de normalizar `start` e `destination` (garantir qual é o menor índice) antes de somar o trecho — sem isso, o intervalo `[start, destination)` pode ficar invertido ou incorreto.
- Confundir "soma do trecho direto" com "soma de tudo exceto o trecho" — a resposta é o MENOR entre os dois sentidos possíveis do círculo, não necessariamente o trecho direto calculado.
- Somar `distance[destination]` por engano (incluir a parada de destino no intervalo) — o intervalo correto é `[menor, maior)`, exclusivo no índice maior, pois `distance[i]` representa o trecho ENTRE a parada `i` e a `i+1`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Trecho direto menor | `distance=[1,2,3,4], start=0, destination=1` | 1 | caminho direto (1) é menor que o resto do círculo (9) |
| Volta é mais curta | `distance=[1,2,3,4], start=0, destination=3` | 4 | caminho direto (6) é maior que o resto do círculo (4) |
| start igual a destination | `distance=[1,2,3], start=1, destination=1` | 0 | nenhuma distância a percorrer |
| Duas paradas | `distance=[5,5], start=0, destination=1` | 5 | ambos os sentidos têm distância 5, empate |

## 🔗 Conexões

- Problemas irmãos: [0724] Find Pivot Index (mesma técnica de soma total menos soma parcial), [0238] Product of Array Except Self (mesma ideia de "tudo exceto um trecho")
- No backend: cálculo de distância mínima em rotas circulares (ex.: elevadores, trens circulares, ou redes de anéis em topologias de rede) onde o caminho pode ser percorrido em dois sentidos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
