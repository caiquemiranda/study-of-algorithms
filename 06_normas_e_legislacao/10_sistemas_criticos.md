# 🚨 Sistemas Críticos — IEC 61508, 62443, 61131

> Parte X (Vol. 4). ⭐ Onde seu domínio de automação vira vantagem.

---

# PARTE X — Sistemas Críticos: onde seu domínio vira vantagem

> Aqui está o **seu diferencial mais forte de todos**. Você já vive num mundo onde software com falha não gera bug — gera vítima. A indústria de software está *aprendendo* isso agora, sob pressão regulatória. Você já sabe.

## X.1 Segurança funcional (Functional Safety)
- [ ] ⭐ **IEC 61508** — a norma-mãe de segurança funcional para sistemas elétricos/eletrônicos/programáveis
- [ ] **SIL (Safety Integrity Level) 1 a 4** — nível de redução de risco exigido; SIL 4 é o mais rigoroso
- [ ] Ciclo de vida de segurança: análise de perigo (HAZOP), determinação de SIL, especificação, projeto, verificação, validação, operação
- [ ] Falha sistemática × falha aleatória; PFD (probabilidade de falha sob demanda); tolerância a falha de hardware
- [ ] Requisitos de software por SIL: **rastreabilidade total**, restrição de linguagem, cobertura **MC/DC**, análise estática obrigatória, revisão formal, testes de injeção de falha
- [ ] **Derivadas setoriais**: **IEC 61511** (processo), **ISO 26262** (automotivo, com ASIL A–D), **EN 50128** (ferroviário), **IEC 62304** (dispositivo médico — classes A/B/C), **DO-178C** (aviônica — níveis DAL A–E, o mais rigoroso que existe)

## X.2 Segurança cibernética industrial (OT)
- [ ] ⭐ **IEC 62443** — a norma de segurança para sistemas de automação e controle industrial
- [ ] Conceito de **zonas e condutos** (segmentação); **Security Levels SL 0 a 4**
- [ ] **IEC 62443-4-1** — ciclo de vida de desenvolvimento seguro de produto (é o equivalente industrial do NIST SSDF)
- [ ] **IEC 62443-4-2** — requisitos técnicos de segurança para componentes
- [ ] **IEC 62443-3-3** — requisitos de segurança de sistema
- [ ] **Modelo Purdue** de arquitetura industrial (níveis 0 a 5) e a segmentação IT/OT
- [ ] A diferença fundamental de prioridade: em TI a tríade é **C-I-A** (confidencialidade primeiro); em OT é **A-I-C** — **disponibilidade primeiro**, porque parar a planta é o dano

## X.3 Normas do seu domínio direto
- [ ] **ABNT NBR 17240** — Sistemas de detecção e alarme de incêndio: projeto, instalação, comissionamento e manutenção
- [ ] **ABNT NBR 9441**, **NBR 5410** (instalações elétricas de baixa tensão), **NBR 5419** (proteção contra descargas atmosféricas)
- [ ] **NR-10** (segurança em eletricidade) e **NR-12** (máquinas e equipamentos)
- [ ] Instruções Técnicas do Corpo de Bombeiros do seu estado
- [ ] **IEC 61131-3** — as 5 linguagens de programação de CLP: **LD** (Ladder), **FBD** (blocos funcionais), **ST** (texto estruturado), **IL** (lista de instruções, obsoleta), **SFC** (sequenciamento). ST é essencialmente uma linguagem imperativa — e sua ponte natural entre CLP e software
- [ ] **IEC 61499** — o modelo distribuído orientado a evento (a evolução da 61131 para sistemas distribuídos)
- [ ] **OPC-UA (IEC 62541)** — o padrão de interoperabilidade da Indústria 4.0, com modelo de informação e segurança embutidos

## X.4 Práticas de codificação para software crítico
- [ ] **MISRA C / MISRA C++** — regras restritivas de codificação para sistemas embarcados críticos
- [ ] **CERT C/C++/Java** (SEI) — regras de codificação segura
- [ ] **AUTOSAR C++14** — automotivo
- [ ] Princípios: sem alocação dinâmica em runtime, sem recursão, limites determinísticos de tempo e memória, **The Power of Ten** (regras da NASA/JPL para código crítico)
- [ ] Verificação formal e análise estática profunda (Frama-C, Polyspace, Astrée)
- [ ] Redundância, diversidade e voto (2oo3), watchdog, fail-safe × fail-operational

> **💡 O ponto estratégico:** existem pouquíssimos profissionais que entendem simultaneamente arquitetura de software moderna **e** IEC 61508/62443/61131. A convergência IT/OT é uma das áreas com maior demanda e menor oferta de gente qualificada no mundo. Você está a um roadmap de distância de estar nessa interseção.
