# `grade()`

> Distribui elementos em uma grade CSS responsiva — 1 coluna no mobile, N colunas no desktop.

`layout.py` · `layout`

---

## Assinatura

```python
grade(*conteudo: str, colunas: int = 1, distanciamento: int = 4, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Elementos a distribuir na grade |
| `colunas` | `int` | `1` | Número de colunas no breakpoint `md` (≥768px) |
| `distanciamento` | `int` | `4` | Espaçamento entre células via `gap-N` |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Três cards em grade

```python
from pytohtml import grade, cartao, titulo, paragrafo

grade(
    cartao(titulo("Card 1", tamanho="medio"), paragrafo("Conteúdo do card 1.")),
    cartao(titulo("Card 2", tamanho="medio"), paragrafo("Conteúdo do card 2.")),
    cartao(titulo("Card 3", tamanho="medio"), paragrafo("Conteúdo do card 3.")),
    colunas=3,
)
```

**HTML gerado:**

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
  <div class="bg-white ...">...</div>
  <div class="bg-white ...">...</div>
  <div class="bg-white ...">...</div>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Grades com diferentes números de colunas

```python
from pytohtml import grade, cartao, titulo, etiqueta

# Grade de 2 colunas
grade(
    cartao(titulo("Funcionalidade A", tamanho="medio")),
    cartao(titulo("Funcionalidade B", tamanho="medio")),
    colunas=2,
)

# Grade de 4 colunas (estatísticas)
grade(
    cartao(titulo("42", tamanho="grande"), etiqueta("Commits", cor="azul")),
    cartao(titulo("8",  tamanho="grande"), etiqueta("Releases", cor="verde")),
    cartao(titulo("156", tamanho="grande"), etiqueta("Stars", cor="amarelo")),
    cartao(titulo("23", tamanho="grande"), etiqueta("Forks", cor="roxo")),
    colunas=4,
    distanciamento=3,
)
```

> 💡 **Dica:** `grid-cols-1` é sempre aplicado para mobile (telas menores que `md`). O breakpoint `md:grid-cols-N` entra em ação em telas ≥768px. Para controle fino por breakpoint, use `classes="grid-cols-1 sm:grid-cols-2 lg:grid-cols-4"`.

---

### 🟡 Nível 3 — Difícil

> Galeria de imagens responsiva

```python
from pytohtml import grade, imagem

urls = [f"https://picsum.photos/300/200?random={i}" for i in range(6)]

grade(
    *[imagem(url, alt=f"Foto {i+1}", classes="w-full h-40 object-cover") for i, url in enumerate(urls)],
    colunas=3,
    distanciamento=2,
    classes="rounded-xl overflow-hidden",
)
```

---

### 🟣 Nível 4 — Profissional

> Grid de pricing com destaque no plano central

```python
from pytohtml import grade, cartao, coluna, titulo, paragrafo, lista, botao, etiqueta

def card_plano(nome, preco, cor, recursos, destaque=False):
    cls = "ring-2 ring-blue-500 scale-105 shadow-xl" if destaque else ""
    return cartao(
        coluna(
            etiqueta(nome,   cor=cor),
            titulo(preco,    tamanho="gigante"),
            lista(*recursos),
            botao("Escolher", variante="primario" if destaque else "fantasma", classes="w-full mt-2"),
            centralizado=True, distanciamento=3,
        ),
        classes=cls,
    )

grade(
    card_plano("Free",       "R$ 0",   "cinza",   ["5 projetos", "1 GB storage",  "Suporte básico"]),
    card_plano("Pro",        "R$ 49",  "azul",    ["Ilimitado",  "50 GB storage", "Suporte prioritário"], destaque=True),
    card_plano("Enterprise", "Custom", "roxo",    ["Ilimitado",  "500 GB storage","SLA garantido"]),
    colunas=3,
    distanciamento=6,
)
```

---

## Referência Rápida

| `colunas=` | Classe gerada | Uso típico |
|------------|---------------|------------|
| `2` | `md:grid-cols-2` | Cards lado a lado |
| `3` | `md:grid-cols-3` | Galeria, features |
| `4` | `md:grid-cols-4` | Estatísticas, ícones |
| `6` | `md:grid-cols-6` | Logos, parceiros |

---

← [linha-e-coluna](linha-e-coluna) · **grade** · [container →](container)
