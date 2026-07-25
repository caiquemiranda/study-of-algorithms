# 08 — Tries (Árvores de Prefixo)

> Uma árvore onde cada caminho da raiz soletra um prefixo. Problemas em [`../problemas/08_tries/`](../problemas/08_tries/).

## Conceito

Cada nó tem um mapa `char → filho` e uma flag `fim_de_palavra`. Inserir/buscar a palavra de tamanho m custa **O(m)** — independente de quantas palavras existem na estrutura. É a resposta certa quando o problema gira em torno de **prefixos compartilhados**: autocompletar, dicionários, busca de múltiplas palavras ao mesmo tempo.

**Radix Tree (Patricia Trie)**: trie comprimida — nós com filho único são fundidos, guardando fatias de string na aresta. Menos memória, mesmos O(m). **É a estrutura do roteador de URLs de frameworks modernos** (FastAPI/Starlette, Gin, Echo): cada `/` desce um nível, `/users/{id}` vira um nó-parâmetro (pilar 4.8).

## Como reconhecer no enunciado

- "prefixo", "começa com", "autocompletar", "dicionário de palavras"
- Buscar **muitas** palavras num texto/grade ao mesmo tempo (Word Search II) — a trie evita recomeçar do zero para cada palavra
- Curinga `.` casando com qualquer letra → DFS na trie

## Templates

```python
# Trie com dict — insert / search / startsWith em O(m)
class Trie:
    def __init__(self):
        self.filhos = {}
        self.fim = False

    def insert(self, palavra):
        no = self
        for ch in palavra:
            no = no.filhos.setdefault(ch, Trie())
        no.fim = True

    def search(self, palavra):
        no = self._desce(palavra)
        return no is not None and no.fim

    def startsWith(self, prefixo):
        return self._desce(prefixo) is not None

    def _desce(self, s):
        no = self
        for ch in s:
            no = no.filhos.get(ch)
            if no is None:
                return None
        return no

# Busca com curinga '.' — DFS
def search_wildcard(no, palavra, i=0):
    if i == len(palavra):
        return no.fim
    ch = palavra[i]
    if ch == ".":
        return any(search_wildcard(f, palavra, i + 1) for f in no.filhos.values())
    prox = no.filhos.get(ch)
    return prox is not None and search_wildcard(prox, palavra, i + 1)
```

**Word Search II (esqueleto):** insira todas as palavras na trie; faça DFS na grade **descendo na trie junto** — pode caminhar na grade apenas se o caractere existe como filho. Ao achar `fim`, registre e desligue a flag (evita duplicata). Poda: remova nós-folha esgotados.

## Complexidade típica

Insert/search: O(m). Espaço: O(total de caracteres × tamanho do alfabeto) — a trie troca memória por velocidade de prefixo. Hash set responde "palavra exata existe?" no mesmo O(m), mas **não** responde "algo começa com este prefixo?" — essa é a diferença que justifica a trie.

## Erros comuns

- Esquecer a flag `fim` (confundir "é palavra completa" com "é prefixo de alguma")
- Em Word Search II, buscar cada palavra separadamente com DFS (TLE) — a trie compartilha o trabalho dos prefixos
- Não desmarcar a célula visitada no backtracking da grade
- Usar array de 26 posições quando o alfabeto é maior (unicode) — prefira dict

## Problemas recomendados

| Problema | Dificuldade |
|---|---|
| 208. Implement Trie | 🟡 medium |
| 211. Design Add and Search Words (curinga) | 🟡 medium |
| 212. Word Search II | 🔴 hard |

## Conexão com backend

**Implemente um roteador de URLs com Radix Tree** — é o exercício-ponte da Fase 4.8, e o que mais eleva estrutura de dados aplicada. Tries também sustentam autocompletar de buscadores, tabelas de roteamento IP (longest prefix match em roteadores de rede) e dicionários de compressão.
