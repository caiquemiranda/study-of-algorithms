# ☁️ Cloud a Sério

> Módulo H.3 (Vol. 3): IAM, VPC, Terraform, 6 R's de migração.

---

## H.3 Cloud a sério (não só "noção")
- [ ] Modelos: IaaS · PaaS · CaaS · FaaS · SaaS — e o que você deixa de controlar em cada um
- [ ] Regiões, **zonas de disponibilidade**, edge locations
- [ ] **IAM** — o serviço mais importante e o mais mal usado: princípio do menor privilégio, roles vs users, policies, credenciais temporárias
- [ ] Computação: VM (EC2), container gerenciado (ECS/Fargate, Cloud Run), Kubernetes gerenciado (EKS/AKS/GKE), serverless (Lambda)
- [ ] Armazenamento: object storage (**S3**), block storage (EBS), file storage (EFS); classes de armazenamento e ciclo de vida
- [ ] Banco gerenciado: RDS/Aurora, DynamoDB, ElastiCache
- [ ] Rede: **VPC**, subnet pública/privada, security group, NAT gateway, load balancer (ALB/NLB), API Gateway
- [ ] Mensageria gerenciada: SQS, SNS, EventBridge, MSK (Kafka gerenciado)
- [ ] Observabilidade: CloudWatch, X-Ray
- [ ] Segredos: Secrets Manager, Parameter Store, KMS
- [ ] **Infraestrutura como Código**: **Terraform** (multi-cloud, o padrão de mercado), CloudFormation, Pulumi, CDK
- [ ] **Cold start** em serverless e por que isso destrói p99
- [ ] **Migração para cloud — os 6 R's**: Rehost (lift-and-shift), Replatform, Repurchase, **Refactor**, Retire, Retain
- [ ] Estratégia de migração incremental (**Strangler Fig** na prática) e o risco do big bang
- [ ] Vendor lock-in — quando aceitar conscientemente e quando evitar
- [ ] Certificação (opcional mas ajuda no filtro de RH): **AWS Solutions Architect Associate** é a de melhor custo-benefício
