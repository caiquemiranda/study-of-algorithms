# 🧩 SOLID e Design Patterns

> Fase 13.1–13.2 (Vol. 1). Arquiteturas (13.3+) no Sênior (`04_senior/03` — livros lá).

---

## 13.1 Princípios
- [ ] **SOLID**, um por um, com exemplo de violação e correção:
  - [ ] **S**ingle Responsibility
  - [ ] **O**pen/Closed
  - [ ] **L**iskov Substitution (o mais mal compreendido)
  - [ ] **I**nterface Segregation
  - [ ] **D**ependency Inversion (**e a diferença entre isso e Injeção de Dependência**)
- [ ] DRY, KISS, YAGNI — e quando o DRY vira acoplamento ruim
- [ ] Coesão alta, acoplamento baixo
- [ ] Lei de Deméter
- [ ] Composição sobre herança
- [ ] Separação de responsabilidades por camada

## 13.2 Design Patterns (GoF) — os que realmente aparecem
**Criacionais**
- [ ] Singleton (e por que costuma ser antipadrão fora do container de DI)
- [ ] Factory Method e Abstract Factory
- [ ] **Builder** (muito usado em Java)
- [ ] Prototype

**Estruturais**
- [ ] **Adapter** — integrar sistema legado
- [ ] **Decorator** — adicionar comportamento sem herança
- [ ] **Proxy** — é o mecanismo do `@Transactional` do Spring
- [ ] Facade — simplificar subsistema complexo
- [ ] Composite, Bridge, Flyweight

**Comportamentais**
- [ ] **Strategy** — o mais útil no dia a dia
- [ ] **Observer** — base de eventos
- [ ] **Template Method**
- [ ] **Chain of Responsibility** — é a cadeia de filtros do Spring Security
- [ ] Command, State, Iterator, Mediator, Visitor, Memento
