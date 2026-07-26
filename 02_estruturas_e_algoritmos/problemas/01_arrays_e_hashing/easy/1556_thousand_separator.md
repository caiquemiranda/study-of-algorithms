# [1556] Thousand Separator

> 🔗 [LeetCode 1556](https://leetcode.com/problems/thousand-separator/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Dado um inteiro `n`, adicione um ponto (".") como separador de milhar e retorne em formato de string.

**Exemplos:**
```
Input:  n = 987
Output: "987"

Input:  n = 1234
Output: "1.234"
```

**Restrições (e o que elas denunciam):**
- `0 <= n <= 2^31 - 1` → valores grandes, cabe em `int`, mas a string resultante pode ter vários pontos
- separador é `.` (não vírgula) → específico deste problema

## 🧭 Como reconhecer o padrão

"Inserir um separador a cada K dígitos, contando a partir do FIM do número" é o mesmo padrão de [0482] License Key Formatting: construir de trás para frente, inserindo o separador a cada 3 dígitos processados.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Converter `n` para string, e então, da esquerda para a direita, calcular em qual posição inserir cada ponto usando aritmética de módulo sobre o tamanho total da string.

- Tempo: O(d) onde d é o número de dígitos (bem pequeno) · Espaço: O(d)
- **Por que vale nomear mesmo assim:** calcular a posição do separador da esquerda para a direita exige saber o tamanho total primeiro (`tamanho % 3`), enquanto construir de trás para frente elimina essa conta.

## 💡 Solução 2 — A ideia otimizada (intuição)

Converta `n` para string. Percorra de trás para frente com um contador de dígitos processados; a cada 3 dígitos, insira um `.` antes de continuar.

## 🎬 Exemplo passo a passo

`n = 1234` → string "1234", processando de trás para frente: 4,3,2,1

| Passo | dígito | contador antes | Ação | resultado (construído de trás pra frente) |
|---|---|---|---|---|
| 1 | 4 | 0 | acrescenta, contador=1 | 4 |
| 2 | 3 | 1 | acrescenta, contador=2 | 43 |
| 3 | 2 | 2 | acrescenta, contador=3 | 432 |
| 4 | 1 | 3 | contador==3: insere '.', reseta; acrescenta '1', contador=1 | 432.1 |

Invertendo o resultado: `"432.1"` invertido = `"1.234"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(d) — d = número de dígitos
- **Espaço:** O(d)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String thousandSeparator(int n) {
    String digitos = String.valueOf(n);
    StringBuilder resultado = new StringBuilder();
    int contador = 0;

    for (int i = digitos.length() - 1; i >= 0; i--) {
        if (contador == 3) {
            resultado.append('.'); // fecha um grupo de 3 antes de começar o próximo
            contador = 0;
        }
        resultado.append(digitos.charAt(i));
        contador++;
    }
    return resultado.reverse().toString(); // foi construído de trás para frente
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

- Construir da esquerda para a direita sem calcular antecipadamente `tamanho % 3` — obriga a uma conta extra para saber onde cai o primeiro separador; construir do fim evita isso.
- Esquecer o caso `n = 0` — a string "0" tem só 1 dígito, sem necessidade de separador nenhum; o código já lida com isso naturalmente.
- Confundir o separador de milhar (`.`) com separador decimal — este problema não lida com casas decimais, `n` é sempre um inteiro.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Sem separador necessário | 987 | "987" | menos de 4 dígitos, nenhum ponto |
| Um separador | 1234 | "1.234" | caso padrão do enunciado |
| Múltiplos separadores | 1234567 | "1.234.567" | vários grupos de 3 |
| Zero | 0 | "0" | caso de borda mínimo |

## 🔗 Conexões

- Problemas irmãos: [0482] License Key Formatting (mesma técnica de construir de trás para frente inserindo separador a cada K caracteres), [0038] Count and Say (mesmo domínio de construção de string com `StringBuilder`)
- No backend: formatação de valores monetários ou grandes números para exibição em interfaces de usuário (ex.: exibir "R$ 1.234.567,89" em vez do número cru).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
