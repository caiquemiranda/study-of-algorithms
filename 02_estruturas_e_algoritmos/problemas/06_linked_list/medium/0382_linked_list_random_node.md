# [0382] Linked List Random Node

> 🔗 [LeetCode 382](https://leetcode.com/problems/linked-list-random-node/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#ReservoirSampling` `#Randomized` `#Medium`

## 📜 O Problema

Dada uma linked list simples, retorne o valor de um nó **aleatório**, com **probabilidade igual** para cada nó. Implemente a classe `Solution`:
- `Solution(ListNode head)`: inicializa o objeto com a `head` da lista.
- `int getRandom()`: escolhe um nó aleatoriamente e retorna seu valor. Todos os nós devem ter a mesma probabilidade de serem escolhidos.

**Exemplos:**
```
Input:
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1,2,3]], [], [], [], [], []]
Output:
[null, 1, 3, 2, 2, 3]

Explicação: getRandom() deve retornar 1, 2 ou 3, cada um com probabilidade 1/3.
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 10^4]`, até `10^4` chamadas a `getRandom` → volume razoável; O(n) por chamada (percorrer a lista) já é aceitável dentro do limite
- Follow-up "e se a lista for extremamente grande e o tamanho **desconhecido**?" e "sem usar espaço extra" → **esta é a pergunta central do problema**: se desse para saber o tamanho `n` de antemão (ou guardar todos os nós num array), bastaria sortear um índice de `0` a `n-1` — o desafio real é escolher uniformemente **sem saber quantos nós existem até terminar de percorrer a lista**, e sem gastar memória proporcional a `n`

## 🧭 Como reconhecer o padrão

"Escolha um elemento aleatório de um stream de tamanho desconhecido, com probabilidade uniforme, numa única passada" é a assinatura do **reservoir sampling** — um algoritmo clássico de amostragem, aqui aplicado a uma linked list porque ela só permite percorrer para frente, sem acesso por índice nem tamanho conhecido de antemão (a mesma limitação que já motiva fast & slow e outras técnicas da categoria, ver [fundamentos](../../../fundamentos/06_linked_list.md)).

## 🐢 Solução 1 — Força bruta (copiar valores para um array no construtor)

No construtor, percorre a lista uma vez e copia todos os valores para um array. Em cada `getRandom()`, sorteia um índice uniforme de `0` a `n-1` (agora que `n` é conhecido) e retorna `array[índice]` em O(1).

- Tempo: O(n) no construtor, O(1) por chamada de `getRandom` · Espaço: O(n) para o array
- **Por que não basta:** é rápida por chamada, mas o follow-up pede explicitamente uma solução que funcione **sem conhecer o tamanho da lista de antemão** e **sem espaço extra** — guardar todos os valores num array viola as duas condições ao mesmo tempo (usa O(n) de memória e depende de já saber que a lista tem fim antes de processá-la).

## 💡 Solução 2 — A ideia otimizada (intuição — reservoir sampling)

Percorre a lista **uma única vez**, nó a nó, mantendo um "resultado atual" candidato. No `i`-ésimo nó visitado (contando de 1), substitui o resultado atual pelo valor desse nó com probabilidade `1/i`. A sacada: isso garante, **matematicamente**, que ao final da travessia cada nó teve exatamente `1/n` de chance de ser o valor retornado — mesmo sem nunca saber, durante o percurso, qual é o `n` final. Não precisa saber o tamanho antes: a cada passo, a decisão só depende de "quantos nós eu já vi até agora" (`i`), não de quantos ainda faltam.

## 🎬 Exemplo passo a passo

`head = [1,2,3]` — em vez de traçar uma única execução (o resultado é aleatório por natureza), a tabela abaixo prova que cada nó termina com probabilidade exatamente `1/3`, o que é a garantia de corretude do algoritmo:

| Nó (posição `i`) | P(escolhido no passo `i`) | P(sobrevive aos passos seguintes, sem ser sobrescrito) | P(é o resultado final) |
|---|---|---|---|
| valor 1 (`i=1`) | `1/1 = 1` (único candidato) | não sobrescrito no passo 2 (`1 - 1/2`) **e** no passo 3 (`1 - 1/3`) → `1/2 × 2/3` | `1 × 1/2 × 2/3 = 1/3` |
| valor 2 (`i=2`) | `1/2` | não sobrescrito no passo 3 (`1 - 1/3 = 2/3`) | `1/2 × 2/3 = 1/3` |
| valor 3 (`i=3`) | `1/3` | não há passo seguinte | `1/3` |

Resultado: cada um dos 3 nós tem probabilidade `1/3` de ser o valor retornado ✔ — exatamente a garantia exigida pelo enunciado ("cada nó deve ter probabilidade igual").

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) por chamada de `getRandom` — percorre a lista inteira uma vez (sem `n` conhecido de antemão, não há como fazer melhor que uma passada completa)
- **Espaço:** O(1) — nenhuma estrutura auxiliar, só o contador `i` e o resultado corrente

## 💻 Implementações

### Java (referência completa e comentada)
```java
class Solution {
    private final ListNode head;
    private final Random rand = new Random();

    public Solution(ListNode head) {
        this.head = head; // não copia nada: só guarda a referência
    }

    public int getRandom() {
        int resultado = 0;
        int i = 0;
        ListNode cur = head;

        while (cur != null) {
            i++;
            // A cada nó, substitui o resultado com probabilidade 1/i.
            // rand.nextInt(i) sorteia um inteiro uniforme em [0, i-1]; comparar com 0
            // dá exatamente probabilidade 1/i de "vencer" nesta rodada.
            if (rand.nextInt(i) == 0) {
                resultado = cur.val;
            }
            cur = cur.next;
        }

        return resultado;
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

- **Sortear com peso errado (ex.: `1/n` fixo em vez de `1/i` crescente)**: sem recalcular a probabilidade a cada nó com base em quantos já foram vistos, a distribuição final não é uniforme — nós do início ou do fim ficam favorecidos.
- **Achar que basta sortear o primeiro nó com prob. 100% e nunca mais mudar**: viola completamente a uniformidade — só o primeiro nó teria chance de ser escolhido.
- **Confundir "espaço O(1)" com "tempo O(1)"**: reservoir sampling é O(1) de **espaço**, mas ainda é O(n) de **tempo** por chamada — não existe forma de escolher uniformemente sem ver todos os nós ao menos uma vez, já que o tamanho não é conhecido de antemão.
- **Testar a corretude olhando o resultado de uma única chamada**: como o algoritmo é probabilístico, validar exige rodar `getRandom()` muitas vezes e checar se a distribuição dos resultados se aproxima de uniforme — um único resultado não prova nem refuta a implementação.

## 🧪 Casos de teste para validar

| Caso | Input | Comportamento esperado | Por quê |
|---|---|---|---|
| Lista de 1 nó | `head = [7]` | `getRandom()` sempre retorna `7` | único candidato possível, probabilidade 1 |
| Lista de 2 nós, muitas chamadas | `head = [1,2]`, 10.000 chamadas | aproximadamente 50% de `1` e 50% de `2` | valida a uniformidade estatisticamente |
| Lista maior, exemplo do enunciado | `head = [1,2,3]`, várias chamadas | aproximadamente 1/3 para cada valor | trace de probabilidades acima |
| Valores repetidos na lista | `head = [5,5,5]` | sempre retorna `5` | garante que a lógica de índice/posição funciona independente dos valores serem iguais |
| Lista bem maior (validação de escala) | lista com 10^4 nós | cada valor com probabilidade ~`1/10^4` ao longo de muitas chamadas | valida que o algoritmo não degrada com `n` grande, já que é O(n) por chamada de qualquer forma |

## 🔗 Conexões

- Problemas irmãos: **[0398] Random Pick Index** (mesma ideia de reservoir sampling, aplicada a um array com possíveis valores repetidos, escolhendo entre os índices que batem um alvo), **[0384] Shuffle an Array** (também usa aleatoriedade uniforme, mas com o Fisher-Yates shuffle em vez de reservoir sampling)
- No backend: reservoir sampling é usado para **amostrar uniformemente de streams de dados de tamanho desconhecido** — por exemplo, escolher uma amostra representativa de logs de um pipeline que nunca "termina" de verdade, ou selecionar aleatoriamente registros de uma tabela grande demais para carregar inteira em memória (`ORDER BY RANDOM() LIMIT 1` de bancos de dados, quando implementado eficientemente, usa uma ideia semelhante).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
