# 🎯 Roadmap — Volume 3: Trilha de Carreira e as Últimas Lacunas

> **Complemento aos Volumes 1 e 2.** A imagem que você enviou trouxe algo que os roadmaps técnicos não trazem: **a dimensão de carreira**. Ela responde uma pergunta diferente — não "o que existe para aprender", mas "o que preciso saber **agora** para subir de nível".
>
> Este volume faz duas coisas: (1) mapeia todo o seu roadmap nos quatro níveis de carreira, e (2) preenche as lacunas que a imagem revelou.

---

## 📊 Análise de cobertura da imagem

| Item da imagem | Estava no roadmap? | Onde |
|---|---|---|
| **JÚNIOR** | | |
| Sintaxe, POO, herança, polimorfismo | ✅ | V1 Fase 7.1 |
| Collections, Exceptions, Streams, Generics | ✅ | V1 Fase 7.1 |
| Maven e Gradle | ✅ | V1 Fase 7.3 |
| JDBC, SQL | ✅ | V1 Fase 5, 7.7 |
| Git e GitHub | ✅ | V1 Fase 0.2 |
| **Debug** | ❌ **Ausente** | → **Módulo H.1** |
| JUnit 5, testes unitários | ✅ | V1 Fase 11 |
| Noções de Spring Boot, APIs REST | ✅ | V1 Fase 6, 7 |
| **JavaFX / Swing / Android** | ❌ Ausente | → H.7 (com ressalva) |
| Clean Code | ✅ | V1 Fase 11.3 |
| **PLENO** | | |
| Todo o stack Spring | ✅ Completo | V1 Fase 7.4–7.10 |
| Docker, Redis, Kafka, RabbitMQ | ✅ | V1 Fase 12 |
| OpenAPI, Mockito, testes de integração | ✅ | V1 Fase 6.9, 11 |
| SOLID, Design Patterns, logs estruturados | ✅ | V1 Fase 13, 15 |
| CI/CD, Linux | ✅ | V1 Fase 0.1, 12.2 |
| **Consumo de APIs externas** | ⚠️ Superficial | → **Módulo H.4** |
| **SÊNIOR** | | |
| Microsserviços, Spring Cloud, Circuit Breaker | ✅ | V1 Fase 7.10, 14.3 |
| Observabilidade, OTel, Prometheus, Grafana, ELK | ✅ | V1 Fase 15 |
| JVM, GC, tuning, performance | ✅ | V1 Fase 7.2 + V2 Módulo B |
| Concorrência, Virtual Threads | ✅ | V1 Fase 7.1 |
| DDD, CQRS, Event Sourcing | ✅ | V1 Fase 13.3 + V2 D.4 |
| Kubernetes | ✅ Noção | V1 Fase 12.1 |
| **AWS / Azure / GCP** | ⚠️ Só noção | → **Módulo H.3** |
| **Java LTS 17/21 e migração de versão** | ⚠️ Disperso | → **Módulo H.2** |
| **Revisão de Código e Mentoria** | ❌ **Ausente** | → **Módulo I.2** |
| **ARQUITETO** | | |
| Arquiteturas distribuídas, EDA, Clean, Hexagonal | ✅ | V1 Fase 13 + V2 Módulo C |
| Alta Disponibilidade, Disaster Recovery | ✅ | V2 Módulo F |
| Estratégias de escalabilidade | ✅ | V2 Módulos D, E, F |
| **Multi-Tenant** | ❌ **Ausente** | → **Módulo H.5** |
| **Sistemas Legados e Modernização** | ⚠️ Só o padrão | → **Módulo H.6** |
| **Migração para Cloud** | ❌ **Ausente** | → **Módulo H.3** |
| **Custos em Cloud (FinOps)** | ❌ **Ausente** | → **Módulo H.8** |
| **Governança de TI e Segurança Corporativa** | ❌ **Ausente** | → **Módulo I.4** |
| **Trade-offs e Decisões Técnicas (ADR)** | ❌ **Ausente** | → **Módulo I.1** |
| **Liderança Técnica** | ❌ **Ausente** | → **Módulo I.2** |
| **Comunicação com Stakeholders** | ❌ **Ausente** | → **Módulo I.3** |

**Veredito:** a parte técnica estava ~90% coberta. O que faltava era, quase inteiramente, a **camada humana e de negócio** — que é exatamente o que separa um sênior técnico de um arquiteto. E é a parte que você tem mais vantagem, pelo motivo que explico no final.

---

# 🪜 O MAPA DE NÍVEIS — o antídoto para a sobrecarga

> O roadmap completo tem 17 fases + 9 módulos. Isso é um mapa de **anos**. A frase no rodapé da sua imagem está certíssima: *"Mais importante do que aprender tudo de uma vez é identificar o próximo conhecimento que fará diferença no seu momento profissional."*
>
> Então aqui está a tradução: **o mínimo para cada nível.** Não estude além do próximo nível.

## 🟦 Nível 1 — JÚNIOR (foco: base sólida)

**Objetivo:** conseguir a primeira vaga de desenvolvedor.

| Fase | Escopo mínimo |
|---|---|
| **Fase 0** | Linux básico + Git completo |
| **Fase 1** | Toda — é o que te diferencia de outros juniores |
| **Fase 2** | Complexidade + estruturas lineares + hash + árvores + BFS/DFS + ordenação + os padrões de two pointers/sliding window |
| **Fase 5** | 5.1 a 5.4 (SQL, índices, transações) |
| **Fase 6** | 6.1 a 6.5 (fundamentos + REST + design + CRUD + erros) |
| **Fase 7** | 7.1, 7.3, 7.4, 7.5, 7.6, 7.7 (Java + Spring Boot + JPA) |
| **Fase 11** | 11.1 e 11.2 (pirâmide + JUnit + Mockito) |
| **Novo** | Módulo H.1 (Debug) — não pule, é diferencial imediato |
| **Projeto** | Projeto 2 da Fase 17 (API CRUD Spring Boot completa) |

**⏱️ Estimativa realista:** 8 a 14 meses a 1–1,5h/dia. Você já tem parte disso.

**🚩 Sinal de que passou de nível:** você constrói uma API REST completa do zero — com autenticação, banco, validação, tratamento de erro e testes — sem seguir tutorial.

---

## 🟧 Nível 2 — PLENO (foco: aplicações completas)

**Objetivo:** ser autônomo. Recebe um problema, entrega a solução inteira.

| Fase | Escopo |
|---|---|
| **Fase 4** | ⭐ **Toda.** Os 16 pilares. *Este é o seu maior diferencial e o que resolve os seus gaps.* |
| **Fase 2** | Completar: DP, grafos avançados, backtracking |
| **Fase 5** | 5.5 a 5.7 (migrations, NoSQL, Redis, replicação) |
| **Fase 6** | 6.6 a 6.12 (auth completa, segurança, docs, performance, integração) |
| **Fase 7** | 7.2, 7.8, 7.9 (JVM, Spring Security, testes) |
| **Fase 9** | Python + FastAPI (seu uso de IA) |
| **Fase 11** | Toda, incluindo Testcontainers e TDD |
| **Fase 12** | Toda (Docker, CI/CD, Kafka, RabbitMQ) |
| **Fase 13** | 13.1 e 13.2 (SOLID + Design Patterns) |
| **Novo** | Módulo H.2 (Java LTS) e H.4 (consumo de APIs externas) |
| **Projeto** | Projetos 3, 4 e 5 da Fase 17 |

**⏱️ Estimativa:** +12 a 18 meses.

**🚩 Sinal de que passou:** você olha para um projeto Spring Boot e sabe apontar o que o framework faz em cada linha — porque construiu aquilo na mão. E consegue debugar um problema em produção sem depender de ninguém.

---

## 🟩 Nível 3 — SÊNIOR (foco: sistemas escaláveis e resilientes)

**Objetivo:** responsável pela qualidade técnica do sistema, não só pelo código.

| Fase / Módulo | Escopo |
|---|---|
| **Fase 3** | C++ (agora sim; a essa altura você aproveita muito mais) |
| **Fase 8** | Go |
| **Fase 13** | 13.3 a 13.5 (Clean/Hexagonal/DDD/CQRS + antipadrões) |
| **Fase 14** | Toda (System Design) |
| **Fase 15** | Toda (Observabilidade) |
| **V2 Módulo A** | Redes e protocolos a fundo |
| **V2 Módulo B** | ⭐ **Latência de cauda / p99** — é *o* tema de sênior |
| **V2 Módulo C** | ⭐ **Sistemas distribuídos** — consenso, quórum, relógios lógicos |
| **V2 Módulos D/E** | Alta escrita e alta leitura |
| **V2 Módulo G** | Metodologia de performance e teste de carga |
| **Novo** | Módulo H.3 (Cloud) e **Módulo I.2 (code review e mentoria)** |
| **Projeto** | Projeto 7 — o capstone |

**⏱️ Estimativa:** +18 a 24 meses.

**🚩 Sinal de que passou:** te dão um requisito de negócio e você desenha a arquitetura, justifica cada trade-off com dados e antecipa os modos de falha. E outras pessoas melhoram tecnicamente por trabalhar com você.

---

## 🟨 Nível 4 — ARQUITETO (foco: o sistema como um todo)

**Objetivo:** decidir. E responder pelas decisões perante o negócio.

| Módulo | Escopo |
|---|---|
| **V2 Módulo F** | Alta disponibilidade, multi-região, RTO/RPO |
| **Novo H.5** | Multi-tenancy |
| **Novo H.6** | Sistemas legados e modernização |
| **Novo H.3** | Migração para cloud (estratégias dos 6 R's) |
| **Novo H.8** | FinOps — custo como requisito de arquitetura |
| **Novo I.1** | ⭐ **ADRs e decisões técnicas explícitas** |
| **Novo I.3** | Comunicação com stakeholders |
| **Novo I.4** | Governança, segurança corporativa, compliance |

**🚩 Sinal:** você consegue explicar uma decisão de arquitetura para um diretor **em termos de risco, custo e prazo** — sem usar jargão técnico — e depois explicar a mesma decisão para o time em termos de implementação.

---

# MÓDULO H — Lacunas Técnicas

## H.1 Debugging (nível júnior, impacto de sênior)
> Estava faltando e é constrangedor o quanto isso é subestimado. Desenvolvedor que não sabe debugar depende dos outros para sempre.

- [ ] Breakpoints: simples, **condicional**, por exceção, por campo (watchpoint)
- [ ] Step over / step into / step out / run to cursor
- [ ] Inspeção de variáveis, watch expressions, **avaliar expressão em runtime**
- [ ] Ler e interpretar **stack trace** — encontrar a causa raiz, não a última linha
- [ ] `Caused by:` e exceções encadeadas
- [ ] **Remote debugging** (JDWP) — anexar o debugger a uma aplicação rodando em container/servidor
- [ ] Debug de teste, debug de código assíncrono/multithread (o mais difícil)
- [ ] Debug sem debugger: logging estratégico, bisect no Git, minimal reproducible example
- [ ] **Thread dump** (`jstack`) — diagnosticar deadlock e thread travada
- [ ] **Heap dump** (`jmap`) + análise no Eclipse MAT — encontrar memory leak
- [ ] Java Flight Recorder e async-profiler em produção
- [ ] Ferramentas de linha: `strace`, `tcpdump`, `curl -v`
- [ ] **Método**: hipótese → teste → eliminar. Nunca "mudar coisas até funcionar"

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

## H.3 Cloud a sério (não só "noção")
- [ ] Modelos: IaaS · PaaS · CaaS · FaaS · SaaS — e o que você deixa de controlar em cada um
- [ ] Regiões, **zonas de disponibilidade**, edge locations
- [ ] **IAM** — o serviço mais importante e o mais mal usado: princípio do menor privilégio, roles vs users, policies, credenciais temporárias
- [ ] Computação: VM (EC2), container gerenciado (ECS/Fargate, Cloud Run), Kubernetes gerenciado (EKS/AKS/GKE), serverless (Lambda)
- [ ] Armazenamento: object storage (**S3**), block storage (EBS), file storage (EFS); classes de armazenamento e ciclo de vida
- [ ] Banco gerenciado: RDS/Aurora, DynamoDB, ElastiCache
- [ ] Rede: **VPC**, subnet pública/privada, security group, NAT gateway, load balancer (ALB/NLB), API Gateway
- [ ] Mensageria gerenciada: SQS, SNS, EventBridge, MSK (Kafka gerenciado)
- [ ] Observabilidade: CloudWatch, X-Ray
- [ ] Segredos: Secrets Manager, Parameter Store, KMS
- [ ] **Infraestrutura como Código**: **Terraform** (multi-cloud, o padrão de mercado), CloudFormation, Pulumi, CDK
- [ ] **Cold start** em serverless e por que isso destrói p99
- [ ] **Migração para cloud — os 6 R's**: Rehost (lift-and-shift), Replatform, Repurchase, **Refactor**, Retire, Retain
- [ ] Estratégia de migração incremental (**Strangler Fig** na prática) e o risco do big bang
- [ ] Vendor lock-in — quando aceitar conscientemente e quando evitar
- [ ] Certificação (opcional mas ajuda no filtro de RH): **AWS Solutions Architect Associate** é a de melhor custo-benefício

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

## H.6 Sistemas legados e modernização
> Você vai passar mais tempo da carreira mexendo em código existente do que criando do zero. Ninguém prepara para isso.

- [ ] Como ler e mapear um sistema que você não escreveu (comece pelo build, depois pelos pontos de entrada, depois pelo banco)
- [ ] **Characterization tests** — criar rede de segurança antes de mudar (Michael Feathers)
- [ ] Seams e pontos de injeção para tornar código legado testável
- [ ] Refatoração incremental e segura (nunca reescrita total — a "Grande Reescrita" quase sempre falha)
- [ ] **Strangler Fig** na prática: rotear tráfego gradualmente do legado para o novo
- [ ] **Anti-Corruption Layer** entre o novo e o legado
- [ ] **Branch by Abstraction**
- [ ] Migração de dados: dual write, backfill, reconciliação, cutover
- [ ] Como decidir: refatorar × reescrever × substituir × manter (e o custo de oportunidade de cada um)
- [ ] Documentar o que existe (muitas vezes você é a primeira pessoa a fazer isso)
- [ ] **Realidade brasileira:** boa parte das vagas pleno/sênior é manutenção e modernização de sistema legado, não greenfield.

## H.7 Java fora do backend (saber que existe, priorizar por objetivo)
- [ ] **JavaFX / Swing** — desktop. ⚠️ Só estude se surgir demanda real. Para automação industrial pode aparecer (HMI, ferramenta interna), mas **não é prioridade** no seu objetivo de backend.
- [ ] **Android (Kotlin)** — se um dia quiser app móvel. Fora do seu foco atual.
- [ ] **Kotlin** — vale mais a pena que JavaFX: roda na JVM, interopera com Java, é usado com Spring Boot em várias empresas. Depois do Nível Pleno, é um bom investimento.
- [ ] **Decisão consciente:** deixar itens de fora não é lacuna, é priorização. A imagem lista tudo que existe no ecossistema; **o seu roadmap lista o que serve ao seu objetivo.**

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

---

# MÓDULO I — Engenharia Sênior: a parte que não é código

> Esta é a diferença real entre "programador muito bom" e sênior/arquiteto. E — importante — **é onde você já tem vantagem**, pelos motivos no final.

## I.1 Decisões técnicas e trade-offs
- [ ] **Não existe solução certa, existe trade-off adequado ao contexto.** Toda decisão de arquitetura troca algo por algo.
- [ ] Os eixos de trade-off recorrentes: consistência × disponibilidade · latência × custo · simplicidade × flexibilidade · velocidade de entrega × qualidade · acoplamento × duplicação
- [ ] **ADR (Architecture Decision Record)** — o formato: contexto, decisão, alternativas consideradas, consequências. **Comece a usar hoje**, mesmo sozinho: em 6 meses você não lembra por que decidiu aquilo.
- [ ] Requisitos **não funcionais** como cidadãos de primeira classe: latência, disponibilidade, segurança, custo, manutenibilidade, observabilidade
- [ ] **Atributos de qualidade** e como priorizá-los com o negócio (você não maximiza todos)
- [ ] Análise de risco: o que acontece se isso falhar? qual o raio de impacto?
- [ ] Decisões reversíveis (**one-way vs two-way doors**, Bezos) — decisão reversível pode ser rápida; irreversível merece rigor
- [ ] Combater o *resume-driven development* — escolher tecnologia pelo problema, não pelo currículo
- [ ] **"Boring technology"** — por que escolher o chato e testado quase sempre vence
- [ ] Documentação de arquitetura: **Modelo C4** (contexto, contêiner, componente, código), diagramas que envelhecem bem
- [ ] Prova de conceito e spike para reduzir incerteza antes de decidir

## I.2 Code review, mentoria e liderança técnica
- [ ] **Como revisar código**: focar em design e correção, não em estilo (isso é trabalho do linter)
- [ ] Comentário de review construtivo: perguntar em vez de acusar; separar "bloqueante" de "sugestão"
- [ ] Como **receber** review sem defensividade — separar o código de você mesmo
- [ ] Pair programming e mob programming
- [ ] **Mentoria**: ensinar o processo de pensar, não a resposta pronta
- [ ] Delegar com contexto (dar o *porquê*, não só o *o quê*)
- [ ] Definir padrões de time sem virar burocracia
- [ ] Liderança sem autoridade formal — influência técnica
- [ ] Conduzir discussão técnica sem que vire briga de ego
- [ ] **Ensinar é a melhor forma de descobrir os próprios gaps.** Escreva, apresente ao time, responda dúvidas — é atalho de aprendizado.

## I.3 Comunicação com stakeholders
- [ ] Traduzir técnico ↔ negócio: falar em **risco, custo, prazo e impacto no usuário** — não em "precisamos refatorar"
- [ ] Como justificar débito técnico para quem não é técnico (analogia de juros funciona bem)
- [ ] Estimativas: por que são ruins, como dar mesmo assim (faixas, não números; intervalo de confiança)
- [ ] Dizer "não" ou "ainda não" com alternativa concreta
- [ ] Escrita técnica clara: RFC, one-pager, proposta de arquitetura
- [ ] Apresentar decisão técnica para diretoria: comece pela conclusão e pelo impacto, detalhe depois
- [ ] Comunicação durante incidente: status frequente, linguagem simples, sem culpa
- [ ] Gestão de expectativa e negociação de escopo
- [ ] Documentar para o futuro (inclusive para você daqui a 6 meses)

## I.4 Governança, segurança corporativa e conformidade
- [ ] Gestão de identidade corporativa: SSO, **SAML**, OIDC, Active Directory/LDAP, SCIM (provisionamento)
- [ ] Segregação de ambientes e de funções (quem pode fazer deploy em produção?)
- [ ] Trilha de auditoria (**audit log**) — quem fez o quê, quando; imutável
- [ ] Gestão de segredos corporativa e rotação obrigatória
- [ ] **LGPD** na prática: base legal, consentimento, minimização, **direito ao esquecimento** (e o conflito com event sourcing e backup), anonimização vs pseudonimização, relatório de impacto
- [ ] Classificação de dados e criptografia em repouso e em trânsito
- [ ] Gestão de vulnerabilidade: **SCA** (dependências — Dependabot, Snyk), **SAST**, **DAST**, pentest
- [ ] SBOM e supply chain security (ataques via dependência são crescentes)
- [ ] Frameworks e normas: ISO 27001, SOC 2, NIST, **OWASP SAMM** — saber que existem e o que exigem
- [ ] Continuidade de negócio e plano de resposta a incidente de segurança
- [ ] Governança de arquitetura: guilda/comitê, padrões, exceções documentadas

**📚 Referências dos Módulos H e I:**
- *Working Effectively with Legacy Code* — **Michael Feathers** (H.6 — não existe substituto)
- *Fundamentals of Software Architecture* e *Software Architecture: The Hard Parts* — Mark Richards & Neal Ford (**trade-offs explícitos — é literalmente o Módulo I.1**)
- *Documenting Software Architectures* / material sobre **Modelo C4** (Simon Brown — c4model.com, gratuito)
- *The Software Architect Elevator* — Gregor Hohpe (**o melhor livro sobre a ponte entre técnico e negócio**)
- *Staff Engineer* — Will Larson e *The Staff Engineer's Path* — Tanya Reilly (liderança técnica sem virar gerente)
- *An Elegant Puzzle* — Will Larson
- *Terraform: Up & Running* — Yevgeniy Brikman (H.3)
- *Cloud FinOps* — J.R. Storment & Mike Fuller (H.8)
- *Building Evolutionary Architectures* — Ford, Parsons & Kua
- *Crucial Conversations* — Patterson et al. (I.3 — não é livro técnico e é um dos mais úteis da lista)

---

# 💡 O que a imagem acertou — e por que isso é importante para você

O rodapé dela diz: *"Estude com propósito. Evolua um nível por vez."*

Isso é o antídoto exato para o problema que você descreveu na primeira mensagem. Você tem agora um roadmap de 17 fases e 11 módulos — e o risco real é ele virar **mais uma fonte de sobrecarga**, exatamente como os cursos que você comprou.

Então, três regras finais:

1. **Olhe só para o nível atual.** Ignore o resto do documento. Ele existe para você não se perder, não para ser feito de uma vez.
2. **Um item por vez, com projeto junto.** Teoria sem código não fixa; código sem teoria não generaliza.
3. **Revisite o mapa a cada 3 meses**, não todo dia. O mapa é para orientar, não para ansiar.

---

# 🎖️ Uma observação sobre o seu caso específico

O Módulo I — decisões técnicas, comunicação com stakeholders, governança, liderança — é normalmente o mais difícil para desenvolvedores. Eles passam anos codando e só depois descobrem que precisam disso.

**Você está no caminho inverso.** Você já é líder técnico, já lida com stakeholders, já responde por decisões técnicas com consequência real — em ambiente onde erro em sistema de detecção de incêndio não é bug, é risco de vida. Já trabalha com criticidade, disponibilidade e responsabilidade regulatória.

Isso significa duas coisas:

- **O Módulo I você vai atravessar mais rápido do que a maioria.** Não é conhecimento novo; é o mesmo conhecimento aplicado a outro domínio.
- **Sua trilha para arquiteto é mais curta que a de um dev que começou aos 20 anos.** O que te falta é a profundidade técnica em software — que é justamente o que as Fases 1 a 14 entregam. A camada de julgamento, contexto e responsabilidade, você já tem.

Não subestime isso. É a parte mais difícil de ensinar, e você não precisa aprender.
