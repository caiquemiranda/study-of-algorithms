# ⚡ Engenharia de Latência de Cauda (p99)

> Módulo B (Vol. 2). ⭐ *O* tema de sênior.

---

# MÓDULO B — Engenharia de Latência de Cauda (p99)
*(módulo novo — estude após a Fase 12, revisite sempre)*

> **A premissa:** a média mente. Se 1% das suas requisições demora 3 segundos e você tem 100 chamadas internas por página, **63% dos usuários** vão sentir esse 1%. Latência de cauda é o problema mais mal compreendido de backend.

## B.1 Medição correta
- [ ] Por que **média e mediana escondem o problema**; sempre p50/p90/p95/**p99**/p99.9
- [ ] Percentis **não somam nem tiram média** — p99 de um agregado ≠ média dos p99
- [ ] **HdrHistogram** — por que histogramas comuns perdem precisão na cauda
- [ ] Latência **por endpoint**, não global (um endpoint lento contamina a métrica geral)
- [ ] Distinguir latência do servidor, da rede e percebida pelo usuário
- [ ] Instrumentar desde o primeiro dia — não dá para otimizar o que não se mede

## B.2 Teoria de filas — a matemática que explica tudo
- [ ] **Lei de Little**: `L = λ × W` (itens no sistema = taxa de chegada × tempo no sistema)
- [ ] **Utilização vs latência**: a curva é exponencial. A 80% de utilização a fila já explode; a 95%, o p99 desaparece. **Nunca opere um sistema perto de 100% de utilização.**
- [ ] Teoria de filas M/M/1 e M/M/c (noção)
- [ ] **Lei de Amdahl** — o teto de ganho ao paralelizar (a parte serial limita tudo)
- [ ] **Lei Universal de Escalabilidade (USL)** de Gunther — além da contenção, existe a **coerência** (custo de sincronizar): a partir de certo ponto, **adicionar servidor piora a performance**
- [ ] Saturação e o ponto de joelho (*knee*) da curva

## B.3 As causas reais da cauda longa
- [ ] **Pausas de Garbage Collection** (stop-the-world)
- [ ] **Contenção de lock** — thread esperando thread
- [ ] Fila de conexão cheia (pool esgotado, backlog TCP)
- [ ] **Noisy neighbor** — CPU/disco compartilhado em nuvem
- [ ] Escalonamento do SO e context switching
- [ ] Cache miss e cold start (JIT ainda não compilou, cache vazio, lambda frio)
- [ ] Retentativa e timeout mal configurados (o retry vira o problema)
- [ ] Query lenta esporádica (plano de execução mudou, tabela cresceu, lock no banco)
- [ ] **Head-of-line blocking** em qualquer camada
- [ ] Checkpoint/compactação de banco (LSM compaction, autovacuum do Postgres)
- [ ] Latência de disco e de rede em nuvem (variância natural)

## B.4 Técnicas de mitigação
**No runtime**
- [ ] Escolher o GC certo: **ZGC** ou **Shenandoah** (pausas sub-milissegundo) vs G1 (throughput). Medir, não adivinhar.
- [ ] Reduzir alocação (object pooling onde faz sentido, evitar autoboxing em hot path)
- [ ] Dimensionar heap corretamente (heap grande demais = GC longo; pequeno demais = GC frequente)
- [ ] JIT warmup e Ahead-of-Time (GraalVM native image) para eliminar cold start
- [ ] Java: **Virtual Threads** para trocar thread-per-request por concorrência barata

**Na arquitetura**
- [ ] **Hedged requests** — mandar a mesma requisição para 2 réplicas após o p95 e usar a primeira resposta (técnica do paper *The Tail at Scale*)
- [ ] **Tied requests** — as réplicas se avisam para cancelar a duplicata
- [ ] **Request coalescing / single-flight** — N requisições iguais viram 1 chamada ao backend
- [ ] **Timeout agressivo + fail fast** — melhor errar rápido que travar tudo
- [ ] **Budget de latência**: distribuir o SLA total entre as chamadas em cadeia (se o total é 200ms e há 4 saltos, cada um tem ~50ms)
- [ ] **Load shedding / admission control** — recusar carga excedente para proteger quem já está sendo atendido
- [ ] Isolamento por **Bulkhead** — pool separado por dependência
- [ ] **Backpressure** — propagar "estou cheio" em vez de acumular fila infinita
- [ ] Retry com **backoff exponencial + jitter** e **budget de retry** (nunca retry ilimitado)
- [ ] Processamento assíncrono: tirar do caminho crítico tudo que não precisa ser síncrono

**No I/O**
- [ ] Non-blocking I/O em todo o caminho (um único ponto bloqueante anula o resto)
- [ ] Connection pooling com dimensionamento correto (pool grande demais causa contenção no banco; pequeno demais causa fila na aplicação)
- [ ] Batching de chamadas e de escrita
- [ ] Reduzir round-trips: 1 query que traz tudo > 10 queries pequenas (o oposto do "chatty I/O")

**✅ Checkpoint do Módulo B:** você pega um serviço real, mede o p99, identifica a causa dominante da cauda com dados (não com palpite) e reduz o p99 — documentando a metodologia.

**📚 Referências do Módulo B:**
- 📄 **"The Tail at Scale"** — Jeff Dean & Luiz Barroso (Google, 2013) — **leia este paper. É curto e é o texto fundador do assunto.**
- *Systems Performance* — **Brendan Gregg** (2ª ed.) — a bíblia de performance; método USE
- *BPF Performance Tools* — Brendan Gregg
- *Optimizing Java* — Benjamin Evans, James Gough & Chris Newland
- *The Every Computer Performance Book* — Bob Wescott (curto e acessível)
- Blog e talks de **Gil Tene** (criador do HdrHistogram) sobre *Coordinated Omission* — mudam a forma como você mede
