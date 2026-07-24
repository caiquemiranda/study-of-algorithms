# 🇧🇷 Legislação Brasileira — LGPD, Marco Civil, Lei do Software

> Parte VIII (Vol. 4).

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
