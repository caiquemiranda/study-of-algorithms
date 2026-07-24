# 🐳 Docker, CI/CD, Mensageria e Cloud (noção)

> Fase 12 (Vol. 1).

---

# FASE 12 — Docker, CI/CD e Operação [NÚCLEO]

## 12.1 Containers
- [ ] O que é um container por baixo: **namespaces + cgroups** (não é VM!)
- [ ] Imagem vs container vs layer
- [ ] **Dockerfile**: `FROM`, `RUN`, `COPY`, `WORKDIR`, `ENV`, `EXPOSE`, `CMD` vs `ENTRYPOINT`
- [ ] **Multi-stage build** — imagem final pequena (essencial em Java)
- [ ] Cache de layers e ordem das instruções
- [ ] Volumes (persistência) e bind mounts
- [ ] Redes Docker: bridge, host, custom network
- [ ] **Docker Compose** — subir API + Postgres + Redis + Kafka localmente com um comando
- [ ] Boas práticas: usuário não-root, imagem base slim/alpine/distroless, `.dockerignore`, health check
- [ ] Registry: Docker Hub, ECR, GHCR
- [ ] **Kubernetes** (noção): Pod, Deployment, Service, Ingress, ConfigMap, Secret, HPA

## 12.2 CI/CD
- [ ] Integração Contínua: build + testes + análise estática a cada push
- [ ] **GitHub Actions** — workflow, jobs, steps, matrix, secrets, cache
- [ ] Pipeline típico: lint → test → build → scan de segurança → build da imagem → push → deploy
- [ ] Ambientes: dev → staging → produção
- [ ] Estratégias de deploy: **rolling, blue-green, canary**, feature flags
- [ ] Rollback e versionamento de artefato
- [ ] Segredos no pipeline (nunca em texto puro no repositório)

## 12.3 Mensageria
- [ ] Por que filas existem: desacoplamento, absorção de pico, resiliência
- [ ] **RabbitMQ**: exchange (direct, topic, fanout, headers), queue, binding, ack/nack, DLQ (Dead Letter Queue), prefetch
- [ ] **Kafka**: tópico, **partição**, offset, consumer group, replicação, retenção, compactação
- [ ] Quando RabbitMQ e quando Kafka (fila de tarefas vs log de eventos)
- [ ] Garantias de entrega: at-most-once, at-least-once, exactly-once (e por que "exactly-once" é mais complicado do que parece)
- [ ] **Idempotência no consumidor** — obrigatório quando a entrega é at-least-once
- [ ] Ordenação de mensagens e a relação com partições
- [ ] **Outbox Pattern** — como publicar evento e gravar no banco atomicamente
- [ ] Saga Pattern — transação distribuída (coreografia vs orquestração)

## 12.4 Cloud (noção suficiente)
- [ ] Modelos: IaaS, PaaS, SaaS, Serverless
- [ ] Serviços básicos (AWS como referência): EC2, S3, RDS, SQS/SNS, Lambda, ECS/EKS, CloudWatch, IAM
- [ ] Twelve-Factor App — os 12 princípios (config no ambiente, logs como stream, processos stateless, etc.)

**📚 Livros:**
- *Docker Deep Dive* — Nigel Poulton
- *The Phoenix Project* e *The DevOps Handbook* — Gene Kim et al. (cultura e por que DevOps existe)
- *Continuous Delivery* — Jez Humble & David Farley
- *Kafka: The Definitive Guide* — Narkhede, Shapira & Palino (**gratuito** pela Confluent)
- *Enterprise Integration Patterns* — Hohpe & Woolf (o catálogo clássico de mensageria)
