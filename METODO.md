# 🧭 Método de Estudo

> Como usar este repositório: sistema de marcação, regras, mapa geral das fases e avisos.
> Fonte: Volumes 1, 2 e 3 (originais em `roadmap/_arquivo/`).

---

## 📋 Como usar este roadmap

### Sistema de marcação
Passe por **todos** os itens uma vez marcando o status. Não estude ainda — só classifique:

- 🔴 **Zero** — nunca estudei. Estudar do início, com prática.
- 🟡 **Superficial** — já usei/ouvi falar, mas não sei explicar como funciona por dentro. **Esses são seus buracos.** É o item mais importante da lista.
- 🟢 **Domino** — já expliquei para alguém, já usei com profundidade. Pula na 1ª passada.

### As 3 regras que resolvem seu problema

1. **Nunca avance de fase com 🔴 pendente na fase atual.** Foi pular fundamento que criou os buracos.
2. **🟡 é mais perigoso que 🔴.** O 🔴 você sabe que não sabe. O 🟡 te dá falsa confiança e te derruba lá na frente.
3. **Segunda passada obrigatória.** Terminou tudo? Volte e refaça os 🟢. Você vai descobrir que alguns eram 🟡 disfarçados.

### Teste de domínio real (aplique em cada item antes de marcar 🟢)
> Consigo explicar isso em voz alta, sem consultar nada, para alguém que não sabe — incluindo **por que existe** e **o que aconteceria se não existisse**?

Se não: é 🟡.

### Ordem de prioridade se o tempo apertar
As fases marcadas **[NÚCLEO]** são inegociáveis para o seu objetivo. As **[APOIO]** podem ser feitas em paralelo, mais devagar, ou depois. As **[AMPLIAÇÃO]** são para consolidar sênior.

---

## 🧭 Mapa geral

| # | Fase | Peso | Por que aqui |
|---|---|---|---|
| 0 | Ferramentas base (Linux, terminal, Git) | [NÚCLEO] | Sem isso nada mais funciona |
| 1 | Computação, memória, SO, redes | [NÚCLEO] | Base de todos os buracos |
| 2 | Algoritmos e Estruturas de Dados | [NÚCLEO] | Vocabulário de raciocínio |
| 3 | C++ — baixa abstração | [APOIO] | Ver o que Java/Python escondem |
| 4 | A Web sem frameworks (16 pilares) | [NÚCLEO] | Desmistifica Spring/FastAPI |
| 5 | SQL e Bancos Relacionais | [NÚCLEO] | Toda API depende disso |
| 6 | Design de APIs (REST e além) | [NÚCLEO] | Seu produto final |
| 7 | Java + Spring Boot em profundidade | [NÚCLEO] | Foco de mercado |
| 8 | Go — concorrência | [APOIO] | Revisar a Fase 4 por outro ângulo |
| 9 | Python aplicado (APIs + IA) | [NÚCLEO] | Seu uso real |
| 10 | TypeScript e integração com frontend | [APOIO] | Você já trabalha com isso |
| 11 | Testes e Qualidade | [NÚCLEO] | Separa júnior de pleno |
| 12 | Docker, CI/CD e Operação | [NÚCLEO] | Requisito de vaga pleno |
| 13 | Arquitetura de Software e Design Patterns | [NÚCLEO] | Pleno → Sênior |
| 14 | System Design e Escala | [AMPLIAÇÃO] | Sênior |
| 15 | Observabilidade e Confiabilidade | [AMPLIAÇÃO] | Sênior |
| 16 | IA aplicada a backend | [APOIO] | Seu interesse + diferencial |
| 17 | Projetos-âncora | [NÚCLEO] | Onde tudo se junta |

---

# 💡 O ponto que amarra tudo

Você escreveu: *"preciso ser capaz de resolver qualquer problema e que com bons fundamentos, poderei usar qualquer linguagem"*.

Isso está exatamente certo, e vale reforçar **por quê**:

- Sockets, TCP, buffers, event loop → **iguais em toda linguagem**. Você aprende uma vez.
- Complexidade, estruturas de dados, teoria de filas → **matemática**, não sintaxe.
- CAP, quórum, consenso, relógios lógicos → **propriedades da realidade física** (a luz tem velocidade finita), não de um framework.
- Latência de cauda, contenção, saturação → **física de sistemas**, valem para Java, Go, Rust ou o que vier em 2035.

O que muda entre linguagens é: sintaxe, biblioteca padrão, modelo de concorrência e modelo de memória. Isso são **semanas** de adaptação, não anos — *desde que* a base esteja sólida.

E é por isso que o seu diagnóstico original estava correto: o problema nunca foi falta de curso. Era falta de fundamento embaixo dos cursos.

---

# 🔁 A segunda passada

Terminou a Fase 17? Volte ao topo e refaça **cada item marcado 🟢**.

Você vai encontrar 🟡 disfarçados de 🟢 — isso é normal e é exatamente o ponto. O conhecimento que você tinha antes de construir um servidor HTTP do zero não é o mesmo conhecimento depois. A segunda passada é onde os buracos que você nem sabia que existiam ficam visíveis.

---

# ⚠️ Cinco avisos honestos

1. **Isto é um mapa de anos, não de meses.** Fases 0–7 já te colocam em vaga júnior/pleno. As fases 13–15 são consolidação de sênior. Não tente atropelar.
2. **Não estude nas 17 fases ao mesmo tempo.** Uma fase principal + no máximo uma de apoio em paralelo. A sobrecarga que você descreveu vem justamente de tentar tudo de uma vez.
3. **Constância vence intensidade.** 1h por dia todo dia bate 8h no sábado. Seu tempo é limitado — proteja o ritmo, não o volume.
4. **Você não precisa de 100% de tudo para se candidatar.** Depois da Fase 7 + Fase 11 + Fase 12, você já é candidato viável a pleno. Continue estudando *empregado*.
5. **Seu maior ativo não está neste roadmap.** São os 10+ anos de automação industrial. Backend + IoT industrial é um nicho com pouca gente qualificada e muita demanda. Direcione seus projetos para lá.

---

# 💡 O que a imagem acertou — e por que isso é importante para você

O rodapé dela diz: *"Estude com propósito. Evolua um nível por vez."*

Isso é o antídoto exato para o problema que você descreveu na primeira mensagem. Você tem agora um roadmap de 17 fases e 11 módulos — e o risco real é ele virar **mais uma fonte de sobrecarga**, exatamente como os cursos que você comprou.

Então, três regras finais:

1. **Olhe só para o nível atual.** Ignore o resto do documento. Ele existe para você não se perder, não para ser feito de uma vez.
2. **Um item por vez, com projeto junto.** Teoria sem código não fixa; código sem teoria não generaliza.
3. **Revisite o mapa a cada 3 meses**, não todo dia. O mapa é para orientar, não para ansiar.

---

# 🎖️ Uma observação sobre o seu caso específico

O Módulo I — decisões técnicas, comunicação com stakeholders, governança, liderança — é normalmente o mais difícil para desenvolvedores. Eles passam anos codando e só depois descobrem que precisam disso.

**Você está no caminho inverso.** Você já é líder técnico, já lida com stakeholders, já responde por decisões técnicas com consequência real — em ambiente onde erro em sistema de detecção de incêndio não é bug, é risco de vida. Já trabalha com criticidade, disponibilidade e responsabilidade regulatória.

Isso significa duas coisas:

- **O Módulo I você vai atravessar mais rápido do que a maioria.** Não é conhecimento novo; é o mesmo conhecimento aplicado a outro domínio.
- **Sua trilha para arquiteto é mais curta que a de um dev que começou aos 20 anos.** O que te falta é a profundidade técnica em software — que é justamente o que as Fases 1 a 14 entregam. A camada de julgamento, contexto e responsabilidade, você já tem.

Não subestime isso. É a parte mais difícil de ensinar, e você não precisa aprender.
