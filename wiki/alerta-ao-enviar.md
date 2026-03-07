# `alerta_ao_enviar()`

> Intercepta o submit de um formulário e exibe um popup SweetAlert2 de sucesso, sem recarregar a página.

`interatividade.py` · `sweetalert2` · **Não requer `brython=True`**

---

## Assinatura

```python
alerta_ao_enviar(seletor_form: str, mensagem_sucesso: str = "Enviado com sucesso!") → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `seletor_form` | `str` | — | Seletor CSS do formulário (obrigatório) |
| `mensagem_sucesso` | `str` | `"Enviado com sucesso!"` | Título do popup de sucesso |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Feedback visual ao submeter um formulário

```python
from pytohtml import html, formulario, rotulo, entrada, botao, alerta_ao_enviar

pagina = html(
    formulario(
        rotulo("Nome", para="nome"),
        entrada(nome="nome", placeholder="Seu nome"),
        botao("Enviar", variante="primario", tipo="submit", classes="w-full"),
        acao="#",
    ),
    alerta_ao_enviar("form", "Formulário enviado com sucesso!"),
    titulo_pagina="Formulário",
)
```

**Script gerado:**

```html
<script>
document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function(ev) {
            ev.preventDefault();
            Swal.fire({
                icon: "success",
                title: "Formulário enviado com sucesso!",
                confirmButtonColor: "#16a34a",
            });
        });
    }
});
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Diferença entre `alerta_ao_enviar()` e `enviar_formulario()`

```python
# alerta_ao_enviar() — apenas exibe o popup, NÃO envia para a URL
# Ideal para: demos, testes, forms sem backend
alerta_ao_enviar("form", "Dados recebidos!")

# enviar_formulario() — envia via AJAX para a URL + exibe popup
# Ideal para: integração real com APIs, produção
# enviar_formulario("form", "https://api.exemplo.com/contato")
```

> 💡 **Dica:** Use `alerta_ao_enviar()` para protótipos e demonstrações onde você quer mostrar o comportamento do form sem integrar com backend. Para envio real via AJAX, use `enviar_formulario()`.

---

### 🟡 Nível 3 — Difícil

> Formulário de newsletter com ID específico

```python
from pytohtml import html, cartao, titulo, paragrafo, formulario, entrada, botao, alerta_ao_enviar

pagina = html(
    cartao(
        titulo("Newsletter", tamanho="medio"),
        paragrafo("Receba novidades sobre o pytohtml direto no seu email.", classes="text-gray-400 text-sm"),
        formulario(
            entrada(tipo="email", nome="email", placeholder="seu@email.com", obrigatorio=True),
            botao("Inscrever-se", variante="primario", tipo="submit", classes="w-full"),
            classes='id="form-newsletter"',
            acao="#",
        ),
        alerta_ao_enviar("#form-newsletter", "Inscrito com sucesso! Bem-vindo(a) 🎉"),
        classes="max-w-sm mx-auto",
    ),
    titulo_pagina="Newsletter",
)
```

---

### 🟣 Nível 4 — Profissional

> Múltiplos formulários na mesma página com alertas independentes

```python
from pytohtml import html, grade, cartao, titulo, formulario, rotulo, entrada, textarea, botao, alerta_ao_enviar

pagina = html(
    grade(
        cartao(
            titulo("Login", tamanho="medio"),
            formulario(
                rotulo("Email", para="login-email"),
                entrada(tipo="email",    nome="login-email",    placeholder="seu@email.com"),
                rotulo("Senha", para="login-senha"),
                entrada(tipo="password", nome="login-senha",    placeholder="Sua senha"),
                botao("Entrar", variante="primario", tipo="submit", classes="w-full"),
                classes='id="form-login"',
                acao="#",
            ),
        ),
        cartao(
            titulo("Contato", tamanho="medio"),
            formulario(
                rotulo("Mensagem", para="msg"),
                textarea(nome="msg", placeholder="Sua mensagem...", linhas=4),
                botao("Enviar", variante="sucesso", tipo="submit", classes="w-full"),
                classes='id="form-contato"',
                acao="#",
            ),
        ),
        colunas=2,
    ),
    alerta_ao_enviar("#form-login",   "Login realizado com sucesso!"),
    alerta_ao_enviar("#form-contato", "Mensagem enviada! Responderemos em breve."),
    titulo_pagina="Demo",
)
```

---

## Referência Rápida

| Cenário | Função recomendada |
|---------|-------------------|
| Demo / protótipo sem backend | `alerta_ao_enviar()` |
| Envio real via AJAX | `enviar_formulario()` |
| Form com redirect após sucesso | JS puro via `html(...)` |

---

← [pedir-confirmacao](pedir-confirmacao) · **alerta-ao-enviar** · [abrir-modal-ao-clicar →](abrir-modal-ao-clicar)
