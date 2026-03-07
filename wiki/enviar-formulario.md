# `enviar_formulario()`

> Gera código Brython que intercepta o submit de um formulário, coleta os campos e envia via AJAX com feedback automático de sucesso/erro.

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
enviar_formulario(
    seletor_form: str,
    url: str,
    metodo: str = "POST",
    mensagem_sucesso: str = "Enviado com sucesso!",
    texto_carregando: str = "Enviando...",
) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `seletor_form` | `str` | — | Seletor CSS do formulário (ex: `"form"`, `"#form-contato"`) |
| `url` | `str` | — | URL da API de destino (obrigatório) |
| `metodo` | `str` | `"POST"` | Método HTTP |
| `mensagem_sucesso` | `str` | `"Enviado com sucesso!"` | Título do popup SweetAlert2 ao concluir |
| `texto_carregando` | `str` | `"Enviando..."` | Texto do botão submit durante o envio |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Formulário de contato com envio assíncrono

```python
from pytohtml import html, formulario, rotulo, entrada, botao, enviar_formulario

pagina = html(
    formulario(
        rotulo("Nome", para="nome"),
        entrada(nome="nome", placeholder="Seu nome"),
        rotulo("Email", para="email"),
        entrada(tipo="email", nome="email", placeholder="seu@email.com"),
        botao("Enviar", variante="primario", tipo="submit", classes="w-full"),
        acao="#",
    ),
    enviar_formulario(
        "form",
        url="https://jsonplaceholder.typicode.com/posts",
    ),
    titulo_pagina="Contato",
    brython=True,
)
```

---

### 🔵 Nível 2 — Intermediário

> Mensagem de sucesso e texto de carregamento customizados

```python
from pytohtml import html, cartao, titulo, formulario, rotulo, entrada, textarea, botao, enviar_formulario

pagina = html(
    cartao(
        titulo("Fale conosco", tamanho="medio"),
        formulario(
            rotulo("Assunto", para="assunto"),
            entrada(nome="assunto", placeholder="Assunto da mensagem", obrigatorio=True),
            rotulo("Mensagem", para="mensagem"),
            textarea(nome="mensagem", placeholder="Sua mensagem...", linhas=5, obrigatorio=True),
            botao("Enviar mensagem", variante="sucesso", tipo="submit", classes="w-full"),
            acao="#",
        ),
        enviar_formulario(
            "form",
            url="https://jsonplaceholder.typicode.com/posts",
            mensagem_sucesso="Mensagem enviada! Responderemos em breve.",
            texto_carregando="Enviando mensagem...",
        ),
    ),
    titulo_pagina="Contato",
    brython=True,
)
```

> 💡 **Dica:** Durante o envio, o botão `type="submit"` fica desabilitado e com o texto `texto_carregando`, impedindo múltiplos submits acidentais. Após a resposta, ele volta ao estado original.

---

### 🟡 Nível 3 — Difícil

> Formulário em card com ID específico

```python
from pytohtml import html, cartao, formulario, rotulo, entrada, botao, enviar_formulario

pagina = html(
    cartao(
        formulario(
            rotulo("Título do Post", para="title"),
            entrada(nome="title", placeholder="Título", obrigatorio=True),
            rotulo("Conteúdo", para="body"),
            textarea(nome="body", placeholder="Conteúdo do post...", linhas=6),
            botao("Publicar", variante="primario", tipo="submit", classes="w-full"),
            # ID específico para o seletor
            classes='id="form-post"',
            acao="#",
        ),
        classes="max-w-lg mx-auto",
    ),
    enviar_formulario(
        "#form-post",  # Seletor mais específico
        url="https://jsonplaceholder.typicode.com/posts",
        mensagem_sucesso="Post publicado com sucesso!",
    ),
    titulo_pagina="Novo Post",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Formulário de cadastro com múltiplas etapas (step form)

```python
from pytohtml import html, cartao, coluna, titulo, formulario, rotulo, entrada, botao, enviar_formulario

pagina = html(
    cartao(
        coluna(
            titulo("Criar Conta", tamanho="medio"),
            formulario(
                rotulo("Nome completo", para="name"),
                entrada(tipo="text",     nome="name",     placeholder="Gabriel Uzeda", obrigatorio=True),
                rotulo("Email",          para="email"),
                entrada(tipo="email",    nome="email",    placeholder="gabriel@exemplo.com", obrigatorio=True),
                rotulo("Senha",          para="password"),
                entrada(tipo="password", nome="password", placeholder="Mínimo 8 caracteres"),
                rotulo("Cargo",          para="job"),
                entrada(tipo="text",     nome="job",      placeholder="Desenvolvedor Python"),
                botao("Criar conta gratuitamente", variante="primario", tipo="submit", classes="w-full mt-2"),
                acao="#",
            ),
            enviar_formulario(
                "form",
                url="https://dummyjson.com/users/add",
                mensagem_sucesso="Conta criada com sucesso! Bem-vindo(a)!",
                texto_carregando="Criando sua conta...",
            ),
            centralizado=False, distanciamento=4,
        ),
        classes="max-w-md mx-auto",
    ),
    titulo_pagina="Cadastro",
    brython=True,
)
```

---

## O que acontece por baixo

1. **Submit interceptado** — `ev.preventDefault()` cancela o comportamento padrão
2. **Campos coletados** — todos os `<input>`, `<textarea>` e `<select>` com `name` são serializados como JSON
3. **Botão bloqueado** — texto muda para `texto_carregando` e `disabled=True`
4. **AJAX enviado** — `Content-Type: application/json` via `browser.ajax`
5. **Resposta tratada** — status 200–204: popup de sucesso + `form.reset()` | outros: popup de erro

---

← [buscar-dados](buscar-dados) · **enviar-formulario** · [alerta →](alerta)
