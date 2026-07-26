# [0929] Unique Email Addresses

> 🔗 [LeetCode 929](https://leetcode.com/problems/unique-email-addresses/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-25 · Revisões: —

Tags: `#HashTable` `#Array` `#String` `#Easy`

## 📜 O Problema

Todo **e-mail válido** consiste num **nome local** e um **nome de domínio**, separados por `'@'`. Além de letras minúsculas, o e-mail pode conter um ou mais `'.'` ou `'+'`.

Se você adicionar pontos `'.'` entre caracteres no **nome local**, o e-mail é encaminhado para o mesmo endereço sem os pontos (essa regra não se aplica ao domínio). Se você adicionar um `'+'` no nome local, tudo depois do primeiro `+` **é ignorado** (também só no nome local).

Dado um array de strings `emails`, retorne **o número de endereços diferentes que realmente recebem e-mails**.

**Exemplos:**
```
Input:  emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explicação: "testemail@leetcode.com" e "testemail@lee.tcode.com" recebem, de fato, os e-mails.

Input:  emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
```

**Restrições (e o que elas denunciam):**
- `1 <= emails.length <= 100`, tamanhos pequenos → O(n×L) resolve com folga
- regras de normalização só afetam o "local name" (antes do @), nunca o domínio → precisa separar a string em duas partes pelo `@` antes de normalizar
- pontos são removidos, e tudo depois do primeiro `+` é ignorado, só no local name

## 🧭 Como reconhecer o padrão

"Normalizar cada item segundo uma regra e contar quantos resultados distintos existem" é sempre resolvido aplicando a normalização a cada elemento e jogando o resultado num hash set — o set elimina duplicatas automaticamente, a resposta é o tamanho dele.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Normalizar cada e-mail construindo a string caractere por caractere com um loop manual que trata pontos e `+` ao mesmo tempo, e comparar cada normalizado com todos os anteriores já vistos.

- Tempo: O(n² × L) — comparação par a par das strings normalizadas · Espaço: O(n×L)
- **Por que não basta:** repete a comparação "já vi este e-mail normalizado?" par a par, quando um hash set decide isso em O(1) amortizado por inserção.

## 💡 Solução 2 — A ideia otimizada (intuição)

Para cada e-mail, separe em `local` e `domain` pelo primeiro `@`. No `local`, remova todos os pontos e corte tudo a partir do primeiro `+` (se existir). Reconstrua o e-mail normalizado como `localLimpo + "@" + domain` e adicione a um hash set. A resposta é o tamanho do set.

## 🎬 Exemplo passo a passo

`emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]`

| Passo | email original | local após cortar no '+' | local sem pontos | domain | normalizado |
|---|---|---|---|---|---|
| 1 | test.email+alex@leetcode.com | test.email | testemail | @leetcode.com | testemail@leetcode.com |
| 2 | test.e.mail+bob.cathy@leetcode.com | test.e.mail | testemail | @leetcode.com | testemail@leetcode.com (já existe) |
| 3 | testemail+david@lee.tcode.com | testemail | testemail | @lee.tcode.com | testemail@lee.tcode.com |

Set final: `{testemail@leetcode.com, testemail@lee.tcode.com}` → tamanho **2** ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(soma dos tamanhos dos e-mails)
- **Espaço:** O(n×L) — para o hash set

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int numUniqueEmails(String[] emails) {
    Set<String> normalizados = new HashSet<>();

    for (String email : emails) {
        int arroba = email.indexOf('@');
        String local = email.substring(0, arroba);
        String dominio = email.substring(arroba); // inclui o '@' para facilitar a concatenação depois

        int posMais = local.indexOf('+');
        if (posMais != -1) {
            local = local.substring(0, posMais); // descarta tudo a partir do primeiro '+'
        }
        local = local.replace(".", ""); // remove todos os pontos do local name

        normalizados.add(local + dominio);
    }
    return normalizados.size();
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

- Aplicar a remoção de pontos e o corte no `+` ao DOMÍNIO também — o enunciado é explícito que essas regras não se aplicam ao domínio; pontos no domínio (ex.: `"lee.tcode.com"`) fazem parte do endereço real.
- Cortar no `+` antes de remover os pontos, mas esquecer que o `+` pode vir DEPOIS de um ponto — a ordem das operações (cortar primeiro, depois limpar pontos do que sobrou) evita processar caracteres que já deveriam ter sido descartados.
- Usar `email.split("@")` sem tratar o caso de garantir só o PRIMEIRO `@`; `indexOf` + `substring` é mais explícito que isso importa.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Normalização combinada | `["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]` | 2 | dois primeiros e-mails normalizam para o mesmo endereço |
| Sem regras especiais | `["a@leetcode.com","b@leetcode.com","c@leetcode.com"]` | 3 | nenhuma normalização muda nada, todos distintos |
| Só ponto, sem + | `["a.b@x.com","ab@x.com"]` | 1 | pontos no local name são removidos |
| Domínio com ponto extra | `["a+x@sub.domain.com"]` | 1 | pontos no domínio NÃO são removidos, mas isso não afeta a contagem de um único e-mail |

## 🔗 Conexões

- Problemas irmãos: [0804] Unique Morse Code Words (mesmo padrão de "normalizar e contar distintos com hash set"), [0049] Group Anagrams (mesma ideia de canonicalizar uma string antes de agrupar/comparar)
- No backend: deduplicação de contatos de e-mail antes de uma campanha de marketing, evitando enviar a mesma mensagem duas vezes para o mesmo destinatário real por causa de variações de formatação do endereço.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
