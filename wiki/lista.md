# `lista()`

> Gera uma lista de itens estilizada — não ordenada (`<ul>`) ou ordenada (`<ol>`).

`elementos.py` · `tipografia`

---

## Assinatura

```python
lista(*itens: str, ordenada: bool = False, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*itens` | `str` | — | Textos ou HTML de cada item da lista (ao menos 1) |
| `ordenada` | `bool` | `False` | Se `True`, usa `<ol>` (numerada); se `False`, usa `<ul>` (com marcador) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Lista simples com marcadores

```python
from pytohtml import lista

lista("Maçã", "Banana", "Laranja")
```

**HTML gerado:**

```html
<ul class="list-disc list-inside space-y-1 text-gray-600 text-base">
  <li class="leading-relaxed">Maçã</li>
  <li class="leading-relaxed">Banana</li>
  <li class="leading-relaxed">Laranja</li>
</ul>
```

---

### 🔵 Nível 2 — Intermediário

> Lista numerada de passos

```python
lista(
    "Instale o Python 3.10 ou superior",
    "Copie a pasta pytohtml/ para seu projeto",
    "Importe com: from pytohtml import *",
    "Gere sua primeira página com html() e salvar()",
    ordenada=True,
)
```

> 💡 **Dica:** Use `ordenada=True` para tutoriais, passos de instalação ou rankings. Use `ordenada=False` (padrão) para listas de características, opções ou ingredientes.

---

### 🟡 Nível 3 — Difícil

> Lista dentro de um card de funcionalidades

```python
from pytohtml import cartao, titulo, lista

cartao(
    titulo("Funcionalidades", tamanho="medio"),
    lista(
        "Geração de HTML com Python puro",
        "Tailwind CSS via CDN, sem configuração",
        "Interatividade com Brython (Python no browser)",
        "Popups elegantes com SweetAlert2",
        "Componentes reutilizáveis prontos",
        classes="mt-2",
    ),
)
```

---

### 🟣 Nível 4 — Profissional

> Lista com HTML inline nos itens (links, badges, negrito)

```python
from pytohtml import lista, link, etiqueta

lista(
    etiqueta("Python 3.10+", cor="azul") + " — interpretador principal",
    etiqueta("Tailwind CSS",  cor="roxo") + " — via CDN, sem instalação",
    etiqueta("SweetAlert2",   cor="verde") + " — popups e notificações",
    etiqueta("Brython",       cor="amarelo") + " — Python no browser (opcional)",
)
```

> ⚠️ **Atenção:** Ao passar HTML nos itens, certifique-se de que o conteúdo é confiável. Os itens passados como `*itens` são inseridos diretamente sem escapamento adicional.

---

## Referência Rápida

| Parâmetro / Classe | Efeito |
|--------------------|--------|
| `ordenada=False` | `<ul>` com marcadores redondos (padrão) |
| `ordenada=True` | `<ol>` com números |
| `classes="text-sm"` | Itens com fonte menor |
| `classes="space-y-3"` | Mais espaço entre os itens |
| `classes="text-gray-400"` | Cor mais suave |

---

← [cartao](cartao) · **lista** · [tabela →](tabela)
