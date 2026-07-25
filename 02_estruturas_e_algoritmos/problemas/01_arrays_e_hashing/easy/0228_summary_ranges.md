# [0228] Summary Ranges

> 🔗 [LeetCode 228](https://leetcode.com/problems/summary-ranges/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Dado um array `nums` **ordenado e com valores únicos**, retorne a menor lista de faixas `[a,b]` que cobre exatamente todos os números do array. Cada faixa vira uma string: `"a->b"` se `a != b`, ou apenas `"a"` se `a == b`.

**Exemplos:**
```
Input:  nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Input:  nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
```

**Restrições (e o que elas denunciam):**
- `0 <= nums.length <= 20` → o tamanho é pequeno de propósito; o desafio não é performance, é **tratar corretamente os casos de borda** (array vazio, faixa de 1 elemento)
- `-2^31 <= nums[i] <= 2^31 - 1` → os valores cabem em `int`, mas cuidado ao comparar `nums[i] + 1` com o próximo (não há overflow real aqui, mas é hábito a checar)
- "valores únicos e ordenados" → você NÃO precisa de hash map nem de ordenação — é uma varredura linear simples com dois marcadores

## 🧭 Como reconhecer o padrão

Array já ordenado + "encontre sequências consecutivas" é um sinal de **varredura de intervalo com dois ponteiros**: um marca o início da sequência atual, o outro avança enquanto os números continuam consecutivos (`nums[i+1] == nums[i] + 1`).

## 🐢 Solução 1 — Força bruta

Para cada início de faixa, procurar o fim da faixa refazendo uma busca a partir dali (ex.: usando índice de busca a cada passo em vez de avançar incrementalmente), reconstruindo listas intermediárias.

- Tempo: O(n²) no pior caso (se cada busca de fim de faixa reprocessa o restante do array) · Espaço: O(n)
- **Por que não é a ideal:** o array já está ordenado — cada elemento só precisa ser visitado **uma vez** para saber se continua ou quebra a sequência atual; refazer buscas é trabalho redundante.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra o array com um ponteiro `i`. Para cada posição, deixe um segundo ponteiro `j` andar **enquanto os números continuarem consecutivos** (`nums[j+1] == nums[j] + 1`). Quando a sequência quebra, você tem a faixa completa `[nums[i], nums[j]]` — formate a string e pule `i` para logo depois de `j`.

## 🎬 Exemplo passo a passo

`nums = [0, 1, 2, 4, 5, 7]`

| i (início) | j avança enquanto consecutivo | j final | Faixa formatada | resultado parcial |
|---|---|---|---|---|
| 0 | 0→1 (1==0+1) →2 (2==1+1) →para (4≠2+1) | 2 | "0->2" | `["0->2"]` |
| 3 | 3→4 (5==4+1) →para (7≠5+1) | 4 | "4->5" | `["0->2","4->5"]` |
| 5 | não avança (não há próximo) | 5 | "7" (a==b) | `["0->2","4->5","7"]` |

Resultado final: `["0->2", "4->5", "7"]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada elemento é visitado exatamente uma vez, seja como `i` seja como `j`
- **Espaço:** O(1) extra (fora a lista de resultado, que é proporcional à saída, não ao processamento)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<String> summaryRanges(int[] nums) {
    List<String> resultado = new ArrayList<>();
    int n = nums.length;
    int i = 0;

    while (i < n) {
        int inicio = i;
        // avança 'i' enquanto a sequência continuar consecutiva (nums[i+1] == nums[i] + 1)
        while (i + 1 < n && nums[i + 1] == nums[i] + 1) {
            i++;
        }
        // 'i' agora aponta para o FIM da faixa atual
        if (inicio == i) {
            resultado.add(String.valueOf(nums[inicio]));       // faixa de um único número
        } else {
            resultado.add(nums[inicio] + "->" + nums[i]);      // faixa de vários números
        }
        i++; // pula para o começo da próxima faixa candidata
    }
    return resultado;
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

- Esquecer o caso **array vazio** (`nums.length == 0`) → deve retornar lista vazia, não erro.
- Esquecer o caso **faixa de um elemento só** → a string é só `"a"`, sem a seta `->`.
- Comparar `nums[i+1] == nums[i] + 1` sem checar `i + 1 < n` primeiro → `ArrayIndexOutOfBoundsException`.
- **Java**: concatenar String com `+` dentro de um loop grande seria O(n²) por causa da imutabilidade — aqui não é problema (poucas faixas), mas é bom saber quando usar `StringBuilder`.
- Confundir esta categoria com **Merge Intervals** ([56]) — aqui os números já são únicos e ordenados, não há sobreposição para resolver, só consecutividade para detectar.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Array vazio | `[]` | `[]` | borda mínima |
| Um elemento | `[5]` | `["5"]` | faixa de tamanho 1 |
| Tudo consecutivo | `[1,2,3,4]` | `["1->4"]` | uma única faixa grande |
| Nada consecutivo | `[1,3,5]` | `["1","3","5"]` | todas as faixas de tamanho 1 |

## 🔗 Conexões

- Problemas irmãos: **[0056] Merge Intervals** (junta intervalos que se sobrepõem, não apenas números consecutivos), **[0163] Missing Ranges** (o inverso: encontrar os buracos em vez das faixas presentes)
- No backend: compactar uma lista de IDs de página lida (`1,2,3,7,8` → `"1-3, 7-8"`) para logs legíveis, ou resumir portas TCP abertas num range scan, usa exatamente esta técnica de agrupar consecutivos.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
