# 🔄 Versões do Java, Consumo de APIs Externas e Ecossistema

> Módulos H.2, H.4 e H.7 (Vol. 3).

---

## H.2 Versões do Java e migração
- [ ] O modelo de release: 6 meses por versão, **LTS a cada 2 anos** (8 → 11 → 17 → **21** → 25)
- [ ] Java 8: lambdas, streams, `Optional`, nova API de data/hora (`java.time`)
- [ ] Java 9–11: módulos (JPMS), `var`, HTTP Client nativo, `String` methods
- [ ] Java 12–17: **records**, sealed classes, switch expressions, text blocks, pattern matching for `instanceof`
- [ ] Java 18–21: **Virtual Threads**, pattern matching for `switch`, sequenced collections, structured concurrency (preview)
- [ ] Java 22–25: novidades recentes (consulte, pois muda rápido)
- [ ] **Migração de versão**: o que quebra (JPMS, remoção de módulos Java EE, mudanças de GC padrão), ferramenta `jdeprscan`, `jdeps`
- [ ] Distribuições da JDK: Oracle, **Temurin/Adoptium**, Corretto, Zulu, GraalVM — e as diferenças de licença
- [ ] **Realidade de mercado:** muita vaga ainda é Java 8/11. Saiba trabalhar nelas e saiba argumentar a migração.

---

## H.4 Consumo de APIs externas (disciplina própria)
> Você vai integrar com ERP, gateway de pagamento, API de LLM, SCADA. Consumir API bem é diferente de expor API bem.

- [ ] Cliente HTTP: `RestClient`/`WebClient` (Spring 6+), **OpenFeign**, `HttpClient` nativo
- [ ] **Timeout sempre** — de conexão e de leitura. API externa sem timeout é bomba-relógio.
- [ ] Retry com backoff + jitter, e **só em erro transitório** (5xx, timeout — nunca em 4xx)
- [ ] **Circuit breaker** em toda dependência externa (Resilience4j)
- [ ] Fallback e degradação quando o terceiro cai
- [ ] Cache de resposta de terceiro (e respeitar o `Cache-Control` deles)
- [ ] **Idempotência na sua ponta** — assumir que a chamada pode duplicar
- [ ] Rate limit do fornecedor: respeitar `429` e `Retry-After`
- [ ] Gestão de credenciais e rotação de token (refresh automático de OAuth2)
- [ ] **Anti-Corruption Layer** — nunca deixar o modelo do terceiro vazar para o seu domínio
- [ ] Versionamento e depreciação do fornecedor — como se proteger de quebra
- [ ] Testes: **WireMock/MockServer** para simular o terceiro; **contract testing**
- [ ] Sandbox vs produção; observabilidade específica (latência e taxa de erro **por fornecedor**)
- [ ] Webhook de entrada: validar assinatura HMAC, responder rápido e processar assíncrono, tratar reentrega

---

## H.7 Java fora do backend (saber que existe, priorizar por objetivo)
- [ ] **JavaFX / Swing** — desktop. ⚠️ Só estude se surgir demanda real. Para automação industrial pode aparecer (HMI, ferramenta interna), mas **não é prioridade** no seu objetivo de backend.
- [ ] **Android (Kotlin)** — se um dia quiser app móvel. Fora do seu foco atual.
- [ ] **Kotlin** — vale mais a pena que JavaFX: roda na JVM, interopera com Java, é usado com Spring Boot em várias empresas. Depois do Nível Pleno, é um bom investimento.
- [ ] **Decisão consciente:** deixar itens de fora não é lacuna, é priorização. A imagem lista tudo que existe no ecossistema; **o seu roadmap lista o que serve ao seu objetivo.**
