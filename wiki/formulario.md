# `formulario()`

> Gera um elemento `<form>` com espaçamento automático entre os campos filhos.

`elementos.py` · `formulários`

---

## Assinatura

```python
formulario(*conteudo: str, acao: str = "#", metodo: str = "post", classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Campos, rótulos e botões do formulário |
| `acao` | `str` | `"#"` | Atributo `action` — URL de destino do envio |
| `metodo` | `str` | `"post"` | Atributo `method` — `"get"` ou `"post"` |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Formulário simples de login

```python
from pytohtml import formulario, rotulo, entrada, botao

formulario(
    rotulo("Email", para="email"),
    entrada(tipo="email", nome="email", placeholder="seu@email.com"),
    rotulo("Senha", para="senha"),
    entrada(tipo="password", nome="senha", placeholder="Sua senha"),
    botao("Entrar", variante="primario", tipo="submit", classes="w-full"),
)
```

**HTML gerado (estrutura):**

```html
<form action="#" method="post" class="space-y-4">
  <label for="email" ...>Email</label>
  <input type="email" name="email" ... />
  <label for="senha" ...>Senha</label>
  <input type="password" name="senha" ... />
  <button type="submit" ...>Entrar</button>
</form>
```

---

### 🔵 Nível 2 — Intermediário

> Formulário GET para busca

```python
formulario(
    entrada(tipo="search", nome="q", placeholder="Buscar..."),
    botao("Buscar", variante="primario", tipo="submit"),
    acao="/buscar",
    metodo="get",
)
```

> 💡 **Dica:** `space-y-4` já vem aplicado por padrão — ele adiciona espaçamento vertical automático entre todos os filhos diretos do form. Para formulários mais compactos, adicione `classes="space-y-2"`.

---

### 🟡 Nível 3 — Difícil

> Formulário de cadastro em duas colunas

```python
from pytohtml import formulario, grade, rotulo, entrada, textarea, botao, divisor

formulario(
    grade(
        coluna(rotulo("Nome", para="nome"),   entrada(nome="nome",  placeholder="Nome"),  centralizado=False, distanciamento=1),
        coluna(rotulo("Sobrenome", para="sob"), entrada(nome="sob", placeholder="Sobrenome"), centralizado=False, distanciamento=1),
        colunas=2,
    ),
    rotulo("Email", para="email"),
    entrada(tipo="email", nome="email", placeholder="seu@email.com", obrigatorio=True),
    rotulo("Mensagem", para="msg"),
    textarea(nome="msg", placeholder="Sua mensagem...", linhas=4),
    divisor(classes="my-2"),
    botao("Enviar cadastro", variante="primario", tipo="submit", classes="w-full"),
    acao="/cadastro",
    metodo="post",
)
```

---

### 🟣 Nível 4 — Profissional

> Formulário com envio assíncrono via `enviar_formulario()`

```python
from pytohtml import html, cartao, formulario, rotulo, entrada, textarea, botao, enviar_formulario

pagina = html(
    cartao(
        formulario(
            rotulo("Título", para="titulo"),
            entrada(nome="titulo", placeholder="Título do post", obrigatorio=True),
            rotulo("Conteúdo", para="body"),
            textarea(nome="body", placeholder="Escreva o conteúdo...", linhas=6, obrigatorio=True),
            botao("Publicar", variante="sucesso", tipo="submit", classes="w-full"),
            acao="#",  # A URL real é passada para enviar_formulario()
        ),
        enviar_formulario(
            "form",
            url="https://jsonplaceholder.typicode.com/posts",
            mensagem_sucesso="Post publicado com sucesso!",
        ),
        classes="max-w-lg mx-auto",
    ),
    titulo_pagina="Novo Post",
    brython=True,
)
```

> ⚠️ **Atenção:** Ao usar `enviar_formulario()`, defina `acao="#"` no `formulario()` — o envio real é interceptado pelo script Brython antes de chegar ao `action` padrão.

---

## Referência Rápida

| Parâmetro | Efeito |
|-----------|--------|
| `acao="/"` | Envia para a raiz do site |
| `acao="https://..."` | Envia para API externa |
| `metodo="get"` | Parâmetros na URL (busca, filtros) |
| `metodo="post"` | Dados no body (padrão, seguro) |
| `classes="space-y-2"` | Espaçamento menor entre campos |

---

← [textarea](textarea) · **formulario** · [linha-e-coluna →](linha-e-coluna)
