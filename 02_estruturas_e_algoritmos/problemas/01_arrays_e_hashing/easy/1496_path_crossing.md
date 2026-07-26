# [1496] Path Crossing

> 🔗 [LeetCode 1496](https://leetcode.com/problems/path-crossing/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#HashTable` `#String` `#Easy`

## 📜 O Problema

Dada uma string `path`, onde `path[i] = 'N'`, `'S'`, `'E'` ou `'W'` representa mover uma unidade para norte, sul, leste ou oeste respectivamente. Você começa na origem `(0, 0)` num plano 2D e anda pelo caminho especificado por `path`.

Retorne `true` se o caminho cruza a si mesmo em algum ponto, ou seja, se em algum momento você está numa localização já visitada anteriormente. Caso contrário, retorne `false`.

**Exemplos:**
```
Input:  path = "NES"
Output: false
Explicação: o caminho não cruza nenhum ponto mais de uma vez.

Input:  path = "NESWW"
Output: true
Explicação: o caminho visita a origem duas vezes.
```

**Restrições (e o que elas denunciam):**
- `1 <= path.length <= 10^4` → O(n) resolve com folga
- movimentos N/S/E/W → mapeamento direto para deltas de coordenada (dx, dy)

## 🧭 Como reconhecer o padrão

"O caminho cruza a si mesmo" é resolvido rastreando todas as posições já visitadas num hash set de coordenadas, e checando a cada passo se a NOVA posição já está no set — se estiver, já é um cruzamento.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Guardar todas as posições visitadas numa lista, e a cada novo passo, percorrer a lista inteira comparando com a nova posição.

- Tempo: O(n²) — para cada passo, uma varredura da lista de posições já visitadas · Espaço: O(n)
- **Por que não basta:** repete a busca "já visitei esta posição?" O(n) vezes por passo, quando um hash set responde isso em O(1).

## 💡 Solução 2 — A ideia otimizada (intuição)

Mantenha a posição atual `(x, y)` e um hash set de posições visitadas (começando com `(0,0)`). A cada movimento, atualize `(x,y)` conforme a direção, e verifique se essa nova posição já está no set; se estiver, retorne `true` na hora; senão, adicione-a ao set.

## 🎬 Exemplo passo a passo

`path = "NESWW"` — posição inicial `(0,0)`

| Passo | movimento | nova posição | já visitada? | Ação |
|---|---|---|---|---|
| 1 | N | (0,1) | não | adiciona |
| 2 | E | (1,1) | não | adiciona |
| 3 | S | (1,0) | não | adiciona |
| 4 | W | (0,0) | **sim** (é a origem) | retorna true |

Resultado final: `true` ✔ (a origem é revisitada)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada
- **Espaço:** O(n) — para o set de posições

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isPathCrossing(String path) {
    Set<Long> visitadas = new HashSet<>();
    int x = 0, y = 0;
    visitadas.add(codificar(x, y)); // a origem já conta como visitada

    for (char dir : path.toCharArray()) {
        switch (dir) {
            case 'N' -> y++;
            case 'S' -> y--;
            case 'E' -> x++;
            case 'W' -> x--;
        }
        long codigo = codificar(x, y);
        if (!visitadas.add(codigo)) {
            return true; // add() retorna false se a posição já existia no set
        }
    }
    return false;
}

private long codificar(int x, int y) {
    // combina x e y numa única chave numérica sem colisão, deslocando x para os bits altos
    return ((long) x << 32) ^ (y & 0xFFFFFFFFL);
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

- Esquecer de adicionar a posição INICIAL `(0,0)` ao set antes de começar a andar — o caminho pode voltar para a origem, que já conta como "visitada" desde o início.
- Usar uma `String` como chave (ex.: `x + "," + y`) em vez de uma codificação numérica — funciona, mas gasta mais memória e é mais lento para hashear do que um `long` codificado.
- Não tratar corretamente coordenadas negativas na codificação — usar concatenação de string ingênua pode confundir posições diferentes; a codificação com deslocamento de bits evita essa ambiguidade.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem cruzamento | "NES" | false | caminho nunca revisita uma posição |
| Cruzamento na origem | "NESWW" | true | volta para (0,0) |
| Caminho de ida e volta simples | "NS" | true | volta imediatamente para a origem |
| Um único passo | "N" | false | só duas posições, nunca repetidas |

## 🔗 Conexões

- Problemas irmãos: [0657] Robot Return to Origin (mesmo domínio de simulação de movimento em grade), [1041] Robot Bounded In Circle (mesma família de simulação de robô com direções)
- No backend: detecção de ciclos em trajetórias de movimento (ex.: rastreamento de veículos ou robôs que retornam a um ponto já visitado, útil em otimização de rotas).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
