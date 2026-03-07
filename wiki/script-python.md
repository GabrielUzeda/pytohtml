# `script_python()`

> Encapsula código Python livre dentro de `<script type="text/python">` para execução pelo Brython no browser.

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
script_python(*codigo: str) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*codigo` | `str` | — | Blocos de código Python para execução no browser via Brython |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Script Python simples no browser

```python
from pytohtml import html, script_python

pagina = html(
    script_python('''
        from browser import alert
        alert("Olá do Brython!")
    '''),
    titulo_pagina="Script Python",
    brython=True,
)
```

**HTML gerado:**

```html
<script type="text/python">
from browser import alert
alert("Olá do Brython!")
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Definir funções reutilizáveis no browser

```python
from pytohtml import html, botao, espaco_dinamico, script_python

pagina = html(
    espaco_dinamico("resultado"),
    botao("Gerar número", classes='id="btn-rand"'),
    script_python('''
        from browser import document
        import random

        def gerar_numero():
            n = random.randint(1, 100)
            document["resultado"].html = f"<span class='text-2xl font-bold text-blue-600'>{n}</span>"

        document["btn-rand"].bind("click", lambda ev: gerar_numero())
    '''),
    titulo_pagina="Aleatório",
    brython=True,
)
```

> 💡 **Dica:** `script_python()` é a base de todas as outras funções de interatividade (`ao_clicar`, `ao_carregar`, `estado`, `buscar_dados`). Use-o diretamente quando precisar de controle total sobre o script Brython.

---

### 🟡 Nível 3 — Difícil

> Múltiplos blocos concatenados

```python
from pytohtml import html, script_python

# Blocos separados mas executados no mesmo contexto
pagina = html(
    script_python(
        # Bloco 1: definições
        '''
        from browser import document, window
        import json

        DADOS = {"nome": "Gabriel", "linguagem": "Python"}
        ''',
        # Bloco 2: execução
        '''
        el = document.select("body")[0]
        el.html += f"<p>Olá, {DADOS['nome']}! Você usa {DADOS['linguagem']}.</p>"
        '''
    ),
    titulo_pagina="Multi-bloco",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Integração com APIs do browser (localStorage, clipboard)

```python
from pytohtml import html, coluna, botao, espaco_dinamico, script_python

pagina = html(
    coluna(
        espaco_dinamico("valor-salvo", "text-gray-500 text-sm"),
        botao("Salvar no localStorage", classes='id="btn-salvar"'),
        botao("Ler do localStorage",    classes='id="btn-ler"'),
        botao("Copiar para clipboard",  classes='id="btn-copiar"'),
    ),
    script_python('''
        from browser import document, window

        CHAVE = "pytohtml_demo"
        VALOR = "Dados salvos com Python no browser!"

        def salvar(ev):
            window.localStorage.setItem(CHAVE, VALOR)
            document["valor-salvo"].text = "Salvo!"

        def ler(ev):
            v = window.localStorage.getItem(CHAVE)
            document["valor-salvo"].text = v or "(nenhum dado salvo)"

        def copiar(ev):
            window.navigator.clipboard.writeText(VALOR)
            document["valor-salvo"].text = "Copiado!"

        document["btn-salvar"].bind("click", salvar)
        document["btn-ler"].bind("click",    ler)
        document["btn-copiar"].bind("click", copiar)
    '''),
    titulo_pagina="LocalStorage",
    brython=True,
)
```

---

## Referência Rápida — APIs do Brython

| Import | O que acessa |
|--------|-------------|
| `from browser import document` | DOM completo |
| `from browser import window` | `window` global (localStorage, location, etc.) |
| `from browser import alert` | `window.alert()` |
| `from browser import ajax` | Requisições HTTP |
| `from browser import timer` | `setTimeout`, `setInterval` |

---

← [ao-carregar](ao-carregar) · **script-python** · [espaco-dinamico →](espaco-dinamico)
