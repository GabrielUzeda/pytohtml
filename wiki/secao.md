# `secao()`

> Bloco semântico `<section>` com padding vertical padrão para separar regiões de conteúdo.

`layout.py` · `layout`

---

## Assinatura

```python
secao(*conteudo: str, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Elementos filhos da seção |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Seção simples com título e parágrafo

```python
from pytohtml import secao, titulo, paragrafo

secao(
    titulo("Sobre nós"),
    paragrafo("Somos uma equipe apaixonada por Python."),
)
```

**HTML gerado:**

```html
<section class="py-12 px-4">
  <h2 ...>Sobre nós</h2>
  <p ...>Somos uma equipe apaixonada por Python.</p>
</section>
```

---

### 🔵 Nível 2 — Intermediário

> Seções alternadas com cores de fundo diferentes

```python
from pytohtml import secao, container, titulo, paragrafo

secao(
    container(titulo("Funcionalidades"), paragrafo("O que a lib oferece...")),
)

secao(
    container(titulo("Como usar"),       paragrafo("Guia passo a passo...")),
    classes="bg-white",
)

secao(
    container(titulo("Depoimentos"),     paragrafo("O que dizem sobre nós...")),
    classes="bg-blue-50",
)
```

> 💡 **Dica:** `py-12 px-4` já vem por padrão — padding vertical de 48px e horizontal de 16px. Para seções mais espaçosas (hero, CTA), use `classes="py-24"`.

---

### 🟡 Nível 3 — Difícil

> Seção com borda superior e ID para âncora

```python
from pytohtml import secao, container, titulo, grade, cartao, paragrafo

secao(
    container(
        titulo("Planos e Preços", tamanho="grande", classes="text-center"),
        paragrafo("Escolha o plano ideal para seu projeto.", classes="text-center text-gray-400"),
        grade(
            cartao(titulo("Free", tamanho="medio"),       paragrafo("Para começar")),
            cartao(titulo("Pro", tamanho="medio"),        paragrafo("Para projetos sérios")),
            cartao(titulo("Enterprise", tamanho="medio"), paragrafo("Para times grandes")),
            colunas=3,
            distanciamento=6,
        ),
    ),
    classes="bg-gray-50 border-t border-gray-100",
)
```

---

### 🟣 Nível 4 — Profissional

> Landing page com múltiplas seções bem estruturadas

```python
from pytohtml import html, cabecalho, secao, container, destaque, grade, cartao, titulo, paragrafo, botao, rodape

pagina = html(
    cabecalho(titulo("pytohtml", tamanho="medio")),

    secao(
        destaque(
            "HTML com Python puro",
            "Sem HTML, sem CSS — apenas chamadas de função Python.",
            botao("Começar", variante="primario"),
            botao("Ver docs", variante="fantasma"),
        ),
        classes="bg-gradient-to-br from-blue-50 to-indigo-50 py-24",
    ),

    secao(
        container(
            titulo("Por que pytohtml?", tamanho="grande", classes="text-center mb-8"),
            grade(
                cartao(titulo("Simples", tamanho="medio"), paragrafo("API intuitiva.")),
                cartao(titulo("Rápido",  tamanho="medio"), paragrafo("Zero configuração.")),
                cartao(titulo("Moderno", tamanho="medio"), paragrafo("Tailwind nativo.")),
                colunas=3,
            ),
        ),
        classes="bg-white",
    ),

    rodape(paragrafo("© 2026 pytohtml", classes="text-gray-400")),
    titulo_pagina="pytohtml",
)
```

---

← [container](container) · **secao** · [cabecalho-e-rodape →](cabecalho-e-rodape)
