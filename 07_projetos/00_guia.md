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
