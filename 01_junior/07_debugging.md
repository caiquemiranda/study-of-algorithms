# 🐞 Debugging

> Módulo H.1 (Vol. 3) — nível júnior, impacto de sênior.

---

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
