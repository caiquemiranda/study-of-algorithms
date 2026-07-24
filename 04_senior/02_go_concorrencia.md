# 🐹 Go — Concorrência

> Fase 8 (Vol. 1). Goroutines, channels, context.

---

# FASE 8 — Go [APOIO]

- [ ] Sintaxe, tipagem estática, `struct`, métodos, **interfaces implícitas** (duck typing em tempo de compilação)
- [ ] Tratamento de erro como valor (`if err != nil`) — a filosofia oposta a exceptions
- [ ] Ponteiros em Go (existem, mas sem aritmética)
- [ ] Slices, maps e o modelo de memória por trás deles
- [ ] **Goroutines** — por que são baratas (crescem sob demanda, escalonadas em user space)
- [ ] **Channels** — buffered vs unbuffered, `select`, fechamento de canal
- [ ] "Don't communicate by sharing memory; share memory by communicating"
- [ ] `sync` package: `WaitGroup`, `Mutex`, `Once`
- [ ] `context.Context` — cancelamento e timeout propagados
- [ ] `net/http` da stdlib — servidor e cliente
- [ ] Testes nativos (`testing`, table-driven tests)
- [ ] Módulos (`go mod`) e compilação para binário único
- [ ] **Projeto:** recriar o servidor HTTP da Fase 4 em Go puro e comparar o modelo de concorrência com o event loop que você escreveu em Python

**📚 Livros:**
- *The Go Programming Language* — Donovan & Kernighan (a referência)
- *Learning Go* — Jon Bodner (mais moderno e didático)
- *Concurrency in Go* — Katherine Cox-Buday (excelente, focado no que Go tem de melhor)
