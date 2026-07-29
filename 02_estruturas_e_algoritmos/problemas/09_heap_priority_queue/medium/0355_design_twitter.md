# [0355] Design Twitter

> 🔗 [LeetCode 355](https://leetcode.com/problems/design-twitter/) · Dificuldade: 🟡 medium · Categoria: [`09_heap_priority_queue`](../../../fundamentos/09_heap_priority_queue.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Heap` `#MergeKFontes` `#HashTable` `#Medium`

## 📜 O Problema

Projete uma versão simplificada do Twitter. Implemente a classe `Twitter`:
- `postTweet(userId, tweetId)`: publica um tweet (IDs sempre únicos).
- `getNewsFeed(userId)`: retorna os **10 tweets mais recentes** no feed do usuário — postados por ele mesmo ou por quem ele segue —, do mais recente para o mais antigo.
- `follow(followerId, followeeId)`: `followerId` passa a seguir `followeeId`.
- `unfollow(followerId, followeeId)`: `followerId` deixa de seguir `followeeId`.

**Exemplos:**
```
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1,5], [1], [1,2], [2,6], [1], [1,2], [1]]
Output:
[null, null, [5], null, null, [6,5], null, [5]]

Explicação:
postTweet(1,5) → usuário 1 posta o tweet 5;
getNewsFeed(1) → [5] (só o próprio tweet);
follow(1,2) → usuário 1 passa a seguir o usuário 2;
postTweet(2,6) → usuário 2 posta o tweet 6;
getNewsFeed(1) → [6,5] (tweet 6 é mais recente que o 5);
unfollow(1,2) → usuário 1 deixa de seguir o usuário 2;
getNewsFeed(1) → [5] (não vê mais os tweets do usuário 2)
```

**Restrições (e o que elas denunciam):**
- `1 <= userId, followerId, followeeId <= 500` → até 500 usuários, um número de "fontes" (pessoas seguidas) gerenciável por usuário
- `0 <= tweetId <= 10^4`, IDs únicos → cada tweet é identificável sem ambiguidade
- até `3 * 10^4` chamadas no total → `getNewsFeed` pode ser chamado muitas vezes; refazer um trabalho caro (como ordenar todos os tweets de todos os seguidos) a cada chamada é o que a solução otimizada evita
- "os 10 mais recentes" → o número fixo (10) é o sinal clássico de **Top-K com heap**: não é preciso ordenar tudo, só manter os 10 melhores candidatos em cada momento

## 🧭 Como reconhecer o padrão

Cada usuário seguido é uma **fonte já ordenada** de tweets (cada usuário posta em ordem cronológica crescente). "Combine os itens mais recentes de várias fontes ordenadas" é a assinatura exata de **merge de N fontes com heap** — ver [fundamentos](../../../fundamentos/09_heap_priority_queue.md), seção "Como Reconhecer": *"se pede 'mescle N listas/fontes ordenadas' → heap com um cursor por fonte"*. Aqui, cada usuário seguido (+ o próprio usuário) é uma fonte, e o "cursor" percorre os tweets dessa fonte do mais recente para o mais antigo.

## 🐢 Solução 1 — Força bruta (juntar tudo, ordenar, pegar os 10 primeiros)

Em `getNewsFeed`, junta numa lista só **todos** os tweets do usuário e de todos que ele segue, ordena essa lista inteira por timestamp decrescente, e retorna os 10 primeiros.

- Tempo: O(T log T) por chamada de `getNewsFeed`, onde `T` é o total de tweets de todas as fontes envolvidas · Espaço: O(T)
- **Por que não basta:** com até `3 × 10^4` chamadas no total e um usuário podendo seguir até 500 pessoas, reordenar **todos** os tweets de **todas** as fontes a cada chamada de `getNewsFeed` é um desperdício gigantesco — na prática, só os 10 tweets mais recentes de cada fonte (no máximo) importam para o resultado final.

## 💡 Solução 2 — A ideia otimizada (intuição)

Cada usuário mantém sua própria lista de tweets, já em ordem cronológica (cada `postTweet` só adiciona no fim, com um contador de tempo global crescente). Em `getNewsFeed`: para cada fonte (o próprio usuário + cada um dos seguidos), empurra num **max-heap** só o tweet **mais recente** dessa fonte, junto com um "cursor" indicando de onde ele veio. Repete 10 vezes (ou até o heap esvaziar): tira o topo do heap (o mais recente entre todos os candidatos atuais), adiciona ao resultado, e empurra o **próximo** tweet (mais antigo) daquela mesma fonte, se houver. Isso nunca materializa mais do que "1 candidato por fonte" no heap de cada vez — é o mesmo padrão de **merge de K listas ordenadas**.

## 🎬 Exemplo passo a passo

Sequência do enunciado, focando em `getNewsFeed(1)` após `follow(1,2)` e `postTweet(2,6)`:

Estado: usuário 1 tem tweets `[(tempo=1, id=5)]`; usuário 2 tem tweets `[(tempo=2, id=6)]`; usuário 1 segue o usuário 2 (e a si mesmo, implicitamente).

| Passo | Heap (topo = maior tempo) | Ação | Resultado parcial |
|---|---|---|---|
| início | empurra o tweet mais recente de cada fonte: `(2,id6)` de u2, `(1,id5)` de u1 | heap = `{(2,6), (1,5)}` | `[]` |
| 1 | topo = `(2,6)` | tira do heap, adiciona `6`; fonte u2 não tem mais tweets — nada a empurrar | `[6]` |
| 2 | topo = `(1,5)` | tira do heap, adiciona `5`; fonte u1 não tem mais tweets — nada a empurrar | `[6,5]` |
| fim | heap vazio | para (também já bateria o limite de 10) | `[6,5]` |

Resultado final: `[6, 5]` ✔ — bate com o esperado no enunciado.

## ⚡ Complexidade da solução ótima

- **Tempo:** `postTweet`/`follow`/`unfollow` são O(1). `getNewsFeed` é O(F log F) — `F` é o número de fontes (seguidos + o próprio usuário, no máximo 501); o heap nunca guarda mais que `F` elementos, e o laço roda no máximo 10 vezes
- **Espaço:** O(F) para o heap por chamada de `getNewsFeed`, mais O(T) total para armazenar todos os tweets já postados (inevitável — são o próprio dado do sistema)

## 💻 Implementações

### Java (referência completa e comentada)
```java
class Twitter {
    private int time = 0; // relógio lógico: cresce a cada postTweet, define a ordem cronológica
    private final Map<Integer, List<int[]>> tweets = new HashMap<>();     // userId -> [tempo, tweetId] em ordem crescente
    private final Map<Integer, Set<Integer>> following = new HashMap<>(); // userId -> quem ele segue

    public void postTweet(int userId, int tweetId) {
        tweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(new int[]{time++, tweetId});
    }

    public List<Integer> getNewsFeed(int userId) {
        // Max-heap por tempo: cada entrada é [tempo, tweetId, índiceDaFonte, índiceNaLista].
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> b[0] - a[0]);

        Set<Integer> fontes = new HashSet<>(following.getOrDefault(userId, Collections.emptySet()));
        fontes.add(userId); // o próprio usuário sempre aparece no feed dele

        List<List<int[]>> listas = new ArrayList<>();
        for (int src : fontes) {
            List<int[]> lista = tweets.getOrDefault(src, Collections.emptyList());
            if (!lista.isEmpty()) {
                int idx = lista.size() - 1; // cursor começa no MAIS RECENTE (fim da lista)
                int[] tw = lista.get(idx);
                heap.offer(new int[]{tw[0], tw[1], listas.size(), idx});
                listas.add(lista);
            }
        }

        List<Integer> resultado = new ArrayList<>();
        while (!heap.isEmpty() && resultado.size() < 10) {
            int[] topo = heap.poll();
            resultado.add(topo[1]); // tweetId do mais recente entre os candidatos atuais

            int listaIdx = topo[2], proximoIdx = topo[3] - 1; // anda o cursor DESSA fonte p/ trás no tempo
            if (proximoIdx >= 0) {
                int[] proximo = listas.get(listaIdx).get(proximoIdx);
                heap.offer(new int[]{proximo[0], proximo[1], listaIdx, proximoIdx});
            }
        }

        return resultado;
    }

    public void follow(int followerId, int followeeId) {
        if (followerId != followeeId) { // regra do enunciado: um usuário não pode se seguir
            following.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
        }
    }

    public void unfollow(int followerId, int followeeId) {
        Set<Integer> seguidos = following.get(followerId);
        if (seguidos != null) {
            seguidos.remove(followeeId);
        }
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

- **Esquecer de incluir o próprio usuário como uma "fonte" em `getNewsFeed`**: o enunciado exige tweets do usuário **e** de quem ele segue — omitir a si mesmo perde os próprios tweets do feed.
- **Reordenar todos os tweets de todas as fontes a cada chamada**: funciona, mas é exatamente o desperdício que a solução com heap evita — só o candidato "atual" de cada fonte precisa estar no heap a qualquer momento.
- **Usar um min-heap em vez de max-heap (ou esquecer de inverter o comparator)**: o objetivo é sempre pegar o tweet **mais recente** disponível entre os candidatos — um min-heap traria os mais antigos primeiro, invertendo a ordem do feed.
- **Não avançar o cursor da fonte de onde saiu o topo do heap**: sem empurrar o próximo tweet (mais antigo) daquela mesma fonte, o heap "esquece" tweets mais antigos dela que ainda poderiam entrar nos 10 primeiros.

## 🧪 Casos de teste para validar

| Caso | Sequência | Esperado | Por quê |
|---|---|---|---|
| Feed vazio | `getNewsFeed(1)` sem nenhum post | `[]` | nenhuma fonte tem tweets, heap começa e termina vazio |
| Mais de 10 tweets do próprio usuário | 15 `postTweet(1, i)` seguidos de `getNewsFeed(1)` | os 10 IDs mais recentes, do mais novo ao mais velho | valida o limite de 10 e a ordem decrescente de tempo |
| Usuário tentando seguir a si mesmo | `follow(1,1)` | não deve ter efeito (regra "não pode seguir a si mesmo") | o próprio usuário já está implicitamente no feed dele |
| Unfollow de alguém que não é seguido | `unfollow(1,2)` sem `follow(1,2)` antes | nenhum erro, `getNewsFeed` inalterado | `unfollow` deve ser no-op seguro |
| Exemplo completo do enunciado | sequência do enunciado | `[null,null,[5],null,null,[6,5],null,[5]]` | trace acima |

## 🔗 Conexões

- Problemas irmãos: **[0023] Merge k Sorted Lists** (o mesmo padrão de "heap com um cursor por fonte", aplicado a listas encadeadas em vez de listas de tweets), **[0295] Find Median from Data Stream** (outro problema de heap para um sistema que recebe dados continuamente)
- No backend: gerar um "feed" combinando várias fontes ordenadas por tempo, sem materializar tudo de uma vez, é exatamente como funcionam os **feeds de rede social em produção** (fan-out on read: o feed é montado na hora, mesclando as fontes seguidas) e sistemas de **agregação de logs distribuídos** (mesclar logs de múltiplos servidores, cada um já ordenado por timestamp, para reconstruir uma timeline global).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
