# ☕ Java e Spring Boot — parte Júnior

> Fase 7.1, 7.3–7.7 (Vol. 1). Continua no Pleno: JVM, Spring Security e testes (`03_pleno/04`).

---

# FASE 7 — Java e Spring Boot em Profundidade [NÚCLEO]

## 7.1 Java — a linguagem
- [ ] Sintaxe, tipos primitivos vs wrappers, autoboxing (e a armadilha do `==` vs `.equals()`)
- [ ] **OOP de verdade**: encapsulamento, herança, polimorfismo, abstração
- [ ] Interface vs classe abstrata; `default methods`
- [ ] **Composição sobre herança** — e por quê
- [ ] `equals()` e `hashCode()` — o contrato entre eles e o que quebra no HashMap se você errar
- [ ] Imutabilidade, `final`, e `record` (Java 16+)
- [ ] **Collections Framework**: `List` (ArrayList vs LinkedList), `Set` (HashSet vs TreeSet vs LinkedHashSet), `Map` (HashMap vs TreeMap vs LinkedHashMap vs ConcurrentHashMap) — **quando usar cada um** (conecta com a Fase 2)
- [ ] Generics, wildcards (`? extends`, `? super`), type erasure
- [ ] **Exceptions**: checked vs unchecked, `try-with-resources`, quando criar exception customizada, por que nunca engolir exception
- [ ] **Streams API** e programação funcional: `map`, `filter`, `reduce`, `collect`, lazy evaluation
- [ ] `Optional` — usar certo (não como substituto de `null` em todo lugar)
- [ ] `Comparable` vs `Comparator`
- [ ] I/O e NIO
- [ ] **Concorrência**: `Thread`, `Runnable`, `ExecutorService`, `CompletableFuture`, `synchronized`, `volatile`, `AtomicInteger`, `ConcurrentHashMap`
- [ ] **Virtual Threads** (Java 21+) — a mudança de paradigma do Loom
- [ ] Novidades modernas: `var`, switch expressions, text blocks, sealed classes, pattern matching

---

## 7.3 Ecossistema e build
- [ ] **Maven** — `pom.xml`, ciclo de vida, dependências, escopos, plugins, multi-módulo
- [ ] **Gradle** — noção (muitos projetos modernos usam)
- [ ] Gerenciamento de dependências transitivas e conflito de versão

## 7.4 Spring — os fundamentos que ninguém explica
- [ ] **IoC (Inversão de Controle)** e o **Container** Spring
- [ ] **Injeção de Dependência**: por construtor (**preferida**), setter, campo — e por que `@Autowired` em campo é ruim
- [ ] **Beans**: ciclo de vida, `@Component`/`@Service`/`@Repository`/`@Configuration`
- [ ] **Escopos de bean**: singleton (padrão), prototype, request, session
- [ ] **AOP** (Programação Orientada a Aspectos): proxy dinâmico, `@Aspect`, e como `@Transactional` e `@Cacheable` funcionam por baixo (**é AOP, não mágica**)
- [ ] A armadilha do self-invocation (chamar método `@Transactional` de dentro da mesma classe não funciona — e você vai saber por quê)
- [ ] Configuração: `application.yml`/`.properties`, `@Value`, `@ConfigurationProperties`, **Profiles** (dev/staging/prod)
- [ ] Anotações essenciais e o que cada uma realmente faz

## 7.5 Spring Boot
- [ ] **Starters** — o que são e o que trazem
- [ ] **Autoconfiguration** — `@ConditionalOn...`, e como ler o relatório de autoconfiguração para entender o que o Boot ligou sozinho
- [ ] **Embedded Server** — Tomcat/Jetty/Undertow embutido; por que o JAR "roda sozinho"
- [ ] **Actuator** — health, metrics, info, env; e como proteger esses endpoints
- [ ] DevTools, hot reload

## 7.6 Spring MVC / Web
- [ ] Arquitetura: **DispatcherServlet** → HandlerMapping → Controller → ViewResolver (e como isso é a Fase 4.4 e 4.8 na prática)
- [ ] `@RestController`, `@RequestMapping`, `@GetMapping` e família
- [ ] `@RequestBody`, `@ResponseBody`, `@PathVariable`, `@RequestParam`, `@RequestHeader`
- [ ] `ResponseEntity` e controle fino de status/headers
- [ ] **Bean Validation** (`@Valid`, `@NotNull`, `@Size`, validador customizado)
- [ ] **`@ControllerAdvice` / `@ExceptionHandler`** — tratamento global de erro (implemente com RFC 7807)
- [ ] Filtros vs Interceptors — e onde cada um entra na cadeia
- [ ] Configuração de CORS
- [ ] **Spring WebFlux** e programação reativa (Mono/Flux) — saber que existe e quando faz sentido

## 7.7 Persistência
- [ ] **JDBC** puro primeiro (para ver o que o JPA esconde) e `JdbcTemplate`
- [ ] **JPA / Hibernate**: `@Entity`, `@Id`, estratégias de geração de ID
- [ ] **Relacionamentos**: `@OneToOne`, `@OneToMany`, `@ManyToOne`, `@ManyToMany`; `mappedBy` e lado dono
- [ ] **Fetch types**: LAZY vs EAGER — e por que EAGER é quase sempre um erro
- [ ] **`LazyInitializationException`** — por que acontece e como resolver certo
- [ ] **Ciclo de vida da entidade**: transient → managed → detached → removed
- [ ] **Persistence Context / 1st level cache**, `flush`, `dirty checking`
- [ ] **Problema N+1 no Hibernate** — detectar com log de SQL e resolver com `JOIN FETCH`, `@EntityGraph`, `@BatchSize`
- [ ] **Spring Data JPA**: repositórios, query methods derivados, `@Query` (JPQL e nativa), `Specification`, `Pageable`
- [ ] **`@Transactional`**: propagação (REQUIRED, REQUIRES_NEW, ...), isolamento, `readOnly`, rollback rules
- [ ] Spring Data JDBC e Spring Data MongoDB (noção)
- [ ] Migrations com **Flyway** ou Liquibase
- [ ] Connection pool **HikariCP** — tuning de pool size

---

**✅ Checkpoint da Fase 7:** você constrói uma API Spring Boot completa (auth JWT, JPA com relacionamentos, validação, tratamento global de erro, testes, migrations) e explica o que o framework faz em cada ponto — porque você já construiu aquilo na mão na Fase 4.

**📚 Livros:**
- *Effective Java* — **Joshua Bloch** — obrigatório. Leia depois de saber Java básico; é o livro que faz você escrever Java como profissional.
- *Java: Como Programar* — Deitel (base, em PT-BR) ou *Head First Java* (mais leve)
- *Spring in Action* — Craig Walls (a referência de Spring)
- *Spring Boot: Up and Running* — Mark Heckler
- *Java Concurrency in Practice* — Brian Goetz (denso, mas é *a* referência de concorrência em Java)
- *Java Persistence with Hibernate* — Bauer & King (para JPA a fundo)
- *Optimizing Java* — Benjamin Evans (JVM, GC e performance)
