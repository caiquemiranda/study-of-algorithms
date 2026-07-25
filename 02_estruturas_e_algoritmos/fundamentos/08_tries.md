# 08 — Tries (Árvores de Prefixo)

> Cada caminho da raiz soletra um prefixo. Soluções em [`../problemas/08_tries/`](../problemas/08_tries/).

## 1. Conceito Central e Analogia Didática

- Cada nó guarda um mapa `char → filho` + flag `fimDePalavra`; inserir/buscar palavra de tamanho m custa **O(m)**, independente de quantas palavras a trie contém.
- Palavras com prefixo comum **compartilham o caminho** — é o que torna "começa com...?" trivial (hash set não responde isso).
- **Radix Tree** = trie comprimida (nós de filho único fundidos): é o roteador de URLs de FastAPI/Gin (pilar 4.8).

**Analogia:** lista telefônica em árvore de decisões: para achar "CAIQUE", siga a gaveta C → A → I... Todos os "CA..." dividem as duas primeiras gavetas — por isso autocompletar é só "desça até o prefixo e liste o que há abaixo".

## 2. Como Reconhecer (Padrões de Enunciado)

- Se aparece "**prefixo**", "**começa com**", "autocompletar", "dicionário" → trie.
- Se busca **muitas palavras ao mesmo tempo** num texto/grade (Word Search II) → trie compartilha o trabalho dos prefixos.
- Se há curinga `.` casando qualquer letra → DFS descendo a trie.
- Se pede "maior XOR de par" → trie **binária** de bits (variação avançada).

## 3. Templates de Código

### Trie completa (insert / search / startsWith)

```java
// Java — array de 26 filhos: mais rápido que HashMap quando o alfabeto é fixo a-z
class Trie {
    private final Trie[] filhos = new Trie[26];
    private boolean fim = false;              // distingue palavra completa de mero prefixo

    public void insert(String palavra) {
        Trie no = this;
        for (char c : palavra.toCharArray()) {
            int i = c - 'a';                  // mapeia o char para o slot do array
            if (no.filhos[i] == null) no.filhos[i] = new Trie(); // cria o caminho sob demanda
            no = no.filhos[i];
        }
        no.fim = true;                        // marca APENAS o último nó
    }

    public boolean search(String palavra) {
        Trie no = desce(palavra);
        return no != null && no.fim;          // precisa existir E ser fim de palavra
    }

    public boolean startsWith(String prefixo) {
        return desce(prefixo) != null;        // para prefixo, basta o caminho existir
    }

    private Trie desce(String s) {
        Trie no = this;
        for (char c : s.toCharArray()) {
            no = no.filhos[c - 'a'];
            if (no == null) return null;      // caminho quebrou: não existe
        }
        return no;
    }
}
```

```python
class Trie:
    def __init__(self):
        self.filhos = {}          # dict: flexível para qualquer alfabeto (unicode incluso)
        self.fim = False

    def insert(self, palavra):
        no = self
        for ch in palavra:
            no = no.filhos.setdefault(ch, Trie())  # cria o nó só se o caminho ainda não existe
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
```

### Busca com curinga `.` (DFS na trie)

```python
def search_wildcard(no, palavra, i=0):
    if i == len(palavra):
        return no.fim                          # consumiu tudo: vale se for palavra completa
    ch = palavra[i]
    if ch == ".":
        # o curinga obriga a testar TODOS os filhos deste nível (é aqui que o custo cresce)
        return any(search_wildcard(f, palavra, i + 1) for f in no.filhos.values())
    prox = no.filhos.get(ch)
    return prox is not None and search_wildcard(prox, palavra, i + 1)
```

## 4. Walkthrough Visual (Teste de Mesa)

`insert("car")`, `insert("cat")`, depois consultas:

```
raiz ── c ── a ── r*      (* = fim de palavra)
              └── t*
```

| Operação | Caminho percorrido | Resultado |
|---|---|---|
| `insert("car")` | cria c → a → r, marca r como fim | — |
| `insert("cat")` | reusa c → a, cria t, marca fim | só 1 nó novo! |
| `search("ca")` | c → a existe, mas `a.fim == false` | **false** |
| `startsWith("ca")` | c → a existe | **true** |
| `search("cat")` | c → a → t, `t.fim == true` | **true** ✔ |

## 5. Complexidade (Tempo e Espaço)

| Operação | Complexidade | Motivo |
|---|---|---|
| insert / search / startsWith | O(m) | m = tamanho da palavra; independe do nº de palavras |
| Curinga `.` | O(26^k · m) pior caso | cada `.` ramifica em todos os filhos |
| Espaço | O(total de chars × alfabeto) | o preço da velocidade de prefixo |

## 6. Pegadinhas e Erros Comuns

- Esquecer a flag `fim` → `search("ca")` retorna true só porque "ca" é prefixo de "cat".
- Word Search II buscando **cada palavra separadamente** na grade → TLE; a trie existe para compartilhar prefixos.
- No backtracking da grade, não desmarcar a célula visitada ao retornar.
- **Java**: `c - 'a'` estoura o array com maiúsculas/acentos — valide o alfabeto ou use `HashMap`.
- **Java**: `String.charAt` em recursão profunda tudo bem, mas concatenar prefixo por nó gera O(m²) — carregue índices.
- **Python**: `setdefault` cria nó por consulta se usado em `search` por engano — em busca, use `.get`.
- Não podar nós esgotados no Word Search II (remover folhas já encontradas) — a diferença entre aceito e TLE.

## 7. Aplicações no Mundo Real (Backend)

- **Roteador de URLs**: FastAPI/Starlette, Gin e Echo resolvem `/users/{id}` com **Radix Tree** — implemente um (pilar 4.8, o exercício-ponte da Fase 4).
- **Autocompletar** de buscadores e IDEs: desça ao prefixo, colete as folhas.
- **Tabelas de roteamento IP**: longest prefix match em roteadores é uma trie binária de bits.
- **PostgreSQL**: índices **SP-GiST** suportam tries para buscas por prefixo em texto.
- Dicionários de compressão (LZ78/LZW) constroem tries dos padrões já vistos.

## 8. Problemas Recomendados (Trilha de Estudo)

| # | Problema | Dificuldade |
|---|---|---|
| 208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium |
| 211 | [Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 Medium |
| 1268 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | 🟡 Medium |
| 421 | [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | 🟡 Medium |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | 🔴 Hard |
