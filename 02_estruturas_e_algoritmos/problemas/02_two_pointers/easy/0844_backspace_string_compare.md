# [0844] Backspace String Compare

> 🔗 [LeetCode 844](https://leetcode.com/problems/backspace-string-compare/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#String` `#Stack` `#Simulation` `#Easy`

## 📜 O Problema

Dadas duas strings `s` e `t`, retorne `true` se elas ficarem iguais depois de digitadas num editor de texto vazio, onde `'#'` representa uma tecla de backspace (apaga o caractere anterior; num texto já vazio, o backspace não faz nada).

**Exemplos:**
```
Input:  s = "ab#c", t = "ad#c"
Output: true
Explicação: as duas ficam "ac".

Input:  s = "ab##", t = "c#d#"
Output: true
Explicação: as duas ficam "".

Input:  s = "a#c", t = "b"
Output: false
Explicação: s fica "c", t fica "b".
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length, t.length <= 200` → tamanho pequeno, mas o follow-up pede O(n) tempo e **O(1) espaço**, o que descarta materializar a string final
- `s` e `t` só têm letras minúsculas e `'#'` → sem outros caracteres especiais a considerar

## 🧭 Como reconhecer o padrão

"Simular backspaces sem construir o texto final" é resolvido processando a string **de trás para frente** com dois ponteiros: um `'#'` só afeta o que vem **antes** dele, então andar do fim pro início permite decidir, character por character, se ele "sobrevive" aos apagamentos sem precisar saber o texto completo já processado.

## 🐢 Solução 1 — Força bruta (com pilha)

Para cada string, percorrer da esquerda pra direita usando uma pilha: empilhar cada letra, e ao encontrar `'#'`, desempilhar (se a pilha não estiver vazia). Ao final, comparar as duas pilhas/strings resultantes.

- Tempo: O(n) · Espaço: O(n) — a pilha guarda até n caracteres por string
- **Por que não basta:** já é O(n) em tempo, mas usa O(n) de espaço para materializar o texto final; o follow-up pede explicitamente O(1) de espaço extra, o que exige processar sem montar a string resultante.

## 💡 Solução 2 — A ideia otimizada (intuição)

Use um ponteiro em cada string, começando no **último** caractere. Para achar o próximo caractere "válido" (que sobrevive aos backspaces) andando pra trás, conte quantos `'#'` você encontra (variável `skip`): cada `'#'` significa que o próximo caractere não-`'#'` encontrado deve ser pulado também. Compare os caracteres válidos das duas strings um a um; se algum par for diferente, ou se uma string acabar antes da outra, elas não são iguais.

## 🎬 Exemplo passo a passo

`s = "ab#c"`, `t = "ad#c"` (índices 0 a 3 em cada)

| Passo | Posição em s | Caractere efetivo | Posição em t | Caractere efetivo | Igual? | Ação |
|---|---|---|---|---|---|---|
| 1 | i=3 (nenhum `#` a processar) | `c` | j=3 (nenhum `#`) | `c` | sim | avança: i=2, j=2 |
| 2 | i=2 → pula `#` e o `b` que ele apaga → chega em i=0 | `a` | j=2 → pula `#` e o `d` que ele apaga → chega em j=0 | `a` | sim | avança: i=-1, j=-1 |
| 3 | i=-1 | — | j=-1 | — | ambos esgotaram juntos | loop termina, **true** |

Resultado final: `true` ✔ (ambas equivalem a `"ac"`, como no enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — cada string é percorrida uma única vez, de trás para frente
- **Espaço:** O(1) — só os índices e o contador `skip`, sem construir nenhuma string nova

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean backspaceCompare(String s, String t) {
    int i = s.length() - 1;
    int j = t.length() - 1;

    while (i >= 0 || j >= 0) {
        i = proximoValido(s, i);
        j = proximoValido(t, j);

        if (i < 0 && j < 0) {
            return true; // as duas esgotaram ao mesmo tempo, sem nenhum mismatch
        }
        if (i < 0 || j < 0) {
            return false; // uma esgotou antes da outra: tamanhos efetivos diferentes
        }
        if (s.charAt(i) != t.charAt(j)) {
            return false;
        }
        i--;
        j--;
    }

    return true;
}

private int proximoValido(String str, int idx) {
    int skip = 0;
    while (idx >= 0) {
        if (str.charAt(idx) == '#') {
            skip++; // este # vai apagar o próximo caractere não-# encontrado
            idx--;
        } else if (skip > 0) {
            skip--; // este caractere foi "consumido" por um # anterior
            idx--;
        } else {
            break; // achou um caractere que sobrevive aos backspaces
        }
    }
    return idx;
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

- Usar uma pilha para montar a string final e comparar — funciona, mas gasta O(n) de espaço extra; o follow-up pede O(1), só possível processando de trás pra frente sem materializar o resultado.
- Achar que cada `'#'` só apaga UM caractere isoladamente — múltiplos `'#'` consecutivos acumulam múltiplos apagamentos (`skip` pode chegar a mais de 1), e é preciso "descontar" um apagamento por vez a cada caractere não-`'#'` encontrado.
- Parar a comparação assim que uma das strings "esgotar" sem checar se a outra também esgotou — se `i` chega a -1 mas `j` ainda tem caractere válido sobrando, as strings efetivas têm tamanhos diferentes e não podem ser iguais.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Iguais após backspace | `s="ab#c"`, `t="ad#c"` | true | ambas resultam em `"ac"` |
| Ambas vazias no final | `s="ab##"`, `t="c#d#"` | true | os `#` apagam tudo, ambas ficam `""` |
| Tamanhos efetivos diferentes | `s="a#c"`, `t="b"` | false | `s` vira `"c"`, `t` continua `"b"` |
| Excesso de `#` no início | `s="###a"`, `t="a"` | true | `#` num texto já vazio não tem efeito nenhum |

## 🔗 Conexões

- Problemas irmãos: [0071] Simplify Path (mesma ideia de "desfazer" elementos usando uma pilha, aplicada a diretórios em vez de backspace), [0682] Baseball Game (também processa uma sequência de comandos que podem desfazer entradas anteriores)
- No backend: comparar dois resultados de um log de edições com comandos de desfazer (undo), sem precisar materializar o estado final de cada lado — só o suficiente para responder "são iguais?".

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
