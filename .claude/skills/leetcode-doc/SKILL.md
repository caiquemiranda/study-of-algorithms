---
name: leetcode-doc
description: Gera o documento de estudo de UM problema do LeetCode a partir do cache local do pipeline (_pipeline/enunciados/). Use quando invocada com um número de problema — ex. "/leetcode-doc 58" — pelo orquestrador gerar_docs.py ou manualmente. Não busca nada na web; se o enunciado não está no cache, falha com instrução clara.
---

# Skill: gerar doc de um problema (a partir do cache)

Você está numa sessão dedicada a UM único problema. Gere o documento completo e termine. Não faça mais nada além do descrito aqui.

## Passo 1 — Carregar o enunciado do cache

- O argumento é o número do problema (ex.: `58`).
- Glob: `02_estruturas_e_algoritmos/_pipeline/enunciados/<numero com 4 dígitos>_*.json` e leia o JSON: `id`, `titulo`, `slug`, `url`, `dif`, `tags`, `categoria` (sugestão) e `enunciado` (texto original).
- **Cache ausente** → responda apenas: `ERRO: enunciado <id> não está no cache. Rode: python 02_estruturas_e_algoritmos/_pipeline/lc_fetch.py baixar-tudo` e PARE. Nunca busque na web, nunca invente o enunciado.

## Passo 2 — Checar duplicata

- Glob `02_estruturas_e_algoritmos/problemas/*/*/<numero com 4 dígitos>_*.md`.
- Se existir → responda `JÁ EXISTE: <caminho>` e PARE (não sobrescreva).

## Passo 3 — Escrever o documento

- Leia `02_estruturas_e_algoritmos/problemas/_TEMPLATE.md` e siga TODAS as seções.
- Caminho: `02_estruturas_e_algoritmos/problemas/<categoria>/<dif>/<numero 4 dígitos>_<slug_com_underscores>.md`
  - A `categoria` do cache é sugestão por tags. **Reclassifique pela técnica da solução ótima** (tabela de decisão na skill `leetcode-problems`) se discordar — sem perguntar; apenas registre a divergência na última linha da sua resposta.
- Regras de qualidade (o validador mecânico confere TODAS — doc reprovado volta para você):
  1. Todas as seções do template presentes (📜 🧭 🐢 💡 🎬 ⚡ 💻 ⚠️ 🧪 🔗 📝)
  2. Enunciado resumido em português + exemplos + **restrições comentadas** (o que cada uma denuncia da complexidade esperada)
  3. **Força bruta antes da ótima**, com complexidade e por que não basta
  4. **Walkthrough em tabela** com o exemplo do enunciado, estado por estado, resultado com ✔
  5. **Java completo e comentado** (comentários de "porquê"; ≥ 60 caracteres de código)
  6. **Python e C++ apenas com TODO** — são exercício do usuário; NUNCA os preencha
  7. **"📝 O que eu aprendi" fica vazia** (só o comentário HTML do template)
  8. Cabeçalho com link `leetcode.com/problems/...`, dificuldade, categoria e `Resolvido em: <data de hoje>`
  9. Pegadinhas específicas DESTE problema; casos de teste de borda em tabela; 2+ problemas irmãos nas conexões
  10. Didática de iniciante: frases curtas, analogia quando ajudar, termos técnicos explicados na primeira ocorrência
- O número no título `# [NNNN] ...` deve bater com o nome do arquivo.

## Passo 4 — Encerrar

- NÃO rode scripts (índice/fila são responsabilidade do orquestrador).
- Última linha da resposta: `OK <caminho relativo do doc>` (+ nota de divergência de categoria, se houver).
