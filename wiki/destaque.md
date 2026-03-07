# `destaque()`

> Seção hero de destaque — comum no topo de landing pages, com título grande, subtítulo e botões centralizados.

`layout.py` · `layout`

---

## Assinatura

```python
destaque(titulo_destaque: str, subtitulo: str, *botoes: str, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `titulo_destaque` | `str` | — | Título principal da seção (obrigatório) |
| `subtitulo` | `str` | — | Subtítulo descritivo (obrigatório) |
| `*botoes` | `str` | — | Botões CTA (call-to-action) — opcionais |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Hero simples sem botões

```python
from pytohtml import destaque

destaque(
    "Bem-vindo ao pytohtml",
    "Gere HTML com Python puro, sem escrever HTML."
)
```

**HTML gerado:**

```html
<div class="relative pt-24 pb-32 px-4 text-center overflow-hidden">
  <h1 class="text-5xl md:text-6xl font-extrabold tracking-tight mb-6">Bem-vindo ao pytohtml</h1>
  <p class="mt-4 text-xl md:text-2xl max-w-3xl mx-auto mb-10 opacity-80">Gere HTML com Python puro...</p>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Hero com botões CTA

```python
from pytohtml import destaque, botao

destaque(
    "pytohtml",
    "HTML + Tailwind CSS gerado com Python puro.",
    botao("Começar agora",  variante="primario",   classes="px-8 py-3 text-base rounded-full shadow-lg"),
    botao("Ver exemplos",   variante="secundario",  classes="px-8 py-3 text-base rounded-full"),
)
```

> 💡 **Dica:** Os `*botoes` são colocados dentro de um `<div class="mt-8 flex justify-center gap-4">` automaticamente. Use `variante="primario"` para o CTA principal e `variante="fantasma"` ou `"secundario"` para a opção secundária.

---

### 🟡 Nível 3 — Difícil

> Hero com gradiente de fundo

```python
from pytohtml import destaque, botao

destaque(
    "HTML que escreve a si mesmo",
    "Com pytohtml, sua UI vive onde sempre deveria: no Python.",
    botao("Instalar agora",     variante="primario",  classes="rounded-full shadow-xl px-8 py-3 text-base"),
    botao("Ver no GitHub",      variante="fantasma",  classes="rounded-full px-8 py-3 text-base border-white text-white hover:bg-white/10"),
    classes="bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-700 text-white",
)
```

---

### 🟣 Nível 4 — Profissional

> Landing page completa com hero, features e CTA final

```python
from pytohtml import html, cabecalho, secao, container, destaque, grade, cartao, titulo, paragrafo, botao, rodape, linha, nav, link

pagina = html(
    cabecalho(
        linha(
            titulo("pytohtml", tamanho="medio"),
            nav(link("Docs", href="/docs"), botao("Começar", variante="primario")),
            centralizado=False, distanciamento=0, classes="w-full justify-between",
        ),
        classes="sticky top-0 z-50 bg-white/90 backdrop-blur-md shadow-sm border-b border-gray-100",
    ),

    secao(
        destaque(
            "HTML com Python puro",
            "Tailwind CSS, SweetAlert2 e Brython prontos para usar. Sem configuração.",
            botao("Começar grátis", variante="primario",  classes="rounded-full px-8 py-3 text-base shadow-lg"),
            botao("Ver docs",       variante="fantasma",  classes="rounded-full px-8 py-3 text-base"),
        ),
        classes="bg-gradient-to-b from-blue-50 to-white",
    ),

    secao(
        container(
            titulo("O que você obtém", tamanho="grande", classes="text-center mb-8"),
            grade(
                cartao(titulo("40+ componentes", tamanho="medio"), paragrafo("Tipografia, layout, formulários e mais.")),
                cartao(titulo("Zero dependências", tamanho="medio"), paragrafo("Tudo via CDN no browser.")),
                cartao(titulo("Brython incluso", tamanho="medio"), paragrafo("Python interativo no browser.")),
                colunas=3,
            ),
        ),
    ),

    rodape(paragrafo("© 2026 pytohtml · MIT License", classes="text-gray-400")),
    titulo_pagina="pytohtml — HTML com Python",
)
```

---

## Referência Rápida

| Elemento | Tag / classe | Descrição |
|----------|-------------|-----------|
| Título | `<h1 class="text-5xl md:text-6xl font-extrabold">` | Automático — use `titulo_destaque` |
| Subtítulo | `<p class="text-xl md:text-2xl max-w-3xl mx-auto">` | Automático — use `subtitulo` |
| Botões | `<div class="flex justify-center gap-4">` | Agrupados automaticamente |

---

← [nav](nav) · **destaque** · [modal →](modal)
