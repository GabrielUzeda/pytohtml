# `etiqueta()`

> Gera uma badge/etiqueta colorida, usada para categorias, status e rótulos inline.

`elementos.py` · `visual`

---

## Assinatura

```python
etiqueta(texto: str, cor: str = "cinza", classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Texto da etiqueta (obrigatório) |
| `cor` | `str` | `"cinza"` | Paleta de cor — veja tabela de cores abaixo |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |
| `escapar` | `bool` | `True` | Escapa HTML para prevenir XSS |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Etiqueta cinza padrão

```python
from pytohtml import etiqueta

etiqueta("Novo")
```

**HTML gerado:**

```html
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-700">Novo</span>
```

---

### 🔵 Nível 2 — Intermediário

> Todas as cores disponíveis

```python
from pytohtml import linha, etiqueta

linha(
    etiqueta("Cinza",    cor="cinza"),
    etiqueta("Azul",     cor="azul"),
    etiqueta("Verde",    cor="verde"),
    etiqueta("Vermelho", cor="vermelho"),
    etiqueta("Amarelo",  cor="amarelo"),
    etiqueta("Roxo",     cor="roxo"),
)
```

> 💡 **Dica:** Use cores semanticamente — `"verde"` para status ativo/aprovado, `"vermelho"` para erros/bloqueado, `"amarelo"` para pendente/aviso, `"azul"` para informação.

---

### 🟡 Nível 3 — Difícil

> Combinando etiquetas com `cartao()` e `titulo()` para cards de produto

```python
from pytohtml import cartao, linha, titulo, paragrafo, etiqueta

cartao(
    linha(
        etiqueta("Em estoque", cor="verde"),
        etiqueta("Promoção",   cor="amarelo"),
        centralizado=False, distanciamento=2,
    ),
    titulo("Produto Premium", tamanho="medio"),
    paragrafo("Descrição resumida do produto com qualidade garantida."),
)
```

---

### 🟣 Nível 4 — Profissional

> Etiquetas como indicadores de módulo em documentação técnica

```python
from pytohtml import linha, etiqueta, titulo

# Cabeçalho de função documentada
linha(
    titulo("ao_clicar()", tamanho="grande", classes="mono"),
    linha(
        etiqueta("interatividade.py", cor="cinza",  classes="mono text-xs"),
        etiqueta("brython",           cor="azul",   classes="mono text-xs"),
        etiqueta("requer brython=True", cor="amarelo", classes="mono text-xs"),
        centralizado=True, distanciamento=2,
    ),
    centralizado=False, distanciamento=0,
    classes="w-full justify-between items-start",
)
```

---

## Referência Rápida

| `cor=` | Fundo | Texto | Uso típico |
|--------|-------|-------|------------|
| `"cinza"` | `bg-gray-100` | `text-gray-700` | Neutro, categoria |
| `"azul"` | `bg-blue-100` | `text-blue-700` | Informação, módulo |
| `"verde"` | `bg-green-100` | `text-green-700` | Sucesso, ativo |
| `"vermelho"` | `bg-red-100` | `text-red-700` | Erro, bloqueado |
| `"amarelo"` | `bg-yellow-100` | `text-yellow-700` | Aviso, pendente |
| `"roxo"` | `bg-purple-100` | `text-purple-700` | Destaque, especial |

---

← [botao](botao) · **etiqueta** · [link →](link)
