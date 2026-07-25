---
name: leetcode-lote
description: Processa um lote de problemas do LeetCode baixado pelo pipeline (02_estruturas_e_algoritmos/_pipeline/) e gera os documentos de estudo de todos eles. Use quando o usuário pedir para processar/documentar um lote — ex. "/leetcode-lote lote_001", "processa o próximo lote", "documenta o lote 3" — ou mencionar o arquivo lotes/lote_NNN.json.
---

# Skill: processar lote de problemas do LeetCode

Você vai gerar os documentos de estudo de TODOS os problemas de um lote baixado pelo pipeline.

## Passo 1 — Carregar o lote

- O argumento é o nome (`lote_001`) ou caminho do arquivo em `02_estruturas_e_algoritmos/_pipeline/lotes/`.
- Sem argumento: use o lote de maior número que ainda tenha problemas não documentados.
- Cada item traz: `id`, `titulo`, `slug`, `url`, `dif`, `tags`, `categoria` (SUGESTÃO do script) e `enunciado` (texto limpo do original).

## Passo 2 — Gerar um doc por problema

Para CADA problema do lote, siga **integralmente** as regras da skill `leetcode-problems` (leia-a em `.claude/skills/leetcode-problems/SKILL.md` se ainda não estiver em contexto):

- Caminho: `02_estruturas_e_algoritmos/problemas/<categoria>/<dif>/<id 4 dígitos>_<slug_com_underscores>.md`
- A `categoria` do lote é sugestão por tags — **reclassifique pela técnica da solução ótima** se discordar (regra de ouro da skill principal). Não pergunte ao usuário em lote; registre a divergência no relatório final.
- Template completo de `problemas/_TEMPLATE.md`: enunciado resumido em português + exemplos + restrições comentadas, como reconhecer, força bruta, ideia otimizada, walkthrough em tabela, complexidade, Java completo comentado, **Python/C++ como TODO**, pegadinhas, casos de teste, conexões, e **"O que eu aprendi" vazia**.
- Antes de criar, cheque duplicata (`Glob problemas/**/<id>_*.md`); se existir, pule e registre.
- Trabalhe em sequência, um arquivo por vez. Qualidade não cai no item 15: cada doc recebe o mesmo rigor do primeiro — se o contexto da sessão estiver ficando longo, PARE, informe quantos faltam e sugira continuar em nova sessão com o mesmo lote (a skill pula os já criados).

## Passo 3 — Fechamento (obrigatório)

1. `python 02_estruturas_e_algoritmos/gerador_de_indice.py` (INDICE + PROGRESSO)
2. `python 02_estruturas_e_algoritmos/_pipeline/lc_fetch.py sincronizar` (marca a fila)
3. Relatório final: quantos docs criados, quantos pulados (duplicata/indisponível), divergências de categoria (id: sugerida → final), e o comando para o usuário baixar o próximo lote:
   `python 02_estruturas_e_algoritmos/_pipeline/lc_fetch.py lote 20`

## Regras de honestidade

- Nunca invente enunciado, exemplos ou constraints além do que está no lote — se um item vier truncado/vazio, pule e reporte.
- Docs em lote são material de CONSULTA: lembre o usuário (uma vez, no relatório) de que a regra dos 30 minutos e o "O que eu aprendi" continuam sendo o estudo de verdade.
