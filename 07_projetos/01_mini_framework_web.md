# 🏗️ Projeto 1 — Mini-Framework Web (do zero, sem dependências)

**Nível:** Pleno · **Fase de origem:** 4 (os 16 pilares)

## Objetivo
Servidor HTTP em Python puro (biblioteca padrão, zero dependências), depois replicado em Go. É o projeto que transforma Spring/FastAPI de "magia" em "eu sei o que isso faz".

## Escopo (do projeto central da Fase 4 — detalhes em [`03_pleno/01`](../03_pleno/01_web_sem_frameworks_16_pilares.md))
- [ ] Servidor HTTP do zero: sockets → parsing → resposta, com roteador em **Radix Tree**
- [ ] Suporte a **thread pool** e depois **event loop** — medir a diferença sob carga
- [ ] Autenticação com sessão via cookie **e** via JWT (as duas, para comparar)
- [ ] Upload multipart salvando em chunks no disco
- [ ] Servir estáticos com `ETag` e `304`
- [ ] Proxy reverso simples na frente de tudo
- [ ] (Fase 8) Replicar em Go puro e comparar goroutines vs event loop

## Referência
Repositório `codecrafters-io/build-your-own-x` — seções *Build your own Web Server* e *Build your own Database*.

## Status
🔴 Não iniciado
