# ☕ Java Avançado — JVM, Spring Security e Testes no Spring

> Fase 7.2, 7.8, 7.9 (Vol. 1). Parte Júnior em `01_junior/05` (livros lá). Spring Cloud/microsserviços no Sênior (`04_senior/03`).

---

## 7.2 JVM
- [ ] Compilação: `.java` → bytecode `.class` → JVM → JIT → código nativo
- [ ] **Áreas de memória**: Heap (young/old generation), Stack por thread, Metaspace, Code Cache
- [ ] **Garbage Collectors**: Serial, Parallel, CMS, **G1** (padrão), **ZGC** e Shenandoah (baixa pausa)
- [ ] Stop-the-world e tuning básico (`-Xms`, `-Xmx`)
- [ ] Classloading e o modelo de delegação
- [ ] Ferramentas: `jstack`, `jmap`, `jstat`, **VisualVM**, JProfiler, Java Flight Recorder
- [ ] Diagnóstico de memory leak com heap dump

---

## 7.8 Spring Security
- [ ] A **cadeia de filtros** (SecurityFilterChain) — o coração do Spring Security
- [ ] `AuthenticationManager`, `UserDetailsService`, `PasswordEncoder` (BCrypt)
- [ ] Autenticação stateless com **JWT** (implementar o filtro na mão pelo menos uma vez)
- [ ] Autorização: `@PreAuthorize`, `@Secured`, configuração por rota, `hasRole` vs `hasAuthority`
- [ ] **OAuth2 Resource Server** e OAuth2 Client
- [ ] CSRF: quando desabilitar (API stateless) e quando **não** (app com sessão/cookie)
- [ ] Method security e segurança em nível de objeto

## 7.9 Testes no Spring
- [ ] `@SpringBootTest` (integração) vs teste unitário puro
- [ ] `@WebMvcTest` + **MockMvc** — testar controller isolado
- [ ] `@DataJpaTest` — testar repositório
- [ ] `@MockBean` / `@MockitoBean`
- [ ] **Testcontainers** — testes de integração com banco real em container (padrão de mercado hoje)
- [ ] RestAssured para testes de API
