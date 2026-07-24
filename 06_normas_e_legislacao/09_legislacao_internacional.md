# 🌍 Legislação Internacional — GDPR, CRA, AI Act, NIS2

> Parte IX (Vol. 4).

---

# PARTE IX — Legislação Internacional

## IX.1 GDPR (Regulamento UE 2016/679)
- [ ] A LGPD é fortemente inspirada nele — conceitos quase equivalentes
- [ ] Diferenças relevantes: DPO obrigatório em mais casos, prazo de **72h** para notificar violação, multa até 4% do faturamento global
- [ ] **Aplica-se extraterritorialmente** — se você atende usuário na UE, se aplica a você no Brasil

## IX.2 EU Cyber Resilience Act (CRA) — Regulamento (UE) 2024/2847 🔄
> **Este é o mais importante e o mais desconhecido pelos desenvolvedores.** Ele transforma boa prática de engenharia em **obrigação legal com multa**.

- [ ] Escopo: praticamente **todo "produto com elementos digitais"** colocado no mercado da UE — hardware e software com conexão de dados
- [ ] <cite index="17-1">Entrou em vigor em 10 de dezembro de 2024; as obrigações de reporte passam a valer em 11 de setembro de 2026 e as obrigações principais em 11 de dezembro de 2027</cite>
- [ ] <cite index="13-1">As obrigações incluem SBOM em formato legível por máquina, engenharia *secure-by-design*, divulgação coordenada de vulnerabilidades e atualizações de segurança durante todo o período de suporte do produto; fabricantes têm 24 horas para o alerta inicial e 72 horas para a notificação completa de vulnerabilidade explorada</cite>
- [ ] <cite index="13-1">Multas podem chegar a €15 milhões ou 2,5% do faturamento anual global, o que for maior, e fabricantes fora da UE estão no escopo se seus produtos chegam ao mercado europeu</cite>
- [ ] Marcação **CE** e avaliação de conformidade para software
- [ ] **Por que isso é diretamente relevante para você:** produtos de automação predial, controladores, gateways IoT e o software embarcado neles entram no escopo. Se a IBSystems ou um cliente exportar ou integrar produto europeu, isso vira requisito contratual.

## IX.3 EU AI Act 🔄
- [ ] Modelo baseado em **risco**: inaceitável (proibido) → alto risco → risco limitado (transparência) → risco mínimo
- [ ] Obrigações para sistemas de alto risco: gestão de risco, governança de dados, documentação técnica, log, transparência, supervisão humana, robustez
- [ ] Regras específicas para modelos de propósito geral (GPAI)
- [ ] Aplicação faseada ao longo de 2025–2027 — **confirme o cronograma vigente**

## IX.4 Outros
- [ ] **NIS2** — resiliência cibernética de setores essenciais na UE (inclui infraestrutura e serviços digitais)
- [ ] **DORA (financeiro, UE)** — resiliência operacional, teste de resiliência, gestão de risco de terceiros
- [ ] **HIPAA** (saúde, EUA), **FedRAMP** (nuvem para governo americano), **CCPA/CPRA** (Califórnia)
- [ ] **EU Data Act** e **Digital Services Act** — dependendo do produto
