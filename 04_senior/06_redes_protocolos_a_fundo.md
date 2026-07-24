# 🌐 Redes e Protocolos a Fundo

> Módulo A (Vol. 2): TCP internals, HTTP/2/3, TLS, MQTT/OPC-UA/Modbus (seu diferencial), WebRTC.

---

# MÓDULO A — Redes e Protocolos: cobertura total
*(entra nas Fases 1.4 e 4 — estude junto com elas)*

## A.1 TCP a fundo — além do handshake
- [ ] Estados da conexão TCP (máquina de estados): `LISTEN`, `SYN_SENT`, `ESTABLISHED`, `FIN_WAIT`, **`TIME_WAIT`** — e por que `TIME_WAIT` acumulado esgota portas em servidor de alto tráfego
- [ ] **Janela deslizante** e controle de fluxo (`rwnd`)
- [ ] **Controle de congestionamento**: slow start, congestion avoidance, fast retransmit/recovery
- [ ] Algoritmos: Reno, CUBIC (padrão do Linux), **BBR** (Google — muda o jogo em rede com perda)
- [ ] **Algoritmo de Nagle** e `TCP_NODELAY` — por que ele adiciona ~40ms de latência em requisições pequenas (bug clássico de p99)
- [ ] **Delayed ACK** e a interação tóxica com Nagle
- [ ] MTU, MSS, fragmentação, Path MTU Discovery
- [ ] **Head-of-line blocking** no TCP — e por que isso motivou o QUIC
- [ ] `SO_REUSEPORT` — múltiplos processos aceitando na mesma porta (escala de accept)
- [ ] Backlog de conexão (`somaxconn`) — a fila invisível que derruba servidores sob pico
- [ ] Keep-alive TCP vs keep-alive HTTP (são coisas diferentes)
- [ ] Tuning de kernel: buffers (`net.core.rmem_max`), `tcp_tw_reuse`, limite de file descriptors (`ulimit -n`)

## A.2 Evolução do HTTP
- [ ] **HTTP/1.0** → **HTTP/1.1**: keep-alive, pipelining (e por que pipelining fracassou)
- [ ] Limite de 6 conexões por domínio e os hacks da época (domain sharding, sprites)
- [ ] **HTTP/2**: binário, **multiplexação de streams**, HPACK (compressão de header), priorização, server push (depreciado)
- [ ] O head-of-line blocking que o HTTP/2 **não** resolveu (porque está no TCP)
- [ ] **HTTP/3 + QUIC**: sobre UDP, streams independentes, handshake em 1-RTT (ou **0-RTT**), migração de conexão (troca de Wi-Fi para 4G sem cair)
- [ ] Compressão de corpo: gzip, deflate, **brotli**, zstd

## A.3 TLS a fundo
- [ ] TLS 1.2 vs **TLS 1.3** (handshake de 1-RTT, 0-RTT resumption e o risco de replay attack)
- [ ] Cipher suites, perfect forward secrecy, ECDHE
- [ ] Certificados X.509, cadeia de confiança, certificado intermediário, SNI
- [ ] Revogação: CRL, OCSP, **OCSP stapling**
- [ ] **mTLS** — autenticação mútua (padrão em service mesh)
- [ ] Custo de CPU do handshake TLS — e por que **terminação TLS no load balancer** + session resumption importam para p99
- [ ] HSTS, certificate pinning

## A.4 A camada abaixo (o que quase ninguém sabe)
- [ ] Ethernet, MAC, **ARP**
- [ ] IPv4 vs IPv6, roteamento, tabela de rotas, TTL/hop limit
- [ ] **ICMP** (por trás do `ping` e do `traceroute`)
- [ ] **DHCP**, **NTP** (sincronização de relógio — e por que isso é crítico em sistema distribuído)
- [ ] **BGP** e **Anycast** — como CDN e DNS global funcionam de verdade
- [ ] NAT, port forwarding, e por que P2P precisa de STUN/TURN
- [ ] Ferramentas de diagnóstico: `tcpdump`, **Wireshark**, `traceroute`, `mtr`, `ss`, `iftop`
- [ ] Noção de kernel bypass: `io_uring`, **eBPF**, DPDK (só para saber que existe e quando entra)

## A.5 Protocolos de aplicação além do HTTP
> **Esta seção é o seu diferencial de mercado.** Ninguém que vem de "curso de backend" conhece a metade disso — e você já vive nesse mundo.

**Mensageria e IoT**
- [ ] **MQTT** — pub/sub leve, QoS 0/1/2, retained message, last will & testament, broker (Mosquitto, EMQX). **É o protocolo padrão de IoT e automação predial**
- [ ] **CoAP** — REST sobre UDP para dispositivos restritos
- [ ] **AMQP** — o protocolo por trás do RabbitMQ
- [ ] Protocolo binário do **Kafka**

**Industrial (seu domínio — leve para o currículo)**
- [ ] **Modbus TCP/RTU** — o mais difundido em automação
- [ ] **BACnet/IP** — automação predial (HVAC, iluminação, incêndio)
- [ ] **OPC-UA** — o padrão de Indústria 4.0, com modelo de informação e segurança embutida
- [ ] Conceito de gateway de protocolo (traduzir Modbus/BACnet → MQTT → API REST) — **este é literalmente o produto que você pode construir**

**Outros**
- [ ] SMTP, IMAP, POP3 (e-mail)
- [ ] FTP, SFTP, SCP, rsync
- [ ] LDAP / Active Directory (autenticação corporativa)
- [ ] SNMP (monitoramento de equipamento de rede)
- [ ] SSH (túnel, port forwarding, jump host)

## A.6 WebRTC — o que faltava
- [ ] Modelo P2P: por que não passa por servidor (e quando precisa passar)
- [ ] **Sinalização (signaling)** — o WebRTC **não** define isso; você implementa com WebSocket
- [ ] **SDP (Session Description Protocol)** — negociação de codec e capacidades
- [ ] **ICE** (Interactive Connectivity Establishment): candidatos, e como atravessar NAT
- [ ] **STUN** — descobrir o próprio IP público
- [ ] **TURN** — relay quando o P2P direto falha (e por que ele custa caro em banda)
- [ ] **DTLS** (segurança sobre UDP) e **SRTP** (mídia segura)
- [ ] Data Channels — trocar dados arbitrários P2P, não só áudio/vídeo
- [ ] Arquiteturas de conferência: Mesh vs **SFU** (Selective Forwarding Unit) vs MCU
- [ ] Quando usar WebRTC vs WebSocket vs SSE

## A.7 Tabela de decisão: qual protocolo usar

| Necessidade | Escolha | Por quê |
|---|---|---|
| CRUD entre sistemas heterogêneos | REST/JSON | Universal, cacheável, simples |
| Comunicação interna entre microsserviços | **gRPC** | Binário, HTTP/2, contrato forte, streaming |
| Cliente precisa de dados sob medida | GraphQL | Evita over/under-fetching |
| Integração corporativa/bancária legada | SOAP | Contrato WSDL, WS-Security |
| Notificar outro sistema de um evento | Webhook | Assíncrono, sem polling |
| Servidor → cliente, unidirecional (ex: streaming de LLM) | **SSE** | Simples, sobre HTTP, reconecta sozinho |
| Bidirecional em tempo real (chat, colaboração) | **WebSocket** | Full-duplex persistente |
| Áudio/vídeo P2P, latência mínima | **WebRTC** | Sem servidor no meio da mídia |
| Dispositivo IoT com pouca banda/energia | **MQTT** | Leve, pub/sub, QoS |
| Desacoplar produtores e consumidores | Kafka/RabbitMQ | Buffer, retry, replay |
| Máxima vazão, perda tolerável | UDP puro | Sem overhead de confiabilidade |

**📚 Referências do Módulo A:**
- *TCP/IP Illustrated, Vol. 1* — W. Richard Stevens
- *High Performance Browser Networking* — Ilya Grigorik (**grátis**, hpbn.co) — cobre HTTP/2, TLS, WebRTC e WebSocket com profundidade rara
- *Bulletproof SSL and TLS* — Ivan Ristić
- *Systems Performance* — Brendan Gregg (capítulos de rede)
