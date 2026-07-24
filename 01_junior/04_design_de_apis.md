# 🔌 Design de APIs — parte Júnior

> Fase 6.1–6.5 (Vol. 1). Continua no Pleno: auth, segurança, docs e performance (`03_pleno/03`).

---

# FASE 6 — Design de APIs [NÚCLEO]

> Consolida o roadmap "Building APIs" do roadmap.sh. Você já tem os fundamentos da Fase 4 — agora é sobre **projetar bem**.

## 6.1 Fundamentos
- [ ] O que é uma API, contrato, e por que ele é a "interface pública" do seu sistema
- [ ] URL, path parameters, query parameters, matrix parameters, fragmentos
- [ ] **Content Negotiation**: `Accept`, `Content-Type`, `Accept-Language`, `Accept-Encoding`
- [ ] **CORS** por dentro: preflight `OPTIONS`, `Access-Control-Allow-Origin`, credenciais, e por que o erro aparece só no navegador
- [ ] HTTP Caching aplicado a API (`ETag`, `Cache-Control`)

## 6.2 Estilos de API
- [ ] **REST** — os 6 constraints de Fielding, níveis do Modelo de Maturidade de Richardson
- [ ] Simple JSON APIs (o que 90% do mercado chama de "REST" e não é)
- [ ] **gRPC** — Protobuf, HTTP/2, streaming bidirecional; ideal para comunicação interna entre serviços
- [ ] **GraphQL** — schema, query, mutation, subscription, resolvers; o problema N+1 e o DataLoader
- [ ] **SOAP / XML** — saber ler (legado, ainda vivo em ERPs e integrações bancárias)
- [ ] **Webhooks** — API ao contrário; assinatura HMAC do payload, retry, idempotência
- [ ] Quando escolher cada um

## 6.3 Design First — projetar antes de codar
- [ ] **Princípios REST**: recursos, representações, stateless, interface uniforme
- [ ] **Design de URI**: substantivos no plural, hierarquia (`/clientes/{id}/pedidos`), sem verbos
- [ ] Modelagem de recursos e convenções de nomenclatura (camelCase vs snake_case — escolha uma e mantenha)
- [ ] **Versionamento**: na URL (`/v1/`), no header, por content-type — prós e contras
- [ ] **HATEOAS** — o nível 3 de REST (saber o que é, e por que quase ninguém usa)
- [ ] Design de DTOs: separar modelo de domínio do contrato de API

## 6.4 Manipulação de dados e requisições
- [ ] CRUD mapeado corretamente em métodos HTTP e status codes
- [ ] **Filtragem, ordenação e busca** — padrões de query string
- [ ] **Paginação**: offset/limit, page/size, **cursor-based** (e quando cada uma quebra)
- [ ] **Idempotência**: quais métodos são idempotentes por definição, e como implementar `Idempotency-Key` em POST (crítico para pagamento)
- [ ] Bulk operations e partial update (`PATCH` com JSON Merge Patch ou JSON Patch)
- [ ] Validação de entrada e mensagens de erro úteis

## 6.5 Controle de tráfego e erros
- [ ] **Rate Limiting**: algoritmos — Token Bucket, Leaky Bucket, Fixed Window, **Sliding Window**
- [ ] Headers de rate limit (`X-RateLimit-*`, `Retry-After`) e o status `429`
- [ ] Throttling vs rate limiting vs quota
- [ ] **RFC 7807 / RFC 9457 — Problem Details for HTTP APIs**: o formato padronizado de erro (`type`, `title`, `status`, `detail`, `instance`) — implemente isso, poucos fazem
- [ ] Tratamento de erro consistente: nunca vazar stack trace, sempre correlacionar com um trace ID
