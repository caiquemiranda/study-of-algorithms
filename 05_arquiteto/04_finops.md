# 💰 FinOps — Custo como Requisito de Arquitetura

> Módulo H.8 (Vol. 3).

---

## H.8 FinOps — custo como requisito de arquitetura
- [ ] Modelos de precificação: sob demanda, reservado, **spot**, savings plan
- [ ] Os custos que surpreendem: **transferência de dados de saída (egress)**, cross-AZ traffic, NAT gateway, requisições em object storage, log retido
- [ ] Custo por requisição / por tenant / por feature — **unit economics**
- [ ] Rightsizing — a maioria dos ambientes está superdimensionada
- [ ] Trade-off explícito: cache custa memória mas economiza banco; serverless é barato em baixo tráfego e caro em alto
- [ ] Tagging e alocação de custo por time/produto
- [ ] Orçamento e alerta de anomalia de custo
- [ ] **Custo como requisito não-funcional**, ao lado de latência e disponibilidade
- [ ] Custo de arquitetura ≠ custo de infraestrutura: microsserviços custam em observabilidade, deploy, rede e **tempo de gente**
