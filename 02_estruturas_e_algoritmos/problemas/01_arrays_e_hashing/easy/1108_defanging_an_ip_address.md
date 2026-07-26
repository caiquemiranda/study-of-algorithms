# [1108] Defanging an IP Address

> 🔗 [LeetCode 1108](https://leetcode.com/problems/defanging-an-ip-address/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Dado um endereço IPv4 válido `address`, retorne uma versão "defangada" desse endereço IP. Um **endereço IP defangado** substitui cada ponto `"."` por `"[.]"`.

**Exemplos:**
```
Input:  address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input:  address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
```

**Restrições (e o que elas denunciam):**
- o `address` fornecido é sempre um IPv4 válido → não precisa validar formato, só substituir

## 🧭 Como reconhecer o padrão

"Substitua toda ocorrência de um caractere por uma sequência maior" é o problema mais simples possível de manipulação de string — existe até um método pronto na maioria das linguagens (`replace`), mas vale entender a versão manual para reforçar a construção de string com `StringBuilder`.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Usar `s.replace(".", "[.]")` diretamente — tecnicamente já é a solução ótima (o método da biblioteca é O(n)); para fins didáticos, vale construir manualmente com um `StringBuilder`, percorrendo caractere por caractere.

- Tempo: O(n) tanto a versão manual quanto `replace` · Espaço: O(n) para a string resultante
- **Por que vale fazer manualmente mesmo sendo O(n) de qualquer forma:** reforça a mecânica de "percorrer e decidir o que emitir por caractere", útil para problemas de manipulação de string mais complexos.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `address` caractere por caractere com um `StringBuilder`; sempre que encontrar um `.`, emita `"[.]"` em vez do ponto; para qualquer outro caractere, emita-o normalmente.

## 🎬 Exemplo passo a passo

`address = "1.1.1.1"`

| Passo | i | char | Ação | resultado parcial |
|---|---|---|---|---|
| 1 | 0 | 1 | emite '1' | 1 |
| 2 | 1 | . | emite "[.]" | 1[.] |
| 3 | 2 | 1 | emite '1' | 1[.]1 |
| 4 | 3 | . | emite "[.]" | 1[.]1[.] |
| 5 | 4 | 1 | emite '1' | 1[.]1[.]1 |
| 6 | 5 | . | emite "[.]" | 1[.]1[.]1[.] |
| 7 | 6 | 1 | emite '1' | 1[.]1[.]1[.]1 |

Resultado final: `"1[.]1[.]1[.]1"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n) — para a string resultante

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String defangIPaddr(String address) {
    StringBuilder resultado = new StringBuilder();
    for (char c : address.toCharArray()) {
        if (c == '.') {
            resultado.append("[.]"); // substitui o ponto pela versão "defangada"
        } else {
            resultado.append(c);
        }
    }
    return resultado.toString();
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

- Nenhuma pegadinha real de lógica aqui — o cuidado principal é de estilo: usar `StringBuilder` em vez de concatenação de `String` dentro do loop, mesmo sendo um problema pequeno, como treino do hábito correto.
- Esquecer que `address.replace(".", "[.]")` já resolveria o problema em uma linha — não é errado usar, mas o exercício de fazer manualmente com `StringBuilder` treina a técnica usada em problemas mais complexos de transformação de string.
- Confundir `replace` (troca literal de caracteres/substrings) com `replaceAll` (que interpreta o argumento como regex) — para este caso, `.` seria interpretado como "qualquer caractere" se usado incorretamente com `replaceAll`.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| IP simples | `"1.1.1.1"` | "1[.]1[.]1[.]1" | caso padrão do enunciado |
| Números com múltiplos dígitos | `"255.100.50.0"` | "255[.]100[.]50[.]0" | garante que só o ponto é afetado, não os dígitos |
| Todos zeros | `"0.0.0.0"` | "0[.]0[.]0[.]0" | caso de borda com o menor valor possível por octeto |
| Valores máximos | `"255.255.255.255"` | "255[.]255[.]255[.]255" | maior IP válido possível |

## 🔗 Conexões

- Problemas irmãos: [0709] To Lower Case (mesmo nível de manipulação básica de string caractere a caractere), [0482] License Key Formatting (mesma técnica de reconstruir string com `StringBuilder`)
- No backend: sanitização de dados sensíveis antes de logar (ex.: "defangar" IPs ou URLs em logs de segurança para que não sejam clicáveis/ativos acidentalmente, prática comum em relatórios de threat intelligence).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
