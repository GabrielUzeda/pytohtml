# `ao_clicar()`

> Vincula um handler de clique a um elemento do DOM via seletor CSS, usando Brython (Python no browser).

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
ao_clicar(seletor: str, codigo: str) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `seletor` | `str` | — | Seletor CSS do elemento alvo (ex: `"#meu-botao"`, `".classe"`) |
| `codigo` | `str` | — | Corpo do handler Python — recebe `ev` como argumento do evento |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Alerta ao clicar em um botão

```python
from pytohtml import html, botao, ao_clicar

pagina = html(
    botao("Clique aqui", classes='id="btn-ola"'),
    ao_clicar("#btn-ola", '''
        from browser import alert
        alert("Olá do Brython!")
    '''),
    titulo_pagina="Clique",
    brython=True,
)
```

**Script gerado:**

```html
<script type="text/python">
from browser import document

def _handler(ev):
    from browser import alert
    alert("Olá do Brython!")

document.select("#btn-ola")[0].bind("click", _handler)
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Modificar o DOM ao clicar

```python
from pytohtml import html, botao, espaco_dinamico, ao_clicar

pagina = html(
    espaco_dinamico("resultado", "mt-4 p-4 bg-blue-50 rounded-lg hidden"),
    botao("Mostrar mensagem", variante="primario", classes='id="btn-mostrar"'),
    ao_clicar("#btn-mostrar", '''
        from browser import document
        el = document["resultado"]
        el.html = "<strong>Mensagem exibida com sucesso!</strong>"
        el.classList.remove("hidden")
    '''),
    titulo_pagina="DOM",
    brython=True,
)
```

> 💡 **Dica:** Dentro do handler Brython, use `from browser import document` para acessar o DOM. `document["id"]` retorna o elemento diretamente pelo ID (sem o `#`). Para seletores CSS, use `document.select(".classe")[0]`.

---

### 🟡 Nível 3 — Difícil

> Contador com estado e atualização do DOM

```python
from pytohtml import html, coluna, linha, botao, espaco_dinamico, ao_clicar, estado

pagina = html(
    coluna(
        espaco_dinamico("contador", "text-4xl font-bold text-blue-600 text-center"),
        linha(
            botao("−", variante="secundario", classes='id="btn-dec" text-xl px-6'),
            botao("+", variante="primario",   classes='id="btn-inc" text-xl px-6'),
        ),
    ),
    estado("contador", "0", "#contador"),
    ao_clicar("#btn-inc", '''
        n = int(_estado["contador"])
        set_estado("contador", n + 1)
    '''),
    ao_clicar("#btn-dec", '''
        n = int(_estado["contador"])
        set_estado("contador", n - 1)
    '''),
    titulo_pagina="Contador",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Toggle de tema claro/escuro

```python
from pytohtml import html, botao, ao_clicar

pagina = html(
    botao("Alternar tema", variante="fantasma", classes='id="btn-tema"'),
    ao_clicar("#btn-tema", '''
        from browser import document
        body = document.select("body")[0]
        if "dark" in body.classList:
            body.classList.remove("dark")
            body.style.background = "#f9fafb"
            body.style.color = "#111827"
        else:
            body.classList.add("dark")
            body.style.background = "#111827"
            body.style.color = "#f9fafb"
    '''),
    titulo_pagina="Tema",
    brython=True,
)
```

---

## Referência Rápida

| Padrão de seletor | Exemplo |
|-------------------|---------|
| Por ID | `"#meu-botao"` |
| Por classe | `".minha-classe"` |
| Por tag | `"button"` |
| Por atributo | `'[data-action="confirmar"]'` |

> ⚠️ **Atenção:** Para adicionar `id` a um elemento gerado pela lib, use o parâmetro `classes` com HTML de atributo: `classes='id="meu-id"'`. Isso funciona porque `classes` é inserido diretamente nos atributos do elemento.

---

← [modal](modal) · **ao-clicar** · [ao-carregar →](ao-carregar)
