# `paragrafo()`

> Gera um parágrafo de texto simples com estilos de leitura confortáveis.

`elementos.py` · `tipografia`

---

## Assinatura

```python
paragrafo(texto: str, classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Conteúdo do parágrafo (obrigatório) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras para personalizar o estilo |
| `escapar` | `bool` | `True` | Escapa HTML para prevenir XSS (desative ao compor HTML) |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Uso mais básico — parágrafo com configuração padrão

```python
from pytohtml import paragrafo

paragrafo("Este é um parágrafo de exemplo.")
```

**HTML gerado:**

```html
<p class="text-base text-gray-600 leading-relaxed">Este é um parágrafo de exemplo.</p>
```

---

### 🔵 Nível 2 — Intermediário

> Variações de tamanho e cor com classes Tailwind

```python
paragrafo("Texto padrão — tom cinza suave para corpo de texto.")
paragrafo("Texto grande e escuro.", classes="text-lg text-gray-900")
paragrafo("Texto pequeno e discreto.", classes="text-sm text-gray-400")
paragrafo("Destaque em cor primária.", classes="text-blue-600 font-medium")
```

> 💡 **Dica:** `leading-relaxed` (espaçamento entre linhas confortável) já vem aplicado por padrão. Para textos densos, `leading-tight` pode ser mais adequado.

---

### 🟡 Nível 3 — Difícil

> Combinando com `cartao()` e `titulo()` para criar seções completas

```python
from pytohtml import cartao, titulo, paragrafo

cartao(
    titulo("Sobre o projeto", tamanho="medio"),
    paragrafo(
        "pytohtml é uma biblioteca Python pura para gerar HTML com Tailwind CSS.",
        classes="text-gray-500 mt-1"
    ),
    paragrafo(
        "Sem escrever HTML, CSS ou JavaScript — apenas chamadas de função Python.",
        classes="text-gray-500"
    ),
)
```

---

### 🟣 Nível 4 — Profissional

> Usando `escapar=False` para embutir HTML inline (links, negrito, destaque)

```python
texto_rico = (
    'Leia a <a href="/docs" class="text-blue-600 underline">documentação completa</a> '
    'ou veja os <strong>exemplos interativos</strong> para começar.'
)

paragrafo(texto_rico, escapar=False, classes="text-gray-600 leading-relaxed")
```

> ⚠️ **Atenção:** Com `escapar=False` o texto é inserido como HTML bruto. Nunca passe input do usuário diretamente — isso abre falha **XSS**. Use apenas com strings construídas no seu próprio código.

---

## Referência Rápida

| Classe extra | Efeito |
|--------------|--------|
| `text-sm` | Texto menor (0.875rem) |
| `text-lg` | Texto maior (1.125rem) |
| `text-gray-900` | Tom escuro para destaque |
| `text-gray-400` | Tom claro para informações secundárias |
| `font-medium` | Peso semibold |
| `text-center` | Centralizar |
| `max-w-prose` | Largura máxima ideal para leitura (~65ch) |

---

← [titulo](titulo) · **paragrafo** · [botao →](botao)
