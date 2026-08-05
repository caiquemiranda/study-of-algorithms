# 🏛️ Arquiteturas de Aplicação e Sistema + Spring Cloud

> Fase 13.3–13.5 e 7.10 (Vol. 1): Hexagonal, Clean, DDD, CQRS, microsserviços, antipadrões.

---

## 13.3 Arquiteturas de aplicação
- [ ] **Camadas** (Controller → Service → Repository) — o que a maioria faz
- [ ] **Arquitetura Hexagonal / Ports & Adapters**
- [ ] **Clean Architecture** — a regra de dependência apontando para dentro
- [ ] Onion Architecture
- [ ] **DDD (Domain-Driven Design)**: entidade, value object, agregado, repositório, serviço de domínio, bounded context, linguagem ubíqua
  - [ ] **Context Map** — desenhar as relações entre bounded contexts (Partnership, Shared Kernel, Customer-Supplier, Conformist, Anticorruption Layer) — sem isso o "bounded context" fica um conceito solto, sem mostrar onde um módulo invade o outro
  - [ ] **EventStorming** — workshop com pós-its laranjas (eventos de domínio) para descobrir o modelo junto com quem entende do negócio, antes de escrever uma linha de código; big picture → process modeling → design level
  - [ ] **Domain Storytelling** — narrar o processo de negócio como uma história (atores → ações → objetos) para validar que você entendeu o fluxo real, não o que você *acha* que é o fluxo
  - [ ] **User Story Mapping** — organizar histórias de usuário por jornada (eixo horizontal) e prioridade (eixo vertical) — expõe buracos de escopo que uma lista plana de backlog esconde
  - [ ] **Business Model Canvas** — visão de uma página do modelo de negócio (proposta de valor, canais, receita, custo); útil para o arquiteto entender **por que** o sistema existe antes de desenhar **como**
  - [ ] Quando usar cada um: EventStorming para descobrir o domínio, Context Map para desenhar fronteiras entre times/sistemas, Story Mapping para fatiar entrega — ferramentas complementares, não concorrentes
- [ ] **CQRS** — separar modelo de leitura e escrita
- [ ] **Event Sourcing** — estado como sequência de eventos
- [ ] MVC, MVP, MVVM (contexto)

## 13.4 Arquiteturas de sistema
- [ ] **Monolito** (e o **monolito modular** — a resposta certa para 90% dos projetos)
- [ ] **Microsserviços**: benefícios reais e os custos escondidos (rede, consistência, observabilidade, deploy, time)
- [ ] SOA
- [ ] **Serverless** — quando compensa, cold start
- [ ] Service Mesh (Istio, Linkerd) — noção
- [ ] **Strangler Fig** — migrar legado incrementalmente
- [ ] Anti-Corruption Layer
- [ ] Sidecar, Ambassador, Gateway (Routing / Offloading / Aggregation)
- [ ] BFF (Backends for Frontends)

## 13.5 Antipadrões de performance (saber reconhecer)
- [ ] Chatty I/O (muitas chamadas pequenas)
- [ ] Busy Database (lógica de negócio no banco)
- [ ] Busy Frontend
- [ ] Extraneous Fetching (buscar mais dados do que precisa — o `SELECT *` da vida)
- [ ] Improper Instantiation (criar cliente HTTP/conexão a cada chamada)
- [ ] Monolithic Persistence
- [ ] Noisy Neighbor
- [ ] Retry Storm
- [ ] Synchronous I/O bloqueante
- [ ] No Caching

---

## 7.10 Microsserviços com Spring Cloud
- [ ] Quando **não** usar microsserviços (comece monolito modular — sério)
- [ ] **Spring Cloud Gateway** — API Gateway
- [ ] **Config Server** — configuração centralizada
- [ ] **Eureka / Service Discovery**
- [ ] **OpenFeign** — cliente HTTP declarativo
- [ ] **Resilience4j** — Circuit Breaker, Retry, Bulkhead, Rate Limiter
- [ ] **Micrometer** — métricas e tracing distribuído

---

**📚 Livros:**
- ⭐ *Clean Architecture* — **Robert C. Martin** — a explicação mais clara de dependência e fronteira
- *Design Patterns* (GoF) — Gamma, Helm, Johnson & Vlissides — o original (denso); **alternativa mais leve:** *Head First Design Patterns* (Freeman) ou o site Refactoring.Guru (excelente e em PT-BR)
- *Domain-Driven Design* — Eric Evans (o "livro azul"; denso) — **comece por** *Implementing Domain-Driven Design* (Vaughn Vernon) ou *Learning DDD* (Vlad Khononov)
- *Introducing EventStorming* — Alberto Brandolini (o criador da técnica; também em [eventstorming.com](https://www.eventstorming.com/), gratuito)
- *Patterns of Enterprise Application Architecture* — Martin Fowler
- *Building Microservices* — **Sam Newman** (2ª ed.) — honesto sobre os custos
- *Monolith to Microservices* — Sam Newman
- *Fundamentals of Software Architecture* — Mark Richards & Neal Ford
- *A Philosophy of Software Design* — John Ousterhout (curto, brilhante, e discorda do Clean Code em pontos importantes — ler os dois é formador)
