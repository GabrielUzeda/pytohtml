# `container()`

> Contêiner centralizado com largura máxima e padding lateral — elemento fundamental para limitar o conteúdo a uma largura legível.

`layout.py` · `layout`

---

## Assinatura

```python
container(*conteudo: str, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Elementos filhos |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Página centralizada com largura máxima

```python
from pytohtml import html, container, titulo, paragrafo

pagina = html(
    container(
        titulo("Meu Site"),
        paragrafo("Conteúdo centralizado com largura máxima de 1024px."),
    ),
    titulo_pagina="Início"
)
```

**HTML gerado:**

```html
<div class="max-w-5xl mx-auto px-4 py-8">
  <h2 ...>Meu Site</h2>
  <p ...>Conteúdo centralizado com largura máxima de 1024px.</p>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Containers aninhados para diferentes larguras

```python
from pytohtml import container, titulo, paragrafo, grade, cartao

# Container padrão (max-w-5xl = ~1024px)
container(
    titulo("Seção de destaque"),
    paragrafo("Conteúdo com largura padrão."),
)

# Container mais estreito para formulários ou texto
container(
    titulo("Formulário", tamanho="medio"),
    paragrafo("Texto com largura estreita, ideal para leitura."),
    classes="max-w-lg",  # Sobrescreve max-w-5xl
)

# Container largo para dashboards
container(
    grade(cartao("A"), cartao("B"), cartao("C"), colunas=3),
    classes="max-w-7xl",
)
```

> 💡 **Dica:** `max-w-5xl mx-auto px-4 py-8` já vem por padrão. Para sobrescrever a largura máxima, passe a nova classe via `classes=` — ela será adicionada, mas o `max-w-5xl` original também permanece. Use `classes="!max-w-lg"` (com `!` para `!important`) se precisar garantir a sobreposição.

---

### 🟡 Nível 3 — Difícil

> Container em cada seção de uma landing page

```python
from pytohtml import html, secao, container, destaque, grade, cartao, titulo, paragrafo, botao

pagina = html(
    # Hero sem container (largura total)
    destaque(
        "pytohtml",
        "HTML com Python puro + Tailwind CSS",
        botao("Começar agora", variante="sucesso"),
    ),

    # Seção de features com container
    secao(
        container(
            titulo("Funcionalidades", tamanho="grande", classes="text-center mb-8"),
            grade(
                cartao(titulo("Simples", tamanho="medio"),   paragrafo("API Python intuitiva.")),
                cartao(titulo("Rápido",  tamanho="medio"),   paragrafo("Gera HTML puro.")),
                cartao(titulo("Moderno", tamanho="medio"),   paragrafo("Tailwind CSS built-in.")),
                colunas=3,
            ),
        )
    ),

    titulo_pagina="pytohtml",
)
```

---

### 🟣 Nível 4 — Profissional

> Layout de blog com container de conteúdo estreito

```python
from pytohtml import html, cabecalho, container, coluna, titulo, paragrafo, etiqueta, divisor, rodape

post = html(
    cabecalho(titulo("Blog pytohtml", tamanho="medio")),
    container(
        coluna(
            linha(etiqueta("Tutorial", cor="azul"), etiqueta("Python", cor="roxo"), centralizado=False, distanciamento=2),
            titulo("Como gerar uma landing page em 10 linhas", tamanho="gigante"),
            paragrafo("Publicado em 7 de março de 2026 · 5 min de leitura", classes="text-gray-400 text-sm"),
            divisor(),
            paragrafo("Neste tutorial, vamos criar uma landing page completa usando apenas Python e a biblioteca pytohtml..."),
            centralizado=False, distanciamento=4,
        ),
        classes="max-w-2xl",  # Largura ideal para leitura de artigo
    ),
    rodape(paragrafo("© 2026 pytohtml", classes="text-gray-400")),
    titulo_pagina="Blog",
)
```

---

## Referência Rápida

| Largura | Classe | Pixels aprox. | Uso típico |
|---------|--------|--------------|------------|
| `max-w-sm` | ~384px | Formulários estreitos |
| `max-w-lg` | ~512px | Formulários, modals |
| `max-w-2xl` | ~672px | Artigos, blog posts |
| `max-w-4xl` | ~896px | Documentação |
| `max-w-5xl` | ~1024px | Padrão do `container()` |
| `max-w-7xl` | ~1280px | Dashboards, admin |

---

← [grade](grade) · **container** · [secao →](secao)
