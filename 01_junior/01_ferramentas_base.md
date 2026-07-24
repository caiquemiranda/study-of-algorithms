# 🧰 Ferramentas Base — Linux, Terminal e Git

> Fase 0 do roadmap (Vol. 1).

---

# FASE 0 — Ferramentas Base [NÚCLEO]

> Não estava na v1 do roadmap e é um buraco clássico. Ninguém ensina, todo mundo cobra.

## 0.1 Linux e terminal
- [ ] Estrutura de diretórios do Linux (`/etc`, `/var`, `/usr`, `/home`, `/proc`)
- [ ] Navegação e manipulação: `cd`, `ls`, `cp`, `mv`, `rm`, `find`
- [ ] Permissões: `chmod`, `chown`, o que significa `755` e `644` (e por que isso derruba deploy)
- [ ] Pipes e redirecionamento: `|`, `>`, `>>`, `2>&1`
- [ ] Ferramentas de texto: `grep`, `sed`, `awk`, `cat`, `less`, `tail -f`
- [ ] Processos: `ps`, `top`/`htop`, `kill`, `&`, `nohup`
- [ ] Rede pelo terminal: `curl`, `netstat`/`ss`, `ping`, `dig`, `telnet`, `nc` (netcat)
- [ ] Variáveis de ambiente e `PATH`
- [ ] Shell script básico (variáveis, `if`, loop, argumentos)
- [ ] SSH: chaves pública/privada, `ssh-keygen`, acesso a servidor remoto

## 0.2 Git e GitHub
- [ ] Modelo mental do Git: working directory → staging → commit → remote
- [ ] `init`, `clone`, `add`, `commit`, `push`, `pull`, `fetch`
- [ ] Branches: criar, trocar, `merge` vs `rebase` (e quando cada um)
- [ ] Resolver conflitos de merge na mão
- [ ] `log`, `diff`, `blame`, `stash`
- [ ] Desfazer coisas: `reset` (soft/mixed/hard), `revert`, `checkout` de arquivo
- [ ] `.gitignore` e o que **nunca** commitar (segredos, `.env`, `node_modules`, `target/`)
- [ ] Pull Request / Code Review: como abrir, como revisar
- [ ] Estratégias de branching: Git Flow, GitHub Flow, Trunk-Based
- [ ] Conventional Commits (padrão de mensagem)
- [ ] Tags e versionamento semântico (SemVer: MAJOR.MINOR.PATCH)

**✅ Checkpoint:** você resolve um conflito de merge sem pânico e sabe recuperar um commit "perdido" com `reflog`.

**📚 Livros:**
- *Pro Git* — Scott Chacon & Ben Straub (**gratuito** em git-scm.com/book/pt-br) — a referência oficial
- *The Linux Command Line* — William Shotts (**gratuito** em linuxcommand.org)
