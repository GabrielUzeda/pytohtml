# `link()`

> Gera um link HTML estilizado com sublinhado azul e transição de cor ao passar o mouse.

`elementos.py` · `tipografia`

---

## Assinatura

```python
link(texto: str, href: str = "#", classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Texto visível do link (obrigatório) |
| `href` | `str` | `"#"` | URL de destino |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |
| `escapar` | `bool` | `True` | Escapa HTML para prevenir XSS |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Link simples com URL

```python
from pytohtml import link

link("Acesse a documentação", href="/docs")
```

**HTML gerado:**

```html
<a href="/docs" class="text-blue-600 hover:text-blue-800 underline underline-offset-2 transition-colors">Acesse a documentação</a>
```

---

### 🔵 Nível 2 — Intermediário

> Links com diferentes estilos e destinos

```python
# Link para URL externa
link("GitHub", href="https://github.com/GabrielUzeda/pytohtml")

# Link para âncora na mesma página
link("Ver exemplos", href="#exemplos")

# Link sem decoração de sublinhado
link("Voltar ao início", href="/", classes="no-underline text-gray-600 hover:text-blue-600")

# Link que abre em nova aba (via escapar=False com atributo target)
link(
    '<span>Abrir em nova aba ↗</span>',
    href="https://tailwindcss.com",
    escapar=False,
    classes="inline-flex items-center gap-1"
)
```

> 💡 **Dica:** Para links externos que devem abrir em nova aba, use `escapar=False` para inserir o atributo `target="_blank"` diretamente na string, ou use HTML bruto via `head_extra` ou `script_python`.

---

### 🟡 Nível 3 — Difícil

> Links em contexto de navegação e rodapé

```python
from pytohtml import nav, link, rodape, coluna, linha

# Barra de navegação
nav(
    link("Início",       href="/"),
    link("Sobre",        href="/sobre"),
    link("Documentação", href="/docs"),
    link("Contato",      href="/contato"),
)

# Rodapé com links sociais
rodape(
    coluna(
        linha(
            link("GitHub",   href="https://github.com", classes="text-gray-400 hover:text-white"),
            link("LinkedIn", href="https://linkedin.com", classes="text-gray-400 hover:text-white"),
            centralizado=True, distanciamento=4,
        ),
    )
)
```

---

### 🟣 Nível 4 — Profissional

> Link estilizado como botão (call-to-action em parágrafos)

```python
from pytohtml import paragrafo, link

# Inserindo link dentro de um parágrafo via escapar=False
texto = (
    'Para começar, leia o '
    + link("guia de instalação", href="/wiki/Instalacao", classes="font-semibold")
    + ' ou veja os '
    + link("exemplos completos", href="/wiki/Home", classes="font-semibold")
    + '.'
)

paragrafo(texto, escapar=False)
```

> ⚠️ **Atenção:** Ao usar `paragrafo(..., escapar=False)` com HTML gerado por outras funções da lib, o conteúdo já foi escapado internamente — não haverá dupla escapagem.

---

## Referência Rápida

| Classe extra | Efeito |
|--------------|--------|
| `no-underline` | Remove o sublinhado |
| `font-semibold` | Texto mais espesso |
| `text-gray-600` | Tom neutro ao invés de azul |
| `hover:text-white` | Muda cor no hover (para fundos escuros) |
| `transition-colors` | Já incluído por padrão |

---

← [etiqueta](etiqueta) · **link** · [divisor →](divisor)
