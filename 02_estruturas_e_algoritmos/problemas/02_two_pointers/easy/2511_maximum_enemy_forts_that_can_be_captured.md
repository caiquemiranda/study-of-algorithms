# [2511] Maximum Enemy Forts That Can Be Captured

> 🔗 [LeetCode 2511](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array `forts` onde `-1` é posição vazia, `0` é forte inimigo e `1` é seu forte, você pode mover seu exército de uma posição `i` (sua) até uma posição `j` **vazia**, desde que **todo** o trecho estritamente entre `i` e `j` seja só fortes inimigos (`0`). Todo inimigo no caminho é capturado. Retorne o número **máximo** de inimigos capturáveis numa única movimentação (`0` se nenhuma movimentação for possível).

**Exemplos:**
```
Input:  forts = [1,0,0,-1,0,0,0,0,1]
Output: 4
Explicação: mover de 8 até 3 captura os 4 inimigos entre eles.

Input:  forts = [0,0,1,-1]
Output: 0
```

**Restrições (e o que elas denunciam):**
- `1 <= forts.length <= 1000` → O(n²) já passaria, mas O(n) é natural
- Valores só `-1`, `0` ou `1` → só existem dois tipos de "marcador de fronteira" (`1` e `-1`); tudo o mais é `0` (potencial capturável)
- O caminho precisa ser **só** inimigos → qualquer `1` ou `-1` no meio do trecho invalida a travessia

## 🧭 Como reconhecer o padrão

"Encontrar o maior trecho de zeros entre dois marcadores de tipos opostos" é resolvido rastreando, numa única passada, apenas o marcador (`1` ou `-1`) **mais recente** visto: sempre que aparece outro marcador, se ele for do tipo **oposto** ao anterior, o trecho entre os dois é garantidamente só inimigos (não podia haver outro marcador no meio, senão ele teria sido o "mais recente" antes deste).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(i, j)` com `forts[i] == 1` e `forts[j] == -1`, verificar se todo o trecho entre eles é só zeros (varrendo o trecho inteiro), contando os zeros se for válido.

- Tempo: O(n²) no pior caso — n candidatos de `i`, cada verificação percorre até `n` posições · Espaço: O(1)
- **Por que não basta:** testa pares de posições que muitas vezes nem poderiam formar um caminho válido (havendo outro marcador no meio); rastrear só o marcador mais recente numa única passada já garante que todo candidato considerado é automaticamente válido, sem precisar reverificar o trecho.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `forts` guardando o índice e o valor do último marcador (`1` ou `-1`) encontrado. Toda vez que encontrar um novo marcador, se ele for do **tipo oposto** ao anterior, o trecho estritamente entre os dois é só inimigos — atualize o máximo com o tamanho desse trecho (`i - anterior - 1`). Se for do mesmo tipo (dois `1`s ou dois `-1`s seguidos sem oposto no meio), não há travessia válida ali, só atualize o marcador "mais recente".

## 🎬 Exemplo passo a passo

`forts = [1,0,0,-1,0,0,0,0,1]`

| Passo | i | forts[i] | marcador anterior | Ação |
|---|---|---|---|---|
| 1 | 0 | 1 | nenhum ainda | primeiro marcador, guarda (0, 1); sem candidato |
| 2 | 3 | -1 | (0, 1) | tipos diferentes → candidato = `3-0-1=2` zeros; guarda (3, -1) |
| 3 | 8 | 1 | (3, -1) | tipos diferentes → candidato = `8-3-1=4` zeros; guarda (8, 1) |

Máximo final: `max(2, 4) = 4` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada pelo array
- **Espaço:** O(1) — só o índice e o valor do último marcador visto

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int captureForts(int[] forts) {
    int n = forts.length;
    int prevIdx = -1; // -1 = ainda não vimos nenhum marcador (1 ou -1)
    int prevVal = 0;
    int maxCaptured = 0;

    for (int i = 0; i < n; i++) {
        if (forts[i] == 0) {
            continue; // posição de inimigo: parte de um possível caminho, não é marcador
        }
        if (prevIdx != -1 && prevVal != forts[i]) {
            // marcador anterior era do tipo oposto: o trecho entre eles é só inimigos
            maxCaptured = Math.max(maxCaptured, i - prevIdx - 1);
        }
        prevIdx = i;
        prevVal = forts[i];
    }

    return maxCaptured;
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

- Contar como candidato válido um trecho entre dois marcadores do MESMO tipo (dois `1`s ou dois `-1`s seguidos) — não é uma travessia válida; o exército só se move entre um forte seu (`1`) e uma posição vazia (`-1`), nunca entre dois do mesmo tipo.
- Confundir `-1` com "posição inválida/fora dos limites" — aqui `-1` significa "posição vazia", um destino perfeitamente válido para a movimentação.
- Testar todos os pares `(i, j)` e reverificar o trecho inteiro a cada vez — desperdiça trabalho; como só o marcador mais recente importa para formar um caminho válido, uma única passada já é suficiente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo do enunciado | `[1,0,0,-1,0,0,0,0,1]` | 4 | maior trecho de zeros entre marcadores opostos |
| Sem captura possível | `[0,0,1,-1]` | 0 | o `1` só aparece depois dos zeros, sem marcador oposto antes dele |
| Marcadores adjacentes (sem zeros) | `[1,-1]` | 0 | nenhum inimigo no meio, 0 capturas |
| Sem posição vazia disponível | `[1,0,0,0]` | 0 | nenhum `-1` no array pra completar o caminho |

## 🔗 Conexões

- Problemas irmãos: [0821] Shortest Distance to a Character (mesma técnica de rastrear a ocorrência mais recente de um marcador numa única passada), [0011] Container With Most Water (mesma família de maximizar uma métrica entre dois marcadores de um array)
- No backend: encontrar o maior intervalo "capturável" entre dois eventos de fronteira num log sequencial — por exemplo, a maior sequência de eventos neutros entre dois eventos de tipos opostos, como transições de estado "ligado"/"desligado" com eventos neutros no meio.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
