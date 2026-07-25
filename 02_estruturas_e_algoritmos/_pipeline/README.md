# Pipeline LeetCode — como usar

Gera documentos de estudo para os ~3.581 problemas de algoritmos do LeetCode, **um por sessão fresca de IA** (sem fadiga de lote), com validação mecânica do padrão.

> Sem o CLI autenticado no subprocess (`gerar_docs.py`), gere manualmente numa sessão de chat: abra [CONTEXTO_IA.md](CONTEXTO_IA.md) e peça para a IA executá-lo (ex.: "execute o CONTEXTO_IA.md, processe os próximos 15"). É o mesmo padrão, só sem a etapa headless.

## Pré-requisitos

- Python 3.8+ (só biblioteca padrão, nada de `pip install`)
- CLI do Claude Code no PATH — teste com `claude --version`.
  Se não tiver: `npm install -g @anthropic-ai/claude-code` (usa o mesmo login do app)

## Fluxo completo

```
┌─ 1x ──────────────────────────────────────────────────────────┐
│ python lc_fetch.py catalogo       fila ordenada (3.581)       │
│ python lc_fetch.py baixar-tudo    cache de enunciados (~70min)│
└───────────────────────────────────────────────────────────────┘
┌─ sempre que quiser gerar docs ────────────────────────────────┐
│ python gerar_docs.py --n 10       10 docs, 1 por sessão fresca│
│   → valida cada doc; aprovado = 'documentado' na fila         │
│   → reprovado vai p/ rejeitados/ e é retentado 1x             │
│   → ao final: INDICE.md e PROGRESSO.md atualizados            │
└───────────────────────────────────────────────────────────────┘
```

Rode tudo a partir desta pasta (`02_estruturas_e_algoritmos/_pipeline/`).

## Comandos

| Comando | O que faz |
|---|---|
| `python lc_fetch.py catalogo` | Baixa/atualiza o catálogo e (re)gera a `fila.json` ordenada. Preserva progresso |
| `python lc_fetch.py baixar-tudo` | Baixa TODOS os enunciados acessíveis para `enunciados/` (retomável: Ctrl+C à vontade) |
| `python lc_fetch.py baixar-tudo 50` | Idem, limitado a 50 (para testar) |
| `python gerar_docs.py --n 10` | Gera os próximos 10 da fila (1 sessão de IA por problema + validação) |
| `python gerar_docs.py --dry --n 10` | Só lista o que seria gerado, sem gastar IA |
| `python gerar_docs.py --ids 58,169` | Gera problemas específicos |
| `python gerar_docs.py --revisar` | Retenta os que falharam na validação |
| `python lc_fetch.py validar` | Confere todos os docs contra o padrão do `_TEMPLATE.md` |
| `python lc_fetch.py status` | Resumo da fila |
| `python lc_fetch.py sincronizar` | Realinha a fila com os docs existentes em `problemas/` |
| `python lc_fetch.py resetar orfaos` | Devolve à fila problemas de lotes apagados (fluxo antigo) |

## Ordem da fila

`dificuldade (easy→medium→hard)` → `categoria (01→18, conceitos simples→complexos)` → `número`.

## Status possíveis na fila

| Status | Significado |
|---|---|
| `pendente` | Aguardando geração |
| `documentado` | Doc gerado E aprovado na validação |
| `revisar` | Falhou na validação 2x — versões reprovadas em `rejeitados/`, detalhes em `logs/<id>.log` |
| `premium` / `indisponivel` | Sem enunciado acessível; ignorado para sempre |

## O que a validação confere (portão do padrão)

Seções obrigatórias do template · Java preenchido · Python/C++ apenas com TODO (seu exercício!) · "O que eu aprendi" vazia (seu retrieval!) · link + data · tabela de trace no walkthrough · pasta de dificuldade coerente com a fila.

## Se algo der errado

- **Download interrompido** → rode `baixar-tudo` de novo; ele retoma do ponto exato.
- **Doc reprovado (`revisar`)** → veja `logs/<id>.log` e `rejeitados/`; retente com `--revisar` ou gere numa sessão interativa: `/leetcode-doc <id>`.
- **`claude: command not found`** → instale a CLI (pré-requisitos acima).
- **Duas execuções ao mesmo tempo** → nunca. Uma instância por vez (fila e servidor agradecem).

## Regras de ouro

1. `enunciados/`, `lotes/`, `logs/` e `rejeitados/` estão no `.gitignore` — **enunciado do LeetCode não vai para o GitHub** (copyright). `fila.json` e os scripts são versionados.
2. Os docs gerados são material de **consulta**. O estudo de verdade continua sendo: 30 min tentando sozinho → ler o doc → reimplementar Python/C++ do zero → preencher "O que eu aprendi" de memória.
3. Gere no ritmo da sua franquia de uso (10–40/dia). São ~3.050 problemas: é maratona, não sprint.
