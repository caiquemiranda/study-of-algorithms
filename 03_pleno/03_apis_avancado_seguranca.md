# 🔐 APIs — Auth, Segurança, Docs e Performance

> Fase 6.6–6.12 (Vol. 1). Parte Júnior em `01_junior/04`.

---

## 6.6 Autenticação
- [ ] **Basic Auth** — Base64, e por que só serve sobre HTTPS
- [ ] **Token-based Auth** (Bearer)
- [ ] **JWT** — estrutura, assinatura, `exp`, refresh token, revogação (retomando a Fase 4.6)
- [ ] **Session-based Auth** — cookie + store server-side
- [ ] **OAuth 2.0** — os fluxos: Authorization Code (+ **PKCE**), Client Credentials, Device Code; e por que Implicit e Password Grant foram **descontinuados**
- [ ] **OIDC (OpenID Connect)** — a camada de *identidade* sobre OAuth2; `id_token`
- [ ] **SAML** — legado corporativo, mas vivo em SSO empresarial
- [ ] mTLS (autenticação mútua por certificado) — comum entre serviços internos
- [ ] API Keys: geração, **rotação**, escopos, armazenamento (hash, nunca em texto puro)

## 6.7 Autorização
- [ ] **RBAC** (Role-Based) — o mais comum; papéis e permissões
- [ ] **ABAC** (Attribute-Based) — decisão baseada em atributos do usuário/recurso/contexto
- [ ] **ReBAC** (Relationship-Based) — modelo do Google Zanzibar
- [ ] PBAC (Policy-Based), DAC (Discretionary), MAC (Mandatory)
- [ ] Escopos e permissões granulares
- [ ] Onde autorizar: gateway, filtro, service layer, ou banco (row-level security)

## 6.8 Segurança de API
- [ ] **OWASP Top 10** e **OWASP API Security Top 10** (são listas diferentes — estude as duas)
- [ ] Injection: SQL, NoSQL, Command, LDAP
- [ ] Broken Object Level Authorization (**BOLA/IDOR**) — a vulnerabilidade nº1 de APIs
- [ ] Mass Assignment / Excessive Data Exposure
- [ ] XSS, CSRF (e por que API stateless com Bearer token é menos vulnerável a CSRF)
- [ ] SSRF, XXE, Insecure Deserialization
- [ ] **CSP** (Content Security Policy), HSTS, security headers
- [ ] Gestão de segredos: variáveis de ambiente, Vault, AWS Secrets Manager — **nunca no Git**
- [ ] Sanitização de log (não logar senha, token, PII)

## 6.9 Documentação
- [ ] **OpenAPI / Swagger** — escrever a spec, gerar doc, gerar client
- [ ] Code-first vs Spec-first (Design First)
- [ ] **Postman / Insomnia / Bruno** — coleções, environments, testes automatizados
- [ ] Stoplight, Readme.com, Redoc
- [ ] Boa documentação: exemplos de request/response reais, erros documentados, changelog

## 6.10 Performance de API
- [ ] Métricas que importam: **latência p50/p95/p99** (não use média!), throughput, taxa de erro
- [ ] Estratégias de cache em cada camada (cliente, CDN, gateway, aplicação, banco)
- [ ] Load balancing (aprofunda na Fase 14)
- [ ] Compressão (`gzip`, `brotli`)
- [ ] Profiling e monitoramento
- [ ] **Retry com backoff exponencial + jitter** — e por que retry ingênuo causa *retry storm*
- [ ] Timeouts em todas as camadas (nunca deixar sem timeout)

## 6.11 Padrões de integração
- [ ] APIs síncronas vs assíncronas
- [ ] **API Gateway** — roteamento, auth centralizada, rate limit, agregação
- [ ] **BFF (Backend for Frontend)** — uma API por tipo de cliente
- [ ] **Event-Driven Architecture** — publish/subscribe, event sourcing (noção)
- [ ] Webhooks vs Polling — trade-offs
- [ ] Batch processing
- [ ] Filas de mensagem como integração (aprofunda na Fase 12)

## 6.12 Ciclo de vida, padrões e conformidade
- [ ] API Lifecycle: design → desenvolvimento → publicação → versionamento → **depreciação** (com `Sunset` header e prazo)
- [ ] Contract testing (Pact) — garantir que provider e consumer não quebrem um ao outro
- [ ] **LGPD** (é a lei que se aplica a você no Brasil) e **GDPR** (equivalente europeu)
- [ ] Conceito de **PII** (dados pessoais identificáveis) e minimização de dados
- [ ] PCI DSS (cartão), HIPAA (saúde, EUA) — saber que existem e quando se aplicam

**✅ Checkpoint da Fase 6:** você projeta uma API do zero em OpenAPI, com versionamento, paginação por cursor, rate limit, erros em RFC 7807 e OAuth2 — e defende cada decisão.

**📚 Livros:**
- *RESTful Web APIs* — Leonard Richardson & Mike Amundsen (a referência de REST)
- *API Design Patterns* — JJ Geewax (Google) — excelente e moderno
- *Designing Web APIs* — Brenda Jin et al. (prático, curto)
- *The Web Application Hacker's Handbook* — Stuttard & Pinto (segurança ofensiva; ler para saber se defender)
