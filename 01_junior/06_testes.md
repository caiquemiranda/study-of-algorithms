# ✅ Testes — parte Júnior

> Fase 11.1–11.2 (Vol. 1): pirâmide, AAA, mocks. Itens avançados (Testcontainers, TDD, carga, mutação) completam-se no Pleno (`03_pleno/06`).

---

# FASE 11 — Testes e Qualidade [NÚCLEO]

> **Estava faltando por completo na v1.** É o que mais separa júnior de pleno em entrevista técnica.

## 11.1 Pirâmide de testes
- [ ] Unitário (muitos, rápidos, isolados)
- [ ] Integração (menos, testam a junção com banco/fila/API externa)
- [ ] End-to-End (poucos, lentos, frágeis, mas valiosos)
- [ ] O antipadrão "cone de sorvete" (muitos E2E, poucos unitários)

## 11.2 Prática
- [ ] AAA: Arrange, Act, Assert
- [ ] Test doubles: **dummy, stub, spy, mock, fake** — saber a diferença de verdade
- [ ] Mockito (Java) / `unittest.mock` e `pytest-mock` (Python)
- [ ] **Testcontainers** — banco/Kafka reais em container para teste de integração
- [ ] Testes funcionais e de contrato (**Pact**)
- [ ] Testes de carga: **k6**, JMeter, Gatling, Locust — e como interpretar p95/p99
- [ ] Mocking de API externa: WireMock, MockServer
- [ ] Cobertura de código (JaCoCo) — **e por que 100% de cobertura não significa qualidade**
- [ ] **TDD** — red/green/refactor; pelo menos experimentar de verdade num projeto
- [ ] Testes de mutação (PIT) — a métrica que realmente mede a qualidade dos testes
