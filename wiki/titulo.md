# `titulo()`

> Gera títulos semânticos HTML — do `<h1>` ao `<h4>` com estilos automáticos via Tailwind.

`elementos.py` · `tipografia`

---

## Assinatura

```python
titulo(texto: str, tamanho: str = "grande", nivel: int | None = None, classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Conteúdo do título (obrigatório) |
| `tamanho` | `str` | `"grande"` | `"pequeno"` / `"medio"` / `"grande"` / `"gigante"` |
| `nivel` | `int \| None` | `None` | Legado: 1–4. Substituído por `tamanho` |
| `classes` | `str \| None` | `None` | Classes Tailwind extras para personalizar o estilo |
| `escapar` | `bool` | `True` | Escapa HTML para prevenir XSS (desative ao compor HTML) |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Uso mais básico — um título com configuração padrão

```python
from pytohtml import titulo

titulo("Olá, Mundo!")
```

**HTML gerado:**

```html
<h2 class="text-3xl font-semibold text-gray-800 leading-snug">Olá, Mundo!</h2>
```

---

### 🔵 Nível 2 — Intermediário

> Todos os tamanhos — construindo hierarquia visual

```python
titulo("Título Gigante", tamanho="gigante")
titulo("Título Grande",  tamanho="grande")
titulo("Título Médio",   tamanho="medio")
titulo("Título Pequeno", tamanho="pequeno")
```

**HTML gerado:**

```html
<h1 class="text-4xl font-bold text-gray-900 leading-tight">Título Gigante</h1>
<h2 class="text-3xl font-semibold text-gray-800 leading-snug">Título Grande</h2>
<h3 class="text-2xl font-semibold text-gray-800">Título Médio</h3>
<h4 class="text-xl font-medium text-gray-700">Título Pequeno</h4>
```

> 💡 **Dica:** Cada tamanho gera uma tag semântica diferente: `gigante→h1`, `grande→h2`, `medio→h3`, `pequeno→h4`. Isso é importante para SEO e acessibilidade.

---

### 🟡 Nível 3 — Difícil

> Personalizando com classes Tailwind extras

```python
# Título com gradiente via classes Tailwind
titulo(
    "Design Moderno",
    tamanho="gigante",
    classes="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-purple-600"
)

# Título centralizado com cor customizada
titulo(
    "Seção de Destaque",
    tamanho="medio",
    classes="text-center text-indigo-700"
)
```

---

### 🟣 Nível 4 — Profissional

> Usando `escapar=False` para embutir HTML confiável no título

```python
# escapar=False permite embutir HTML confiável no título
# Útil para ícones SVG, spans coloridos ou formatação inline

icone_python = '<img src="https://www.python.org/static/favicon.ico" class="inline w-8 h-8 mr-2 align-middle" />'

titulo(
    icone_python + "Bem-vindo ao pytohtml",
    tamanho="gigante",
    escapar=False,
)

# Parte do texto em destaque com span colorido
texto_misto = 'Python <span class="text-blue-600">puro</span> e simples'

titulo(
    texto_misto,
    tamanho="medio",
    escapar=False,
)
```

> ⚠️ **Atenção:** Com `escapar=False` o texto é inserido como HTML bruto — nunca passe texto vindo do usuário assim, pois isso abre falha **XSS**. Use apenas com strings que você mesmo construiu no Python.

---

## Referência Rápida

| `tamanho=` | Tag HTML | Uso típico | Fonte gerada |
|------------|----------|------------|--------------|
| `"gigante"` | `<h1>` | Hero, título da página | `text-4xl font-bold` |
| `"grande"` | `<h2>` | Seções principais | `text-3xl font-semibold` |
| `"medio"` | `<h3>` | Subseções, cards | `text-2xl font-semibold` |
| `"pequeno"` | `<h4>` | Rótulos, subtítulos | `text-xl font-medium` |

---

← [Início](Home) · **titulo** · [paragrafo →](paragrafo)
