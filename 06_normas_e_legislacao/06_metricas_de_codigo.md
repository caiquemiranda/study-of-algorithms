# 📏 Métricas Objetivas de Qualidade de Código

> Parte VI (Vol. 4): ISO 5055, complexidade, dívida técnica, quality gates.

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
