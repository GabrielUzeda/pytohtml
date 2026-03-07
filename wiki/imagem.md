# `imagem()`

> Gera uma tag `<img>` responsiva, opcionalmente com bordas arredondadas.

`elementos.py` · `mídia`

---

## Assinatura

```python
imagem(src: str, alt: str = "", arredondada: bool = True, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `src` | `str` | — | Caminho ou URL da imagem (obrigatório) |
| `alt` | `str` | `""` | Texto alternativo para acessibilidade |
| `arredondada` | `bool` | `True` | Aplica `rounded-xl` nas bordas |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Imagem simples com URL e texto alternativo

```python
from pytohtml import imagem

imagem("https://picsum.photos/400/200", alt="Imagem de exemplo")
```

**HTML gerado:**

```html
<img src="https://picsum.photos/400/200" alt="Imagem de exemplo" class="max-w-full h-auto rounded-xl" />
```

---

### 🔵 Nível 2 — Intermediário

> Imagem sem arredondamento e com dimensões fixas

```python
# Imagem quadrada sem arredondamento (ex: logo)
imagem(
    "https://www.python.org/static/favicon.ico",
    alt="Logo Python",
    arredondada=False,
    classes="w-12 h-12"
)

# Imagem em largura total com altura fixa (banner)
imagem(
    "https://picsum.photos/1200/400",
    alt="Banner do site",
    classes="w-full h-48 object-cover"
)
```

> 💡 **Dica:** `max-w-full h-auto` já vem por padrão, garantindo que a imagem nunca ultrapasse o container pai. Para alturas fixas, adicione `object-cover` para evitar distorção.

---

### 🟡 Nível 3 — Difícil

> Galeria de imagens em grade responsiva

```python
from pytohtml import grade, imagem

fotos = [
    "https://picsum.photos/400/300?random=1",
    "https://picsum.photos/400/300?random=2",
    "https://picsum.photos/400/300?random=3",
    "https://picsum.photos/400/300?random=4",
    "https://picsum.photos/400/300?random=5",
    "https://picsum.photos/400/300?random=6",
]

grade(
    *[imagem(src, alt=f"Foto {i+1}", classes="w-full h-48 object-cover") for i, src in enumerate(fotos)],
    colunas=3,
    distanciamento=3,
)
```

---

### 🟣 Nível 4 — Profissional

> Imagem com overlay de texto (hero com imagem de fundo)

```python
from pytohtml import html, titulo, paragrafo, botao

# Seção hero com imagem de fundo via CSS inline
hero_html = '''
<div style="background-image: url('https://picsum.photos/1200/600');
            background-size: cover; background-position: center;
            padding: 6rem 2rem; text-align: center; position: relative;">
  <div style="background: rgba(0,0,0,0.5); position: absolute; inset: 0;"></div>
  <div style="position: relative; color: white;">
    {titulo}
    {subtitulo}
    {cta}
  </div>
</div>
'''.format(
    titulo=titulo("Bem-vindo ao pytohtml", tamanho="gigante", classes="text-white"),
    subtitulo=paragrafo("Gere HTML com Python puro.", classes="text-gray-200 text-xl"),
    cta=botao("Começar agora", variante="sucesso", classes="mt-4"),
)

pagina = html(hero_html, titulo_pagina="Landing Page")
```

---

## Referência Rápida

| Classe extra | Efeito |
|--------------|--------|
| `arredondada=True` | `rounded-xl` (padrão) |
| `arredondada=False` | Sem arredondamento |
| `w-full` | Largura total do container |
| `h-48 object-cover` | Altura fixa sem distorção |
| `shadow-lg` | Sombra para elevação |
| `border border-gray-200` | Borda sutil |

---

← [tabela](tabela) · **imagem** · [avatar →](avatar)
