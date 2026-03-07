# `avatar()`

> Imagem de perfil circular. Exibe a foto se `src` for fornecido, ou as iniciais do nome caso contrário.

`elementos.py` · `mídia`

---

## Assinatura

```python
avatar(src: str = "", tamanho: int = 12, alt: str = "Avatar", iniciais: str = "", classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `src` | `str` | `""` | URL da foto de perfil (opcional) |
| `tamanho` | `int` | `12` | Tamanho em unidades Tailwind (`w-N h-N`). Recomendados: 8, 10, 12, 16 |
| `alt` | `str` | `"Avatar"` | Texto alternativo da imagem |
| `iniciais` | `str` | `""` | Texto exibido quando `src` está vazio (ex: `"GU"`) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Avatar com iniciais (sem foto)

```python
from pytohtml import avatar

avatar(iniciais="GU")
```

**HTML gerado:**

```html
<div class="inline-flex items-center justify-center relative rounded-full overflow-hidden bg-gray-200 border border-gray-300 w-12 h-12 shrink-0">
  <span class="font-medium text-gray-600 uppercase">GU</span>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Avatar com foto e diferentes tamanhos

```python
# Avatar com foto real
avatar("https://i.pravatar.cc/150?img=3", alt="Ana Silva", tamanho=16)

# Avatar grande com iniciais
avatar(iniciais="JS", tamanho=20)

# Avatar pequeno (tipo lista de usuários)
avatar(iniciais="MK", tamanho=8)
```

> 💡 **Dica:** Tamanhos Tailwind recomendados: `8` (32px), `10` (40px), `12` (48px — padrão), `16` (64px), `20` (80px). Para tamanhos não padrão do Tailwind, use `classes="w-[56px] h-[56px]"`.

---

### 🟡 Nível 3 — Difícil

> Lista de usuários com avatar, nome e status

```python
from pytohtml import coluna, linha, avatar, titulo, paragrafo, etiqueta

def card_usuario(foto, nome, cargo, status):
    return linha(
        avatar(foto, alt=nome, tamanho=12),
        coluna(
            titulo(nome, tamanho="pequeno"),
            paragrafo(cargo, classes="text-xs text-gray-400 -mt-2"),
            centralizado=False, distanciamento=0,
        ),
        etiqueta(status, cor="verde" if status == "Online" else "cinza"),
        centralizado=False, distanciamento=3,
        classes="w-full justify-between",
    )

coluna(
    card_usuario("https://i.pravatar.cc/150?img=1", "Ana Silva",  "Dev Python",   "Online"),
    card_usuario("",                                 "João Costa", "Designer",     "Offline"),
    card_usuario("https://i.pravatar.cc/150?img=5", "Maria Lima", "Product Owner","Online"),
    centralizado=False, distanciamento=3,
)
```

---

### 🟣 Nível 4 — Profissional

> Grupo de avatares sobrepostos (stack de usuários)

```python
from pytohtml import html

avatares = [
    "https://i.pravatar.cc/150?img=1",
    "https://i.pravatar.cc/150?img=2",
    "https://i.pravatar.cc/150?img=3",
    "https://i.pravatar.cc/150?img=4",
]

# Stack com HTML puro (sobreposição não é suportada nativamente pela lib)
imgs_html = "".join(
    f'<img src="{src}" class="w-10 h-10 rounded-full border-2 border-white -ml-2 first:ml-0 object-cover" />'
    for src in avatares
)
stack = f'<div class="flex items-center">{imgs_html}<span class="ml-2 text-sm text-gray-500">+12 membros</span></div>'

pagina = html(stack, titulo_pagina="Time")
```

---

## Referência Rápida

| Tamanho Tailwind | Pixels | Uso típico |
|-----------------|--------|------------|
| `tamanho=8` | 32px | Lista compacta |
| `tamanho=10` | 40px | Comentários |
| `tamanho=12` | 48px | Padrão — cards de usuário |
| `tamanho=16` | 64px | Perfil em destaque |
| `tamanho=20` | 80px | Página de perfil |

---

← [imagem](imagem) · **avatar** · [codigo →](codigo)
