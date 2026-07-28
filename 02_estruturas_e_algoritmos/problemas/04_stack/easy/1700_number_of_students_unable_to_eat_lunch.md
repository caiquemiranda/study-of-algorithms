# [1700] Number of Students Unable to Eat Lunch

> 🔗 [LeetCode 1700](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) · Dificuldade: 🟢 easy · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#Queue` `#Simulation`

## 📜 O Problema

A cantina da escola oferece sanduíches circulares e quadrados, referidos pelos números `0` e `1`. Todos os alunos ficam em fila; cada aluno prefere um dos dois tipos. O número de sanduíches é igual ao número de alunos, e eles estão empilhados (o índice `0` do array `sandwiches` é o topo da pilha).

A cada passo: se o aluno na **frente da fila** prefere o sanduíche do **topo da pilha**, ele o pega e sai da fila. Caso contrário, ele desiste (por enquanto) e vai para o **fim da fila**. Isso continua até que nenhum aluno restante na fila queira o sanduíche do topo.

Você recebe `students[j]` (preferência do aluno `j`, `j=0` é a frente) e `sandwiches[i]` (tipo do sanduíche `i`, `i=0` é o topo). Retorne **quantos alunos não conseguem comer**.

**Exemplos:**
```
Input:  students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0
Explicação: após vários ciclos de "desiste, volta pro fim", todos os alunos conseguem comer.

Input:  students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
```

**Restrições (e o que elas denunciam):**
- `1 <= students.length, sandwiches.length <= 100` → tamanho minúsculo, até uma simulação O(n²) passaria tranquilamente
- `students.length == sandwiches.length` → sempre há exatamente um sanduíche por aluno, garantindo que a simulação termina (ou todos comem, ou sobra um "empate" que nunca se resolve)
- `sandwiches[i]` e `students[i]` são `0` ou `1` → só duas categorias, o que permite trocar a simulação literal por uma **contagem de preferências**

## 🧭 Como reconhecer o padrão

O enunciado já entrega a estrutura: "pilha" de sanduíches (LIFO, só mexe no topo) e "fila" de alunos (FIFO, quem desiste vai para o fim). Simular literalmente com uma pilha e uma fila resolve, mas a observação chave é que, como só existem 2 tipos, **a ordem dos alunos na fila deixa de importar** assim que você percebe que o processo só para quando nenhum aluno restante quer o sanduíche do topo — e "nenhum aluno restante quer X" é uma pergunta sobre **contagem**, não sobre ordem.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Simule literalmente com uma fila (`Deque`) de alunos e uma pilha (ou índice) de sanduíches. Repita: se o aluno da frente da fila quer o sanduíche do topo, ambos saem; senão, o aluno vai para o fim da fila. Pare quando: a pilha esvaziar (todos comeram) OU um ciclo completo pela fila não resultar em nenhuma remoção (ninguém mais quer o topo).

- Tempo: O(n²) pior caso · Espaço: O(n)
- **Por que não basta:** para `n=100` isso passa tranquilo, mas o "ninguém mais quer o topo" exige detectar quando a fila deu uma volta completa sem progresso — fácil de errar (loop infinito se mal implementado). A solução ótima elimina essa complicação observando que só a **contagem** de cada preferência importa, não a ordem exata dos alunos que desistem.

## 💡 Solução 2 — A ideia otimizada (intuição)

Conte quantos alunos preferem `0` e quantos preferem `1` (dois contadores). Agora percorra a pilha de sanduíches do topo para baixo: para o sanduíche atual, se ainda existe algum aluno com aquela preferência (contador > 0), "sirva" esse aluno — decremente o contador correspondente e continue para o próximo sanduíche. Assim que o sanduíche do topo não tiver **nenhum** aluno interessado (contador daquele tipo é 0), o processo trava ali: **todos** os alunos restantes na fila (que é exatamente a soma dos dois contadores nesse ponto) nunca vão conseguir comer, porque eles só rotacionam infinitamente sem ninguém querer o topo. A resposta é a soma dos contadores restantes nesse momento de trava (ou 0 se a pilha inteira for consumida).

## 🎬 Exemplo passo a passo

`students = [1,1,1,0,0,1]`, `sandwiches = [1,0,0,0,1,1]`

Contagem inicial: `count[0] = 2` (dois alunos preferem 0), `count[1] = 4` (quatro preferem 1).

| Passo | sanduíche (topo) | count[0] | count[1] | Ação |
|---|---|---|---|---|
| 1 | 1 | 2 | 4 | count[1] > 0 → serve, count[1]-- | 
| 2 | 0 | 2 | 3 | count[0] > 0 → serve, count[0]-- |
| 3 | 0 | 1 | 3 | count[0] > 0 → serve, count[0]-- |
| 4 | 0 | 0 | 3 | count[0] == 0 → **trava aqui** |

Ninguém mais quer sanduíche tipo `0`, e ainda restam 2 sanduíches tipo `0` na pilha (índices 3 e o 0 que acabou de travar já foi contabilizado — na prática restam os sanduíches nos índices 3 e o processo para no índice 3). Alunos restantes na fila: `count[0] + count[1] = 0 + 3 = 3`.

Resultado final: `3` ✔ (bate com o enunciado)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para contar preferências, outra para consumir a pilha de sanduíches
- **Espaço:** O(1) — só dois contadores, independente de `n`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int countStudents(int[] students, int[] sandwiches) {
    int[] count = new int[2]; // count[0] = nº de alunos que preferem circular, count[1] = quadrado
    for (int pref : students) {
        count[pref]++;
    }

    for (int tipo : sandwiches) {
        if (count[tipo] == 0) {
            break; // ninguém na fila quer mais este topo: processo trava aqui
        }
        count[tipo]--; // "serve" um aluno com essa preferência
    }

    return count[0] + count[1]; // quem sobrou nunca vai conseguir comer
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

- Simular literalmente com uma fila que rotaciona sem uma condição de parada por "ciclo completo sem progresso" — sem essa checagem, o código entra em loop infinito quando sobra um sanduíche que ninguém quer.
- Esquecer que a ordem original dos alunos deixa de importar depois da observação central — tentar preservar a ordem exata da fila é trabalho desnecessário para a resposta pedida (a contagem final).
- Confundir índice do sanduíche com o array de contagem — `sandwiches[i]` é `0` ou `1`, que é usado diretamente como índice em `count[tipo]`, não precisa de mapeamento extra.
- Parar a contagem de sanduíches cedo demais ou tarde demais — o `break` deve ocorrer assim que o **primeiro** sanduíche sem candidatos aparece, porque a pilha só é consumida do topo pra baixo, em ordem.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Todos conseguem comer | `students=[1,1,0,0], sandwiches=[0,1,0,1]` | 0 | a rotação eventualmente serve todo mundo |
| Trava imediata no primeiro sanduíche | `students=[0,0,0], sandwiches=[1,1,1]` | 3 | ninguém quer o tipo 1 desde o início, todos ficam presos |
| Preferências uniformes que batem exatamente | `students=[1,1], sandwiches=[1,1]` | 0 | contadores se esgotam junto com a pilha, sem sobra |
| Um único aluno e sanduíche que não batem | `students=[0], sandwiches=[1]` | 1 | caso mínimo de travamento total |

## 🔗 Conexões

- Problemas irmãos: [2073] Time Needed to Buy Tickets (outra simulação de fila que se resolve com contagem/matemática em vez de simulação literal), [0933] Number of Recent Calls (fila real onde a ordem importa e não pode ser substituída por contagem)
- No backend: essa troca de "simulação passo a passo" por "contagem agregada" é o mesmo raciocínio usado para otimizar filas de atendimento com categorias limitadas (ex.: filas de suporte com poucos tipos de chamado) — quando o número de categorias é pequeno e fixo, muitas vezes dá para prever o resultado final sem simular cada rotação individual.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
