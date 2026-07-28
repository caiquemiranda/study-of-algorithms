# [0496] Next Greater Element I

> 🔗 [LeetCode 496](https://leetcode.com/problems/next-greater-element-i/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-27 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#HashTable`

## 📜 O Problema

O **próximo elemento maior** de um elemento `x` num array é o primeiro elemento maior que `x`, à direita de `x`, no mesmo array.

Você recebe dois arrays de inteiros **distintos** e **0-indexados**, `nums1` e `nums2`, onde `nums1` é um subconjunto de `nums2`. Para cada `i` de `nums1`, encontre o índice `j` tal que `nums1[i] == nums2[j]`, e determine o próximo elemento maior de `nums2[j]` **dentro de `nums2`**. Se não existir, a resposta para essa posição é `-1`.

Retorne um array `ans` de mesmo tamanho que `nums1`, com o próximo maior elemento correspondente.

**Exemplos:**
```
Input:  nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explicação:
- 4 está em nums2 = [1,3,4,2]. Não há elemento maior à direita → -1.
- 1 está em nums2 = [1,3,4,2]. O próximo maior é 3.
- 2 está em nums2 = [1,3,4,2]. Não há elemento maior à direita → -1.

Input:  nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

**Restrições (e o que elas denunciam):**
- `1 <= nums1.length <= nums2.length <= 1000` → mesmo O(n²) passaria dentro do tempo (1000² = 10^6), mas o follow-up pede O(nums1.length + nums2.length), sinalizando que existe uma solução linear
- Todos os inteiros de `nums1` e `nums2` são **únicos** (dentro de cada array) → não há ambiguidade de "qual ocorrência" ao buscar `nums1[i]` dentro de `nums2`, cada valor mapeia para exatamente uma posição
- Todos os elementos de `nums1` também aparecem em `nums2` → toda busca em `nums2` é garantida ter sucesso, não precisa tratar "não encontrado" na busca em si (só o "não há maior à direita")

## 🧭 Como reconhecer o padrão

"Para cada elemento, encontrar o **próximo** elemento maior/menor à direita" é a assinatura clássica de **monotonic stack**: em vez de, para cada posição, varrer tudo à direita de novo (O(n²)), você processa o array uma vez mantendo uma pilha que só cresce (ou só decresce), e cada elemento "resolve" a pendência de todos os elementos menores que ele ainda pendentes na pilha.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada valor de `nums1[i]`, encontre sua posição `j` em `nums2` (varrendo `nums2`), depois continue varrendo `nums2` a partir de `j+1` até achar o primeiro valor maior que `nums2[j]`.

- Tempo: O(nums1.length × nums2.length) · Espaço: O(1) extra (fora a resposta)
- **Por que não basta:** para cada elemento de `nums1`, você refaz uma varredura de `nums2` inteiro — o mesmo trecho de `nums2` acaba sendo varrido repetidamente para elementos diferentes. O follow-up pede O(n + m); a solução monotônica calcula o "próximo maior" de **todo mundo em `nums2`** de uma vez, em uma única passada.

## 💡 Solução 2 — A ideia otimizada (intuição)

Pré-processe `nums2` uma única vez com uma pilha monotônica **decrescente** (de baixo para cima) guardando valores ainda "à espera" do seu próximo maior. Percorra `nums2` da esquerda para a direita: enquanto o valor atual for maior que o topo da pilha, esse topo acabou de encontrar seu próximo maior (o valor atual) — desempilhe e registre num mapa `valor → próximo_maior`. Depois empilhe o valor atual. No final, quem sobrar na pilha nunca encontrou um maior à direita (fica com `-1`). Com esse mapa pronto, responder cada `nums1[i]` é uma simples consulta O(1).

## 🎬 Exemplo passo a passo

`nums2 = [1,3,4,2]`, construindo o mapa `próximo_maior`

| Passo | valor | Ação do while (desempilha e resolve) | Pilha após | Mapa após |
|---|---|---|---|---|
| 1 | 1 | pilha vazia, nada a resolver | `[1]` | `{}` |
| 2 | 3 | 3 > 1 → pop 1, mapa[1] = 3 | `[3]` | `{1:3}` |
| 3 | 4 | 4 > 3 → pop 3, mapa[3] = 4 | `[4]` | `{1:3, 3:4}` |
| 4 | 2 | 2 < 4 → mantém monotonia | `[4, 2]` | `{1:3, 3:4}` |

Sobrou `[4, 2]` na pilha → `mapa[4] = -1`, `mapa[2] = -1`.

Consultando `nums1 = [4,1,2]`: `mapa[4] = -1`, `mapa[1] = 3`, `mapa[2] = -1`.

Resultado final: `[-1, 3, -1]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — uma passada O(m) para construir o mapa a partir de `nums2` (cada elemento entra e sai da pilha no máximo uma vez), mais O(n) para consultar `nums1`
- **Espaço:** O(m) — a pilha e o mapa guardam no máximo todos os elementos de `nums2`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    Map<Integer, Integer> proximoMaior = new HashMap<>();
    Deque<Integer> pilha = new ArrayDeque<>(); // valores em ordem decrescente de baixo pra cima

    for (int atual : nums2) {
        // enquanto o topo for menor que o atual, o atual É o próximo maior do topo
        while (!pilha.isEmpty() && pilha.peek() < atual) {
            proximoMaior.put(pilha.pop(), atual);
        }
        pilha.push(atual);
    }
    // quem sobrou na pilha nunca teve um maior à direita: fica default -1 no getOrDefault abaixo

    int[] resposta = new int[nums1.length];
    for (int i = 0; i < nums1.length; i++) {
        resposta[i] = proximoMaior.getOrDefault(nums1[i], -1);
    }
    return resposta;
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

- Construir a pilha monotônica sobre `nums1` em vez de `nums2` — o "próximo maior" precisa ser calculado dentro de `nums2` (o array maior/completo); `nums1` é só a lista de consultas.
- Guardar índices em vez de valores na pilha (ou vice-versa) sem ajustar a lógica — aqui, como os valores são únicos e o mapa é `valor → próximo_maior`, guardar valores diretamente simplifica; em variações do problema com valores repetidos, seria necessário guardar índices.
- Esquecer o `-1` default para quem nunca é resolvido — elementos que sobram na pilha ao final do loop nunca passam pelo `while`, então nunca entram no mapa; usar `getOrDefault(..., -1)` (ou equivalente) cobre isso automaticamente.
- Achar que precisa refazer a busca de `nums1[i]` dentro de `nums2` a cada consulta — com o mapa pré-computado, a resposta é O(1) por consulta, não precisa buscar a posição de novo.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Maior elemento de `nums2` está em `nums1` | `nums1=[4], nums2=[1,3,4,2]` | `[-1]` | o maior valor do array nunca tem um "próximo maior" |
| Sequência estritamente crescente | `nums1=[1,2], nums2=[1,2,3]` | `[2,3]` | cada elemento resolve o anterior imediatamente, pilha nunca acumula mais de 1 |
| Sequência estritamente decrescente | `nums1=[3,2], nums2=[3,2,1]` | `[-1,-1]` | nenhum elemento encontra maior à direita, todos ficam na pilha até o fim |
| `nums1` igual a `nums2` (mesmo tamanho) | `nums1=[2,4], nums2=[1,2,3,4]` | `[3,-1]` | consulta cobre todo o array, não só um subconjunto |

## 🔗 Conexões

- Problemas irmãos: [0503] Next Greater Element II (mesma técnica, mas array circular), [0739] Daily Temperatures (mesma ideia de "próximo maior", retornando distância em vez do valor), [1475] Final Prices With a Special Discount in a Shop (monotonic stack buscando o próximo **menor ou igual**)
- No backend: monotonic stack aparece em análise de séries temporais — por exemplo, achar para cada preço de uma ação o próximo momento em que ele foi superado (sinaliza tendência de alta), ou detectar o próximo evento que "resolve" um alerta pendente numa fila de monitoramento.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
