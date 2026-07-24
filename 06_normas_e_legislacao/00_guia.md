# ⚖️ Normas, Qualidade e Legislação — Guia

> Vol. 4: por que importa, o mapa das 7 famílias, priorização, certificações e como aplicar nos projetos.

---

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
