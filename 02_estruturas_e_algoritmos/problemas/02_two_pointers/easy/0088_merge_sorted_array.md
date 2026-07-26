# [0088] Merge Sorted Array

> 🔗 [LeetCode 88](https://leetcode.com/problems/merge-sorted-array/) · Dificuldade: 🟢 easy · Categoria: [`02_two_pointers`](../../../fundamentos/02_two_pointers.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#TwoPointers` `#Array` `#Sorting` `#Easy`

## 📜 O Problema

Você recebe `nums1` e `nums2`, ambos ordenados em não decrescente, e dois inteiros `m` e `n` com a quantidade de elementos válidos em cada um. `nums1` tem tamanho `m + n`: os primeiros `m` elementos são os válidos, os últimos `n` são `0` só para "abrir espaço". Mescle os dois arrays de forma que o resultado final (ordenado) fique **dentro de `nums1`**.

**Exemplos:**
```
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Input:  nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

**Restrições (e o que elas denunciam):**
- `0 <= m, n <= 200` → inclui os casos de borda `m = 0` ou `n = 0` (um dos arrays "vazio")
- `nums1.length == m + n` → o espaço para o resultado já existe dentro de `nums1`, não é preciso alocar nada novo
- `nums1` e `nums2` já vêm **ordenados** → é o que permite mesclar em uma única passada, sem comparar todos-com-todos
- Follow-up pede O(m+n) → aponta que dá pra resolver sem sort completo e sem array auxiliar

## 🧭 Como reconhecer o padrão

"Mesclar duas sequências já ordenadas em uma só" é o padrão clássico de dois ponteiros andando em direções coordenadas: um ponteiro em cada array, sempre escolhendo o menor (ou, aqui, o maior) dos dois valores atuais para escrever na posição certa do resultado.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Copiar `nums2` para o final de `nums1` (nas posições que eram `0`) e depois ordenar `nums1` inteiro com um sort genérico.

- Tempo: O((m+n) log(m+n)) · Espaço: O(log(m+n)) a O(m+n), dependendo do algoritmo de sort
- **Por que não basta:** ignora completamente que os dois arrays **já estão ordenados** — usar um sort genérico desperdiça a estrutura que já existe na entrada; um merge de duas listas ordenadas resolve em O(m+n), sem comparações redundantes.

## 💡 Solução 2 — A ideia otimizada (intuição)

Mesclar **de trás para frente**. Use três ponteiros: `p1` no último elemento válido de `nums1` (índice `m-1`), `p2` no último de `nums2` (índice `n-1`), e `escrita` na última posição de `nums1` (índice `m+n-1`). A cada passo, coloque em `escrita` o **maior** valor entre `nums1[p1]` e `nums2[p2]`, e avance o ponteiro correspondente para trás. Mesclar de trás pra frente garante que você só escreve em posições que já foram lidas ou que são "lixo" (os zeros), nunca sobrescrevendo um valor de `nums1` antes de compará-lo.

## 🎬 Exemplo passo a passo

`nums1 = [1,2,3,0,0,0]` (m=3), `nums2 = [2,5,6]` (n=3)

| Passo | nums1[p1] | nums2[p2] | Maior | escrita ← | p1,p2 depois |
|---|---|---|---|---|---|
| 1 | 3 (p1=2) | 6 (p2=2) | 6 | nums1[5]=6 | p1=2, p2=1 |
| 2 | 3 (p1=2) | 5 (p2=1) | 5 | nums1[4]=5 | p1=2, p2=0 |
| 3 | 3 (p1=2) | 2 (p2=0) | 3 | nums1[3]=3 | p1=1, p2=0 |
| 4 | 2 (p1=1) | 2 (p2=0) | 2 (empate, usa nums1) | nums1[2]=2 | p1=0, p2=0 |
| 5 | 1 (p1=0) | 2 (p2=0) | 2 | nums1[1]=2 | p1=0, p2=-1 |

`p2 < 0` → loop termina; `nums1[0]=1` já estava correto (sobrou só ele, e é o menor de todos)

Resultado final: `[1,2,2,3,5,6]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(m + n) — cada elemento dos dois arrays é visitado exatamente uma vez
- **Espaço:** O(1) — mescla in-place dentro do próprio `nums1`, sem array auxiliar

## 💻 Implementações

### Java (referência completa e comentada)
```java
public void merge(int[] nums1, int m, int[] nums2, int n) {
    int p1 = m - 1;
    int p2 = n - 1;
    int escrita = m + n - 1;

    // mescla de trás para frente: a "cauda" de nums1 (posições altas) ainda
    // não foi lida, então é segura para escrever sem perder nenhum dado
    while (p2 >= 0) {
        if (p1 >= 0 && nums1[p1] > nums2[p2]) {
            nums1[escrita] = nums1[p1];
            p1--;
        } else {
            nums1[escrita] = nums2[p2];
            p2--;
        }
        escrita--;
    }
    // se p2 esgota antes de p1, os elementos restantes de nums1 já estão
    // na posição certa (vieram do próprio nums1, nunca precisaram se mover)
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

- Mesclar de **frente para trás** (como um merge normal de duas listas) — isso sobrescreve posições de `nums1` que ainda não foram lidas, corrompendo a entrada antes de terminar a comparação. A mesclagem só funciona in-place porque começa pelo **final**, onde há espaço "vazio" garantido.
- Esquecer o `p1 >= 0` na condição do `if` — quando `nums1` já foi totalmente consumido mas `nums2` ainda tem elementos, comparar `nums1[p1]` com `p1 = -1` acessa índice inválido.
- Tratar `n == 0` como caso especial — não é preciso: o loop `while (p2 >= 0)` simplesmente não executa nenhuma vez, e `nums1` já está correto (não tem nada de `nums2` pra mesclar).

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| nums2 vazio | `nums1=[1]`, m=1, `nums2=[]`, n=0 | `[1]` | loop não executa nenhuma vez |
| nums1 "vazio" (m=0) | `nums1=[0]`, m=0, `nums2=[1]`, n=1 | `[1]` | todo o resultado final vem de nums2 |
| Valores empatados | `nums1=[2,4,0,0]`, m=2, `nums2=[2,3]`, n=2 | `[2,2,3,4]` | testa o critério de decisão quando os dois valores atuais são iguais |
| nums2 todo maior | `nums1=[1,2,3,0,0,0]`, m=3, `nums2=[4,5,6]`, n=3 | `[1,2,3,4,5,6]` | p1 esgota primeiro, resto de nums2 é copiado em sequência |

## 🔗 Conexões

- Problemas irmãos: [0021] Merge Two Sorted Lists (mesma ideia de mesclar duas sequências ordenadas, mas em lista encadeada), [0026] Remove Duplicates from Sorted Array (mesma família de manipulação in-place de array ordenado com ponteiros)
- No backend: é literalmente o passo de "merge" de um merge sort externo (juntar partições já ordenadas maiores que a memória disponível), ou combinar duas páginas de resultado já ordenadas vindas de shards diferentes de um banco, sem alocar buffer extra.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
