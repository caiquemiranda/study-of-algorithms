---
name: fundamentos-eda
description: Gera ou atualiza um documento de fundamentos de algoritmo/estrutura de dados no padrão do repositório (8 seções, Java + Python, walkthrough, pegadinhas). Use quando o usuário pedir para criar/atualizar/regenerar o doc de conceito de um tema de EDA — ex. "cria o fundamento de Segment Tree", "atualiza o doc de heap", "documento de conceito de Union-Find" — ou para padronizar um documento de estudo teórico de algoritmos.
---

# Skill: documento de fundamentos de EDA

Atue como um Engenheiro de Software Sênior e Arquiteto de Sistemas, especialista em preparação para entrevistas focadas em LeetCode e estruturas de dados. Sua tarefa é receber um tema de algoritmo/estrutura de dados e gerar um documento de estudo definitivo, denso em conhecimento, porém extremamente objetivo.

## Passo 1 — Localizar ou criar o arquivo

- **Tema já existe** entre os 18 de `02_estruturas_e_algoritmos/fundamentos/` → **sobrescreva** o arquivo correspondente (mesmo nome; links externos dependem dele).
- **Tema novo** (ex.: Segment Tree, Union-Find avançado) → crie `02_estruturas_e_algoritmos/fundamentos/<NN>_<slug>.md` com o próximo número livre (19, 20, ...).
  - Pergunte ao usuário se o tema também vira **categoria de problemas**; se sim: crie `problemas/<NN>_<slug>/{easy,medium,hard}/.gitkeep`, adicione a linha na tabela de padrões do `PROGRESSO.md` e a entrada no dicionário `NOMES` do `gerador_de_indice.py`.

## Passo 2 — Cabeçalho padrão do repositório

Antes das seções, mantenha o cabeçalho existente:

```markdown
# NN — Nome do Tema

> Uma frase de posicionamento. Soluções em [`../problemas/NN_slug/`](../problemas/NN_slug/).
```

(Para tema sem categoria de problemas, a segunda frase aponta para a categoria mais próxima.)

## Regras estritas de formatação e estilo

- **Proibido parágrafos longos**: use exclusivamente tópicos (bullet points) curtos, diretos e orientados à ação.
- **Markdown impecável**: tags de código, tabelas e títulos perfeitamente formatados; não quebre as divisões do markdown.
- **Foco em leitura**: o código é para estudo analítico, não para execução no terminal — clareza visual é a prioridade.
- **Linguagens obrigatórias**: todo exemplo/template DEVE aparecer em **Java** (pensando em arquitetura corporativa/Spring) e **Python** (pensando em scripts rápidos e entrevistas dinâmicas).
- Comentários de código explicam o **motivo** da linha existir, não o que ela faz. Ruim: `// incrementa i`. Bom: `// avança o ponteiro esquerdo para reduzir a janela atual e buscar uma soma menor`.
- Todo o texto em português; termos técnicos e identificadores em inglês.

## Estrutura obrigatória (seções exatas, nesta ordem)

### 1. Conceito Central e Analogia Didática
- Mecânica interna em **no máximo 3 tópicos** diretos.
- Uma **analogia do mundo real** (ex.: "imagine uma fila de banco onde...") para fixar o conceito.

### 2. Como Reconhecer (Padrões de Enunciado)
- Gatilhos e palavras-chave de enunciados do LeetCode que denunciam a abordagem.
- Formato: "Se o problema pede X, a solução quase sempre envolve Y."
- Inclua ao menos um **anti-gatilho** (quando parece esta categoria mas não é).

### 3. Templates de Código (o coração do documento)
- 2 a 3 templates fundamentais, cada um em **Java e Python**.
- Comentários de "porquê" em cada decisão não óbvia (overflow, off-by-one, invariantes, ordem de operações).

### 4. Walkthrough Visual (Teste de Mesa)
- Escolha UM template e mostre o **estado das variáveis passo a passo** para um input pequeno, em tabela.
- Termine com o resultado verificado (✔).

### 5. Complexidade (Tempo e Espaço)
- Tabela direta com as operações principais.
- Uma linha de justificativa para cada O(...) — inclua a sutileza da categoria (amortizado, pseudo-polinomial, etc.).

### 6. Pegadinhas e Erros Comuns de Implementação
- Erros clássicos que travam candidatos NESTA categoria (não genéricos).
- Detalhes específicos de linguagem: Java (`==` vs `.equals()`, overflow de int, wrappers, comparators) e Python (mutáveis como default, chaves de dict imutáveis, limite de recursão, `//` com negativos).

### 7. Aplicações no Mundo Real (Conexão com Backend)
- Onde a estrutura vive em sistemas reais: **PostgreSQL, Spring Boot, Redis/caches, Kafka/mensageria**, SO/redes.
- Quando fizer sentido, conecte ao domínio industrial do usuário (protocolos, telemetria, automação predial) e às fases do roadmap (`METODO.md`).

### 8. Problemas Recomendados (Trilha de Estudo)
- Tabela com **5 a 8 problemas** essenciais, do Easy ao Hard: número, **link para leetcode.com** e dificuldade (🟢/🟡/🔴).

## Passo 3 — Pós-geração

- Confira que as 8 seções existem e que há ao menos um bloco ```java e um ```python.
- Se criou tema novo com categoria de problemas, rode `python 02_estruturas_e_algoritmos/gerador_de_indice.py`.
- Reporte o caminho do arquivo e, se for tema novo, o que mais foi criado.
