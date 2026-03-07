# `nav()`

> Gera uma barra de navegação horizontal com `<nav>` e espaçamento automático entre os itens.

`layout.py` · `layout`

---

## Assinatura

```python
nav(*conteudo: str, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Itens de navegação (links, botões) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Navegação com links simples

```python
from pytohtml import nav, link

nav(
    link("Início",    href="/"),
    link("Sobre",     href="/sobre"),
    link("Contato",   href="/contato"),
)
```

**HTML gerado:**

```html
<nav class="flex gap-6 items-center">
  <a href="/" ...>Início</a>
  <a href="/sobre" ...>Sobre</a>
  <a href="/contato" ...>Contato</a>
</nav>
```

---

### 🔵 Nível 2 — Intermediário

> Nav com links e botão CTA

```python
from pytohtml import nav, link, botao

nav(
    link("Documentação", href="/docs",     classes="text-gray-600 hover:text-blue-600 no-underline"),
    link("Exemplos",     href="/exemplos", classes="text-gray-600 hover:text-blue-600 no-underline"),
    link("GitHub",       href="https://github.com/GabrielUzeda/pytohtml", classes="text-gray-600 hover:text-blue-600 no-underline"),
    botao("Começar grátis", variante="primario", classes="rounded-full text-sm shadow-md"),
)
```

> 💡 **Dica:** `flex gap-6 items-center` já vem por padrão. Para nav vertical (sidebar), use `classes="flex-col items-start gap-2"`.

---

### 🟡 Nível 3 — Difícil

> Nav responsiva dentro do cabeçalho

```python
from pytohtml import cabecalho, linha, nav, titulo, imagem, botao, link

cabecalho(
    linha(
        # Logo
        linha(
            imagem("https://www.python.org/static/favicon.ico", arredondada=False, classes="w-7 h-7"),
            titulo("pytohtml", tamanho="medio", classes="text-lg font-black"),
            centralizado=True, distanciamento=2,
        ),
        # Links centrais
        nav(
            link("Docs",     href="/docs",     classes="text-sm text-gray-600 hover:text-blue-600 no-underline font-medium"),
            link("Exemplos", href="/exemplos", classes="text-sm text-gray-600 hover:text-blue-600 no-underline font-medium"),
            link("Blog",     href="/blog",     classes="text-sm text-gray-600 hover:text-blue-600 no-underline font-medium"),
        ),
        # Ações à direita
        nav(
            link("Entrar",    href="/login",   classes="text-sm text-gray-600 no-underline"),
            botao("Começar",  variante="primario", classes="text-sm rounded-full"),
        ),
        centralizado=False, distanciamento=0, classes="w-full justify-between",
    ),
    classes="sticky top-0 z-50 border-b border-gray-100 shadow-sm",
)
```

---

### 🟣 Nível 4 — Profissional

> Sidebar de navegação vertical com seções

```python
from pytohtml import coluna, nav, titulo, link, divisor, etiqueta

def nav_section(nome_secao, *links):
    return coluna(
        titulo(nome_secao, tamanho="pequeno", classes="text-xs text-gray-400 uppercase tracking-wider"),
        nav(
            *links,
            classes="flex-col items-start gap-1",
        ),
        centralizado=False, distanciamento=1,
    )

sidebar = coluna(
    nav_section("Começar",
        link("Instalação",  href="/wiki/Instalacao", classes="text-sm text-gray-700 no-underline hover:text-blue-600"),
        link("html e salvar", href="/wiki/html-e-salvar", classes="text-sm text-gray-700 no-underline hover:text-blue-600"),
    ),
    divisor(classes="my-2"),
    nav_section("Componentes",
        link("titulo()",    href="/wiki/titulo",   classes="text-sm text-gray-700 no-underline hover:text-blue-600"),
        link("paragrafo()", href="/wiki/paragrafo", classes="text-sm text-gray-700 no-underline hover:text-blue-600"),
        link("botao()",     href="/wiki/botao",    classes="text-sm text-gray-700 no-underline hover:text-blue-600"),
    ),
    centralizado=False, distanciamento=3,
    classes="w-56 p-4 border-r border-gray-200 min-h-screen",
)
```

---

← [cabecalho-e-rodape](cabecalho-e-rodape) · **nav** · [destaque →](destaque)
