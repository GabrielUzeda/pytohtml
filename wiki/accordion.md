# `accordion()`

> Painel retrátil expansível nativo usando as tags HTML `<details>` e `<summary>` — sem JavaScript.

`elementos.py` · `layout`

---

## Assinatura

```python
accordion(titulo_aba: str, *conteudo: str, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `titulo_aba` | `str` | — | Texto do cabeçalho clicável (obrigatório) |
| `*conteudo` | `str` | — | Elementos filhos exibidos ao expandir |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Accordion simples com um parágrafo

```python
from pytohtml import accordion, paragrafo

accordion(
    "O que é pytohtml?",
    paragrafo("Uma biblioteca Python pura para gerar HTML com Tailwind CSS.")
)
```

**HTML gerado (estrutura):**

```html
<details class="group border border-gray-200 rounded-xl bg-white overflow-hidden my-4">
  <summary class="cursor-pointer px-5 py-4 font-medium text-gray-800 bg-gray-50 ...">
    O que é pytohtml?
    <span class="text-gray-400 group-open:rotate-180 transition-transform duration-200">▼</span>
  </summary>
  <div class="px-5 py-4 text-gray-600 bg-white border-t border-gray-200">
    <p ...>Uma biblioteca Python pura para gerar HTML com Tailwind CSS.</p>
  </div>
</details>
```

---

### 🔵 Nível 2 — Intermediário

> FAQ com múltiplos accordions

```python
from pytohtml import accordion, paragrafo, coluna

coluna(
    accordion(
        "O que é pytohtml?",
        paragrafo("Uma biblioteca Python para gerar HTML com Tailwind CSS, sem escrever HTML manualmente.")
    ),
    accordion(
        "Preciso instalar alguma dependência?",
        paragrafo("Não. A lib usa Python padrão e carrega Tailwind CSS e SweetAlert2 via CDN automaticamente.")
    ),
    accordion(
        "Posso usar em produção?",
        paragrafo("Sim. A lib gera arquivos HTML estáticos que podem ser servidos por qualquer servidor web.")
    ),
    centralizado=False, distanciamento=0,
)
```

> 💡 **Dica:** O ícone `▼` no cabeçalho rotaciona automaticamente ao expandir (`group-open:rotate-180`) usando apenas CSS, sem JavaScript.

---

### 🟡 Nível 3 — Difícil

> Accordion com conteúdo rico (tabela, lista e código)

```python
from pytohtml import accordion, tabela, lista, codigo

accordion(
    "Referência rápida dos parâmetros",
    tabela([
        ["Parâmetro", "Tipo",   "Padrão",  "Descrição"],
        ["titulo_aba","str",    "—",       "Texto clicável"],
        ["*conteudo", "str",    "—",       "Elementos filhos"],
        ["classes",   "str|None","None",   "Classes extras"],
    ]),
)

accordion(
    "Tipos de skeleton disponíveis",
    lista("texto — linhas de texto", "imagem — bloco retangular", "avatar — círculo"),
)

accordion(
    "Exemplo de código",
    codigo('accordion("Título", paragrafo("Conteúdo"))', bloco=True),
)
```

---

### 🟣 Nível 4 — Profissional

> Accordion em sidebar de documentação

```python
from pytohtml import html, coluna, accordion, lista, link

sidebar = coluna(
    accordion(
        "Fundamentos Visuais",
        lista(
            link("titulo()",    href="/wiki/titulo"),
            link("paragrafo()", href="/wiki/paragrafo"),
            link("botao()",     href="/wiki/botao"),
        ),
    ),
    accordion(
        "Layout Composto",
        lista(
            link("linha() / coluna()", href="/wiki/linha-e-coluna"),
            link("grade()",            href="/wiki/grade"),
            link("container()",        href="/wiki/container"),
        ),
    ),
    centralizado=False, distanciamento=0,
    classes="w-64 border-r border-gray-200 p-4",
)
```

---

## Referência Rápida

| Comportamento | Detalhes |
|--------------|---------|
| Estado padrão | Fechado |
| Animação do ícone | `▼` rotaciona 180° via `group-open:rotate-180` |
| Requer JavaScript | Não — usa `<details>` nativo do HTML5 |
| Múltiplos abertos ao mesmo tempo | Sim (comportamento padrão do `<details>`) |

---

← [animacao-carregando](animacao-carregando) · **accordion** · [rotulo-e-entrada →](rotulo-e-entrada)
