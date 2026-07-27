# [1089] Duplicate Zeros

> 🔗 [LeetCode 1089](https://leetcode.com/problems/duplicate-zeros/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Easy`

## 📜 O Problema

Dado um array `arr` de tamanho fixo, duplique cada ocorrência de `0`, empurrando os elementos restantes pra direita. Elementos que ultrapassarem o tamanho original **não são escritos** (são descartados). Faça a modificação **in-place**, sem retornar nada.

**Exemplos:**
```
Input:  arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]

Input:  arr = [1,2,3]
Output: [1,2,3]
```

**Restrições (e o que elas denunciam):**
- `1 <= arr.length <= 10^4` → O(n) esperado
- `0 <= arr[i] <= 9` → sem negativos, mas isso não muda a lógica; o que importa é só a igualdade com `0`
- "In-place" e "não retorna nada" → proíbe montar um array novo e devolvê-lo; a modificação precisa acontecer no array original

## 🧭 Como reconhecer o padrão

"Inserir elementos extras num array de tamanho fixo, empurrando o resto e descartando o que sair dos limites" é resolvido escrevendo **de trás para frente**, como em [0088] Merge Sorted Array: calcule primeiro o quanto cada posição vai se deslocar (aqui, quantos zeros existem no total) e depois escreva do índice mais alto pro mais baixo, garantindo nunca sobrescrever um valor que ainda precisa ser lido.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Percorrer o array da esquerda pra direita construindo uma lista nova, duplicando cada zero encontrado, e depois copiar de volta só os primeiros `n` elementos dessa lista pro array original.

- Tempo: O(n) · Espaço: O(n) — a lista nova pode crescer até quase o dobro do tamanho original antes de ser truncada
- **Por que não basta:** o enunciado pede modificação in-place; construir uma lista auxiliar do tamanho (quase) dobrado desperdiça espaço proporcional à entrada, quando dá pra calcular o deslocamento necessário e escrever direto no array original.

## 💡 Solução 2 — A ideia otimizada (intuição)

Primeiro, conte quantos zeros existem no array (`countZeros`) — esse é o total de posições extras que seriam necessárias se o array pudesse crescer. Use um ponteiro `i` no último índice original e um ponteiro `j` na posição "virtual" `n - 1 + countZeros` (onde esse elemento cairia se o array realmente crescesse). Percorra de trás pra frente: se `j` ainda está dentro dos limites (`j < n`), escreva `arr[i]` em `arr[j]`; se `arr[i]` for zero, escreva uma segunda cópia (decrementando `j` de novo, sempre checando o limite). Como tudo é escrito em posições `>= i`, nunca se perde um valor ainda não lido.

## 🎬 Exemplo passo a passo

`arr = [1,0,2,3,0,4,5,0]` (n=8), `countZeros = 3` (índices 1, 4, 7)

| Passo | i | j (início) | Ação | Array depois |
|---|---|---|---|---|
| 1 | 7 | 10 | ambas as escritas fora dos limites (`j >= n`), nada muda | `[1,0,2,3,0,4,5,0]` |
| 2 | 6 | 8 | escrita fora dos limites, nada muda | `[1,0,2,3,0,4,5,0]` |
| 3 | 5 | 7 | `arr[7] = arr[5] = 4` | `[1,0,2,3,0,4,5,4]` |
| 4 | 4 | 6 | `arr[4]=0`: `arr[6]=0`, depois `arr[5]=0` | `[1,0,2,3,0,0,0,4]` |
| 5 | 3 | 4 | `arr[4] = arr[3] = 3` | `[1,0,2,3,3,0,0,4]` |
| 6 | 2 | 3 | `arr[3] = arr[2] = 2` | `[1,0,2,2,3,0,0,4]` |
| 7 | 1 | 2 | `arr[1]=0`: `arr[2]=0`, depois `arr[1]=0` | `[1,0,0,2,3,0,0,4]` |
| 8 | 0 | 0 | `arr[0] = arr[0] = 1` (sem mudança) | `[1,0,0,2,3,0,0,4]` |

Resultado final: `[1,0,0,2,3,0,0,4]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada pra contar zeros, outra pra escrever de trás pra frente
- **Espaço:** O(1) — só os índices `i`, `j` e o contador, tudo escrito no array original

## 💻 Implementações

### Java (referência completa e comentada)
```java
public void duplicateZeros(int[] arr) {
    int n = arr.length;
    int countZeros = 0;
    for (int val : arr) {
        if (val == 0) {
            countZeros++;
        }
    }

    int i = n - 1;
    int j = n - 1 + countZeros; // posição "virtual" de escrita, incluindo o espaço extra dos zeros

    while (i >= 0) {
        if (j < n) {
            arr[j] = arr[i];
        }
        if (arr[i] == 0) {
            j--;
            if (j < n) {
                arr[j] = 0; // segunda cópia do zero
            }
        }
        i--;
        j--;
    }
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

- Percorrer da ESQUERDA pra direita fazendo a duplicação diretamente — isso sobrescreve elementos que ainda não foram lidos, corrompendo a entrada (mesmo problema de [0088] Merge Sorted Array); por isso o preenchimento tem que ser de trás pra frente.
- Esquecer de descartar duplicatas que "vazam" pra fora do tamanho original — o enunciado é explícito ("elements beyond the length... are not written"); daí a checagem `j < n` antes de cada escrita.
- Contar `countZeros` de forma incompleta (ex.: só os que "sobrevivem") — a contagem é de TODOS os zeros do array original; o deslocamento inicial já é grande o suficiente, e a checagem `j < n` descarta o excedente sozinha.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Caso padrão | `[1,0,2,3,0,4,5,0]` | `[1,0,0,2,3,0,0,4]` | mistura de zeros e não-zeros, algumas duplicatas descartadas |
| Sem zeros | `[1,2,3]` | `[1,2,3]` | `countZeros=0`, array não muda |
| Zero "vaza" pro final | `[1,0,2,0]` | `[1,0,0,2]` | a duplicata do último zero original ultrapassa o tamanho e é descartada |
| Único elemento zero | `[0]` | `[0]` | só uma posição disponível, a duplicata não cabe |

## 🔗 Conexões

- Problemas irmãos: [0088] Merge Sorted Array (mesma técnica de escrever de trás para frente pra evitar sobrescrever dados não lidos), [0283] Move Zeroes (mesma família de manipulação de zeros num array, mas empurrando pro fim em vez de duplicar)
- No backend: expandir um buffer in-place aplicando uma regra de "inserção condicional" — por exemplo, escapar caracteres especiais duplicando-os dentro de um buffer de tamanho fixo, descartando o que ultrapassar o limite (técnica comum em parsers e serializadores de baixo nível).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
