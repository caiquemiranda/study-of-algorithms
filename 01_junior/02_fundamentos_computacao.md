# 💻 Computação, Memória, SO e Redes

> Fase 1 do roadmap (Vol. 1). Aprofundamento de redes no Sênior (`04_senior/06`).

---

# FASE 1 — Computação, Memória, SO e Redes [NÚCLEO]

## 1.1 Como o computador executa um programa
- [ ] Sistemas numéricos: binário, hexadecimal, conversões
- [ ] Representação de dados: inteiros com sinal (complemento de dois), ponto flutuante IEEE 754 (**e por que `0.1 + 0.2 != 0.3`**)
- [ ] Codificação de texto: ASCII, UTF-8, Unicode (e por que acento quebra em API mal configurada)
- [ ] CPU: registradores, ULA, ciclo *fetch-decode-execute*
- [ ] Hierarquia de memória: registrador → cache L1/L2/L3 → RAM → SSD/HD → rede (e a diferença de latência entre eles, em ordens de grandeza)
- [ ] Localidade de referência (temporal e espacial) — por que percorrer um array é mais rápido que uma linked list
- [ ] Compilado vs interpretado vs máquina virtual: o que acontece com um `.c`, um `.java` e um `.py` até virar instrução na CPU

## 1.2 Memória em nível de processo
- [ ] Layout de memória de um processo: text, data, BSS, heap, stack
- [ ] **Stack**: frames de função, variáveis locais, por que é rápida, por que é limitada (*stack overflow*)
- [ ] **Heap**: alocação dinâmica, fragmentação, por que precisa ser gerenciada
- [ ] Ponteiros, endereços e referências (conceito)
- [ ] Memory leak: o que é e por que só aparece em processo de longa duração
- [ ] Garbage Collection: contagem de referência vs mark-and-sweep vs generational (visão geral — aprofunda na Fase 7 com a JVM)
- [ ] Memória virtual, paginação e *swap*

## 1.3 Sistema Operacional
- [ ] Processo vs Thread: o que o SO enxerga, custo de criação de cada um
- [ ] *Context switching* — por que ter 10.000 threads é ruim
- [ ] Escalonamento de processos (visão geral: preemptivo, quantum)
- [ ] File Descriptor e a filosofia Unix "tudo é arquivo" — **por que um socket de rede é tratado como arquivo**
- [ ] Syscalls: a fronteira user space / kernel space
- [ ] Sinais POSIX: `SIGINT`, `SIGTERM`, `SIGKILL` — como desligar um servidor sem corromper dados
- [ ] `fork` e `exec` — criação de processos
- [ ] IPC (comunicação entre processos): pipes, sockets, memória compartilhada
- [ ] Concorrência: *race condition*, seção crítica, mutex, semáforo, *deadlock* (as 4 condições de Coffman)

## 1.4 Redes
- [ ] Modelo em camadas: TCP/IP (4 camadas) e sua relação com o OSI (7 camadas)
- [ ] Endereçamento IP, máscara de sub-rede, CIDR, IP público vs privado, NAT
- [ ] Portas e o conceito de socket (IP + porta)
- [ ] **TCP**: orientado a conexão, confiável, ordenado
  - [ ] *3-way handshake* (`SYN` → `SYN-ACK` → `ACK`)
  - [ ] Encerramento (`FIN`/`ACK`) e o estado `TIME_WAIT`
  - [ ] Controle de fluxo (janela deslizante) e controle de congestionamento
  - [ ] **TCP é um fluxo contínuo de bytes** — não existe "pacote = mensagem". Por isso você lê em buffers.
- [ ] **UDP**: sem conexão, sem garantia — quando isso é *melhor* (streaming, DNS, jogos)
- [ ] `127.0.0.1` (loopback) vs `0.0.0.0` (todas as interfaces) — decide quem consegue acessar sua aplicação
- [ ] DNS: hierarquia (root → TLD → autoritativo), tipos de registro (A, AAAA, CNAME, MX, TXT), TTL e cache
- [ ] Como funciona a internet, ponta a ponta: o que acontece entre digitar a URL e a página aparecer
- [ ] Firewall e regras básicas de porta

**✅ Checkpoint da Fase 1:** você narra, do teclado ao pixel, todo o caminho de uma requisição — sem dizer "framework" nenhuma vez — e sabe apontar em qual camada cada coisa acontece.

**📚 Livros:**
- *Computer Networking: A Top-Down Approach* — **Kurose & Ross** (redes; a referência de graduação, tem edição em PT-BR: "Redes de Computadores e a Internet")
- *Operating Systems: Three Easy Pieces* — Remzi & Andrea Arpaci-Dusseau (**gratuito** em pages.cs.wisc.edu/~remzi/OSTEP/) — o melhor livro de SO disponível hoje, e é grátis
- *Sistemas Operacionais Modernos* — Andrew Tanenbaum (alternativa clássica, em PT-BR)
- *Code: The Hidden Language of Computer Hardware and Software* — Charles Petzold (para o "como o computador funciona" do zero absoluto; leitura leve e excelente)
- *Computer Systems: A Programmer's Perspective* (CS:APP) — Bryant & O'Hallaron (a ponte definitiva entre hardware e código; denso, mas transformador)
- *TCP/IP Illustrated, Vol. 1* — W. Richard Stevens (consulta, quando quiser o detalhe do protocolo)
