# `html()` e `salvar()`

> Geram a estrutura completa da página HTML e salvam o resultado em disco.

`pagina.py` · `estrutura base`

---

## Assinaturas

```python
html(
    *conteudo: str,
    titulo_pagina: str = "Página",
    lang: str = "pt-BR",
    head_extra: str = "",
    brython: bool = False,
    favicon: str = ""
) → str

salvar(caminho: str, conteudo: str) → None
```

## Parâmetros — `html()`

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Elementos HTML filhos (strings geradas pelas outras funções) |
| `titulo_pagina` | `str` | `"Página"` | Texto do `<title>` |
| `lang` | `str` | `"pt-BR"` | Idioma da página (`lang` do `<html>`) |
| `head_extra` | `str` | `""` | Conteúdo extra inserido no `<head>` (fontes, estilos, scripts) |
| `brython` | `bool` | `False` | Inclui o Brython via CDN para scripts Python client-side |
| `favicon` | `str` | `""` | URL do favicon (`<link rel="icon">`) |

## Parâmetros — `salvar()`

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `caminho` | `str` | — | Caminho do arquivo de destino (ex: `"index.html"`) |
| `conteudo` | `str` | — | String HTML completa retornada por `html()` |

> 💡 `html()` inclui automaticamente Tailwind CSS e SweetAlert2 via CDN. Brython é opcional e ativado por `brython=True`.

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Página mínima com título e parágrafo

```python
from pytohtml import html, salvar, titulo, paragrafo

pagina = html(
    titulo("Olá, Mundo!"),
    paragrafo("Minha primeira página com pytohtml."),
    titulo_pagina="Meu Site"
)

salvar("index.html", pagina)
```

**HTML gerado (estrutura):**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Meu Site</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
</head>
<body class="bg-gray-50 text-gray-800 antialiased min-h-screen">
  <h2 ...>Olá, Mundo!</h2>
  <p ...>Minha primeira página com pytohtml.</p>
</body>
</html>
```

---

### 🔵 Nível 2 — Intermediário

> Adicionando favicon e idioma customizado

```python
pagina = html(
    titulo("Bem-vindo", tamanho="gigante"),
    paragrafo("Site em inglês."),
    titulo_pagina="Welcome",
    lang="en",
    favicon="https://www.python.org/static/favicon.ico"
)

salvar("index.html", pagina)
```

> 💡 **Dica:** O `lang` afeta leitores de tela e ferramentas de SEO. Use `"pt-BR"` para português do Brasil, `"en"` para inglês.

---

### 🟡 Nível 3 — Difícil

> Injetando fontes e estilos customizados via `head_extra`

```python
HEAD_EXTRA = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Inter', sans-serif; }
</style>
"""

pagina = html(
    titulo("Design com fonte customizada", tamanho="gigante"),
    paragrafo("Usando Inter via Google Fonts."),
    titulo_pagina="Custom Fonts",
    head_extra=HEAD_EXTRA
)

salvar("index.html", pagina)
```

---

### 🟣 Nível 4 — Profissional

> Página completa com Brython, favicon e `head_extra`

```python
from pytohtml import *

HEAD_EXTRA = """
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>body { font-family: 'JetBrains Mono', monospace; }</style>
"""

pagina = html(
    cabecalho(titulo("App", tamanho="medio")),
    container(
        espaco_dinamico("resultado", "mt-4"),
        botao("Buscar dados", classes='id="btn"'),
        buscar_dados(
            "https://dummyjson.com/quotes/random",
            seletor_resultado="#resultado",
            gatilho_clique="#btn"
        ),
    ),
    titulo_pagina="Meu App",
    brython=True,
    favicon="https://www.python.org/static/favicon.ico",
    head_extra=HEAD_EXTRA,
)

salvar("app.html", pagina)
```

> ⚠️ **Atenção:** `brython=True` adiciona ~1MB via CDN. Ative apenas quando for usar funções de interatividade (`ao_clicar`, `estado`, `buscar_dados`, etc.).

---

## O que é incluído automaticamente

| Recurso | CDN | Condicional |
|---------|-----|-------------|
| Tailwind CSS | `cdn.tailwindcss.com` | Sempre |
| SweetAlert2 v11 | `cdn.jsdelivr.net/npm/sweetalert2@11` | Sempre |
| Brython 3.14.0 | `cdn.jsdelivr.net/npm/brython@3.14.0` | Só com `brython=True` |
| Favicon | URL informada | Só com `favicon="..."` |

---

[← Instalação](Instalacao) · **html e salvar** · [titulo →](titulo)
