# [0482] License Key Formatting

> 🔗 [LeetCode 482](https://leetcode.com/problems/license-key-formatting/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Formatting` `#Easy`

## 📜 O Problema

Você recebe uma chave de licença `s`, formada apenas por caracteres alfanuméricos e traços, separada em `n + 1` grupos por `n` traços, e um inteiro `k`. Reformate `s` para que cada grupo tenha exatamente `k` caracteres, exceto o primeiro grupo, que pode ser menor que `k` mas precisa ter pelo menos um caractere. Deve haver um traço entre dois grupos, e todas as letras minúsculas devem virar maiúsculas.

**Exemplos:**
```
Input:  s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explicação: os dois traços extras não eram necessários e foram removidos.

Input:  s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explicação: o primeiro grupo pode ser mais curto, os demais têm exatamente 2 caracteres.
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 10^5` → precisa de O(n); concatenar `String` dentro de um loop em Java seria quadrático
- "converter minúsculas em maiúsculas" → precisa de uma normalização de caixa durante a reconstrução
- `1 <= k <= 10^4` → o grupo pode ser maior que a própria string sem os traços, formando um único grupo

## 🧭 Como reconhecer o padrão

"Reformatar em grupos de tamanho fixo, onde o primeiro grupo pode ser menor" é um sinal para construir a string **de trás para frente** (do sufixo para o prefixo), porque o tamanho do primeiro grupo só é conhecido depois de saber quantos caracteres sobram no total.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Remover os traços, guardar os caracteres válidos, calcular `total % k` para saber o tamanho do primeiro grupo, e então construir a string final por concatenação de `String` da esquerda para a direita, inserindo `-` a cada `k` caracteres.

- Tempo: O(n²) se usar concatenação de `String` repetida em Java (cada `+=` cria uma nova string imutável) · Espaço: O(n)
- **Por que não basta:** para n=10^5, o custo quadrático de concatenar strings dentro de um loop chega a 10^10 operações no pior caso — inviável.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra os caracteres válidos **de trás para frente** com um `StringBuilder`, inserindo um `-` a cada `k` caracteres adicionados. Ao final, inverta o `StringBuilder` (porque ele foi construído de trás para frente). Construir do fim evita ter que calcular antecipadamente o tamanho do primeiro grupo: o "resto" sobra naturalmente no início depois da inversão.

## 🎬 Exemplo passo a passo

`s = "5F3Z-2e-9-w"`, `k = 4` — processando de trás para frente, ignorando os traços originais (ordem processada: w, 9, e, 2, Z, 3, F, 5)

| Passo | char (orig) | count antes | Ação | sb (acumulado) |
|---|---|---|---|---|
| 1 | w | 0 | append 'W', count=1 | W |
| 2 | 9 | 1 | append '9', count=2 | W9 |
| 3 | e | 2 | append 'E', count=3 | W9E |
| 4 | 2 | 3 | append '2', count=4 | W9E2 |
| 5 | Z | 4 | count==k: append '-', reset; append 'Z', count=1 | W9E2-Z |
| 6 | 3 | 1 | append '3', count=2 | W9E2-Z3 |
| 7 | F | 2 | append 'F', count=3 | W9E2-Z3F |
| 8 | 5 | 3 | append '5', count=4 | W9E2-Z3F5 |

`sb.reverse()` = `"5F3Z-2E9W"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma única passada mais um reverse final
- **Espaço:** O(n) — para o `StringBuilder` de saída

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String licenseKeyFormatting(String s, int k) {
    StringBuilder sb = new StringBuilder();
    int count = 0;
    // percorre de trás para frente: o último grupo (processado primeiro) é sempre completo,
    // então contar a partir do fim garante que só o primeiro grupo (formado por último) fica menor
    for (int i = s.length() - 1; i >= 0; i--) {
        char c = s.charAt(i);
        if (c == '-') {
            continue; // traços originais são descartados, serão reinseridos do zero
        }
        if (count == k) {
            sb.append('-'); // fecha um grupo completo antes de começar o próximo
            count = 0;
        }
        sb.append(Character.toUpperCase(c));
        count++;
    }
    return sb.reverse().toString(); // foi construído de trás para frente, precisa inverter
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

- Construir da esquerda para a direita — obriga a calcular `total % k` antecipadamente para saber o tamanho do primeiro grupo; construir do fim para o início evita essa conta porque o "resto" sobra naturalmente no início depois do reverse.
- Esquecer de pular os traços originais (`-`) ao contar caracteres — eles não contam para o tamanho do grupo, só marcam onde estavam os separadores antigos (que serão descartados).
- Usar concatenação de `String` (`+=`) em vez de `StringBuilder` dentro do loop — quadrático para strings grandes.
- Deixar um traço sobrando no início do resultado — só acontece se a checagem `count == k` for feita depois do append em vez de antes; a ordem "checa, depois adiciona" evita traço solto na ponta.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Exemplo com grupos exatos | `s="5F3Z-2e-9-w", k=4` | "5F3Z-2E9W" | caso padrão do enunciado |
| Primeiro grupo menor | `s="2-5g-3-J", k=2` | "2-5G-3J" | primeiro grupo sobra com 1 caractere |
| Sem traços originais | `s="abcdefgh", k=3` | "AB-CDE-FGH" | precisa inserir traços do zero |
| k maior que o total de caracteres | `s="a-a-a", k=10` | "AAA" | um único grupo, sem traço nenhum |

## 🔗 Conexões

- Problemas irmãos: [0038] Count and Say (mesma ideia de reconstruir string com `StringBuilder` em vez de concatenação), [0043] Multiply Strings (processamento de string de trás para frente por causa de "vai um"/carry)
- No backend: formatação de números de cartão, CPF, ou chaves de licença de software em sistemas de faturamento — sempre que um identificador precisa ser exibido em blocos fixos com separador.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
