# ⚙️ C++ e Baixa Abstração

> Fase 3 (Vol. 1). Usar C++ como lente de aumento sobre o que Java/Python escondem.

---

# FASE 3 — C++ e Baixa Abstração [APOIO]

> Objetivo: usar C++ como lente de aumento. Não é virar especialista em C++ enterprise.

- [ ] Pipeline de compilação: pré-processador → compilador → assembler → **linker** → executável
- [ ] Header (`.h`) vs implementação (`.cpp`), *include guards*
- [ ] Tipos primitivos e tamanho real em bytes (`sizeof`)
- [ ] **Ponteiros na prática**: aritmética de ponteiro, ponteiro para ponteiro, ponteiro nulo
- [ ] Referências vs ponteiros
- [ ] Alocação: stack (`int x;`) vs heap (`new` / `malloc`) — e a obrigação de `delete` / `free`
- [ ] **Dangling pointer**, double free, buffer overflow — os bugs que Java/Python te impedem de cometer
- [ ] RAII (Resource Acquisition Is Initialization) — o padrão que define C++ moderno
- [ ] Smart pointers: `unique_ptr`, `shared_ptr`, `weak_ptr`
- [ ] Classes: construtor, destrutor, cópia, *move semantics*
- [ ] Layout de objeto na memória, `vtable` e polimorfismo (como herança funciona por baixo)
- [ ] STL: `vector`, `map`, `unordered_map`, `set` — e comparar com o que você implementou na Fase 2
- [ ] Templates (noção de generics em tempo de compilação)
- [ ] **Projeto:** reimplementar Linked List + Hash Table em C++ com gerenciamento manual de memória, e rodar um detector de leak (`valgrind`)

**✅ Checkpoint da Fase 3:** você explica, com exemplo de código, por que Java "não precisa" de `free()` e qual o preço disso (pausas de GC, uso de memória maior).

**📚 Livros:**
- *C++ Primer* — Lippman, Lajoie & Moo (o melhor livro para aprender C++ de verdade)
- *A Tour of C++* — Bjarne Stroustrup (rápido, do criador da linguagem)
- *Effective Modern C++* — Scott Meyers (depois que já souber o básico)
- *The C Programming Language* (K&R) — Kernighan & Ritchie (se quiser passar por C puro antes; é curto e histórico)
