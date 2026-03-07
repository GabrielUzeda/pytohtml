# `buscar_dados()`

> Gera código Brython que faz uma requisição HTTP (fetch) para uma API e renderiza o resultado no DOM.

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
buscar_dados(
    url: str,
    metodo: str = "GET",
    callback_nome: str = "_on_response",
    corpo: str | None = None,
    seletor_resultado: str | None = None,
    silencioso: bool = False,
    gatilho_clique: str | None = None,
) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `url` | `str` | — | URL da API (obrigatório) |
| `metodo` | `str` | `"GET"` | Método HTTP: `"GET"`, `"POST"`, `"PUT"`, `"DELETE"` |
| `callback_nome` | `str` | `"_on_response"` | Nome da função callback que recebe o request |
| `corpo` | `str \| None` | `None` | Body da requisição como JSON string (para POST/PUT) |
| `seletor_resultado` | `str \| None` | `None` | Seletor CSS onde o resultado será renderizado |
| `silencioso` | `bool` | `False` | Se `True`, não exibe SweetAlert2 em erros |
| `gatilho_clique` | `str \| None` | `None` | Seletor CSS do botão que dispara a busca (se `None`, busca ao carregar) |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Buscar dados ao carregar a página

```python
from pytohtml import html, espaco_dinamico, buscar_dados

pagina = html(
    espaco_dinamico("resultado", "mt-4"),
    buscar_dados(
        "https://dummyjson.com/quotes/random",
        seletor_resultado="#resultado",
    ),
    titulo_pagina="Citação do Dia",
    brython=True,
)
```

---

### 🔵 Nível 2 — Intermediário

> Busca acionada por botão com feedback de carregamento

```python
from pytohtml import html, cartao, botao, espaco_dinamico, buscar_dados

pagina = html(
    cartao(
        botao("Buscar usuário aleatório", variante="primario", classes='id="btn-buscar"'),
        espaco_dinamico("dados-usuario", "mt-4 space-y-2"),
    ),
    buscar_dados(
        "https://dummyjson.com/users/1",
        seletor_resultado="#dados-usuario",
        gatilho_clique="#btn-buscar",
    ),
    titulo_pagina="Usuário",
    brython=True,
)
```

> 💡 **Dica:** Quando `gatilho_clique` é fornecido, um skeleton de carregamento (`animate-pulse`) é exibido automaticamente no `seletor_resultado` enquanto a requisição está em andamento.

---

### 🟡 Nível 3 — Difícil

> POST para uma API com corpo JSON

```python
from pytohtml import html, formulario, rotulo, entrada, botao, espaco_dinamico, buscar_dados
import json

novo_post = json.dumps({"title": "pytohtml", "body": "Lib Python para gerar HTML.", "userId": 1})

pagina = html(
    espaco_dinamico("resposta", "mt-4"),
    botao("Enviar POST", variante="primario", classes='id="btn-post"'),
    buscar_dados(
        "https://jsonplaceholder.typicode.com/posts",
        metodo="POST",
        corpo=novo_post,
        seletor_resultado="#resposta",
        gatilho_clique="#btn-post",
    ),
    titulo_pagina="POST Demo",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Dashboard com múltiplas APIs em paralelo

```python
from pytohtml import html, grade, cartao, titulo, espaco_dinamico, buscar_dados

pagina = html(
    grade(
        cartao(
            titulo("Usuário", tamanho="pequeno"),
            espaco_dinamico("dados-user", "space-y-1 text-sm"),
        ),
        cartao(
            titulo("Post recente", tamanho="pequeno"),
            espaco_dinamico("dados-post", "space-y-1 text-sm"),
        ),
        cartao(
            titulo("Produto", tamanho="pequeno"),
            espaco_dinamico("dados-produto", "space-y-1 text-sm"),
        ),
        colunas=3,
    ),
    buscar_dados("https://dummyjson.com/users/1",    seletor_resultado="#dados-user"),
    buscar_dados("https://dummyjson.com/posts/1",     seletor_resultado="#dados-post"),
    buscar_dados("https://dummyjson.com/products/1",  seletor_resultado="#dados-produto"),
    titulo_pagina="Dashboard",
    brython=True,
)
```

---

## Referência Rápida

| Cenário | Parâmetros |
|---------|-----------|
| Busca ao carregar | `buscar_dados(url, seletor_resultado="#el")` |
| Busca ao clicar | `buscar_dados(url, seletor_resultado="#el", gatilho_clique="#btn")` |
| POST com corpo | `buscar_dados(url, metodo="POST", corpo='{"key":"val"}')` |
| Sem SweetAlert2 em erro | `buscar_dados(url, silencioso=True)` |
| Callback customizado | `buscar_dados(url, callback_nome="meu_callback")` |

---

← [estado](estado) · **buscar-dados** · [enviar-formulario →](enviar-formulario)
