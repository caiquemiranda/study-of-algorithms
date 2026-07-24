# 📋 Requisitos, Arquitetura e Documentação

> Parte III (Vol. 4): 29148, 42010, C4, arc42, ADR.

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
