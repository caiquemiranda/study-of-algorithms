# [2337] Move Pieces to Obtain a String

> 🔗 [LeetCode 2337](https://leetcode.com/problems/move-pieces-to-obtain-a-string/) · Dificuldade: 🟡 medium · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#String` `#Medium`

## 📜 O Problema

Dadas `start` e `target` (mesma string de `'L'`, `'R'`, `'_'`), `'L'` só se move pra esquerda (se houver espaço em branco `'_'` ali do lado), `'R'` só pra direita. Retorne se dá pra transformar `start` em `target` com algum número de movimentos.

**Exemplos:**
```
Input:  start = "_L__R__R_", target = "L______RR"
Output: true

Input:  start = "R_L_", target = "__LR"
Output: false

Input:  start = "_R", target = "R_"
Output: false
Explicação: 'R' só pode ir pra direita, mas precisaria ir pra esquerda.
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 10^5` → O(n) esperado, simular movimento por movimento seria inviável
- `'L'` e `'R'` nunca conseguem se ultrapassar (um bloqueia o outro) → a **ordem relativa** das peças é um invariante — se muda, é impossível
- Cada peça só anda numa direção → a posição final de cada peça tem um limite (não pode "ir contra o próprio sentido")

## 🧭 Como reconhecer o padrão

"Comparar duas sequências ignorando um caractere coringa, verificando também uma restrição de direção posição a posição" combina a ideia de [0392] Is Subsequence (dois ponteiros pulando caracteres irrelevantes) com uma checagem extra: como `'L'`/`'R'` nunca se cruzam, a sequência de peças (ignorando `'_'`) tem que ser **idêntica** entre `start` e `target`, e a posição de cada peça só pode mudar na direção que ela tem permissão de mover.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simular todas as sequências possíveis de movimentos (busca em largura sobre o espaço de configurações alcançáveis a partir de `start`), verificando se `target` é alcançável.

- Tempo: exponencial no pior caso — o número de configurações intermediárias possíveis explode rapidamente
- **Por que não basta:** o espaço de estados é gigantesco mesmo para strings moderadas. A observação-chave é que `'L'`s e `'R'`s nunca podem se ultrapassar (ordem relativa é invariante), então basta comparar a sequência de peças ignorando os espaços, com uma checagem de direção por peça — tudo numa única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use `i` em `start` e `j` em `target`, ambos pulando `'_'` antes de cada comparação. Se as duas strings esgotarem juntas, terminou com sucesso. Se uma esgotar antes da outra, as contagens de peças são diferentes — `false`. Compare a peça atual: se forem tipos diferentes (`'L'` vs `'R'`), `false`. Se for `'L'`, a posição em `target` (`j`) precisa ser `<= i` (só anda pra esquerda). Se for `'R'`, precisa ser `>= i` (só anda pra direita). Avance os dois ponteiros e repita.

## 🎬 Exemplo passo a passo

`start = "_L__R__R_"`, `target = "L______RR"` (n=9)

| Passo | i (após pular `_`) | j (após pular `_`) | Peça | Checagem de direção | Ação |
|---|---|---|---|---|---|
| 1 | 1 (`L`) | 0 (`L`) | `L` | posição final `0 <= 1` (moveu p/ esquerda) ✔ | avança: i=2, j=1 |
| 2 | 4 (`R`) | 7 (`R`) | `R` | posição final `7 >= 4` (moveu p/ direita) ✔ | avança: i=5, j=8 |
| 3 | 7 (`R`) | 8 (`R`) | `R` | posição final `8 >= 7` ✔ | avança: i=8, j=9 |
| 4 | 9 (fim) | 9 (fim) | — | ambos esgotaram juntos | **retorna true** |

Resultado final: `true` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — os dois ponteiros juntos percorrem cada string uma única vez
- **Espaço:** O(1) — só os índices `i` e `j`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean canChange(String start, String target) {
    int n = start.length();
    int i = 0;
    int j = 0;

    while (i < n || j < n) {
        while (i < n && start.charAt(i) == '_') i++;
        while (j < n && target.charAt(j) == '_') j++;

        if (i == n && j == n) {
            break; // os dois esgotaram juntos: nenhuma peça sobrando pra comparar
        }
        if (i == n || j == n) {
            return false; // um esgotou antes do outro: quantidade de peças diferente
        }
        if (start.charAt(i) != target.charAt(j)) {
            return false; // sequência de peças (ignorando '_') precisa ser idêntica
        }
        if (start.charAt(i) == 'L' && i < j) {
            return false; // 'L' só anda pra esquerda: posição final não pode ser maior
        }
        if (start.charAt(i) == 'R' && i > j) {
            return false; // 'R' só anda pra direita: posição final não pode ser menor
        }

        i++;
        j++;
    }

    return true;
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

- Comparar `start` e `target` posição a posição incluindo os `'_'` — os espaços podem se redistribuir livremente; o que importa é a sequência de `L`/`R` ignorando `_`, mais a direção de cada movimento.
- Inverter a checagem de direção — `'L'` só vai pra ESQUERDA (posição final `<=` original); `'R'` só pra DIREITA (posição final `>=` original); trocar as condições inverte a lógica.
- Esquecer de checar se as duas strings esgotam JUNTAS — se sobrar peça numa mas não na outra, as contagens de `L`/`R` são diferentes, e a resposta tem que ser `false`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Movimentos válidos | `start="_L__R__R_"`, `target="L______RR"` | true | `L` move esquerda, `R`s movem direita, tudo dentro das regras |
| Ordem bloqueada | `start="R_L_"`, `target="__LR"` | false | `R` não consegue passar por cima do `L` pra chegar na posição final |
| Direção errada | `start="_R"`, `target="R_"` | false | `R` só pode ir pra direita, mas precisaria ir pra esquerda |
| Já são iguais | `start="LR"`, `target="LR"` | true | nenhum movimento necessário |

## 🔗 Conexões

- Problemas irmãos: [0392] Is Subsequence (mesma ideia de comparar duas sequências ignorando certos caracteres), [1963] Minimum Number of Swaps to Make the String Balanced (mesma família de validar uma propriedade estrutural de uma string com uma passada linear)
- No backend: validar se um estado de sistema é alcançável a partir de outro respeitando regras de precedência que nunca podem ser violadas — por exemplo, verificar se uma reordenação de uma fila de processamento é válida quando itens só podem avançar ou atrasar, nunca ultrapassar uns aos outros.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
