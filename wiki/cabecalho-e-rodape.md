# `cabecalho()` e `rodape()`

> `cabecalho()` cria um `<header>` com fundo branco e sombra. `rodape()` cria um `<footer>` com fundo escuro e texto claro.

`layout.py` · `layout`

---

## Assinaturas

```python
cabecalho(*conteudo: str, classes: str | None = None) → str

rodape(*conteudo: str, classes: str | None = None) → str
```

## Parâmetros (iguais em ambas)

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Elementos filhos do header/footer |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Cabeçalho simples com título

```python
from pytohtml import cabecalho, rodape, titulo, paragrafo

cabecalho(titulo("Meu Site", tamanho="medio"))

rodape(paragrafo("© 2026 Meu Site. Todos os direitos reservados.", classes="text-gray-400"))
```

**HTML gerado — `cabecalho()`:**

```html
<header class="bg-white shadow-sm py-4 px-6 flex items-center justify-between">
  <h3 ...>Meu Site</h3>
</header>
```

**HTML gerado — `rodape()`:**

```html
<footer class="bg-gray-800 text-gray-300 text-sm py-6 px-6 text-center mt-auto">
  <p ...>© 2026 Meu Site...</p>
</footer>
```

---

### 🔵 Nível 2 — Intermediário

> Cabeçalho com logo + nav + botão

```python
from pytohtml import cabecalho, linha, nav, titulo, imagem, botao, link

cabecalho(
    linha(
        imagem("https://www.python.org/static/favicon.ico", alt="Logo", arredondada=False, classes="w-7 h-7"),
        titulo("pytohtml", tamanho="medio", classes="text-lg font-bold"),
        centralizado=True, distanciamento=2,
    ),
    nav(
        link("Docs",    href="/docs"),
        link("Exemplos", href="/exemplos"),
        botao("Começar", variante="primario", classes="text-sm"),
    ),
)
```

> 💡 **Dica:** `cabecalho()` já aplica `flex items-center justify-between` — perfeito para logo à esquerda e nav à direita. Se precisar de sticky header, adicione `classes="sticky top-0 z-50 backdrop-blur-md"`.

---

### 🟡 Nível 3 — Difícil

> Rodapé com colunas de links

```python
from pytohtml import rodape, container, grade, coluna, titulo, lista, link, paragrafo, divisor

rodape(
    container(
        grade(
            coluna(
                titulo("pytohtml", tamanho="pequeno", classes="text-white"),
                paragrafo("Gere HTML com Python puro.", classes="text-gray-400 text-sm"),
                centralizado=False, distanciamento=2,
            ),
            coluna(
                titulo("Documentação", tamanho="pequeno", classes="text-gray-300"),
                lista(
                    link("Instalação",   href="/wiki/Instalacao",    classes="text-gray-400 hover:text-white no-underline"),
                    link("Componentes",  href="/wiki/Home",           classes="text-gray-400 hover:text-white no-underline"),
                    link("Exemplos",     href="/exemplos",            classes="text-gray-400 hover:text-white no-underline"),
                    classes="space-y-1",
                ),
                centralizado=False, distanciamento=2,
            ),
            coluna(
                titulo("Links", tamanho="pequeno", classes="text-gray-300"),
                lista(
                    link("GitHub", href="https://github.com/GabrielUzeda/pytohtml", classes="text-gray-400 hover:text-white no-underline"),
                    classes="space-y-1",
                ),
                centralizado=False, distanciamento=2,
            ),
            colunas=3,
        ),
        divisor(classes="border-gray-700 my-6"),
        paragrafo("© 2026 pytohtml. MIT License.", classes="text-gray-500 text-center text-xs"),
        classes="max-w-5xl",
    ),
)
```

---

### 🟣 Nível 4 — Profissional

> Cabeçalho sticky com sombra progressiva no scroll

```python
from pytohtml import html, cabecalho, linha, nav, titulo, botao

pagina = html(
    cabecalho(
        linha(
            titulo("pytohtml", tamanho="medio"),
            nav(
                botao("Início",   variante="texto"),
                botao("Docs",     variante="texto"),
                botao("Começar",  variante="primario", classes="rounded-full shadow-md"),
            ),
            centralizado=False, distanciamento=0, classes="w-full justify-between",
        ),
        classes="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm",
    ),
    titulo_pagina="pytohtml",
)
```

---

## Referência Rápida

| Componente | Tag | Classes padrão |
|------------|-----|----------------|
| `cabecalho()` | `<header>` | `bg-white shadow-sm py-4 px-6 flex items-center justify-between` |
| `rodape()` | `<footer>` | `bg-gray-800 text-gray-300 text-sm py-6 px-6 text-center mt-auto` |

---

← [secao](secao) · **cabecalho e rodape** · [nav →](nav)
