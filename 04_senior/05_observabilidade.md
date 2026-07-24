# 🔭 Observabilidade e Confiabilidade

> Fase 15 (Vol. 1).

---

# FASE 15 — Observabilidade e Confiabilidade [AMPLIAÇÃO]

- [ ] Os **três pilares**: logs, métricas, traces (e o quarto emergente: profiling contínuo)
- [ ] **Logging estruturado** (JSON), níveis de log, **correlation ID / trace ID** propagado entre serviços
- [ ] O que **nunca** logar: senha, token, PII
- [ ] **Métricas**: tipos (counter, gauge, histogram, summary); RED (Rate, Errors, Duration) e USE (Utilization, Saturation, Errors)
- [ ] Prometheus + Grafana; Micrometer no Spring
- [ ] **Tracing distribuído**: OpenTelemetry, Jaeger, Zipkin — spans e contexto propagado
- [ ] Agregação de logs: ELK/OpenSearch, Loki
- [ ] **Alertas que importam**: alertar em sintoma (usuário afetado), não em causa; evitar fadiga de alerta
- [ ] Health checks: liveness vs readiness
- [ ] Instrumentação, telemetria, visualização
- [ ] Postmortem sem culpa (*blameless*) e cultura de incidente
- [ ] Chaos Engineering (noção)

**📚 Livros:**
- *Site Reliability Engineering* — Google (**gratuito** em sre.google/books) — e o *SRE Workbook*, também grátis
- *Observability Engineering* — Charity Majors et al.
- *Release It!* — Michael Nygard (de novo — vale as duas fases)
