# 02 — Two Pointers

> Dois índices percorrendo a estrutura de forma coordenada, eliminando o loop aninhado. Problemas em [`../problemas/02_two_pointers/`](../problemas/02_two_pointers/).

## Conceito

Em vez de testar todos os pares (O(n²)), dois ponteiros se movem segundo uma **regra de decisão** que descarta candidatos com segurança. Funciona quando existe **monotonicidade**: mover um ponteiro numa direção só melhora (ou só piora) o critério — geralmente porque o array está **ordenado** ou porque a resposta tem estrutura simétrica.

**As três variantes:**
1. **Pontas opostas (convergentes)**: `esq` no início, `dir` no fim, movem-se um em direção ao outro. Ex.: par com soma alvo em array ordenado, palíndromo, container com mais água.
2. **Mesma direção (leitor/escritor)**: um ponteiro lê, outro marca a posição de escrita. Ex.: remover duplicatas in-place, mover zeros.
3. **Velocidades diferentes (fast & slow / Floyd)**: um anda 1, outro anda 2. Detecta ciclo, encontra o meio de lista ligada. (Detalhes em [06_linked_list](06_linked_list.md).)

## Como reconhecer no enunciado

- Array **ordenado** + "encontre par/tripla com soma X"
- "in-place, O(1) de espaço extra"
- Palíndromos e comparações simétricas
- "remova/compacte elementos mantendo ordem"
- Se o array não está ordenado e a posição não importa: **ordene primeiro** e avalie se two pointers se aplica

## Templates

```python
# Pontas opostas — par com soma alvo em array ordenado, O(n)
def par_soma(nums, alvo):
    esq, dir = 0, len(nums) - 1
    while esq < dir:
        s = nums[esq] + nums[dir]
        if s == alvo:
            return [esq, dir]
        if s < alvo:
            esq += 1        # soma pequena demais: só melhora avançando esq
        else:
            dir -= 1        # soma grande demais: só melhora recuando dir

# 3Sum — fixa um, two pointers no resto, O(n²)
def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                          # pula duplicata do fixo
        esq, dir = i + 1, len(nums) - 1
        while esq < dir:
            s = nums[i] + nums[esq] + nums[dir]
            if s < 0:   esq += 1
            elif s > 0: dir -= 1
            else:
                res.append([nums[i], nums[esq], nums[dir]])
                esq += 1
                while esq < dir and nums[esq] == nums[esq - 1]:
                    esq += 1                  # pula duplicatas internas
    return res

# Leitor/escritor — remover duplicatas de array ordenado, in-place
def remove_duplicates(nums):
    escreve = 1
    for le in range(1, len(nums)):
        if nums[le] != nums[escreve - 1]:
            nums[escreve] = nums[le]
            escreve += 1
    return escreve
```

## Complexidade típica

O(n) tempo (cada ponteiro percorre o array no máximo uma vez), O(1) espaço. Com ordenação prévia: O(n log n).

## Erros comuns

- Aplicar em array **não ordenado** sem ordenar (a regra de descarte deixa de valer)
- Esquecer de pular duplicatas no 3Sum (resposta com triplas repetidas)
- Off-by-one na condição (`esq < dir` vs `esq <= dir` — pense se os ponteiros podem apontar para o mesmo elemento)
- Não conseguir **justificar por que é seguro descartar** — se você não sabe explicar por que mover o ponteiro não perde a resposta, o padrão pode não se aplicar

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 125. Valid Palindrome | 🟢 easy |
| 167. Two Sum II | 🟢 easy |
| 283. Move Zeroes | 🟢 easy |
| 15. 3Sum | 🟡 medium |
| 11. Container With Most Water | 🟡 medium |
| 42. Trapping Rain Water | 🔴 hard |

## Conexão com backend

O padrão leitor/escritor é o mesmo de compactação de buffers e de merge de arquivos ordenados (merge externo — a base do merge sort em disco e da compactação de SSTables em bancos LSM, Vol. 2 Módulo D).
