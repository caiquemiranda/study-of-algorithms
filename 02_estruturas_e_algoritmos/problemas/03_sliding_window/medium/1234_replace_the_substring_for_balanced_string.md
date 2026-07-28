# [1234] Replace the Substring for Balanced String

> 🔗 [LeetCode 1234](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) · Dificuldade: 🟡 medium · Categoria: [`03_sliding_window`](../../../fundamentos/03_sliding_window.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#SlidingWindow` `#Medium`

## 📜 O Problema

Dada uma string `s` de comprimento `n` contendo só os caracteres `'Q'`, `'W'`, `'E'` e `'R'`, ela é **balanceada** se cada caractere aparece exatamente `n/4` vezes. Retorne o comprimento mínimo de uma substring que pode ser substituída por qualquer outra string do mesmo tamanho para tornar `s` balanceada. Se `s` já é balanceada, retorne `0`.

**Exemplos:**
```
Input:  s = "QWER"
Output: 0
Explicação: já é balanceada.

Input:  s = "QQWE"
Output: 1
Explicação: trocar um 'Q' por 'R' resolve.

Input:  s = "QQQW"
Output: 2
Explicação: trocar "QQ" (os dois primeiros) por "ER" resolve.
```

**Restrições (e o que elas denunciam):**
- `n == s.length`, `4 <= n <= 10^5`, `n` é múltiplo de 4 → o alvo `n/4` é sempre um inteiro exato
- `s` contém só `'Q'`, `'W'`, `'E'`, `'R'` → alfabeto de 4 símbolos, fácil de mapear em contadores fixos

## 🧭 Como reconhecer o padrão

"Menor substring cuja substituição resolve um desbalanceamento" é resolvido pensando ao contrário: a janela representa o trecho que será SUBSTITUÍDO, então o que importa é o que **sobra fora** dela — encontre a menor janela tal que, removendo-a, todo caractere restante em `s` apareça no máximo `n/4` vezes (o excesso "sai" junto com a janela).

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada par `(left, right)`, checar se remover essa janela deixa as contagens de fora dentro do limite, recalculando do zero a cada tentativa.

- Tempo: O(n³) · Espaço: O(1)
- **Por que não basta:** revalida as contagens do zero a cada substring candidata, mesmo quando ela é apenas a anterior estendida em um elemento.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte a frequência total de cada caractere em `s`. Se já são todas `<= n/4`, retorne `0`. Senão, deslize uma janela variável: expanda pela direita incrementando a contagem DENTRO da janela; encolha pela esquerda enquanto a janela ainda for válida (ou seja, `freq[c] - window[c] <= n/4` para TODOS os 4 caracteres), registrando o menor comprimento válido a cada encolhimento.

## 🎬 Exemplo passo a passo

`s = "QQWE"` (n=4, alvo=1). Frequências totais: Q=2, W=1, E=1, R=0. Q>alvo → não balanceada, proceder.

| right | char | window (Q,W,E,R) | Válido (sobra fora <= n/4 pra todos)? | Encolhe | left final | comprimento válido | melhor |
|---|---|---|---|---|---|---|---|
| 0 | Q | (1,0,0,0) | sim | remove s[0]=Q → (0,0,0,0), left=1 | 1 | 1 | 1 |
| 1 | Q | (1,0,0,0) | sim | remove s[1]=Q → (0,0,0,0), left=2 | 2 | 1 | 1 |
| 2 | W | (0,1,0,0) | não (Q fora=2>1) | — | 2 | — | 1 |
| 3 | E | (0,1,1,0) | não (Q fora=2>1) | — | 2 | — | 1 |

Resultado final: `1` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — `right` e `left` cada um avança no máximo `n` vezes
- **Espaço:** O(1) — contadores fixos de 4 caracteres

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int balancedString(String s) {
    int n = s.length();
    int target = n / 4;
    int[] freq = new int[4]; // Q, W, E, R
    for (char c : s.toCharArray()) {
        freq[charIndex(c)]++;
    }

    if (freq[0] <= target && freq[1] <= target && freq[2] <= target && freq[3] <= target) {
        return 0; // já balanceada
    }

    int[] window = new int[4];
    int left = 0;
    int best = n;

    for (int right = 0; right < n; right++) {
        window[charIndex(s.charAt(right))]++;

        while (left <= right && isValid(freq, window, target)) {
            best = Math.min(best, right - left + 1);
            window[charIndex(s.charAt(left))]--;
            left++;
        }
    }

    return best;
}

private boolean isValid(int[] freq, int[] window, int target) {
    for (int i = 0; i < 4; i++) {
        if (freq[i] - window[i] > target) {
            return false; // sobra desse caractere FORA da janela ainda excede o limite
        }
    }
    return true;
}

private int charIndex(char c) {
    return switch (c) {
        case 'Q' -> 0;
        case 'W' -> 1;
        case 'E' -> 2;
        default -> 3; // 'R'
    };
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

- A condição de validade é sobre o que fica FORA da janela (`freq[c] - window[c] <= target`), não sobre o que está dentro — a janela representa o trecho a ser SUBSTITUÍDO, então o que sobra fora é que precisa estar balanceado.
- Checar todos os 4 caracteres a cada validação é obrigatório — uma janela pode resolver o excesso de `Q` mas ainda deixar `W` desbalanceado fora dela.
- Se a string já é balanceada (`freq[c] <= target` para todos), a resposta é `0` diretamente — esse atalho evita processar o loop principal sem necessidade.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Já balanceada | `"QWER"` | 0 | cada caractere já aparece exatamente n/4=1 vez |
| Um caractere dominando levemente | `"QQWE"` | 1 | substituir um único 'Q' resolve |
| Um caractere dominando fortemente | `"QQQW"` | 2 | substituir "QQ" por "ER" resolve |
| Todos do mesmo caractere | `"QQQQ"` (n=4) | 3 | precisa substituir 3 dos 4 'Q's para balancear |

## 🔗 Conexões

- Problemas irmãos: [0424] Longest Repeating Character Replacement (mesma técnica de janela deslizante com validação sobre contagens, mas maximizando em vez de minimizar), [0076] Minimum Window Substring (mesma família de encontrar a MENOR janela que satisfaz uma condição de composição de caracteres)
- No backend: calcular o menor trecho de configuração que precisa ser reescrito para que a distribuição de categorias (tipos de requisição, tiers de usuário) volte a ficar dentro de um limite balanceado esperado.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
