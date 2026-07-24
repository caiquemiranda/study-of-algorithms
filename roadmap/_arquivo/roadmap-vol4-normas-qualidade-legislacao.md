# ⚖️ Normas, Padrões e Legislação de Qualidade de Software

> **Roadmap — Volume 4.** Tudo que define, mede e regula qualidade de software em projetos grandes: normas técnicas, modelos de maturidade, frameworks de segurança e a legislação que hoje **obriga** práticas de engenharia.
>
> Este volume responde uma pergunta diferente dos anteriores. Eles respondiam *"como construir"*. Este responde *"segundo qual critério isso é considerado bom — e quem cobra"*.

---

## ⚠️ Aviso sobre datas

Normas técnicas são revisadas e leis mudam. As datas e status aqui refletem o cenário até meados de 2026. **Antes de usar qualquer item deste documento em decisão profissional, confirme a versão vigente** — especialmente as marcadas com 🔄.

---

## 🧭 Por que isso importa (e por que quase ninguém estuda)

Existe um abismo entre "meu código funciona" e "meu software é de qualidade". A maioria dos desenvolvedores atravessa a carreira inteira com uma noção **intuitiva** de qualidade — "código limpo", "bem testado", "rápido". Isso funciona em projeto pequeno e **desmorona** em projeto grande.

Em projeto grande, qualidade precisa ser:
- **Definida** — o que exatamente estamos chamando de qualidade?
- **Medida** — com número, não com opinião
- **Contratada** — está no contrato, no SLA, no edital
- **Auditada** — alguém de fora vai verificar
- **Legalmente exigida** — cada vez mais, não é opcional

E há um motivo prático e imediato: **licitação pública, contrato corporativo e cliente internacional citam essas normas nominalmente**. Quem sabe ler um edital que exige "conformidade com ABNT NBR ISO/IEC 25010" ou "processo aderente ao MPS.BR nível F" tem uma vantagem enorme sobre quem só sabe programar.

---

## 🗺️ O mapa: as 7 famílias

| Família | Pergunta que responde | Principais |
|---|---|---|
| **1. Qualidade de produto** | O software é bom? | ISO/IEC 25010 (SQuaRE) |
| **2. Qualidade de processo** | O jeito de construir é bom? | ISO/IEC 12207, CMMI, MPS.BR |
| **3. Engenharia de requisitos e arquitetura** | Está bem especificado e documentado? | ISO/IEC/IEEE 29148, 42010 |
| **4. Testes e verificação** | Está bem verificado? | ISO/IEC/IEEE 29119, ISTQB |
| **5. Segurança** | É seguro e resistente? | ISO 27001, OWASP ASVS/SAMM, NIST SSDF |
| **6. Legislação** | É legal? | LGPD, GDPR, CRA, AI Act |
| **7. Sistemas críticos** | Pode matar alguém se falhar? | IEC 61508, IEC 62443, IEC 62304 |

---

# PARTE I — Qualidade de Produto: ISO/IEC 25010

> **Se você só estudar uma norma da vida, que seja esta.** Ela é o vocabulário universal de qualidade de software.

## A família SQuaRE (ISO/IEC 25000)
- [ ] **ISO/IEC 2500n** — Divisão de gestão de qualidade (conceitos gerais)
- [ ] **ISO/IEC 25010** — ⭐ Modelo de qualidade de produto (o coração)
- [ ] **ISO/IEC 25012** — Modelo de qualidade de **dados**
- [ ] **ISO/IEC 25019** — Qualidade em uso / experiência
- [ ] **ISO/IEC 2502n** — Medição de qualidade (métricas)
- [ ] **ISO/IEC 2503n** — Requisitos de qualidade
- [ ] **ISO/IEC 2504n** — Avaliação de qualidade
- [ ] **ISO/IEC 25040** — Processo de avaliação
- [ ] No Brasil: adotadas como **ABNT NBR ISO/IEC 25010** etc.

## As características de qualidade (ISO/IEC 25010:2023 — 9 características)

> ⚠️ A versão de **2011** tinha 8 características (com *Usabilidade* e *Portabilidade*). A revisão de **2023** reorganizou para 9, incluindo **Segurança física (Safety)**. Muitos editais e livros ainda citam a versão de 2011 — conheça as duas.

| # | Característica | Subcaracterísticas | Onde isso aparece no seu roadmap |
|---|---|---|---|
| 1 | **Adequação Funcional** | Completude, correção, adequação | Requisitos, testes funcionais |
| 2 | **Eficiência de Desempenho** | Comportamento temporal, uso de recursos, capacidade | **Vol 2 Módulo B (p99)** |
| 3 | **Compatibilidade** | Coexistência, interoperabilidade | APIs, protocolos (Vol 2 Módulo A) |
| 4 | **Capacidade de Interação** (antes *Usabilidade*) | Reconhecibilidade, aprendizado, operabilidade, proteção contra erro, estética, **acessibilidade** | Parte VII deste doc |
| 5 | **Confiabilidade** | Maturidade, **disponibilidade**, tolerância a falha, recuperabilidade | **Vol 2 Módulo F** |
| 6 | **Segurança (Security)** | Confidencialidade, integridade, não-repúdio, responsabilização, autenticidade, resistência | Fase 6.8, Parte V deste doc |
| 7 | **Manutenibilidade** | Modularidade, reusabilidade, analisabilidade, modificabilidade, testabilidade | Fases 11 e 13 |
| 8 | **Flexibilidade** (absorveu *Portabilidade*) | Adaptabilidade, **escalabilidade**, instalabilidade, substituibilidade | Vol 2 Módulos D/E/F |
| 9 | **Segurança física (Safety)** 🆕 | Restrição operacional, identificação de risco, à prova de falha, aviso, integração segura | Parte X — **seu domínio** |

**Como usar isso na prática:**
- [ ] Ao levantar requisitos, percorra as 9 características e pergunte: *"qual o requisito não funcional aqui?"* — isso sozinho já te coloca acima da média
- [ ] Transformar cada uma em requisito **mensurável**: não "o sistema deve ser rápido", mas "p95 abaixo de 300ms com 500 usuários concorrentes"
- [ ] Priorizar: você **não maximiza todas**. Segurança conflita com usabilidade; performance conflita com manutenibilidade. Escolher é o trabalho do arquiteto.

**✅ Exercício:** pegue um sistema que você conhece e escreva um requisito mensurável para cada uma das 9 características.

---

# PARTE II — Qualidade de Processo

## II.1 ISO/IEC/IEEE 12207 — Ciclo de vida de software
- [ ] Os grupos de processo: acordo, organizacionais, técnicos de gestão, técnicos
- [ ] Processos técnicos: análise de requisitos → arquitetura → projeto → implementação → integração → verificação → transição → validação → operação → manutenção → descarte
- [ ] **ISO/IEC/IEEE 15288** — o equivalente para sistemas (hardware + software) — mais relevante para você, que trabalha com sistemas físicos
- [ ] Como isso mapeia (ou não) em Scrum/Kanban — as normas descrevem *o que* precisa acontecer, não *como*

## II.2 CMMI — Capability Maturity Model Integration
- [ ] Origem: SEI/Carnegie Mellon; hoje mantido pela ISACA
- [ ] **Os 5 níveis de maturidade**:
  1. **Inicial** — caótico, dependente de heróis
  2. **Gerenciado** — processos existem por projeto, planejamento e controle básicos
  3. **Definido** — processos padronizados na organização
  4. **Gerenciado Quantitativamente** — decisões por dados estatísticos
  5. **Em Otimização** — melhoria contínua baseada em dados
- [ ] Representação por estágios vs contínua
- [ ] Onde aparece: exigência em contrato com governo, multinacional e defesa
- [ ] Crítica honesta: CMMI mal aplicado vira burocracia. Bem aplicado, dá previsibilidade real.

## II.3 MPS.BR — o modelo brasileiro
> Muito relevante no Brasil e quase desconhecido por devs. Aparece em edital público.

- [ ] Criado pela **SOFTEX**, adaptado à realidade de PMEs brasileiras (CMMI é caro para empresa pequena)
- [ ] **7 níveis, de G (mais baixo) a A (mais alto)**:
  - **G** — Parcialmente Gerenciado
  - **F** — Gerenciado
  - **E** — Parcialmente Definido
  - **D** — Largamente Definido
  - **C** — Definido
  - **B** — Gerenciado Quantitativamente
  - **A** — Em Otimização
- [ ] Guias: MPS.BR Software (MPS-SW), Serviços (MPS-SV), Gestão de Pessoas, RH
- [ ] Compatível com CMMI e ISO/IEC 12207
- [ ] **Vantagem para você:** empresa de engenharia que quer vender para governo ou grande cliente frequentemente precisa disso — e alguém tem que entender

## II.4 ISO/IEC 33000 (ex-15504 / SPICE)
- [ ] Avaliação de capacidade de processo
- [ ] Níveis de capacidade 0 a 5 (Incompleto → Executado → Gerenciado → Estabelecido → Previsível → Inovador)
- [ ] Substituiu a antiga ISO/IEC 15504 (SPICE)
- [ ] Derivados setoriais: **Automotive SPICE** (indústria automotiva)

## II.5 Métricas modernas de engenharia (o contraponto ágil)
> As normas acima são pesadas. Estas são leves, orientadas a dados e é o que empresa de tecnologia usa hoje.

- [ ] **DORA — as 4 métricas-chave** (do livro *Accelerate*):
  1. **Frequência de deploy**
  2. **Lead time para mudança** (commit → produção)
  3. **Taxa de falha de mudança** (% de deploys que causam incidente)
  4. **Tempo para restaurar serviço** (MTTR)
  - *(uma quinta foi adicionada: confiabilidade / desempenho operacional)*
- [ ] Os 4 perfis: Elite, High, Medium, Low performers
- [ ] A descoberta contra-intuitiva do *Accelerate*: **velocidade e estabilidade não são trade-off** — quem entrega mais rápido também quebra menos
- [ ] **Framework SPACE** — produtividade de desenvolvedor além de linhas de código: Satisfaction, Performance, Activity, Communication, Efficiency
- [ ] ⚠️ Nunca use métrica de indivíduo como avaliação de pessoa — vira jogo de números e destrói o time

**📚 Referências da Parte II:**
- *Accelerate* — Forsgren, Humble & Kim (**leitura obrigatória**; é o único livro dessa parte que é prazeroso de ler)
- *SWEBOK Guide* (IEEE Computer Society) — o corpo de conhecimento de Engenharia de Software; **v4 disponível gratuitamente**, é o índice mestre da disciplina
- Guias do MPS.BR — **gratuitos** no site da SOFTEX
- *Engenharia de Software* — Ian Sommerville (o livro-texto clássico, em PT-BR — cobre normas e processos)
- *Engenharia de Software: Uma Abordagem Profissional* — Pressman & Maxim

---

# PARTE III — Requisitos, Arquitetura e Documentação

## III.1 Requisitos
- [ ] **ISO/IEC/IEEE 29148** — Engenharia de requisitos (substituiu a famosa IEEE 830)
- [ ] Características de um bom requisito: **necessário, verificável, não ambíguo, completo, consistente, rastreável, viável**
- [ ] Requisitos funcionais × **não funcionais** (que são as 9 características da ISO 25010)
- [ ] **Rastreabilidade** requisito → design → código → teste → aceitação (**obrigatória** em sistema crítico)
- [ ] Matriz de rastreabilidade
- [ ] Critérios de aceitação e **Definition of Done**
- [ ] Formatos: user story, caso de uso, especificação formal (**Gherkin/BDD** como ponte entre negócio e teste)

## III.2 Arquitetura
- [ ] **ISO/IEC/IEEE 42010** — Descrição de arquitetura: stakeholders, *concerns*, *viewpoints*, *views*
- [ ] Conceito-chave: **arquitetura não é um diagrama, é o conjunto de decisões estruturais e suas justificativas**
- [ ] **Modelo C4** (Simon Brown): Contexto → Contêiner → Componente → Código — c4model.com, **gratuito**
- [ ] **arc42** — template de documentação de arquitetura, **gratuito** e prático
- [ ] **ADR (Architecture Decision Record)** — retomando o Vol 3 I.1: contexto, decisão, alternativas, consequências
- [ ] Documentação que envelhece bem: diagrama gerado do código > diagrama desenhado à mão
- [ ] **ISO/IEC/IEEE 26511–26515** — documentação para usuário e gestão de informação

## III.3 Gestão de configuração
- [ ] Versionamento, baseline, controle de mudança
- [ ] **SemVer** (versionamento semântico) e changelog
- [ ] Build reproduzível e rastreável (qual commit gerou qual artefato em produção?)
- [ ] Gestão de release e ambientes

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

---

# PARTE V — Segurança

## V.1 Gestão da segurança da informação
- [ ] **ISO/IEC 27001** — Sistema de Gestão de Segurança da Informação (SGSI); é a que se **certifica**
- [ ] **ISO/IEC 27002** — Controles de segurança (o "como fazer" da 27001); ~93 controles em 4 temas
- [ ] **ISO/IEC 27005** — Gestão de risco de segurança
- [ ] **ISO/IEC 27017** — Segurança em nuvem
- [ ] **ISO/IEC 27018** — Proteção de dados pessoais em nuvem
- [ ] **ISO/IEC 27701** — Gestão de privacidade (PIMS) — a extensão da 27001 para LGPD/GDPR
- [ ] **ISO/IEC 27034** — Segurança de aplicações
- [ ] **NIST Cybersecurity Framework 2.0** — 6 funções: **Govern, Identify, Protect, Detect, Respond, Recover**
- [ ] **CIS Controls** — 18 controles priorizados; o mais prático para começar

## V.2 Desenvolvimento seguro
- [ ] **OWASP Top 10** e **OWASP API Security Top 10** — o mínimo absoluto
- [ ] ⭐ **OWASP ASVS** (Application Security Verification Standard) — **este é o padrão que você deve usar**: uma checklist verificável de requisitos de segurança, em 3 níveis (L1 básico, L2 padrão para a maioria das apps, L3 crítico). Coloque no contrato e no Definition of Done.
- [ ] **OWASP SAMM** — modelo de maturidade de segurança no desenvolvimento (governança, projeto, implementação, verificação, operações)
- [ ] **BSIMM** — o equivalente descritivo (mede o que empresas realmente fazem)
- [ ] **OWASP MASVS** — para mobile
- [ ] **OWASP Cheat Sheet Series** — o material prático mais útil da internet sobre segurança de aplicação
- [ ] **NIST SP 800-218 (SSDF)** — Secure Software Development Framework; 4 grupos: **PO** (preparar a organização), **PS** (proteger o software), **PW** (produzir software seguro), **RV** (responder a vulnerabilidades). Virou referência regulatória.
- [ ] **Microsoft SDL** — o precursor de tudo isso
- [ ] **Threat Modeling** — STRIDE, DREAD, PASTA, *attack trees*; e a pergunta central: *o que pode dar errado?*

## V.3 Vulnerabilidades e cadeia de suprimentos
- [ ] **CWE** — catálogo de tipos de fraqueza; **CWE Top 25**
- [ ] **CVE** — vulnerabilidades específicas identificadas
- [ ] **CVSS** — score de severidade (0–10); e a crítica de que score alto ≠ risco alto no *seu* contexto
- [ ] **EPSS** — probabilidade de exploração real (complementa o CVSS)
- [ ] **SBOM** (Software Bill of Materials) — formatos **SPDX** e **CycloneDX**. **Está virando obrigação legal** (ver CRA na Parte IX)
- [ ] **SLSA** — níveis de garantia de integridade da cadeia de build
- [ ] Sigstore, in-toto — assinatura e proveniência de artefato
- [ ] Ferramentas: **SCA** (Dependabot, Snyk, OWASP Dependency-Check), **SAST** (SonarQube, Semgrep, CodeQL), **DAST** (OWASP ZAP), **secret scanning** (gitleaks)
- [ ] Política de resposta: **CVD** (Coordinated Vulnerability Disclosure), `security.txt`, prazo de correção por severidade

## V.4 Setoriais
- [ ] **PCI DSS 4.0** — obrigatório para quem processa cartão; 12 requisitos, e os relacionados a desenvolvimento seguro são bem específicos 🔄
- [ ] **DORA (Digital Operational Resilience Act)** — regulamento europeu de resiliência operacional do setor financeiro (não confundir com as métricas DORA de DevOps — nomes iguais, coisas totalmente diferentes)
- [ ] **SOX** — controles internos e trilha de auditoria em empresa de capital aberto nos EUA
- [ ] Regulamentações do **Banco Central** e **Open Finance** para fintechs no Brasil

---

# PARTE VI — Métricas Objetivas de Qualidade de Código

## VI.1 ISO/IEC 5055 — Medidas automatizadas de qualidade de código
> Padrão do **CISQ** (Consortium for Information & Software Quality), adotado como norma ISO. Define 4 medidas **automatizáveis** a partir do código-fonte:
- [ ] **Confiabilidade** (Reliability)
- [ ] **Eficiência de desempenho** (Performance Efficiency)
- [ ] **Segurança** (Security)
- [ ] **Manutenibilidade** (Maintainability)
- [ ] Cada uma é medida contando ocorrências de padrões de fraqueza específicos (mapeados em CWE)
- [ ] Por que importa: dá um **número auditável** de qualidade de código, contratável e comparável entre fornecedores

## VI.2 Métricas clássicas
- [ ] **Complexidade ciclomática** (McCabe) — número de caminhos independentes; regra prática: >10 é sinal amarelo, >20 é vermelho
- [ ] **Complexidade cognitiva** (SonarSource) — mede o quão difícil é *entender*, não só percorrer; costuma ser mais útil que a ciclomática
- [ ] Métricas de Halstead (volume, dificuldade, esforço)
- [ ] **Índice de manutenibilidade**
- [ ] Acoplamento **aferente (Ca)** e **eferente (Ce)**; **instabilidade** `I = Ce/(Ca+Ce)`; abstratividade; **distância da sequência principal** (métricas de Robert Martin — a base matemática do Clean Architecture)
- [ ] LCOM — falta de coesão de métodos
- [ ] Profundidade de herança, fan-in/fan-out
- [ ] Duplicação de código (%)

## VI.3 Dívida técnica
- [ ] **Método SQALE** — quantifica dívida técnica em **tempo** (ex: "42 dias para remediar"), usado pelo SonarQube
- [ ] **Technical Debt Ratio** = custo de remediação ÷ custo de desenvolvimento
- [ ] O quadrante de dívida técnica de **Martin Fowler**: deliberada × inadvertida, prudente × imprudente
- [ ] Como registrar e priorizar dívida (backlog explícito, não folclore oral)
- [ ] **Como negociar com o negócio:** dívida técnica é juros. Todo mês que não paga, a próxima feature custa mais caro. Esse é o argumento que funciona.

## VI.4 Quality Gates
- [ ] Definir portões objetivos no CI: cobertura mínima, zero vulnerabilidade crítica, complexidade máxima, zero código duplicado acima de X%
- [ ] **Regra prática superior:** aplicar o gate ao **código novo/alterado**, não à base inteira (a estratégia "Clean as You Code" do SonarQube). Isso torna a melhoria viável em legado.

---

# PARTE VII — Acessibilidade (e é lei no Brasil)

> Frequentemente ignorada e **legalmente obrigatória**. Um dos poucos requisitos de qualidade que pode gerar processo judicial diretamente.

- [ ] **WCAG 2.2** (W3C) — as diretrizes de referência mundial
- [ ] Os 4 princípios (**POUR**): **P**erceptível, **O**perável, **C**ompreensível, **R**obusto
- [ ] Níveis de conformidade: **A**, **AA** (o alvo prático e o exigido por lei na maioria dos casos), **AAA**
- [ ] Critérios práticos: contraste, navegação por teclado, texto alternativo, foco visível, rótulo de formulário, tempo ajustável, sem dependência exclusiva de cor
- [ ] **ARIA** — atributos para tecnologia assistiva; e a primeira regra do ARIA: *não use ARIA se HTML semântico resolve*
- [ ] Testes: leitor de tela (NVDA, JAWS, VoiceOver), axe DevTools, Lighthouse, WAVE — **e teste manual com teclado**
- [ ] **Lei Brasileira de Inclusão (Lei 13.146/2015)** — o **art. 63** torna obrigatória a acessibilidade de sites; aplicável a empresas e órgãos públicos
- [ ] **Decreto 5.296/2004** — acessibilidade em sites do governo
- [ ] **eMAG** — Modelo de Acessibilidade em Governo Eletrônico (obrigatório para sites gov.br)
- [ ] **EN 301 549** (Europa) e **Section 508 / ADA** (EUA) — se atender cliente internacional
- [ ] Acessibilidade também é subcaracterística formal da **ISO 25010** (Capacidade de Interação)

---

# PARTE VIII — Legislação Brasileira

## VIII.1 LGPD — Lei 13.709/2018
> A que mais afeta seu dia a dia como desenvolvedor.

- [ ] Conceitos: dado pessoal, **dado pessoal sensível**, titular, controlador, operador, **encarregado (DPO)**
- [ ] **As 10 bases legais** do art. 7º (consentimento é só uma delas — e nem sempre a melhor); legítimo interesse; execução de contrato
- [ ] Princípios do art. 6º: finalidade, adequação, **necessidade (minimização)**, livre acesso, qualidade, transparência, segurança, prevenção, não discriminação, responsabilização
- [ ] **Direitos do titular**: confirmação, acesso, correção, anonimização/bloqueio/eliminação, **portabilidade**, revogação de consentimento, revisão de decisão automatizada
- [ ] **Implicações diretas de arquitetura**:
  - [ ] Como implementar "**direito ao esquecimento**" com backup, réplica, log e **event sourcing** (esse é um problema de arquitetura real, não jurídico)
  - [ ] Anonimização × pseudonimização (só a anonimização tira o dado do escopo da lei)
  - [ ] Retenção e expurgo automático — dado não pode ficar guardado "por via das dúvidas"
  - [ ] Criptografia em repouso e em trânsito
  - [ ] **Log de acesso a dado pessoal** (quem consultou o quê)
  - [ ] Privacy by Design e Privacy by Default — a lei exige isso desde a concepção
  - [ ] Transferência internacional de dados (relevante ao escolher região de nuvem)
- [ ] **RIPD** (Relatório de Impacto à Proteção de Dados)
- [ ] Comunicação de incidente de segurança à **ANPD** e aos titulares
- [ ] Sanções: advertência, multa de até 2% do faturamento limitada a R$ 50 milhões por infração, bloqueio e eliminação de dados
- [ ] **ANPD** — autoridade fiscalizadora; acompanhe as resoluções, que são o detalhamento prático

## VIII.2 Outras leis brasileiras relevantes
- [ ] **Marco Civil da Internet — Lei 12.965/2014**: neutralidade, **guarda obrigatória de logs** (registros de conexão por 1 ano; de acesso a aplicação por 6 meses), responsabilidade de provedor
- [ ] **Lei do Software — Lei 9.609/1998**: software é protegido como **obra intelectual** (regime de direito autoral, não de patente); prazo de 50 anos; registro no INPI é facultativo; contrato de licença; **titularidade do código desenvolvido por empregado pertence ao empregador**, salvo acordo — ponto importante para quem faz freelance
- [ ] **Lei de Direitos Autorais — Lei 9.610/1998**: complementa a anterior; base para entender licenças de código aberto
- [ ] **Código de Defesa do Consumidor (Lei 8.078/1990)**: aplica-se a software vendido a consumidor — vício do produto, direito de arrependimento em compra online (7 dias), publicidade enganosa
- [ ] **Lei 14.129/2021 — Governo Digital**: interoperabilidade, dados abertos, serviços digitais
- [ ] **Marco Legal das Startups — LC 182/2021**: sandbox regulatório, contratação pública de inovação
- [ ] **Lei 12.737/2012 (Lei Carolina Dieckmann)** e arts. do Código Penal sobre invasão de dispositivo — o limite legal de teste de segurança: **pentest sem autorização escrita é crime**
- [ ] Licenças de software livre (MIT, Apache 2.0, GPL, AGPL) — **compliance de licença é risco jurídico real**; GPL/AGPL em produto proprietário pode obrigar abertura do código

---

# PARTE IX — Legislação Internacional

## IX.1 GDPR (Regulamento UE 2016/679)
- [ ] A LGPD é fortemente inspirada nele — conceitos quase equivalentes
- [ ] Diferenças relevantes: DPO obrigatório em mais casos, prazo de **72h** para notificar violação, multa até 4% do faturamento global
- [ ] **Aplica-se extraterritorialmente** — se você atende usuário na UE, se aplica a você no Brasil

## IX.2 EU Cyber Resilience Act (CRA) — Regulamento (UE) 2024/2847 🔄
> **Este é o mais importante e o mais desconhecido pelos desenvolvedores.** Ele transforma boa prática de engenharia em **obrigação legal com multa**.

- [ ] Escopo: praticamente **todo "produto com elementos digitais"** colocado no mercado da UE — hardware e software com conexão de dados
- [ ] <cite index="17-1">Entrou em vigor em 10 de dezembro de 2024; as obrigações de reporte passam a valer em 11 de setembro de 2026 e as obrigações principais em 11 de dezembro de 2027</cite>
- [ ] <cite index="13-1">As obrigações incluem SBOM em formato legível por máquina, engenharia *secure-by-design*, divulgação coordenada de vulnerabilidades e atualizações de segurança durante todo o período de suporte do produto; fabricantes têm 24 horas para o alerta inicial e 72 horas para a notificação completa de vulnerabilidade explorada</cite>
- [ ] <cite index="13-1">Multas podem chegar a €15 milhões ou 2,5% do faturamento anual global, o que for maior, e fabricantes fora da UE estão no escopo se seus produtos chegam ao mercado europeu</cite>
- [ ] Marcação **CE** e avaliação de conformidade para software
- [ ] **Por que isso é diretamente relevante para você:** produtos de automação predial, controladores, gateways IoT e o software embarcado neles entram no escopo. Se a IBSystems ou um cliente exportar ou integrar produto europeu, isso vira requisito contratual.

## IX.3 EU AI Act 🔄
- [ ] Modelo baseado em **risco**: inaceitável (proibido) → alto risco → risco limitado (transparência) → risco mínimo
- [ ] Obrigações para sistemas de alto risco: gestão de risco, governança de dados, documentação técnica, log, transparência, supervisão humana, robustez
- [ ] Regras específicas para modelos de propósito geral (GPAI)
- [ ] Aplicação faseada ao longo de 2025–2027 — **confirme o cronograma vigente**

## IX.4 Outros
- [ ] **NIS2** — resiliência cibernética de setores essenciais na UE (inclui infraestrutura e serviços digitais)
- [ ] **DORA (financeiro, UE)** — resiliência operacional, teste de resiliência, gestão de risco de terceiros
- [ ] **HIPAA** (saúde, EUA), **FedRAMP** (nuvem para governo americano), **CCPA/CPRA** (Califórnia)
- [ ] **EU Data Act** e **Digital Services Act** — dependendo do produto

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

---

# PARTE XI — Inteligência Artificial

- [ ] **ISO/IEC 42001:2023** — Sistema de Gestão de IA (o "27001 da IA"); é certificável
- [ ] **ISO/IEC 23894** — Gestão de risco em IA
- [ ] **ISO/IEC 22989** — Conceitos e terminologia de IA
- [ ] **ISO/IEC 5338** — Ciclo de vida de sistemas de IA
- [ ] **NIST AI Risk Management Framework 1.0** — 4 funções: **GOVERN, MAP, MEASURE, MANAGE**
- [ ] **EU AI Act** (ver Parte IX.3)
- [ ] **Brasil — PL 2338/2023 (Marco Legal da IA)** 🔄: <cite index="7-1">foi aprovado por unanimidade no plenário do Senado em 10 de dezembro de 2024 e segue em tramitação na Câmara dos Deputados; adota o modelo europeu, classificando sistemas de IA por nível de risco (excessivo, alto, baixo/moderado), estabelece direitos dos afetados (transparência, explicação e contestação), cria o Sistema Nacional de Regulação e Governança de IA (SIA) e prevê sanções de até R$ 50 milhões por infração</cite>. <cite index="6-1">A votação, inicialmente prevista para o fim de 2025, foi adiada por impasses políticos</cite> — **acompanhe o status atual antes de qualquer decisão**
- [ ] Temas técnicos de conformidade: explicabilidade, viés e equidade, documentação de modelo (*model cards*), documentação de dados (*datasheets for datasets*), supervisão humana, avaliação de impacto algorítmico, rastreabilidade de decisão automatizada
- [ ] Conexão com a **LGPD**: art. 20 já garante direito à revisão de decisão automatizada

---

# PARTE XII — Governança de TI

- [ ] **COBIT 2019** — governança e gestão de TI corporativa; alinhamento TI–negócio, objetivos em cascata
- [ ] **ITIL 4** — gestão de serviços: gestão de incidente, problema, mudança, configuração, nível de serviço
- [ ] **TOGAF** — framework de arquitetura corporativa (ADM — Architecture Development Method)
- [ ] **ISO/IEC 20000** — gestão de serviços de TI (certificável)
- [ ] **ISO 22301** — continuidade de negócio (conecta com RTO/RPO do Vol 2 Módulo F)
- [ ] **ISO 31000** — gestão de risco (genérica, aplicável a tudo)
- [ ] **ISO 9001** — gestão da qualidade (genérica; muitas empresas de engenharia já têm)
- [ ] Relação entre elas: COBIT governa, ITIL opera, TOGAF estrutura, ISO certifica

---

# 🎯 Priorização: por onde começar

Este documento tem ~150 normas. Você **não** vai estudar todas. Ordem de retorno sobre esforço:

## Comece agora (retorno imediato)
1. ⭐ **ISO/IEC 25010** — as 9 características. É o vocabulário. Uma tarde de estudo, valor permanente.
2. ⭐ **OWASP Top 10 + ASVS L2** — segurança prática e verificável
3. ⭐ **Métricas DORA** — como medir se seu processo de entrega é bom
4. **Complexidade ciclomática e cognitiva + dívida técnica (SQALE)** — configure SonarQube num projeto seu e observe
5. **WCAG 2.2 nível AA** — é lei e é rápido de aprender o básico
6. **LGPD** — os princípios, as bases legais e as implicações de arquitetura

## Nível pleno
7. **ISO 29119 Parte 4** — técnicas de teste (valor limite e particionamento de equivalência sozinhos já mudam sua forma de testar)
8. **ISO/IEC/IEEE 29148** — como escrever requisito verificável
9. **NIST SSDF** e threat modeling (STRIDE)
10. **ISO/IEC/IEEE 42010 + C4 + ADR** — documentar arquitetura

## Nível sênior/arquiteto
11. **ISO 27001/27002** — o vocabulário de segurança corporativa
12. **CMMI ou MPS.BR** — se sua empresa for para certificação ou licitação
13. **EU CRA** — porque vira obrigação contratual em produto conectado
14. **COBIT/ITIL** — se for atuar em governança

## Para o **seu** perfil especificamente — prioridade máxima
15. ⭐ **IEC 62443** — segurança de automação industrial. **Esta é a sua mina de ouro.** Poucos entendem, a demanda é crescente e você já tem o contexto de OT.
16. ⭐ **IEC 61508 / SIL** — você já convive com isso em detecção de incêndio; formalizar esse conhecimento e cruzar com software é raríssimo
17. **IEC 61131-3** (especialmente ST) e **OPC-UA** — a ponte entre o seu passado e o seu futuro

---

# 🎓 Certificações que realmente valem

| Certificação | Vale para | Custo/esforço |
|---|---|---|
| **ISTQB Foundation** | Testes; reconhecida no Brasil (BSTQB) | Baixo |
| **AWS Solutions Architect Associate** | Nuvem; filtro de RH | Médio |
| **Certified Kubernetes Administrator (CKA)** | Se for para infraestrutura | Médio |
| **ISO 27001 Lead Implementer/Auditor** | Segurança corporativa | Médio-alto |
| **IEC 62443 Cybersecurity Specialist (ISA/IEC)** | ⭐ **Automação industrial — seu nicho** | Médio |
| **TÜV Functional Safety Engineer (IEC 61508)** | ⭐ Segurança funcional — seu nicho | Alto |
| **CISSP** | Segurança sênior (exige 5 anos de experiência) | Alto |
| **TOGAF** | Arquitetura corporativa | Médio |

> Certificação **não** substitui competência. Mas em edital público, contrato corporativo e filtro de RH, ela abre portas que competência sozinha não abre. As duas do seu nicho (ISA/IEC 62443 e TÜV 61508) têm relação valor/concorrência excepcional.

---

# 🔨 Como aplicar isso nos projetos do roadmap

Não estude norma no vácuo. Aplique nos projetos da Fase 17:

| Projeto | Norma a aplicar |
|---|---|
| API CRUD Spring Boot | Escreva requisitos não funcionais pelas **9 características da ISO 25010**; aplique **ASVS L1** |
| Sistema com mensageria | Documente com **C4** + escreva 3 **ADRs** justificando as decisões |
| Full-stack completo | **WCAG 2.2 AA** no frontend; **quality gate** no CI com SonarQube; **SBOM** no build |
| Capstone (monitoramento predial) | ⭐ **IEC 62443** (segmentação, SL); **LGPD** (dados de ocupantes); requisitos de **disponibilidade** e **safety** da ISO 25010; rastreabilidade de requisito → teste |

Um portfólio com **ADRs escritos, requisitos não funcionais mensuráveis e quality gate configurado** vale mais numa entrevista de pleno/sênior do que cinco projetos a mais sem isso. É a evidência visível de que você pensa como engenheiro, não como programador.

---

# 📚 Bibliografia

**Fundamentos e normas**
- *Engenharia de Software* — Ian Sommerville (PT-BR; cobre processos, requisitos, qualidade e sistemas críticos)
- *SWEBOK Guide v4* — IEEE (**gratuito**) — o índice mestre da disciplina
- *Software Engineering at Google* — Winters, Manshreck & Wright (**gratuito** online) — qualidade em escala real, com honestidade rara
- *Accelerate* — Forsgren, Humble & Kim
- Guias do **MPS.BR** — SOFTEX (**gratuitos**, em português)

**Segurança**
- *OWASP ASVS*, *SAMM* e *Cheat Sheet Series* — **gratuitos**, e melhores que a maioria dos livros pagos
- *Threat Modeling: Designing for Security* — Adam Shostack
- *The Web Application Hacker's Handbook* — Stuttard & Pinto
- *Alice and Bob Learn Application Security* — Tanya Janca (a introdução mais acessível)

**Qualidade e testes**
- *Base Practices* do syllabus **ISTQB Foundation** (**gratuito** no site do BSTQB, em português)
- *Refactoring* — Martin Fowler
- *Working Effectively with Legacy Code* — Michael Feathers

**Sistemas críticos**
- *Safety-Critical Systems Handbook* — David Smith & Kenneth Simpson (IEC 61508 na prática)
- *Industrial Network Security* — Knapp & Langill (IEC 62443 e Purdue na prática)
- *The Power of Ten* — Gerard Holzmann (NASA/JPL, artigo curto e gratuito)

**Legislação (Brasil)**
- Texto da **LGPD** comentado + resoluções e guias orientativos da **ANPD** (gratuitos no site da ANPD)
- Guia de Boas Práticas da LGPD para a Administração Pública

---

# 💬 Uma observação final

Existe uma armadilha nesta área: **transformar norma em burocracia**. Empresa que "implementa CMMI" gerando documento que ninguém lê, ou que "está em conformidade com a LGPD" com um pop-up de cookie e nada mais.

O propósito real de todas essas normas é um só: **tornar explícito e verificável aquilo que bons engenheiros faziam intuitivamente**. Elas existem porque intuição não escala para 200 pessoas, não sobrevive à rotatividade do time e não pode ser auditada.

Use-as como **checklist de pensamento**, não como ritual. A pergunta certa nunca é *"estamos conformes?"* — é *"o que essa norma está tentando evitar, e esse risco existe no meu caso?"*.

Quando a resposta for não, documente por que e siga em frente. Isso também é engenharia.
