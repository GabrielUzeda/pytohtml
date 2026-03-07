# `ao_carregar()`

> Executa código Python (Brython) imediatamente quando a página termina de carregar.

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
ao_carregar(codigo: str) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `codigo` | `str` | — | Código Python a executar no carregamento da página |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Exibir mensagem ao carregar

```python
from pytohtml import html, ao_carregar

pagina = html(
    ao_carregar('''
        from browser import document
        document["status"].text = "Página carregada com sucesso!"
    '''),
    '<div id="status" class="text-center text-gray-600 mt-8"></div>',
    titulo_pagina="Carregamento",
    brython=True,
)
```

**Script gerado:**

```html
<script type="text/python">
from browser import document
document["status"].text = "Página carregada com sucesso!"
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Inicializar múltiplos elementos ao carregar

```python
from pytohtml import html, espaco_dinamico, ao_carregar

pagina = html(
    espaco_dinamico("hora-atual",  "text-2xl font-bold text-blue-600"),
    espaco_dinamico("data-atual",  "text-gray-400"),
    espaco_dinamico("saudacao",    "text-lg"),
    ao_carregar('''
        from browser import document
        import datetime

        agora = datetime.datetime.now()
        document["hora-atual"].text = agora.strftime("%H:%M:%S")
        document["data-atual"].text = agora.strftime("%d/%m/%Y")

        hora = agora.hour
        if hora < 12:
            saudacao = "Bom dia!"
        elif hora < 18:
            saudacao = "Boa tarde!"
        else:
            saudacao = "Boa noite!"
        document["saudacao"].text = saudacao
    '''),
    titulo_pagina="Data e Hora",
    brython=True,
)
```

> 💡 **Dica:** `ao_carregar()` é executado no escopo global do Brython, então variáveis e funções definidas nele ficam acessíveis para outros `script_python()` e `ao_clicar()` na mesma página — desde que venham depois na ordem do DOM.

---

### 🟡 Nível 3 — Difícil

> Verificar parâmetros da URL e personalizar a página

```python
from pytohtml import html, espaco_dinamico, ao_carregar

pagina = html(
    espaco_dinamico("mensagem-boas-vindas", "text-xl text-center mt-8"),
    ao_carregar('''
        from browser import document, window

        # Lê parâmetros da URL (?nome=Gabriel)
        params = dict(
            p.split("=") for p in window.location.search.lstrip("?").split("&") if "=" in p
        )
        nome = params.get("nome", "Visitante")
        document["mensagem-boas-vindas"].html = f"<strong>Bem-vindo, {nome}!</strong>"
    '''),
    titulo_pagina="Personalizado",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Carregar dados da API imediatamente ao abrir a página

```python
from pytohtml import html, cartao, titulo, espaco_dinamico, ao_carregar, animacao_carregando

pagina = html(
    cartao(
        titulo("Usuário do dia", tamanho="medio"),
        espaco_dinamico("perfil-usuario", "space-y-2"),
        animacao_carregando(tipo="texto", linhas=3),
    ),
    ao_carregar('''
        from browser import ajax, document
        import json

        def exibir_usuario(req):
            if req.status == 200:
                u = json.loads(req.text)
                document["perfil-usuario"].html = f"""
                    <p><strong>Nome:</strong> {u["firstName"]} {u["lastName"]}</p>
                    <p><strong>Email:</strong> {u["email"]}</p>
                    <p><strong>Empresa:</strong> {u["company"]["name"]}</p>
                """

        ajax.get("https://dummyjson.com/users/1", oncomplete=exibir_usuario)
    '''),
    titulo_pagina="Perfil",
    brython=True,
)
```

---

← [ao-clicar](ao-clicar) · **ao-carregar** · [script-python →](script-python)
