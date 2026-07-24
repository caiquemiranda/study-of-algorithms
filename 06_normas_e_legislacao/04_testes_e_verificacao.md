# 🧪 Testes e Verificação — 29119, ISTQB

> Parte IV (Vol. 4).

---

# PARTE IV — Testes e Verificação

## IV.1 ISO/IEC/IEEE 29119 — Testes de software
- [ ] **Parte 1** — Conceitos e definições
- [ ] **Parte 2** — Processos de teste (organizacional, gestão, dinâmico)
- [ ] **Parte 3** — Documentação (plano de teste, especificação, relatório)
- [ ] **Parte 4** — ⭐ **Técnicas de teste** (a parte mais útil no dia a dia)
- [ ] **Parte 5** — Teste orientado a palavra-chave

## IV.2 Técnicas de teste (Parte 4 — estude estas de verdade)
**Baseadas em especificação (caixa-preta)**
- [ ] **Particionamento de equivalência** — dividir entrada em classes que se comportam igual
- [ ] **Análise de valor limite** — a técnica que mais encontra bug com menos esforço (testar 0, 1, max-1, max, max+1)
- [ ] Tabela de decisão
- [ ] Teste de transição de estado
- [ ] Teste de caso de uso
- [ ] **Combinatorial / pairwise testing** — cobrir combinações sem explosão fatorial

**Baseadas em estrutura (caixa-branca)**
- [ ] Cobertura de comando (statement)
- [ ] Cobertura de decisão/ramo (branch)
- [ ] Cobertura de condição e **MC/DC** (Modified Condition/Decision Coverage) — **exigida em software aeronáutico e de segurança crítica**
- [ ] Cobertura de caminho

**Baseadas em experiência**
- [ ] Teste exploratório, error guessing, checklist

## IV.3 Verificação e validação
- [ ] **IEEE 1012** — Verificação e Validação
- [ ] **Verificação** = construímos o produto **certo**? (aderência à especificação)
- [ ] **Validação** = construímos o produto **correto**? (atende à necessidade real)
- [ ] **IEEE 1028 / ISO/IEC 20246** — Revisões: inspeção formal (Fagan), walkthrough, revisão técnica, revisão por pares
- [ ] Análise estática vs dinâmica

## IV.4 ISTQB e certificação
- [ ] **ISTQB Foundation Level** — a certificação de teste mais reconhecida; o syllabus é **gratuito** e vale a leitura mesmo sem fazer a prova
- [ ] Níveis: Foundation → Advanced (Test Analyst, Technical Test Analyst, Test Manager) → Expert
- [ ] Especializações: Agile Tester, Security Tester, Performance Testing, AI Testing
- [ ] No Brasil: **BSTQB** é o board nacional

## IV.5 Métricas de teste
- [ ] Cobertura de código — e por que **100% de cobertura não significa qualidade**
- [ ] **Mutation score** — a métrica que realmente mede se seus testes detectam bugs (PIT/Pitest para Java)
- [ ] Densidade de defeito, taxa de escape de defeito (bugs que chegaram em produção)
- [ ] Flakiness — teste instável destrói a confiança na suíte inteira
