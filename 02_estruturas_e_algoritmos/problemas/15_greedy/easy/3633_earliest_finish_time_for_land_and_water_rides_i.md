# [3633] Earliest Finish Time for Land and Water Rides I

> 🔗 [LeetCode 3633](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/) · Dificuldade: 🟢 easy · Categoria: [`15_greedy`](../../../fundamentos/15_greedy.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Greedy` `#BuscaBinaria` `#Easy`

## 📜 O Problema

Um parque tem atrações de **terra** (`landStartTime[i]`, `landDuration[i]`) e de **água** (`waterStartTime[j]`, `waterDuration[j]`). Um turista precisa andar em **exatamente uma** atração de cada categoria, em **qualquer ordem**. Uma atração só pode começar no horário de abertura dela ou depois; ao terminar uma, o turista pode embarcar imediatamente na outra (se já estiver aberta) ou esperar. Retorne o **menor horário possível** para terminar as duas atrações.

**Exemplos:**
```
Input:  landStartTime=[2,8], landDuration=[4,1], waterStartTime=[6], waterDuration=[3]    Output: 9
        (terra 0: começa 2, termina 6 → água 0: começa 6, termina 9)
Input:  landStartTime=[5], landDuration=[3], waterStartTime=[1], waterDuration=[10]        Output: 14
        (água 0: começa 1, termina 11 → terra 0: começa 11, termina 14)
```

**Restrições (e o que elas denunciam):**
- `1 <= n, m <= 100` → produto de todas as combinações (n × m × 2 ordens) é no máximo 20.000, força bruta passaria fácil, mas existe uma observação que elimina a necessidade de testar todas as combinações
- "andar em exatamente uma atração de cada categoria, **em qualquer ordem**" → não existe restrição de pareamento — qualquer atração de terra pode combinar com qualquer atração de água, o que abre espaço para uma escolha gulosa independente de qual será a segunda atração
- Terminar uma atração mais cedo **nunca atrapalha**: começar a próxima atração antes só pode terminar mais cedo ou igual, nunca mais tarde

## 🧭 Como reconhecer o padrão

A pergunta-chave é: "dado que vou fazer terra **depois** de água (ou vice-versa), qual atração da primeira categoria eu deveria escolher?" Como o horário de término da segunda atração é `max(terminoDaPrimeira, aberturaDaSegunda) + duraçãoDaSegunda`, e essa expressão só **cresce** (ou mantém) conforme `terminoDaPrimeira` aumenta, a melhor escolha da primeira atração é **sempre** a que termina mais cedo — independentemente de qual será a segunda. Essa é uma escolha local ótima que não depende do resto da decisão: a marca registrada de **greedy**.

## 🐢 Solução 1 — Força bruta

Para cada uma das duas ordens possíveis (terra→água ou água→terra), testar **todas** as combinações `(i, j)` de atração de terra com atração de água, calculando o horário de término e guardando o mínimo global.

- Tempo: O(n × m) · Espaço: O(1)
- **Por que não basta:** embora passe tranquilamente nas restrições deste problema, testa combinações redundantes — para uma ordem fixa (ex.: terra antes de água), a atração de terra ideal é sempre a mesma (a que termina mais cedo), não importa qual atração de água vem depois. Repetir essa comparação para cada `j` é trabalho desperdiçado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para a ordem "terra primeiro, água depois": o horário de término final é `max(terminoTerra[i], waterStartTime[j]) + waterDuration[j]`. Fixando `j`, essa expressão é **monotonicamente não decrescente** em `terminoTerra[i]` — ou seja, diminuir `terminoTerra[i]` nunca piora o resultado. Logo, a melhor escolha de `i` **não depende de `j`**: é sempre a atração de terra com o **menor horário de término** (`min(landStartTime[i] + landDuration[i])`).

Isso reduz o problema a: calcular o menor término de terra (O(n)), depois testar contra **cada** atração de água (O(m)) para achar o melhor resultado nessa ordem. Repita simetricamente para a ordem "água primeiro, terra depois", e retorne o menor dos dois resultados.

## 🎬 Exemplo passo a passo

`landStartTime=[2,8], landDuration=[4,1]` → términos de terra: `[6, 9]` · `waterStartTime=[6], waterDuration=[3]`

| Ordem | Melhor 1ª atração (menor término) | Combina com | Cálculo | Resultado da ordem |
|---|---|---|---|---|
| Terra → Água | terra 0, termina em 6 | água 0 (única) | `max(6, 6) + 3` | 9 |
| Água → Terra | água 0, termina em `6+3=9` | testa terra 0: `max(9,2)+4=13` · terra 1: `max(9,8)+1=10` | melhor: 10 | 10 |

Resultado final: `min(9, 10) = 9` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n + m) — uma passada para achar o menor término de cada categoria, mais uma passada em cada uma para testar contra a categoria oposta
- **Espaço:** O(1) — só variáveis acumuladoras

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int earliestFinishTime(int[] landStartTime, int[] landDuration,
                               int[] waterStartTime, int[] waterDuration) {
    // A melhor 1ª atração de cada categoria é sempre a que termina mais cedo,
    // não importa qual será a 2ª (a expressão do término final é monotônica nisso).
    int minTerminoTerra = Integer.MAX_VALUE;
    for (int i = 0; i < landStartTime.length; i++) {
        minTerminoTerra = Math.min(minTerminoTerra, landStartTime[i] + landDuration[i]);
    }
    int minTerminoAgua = Integer.MAX_VALUE;
    for (int j = 0; j < waterStartTime.length; j++) {
        minTerminoAgua = Math.min(minTerminoAgua, waterStartTime[j] + waterDuration[j]);
    }

    int melhorResultado = Integer.MAX_VALUE;

    // Ordem: terra (a melhor) -> testa cada atração de água
    for (int j = 0; j < waterStartTime.length; j++) {
        int termino = Math.max(minTerminoTerra, waterStartTime[j]) + waterDuration[j];
        melhorResultado = Math.min(melhorResultado, termino);
    }
    // Ordem: água (a melhor) -> testa cada atração de terra
    for (int i = 0; i < landStartTime.length; i++) {
        int termino = Math.max(minTerminoAgua, landStartTime[i]) + landDuration[i];
        melhorResultado = Math.min(melhorResultado, termino);
    }

    return melhorResultado;
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

- **Achar que precisa testar todas as combinações `(i, j)`**: é o erro mais comum — a prova de que a atração com menor término é sempre a melhor escolha (independente da segunda) é o que justifica reduzir de O(n×m) para O(n+m); pular essa observação leva a uma solução correta, mas desnecessariamente mais lenta.
- **Esquecer de testar as DUAS ordens**: a ordem ótima (terra→água ou água→terra) não é fixa — depende dos horários de abertura e durações específicas de cada instância; ignorar uma das ordens pode perder o resultado ótimo (ver exemplo 2, onde água→terra vence).
- **Confundir "menor duração" com "menor término"**: a atração ideal para ser a **primeira** é a que **termina** mais cedo (`start + duration`), não necessariamente a de menor duração isolada — uma atração que abre mais cedo mas dura mais pode terminar antes de uma que abre tarde e é rápida.
- **Esquecer o `max()` ao encadear**: se a primeira atração termina antes da segunda abrir, o turista precisa **esperar** até a abertura — usar só a soma (`terminoPrimeira + duraçãoSegunda`) sem o `max()` ignora esse tempo de espera.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Uma atração de cada | `landStartTime=[5], landDuration=[3], waterStartTime=[1], waterDuration=[10]` | 14 | trace do enunciado, testa a ordem água→terra vencendo |
| Sem espera necessária | `landStartTime=[0], landDuration=[5], waterStartTime=[0], waterDuration=[5]` | 10 | ambas abrem no início, nenhuma ordem precisa esperar |
| Água abre muito tarde | `landStartTime=[1], landDuration=[1], waterStartTime=[100], waterDuration=[1]` | 101 | testa espera longa forçada pela abertura tardia |
| Múltiplas opções de cada lado | `landStartTime=[2,8], landDuration=[4,1], waterStartTime=[6], waterDuration=[3]` | 9 | trace acima, escolha da melhor atração de terra |
| Terra e água com mesma abertura | `landStartTime=[3], landDuration=[2], waterStartTime=[3], waterDuration=[2]` | 7 | qualquer ordem dá o mesmo resultado nesse caso simétrico |

## 🔗 Conexões

- Problemas irmãos: **[0435] Non-overlapping Intervals** (outra decisão gulosa sobre agendamento de intervalos), **[0455] Assign Cookies** (greedy: sempre combine o candidato "mais barato" disponível primeiro)
- No backend: encadear duas etapas de um pipeline (ex.: processar um job de import seguido de um job de validação, ou vice-versa) e escolher a ordem/instância que minimiza o tempo total de espera usa exatamente esse raciocínio guloso — a etapa mais rápida disponível primeiro nunca piora o resultado final.

**Nota de reclassificação:** o cache sugeria `05_busca_binaria` (tags do LeetCode incluindo `two-pointers`, `binary-search`, `sorting`), mas a solução ótima não precisa ordenar nem buscar — é uma observação gulosa direta (a melhor 1ª atração de cada categoria é sempre a de menor término, independente da 2ª escolha), resolvida em O(n+m) sem estrutura auxiliar. Por isso o documento foi classificado em `15_greedy`.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
