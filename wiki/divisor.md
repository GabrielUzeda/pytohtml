# `divisor()`

> Gera uma linha horizontal de separação (`<hr>`) para dividir seções de conteúdo.

`elementos.py` · `layout`

---

## Assinatura

```python
divisor(classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `classes` | `str \| None` | `None` | Classes Tailwind extras para customizar a linha |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Divisor padrão entre dois blocos de conteúdo

```python
from pytohtml import paragrafo, divisor

paragrafo("Primeiro bloco de conteúdo.")
divisor()
paragrafo("Segundo bloco de conteúdo.")
```

**HTML gerado:**

```html
<hr class="border-0 border-t border-gray-200 my-6" />
```

---

### 🔵 Nível 2 — Intermediário

> Divisores com espaçamentos diferentes

```python
# Mais espaço acima e abaixo
divisor(classes="my-12")

# Menos espaço
divisor(classes="my-2")

# Linha mais escura
divisor(classes="border-gray-400")
```

> 💡 **Dica:** O `my-6` (margem vertical de 1.5rem) já vem por padrão. Para seções com muito conteúdo, `my-10` ou `my-12` dá mais respiro visual.

---

### 🟡 Nível 3 — Difícil

> Divisor com cor temática em um card

```python
from pytohtml import cartao, titulo, paragrafo, divisor

cartao(
    titulo("Seção A", tamanho="medio"),
    paragrafo("Conteúdo da primeira seção."),
    divisor(classes="border-blue-100 my-4"),
    titulo("Seção B", tamanho="medio"),
    paragrafo("Conteúdo da segunda seção."),
)
```

---

### 🟣 Nível 4 — Profissional

> Divisor com texto centralizado (usando HTML puro via `head_extra` ou como string direta)

```python
from pytohtml import coluna, divisor, paragrafo

# Usando divisores para criar uma timeline visual
coluna(
    paragrafo("Janeiro — Início do projeto"),
    divisor(classes="border-dashed border-blue-200 my-3"),
    paragrafo("Março — Primeira versão publicada"),
    divisor(classes="border-dashed border-blue-200 my-3"),
    paragrafo("Junho — Lançamento oficial"),
    centralizado=False, distanciamento=0,
)
```

---

## Referência Rápida

| Classe extra | Efeito |
|--------------|--------|
| `my-2` | Margem vertical pequena |
| `my-6` | Margem vertical padrão (já incluída) |
| `my-12` | Margem vertical generosa |
| `border-gray-400` | Linha mais escura |
| `border-blue-200` | Linha azul suave |
| `border-dashed` | Linha tracejada |

---

← [link](link) · **divisor** · [aviso-estatico →](aviso-estatico)
