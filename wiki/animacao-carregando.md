# `animacao_carregando()`

> Gera um efeito skeleton loading — placeholder animado exibido enquanto o conteúdo real está sendo carregado.

`elementos.py` · `feedback`

---

## Assinatura

```python
animacao_carregando(tipo: str = "texto", linhas: int = 1, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `tipo` | `str` | `"texto"` | Formato do skeleton — `"texto"`, `"imagem"`, `"avatar"` |
| `linhas` | `int` | `1` | Número de linhas (só usado quando `tipo="texto"`) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Skeleton de texto simples

```python
from pytohtml import animacao_carregando

animacao_carregando()
```

**HTML gerado:**

```html
<div class="space-y-2">
  <div class="animate-pulse bg-gray-200 rounded h-4 w-full"></div>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Todos os tipos de skeleton

```python
from pytohtml import coluna, animacao_carregando

coluna(
    # Parágrafo com 3 linhas (última mais curta, simula texto real)
    animacao_carregando(tipo="texto", linhas=3),

    # Placeholder de imagem
    animacao_carregando(tipo="imagem"),

    # Placeholder de avatar circular
    animacao_carregando(tipo="avatar"),

    centralizado=False, distanciamento=4,
)
```

> 💡 **Dica:** Quando `tipo="texto"` e `linhas > 1`, a última linha fica com `w-3/4` para simular o fim natural de um parágrafo de texto.

---

### 🟡 Nível 3 — Difícil

> Card de carregamento completo (avatar + nome + texto)

```python
from pytohtml import cartao, linha, coluna, animacao_carregando

cartao(
    linha(
        animacao_carregando(tipo="avatar"),
        coluna(
            animacao_carregando(tipo="texto", linhas=1, classes="w-32"),
            animacao_carregando(tipo="texto", linhas=1, classes="w-24"),
            centralizado=False, distanciamento=2,
        ),
        centralizado=False, distanciamento=3,
    ),
    animacao_carregando(tipo="imagem"),
    animacao_carregando(tipo="texto", linhas=3),
    classes="max-w-sm",
)
```

---

### 🟣 Nível 4 — Profissional

> Skeleton substituído por conteúdo real via Brython

```python
from pytohtml import html, cartao, animacao_carregando, espaco_dinamico, buscar_dados

pagina = html(
    cartao(
        # Exibe o skeleton inicialmente
        espaco_dinamico("perfil", "space-y-3"),
        animacao_carregando(tipo="avatar"),
        animacao_carregando(tipo="texto", linhas=2),
    ),
    # Quando os dados chegarem, substitui o conteúdo do #perfil
    buscar_dados(
        "https://dummyjson.com/users/1",
        seletor_resultado="#perfil",
    ),
    titulo_pagina="Perfil",
    brython=True,
)
```

---

## Referência Rápida

| `tipo=` | Formato | Dimensões |
|---------|---------|-----------|
| `"texto"` | Linha(s) horizontais | `h-4 w-full` (última `w-3/4` se >1 linha) |
| `"imagem"` | Retângulo | `w-full h-48` |
| `"avatar"` | Círculo | `w-12 h-12` |

---

← [codigo](codigo) · **animacao-carregando** · [accordion →](accordion)
