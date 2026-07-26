# [0717] 1-bit and 2-bit Characters

> 🔗 [LeetCode 717](https://leetcode.com/problems/1-bit-and-2-bit-characters/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Greedy` `#Easy`

## 📜 O Problema

Temos dois caracteres especiais:
- O primeiro caractere pode ser representado por um único bit `0`.
- O segundo caractere pode ser representado por dois bits (`10` ou `11`).

Dado um array binário `bits` que termina com `0`, retorne `true` se o último caractere deve obrigatoriamente ser um caractere de um bit.

**Exemplos:**
```
Input:  bits = [1,0,0]
Output: true
Explicação: a única forma de decodificar é caractere de dois bits + caractere de um bit.
Logo o último caractere é de um bit.

Input:  bits = [1,1,1,0]
Output: false
Explicação: a única forma de decodificar é caractere de dois bits + caractere de dois bits.
Logo o último caractere NÃO é de um bit.
```

**Restrições (e o que elas denunciam):**
- `1 <= bits.length <= 1000` → entrada pequena, qualquer O(n) resolve com folga
- o array termina com `0` (garantido) → simplifica o caso de borda final, sempre existe um caractere de 1 bit "fechando" a decodificação
- `bits[i]` é `0` ou `1` → só dois símbolos possíveis para os bits

## 🧭 Como reconhecer o padrão

"Decodifique uma sequência onde símbolos têm tamanhos diferentes, determinados pelo próprio valor do primeiro bit" é um problema de simulação gulosa (greedy) da esquerda para a direita: sempre que vir um `1`, você é OBRIGADO a consumir 2 bits (não há ambiguidade, pois `1` nunca é um caractere de 1 bit); só um `0` pode ser interpretado como caractere de 1 bit.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Não existe uma alternativa "ineficiente" relevante aqui — o processo de decodificação é inerentemente sequencial e cada decisão é determinística (não há branching real para explorar). A diferença entre uma solução ingênua e a ótima está só em pensar bit a bit sem "pular" 2 posições de uma vez ao encontrar um caractere de 2 bits.

- Tempo: O(n) — mesmo a versão menos elegante ainda visita cada bit no máximo uma vez · Espaço: O(1)
- **Por que vale otimizar mesmo assim:** simular avançando de 1 ou 2 em 2 deixa claro *por que* a resposta é determinística, em vez de simplesmente "percorrer e ver o que acontece".

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array com um índice `i` começando em 0. Se `bits[i] == 1`, avance `i` em 2 (é um caractere de 2 bits, obrigatoriamente). Se `bits[i] == 0`, avance `i` em 1 (caractere de 1 bit). Repita até `i` alcançar o último índice. Se `i` for exatamente `bits.length - 1` ao final, o último caractere foi decodificado sozinho como 1-bit → `true`. Se `i` ultrapassou esse índice, o `0` final foi "engolido" como parte de um caractere de 2 bits → `false`.

## 🎬 Exemplo passo a passo

`bits = [1,0,0]`

| Passo | i | bits[i] | Ação | novo i |
|---|---|---|---|---|
| 1 | 0 | 1 | caractere de 2 bits, avança 2 | 2 |
| 2 | 2 | 0 | i chegou no último índice (2 = length-1), loop para | — |

`i` final = 2 = `bits.length - 1` (2) → o último `0` foi decodificado sozinho como caractere de 1 bit → **true** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada, avançando 1 ou 2 por vez
- **Espaço:** O(1) — só o índice `i`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public boolean isOneBitCharacter(int[] bits) {
    int i = 0;
    int n = bits.length;
    while (i < n - 1) {
        // se o bit atual é 1, é obrigatoriamente o início de um caractere de 2 bits
        i += (bits[i] == 1) ? 2 : 1;
    }
    // se i parou exatamente no último índice, o 0 final foi consumido sozinho (1 bit)
    // se i "pulou" para além dele, o 0 final foi engolido junto com o bit anterior (2 bits)
    return i == n - 1;
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

- Parar o loop com `i <= n - 1` em vez de `i < n - 1` — faria o loop tentar ler `bits[i+1]` fora dos limites do array quando `i` já é o último índice.
- Esquecer que `1` SEMPRE significa caractere de 2 bits (nunca existe caractere de 1 bit começando com `1`) — não há ambiguidade a resolver, é uma leitura determinística.
- Tentar decodificar de trás para frente contando quantos `1`s consecutivos existem antes do último `0` — também funciona (se a contagem de 1s à esquerda do último 0 for par, o último é 1-bit), mas é menos intuitivo que simular da esquerda para a direita.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Termina isolado | `[1,0,0]` | true | "10" + "0": o último 0 é sozinho |
| Termina engolido | `[1,1,1,0]` | false | "11" + "10": o último 0 faz parte do caractere de 2 bits |
| Só um bit | `[0]` | true | caso trivial, um único caractere de 1 bit |
| Vários 1-bit seguidos | `[1,0,1,0,0]` | true | "10"+"10"+"0": termina isolado |

## 🔗 Conexões

- Problemas irmãos: [0091] Decode Ways (mesma família de decodificação com tamanhos de símbolo variáveis, mas com programação dinâmica por causa da ambiguidade real entre 1 e 2 dígitos), [0392] Is Subsequence (mesmo estilo de ponteiro avançando de forma determinística pela entrada)
- No backend: parsers de protocolos binários de tamanho variável (ex.: UTF-8, onde os primeiros bits de um byte determinam quantos bytes o caractere ocupa) — a mesma lógica de "o próprio símbolo diz seu tamanho" aparece em codecs reais.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
