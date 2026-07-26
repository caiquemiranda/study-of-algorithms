# [0709] To Lower Case

> 🔗 [LeetCode 709](https://leetcode.com/problems/to-lower-case/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Dada uma string `s`, retorne **a string após substituir cada letra maiúscula pela mesma letra minúscula**.

**Exemplos:**
```
Input:  s = "Hello"
Output: "hello"

Input:  s = "here"
Output: "here"

Input:  s = "LOVELY"
Output: "lovely"
```

**Restrições (e o que elas denunciam):**
- `1 <= s.length <= 100` → entrada minúscula, qualquer O(n) resolve tranquilamente
- "printable ASCII characters" → precisa lidar com caracteres que já não são letras maiúsculas (dígitos, pontuação, minúsculas) sem alterá-los

## 🧭 Como reconhecer o padrão

"Transforme cada caractere seguindo uma regra local e independente dos outros" é sempre uma única passada, caractere a caractere, sem precisar de estrutura de dados auxiliar — é o tipo de problema que existe para você conhecer a aritmética de caracteres (ASCII) da sua linguagem, não para testar um algoritmo sofisticado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar diretamente o método pronto da linguagem (`s.toLowerCase()` em Java) — é uma solução válida e O(n), mas não demonstra entendimento da manipulação de caracteres que o problema quer ensinar.

- Tempo: O(n) (o método da biblioteca já é eficiente) · Espaço: O(n) para a nova string
- **Por que não basta:** não é errado em complexidade, mas depende de uma função pronta que esconde a lógica; a versão didática do problema é fazer a conversão manualmente, entendendo a diferença fixa entre `'A'` e `'a'` na tabela ASCII.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra cada caractere; se ele estiver entre `'A'` e `'Z'`, some a diferença fixa `('a' - 'A')` para convertê-lo à minúscula correspondente; caso contrário, mantenha-o como está.

## 🎬 Exemplo passo a passo

`s = "Hello"`

| Passo | i | char | é 'A'-'Z'? | Ação | resultado parcial |
|---|---|---|---|---|---|
| 1 | 0 | H | sim | soma ('a'-'A'), vira 'h' | h |
| 2 | 1 | e | não | mantém | he |
| 3 | 2 | l | não | mantém | hel |
| 4 | 3 | l | não | mantém | hell |
| 5 | 4 | o | não | mantém | hello |

Resultado final: `"hello"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada
- **Espaço:** O(n) — para a string resultante (Strings são imutáveis em Java, precisa de um novo buffer)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String toLowerCase(String s) {
    char[] chars = s.toCharArray();
    for (int i = 0; i < chars.length; i++) {
        if (chars[i] >= 'A' && chars[i] <= 'Z') {
            chars[i] += ('a' - 'A'); // desloca pela distância fixa entre maiúscula e minúscula na tabela ASCII
        }
    }
    return new String(chars);
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

- Somar um número mágico (`+= 32`) em vez de `('a' - 'A')` — funciona por coincidência (a diferença ASCII entre maiúscula e minúscula é sempre 32), mas `('a' - 'A')` é autoexplicativo e não depende de decorar a tabela ASCII.
- Aplicar a conversão em TODOS os caracteres sem checar se já são maiúsculos — deslocaria dígitos e pontuação para símbolos incorretos da tabela ASCII.
- Modificar a `String` original diretamente — Strings são imutáveis em Java; é preciso converter para `char[]` (ou usar `StringBuilder`) antes de alterar caractere a caractere.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Mistura de maiúsculas e minúsculas | `"Hello"` | "hello" | caso padrão do enunciado |
| Já tudo minúsculo | `"here"` | "here" | nenhuma alteração necessária |
| Tudo maiúsculo | `"LOVELY"` | "lovely" | converte cada letra |
| Com dígitos/símbolos | `"already-1"` | "already-1" | caracteres não alfabéticos maiúsculos permanecem intactos |

## 🔗 Conexões

- Problemas irmãos: [0520] Detect Capital (mesma manipulação básica de caixa de caracteres), [0125] Valid Palindrome (também normaliza caixa como parte do pré-processamento)
- No backend: normalização de dados de entrada antes de comparação ou armazenamento (ex.: e-mails e nomes de usuário geralmente são normalizados para minúsculo antes de checar duplicidade no banco).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
