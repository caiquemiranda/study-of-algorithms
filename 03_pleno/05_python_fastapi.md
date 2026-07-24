# 🐍 Python Aplicado — FastAPI e asyncio

> Fase 9 (Vol. 1).

---

# FASE 9 — Python Aplicado [NÚCLEO]

## 9.1 Python além do básico
- [ ] Modelo de dados: tudo é objeto, `__dunder__` methods
- [ ] Mutabilidade e a armadilha do argumento default mutável
- [ ] List/dict/set comprehensions
- [ ] **Generators** e `yield` — lazy evaluation e economia de memória
- [ ] **Decorators** — e como isso é o mecanismo do `@app.get` do FastAPI
- [ ] **Context managers** e `with` (`__enter__`/`__exit__`)
- [ ] Type hints e `typing` (`Optional`, `Union`, `Generic`, `Protocol`); `mypy`
- [ ] **GIL (Global Interpreter Lock)** — por que threading em Python não paraleliza CPU, e o que fazer (multiprocessing)
- [ ] `asyncio`: event loop, coroutines, `async`/`await`, `gather`, `TaskGroup` (retoma a Fase 4.13)
- [ ] Ambientes: `venv`, `poetry`/`uv`, `requirements.txt` vs `pyproject.toml`
- [ ] Testes: `pytest`, fixtures, parametrize, mocks

## 9.2 FastAPI
- [ ] Rotas, path/query params, request body
- [ ] **Pydantic** — validação e serialização por tipo; v1 vs v2
- [ ] Sistema de **Dependency Injection** (`Depends`)
- [ ] Middlewares e exception handlers
- [ ] Docs automáticas (OpenAPI gerado do código)
- [ ] Autenticação OAuth2/JWT
- [ ] Background tasks
- [ ] Rodar com **Uvicorn** (ASGI — retoma a Fase 4.4)
- [ ] SQLAlchemy 2.0 (ORM) + Alembic (migrations)

**📚 Livros:**
- *Fluent Python* — **Luciano Ramalho** (brasileiro; é *o* livro de Python intermediário/avançado. Tem em PT-BR: "Python Fluente")
- *Effective Python* — Brett Slatkin
- *Architecture Patterns with Python* — Percival & Gregory (**gratuito** em cosmicpython.com) — DDD, repositório, unit of work em Python
- *Python Testing with pytest* — Brian Okken
