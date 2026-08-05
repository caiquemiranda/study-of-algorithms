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

### Object Calisthenics — as 9 regras (exercício, não lei)
> Criadas por Jeff Bay (*The ThoughtWorks Anthology*) como um kata: aplique as 9 ao pé da letra num exercício pequeno para sentir a dor dos extremos — não como padrão de produção. O ganho é o **hábito** que sobra depois de tirar o pé do acelerador.
- [ ] **Um nível de indentação por método** — força extrair método em vez de aninhar `if`/`for`
- [ ] **Não use `ELSE`** — *early return* ou polimorfismo no lugar do `if/else` (raiz do "sem `else`" está na Fase 13.1: Open/Closed)
- [ ] **Encapsule todos os primitivos e Strings** — `CPF`, `Email`, `Dinheiro` como Value Object em vez de `String`/`double` soltos (evita "obsessão primitiva" — bug clássico de trocar dois parâmetros do mesmo tipo)
- [ ] **Coleções de primeira classe** — uma classe que só existe para envelopar uma coleção (`PedidoItens` em vez de `List<Item>` passando de mão em mão)
- [ ] **Um ponto por linha** — Lei de Deméter levada ao limite: `a.b().c().d()` é proibido; fale só com quem você conhece diretamente
- [ ] **Não abrevie** — nomes completos, sem `qtd`, `tmp`, `mgr` (o custo de digitar é menor que o custo de decifrar depois)
- [ ] **Mantenha as entidades pequenas** — classes ≤ 50 linhas, pacotes ≤ 10 arquivos (limite artificial que expõe quando uma classe faz coisa demais)
- [ ] **No máximo 2 variáveis de instância por classe** — a regra mais controversa; o ponto real é forçar composição em vez de uma classe "Deus" com 15 campos
- [ ] **Sem getters/setters/properties públicos** — "Tell, Don't Ask": peça para o objeto fazer, não puxe o dado dele para decidir por fora (choca de propósito com o Java Bean tradicional — é o ponto principal do exercício)

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
