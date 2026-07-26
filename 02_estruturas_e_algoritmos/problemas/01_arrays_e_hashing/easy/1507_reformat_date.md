# [1507] Reformat Date

> 🔗 [LeetCode 1507](https://leetcode.com/problems/reformat-date/) · Dificuldade: 🟢 easy · Categoria: [`01_arrays_e_hashing`](../../../fundamentos/01_arrays_e_hashing.md)
> 📅 Resolvido em: 2026-07-26 · Revisões: —

Tags: `#String` `#Easy`

## 📜 O Problema

Dada uma string `date` no formato `Day Month Year`, onde:
- `Day` é do conjunto `{"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}`.
- `Month` é do conjunto `{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}`.
- `Year` está no intervalo `[1900, 2100]`.

Converta a string de data para o formato `YYYY-MM-DD`, onde `YYYY` é o ano com 4 dígitos, `MM` é o mês com 2 dígitos, e `DD` é o dia com 2 dígitos.

**Exemplos:**
```
Input:  date = "20th Oct 2052"
Output: "2052-10-20"

Input:  date = "6th Jun 1933"
Output: "1933-06-06"

Input:  date = "26th May 1960"
Output: "1960-05-26"
```

**Restrições (e o que elas denunciam):**
- as datas são sempre válidas, sem necessidade de tratamento de erro → simplifica o parsing
- meses fixos num conjunto de 12 abreviações → mapa fixo mês→número

## 🧭 Como reconhecer o padrão

"Converter entre formatos de data com componentes fixos e um mapa de abreviações conhecido" é resolvido tokenizando a string por espaço, extraindo o número do dia (removendo o sufixo ordinal), traduzindo o mês via mapa fixo, e remontando no formato alvo.

## 🐢 Solução 1 — Força bruta (o ponto de partida)

Dividir a string em 3 tokens (`split(" ")`), processar cada um individualmente, e concatenar no novo formato — já é essencialmente a única abordagem razoável.

- Tempo: O(1) — a string tem tamanho fixo pequeno · Espaço: O(1)
- **Por que vale nomear mesmo assim:** não há uma versão "pior" real; a única armadilha é extrair corretamente o número do dia removendo o sufixo ordinal ("st", "nd", "rd", "th").

## 💡 Solução 2 — A ideia otimizada (mesma ideia, formalizada)

Use um mapa fixo `mês→número` (com os 12 nomes abreviados). Tokenize a data por espaço. Extraia o dia removendo os últimos 2 caracteres (o sufixo ordinal sempre tem 2 letras). Formate garantindo zero à esquerda no dia.

## 🎬 Exemplo passo a passo

`date = "20th Oct 2052"` — tokens: `["20th", "Oct", "2052"]`

| Passo | Componente | Processamento | Valor |
|---|---|---|---|
| 1 | dia | remove os últimos 2 chars ("th") de "20th" | "20" |
| 2 | mês | mapa["Oct"] | "10" |
| 3 | ano | já está no formato certo | "2052" |
| 4 | montagem | ano-mês-dia | "2052-10-20" |

Resultado final: `"2052-10-20"` ✔

## ⚡ Complexidade da solução ótima

- **Tempo:** O(1) — tamanho fixo pequeno de entrada
- **Espaço:** O(1)

## 💻 Implementações

### Java (referência completa e comentada)
```java
public String reformatDate(String date) {
    Map<String, String> meses = Map.ofEntries(
        Map.entry("Jan", "01"), Map.entry("Feb", "02"), Map.entry("Mar", "03"),
        Map.entry("Apr", "04"), Map.entry("May", "05"), Map.entry("Jun", "06"),
        Map.entry("Jul", "07"), Map.entry("Aug", "08"), Map.entry("Sep", "09"),
        Map.entry("Oct", "10"), Map.entry("Nov", "11"), Map.entry("Dec", "12")
    );

    String[] partes = date.split(" ");
    String diaBruto = partes[0];
    String dia = diaBruto.substring(0, diaBruto.length() - 2); // remove o sufixo ordinal (2 letras)
    if (dia.length() == 1) {
        dia = "0" + dia; // garante 2 dígitos (ex.: "6" vira "06")
    }
    String mes = meses.get(partes[1]);
    String ano = partes[2];

    return ano + "-" + mes + "-" + dia;
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

- Assumir que o sufixo ordinal tem tamanho variável — "st", "nd", "rd" e "th" são sempre 2 caracteres, é seguro removê-los assim.
- Esquecer de adicionar o zero à esquerda no dia quando ele é de um único dígito (ex.: "6th" → dia "6", precisa virar "06") — o mês já vem do mapa fixo com 2 dígitos, mas o dia precisa de tratamento manual.
- Usar `Integer.parseInt` no dia e depois `String.format("%02d", ...)` sem cuidado — funciona, mas manipular a string diretamente evita uma conversão numérica desnecessária.

## 🧪 Casos de teste para validar

| Caso | Input | Esperado | Por quê |
|---|---|---|---|
| Dia de dois dígitos | "20th Oct 2052" | "2052-10-20" | caso padrão do enunciado |
| Dia de um dígito | "6th Jun 1933" | "1933-06-06" | precisa do zero à esquerda no dia |
| Sufixo "th" em dia terminado em 6 | "26th May 1960" | "1960-05-26" | ilustra que o sufixo não depende do último dígito do número |
| Mês de dois dígitos | "1st Dec 2000" | "2000-12-01" | mês "Dec" mapeia para "12", dia "1" vira "01" |

## 🔗 Conexões

- Problemas irmãos: [1108] Defanging an IP Address (mesmo nível de manipulação/reformatação de string), [0165] Compare Version Numbers (mesma técnica de tokenizar e comparar componentes de um formato estruturado)
- No backend: normalização de formatos de data ao integrar sistemas diferentes (ex.: converter datas de uma API externa em formato "DD Mon YYYY" para o padrão ISO 8601 usado internamente).

## 📝 O que eu aprendi (PREENCHER À MÃO — a IA nunca escreve aqui)

<!-- 3 frases, de memória, sem olhar o resto do doc. Se não conseguir, o problema não está aprendido. -->
