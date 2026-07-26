# [1528] Shuffle String

> 🔗 [LeetCode 1528](https://leetcode.com/problems/shuffle-string/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#Array` `#String` `#Easy`

## 📜 O Problema

Você recebe uma string `s` e um array de inteiros `indices` de mesmo tamanho. A string `s` será embaralhada de forma que o caractere na `i`-ésima posição se mova para `indices[i]` na string embaralhada.

Retorne a string embaralhada.

**Exemplos:**
```
Input:  s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explicação: "codeleet" vira "leetcode" após o embaralhamento.

Input:  s = "abc", indices = [0,1,2]
Output: "abc"
Explicação: após o embaralhamento, cada caractere permanece na sua posição.
```

**Restrições (e o que elas denunciam):**
- `1 <= n <= 100` → O(n) resolve com folga
- índices únicos em `indices` → mapeamento bijetor, sem colisão

## 🧭 Como reconhecer o padrão

"Cada elemento sabe exatamente para onde vai" é resolvido com um array de saída de tamanho fixo, onde `resultado[indices[i]] = s[i]` para cada posição — simulação direta O(n), sem nenhuma estrutura extra.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Já é a solução direta aqui (não existe uma versão mais lenta relevante): para cada posição `i` de `s`, escrever o caractere na posição `indices[i]` do array de resultado.

- Tempo: O(n) · Espaço: O(n)
- **Por que vale nomear mesmo assim:** a única armadilha é inverter a direção do mapeamento (escrever `s[indices[i]]` em vez de `resultado[indices[i]] = s[i]`).

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Crie um array de caracteres `resultado` de tamanho `n`. Percorra `s`; para cada índice `i`, coloque `s.charAt(i)` na posição `indices[i]` de `resultado`.

## 🎬 Exemplo passo a passo

`s = "codeleet"`, `indices = [4,5,6,7,0,2,1,3]`

| Passo | i | s[i] | indices[i] | resultado[indices[i]] |
|---|---|---|---|---|
| 1 | 0 | c | 4 | resultado[4]='c' |
| 2 | 1 | o | 5 | resultado[5]='o' |
| 3 | 2 | d | 6 | resultado[6]='d' |
| 4 | 3 | e | 7 | resultado[7]='e' |
| 5 | 4 | l | 0 | resultado[0]='l' |
| 6 | 5 | e | 2 | resultado[2]='e' |
| 7 | 6 | e | 1 | resultado[1]='e' |
| 8 | 7 | t | 3 | resultado[3]='t' |

Resultado final: `"leetcode"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n)
- **Espaço:** O(n)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String restoreString(String s, int[] indices) {
    char[] resultado = new char[s.length()];
    for (int i = 0; i < s.length(); i++) {
        resultado[indices[i]] = s.charAt(i); // o caractere na posição i vai para indices[i]
    }
    return new String(resultado);
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

- Inverter a direção do mapeamento (`resultado[i] = s.charAt(indices[i])`) — essa é a operação INVERSA; o enunciado diz que o caractere na posição `i` MOVE PARA `indices[i]`, não que a posição `i` do resultado vem do índice `indices[i]` de `s`.
- Tentar fazer a reorganização in-place sobrescrevendo `s` diretamente — Strings são imutáveis em Java, então é preciso um array/buffer auxiliar de qualquer forma.
- Esquecer que `indices` pode não estar em ordem alguma — não dá para assumir que `indices[i] == i` nem qualquer padrão; cada posição precisa ser lida do array.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Embaralhamento completo | s="codeleet", indices=[4,5,6,7,0,2,1,3] | "leetcode" | caso padrão do enunciado |
| Sem mudança | s="abc", indices=[0,1,2] | "abc" | cada caractere fica na própria posição |
| Inversão total | s="abc", indices=[2,1,0] | "cba" | mapeamento inverte a ordem completamente |
| Uma única letra | s="a", indices=[0] | "a" | menor entrada possível |

## 🔗 Conexões

- Problemas irmãos: [1470] Shuffle the Array (mesma ideia de mapear posições de origem/destino conhecidas), [0442] Find All Duplicates in an Array (também usa índices como mapa, mas para marcação, não movimento)
- No backend: reordenação de colunas ou campos de um registro segundo um mapeamento de configuração (ex.: reformatar a ordem de campos ao exportar dados para um sistema legado que espera outra ordem).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
