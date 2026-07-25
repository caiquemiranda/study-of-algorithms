---
name: leetcode-problems
description: Cria o documento de estudo detalhado de um problema do LeetCode no local correto do repositório. Use SEMPRE que o usuário enviar um print/screenshot de um problema do LeetCode, um link leetcode.com, um número de problema (ex. "LC 153", "problema 217"), ou pedir para documentar/estudar um problema de algoritmo. Também para atualizar um doc de problema existente.
---

# Skill: documentar problema do LeetCode

Você vai criar (ou atualizar) o material de estudo de um problema, seguindo o template do repositório, no caminho correto, com qualidade de material didático para iniciante.

## Passo 1 — Extrair os dados do problema

Da entrada do usuário (print, link, número ou enunciado colado), identifique:
- **Número** (4 dígitos com zeros à esquerda: `153` → `0153`) e **título oficial em inglês**
- **Dificuldade**: easy / medium / hard
- **Enunciado, exemplos e restrições (constraints)** — as constraints são obrigatórias no doc
- Se o print estiver ilegível ou faltar informação essencial (número, constraints), **pergunte antes de inventar**. Nunca invente enunciado.

## Passo 2 — Classificar na categoria correta

Regra de ouro: **classifique pela TÉCNICA da solução ótima, não pelo tipo de dado do input**.
(Ex.: LC 153 recebe um array, mas a solução é busca binária → `05_busca_binaria`.)

| Categoria | Sinais típicos |
|---|---|
| `01_arrays_e_hashing` | frequência, duplicatas, complemento (Two Sum), prefix sum, chave canônica |
| `02_two_pointers` | array ordenado + par/tripla, in-place O(1), palíndromo |
| `03_sliding_window` | melhor subarray/substring CONTÍGUA, janela de tamanho k |
| `04_stack` | parênteses, aninhamento, "próximo maior/menor elemento" (monotonic) |
| `05_busca_binaria` | ordenado/rotacionado, O(log n), "minimize o máximo" (busca na resposta) |
| `06_linked_list` | input é ListNode; fast & slow, reversão de ponteiros |
| `07_arvores` | TreeNode, travessias, BST, LCA, por nível |
| `08_tries` | prefixos, autocompletar, dicionário de palavras, curinga |
| `09_heap_priority_queue` | "K maiores/menores/mais frequentes", mediana de stream, mesclar N fontes |
| `10_backtracking` | "TODAS as combinações/permutações/subconjuntos", tabuleiros, n ≤ 20 |
| `11_grafos` | ilhas, componentes, BFS menor caminho sem peso, topological sort, Union-Find básico |
| `12_grafos_avancados` | menor caminho COM peso (Dijkstra/Bellman-Ford), MST |
| `13_programacao_dinamica_1d` | "nº de maneiras / min custo" com estado de 1 índice; LIS, Coin Change |
| `14_programacao_dinamica_2d` | duas strings (LCS/edit distance), grade, knapsack |
| `15_greedy` | escolha local ótima provável; Kadane, jump game, agendamento |
| `16_intervals` | intervalos [início, fim]: merge, salas de reunião, remoções |
| `17_matematica_e_geometria` | rotação/espiral de matriz, pow, GCD, aritmética modular |
| `18_bit_manipulation` | XOR, contar bits, "sem usar +", máscaras |

Se ficar genuinamente dividido entre duas categorias, escolha a técnica dominante da solução ótima e registre a secundária como tag. Só pergunte ao usuário se for realmente ambíguo.

## Passo 3 — Criar o arquivo no local certo

```
02_estruturas_e_algoritmos/problemas/<categoria>/<easy|medium|hard>/<NNNN>_<slug_em_ingles>.md
Ex.: 02_estruturas_e_algoritmos/problemas/05_busca_binaria/medium/0153_find_minimum_in_rotated_sorted_array.md
```

- Slug: título oficial em inglês, minúsculas, palavras separadas por `_`
- **Antes de criar, verifique se o arquivo já existe** (Glob por `**/<NNNN>_*.md`). Se existir, atualize-o em vez de duplicar — e preserve a seção "📝 O que eu aprendi" e as datas de revisão intactas

## Passo 4 — Escrever o conteúdo

Siga fielmente a estrutura de [`02_estruturas_e_algoritmos/problemas/_TEMPLATE.md`](../../../02_estruturas_e_algoritmos/problemas/_TEMPLATE.md). Regras de qualidade:

1. **Todas as seções são obrigatórias** — nenhuma fica vazia, exceto onde indicado abaixo
2. **Força bruta SEMPRE antes da ótima** — com complexidade e o motivo de não bastar (aponte qual constraint ela viola)
3. **Restrições comentadas** — cada constraint relevante acompanhada do que ela denuncia sobre a complexidade esperada
4. **Trace em tabela** — o passo a passo usa o exemplo do enunciado com valores concretos, estado por estado, terminando com o resultado verificado (✔)
5. **Java completo e comentado** — solução ótima idiomática; comente cada decisão não óbvia (overflow, off-by-one, invariante do loop). Prefira iterativo a recursivo quando reduzir espaço; se a versão recursiva for didática, mencione-a em Pegadinhas com o custo de pilha
6. **Python e C++ ficam como TODO** — são exercício do usuário (regra da trilha: reimplementar do zero). NÃO os preencha, nem quando souber a resposta
7. **Pegadinhas reais** — os erros que derrubam neste problema específico, não genéricos
8. **Casos de teste de borda** — em tabela, incluindo o caso que quebra o bug clássico
9. **Conexões** — 2+ problemas irmãos com número, e onde o padrão aparece em backend (estilo dos arquivos de `fundamentos/`)
10. **"📝 O que eu aprendi" fica VAZIA** — só o comentário HTML do template. É o exercício de retrieval do usuário; a IA nunca escreve nela
11. Didática de iniciante: frases curtas, analogia quando ajudar, zero jargão sem explicação na primeira ocorrência. Todo o texto em português; termos técnicos e código em inglês
12. Data "Resolvido em": a data de hoje

## Passo 5 — Pós-criação (obrigatório)

1. Rode `python 02_estruturas_e_algoritmos/gerador_de_indice.py` — ele atualiza sozinho o INDICE.md **e** o PROGRESSO.md (contagem por categoria + lista de resolvidos entre os marcadores AUTO). Não edite essas partes à mão
2. Reporte ao usuário: caminho do arquivo criado, categoria escolhida (e por quê, em 1 frase), e lembre-o de: (a) reimplementar em Python/C++ sem olhar o Java, (b) preencher "O que eu aprendi" à mão
