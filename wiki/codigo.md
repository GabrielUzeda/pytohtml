# `codigo()`

> Exibe código inline ou em bloco com estilo monospace e fundo destacado.

`elementos.py` · `tipografia`

---

## Assinatura

```python
codigo(texto: str, bloco: bool = False, classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Código a ser exibido (obrigatório) |
| `bloco` | `bool` | `False` | Se `True`, usa `<pre><code>` (bloco); se `False`, usa `<code>` inline |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |
| `escapar` | `bool` | `True` | Escapa HTML para prevenir XSS (importante para código) |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Código inline dentro de um parágrafo

```python
from pytohtml import paragrafo, codigo

paragrafo(
    "Use a função " + codigo("titulo()") + " para criar títulos.",
    escapar=False,
)
```

**HTML gerado (`codigo()`):**

```html
<code class="bg-gray-100 text-pink-600 rounded px-1.5 py-0.5 text-sm font-mono">titulo()</code>
```

---

### 🔵 Nível 2 — Intermediário

> Bloco de código multilinha

```python
codigo('''from pytohtml import *

pagina = html(
    titulo("Olá, Mundo!"),
    paragrafo("Bem-vindo!"),
    titulo_pagina="Meu Site"
)
salvar("index.html", pagina)''', bloco=True)
```

**HTML gerado (`bloco=True`):**

```html
<pre class="bg-gray-900 text-green-400 rounded-lg p-4 overflow-x-auto text-sm font-mono block"><code>...</code></pre>
```

> 💡 **Dica:** `bloco=True` usa fundo escuro (`bg-gray-900`) com texto verde (`text-green-400`), estilo terminal. `bloco=False` usa fundo cinza claro com texto rosa, ideal para referências inline em texto.

---

### 🟡 Nível 3 — Difícil

> Bloco de código dentro de card de documentação

```python
from pytohtml import cartao, titulo, paragrafo, codigo, divisor

cartao(
    titulo("Exemplo de uso", tamanho="pequeno"),
    paragrafo(
        "Chame " + codigo("botao()") + " com o parâmetro " + codigo('variante="sucesso"') + " para obter um botão verde.",
        escapar=False,
    ),
    divisor(classes="my-3"),
    codigo('botao("Salvar", variante="sucesso")', bloco=True),
)
```

---

### 🟣 Nível 4 — Profissional

> Bloco de código com destaque customizado via `classes`

```python
# Fundo azul escuro em vez do padrão cinza/preto
codigo(
    'SELECT * FROM usuarios WHERE ativo = TRUE;',
    bloco=True,
    classes="bg-blue-950 text-cyan-300 border border-blue-800"
)

# Código inline de erro em vermelho
codigo("NullPointerException", classes="bg-red-50 text-red-600 border border-red-200")
```

> ⚠️ **Atenção:** `escapar=True` (padrão) é especialmente importante para `codigo()` — código-fonte costuma ter `<`, `>` e `&` que precisam ser escapados corretamente para renderizar no HTML.

---

## Referência Rápida

| Modo | Tag HTML | Fundo | Texto | Uso |
|------|----------|-------|-------|-----|
| `bloco=False` (padrão) | `<code>` | `bg-gray-100` | `text-pink-600` | Referência inline |
| `bloco=True` | `<pre><code>` | `bg-gray-900` | `text-green-400` | Blocos de código |

---

← [avatar](avatar) · **codigo** · [animacao-carregando →](animacao-carregando)
