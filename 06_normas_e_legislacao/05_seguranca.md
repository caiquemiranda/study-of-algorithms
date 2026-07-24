# 🔒 Segurança — ISO 27001, OWASP, NIST SSDF, Supply Chain

> Parte V (Vol. 4).

---

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
