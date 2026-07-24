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
