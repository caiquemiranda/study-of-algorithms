# [0475] Heaters

> 🔗 [LeetCode 475](https://leetcode.com/problems/heaters/) · Dificuldade: 🟡 medium · Categoria: [`05_busca_binaria`](../../../fundamentos/05_busca_binaria.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#BuscaBinaria` `#Array` `#Medium`

## 📜 O Problema

Você tem as posições de `houses` (casas) e `heaters` (aquecedores) numa linha. Todo aquecedor tem o **mesmo raio de aquecimento** `r`, e uma casa é aquecida se estiver a distância `<= r` de pelo menos um aquecedor. Retorne o **menor raio** `r` que garante que **todas** as casas sejam aquecidas.

**Exemplos:**
```
Input:  houses = [1,2,3], heaters = [2]      Output: 1
Input:  houses = [1,2,3,4], heaters = [1,4]  Output: 1
Input:  houses = [1,5], heaters = [2]        Output: 3
```

**Restrições (e o que elas denunciam):**
- `1 <= houses.length, heaters.length <= 3 * 10^4` → força bruta O(n×m) chega a 9×10^8, arriscado; existe algo bem melhor
- "todos os aquecedores seguem o mesmo raio" → o raio final precisa ser suficiente para a **pior casa** (a mais isolada de qualquer aquecedor) — o problema é, no fundo, "ache a maior distância mínima entre uma casa e o aquecedor mais próximo dela"
- Não há garantia de que `houses` ou `heaters` venham ordenados → é preciso ordenar antes de aplicar busca binária

## 🧭 Como reconhecer o padrão

Para cada casa, o raio necessário é a distância até o aquecedor **mais próximo** — e a resposta final é o **máximo** dessas distâncias mínimas (o raio precisa cobrir até a casa mais isolada). "Ache o vizinho mais próximo num array ordenado" é a assinatura clássica de busca binária por fronteira: depois de ordenar `heaters`, para cada casa, ache via busca binária o aquecedor imediatamente antes e o imediatamente depois dela, e compare as duas distâncias.

## 🐢 Solução 1 — Força bruta

Para cada casa, percorrer todos os aquecedores calculando a distância e guardando a menor; depois, tirar o máximo dessas menores distâncias entre todas as casas.

- Tempo: O(n × m) · Espaço: O(1)
- **Por que não basta:** com `n` e `m` até 3×10^4, o produto chega a quase 1 bilhão de comparações — lento demais. Ignora que, ordenando os aquecedores, o vizinho mais próximo de cada casa pode ser achado em O(log m) em vez de O(m).

## 💡 Solução 2 — A ideia otimizada (intuição)

Ordene `heaters`. Para cada casa, faça busca binária (lower bound) pela primeira posição de aquecedor `>= casa`. Compare a distância até esse aquecedor (o "de depois") com a distância até o aquecedor imediatamente **anterior** (o "de antes") — o menor dos dois é a distância mínima que essa casa precisa. A resposta final é o **maior** valor entre essas distâncias mínimas, considerando todas as casas.

## 🎬 Exemplo passo a passo

`houses = [1,2,3,4]`, `heaters` ordenado = `[1, 4]`

Busca binária (lower bound) para a casa `2`:

| Passo | left | mid | right | heaters[mid] | Comparação | Decisão |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 (val 4) | 2 | 4 >= 2 → candidato | `right = 1` |
| 2 | 0 | 0 (val 1) | 1 | 1 < 2 → não serve | `left = 1` |
| 3 | 1 | — | 1 | `left==right` → fim | idx = 1 (heaters[1] = 4) |

Distância até o aquecedor de depois (idx=1, valor 4): `4-2=2` · Distância até o de antes (idx-1=0, valor 1): `2-1=1` · mínimo: `1`

Repetindo para todas as casas: casa 1→0, casa 2→1, casa 3→1, casa 4→0

Resultado final: `max(0,1,1,0) = 1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O((n + m) log m) — ordenar `heaters` custa O(m log m); cada uma das `n` casas faz uma busca binária O(log m)
- **Espaço:** O(log m) a O(m) para o sort

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int findRadius(int[] houses, int[] heaters) {
    Arrays.sort(heaters);            // habilita busca binária por vizinho mais próximo
    int raioNecessario = 0;

    for (int casa : houses) {
        int idx = lowerBound(heaters, casa);   // primeiro aquecedor >= casa

        long distDepois = (idx < heaters.length) ? heaters[idx] - casa : Long.MAX_VALUE;
        long distAntes = (idx > 0) ? casa - heaters[idx - 1] : Long.MAX_VALUE;

        long distMinima = Math.min(distAntes, distDepois);
        raioNecessario = (int) Math.max(raioNecessario, distMinima);
    }
    return raioNecessario;
}

// Lower bound clássico: primeira posição com valor >= alvo.
private int lowerBound(int[] arr, int alvo) {
    int left = 0, right = arr.length;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] < alvo) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
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

- **Esquecer de checar o aquecedor "de antes"**: olhar só o primeiro aquecedor `>= casa` (o lower bound) não basta — o aquecedor imediatamente anterior pode estar mais perto (ver casa=2 no trace, onde o aquecedor de antes, distância 1, vence o de depois, distância 2).
- **Não tratar os limites do array**: se `idx == heaters.length` (nenhum aquecedor `>= casa`) ou `idx == 0` (nenhum aquecedor `< casa`), um dos dois lados não existe — usar um valor "infinito" (`Long.MAX_VALUE`) para esse lado evita comparações inválidas.
- **Confundir "menor distância por casa" com "resposta final"**: a resposta é o **máximo** das menores distâncias — pegar o mínimo por engano faria o raio insuficiente para a casa mais isolada.
- **Esquecer de ordenar `heaters`**: sem ordenar, a busca binária simplesmente não funciona — é fácil esquecer esse passo quando o enunciado não deixa explícito que os arrays vêm desordenados.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Um aquecedor, casas ao redor | `houses=[1,2,3], heaters=[2]` | 1 | aquecedor central, raio mínimo simétrico |
| Casa longe de tudo | `houses=[1,5], heaters=[2]` | 3 | testa a casa mais isolada dominando a resposta |
| Aquecedor e casa na mesma posição | `houses=[1,1,1], heaters=[1]` | 0 | distância zero, nenhum raio necessário |
| Casas nas pontas, aquecedores nas pontas | `houses=[1,2,3,4], heaters=[1,4]` | 1 | trace acima |
| Único aquecedor longe de todas as casas | `houses=[1,2,3,4,5], heaters=[100]` | 99 | testa quando só existe o lado "de antes" |

## 🔗 Conexões

- Problemas irmãos: **[0035] Search Insert Position** (o lower bound usado como bloco de construção aqui), **[1385] Find the Distance Value Between Two Arrays** (mesma ideia de achar vizinho mais próximo via busca binária)
- No backend: alocar recursos com "raio de cobertura" fixo para atender pontos de demanda dispersos (ex.: quantos servidores de CDN, com latência máxima igual, cobrem todas as regiões de usuários) usa exatamente esse raciocínio de "achar a pior distância mínima" via busca binária por vizinho mais próximo.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
