# 🏗️ Roadmap Vol. 6 — PROJETOS-ÂNCORA

> Os 7 projetos que integram tudo: do mini-framework web ao capstone de monitoramento predial.
>
> Documento consolidado, gerado das pastas `07_projetos/` em 2026-08-05. **Edite as pastas, não este arquivo** — regenere com `python roadmap/gerar_volumes.py`. Método de estudo e marcação 🔴🟡🟢: ver `METODO.md`.

## Índice deste volume

1. 🏗️ Projetos-Âncora — Guia
2. 🏗️ Projeto 1 — Mini-Framework Web (do zero, sem dependências)
3. 🏗️ Projeto 2 — API CRUD com Spring Boot
4. 🏗️ Projeto 3 — API equivalente em FastAPI
5. 🏗️ Projeto 4 — Sistema com Mensageria
6. 🏗️ Projeto 5 — Full-Stack Completo
7. 🏗️ Projeto 6 — Servidor MCP
8. 🏗️ Projeto 7 — Capstone: Plataforma de Monitoramento Predial/Industrial

---

# 🏗️ Projetos-Âncora — Guia

> Fase 17 (Vol. 1) + mapeamento de normas por projeto (Vol. 4). Um projeto real vale mais que dez cursos assistidos.

---

# FASE 17 — Projetos-Âncora [NÚCLEO]

> Cada projeto força a integração das fases anteriores. **Um projeto real vale mais que dez cursos assistidos.**

1. **Mini-framework web** (Fase 4) — servidor HTTP do zero, sem dependências
2. **API CRUD com Spring Boot** — auth JWT, JPA, validação, tratamento global de erro, testes, migrations, Docker Compose
3. **API equivalente em FastAPI** — para comparar os dois ecossistemas com o mesmo domínio
4. **Sistema com mensageria** — dois serviços conversando via Kafka ou RabbitMQ, com outbox pattern e consumidor idempotente
5. **Full-stack completo** — backend Java + frontend TypeScript com tipos gerados do OpenAPI + Postgres + Redis, tudo em Docker Compose, com CI no GitHub Actions
6. **Servidor MCP** — conectando IA a uma ferramenta real
7. **Capstone — o projeto do seu diferencial:** plataforma de monitoramento predial/industrial. Ingestão de telemetria de dispositivos, banco time-series, alertas em tempo real via WebSocket/SSE, histórico, dashboard, e um módulo de diagnóstico com RAG sobre manuais técnicos.
   > Este último é o que te diferencia de todo mundo que fez o mesmo tutorial de "API de tarefas". Ele cruza os seus 10+ anos de automação com o seu novo perfil de engenheiro de software — e essa combinação é rara no mercado.

---

# 🔨 Como aplicar isso nos projetos do roadmap

Não estude norma no vácuo. Aplique nos projetos da Fase 17:

| Projeto | Norma a aplicar |
|---|---|
| API CRUD Spring Boot | Escreva requisitos não funcionais pelas **9 características da ISO 25010**; aplique **ASVS L1** |
| Sistema com mensageria | Documente com **C4** + escreva 3 **ADRs** justificando as decisões |
| Full-stack completo | **WCAG 2.2 AA** no frontend; **quality gate** no CI com SonarQube; **SBOM** no build |
| Capstone (monitoramento predial) | ⭐ **IEC 62443** (segmentação, SL); **LGPD** (dados de ocupantes); requisitos de **disponibilidade** e **safety** da ISO 25010; rastreabilidade de requisito → teste |

Um portfólio com **ADRs escritos, requisitos não funcionais mensuráveis e quality gate configurado** vale mais numa entrevista de pleno/sênior do que cinco projetos a mais sem isso. É a evidência visível de que você pensa como engenheiro, não como programador.

---

# 🏗️ Projeto 1 — Mini-Framework Web (do zero, sem dependências)

**Nível:** Pleno · **Fase de origem:** 4 (os 16 pilares)

## Objetivo
Servidor HTTP em Python puro (biblioteca padrão, zero dependências), depois replicado em Go. É o projeto que transforma Spring/FastAPI de "magia" em "eu sei o que isso faz".

## Escopo (do projeto central da Fase 4 — detalhes em [`03_pleno/01`](../03_pleno/01_web_sem_frameworks_16_pilares.md))
- [ ] Servidor HTTP do zero: sockets → parsing → resposta, com roteador em **Radix Tree**
- [ ] Suporte a **thread pool** e depois **event loop** — medir a diferença sob carga
- [ ] Autenticação com sessão via cookie **e** via JWT (as duas, para comparar)
- [ ] Upload multipart salvando em chunks no disco
- [ ] Servir estáticos com `ETag` e `304`
- [ ] Proxy reverso simples na frente de tudo
- [ ] (Fase 8) Replicar em Go puro e comparar goroutines vs event loop

## Referência
Repositório `codecrafters-io/build-your-own-x` — seções *Build your own Web Server* e *Build your own Database*.

## Status
🔴 Não iniciado

---

# 🏗️ Projeto 2 — API CRUD com Spring Boot

**Nível:** Júnior (é o projeto de conclusão do nível) · **Fases de origem:** 5, 6, 7, 11

## Objetivo
API REST completa, construída sem tutorial, provando o "sinal de aprovação" do nível Júnior.

## Escopo
- [ ] Auth JWT
- [ ] JPA com relacionamentos (e caçar o N+1 com log de SQL)
- [ ] Validação (`@Valid`) e tratamento global de erro com **RFC 7807**
- [ ] Testes: unitários + `@WebMvcTest` + `@DataJpaTest`
- [ ] Migrations com Flyway
- [ ] Docker Compose (API + Postgres)

## Normas a aplicar (Vol. 4)
- Requisitos não funcionais escritos pelas **9 características da ISO 25010**
- **OWASP ASVS L1** como checklist de segurança

## Status
🔴 Não iniciado

---

# 🏗️ Projeto 3 — API equivalente em FastAPI

**Nível:** Pleno · **Fase de origem:** 9

## Objetivo
Reimplementar o mesmo domínio do Projeto 2 em Python/FastAPI para comparar os dois ecossistemas de igual para igual.

## Escopo
- [ ] Mesmo domínio e contrato do Projeto 2
- [ ] Pydantic v2 + `Depends` (comparar com a DI do Spring)
- [ ] SQLAlchemy 2.0 + Alembic (comparar com JPA + Flyway)
- [ ] Auth OAuth2/JWT
- [ ] Uvicorn/ASGI — e saber apontar onde cada um dos 16 pilares aparece
- [ ] Uma funcionalidade de IA servida pela API (streaming SSE de LLM)

## Status
🔴 Não iniciado

---

# 🏗️ Projeto 4 — Sistema com Mensageria

**Nível:** Pleno · **Fase de origem:** 12

## Objetivo
Dois serviços conversando via Kafka ou RabbitMQ, com as garantias que separam demo de produção.

## Escopo
- [ ] Dois serviços independentes (produtor/consumidor)
- [ ] **Outbox Pattern** — evento e gravação no banco atomicamente
- [ ] **Consumidor idempotente** (entrega at-least-once)
- [ ] DLQ e retry com backoff
- [ ] Docker Compose com broker + bancos

## Normas a aplicar (Vol. 4)
- Documentar com **Modelo C4**
- Escrever **3 ADRs** justificando as decisões (broker escolhido, outbox, idempotência)

## Status
🔴 Não iniciado

---

# 🏗️ Projeto 5 — Full-Stack Completo

**Nível:** Pleno · **Fases de origem:** 7, 10, 12

## Objetivo
O sistema inteiro, ponta a ponta, com pipeline de produção.

## Escopo
- [ ] Backend Java + frontend TypeScript
- [ ] Tipos do front **gerados do OpenAPI** (`openapi-typescript`) — front nunca sai do contrato
- [ ] Postgres + Redis
- [ ] Tudo em Docker Compose
- [ ] CI no GitHub Actions: lint → test → build → scan → imagem → push

## Normas a aplicar (Vol. 4)
- **WCAG 2.2 AA** no frontend
- **Quality gate** no CI com SonarQube
- **SBOM** gerado no build

## Status
🔴 Não iniciado

---

# 🏗️ Projeto 6 — Servidor MCP

**Nível:** Pleno/Sênior · **Fase de origem:** 16

## Objetivo
Conectar IA a uma ferramenta real construindo um servidor **MCP (Model Context Protocol)** próprio.

## Escopo
- [ ] Servidor MCP expondo tools de um domínio real (ex.: consulta a telemetria predial)
- [ ] Structured outputs / function calling
- [ ] Streaming de resposta (SSE — retoma o pilar 4.14)
- [ ] Resiliência com provedor de LLM: timeout, retry, fallback, controle de custo por token

## Status
🔴 Não iniciado

---

# 🏗️ Projeto 7 — Capstone: Plataforma de Monitoramento Predial/Industrial

**Nível:** Sênior (projeto de conclusão) · **Fases de origem:** todas

> Este é o que te diferencia de todo mundo que fez o mesmo tutorial de "API de tarefas". Ele cruza os seus 10+ anos de automação com o seu novo perfil de engenheiro de software — e essa combinação é rara no mercado.

## Objetivo
Plataforma multi-prédio de monitoramento de alarmes de incêndio e telemetria.

## Escopo
- [ ] Ingestão de telemetria de dispositivos (MQTT → gateway → API)
- [ ] Banco time-series para histórico
- [ ] Alertas em tempo real via WebSocket/SSE
- [ ] Dashboard com histórico
- [ ] Módulo de diagnóstico com **RAG sobre manuais técnicos**
- [ ] **Multi-tenancy** (vários prédios/clientes — ver `05_arquiteto/02`)
- [ ] Este também é o sistema de referência para praticar System Design (Fase 14.5)

## Normas a aplicar (Vol. 4)
- ⭐ **IEC 62443** — segmentação por zonas, Security Levels
- **LGPD** — dados de ocupantes
- Requisitos de **disponibilidade** e **safety** pelas características da ISO 25010
- Rastreabilidade requisito → teste

## Status
🔴 Não iniciado
