# [0388] Longest Absolute File Path

> 🔗 [LeetCode 388](https://leetcode.com/problems/longest-absolute-file-path/) · Dificuldade: 🟡 medium · Categoria: [`04_stack`](../../../fundamentos/04_stack.md)
> 📅 Resolvido em: 2026-07-28 · Revisões: —

Tags: `#Stack` `#String` `#DFS`

## 📜 O Problema

Um sistema de arquivos armazena diretórios e arquivos. A representação em texto usa `'\n'` para nova linha e `'\t'` para indentação (um `'\t'` por nível de profundidade). Por exemplo:

```
dir
	subdir1
		file1.ext
		subsubdir1
	subdir2
		subsubdir2
			file2.ext
```

vira a string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`.

Cada arquivo/diretório tem um **caminho absoluto** único, formado pela concatenação dos diretórios com `'/'`. Retorne o **comprimento** do caminho absoluto mais longo até um **arquivo** (não diretório). Se não houver nenhum arquivo, retorne `0`.

**Exemplos:**
```
Input:  input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explicação: único arquivo, caminho "dir/subdir2/file.ext" tem comprimento 20.

Input:  input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explicação: dois arquivos; o caminho "dir/subdir2/subsubdir2/file2.ext" (32) é o mais longo.

Input:  input = "a"
Output: 0
Explicação: só um diretório, nenhum arquivo.
```

**Restrições (e o que elas denunciam):**
- `1 <= input.length <= 10^4` → precisa de solução O(n); reconstruir caminhos completos a cada arquivo do zero seria arriscado
- Nomes de diretório/arquivo consistem de letras, dígitos, espaços; arquivos têm formato `nome.extensao` → detectar "é arquivo" é simplesmente checar se o nome contém um `'.'`
- Testcases garantem sistema de arquivos válido, sem nomes de comprimento 0 → não é preciso validar a estrutura de indentação

## 🧭 Como reconhecer o padrão

"Rastrear o caminho acumulado até o nível de profundidade atual, onde a profundidade é indicada por indentação (`'\t'`)" é a mesma ideia de [1598] Crawler Log Folder e [0071] Simplify Path: cada nível de indentação é análogo a "entrar numa subpasta", e voltar a um nível de indentação menor é análogo a "subir". Aqui, em vez de contar apenas a profundidade, você precisa saber o **comprimento acumulado do caminho** em cada nível — o que se resolve com uma pilha (ou array indexado por profundidade) que guarda o comprimento do caminho até aquele nível.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Para cada linha, reconstruir o caminho completo desde a raiz percorrendo todas as linhas anteriores e concatenando os nomes cuja profundidade é menor ou igual à atual (seguindo a hierarquia).

- Tempo: O(n²) pior caso · Espaço: O(n)
- **Por que não basta:** para cada linha, você refaz a reconstrução do caminho completo, reaproveitando pouco do trabalho já feito para linhas anteriores na mesma hierarquia. Com uma pilha/array de comprimentos por profundidade, cada linha é processada em O(1) amortizado, aproveitando o prefixo já calculado.

## 💡 Solução 2 — A ideia otimizada (intuição)

Divida `input` por `'\n'` para obter cada linha. Use uma estrutura (array ou pilha) `comprimentoAte[profundidade]` que guarda o comprimento acumulado do caminho até aquele nível. Para cada linha: calcule sua **profundidade** contando os `'\t'` no início (removendo-os para obter o nome real). Se a linha contém um `'.'`, é um **arquivo** — calcule seu comprimento total como `comprimentoAte[profundidade] + tamanho_do_nome (+1 para a barra, se profundidade > 0)` e atualize o máximo. Caso contrário, é um **diretório** — atualize `comprimentoAte[profundidade + 1]` com esse mesmo cálculo, para que os filhos dessa pasta possam reaproveitá-lo.

## 🎬 Exemplo passo a passo

`input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` → linhas: `["dir", "\tsubdir1", "\tsubdir2", "\t\tfile.ext"]`

| Passo | Linha | Profundidade | É arquivo? | comprimentoAte[profundidade] | Comprimento calculado | maxLen após |
|---|---|---|---|---|---|---|
| 1 | `"dir"` | 0 | não | 0 (base) | `0 + 3 = 3` | 0 (não é arquivo) |
| 2 | `"\tsubdir1"` | 1 | não | `comprimentoAte[1] = 3` (setado no passo 1) | `3 + 1(/) + 7 = 11` | 0 |
| 3 | `"\tsubdir2"` | 1 | não | `comprimentoAte[1] = 3` (ainda o mesmo, sobrescreve o valor de subdir1) | `3 + 1 + 7 = 11` | 0 |
| 4 | `"\t\tfile.ext"` | 2 | sim (tem `.`) | `comprimentoAte[2] = 11` (setado no passo 3, referente a subdir2) | `11 + 1(/) + 8 = 20` | **20** |

Resultado final: `20` ✔ (bate com o enunciado — caminho `"dir/subdir2/file.ext"`)

## ⚡ Complexidade da solução ótima

- **Tempo:** O(n) — cada caractere da entrada é visitado O(1) vezes no total (dividir por linhas, contar tabs, medir nome)
- **Espaço:** O(profundidade máxima) — o array `comprimentoAte` tem tamanho proporcional ao nível de aninhamento máximo, tipicamente muito menor que `n`

## 💻 Implementações

### Java (referência completa e comentada)
```java
public int lengthLongestPath(String input) {
    String[] linhas = input.split("\n");
    // comprimentoAte[d] = comprimento do caminho acumulado até profundidade d (sem contar o nome desta linha)
    int[] comprimentoAte = new int[linhas.length + 1];
    int maiorArquivo = 0;

    for (String linha : linhas) {
        String nome = linha.replaceFirst("^\t+", ""); // remove os tabs iniciais
        int profundidade = linha.length() - nome.length(); // quantidade de tabs = nível

        // +1 para a barra "/", exceto na raiz (profundidade 0)
        int comprimento = comprimentoAte[profundidade] + nome.length() + (profundidade > 0 ? 1 : 0);

        if (nome.indexOf('.') >= 0) {          // é arquivo: candidato à resposta
            maiorArquivo = Math.max(maiorArquivo, comprimento);
        } else {                                // é diretório: guarda para os filhos reaproveitarem
            comprimentoAte[profundidade + 1] = comprimento;
        }
    }

    return maiorArquivo;
}
```

### Python (pratique você — reimplemente sem olhar o Java)
```python
# TODO: sua vez. Regra da trilha: implemente do zero no dia seguinte.
```

### C++ (pratique você)
```cpp
// TODO: sua vez.
```

## ⚠️ Pegadinhas e erros comuns

- Esquecer o `+1` da barra `'/'` separadora, ou aplicá-lo também na raiz (profundidade 0) — a raiz não tem barra antes dela; só os níveis subsequentes precisam desse `+1`.
- Detectar "é arquivo" de forma incorreta — a regra do problema é simplesmente "contém um ponto `'.'`"; não é preciso validar extensão nem formato, só a presença do caractere.
- Usar uma pilha que precisa ser "podada" manualmente quando a profundidade diminui (voltar de um nível fundo para um raso) — usar um **array indexado por profundidade** (como no código acima) evita esse problema: sobrescrever `comprimentoAte[profundidade+1]` automaticamente "esquece" qualquer irmão mais fundo anterior, sem precisar de lógica de desempilhamento explícita.
- Contar tabs incorretamente quando o nome do arquivo/diretório poderia conter caracteres parecidos — como o enunciado garante que só os tabs iniciais indicam profundidade, `replaceFirst("^\t+", "")` (ou equivalente) captura exatamente isso.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Nenhum arquivo, só diretórios | `"a"` | 0 | sem nenhum `.` na entrada, `maiorArquivo` nunca é atualizado |
| Múltiplos arquivos em profundidades diferentes | `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` | 32 | testa que o maior entre múltiplos candidatos é escolhido corretamente |
| Irmãos no mesmo nível sobrescrevendo o array | `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` | 20 | garante que `comprimentoAte[1]` reflete sempre o irmão mais recente, não uma mistura |
| Arquivo direto na raiz | `"a.txt"` | 5 | caso trivial sem nenhuma indentação |

## 🔗 Conexões

- Problemas irmãos: [1598] Crawler Log Folder (mesmo domínio de navegação hierárquica, mas só rastreando profundidade numérica), [0071] Simplify Path (mesma ideia de acumular caminho por nível, mas processando um caminho já linear em vez de uma árvore serializada por indentação)
- No backend: essa técnica de "array indexado por profundidade guardando o estado acumulado até aquele nível" aparece em processadores de arquivos de configuração indentados (YAML "à mão"), em geradores de breadcrumbs de navegação hierárquica, e em ferramentas de análise de código que calculam caminhos completos a partir de estruturas de indentação (como Python).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
