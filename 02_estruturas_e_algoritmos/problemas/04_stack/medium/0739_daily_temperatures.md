# [0739] Daily Temperatures

> 🔗 [LeetCode 739](https://leetcode.com/problems/daily-temperatures/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#MonotonicStack` `#Array`

## 📜 O Problema

Dado um array de inteiros `temperatures` representando temperaturas diárias, retorne um array `answer` tal que `answer[i]` seja o número de dias que você precisa esperar após o dia `i` para obter uma temperatura mais **quente**. Se não existir um dia futuro assim, `answer[i] = 0`.

**Exemplos:**
```
Input:  temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input:  temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input:  temperatures = [30,60,90]
Output: [1,1,0]
```

**Restrições (e o que elas denunciam):**
- `1 <= temperatures.length <= 10^5` → precisa de solução O(n); força bruta O(n²) estouraria
- `30 <= temperatures[i] <= 100` → faixa de valores pequena e conhecida, mas isso não muda a técnica (não dá para usar contagem por valor de forma direta, já que a resposta depende de **posição**, não de valor)

## 🧭 Como reconhecer o padrão

"Para cada elemento, encontrar quantos passos até o **próximo maior**" é a assinatura mais clássica de **monotonic stack**: em vez de, para cada dia, varrer todos os dias futuros (O(n²)), você processa o array uma vez mantendo uma pilha decrescente de dias "pendentes" — cada novo dia mais quente resolve de uma vez a pendência de todos os dias mais frios ainda esperando na pilha.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada dia `i`, percorrer os dias `j > i` em ordem até encontrar o primeiro `temperatures[j] > temperatures[i]`, e calcular `j - i`.

- Tempo: O(n²) · Espaço: O(1) extra
- **Por que não basta:** para `n = 10^5`, o pior caso (array estritamente decrescente, forçando cada busca a varrer até o fim) é 10^10 operações — muito além do tempo permitido. Cada busca refaz um trabalho que poderia ser compartilhado entre dias.

## 💡 Solução 2 — A ideia otimizada (intuição)

Percorra `temperatures` da esquerda para a direita mantendo uma pilha de **índices** com temperaturas decrescentes de baixo para cima. Para cada dia `i`: enquanto o topo da pilha apontar para um dia com temperatura **menor** que a de hoje, esse dia acabou de encontrar seu "próximo dia mais quente" — desempilhe-o e calcule `answer[topo] = i - topo` (a distância em dias). Depois empilhe `i`. Quem sobra na pilha ao final nunca encontrou um dia mais quente, e mantém `answer = 0` (valor default).

## 🎬 Exemplo passo a passo

`temperatures = [73,74,75,71,69,72,76,73]`

| Passo | i | temp[i] | Ação do while (desempilha índices com temp menor) | Pilha (índices) após | answer após |
|---|---|---|---|---|---|
| 1 | 0 | 73 | pilha vazia | `[0]` | `[0,0,0,0,0,0,0,0]` |
| 2 | 1 | 74 | pop 0 (73<74) → answer[0]=1-0=1 | `[1]` | `[1,0,0,0,0,0,0,0]` |
| 3 | 2 | 75 | pop 1 (74<75) → answer[1]=2-1=1 | `[2]` | `[1,1,0,0,0,0,0,0]` |
| 4 | 3 | 71 | 75 não < 71, para | `[2,3]` | `[1,1,0,0,0,0,0,0]` |
| 5 | 4 | 69 | 71 não < 69, para | `[2,3,4]` | `[1,1,0,0,0,0,0,0]` |
| 6 | 5 | 72 | pop 4 (69<72)→answer[4]=1; pop 3 (71<72)→answer[3]=2; 75 não<72, para | `[2,5]` | `[1,1,0,2,1,0,0,0]` |
| 7 | 6 | 76 | pop 5 (72<76)→answer[5]=1; pop 2 (75<76)→answer[2]=4 | `[6]` | `[1,1,4,2,1,0,0,0]` |
| 8 | 7 | 73 | 76 não < 73, para | `[6,7]` | `[1,1,4,2,1,0,0,0]` |

Sobram `[6, 7]` na pilha → nunca encontram dia mais quente, permanecem com `answer = 0`.

Resultado final: `[1,1,4,2,1,1,0,0]` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada índice é empilhado e desempilhado no máximo uma vez; o `while` interno não torna o algoritmo O(n²) porque o custo total de todos os pops, somado ao longo de toda a execução, é no máximo `n`
- **Espaço:** O(n) — pior caso, array estritamente decrescente, todos os índices ficam na pilha até o fim

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int[] dailyTemperatures(int[] temperatures) {
    int[] answer = new int[temperatures.length]; // default 0: cobre quem nunca esquenta
    Deque<Integer> pilha = new ArrayDeque<>();    // índices com temperaturas decrescentes

    for (int i = 0; i < temperatures.length; i++) {
        // resolve a pendência de todo mundo mais frio que hoje, de uma vez
        while (!pilha.isEmpty() && temperatures[pilha.peek()] < temperatures[i]) {
            int j = pilha.pop();
            answer[j] = i - j; // distância em dias até o próximo dia mais quente
        }
        pilha.push(i);
    }

    return answer;
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

- Guardar **temperaturas** na pilha em vez de **índices** — a resposta precisa da distância (`i - j`), que só pode ser calculada se você souber a posição de cada dia pendente, não só o valor.
- Usar `<=` em vez de `<` na condição do while — dias com temperatura **igual** não devem disparar resolução, já que o enunciado pede estritamente "mais quente" (maior, não maior-ou-igual).
- Achar que o `while` aninhado torna o algoritmo O(n²) — é uma dúvida comum, mas cada índice só pode ser desempilhado **uma vez** em toda a execução, então o número total de operações de pop ao longo de todo o algoritmo é limitado por `n`, não por `n` a cada iteração externa.
- Esquecer que o array `answer` já começa com `0` por padrão em Java — não é preciso inicializar explicitamente os dias que nunca encontram um mais quente, já que o array `int[]` já nasce zerado.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Estritamente crescente | `[30,40,50,60]` | `[1,1,1,0]` | cada dia resolve o anterior imediatamente, pilha nunca acumula mais de 1 elemento |
| Estritamente decrescente | `[76,75,74,73]` | `[0,0,0,0]` | nenhum dia encontra um mais quente, todos ficam na pilha até o fim |
| Um único dia | `[70]` | `[0]` | sem dias futuros, resposta trivial |
| Temperaturas iguais consecutivas | `[70,70,70]` | `[0,0,0]` | "mais quente" é estrito; empates não contam como resolução |

## 🔗 Conexões

- Problemas irmãos: [0496] Next Greater Element I (mesma técnica de monotonic stack, retornando o valor em vez da distância), [0503] Next Greater Element II (mesma técnica em array circular), [0853] Car Fleet (monotonic stack aplicado a um domínio físico diferente)
- No backend: essa técnica de "resolver a pendência de todos os elementos menores de uma vez ao encontrar um maior" aparece em análise de séries temporais para detectar quando um valor supera um pico anterior (ex.: monitoramento de métricas que dispara alerta no primeiro momento em que a carga do sistema volta a subir acima de um nível anterior).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
