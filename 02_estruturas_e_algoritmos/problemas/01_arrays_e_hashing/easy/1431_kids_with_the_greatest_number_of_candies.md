# [1431] Kids With the Greatest Number of Candies

> 🔗 [LeetCode 1431](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#Array` `#Easy`

## 📜 O Problema

Existem `n` crianças com doces. Você recebe um array `candies`, onde `candies[i]` representa a quantidade de doces que a `i`-ésima criança tem, e um inteiro `extraCandies`, o número de doces extras que você tem.

Retorne um array booleano `result` de tamanho `n`, onde `result[i]` é `true` se, depois de dar todos os `extraCandies` para a `i`-ésima criança, ela tiver a **maior** quantidade de doces entre todas as crianças, ou `false` caso contrário.

Note que **múltiplas** crianças podem ter a maior quantidade de doces.

**Exemplos:**
```
Input:  candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

Input:  candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]

Input:  candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

**Restrições (e o que elas denunciam):**
- `2 <= n <= 100`, `1 <= candies[i] <= 100`, `1 <= extraCandies <= 50` → tudo pequeno, O(n) resolve com folga

## 🧭 Como reconhecer o padrão

"Após aplicar um bônus, esse elemento se torna o maior?" é resolvido achando o máximo atual do array primeiro (uma passada), e depois comparando `elemento + bônus >= máximo` para cada elemento (outra passada) — não precisa simular a distribuição do bônus de verdade em cada criança.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada criança `i`, simular dar `extraCandies` a ela, recalcular o máximo do array INTEIRO com essa mudança temporária, e verificar se a criança `i` tem esse novo máximo.

- Tempo: O(n²) — para cada criança, recalcula o máximo do array inteiro do zero · Espaço: O(1) extra
- **Por que não basta:** o máximo das OUTRAS crianças nunca muda quando você dá bônus só para a criança `i`; então o máximo original do array (sem bônus nenhum) já é a referência correta para comparar contra `candies[i] + extraCandies`.

## 💡 Solução 2 — A ideia otimizada (intuição)

Encontre o `maximoOriginal` do array numa única passada. Para cada criança, verifique se `candies[i] + extraCandies >= maximoOriginal`.

## 🎬 Exemplo passo a passo

`candies = [2,3,5,1,3]`, `extraCandies = 3` — `maximoOriginal = 5`

| Passo | i | candies[i] | candies[i]+3 | >= 5? |
|---|---|---|---|---|
| 1 | 0 | 2 | 5 | sim |
| 2 | 1 | 3 | 6 | sim |
| 3 | 2 | 5 | 8 | sim |
| 4 | 3 | 1 | 4 | não |
| 5 | 4 | 3 | 6 | sim |

Resultado final: `[true,true,true,false,true]` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — uma passada para achar o máximo + uma passada para comparar
- **Espaço:** O(n) — para o array de resultado

## 💻 Implementações

### Java (referência completa e comentada)
```java
public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
    int maximoOriginal = 0;
    for (int c : candies) {
        maximoOriginal = Math.max(maximoOriginal, c);
    }

    List<Boolean> resultado = new ArrayList<>();
    for (int c : candies) {
        resultado.add(c + extraCandies >= maximoOriginal); // o máximo original nunca muda com o bônus de UM aluno
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

- Recalcular o máximo do array a cada criança (achando que o bônus mudaria o máximo "global") — o máximo das OUTRAS crianças nunca é afetado pelo bônus dado a uma única criança específica, então o máximo original já basta.
- Usar `>` em vez de `>=` — "ter a MAIOR quantidade" inclui EMPATAR com o máximo, não só superá-lo estritamente (ver nota do enunciado: "múltiplas crianças podem ter a maior quantidade").
- Esquecer que a comparação é sempre contra o `maximoOriginal` (sem bônus), não contra o máximo COM bônus de todo mundo — o bônus é hipotético, dado a UMA criança de cada vez, não a todas simultaneamente.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Vários alcançam o máximo | `candies=[2,3,5,1,3], extraCandies=3` | [true,true,true,false,true] | 4 das 5 crianças alcançam ou superam o máximo original (5) com o bônus |
| Só uma alcança | `candies=[4,2,1,1,2], extraCandies=1` | [true,false,false,false,false] | só quem já tinha o máximo (4) continua no topo com só 1 extra |
| Empate exato | `candies=[12,1,12], extraCandies=10` | [true,false,true] | ambos os "12" já são o máximo, o "1"+10=11 não alcança |
| Bônus muito grande | `candies=[1,1], extraCandies=50` | [true,true] | qualquer criança ultrapassa o máximo original com um bônus grande |

## 🔗 Conexões

- Problemas irmãos: [0747] Largest Number At Least Twice of Others (mesmo domínio de comparar cada elemento contra o máximo do array), [1051] Height Checker (mesma técnica de comparar cada elemento contra uma referência pré-calculada)
- No backend: simulação de "e se" em sistemas de bônus/gamificação (ex.: "se este usuário ganhasse pontos extras, ele ficaria no topo do ranking?") sem precisar recalcular o ranking inteiro para cada simulação.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
