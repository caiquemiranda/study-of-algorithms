# 🔬 Metodologia — Provar que é Rápido e Disponível

> Módulo G (Vol. 2): USE/RED, teste de carga, coordinated omission, back-of-the-envelope.

---

# MÓDULO G — Metodologia: como você prova que é rápido e disponível
*(faça junto com o Módulo B)*

## G.1 Método de investigação de performance
- [ ] **Método USE** (Brendan Gregg): para cada recurso — **U**tilização, **S**aturação, **E**rros
- [ ] **Método RED** (para serviços): **R**ate, **E**rrors, **D**uration
- [ ] Os quatro sinais de ouro do Google SRE: latência, tráfego, erros, **saturação**
- [ ] Profiling: CPU profiler, **flame graphs**, async-profiler (Java), `perf`, eBPF
- [ ] Encontrar o gargalo antes de otimizar (**otimizar o lugar errado é desperdício puro**)
- [ ] Análise de causa raiz com dados; não confiar em intuição

## G.2 Teste de carga feito certo
- [ ] Tipos: **load** (carga esperada), **stress** (até quebrar), **soak/endurance** (24h+, revela memory leak), **spike** (pico súbito), **breakpoint**
- [ ] ⚠️ **Coordinated Omission** — o erro que invalida a maioria dos benchmarks: se o gerador de carga espera a resposta antes de enviar a próxima, ele **deixa de medir justamente os momentos ruins** e seu p99 fica lindo e falso. Ferramentas que corrigem isso: **wrk2**, k6 (com configuração correta), Gatling
- [ ] Testar em ambiente equivalente ao de produção (dados realistas, não tabela vazia)
- [ ] Modelar carga realista (distribuição de endpoints, think time, tamanho de payload real)
- [ ] Ferramentas: **k6** (recomendado — script em JS), Gatling, JMeter, Locust, wrk2
- [ ] Estabelecer **baseline** e detectar regressão de performance no CI
- [ ] Capacity planning: extrapolar da curva medida, não da esperança

## G.3 Estimativa de capacidade (back-of-the-envelope)
- [ ] Números que todo engenheiro deve ter na cabeça (*"Latency Numbers Every Programmer Should Know"* — Jeff Dean): cache L1 ~1ns · RAM ~100ns · SSD ~100µs · disco ~10ms · rede no mesmo DC ~0,5ms · rede intercontinental ~150ms
- [ ] Calcular QPS, storage, banda, número de servidores
- [ ] Relação pico/média (regra prática: pico ≈ 2 a 10× a média)
- [ ] Dimensionar pool de conexões, threads e memória com base em Little's Law
