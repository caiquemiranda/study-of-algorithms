# Contexto para IA — Gerar documentos pendentes do LeetCode

> Este arquivo é instrução de execução, não documentação de leitura passiva. Se você é uma sessão de IA (Claude) recebendo este arquivo como contexto/prompt, **siga os passos na ordem, sem pular nenhum**. Se você é o usuário: cole/aponte este arquivo numa sessão nova e peça "execute o CONTEXTO_IA.md" (opcionalmente com um número, ex.: "processe os próximos 15").

## Objetivo

Gerar os documentos de estudo que faltam, comparando o que já existe (`INDICE.md`) com o que já foi baixado (`_pipeline/enunciados/`), seguindo **rigorosamente** o padrão já estabelecido nos documentos existentes — sem inventar conteúdo, sem pular etapas de validação, sem deixar os arquivos de controle (`INDICE.md`, `PROGRESSO.md`, `fila.json`) desatualizados.

## Pré-requisitos (confira antes de começar)

- `02_estruturas_e_algoritmos/_pipeline/fila.json` existe (rodar `lc_fetch.py catalogo` se não)
- `02_estruturas_e_algoritmos/_pipeline/enunciados/` tem arquivos (rodar `lc_fetch.py baixar-tudo` se vazio)
- Você tem acesso de leitura a `02_estruturas_e_algoritmos/problemas/_TEMPLATE.md` e às skills `leetcode-doc` / `leetcode-problems` do projeto (`.claude/skills/`)

## Passo 1 — Descobrir o estado atual (leitura, não escrita)

1. Leia `02_estruturas_e_algoritmos/INDICE.md` — é o retrato de quais problemas **já têm documento**, por categoria.
2. Leia `02_estruturas_e_algoritmos/_pipeline/fila.json` — cada item tem `id`, `titulo`, `dif`, `categoria` (sugestão), `status` (`pendente` / `documentado` / `baixado` / `revisar` / `premium` / `indisponivel`).
3. Se houver divergência entre o que está em `problemas/**/*.md` e o `status` da fila (ex.: doc existe mas status não é `documentado`), rode primeiro:
   ```
   python 02_estruturas_e_algoritmos/_pipeline/lc_fetch.py sincronizar
   ```
   Isso realinha a fila com a realidade do disco antes de você continuar.

## Passo 2 — Cruzar com os enunciados baixados

1. Liste `02_estruturas_e_algoritmos/_pipeline/enunciados/*.json` — cada arquivo é `NNNN_slug.json` com o enunciado já limpo (campos: `id`, `slug`, `titulo`, `dif`, `tags`, `categoria`, `url`, `enunciado`).
2. Cruze com a fila: você só pode gerar documento para um problema se **(a)** o status na fila for `pendente` ou `baixado` **e** **(b)** existir o arquivo correspondente em `enunciados/`.
3. Se o usuário pediu um número N (ex.: "os próximos 15"), pegue os N primeiros dessa interseção, respeitando a ordem da fila (`dificuldade → categoria → número` — já vem ordenada assim no `fila.json`). Sem número especificado, processe **todos** os prontos, mas veja a trava de fadiga no Passo 5.
4. Se algum problema pedido pelo usuário **não** tem enunciado em `enunciados/`, não invente — reporte que falta baixar (`lc_fetch.py baixar-tudo`) e siga com o resto.

## Passo 3 — Gerar cada documento (um por vez, mesmo rigor em todos)

Para cada problema selecionado, siga **integralmente** as regras da skill `leetcode-doc` (ou `leetcode-problems` se estiver operando fora do fluxo de cache). Resumo do que não pode faltar — o validador do Passo 4 confere tudo isto mecanicamente:

1. **Checar duplicata primeiro**: `Glob 02_estruturas_e_algoritmos/problemas/*/*/<numero 4 dígitos>_*.md`. Se existir, pule e registre — nunca sobrescreva sem que o usuário peça.
2. **Classificar pela técnica da solução ótima**, não aceitar cegamente a `categoria` do cache (ela é só sugestão por tags). Use a tabela de decisão da skill `leetcode-problems` (18 categorias). Se reclassificar, anote a divergência no relatório final.
3. **Caminho do arquivo**: `02_estruturas_e_algoritmos/problemas/<categoria>/<dif>/<numero 4 dígitos>_<slug_com_underscores>.md`
4. **Seguir `_TEMPLATE.md` seção por seção**, sem pular nenhuma:
   - Cabeçalho: link `leetcode.com/problems/...`, dificuldade, categoria, `Resolvido em: <data de hoje>`
   - Enunciado resumido em português (a partir do `enunciado` do cache — nunca invente exemplos/constraints que não estejam lá)
   - Restrições **comentadas** (o que cada uma denuncia sobre a complexidade esperada)
   - Como reconhecer o padrão
   - Força bruta **antes** da ótima, com complexidade e o motivo de não bastar
   - Ideia otimizada (intuição)
   - Walkthrough em **tabela**, com o exemplo do enunciado, terminando em resultado verificado (✔)
   - Complexidade da solução ótima
   - Java **completo e comentado** (comentários de "porquê", não de "o quê")
   - Python e C++ **apenas com `TODO`** — são exercício do usuário, nunca preencha
   - Pegadinhas específicas deste problema (não genéricas)
   - Casos de teste de borda em tabela
   - Conexões (2+ problemas irmãos + aplicação em backend)
   - **"O que eu aprendi" fica vazia** — só o comentário HTML do template, nunca escreva texto ali
5. Título do doc (`# [NNNN] ...`) deve conter o número entre colchetes batendo com o nome do arquivo.

## Passo 4 — Validar mecanicamente (obrigatório, não pule)

Depois de gerar o lote (ou mesmo problema a problema), rode:
```
python 02_estruturas_e_algoritmos/_pipeline/lc_fetch.py validar <id1> <id2> ...
```
- Se algum reprovar, leia os erros listados e **corrija o documento antes de seguir em frente** — não acumule pendências de qualidade.
- Só depois de tudo aprovado (`N/N no padrão`) avance para o Passo 5.

## Passo 5 — Trava de fadiga (não negocie isto)

- Se você notar queda de qualidade ao longo do lote (documentos mais curtos, walkthrough raso, pegadinhas genéricas) ou se o lote for grande (>15-20 problemas), **pare, informe quantos foram gerados e quantos faltam**, e sugira continuar em uma nova sessão/mensagem.
- Retomar depois é seguro: o Passo 1 (checar duplicata) garante que problemas já documentados não são refeitos.

## Passo 6 — Fechamento obrigatório (atualizar os documentos de controle)

**Sempre**, mesmo que só 1 documento tenha sido criado:

```
python 02_estruturas_e_algoritmos/gerador_de_indice.py
```
Isso regenera `INDICE.md` (lista completa por categoria) e atualiza as partes automáticas do `PROGRESSO.md` (contagem por categoria + lista de resolvidos, entre os marcadores `<!-- INICIO:PROBLEMAS-AUTO -->`/`<!-- FIM -->`) — nunca edite essas seções à mão.

```
python 02_estruturas_e_algoritmos/_pipeline/lc_fetch.py sincronizar
```
Isso marca na `fila.json` os problemas recém-documentados como `documentado`, para que a próxima execução deste mesmo processo não os selecione de novo.

## Passo 7 — Relatório final ao usuário

Reporte, em texto direto (sem rodeos):
- Quantos documentos foram criados (com caminho de cada um)
- Quantos foram pulados por já existirem
- Quantos foram pulados por falta de enunciado em cache
- Divergências de categoria (id: sugerida pelo cache → categoria final usada, com o motivo em 1 frase)
- Resultado da validação (`N/N no padrão`)
- Quantos problemas prontos (com cache) ainda restam na fila, para a próxima rodada

## Regras de honestidade (não negociáveis)

- Nunca busque na web — a fonte é exclusivamente `_pipeline/enunciados/`. Sem cache, sem documento.
- Nunca invente enunciado, exemplo ou constraint além do que está no JSON do cache.
- Nunca preencha os blocos Python/C++ nem a seção "O que eu aprendi" — são o exercício de retrieval do usuário (ver `METODO.md` na raiz do repositório).
- Nunca rode `baixar-tudo` ou `catalogo` a partir deste processo sem o usuário pedir explicitamente — eles alteram o cache/fila em escala e têm custo de tempo/rede.
