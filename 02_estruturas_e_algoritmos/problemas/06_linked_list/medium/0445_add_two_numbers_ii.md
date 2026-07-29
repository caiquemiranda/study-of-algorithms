# [0445] Add Two Numbers II

> 🔗 [LeetCode 445](https://leetcode.com/problems/add-two-numbers-ii/) · Dificuldade: 🟡 medium · Categoria: [`06_linked_list`](../../../fundamentos/06_linked_list.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#LinkedList` `#Stack` `#Medium`

## 📜 O Problema

Duas linked lists não vazias representam dois inteiros não negativos, mas agora com o **dígito mais significativo primeiro** (ordem normal de leitura). Some os dois números e retorne o resultado como uma linked list, também com o dígito mais significativo primeiro.

**Exemplos:**
```
Input:  l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Explicação: 7243 + 564 = 7807.

Input:  l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Input:  l1 = [0], l2 = [0]
Output: [0]
```

**Restrições (e o que elas denunciam):**
- Número de nós em `[1, 100]` → O(n) é o esperado
- `0 <= Node.val <= 9` → cada nó é um dígito
- "os números não têm zero à esquerda, exceto o 0 em si" → mesma garantia do LC 2, sem dígitos de preenchimento artificiais
- Follow-up "resolva sem inverter as listas de entrada" → é a diferença central para o LC 2: lá a ordem invertida (unidades primeiro) já vinha "pronta" para somar da esquerda para a direita; aqui, para somar dígito a dígito é preciso processar das **unidades para trás**, mas o enunciado não quer que a solução destrua/reverta fisicamente as listas originais como efeito colateral

## 🧭 Como reconhecer o padrão

Somar dígitos "de trás para frente" a partir de uma estrutura que só permite ler "da frente para trás" é a assinatura clássica de usar uma **pilha**: empilhar os valores enquanto percorre a lista na ordem natural inverte automaticamente a ordem de leitura (LIFO), sem tocar em nenhum ponteiro `next` da lista original. É o mesmo raciocínio de "inverter sem inverter" que aparece sempre que uma lista encadeada precisa ser processada de trás para frente sem mutação.

## 🐢 Solução 1 — Força bruta (inverter as duas listas, somar, inverter o resultado)

Inverte `l1` e `l2` (com a técnica do LC 206), soma dígito a dígito como no LC 2 (agora que a ordem virou "unidades primeiro"), e no final inverte o resultado de volta para "mais significativo primeiro".

- Tempo: O(n) · Espaço: O(1) extra (fora a lista de saída)
- **Por que não basta:** o tempo e o espaço já seriam ótimos, mas essa abordagem **modifica fisicamente** a ordem dos ponteiros das listas de entrada — mesmo que dê para reverter de novo ao final, isso é um efeito colateral arriscado (se outra parte do sistema também tiver uma referência a `l1`/`l2` enquanto a soma está rodando, ela veria a lista temporariamente invertida). É exatamente o que o follow-up pede para evitar.

## 💡 Solução 2 — A ideia otimizada (intuição)

Empilha todos os dígitos de `l1` numa pilha, e todos os de `l2` noutra — isso **lê** cada lista da esquerda para a direita (ordem natural, sem mexer em nenhum ponteiro `next`), mas o efeito de empilhar (LIFO) já entrega os dígitos na ordem "unidades primeiro" na hora de desempilhar. Daí em diante, é a mesma soma com `carry` do LC 2: desempilha um dígito de cada pilha (ou `0`, se a pilha já esvaziou), soma com o carry, e **prepende** (insere no início) o novo nó ao resultado — como os dígitos saem das pilhas do menos para o mais significativo, prepender constrói o resultado já na ordem certa, sem precisar de uma reversão final.

## 🎬 Exemplo passo a passo

`l1 = [7,2,4,3]` (7243), `l2 = [5,6,4]` (564)

**Empilhar** (lendo cada lista da esquerda para a direita): `stack1 = [3,4,2,7]` (topo→3), `stack2 = [4,6,5]` (topo→4)

| Passo | pop stack1 | pop stack2 | carry (entra) | soma | dígito criado | carry (sai) | resultado (prepend) |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 4 | 0 | 7 | 7 | 0 | `7` |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 | `0 → 7` |
| 3 | 2 | 5 | 1 | 8 | 8 | 0 | `8 → 0 → 7` |
| 4 | 7 | — (stack2 vazia) | 0 | 7 | 7 | 0 | `7 → 8 → 0 → 7` |

Resultado final: `7 → 8 → 0 → 7` ✔ — bate com o esperado no enunciado (7243 + 564 = 7807).

## ⚡ Complexidade da solução ótima

- **Tempo:** O(max(m, n)) — empilhar as duas listas é O(m + n); desempilhar e somar é O(max(m, n))
- **Espaço:** O(m + n) para as duas pilhas (mais O(max(m,n)) da lista de resultado, que é a saída exigida, não espaço "extra")

## 💻 Implementações

### Java (referência completa e comentada)
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    Deque<Integer> stack1 = new ArrayDeque<>();
    Deque<Integer> stack2 = new ArrayDeque<>();

    // Empilhar lê cada lista da ESQUERDA para a DIREITA (sem tocar em next),
    // mas o LIFO da pilha entrega os dígitos na ordem "unidades primeiro" ao desempilhar.
    for (ListNode cur = l1; cur != null; cur = cur.next) stack1.push(cur.val);
    for (ListNode cur = l2; cur != null; cur = cur.next) stack2.push(cur.val);

    ListNode resultado = null;
    int carry = 0;

    while (!stack1.isEmpty() || !stack2.isEmpty() || carry != 0) {
        int d1 = stack1.isEmpty() ? 0 : stack1.pop();
        int d2 = stack2.isEmpty() ? 0 : stack2.pop();

        int soma = d1 + d2 + carry;
        carry = soma / 10;

        ListNode novo = new ListNode(soma % 10);
        novo.next = resultado; // PREPEND: o dígito mais recente (menos significativo até agora) vira a nova cabeça
        resultado = novo;
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

- **Prepender no lugar errado (append em vez de prepend)**: como os dígitos são processados do menos para o mais significativo, adicionar no **fim** da lista produziria o resultado na ordem invertida — é o `novo.next = resultado` (inserir na frente) que constrói a ordem certa automaticamente.
- **Esquecer o carry final**: igual ao LC 2, se a última soma gerar `carry = 1` e o loop parar assim que as duas pilhas esvaziarem, falta criar o dígito extra — a condição `|| carry != 0` no `while` cobre isso.
- **Inverter as listas originais "só para simplificar" sem reverter depois**: viola diretamente o follow-up e pode causar bugs sutis se outra parte do código ainda espera a lista na ordem original enquanto a soma está em andamento.
- **Usar recursão para inverter a leitura em vez de pilha explícita**: funciona (a pilha de chamadas faz o mesmo papel de uma pilha explícita), mas gasta espaço de pilha de recursão de forma menos controlada — a versão com `Deque` explícito é mais direta de raciocinar sobre o espaço gasto.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Ambos zero | `l1=[0], l2=[0]` | `[0]` | menor caso possível, sem carry |
| Listas de tamanhos diferentes | `l1=[7,2,4,3], l2=[5,6,4]` | `[7,8,0,7]` | trace acima — testa `d2=0` quando `stack2` esvazia primeiro |
| Carry propaga até criar um dígito novo | `l1=[9,9], l2=[1]` | `[1,0,0]` | valida o carry final criando um dígito a mais que ambas as entradas |
| Sem nenhum carry | `l1=[1,2], l2=[3,4]` | `[4,6]` | garante que a soma simples funciona sem propagação |
| Listas de tamanho igual | `l1=[2,4,3], l2=[5,6,4]` | `[8,0,7]` | exemplo do enunciado, sem diferença de tamanho entre as pilhas |

## 🔗 Conexões

- Problemas irmãos: **[0002] Add Two Numbers** (o mesmo problema, mas com dígitos já em ordem "unidades primeiro" — soma direta, sem precisar de pilhas), **[0206] Reverse Linked List** (a técnica que a força bruta usaria, e que o follow-up pede para evitar)
- No backend: processar uma sequência "de trás para frente" sem alterar a estrutura original é o mesmo padrão de **undo/redo com histórico imutável** (ler o histórico de eventos em ordem reversa para desfazer, sem reescrever a lista de eventos original) e de **parsers que avaliam expressões da direita para a esquerda** usando uma pilha, sem precisar reverter o texto de entrada.

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
