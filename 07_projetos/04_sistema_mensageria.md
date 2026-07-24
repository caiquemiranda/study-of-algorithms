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
