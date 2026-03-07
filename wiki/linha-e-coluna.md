# `linha()` e `coluna()`

> Organizam elementos em flex — `linha()` na horizontal e `coluna()` na vertical.

`layout.py` · `layout`

---

## Assinaturas

```python
linha(
    *conteudo: str,
    centralizado: bool = True,
    distanciamento: int = 4,
    classes: str | None = None,
) → str

coluna(
    *conteudo: str,
    centralizado: bool = True,
    distanciamento: int = 4,
    classes: str | None = None,
) → str
```

## Parâmetros (iguais em ambas)

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Elementos filhos a organizar |
| `centralizado` | `bool` | `True` | Se `True`, aplica `items-center justify-center` |
| `distanciamento` | `int` | `4` | Espaçamento entre filhos via `gap-N` do Tailwind |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Dois botões lado a lado

```python
from pytohtml import linha, botao

linha(
    botao("Confirmar", variante="primario"),
    botao("Cancelar",  variante="secundario"),
)
```

**HTML gerado:**

```html
<div class="flex flex-row gap-4 items-center justify-center">
  <button ...>Confirmar</button>
  <button ...>Cancelar</button>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Diferença entre `linha()` e `coluna()`, e ajuste de distanciamento

```python
from pytohtml import linha, coluna, etiqueta

# Horizontal (padrão: centralizado, gap-4)
linha(
    etiqueta("Python", cor="azul"),
    etiqueta("Tailwind", cor="roxo"),
    etiqueta("Brython", cor="amarelo"),
)

# Vertical
coluna(
    etiqueta("Passo 1", cor="verde"),
    etiqueta("Passo 2", cor="azul"),
    etiqueta("Passo 3", cor="roxo"),
    distanciamento=2,
)

# Linha não centralizada (alinhamento à esquerda)
linha(
    botao("Anterior", variante="fantasma"),
    botao("Próximo",  variante="primario"),
    centralizado=False,
    classes="justify-between w-full",
)
```

> 💡 **Dica:** `distanciamento` aceita os valores de `gap` do Tailwind: 0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24... Para distanciamentos personalizados, use `classes="gap-7"`.

---

### 🟡 Nível 3 — Difícil

> Layout de card de usuário com linha e coluna aninhados

```python
from pytohtml import linha, coluna, avatar, titulo, paragrafo, etiqueta, botao

linha(
    avatar(iniciais="GU", tamanho=14),
    coluna(
        linha(
            titulo("Gabriel Uzeda", tamanho="pequeno"),
            etiqueta("Pro", cor="azul"),
            centralizado=False, distanciamento=2,
        ),
        paragrafo("Desenvolvedor Python & UI", classes="text-sm text-gray-400 -mt-2"),
        centralizado=False, distanciamento=1,
    ),
    botao("Seguir", variante="primario", classes="ml-auto text-xs py-1"),
    centralizado=False, distanciamento=3,
    classes="w-full items-center",
)
```

---

### 🟣 Nível 4 — Profissional

> Layout de página completo com sidebar + conteúdo principal

```python
from pytohtml import html, linha, coluna, titulo, paragrafo, lista, link

sidebar = coluna(
    titulo("Navegação", tamanho="pequeno"),
    lista(
        link("Início",        href="/"),
        link("Documentação",  href="/docs"),
        link("Exemplos",      href="/exemplos"),
    ),
    centralizado=False, distanciamento=3,
    classes="w-64 min-h-screen bg-white border-r border-gray-200 p-6",
)

conteudo = coluna(
    titulo("Bem-vindo ao pytohtml"),
    paragrafo("Selecione um item no menu lateral para começar."),
    centralizado=False, distanciamento=4,
    classes="flex-1 p-8",
)

pagina = html(
    linha(sidebar, conteudo, centralizado=False, distanciamento=0, classes="min-h-screen"),
    titulo_pagina="pytohtml"
)
```

---

## Referência Rápida

| Função | Flex direction | Uso típico |
|--------|---------------|------------|
| `linha()` | `flex-row` | Botões lado a lado, navbar, header |
| `coluna()` | `flex-col` | Formulários, cards, sidebar |

| `distanciamento=` | Gap Tailwind |
|------------------|-------------|
| `0` | `gap-0` |
| `2` | `gap-2` (8px) |
| `4` | `gap-4` (16px) — padrão |
| `6` | `gap-6` (24px) |
| `8` | `gap-8` (32px) |

---

← [formulario](formulario) · **linha e coluna** · [grade →](grade)
