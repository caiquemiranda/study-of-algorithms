# 🧠 Trilha de Estruturas de Dados e Algoritmos

> Trilha **transversal**: começa no Júnior e acompanha todos os níveis. Corresponde à Fase 2 do roadmap (Vol. 1).

## Como esta trilha se organiza

| Pasta / arquivo | O que é |
|---|---|
| [01_complexidade.md](01_complexidade.md) | Big-O, análise amortizada, Teorema Mestre |
| [02_estruturas_de_dados.md](02_estruturas_de_dados.md) | Checklist de estruturas para implementar **do zero** |
| [03_algoritmos_e_padroes.md](03_algoritmos_e_padroes.md) | Ordenação, busca, padrões de entrevista, DP, grafos |
| `fundamentos/` | Uma anotação por padrão (18 categorias, alinhadas ao NeetCode 150) |
| `problemas/` | Soluções LeetCode organizadas por categoria × dificuldade |
| `implementacoes/` | Estruturas implementadas do zero em Java, Python, C++ e Go |
| [INDICE.md](INDICE.md) | Índice gerado automaticamente por `gerador_de_indice.py` |

## Escopo por nível

- **Júnior:** complexidade + estruturas lineares + hash + árvores + BFS/DFS + ordenação + two pointers / sliding window
- **Pleno:** completar DP, grafos avançados, backtracking
- **Sênior:** reimplementar as estruturas em C++ (gerência manual de memória) e Go

## Regras de prática deliberada (Fase 2.4)

- **NeetCode 150** — a lista mais eficiente hoje (organizada exatamente pelas categorias de `problemas/`)
- LeetCode: *Blind 75* ou *Grind 75* como meta mínima
- Codewars ou Exercism para prática diária leve
- Regra: **sem consultar solução por 30 minutos**. Depois de 30min, leia a solução, entenda, feche tudo e reimplemente do zero no dia seguinte.
- Refazer todas as estruturas do zero, sem consultar, em pelo menos uma linguagem

## Convenção de nome dos arquivos de solução

```
problemas/<categoria>/<dificuldade>/<numero-leetcode>_<nome-do-problema>.md
Ex.: problemas/01_arrays_e_hashing/easy/0001_two_sum.md
```

Cada solução deve registrar: enunciado resumido, abordagem, complexidade tempo/espaço, código e o que aprendeu.
Depois de resolver, rode `python gerador_de_indice.py` para atualizar o [INDICE.md](INDICE.md).

**✅ Checkpoint da trilha (nível Júnior):** implementar Hash Table, BST e Grafo com BFS/DFS do zero, sem consulta, e justificar a complexidade de cada operação.
