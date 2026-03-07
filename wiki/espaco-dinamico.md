# `espaco_dinamico()`

> Cria um `<div>` vazio com um `id` específico, pronto para receber conteúdo dinâmico via Brython.

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
espaco_dinamico(id_elemento: str, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `id_elemento` | `str` | — | Atributo `id` do `<div>` (obrigatório) |
| `classes` | `str \| None` | `None` | Classes Tailwind para estilizar o container |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Container vazio que receberá conteúdo dinâmico

```python
from pytohtml import html, espaco_dinamico, ao_clicar, botao

pagina = html(
    espaco_dinamico("mensagem", "mt-4 p-4 bg-green-50 rounded-lg"),
    botao("Carregar mensagem", classes='id="btn"'),
    ao_clicar("#btn", '''
        from browser import document
        document["mensagem"].html = "<strong>Conteúdo carregado!</strong>"
    '''),
    titulo_pagina="Espaço Dinâmico",
    brython=True,
)
```

**HTML gerado:**

```html
<div id="mensagem" class="mt-4 p-4 bg-green-50 rounded-lg"></div>
```

---

### 🔵 Nível 2 — Intermediário

> Múltiplos espaços dinâmicos para diferentes dados

```python
from pytohtml import html, grade, cartao, espaco_dinamico, buscar_dados

pagina = html(
    grade(
        cartao(
            espaco_dinamico("dados-usuario", "space-y-2"),
        ),
        cartao(
            espaco_dinamico("dados-post", "space-y-2"),
        ),
        colunas=2,
    ),
    buscar_dados("https://dummyjson.com/users/1", seletor_resultado="#dados-usuario"),
    buscar_dados("https://dummyjson.com/posts/1",  seletor_resultado="#dados-post"),
    titulo_pagina="Dashboard",
    brython=True,
)
```

> 💡 **Dica:** `espaco_dinamico()` é sempre usado em conjunto com `buscar_dados()`, `inserir_html()`, `ao_clicar()` ou `ao_carregar()`. O `id` é a ponte entre o elemento HTML e o script Brython.

---

### 🟡 Nível 3 — Difícil

> Espaço dinâmico como área de lista atualizada em tempo real

```python
from pytohtml import html, coluna, linha, entrada, botao, espaco_dinamico, script_python

pagina = html(
    coluna(
        linha(
            entrada(nome="novo-item", placeholder="Novo item...", classes='id="input-item"'),
            botao("Adicionar", variante="primario", classes='id="btn-add"'),
            centralizado=False, distanciamento=2,
        ),
        espaco_dinamico("lista-itens", "mt-4 space-y-2"),
    ),
    script_python('''
        from browser import document

        itens = []

        def adicionar(ev):
            inp = document["input-item"]
            texto = inp.value.strip()
            if texto:
                itens.append(texto)
                inp.value = ""
                renderizar()

        def renderizar():
            html_itens = "".join(
                f'<div class="p-3 bg-white border border-gray-200 rounded-lg flex justify-between">'
                f'{item}<span class="text-gray-400 text-sm">#{i+1}</span></div>'
                for i, item in enumerate(itens)
            )
            document["lista-itens"].html = html_itens or "<p class='text-gray-400 text-sm'>Nenhum item adicionado.</p>"

        document["btn-add"].bind("click", adicionar)
        renderizar()
    '''),
    titulo_pagina="Lista Dinâmica",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Espaço com skeleton de carregamento integrado

```python
from pytohtml import html, espaco_dinamico, animacao_carregando, buscar_dados

SKELETON = animacao_carregando(tipo="texto", linhas=4)

pagina = html(
    # Exibe skeleton enquanto os dados não chegam
    espaco_dinamico("conteudo", "space-y-3") + SKELETON,
    buscar_dados(
        "https://dummyjson.com/posts/1",
        seletor_resultado="#conteudo",
    ),
    titulo_pagina="Carregando...",
    brython=True,
)
```

---

← [script-python](script-python) · **espaco-dinamico** · [inserir-html →](inserir-html)
