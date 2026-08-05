# O Mapa do Arquiteto — Estrutura Completa + Fontes por Tópico

> Reconstruído a partir do export CSV do Miro (304 nós + 148 links) e conferido nó a nó contra os prints do board original. Estrutura organizada pelas fases de progressão de carreira marcadas no board (troféus). Os links abaixo de cada bloco são os artigos/documentações que estavam posicionados naquele trecho do board — confirmados por proximidade espacial nos prints e por correspondência de conteúdo com o título do card.
>
> ⚠️ O pequeno ícone de seta em cada card do Miro **não é um link clicável para o artigo** — é o controle de expandir/colapsar do mapa mental (ou, em poucos casos, navega para outro ponto do mesmo board). Os links reais são cards de artigo separados, posicionados fisicamente perto do tópico. É esse posicionamento que usei para montar o mapeamento abaixo.

---

## 🚩 Largada

### Fundamentos
- Como funciona um computador
- Como os programas rodam na memória
- Como os processadores funcionam
- Sistemas Operacionais
- Diferença entre linguagem compilada x interpretada
  - 🖼️ Diagrama do Banco de Imagens: fluxo Source Code → Compiler/Bytecode/Interpreter → Machine Code, comparando Go/C/C++, Java e Python/Ruby
- Linux (Ubuntu ou Debian)
  - 📚 [Linux Command Cheat Sheet: 100 Essential Commands](https://medium.com/@prateek.malhotra004/linux-command-cheat-sheet-100-essential-commands-for-system-administration-and-development-6ee91049d71a)

### Escolha uma linguagem
- Linguagens: C#, Python, Javascript, Java, PHP, Ruby, Go, Rust, C++
- Lógica de programação
- Algoritmos e estruturas de dados
- Paradigmas de Programação → Procedural / Funcional / Orientada a Objetos (Abstração, Herança, Polimorfismo, Encapsulamento)
  - 📚 Treinamento completo: [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) · [CS50x 2025](https://cs50.harvard.edu/x/) · [Week 2 Programming Languages (CS50 Business)](https://cs50.harvard.edu/business/2017/weeks/2/)

### SQL e Bancos relacionais
- Escolha um banco: MySQL, SQLite, PostgreSQL, MariaDB, Oracle
- Operações de CRUD · Relacionamentos · ACID · Transações
  - 📚 [ACID Properties in DBMS](https://www.geeksforgeeks.org/acid-properties-in-dbms/) · [Transaction in DBMS](https://www.geeksforgeeks.org/transaction-in-dbms/) · [Indexing in Databases](https://www.geeksforgeeks.org/indexing-in-databases-set-1/) · [O que é o problema de N+1?](https://medium.com/linkapi-solutions/o-que-%C3%A9-o-problema-de-n-1-24975a28dcb8) · [SQL Performance Tuning](https://www.geeksforgeeks.org/sql-performance-tuning/)
  - 🖼️ Diagrama do Banco de Imagens: exemplo do problema N+1 (N SELECTs em loop) + refatoração em Python/SQLite usando parâmetro (`WHERE user_id = ?`)
  - 📚 Treinamento: [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/2024/) · [SQLBolt](https://sqlbolt.com/lesson/select_queries_introduction)

### Versionamento de Código
- Repositórios Remotos: Github, Gitlab, Bitbucket
- Escolha um framework: NestJS, Laravel, Spring Boot, Flask, Symfony, Ruby on Rails, ASP.NET, Django
  - 📚 [Lista de comandos úteis do GIT](https://gist.github.com/leocomelli/2545add34e4fec21ec16)

### Redes e Internet
- **Fundamentos da WEB**: Como a internet funciona · Nome de Domínio · DNS · URL · Protocolo HTTP · Cliente x servidor · Servidor Web · Cache
  - 📚 [Como a Internet funciona? (MDN)](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work) · [How DNS works](https://howdns.works/ep1/) · [What is a Domain Name? (MDN)](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_domain_name) · [What is a URL? (MDN)](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL) · [Visão geral cliente-servidor (MDN)](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview) · [O que é um servidor web (MDN)](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server) · [Servidor Web x servidor de aplicações (AWS)](https://aws.amazon.com/pt/compare/the-difference-between-web-server-and-application-server/) · [Como a Web funciona (MDN)](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) · [What are hyperlinks (MDN)](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_are_hyperlinks) · [Identificando recursos na web (MDN)](https://developer.mozilla.org/pt-BR/docs/orphaned/Web/HTTP/Basics_of_HTTP/Identifying_resources_on_the_Web) · [Qual a diferença entre página web, site, servidor (MDN)](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Getting_started/Environment_setup/Browsing_the_web)
  - 📚 Treinamento: [Week 1 Hardware (CS50)](https://cs50.harvard.edu/technology/2017/weeks/1/) · [Week 2 Internet (CS50)](https://cs50.harvard.edu/technology/2017/weeks/2/) · [Week 5 Web Development (CS50)](https://cs50.harvard.edu/technology/2017/weeks/5/) · [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/)

- **Segurança**: HTTP vs HTTPS · Login · Autenticação/Autorização · CORS · Cookies · Sessão · VPN · Firewall
  - 📚 [Using HTTP cookies (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies) · [Uma típica sessão HTTP (MDN)](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Session) · [JSON Web Tokens - jwt.io](https://jwt.io/) · [Autenticação x autorização, qual a diferença?](https://www.freecodecamp.org/portuguese/news/autenticacao-x-autorizacao-qual-e-a-diferenca/) · [Resolver problemas de CORS (Microsoft Entra ID)](https://learn.microsoft.com/pt-br/entra/identity/app-proxy/application-proxy-understand-cors-issues) · [Rate Limiting Fundamentals](https://blog.bytebytego.com/p/rate-limiting-fundamentals) · [Rate Limiting pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern) · [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
  - 📚 Treinamento: [Week 4 Security (CS50)](https://cs50.harvard.edu/technology/2017/weeks/4/)

- **APIs & Integrações**: O que é uma API · REST/RESTful · JSON · Métodos HTTP · Status codes · HATEOAS · Paginação/filtros/versionamento · gRPC · GraphQL · HTTP3
  - 📚 [O que é uma API (AWS)](https://aws.amazon.com/pt/what-is/api/) · [O que é a API RESTful (AWS)](https://aws.amazon.com/pt/what-is/restful-api/) · [Como versionar uma API REST](https://www.freecodecamp.org/portuguese/news/como-versionar-uma-api-rest/) · [Detailed Overview of HTTP Methods](https://medium.com/@reetesh043/detailed-overview-of-http-methods-271e88848b0d) · [HTTP Status Code Overview](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/iis/health-diagnostic-performance/http-status-code) · [O que é HATEOAS?](https://www.treinaweb.com.br/blog/o-que-e-hateoas) · [Uma visão geral do HTTP (MDN)](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Overview) · [HTTP caching (MDN)](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Caching) · [Saiba por que o JSON domina a Web](https://www.oracle.com/br/database/what-is-json/) · [gRPC x REST (AWS)](https://aws.amazon.com/pt/compare/the-difference-between-grpc-and-rest/) · [gRPC - .NET](https://learn.microsoft.com/pt-br/dotnet/architecture/cloud-native/grpc) · [API GraphQL vs. API REST (AWS)](https://aws.amazon.com/pt/compare/the-difference-between-graphql-and-rest/) · [O Que é HTTP/3](https://kinsta.com/pt/blog/http3/) · [ByteByteGo - Pagination in API Design](https://bytebytego.com/guides/how-do-we-perform-pagination-in-api-design/)

### Model-View-Controller (MVC) → Docker
- conceitos de conteinerização · Comandos básicos · Imagens/Volumes/Network · Dockerfile · Docker Compose

🏆 **Marco: Programador Júnior**

---

## Rumo a Pleno/Sênior

### Mais sobre bancos de dados
- Bancos não relacionais: Document Store (MongoDB) · Key-Value Store · Graph Database · Search Engine
  - 📚 [Types of NoSQL databases (AWS)](https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/types-of-nosql-databases.html)

### Clean Code Principles
- A regra do escoteiro · Mantenha classes/métodos/arquivos pequenos · Comente apenas o necessário · Use Nomes Significativos · Formatação e estilo de código · Evite abstrações precipitadas · Minimize complexidade ciclomática · Prefira exceções a códigos de erro · Seja consistente · O que são Testes de unidade · Evite passar booleanos e nulos · O que são Funções puras
  - *(referência: livro "Clean Code")*

### Orientação a Objetos Avançada
- **Princípios SOLID**: SRP · OCP · LSP · ISP · DIP
- **Object Calisthenics**: 9 regras (indentação única, sem ELSE, sem getters/setters, classes ≤50 linhas, etc.)

### Princípios de qualidade de Código
- DRY · KISS · YAGNI

### Testes Automatizados
- Testes unitários (80%) · integração (15%) · funcionais (5%)
  - 📚 [The Practical Test Pyramid (Martin Fowler)](https://martinfowler.com/articles/practical-test-pyramid.html)

### Design Patterns
> ⚠️ No board, os 3 grupos abaixo estão rotulados "Padrões Estruturais / Princípios Comportamentais / Object Criacionais", mas os padrões não seguem a categorização clássica do GoF (ex.: Observer/State/Strategy, que são comportamentais, aparecem em "Estruturais"). Reproduzido fielmente — vale confirmar com a fonte se foi um erro de organização.
- **"Padrões Estruturais"**: Observer, State, Strategy, Chain of Responsibility, Command, Iterator, Mediator, Memento, Visitor
- **"Princípios Comportamentais"**: Decorator, Facade, Proxy, Template Method, Adapter, Flyweight, Bridge, Composite
- **"Object Criacionais"**: Singleton, Simple Factory, Factory Method, Abstract Factory, Builder, Prototype

### Técnicas de Refactoring
- O que é débito técnico · Code Smells · Métodos de Composição · Organização de Dados · Expressões condicionais · Simplificar chamadas de métodos
  - 📚 [Refatoração e Padrões de Projeto (Refactoring Guru)](https://refactoring.guru/pt-br) · [Technical debt](https://refactoring.guru/pt-br/refactoring/technical-debt) · [Code Smells](https://refactoring.guru/pt-br/refactoring/smells) · [Composing Methods](https://refactoring.guru/refactoring/techniques/composing-methods) · [Organizing Data](https://refactoring.guru/refactoring/techniques/organizing-data) · [Simplifying Method Calls](https://refactoring.guru/refactoring/techniques/simplifying-method-calls) · [Simplifying Conditional Expressions](https://refactoring.guru/refactoring/techniques/simplifying-conditional-expressions)

### Otimização e Performance
- Cache-Aside Pattern · Jobs Assíncronos · Concorrência e Paralelismo · Otimização e performance de SQL · CDN
  - 📚 [Cache-Aside pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside) · [An Introduction to Asynchronous Processing and Message Queues](https://medium.com/hookdeck/an-introduction-to-asynchronous-processing-and-message-queues-218af596bf1b) · [Concurrency vs parallelism](https://oxylabs.io/blog/concurrency-vs-parallelism) · [Message Queues - System Design](https://www.geeksforgeeks.org/message-queues-system-design/) · [RabbitMQ Documentation](https://www.rabbitmq.com/docs) · [RabbitMQ Tutorials](https://www.rabbitmq.com/tutorials)
  - 🖼️ Diagrama do Banco de Imagens (Cache-Aside Pattern): comparação "No Caching" (app ↔ DB direto) vs "Cache-Aside Pattern" (app ↔ Cache ↔ DB) + diagrama de sequência (User → App → Cache → DB) mostrando cache miss/hit e escrita no cache
  - 🖼️ Diagrama do Banco de Imagens (Jobs Assíncronos): comparação "Sem Processamento assíncrono" (app processa e grava direto no DB) vs "Com Processamento assíncrono" (app publica no RabbitMQ → worker processa → grava no DB)

### Básico das Cloud Providers
- Comparativo AWS / Azure / Google Cloud
  - 📚 [Scalability and Elasticity in Cloud Computing](https://www.geeksforgeeks.org/scalability-and-elasticity-in-cloud-computing/)
  - *(Recomendação: certificação AWS Cloud Practitioner Foundational)*

### Pipelines de CI/CD
- Github Actions · Gitlab CI · Azure Devops Pipelines · Jenkins
  - 📚 [What is CI/CD? (GeeksforGeeks)](https://www.geeksforgeeks.org/what-is-ci-cd/) · [Quickstart for GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart)

🏆 **Marco: Programador Pleno/Sênior → Programador Completo!**

---

## 🏛️ Arquiteto de Software

### Arquitetura de Software
- **Níveis de Arquitetura**: Aplicação · Solução · Corporativa
- **Tipos de Arquiteto**: LLD · HLD · Corporativo
- **Papeis e Responsabilidades**: Requisitos funcionais e não funcionais (com exemplos práticos)

### Domain Driven Design
- **Modelagem Estratégica**: Linguagem Ubíqua · Domínio e Subdomínios · Bounded Contexts · Context Map
- **Modelagem Tática**: Entity · Value Object · Agregate Root · Repository · Domain Service · Factory
- **Ferramentas**: EventStorming · The Business Model Canvas · User Story Mapping · Domain Storytelling
  - 📚 [DDD Starter Modelling Process (GitHub)](https://github.com/RenatoAugustoFS/ddd-starter-modelling-process) · [EventStorming.com](https://www.eventstorming.com/)
  - *(referências: livros de DDD e "Aprendendo Domain-Driven Design")*

### Arquitetura em Camadas
- Clean Architecture · Arquitetura Hexagonal · Onion Architecture

### Monolíto modular

### Arquitetura de Microsserviços
  - 📚 [What are Microservices? (GeeksforGeeks)](https://www.geeksforgeeks.org/microservices/) · [Microservices (Martin Fowler)](https://martinfowler.com/articles/microservices.html) · [Microservices Guide (Martin Fowler)](https://martinfowler.com/microservices/) · [Microservice architecture style (Azure)](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices) · [O que são microsserviços (AWS)](https://aws.amazon.com/pt/microservices/) · [Client-Server Architecture](https://www.geeksforgeeks.org/client-server-architecture-system-design/)

### Arquitetura Orientada a Eventos | EDA
  - 📚 [Event-Driven Architecture (GeeksforGeeks)](https://www.geeksforgeeks.org/event-driven-architecture-system-design/)

### Arquitetura Serverless
  - 📚 [Serverless Architecture (GeeksforGeeks)](https://www.geeksforgeeks.org/serverless-architectures/) · [Serverless Architecture (Datadog)](https://www.datadoghq.com/knowledge-center/serverless-architecture/) · [Peer-to-Peer (P2P) Architecture](https://www.geeksforgeeks.org/peer-to-peer-p2p-architecture/)

🏆 **Marco: Arquiteto de Soluções**

---

## 📐 Requisitos Não Funcionais (NFRs) / System Design

### Planejamento de Capacidade
- Latência vs Throughput · Calcular a Carga (RPS) · Concorrência Simultânea · Utilização/Saturação de Recursos · Taxa de Erros
  - 📚 [Throughput e latência (AWS)](https://aws.amazon.com/pt/compare/the-difference-between-throughput-and-latency/) · [ByteByteGo - Back-of-the-envelope estimation](https://bytebytego.com/courses/system-design-interview/back-of-the-envelope-estimation)

### Escalabilidade e Performance
- Vertical vs Horizontal Scaling · Elasticidade · Load Balancing · Bottlenecks
  - 📚 [Horizontal and Vertical Scaling](https://www.geeksforgeeks.org/system-design-horizontal-and-vertical-scaling/) · [What is Load Balancer](https://www.geeksforgeeks.org/what-is-load-balancer-system-design/) · [Performance testing and antipatterns (Azure)](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/) · [ByteByteGo - Scale from zero to millions](https://bytebytego.com/courses/system-design-interview/scale-from-zero-to-millions-of-users)
  - **Banco de dados e estratégia de leitura**: Database Replication · CQRS · Estratégias de Cache · Database Sharding
    - 📚 [Data Replication (ByteByteGo)](https://blog.bytebytego.com/p/data-replication-a-key-component) · [Caching patterns (AWS)](https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/caching-patterns.html) · [Top 8 Cache Eviction Strategies (ByteByteGo)](https://bytebytego.com/guides/top-8-cache-eviction-strategies/) · [What is Sharding (AWS)](https://aws.amazon.com/what-is/database-sharding/)
    - **Redução de carga e latência**: Assincronicidade/Filas · CDN
      - 📚 [What is CDN in System Design](https://www.geeksforgeeks.org/what-is-content-delivery-networkcdn-in-system-design/)
      - **Performance Anti-Patterns**: Busy Database · Instanciação Imprópria · Persistência Monolítica · Noisy Neighbor · Retry Storm · No Caching

### Consistência de Dados
- Tipos de Consistência · Teorema CAP · Idempotência · ACID vs BASE
  - 📚 [Consistency in System Design](https://www.geeksforgeeks.org/consistency-in-system-design/) · [CQRS pattern (AWS)](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/cqrs-pattern.html) · [The CAP Theorem in DBMS](https://www.geeksforgeeks.org/the-cap-theorem-in-dbms/) · [ACID versus BASE (AWS)](https://aws.amazon.com/pt/compare/the-difference-between-acid-and-base-database/)

### Disponibilidade - Resiliência - Tolerância a falhas
- Redundância · Failover · Zero Downtime Deployment · Graceful Degradation · Chaos Engineering · Tracing e Monitoramento
  - 📚 [Availability in System Design](https://www.geeksforgeeks.org/availability-in-system-design/) · [High Availability in System Design](https://www.geeksforgeeks.org/what-is-high-availability-in-system-design/) · [Design Patterns for High Availability](https://www.geeksforgeeks.org/design-patterns-for-high-availability/) · [Circuit Breaker Pattern](https://www.geeksforgeeks.org/what-is-circuit-breaker-pattern-in-microservices/) · [Zero Downtime Deployments](https://www.geeksforgeeks.org/zero-downtime-deployments-in-distributed-systems/) · [Graceful Degradation](https://www.geeksforgeeks.org/graceful-degradation-in-distributed-systems/) · [Fault Tolerance](https://www.geeksforgeeks.org/fault-tolerance-in-distributed-system/) · [Retry pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [Redundancy in System Design](https://www.geeksforgeeks.org/redundancy-system-design/) · [Failover Mechanisms](https://www.geeksforgeeks.org/failover-mechanisms-in-system-design/) · [Distributed Tracing in Microservices](https://www.geeksforgeeks.org/distributed-tracing-in-microservices/)

### Segurança como Requisito Arquitetural
- VPN · WAF · DDoS · SQL Injection · Criptografia de dados
  - 📚 [Cyber Security Tutorial](https://www.geeksforgeeks.org/cyber-security-tutorial/) · [What is VPN, Types of VPN](https://www.geeksforgeeks.org/what-is-vpn-how-it-works-types-of-vpn/) · [What is a Web Application Firewall](https://www.geeksforgeeks.org/what-is-a-web-application-firewall/) · [What is DDoS](https://www.geeksforgeeks.org/what-is-ddosdistributed-denial-of-service/) · [What is SQL Injection](https://www.geeksforgeeks.org/sql-injection/) · [Cryptography and its Types](https://www.geeksforgeeks.org/cryptography-and-its-types/) · [What is Chaos Engineering](https://www.geeksforgeeks.org/what-is-chaos-engineering/)

### Recomendações finais
- 📚 [AWS Certified Solutions Architect – Associate](https://aws.amazon.com/pt/certification/certified-solutions-architect-associate/) · [– Professional](https://aws.amazon.com/pt/certification/certified-solutions-architect-professional/) · [Solutions Architect – Treinamento (AWS)](https://aws.amazon.com/pt/training/learn-about/architect/)
- 📚 [ByteByteGo – Technical Interview Prep](https://bytebytego.com/?fpr=renato-augusto10)

🏁 **Parabéns — fim da trilha**

---

## 📎 Apêndice — Recursos gerais (não ligados a um nó específico)

**Blogs de Engenharia**: [Cloud Design Patterns (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/) · [AWS Architecture Blog](https://aws.amazon.com/pt/blogs/architecture/) · [Netflix TechBlog](https://netflixtechblog.com/) · [The Cloudflare Blog](https://blog.cloudflare.com/) · [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/) · [Engineering at Meta](https://engineering.fb.com/) · [Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners) · [Stripe Blog: Engineering](https://stripe.com/blog/engineering) · [Discord Blog](https://discord.com/category/engineering) · [GitHub Engineering Blog](https://github.blog/category/engineering/) · [Engineering at Slack](https://slack.engineering/) · [Engineering at Uber](https://www.uber.com/en-BR/blog/rio-de-janeiro/engineering/) · [LinkedIn Engineering Blog](https://www.linkedin.com/blog/engineering)

**Newsletters**: [ByteByteGo (Alex Xu)](https://blog.bytebytego.com/) · [The System Design Newsletter (Neo Kim)](https://newsletter.systemdesign.one/) · [System Design Codex (Saurabh Dashora)](https://newsletter.systemdesigncodex.com/)

**Referências (pessoas)**: Alex Xu, Nina Durán, Raul Junco, Nelson Djalo, Vaughn Vernon, Neo Kim, Martin Fowler, Robert Martin, Sam Newman, James Lewis, Simon Brown, Grady Booch, Gaurav Sen — perfis linkados no board original (LinkedIn)

**Livros indicados**: Domain-Driven Design · Criando Microsserviços · Migrando de Monolitos a Microsserviços · Arquitetura de Software (a parte difícil) · Aprendendo Domain-Driven Design · Refatoração · O Programador Pragmático · System Design Interview (v1/v2) · Código Limpo · Padrões de Projeto (GoF) · Fundamentos da Arquitetura de Software · Designing Data-Intensive Applications (+ livros de educação financeira: O Homem Mais Rico da Babilônia, Pai Rico Pai Pobre, etc.)

**Catálogo de Vídeos** (canal do autor): SOLID, Object Calisthenics, Design Patterns (Adapter, State, Facade, Observer, Decorator, Proxy, Template Method, Singleton, Strategy, Cache-Aside)

**Treinamentos completos (CS50)**: [Hardware](https://cs50.harvard.edu/technology/2017/weeks/1/) · [Python](https://cs50.harvard.edu/python/) · [SQL](https://cs50.harvard.edu/sql/2024/) · [Internet](https://cs50.harvard.edu/technology/2017/weeks/2/) · [Security](https://cs50.harvard.edu/technology/2017/weeks/4/) · [Web Dev](https://cs50.harvard.edu/technology/2017/weeks/5/) · [CS50x 2025](https://cs50.harvard.edu/x/) · [Web Programming (Python/JS)](https://cs50.harvard.edu/web/) · [SQLBolt](https://sqlbolt.com/lesson/select_queries_introduction)

**Banco de Imagens**: os 4 diagramas dessa seção (frame solto no board, sem linha de conexão desenhada até o tronco principal) foram integrados por conteúdo diretamente nos tópicos correspondentes acima — ver marcações 🖼️ em "Diferença entre linguagem compilada x interpretada", "SQL e Bancos relacionais" e "Otimização e Performance".
