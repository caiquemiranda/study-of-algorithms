# 🏢 Multi-Tenancy

> Módulo H.5 (Vol. 3). Central para plataforma que atende vários prédios/clientes.

---

## H.5 Multi-Tenancy
> Faltava por completo e é **central** para o tipo de produto que você pode construir (uma plataforma que atende vários prédios/clientes).

- [ ] O que é tenant e por que multi-tenancy é decisão de arquitetura, não de código
- [ ] **Os três modelos de isolamento de dados**:
  - [ ] **Banco por tenant** — isolamento máximo, custo e operação máximos
  - [ ] **Schema por tenant** — meio-termo (Postgres faz bem)
  - [ ] **Tabela compartilhada com `tenant_id`** — mais barato e escalável, mas o risco de vazamento entre tenants é real
- [ ] Como escolher: número de tenants, exigência regulatória, tamanho de cada tenant, custo
- [ ] **Identificação do tenant**: subdomínio, header, claim no JWT, path
- [ ] Propagação do contexto de tenant (ThreadLocal / `ScopedValue`, e o cuidado com pool de threads e código assíncrono)
- [ ] **Row-Level Security** (Postgres) como rede de segurança contra bug de aplicação
- [ ] Filtro automático de tenant no Hibernate (`@Filter`, `@TenantId`)
- [ ] **Noisy neighbor** — um tenant consumindo tudo; mitigar com rate limit e quota por tenant
- [ ] Migração de schema com N tenants (o problema operacional de rodar a mesma migration 500 vezes)
- [ ] Backup, restore e exportação **por tenant** (exigência de LGPD)
- [ ] Onboarding e offboarding automatizado de tenant
- [ ] Customização por tenant: feature flags, configuração, white-label
- [ ] Métricas e custo **por tenant** (conecta com FinOps)
