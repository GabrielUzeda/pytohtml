# `alerta_ao_clicar()`

> Vincula um popup SweetAlert2 ao clique de um elemento — o alerta só aparece quando o usuário clica.

`interatividade.py` · `sweetalert2` · **Não requer `brython=True`**

---

## Assinatura

```python
alerta_ao_clicar(seletor: str, titulo: str, texto: str = "", icone: str = "info") → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `seletor` | `str` | — | Seletor CSS do elemento que dispara o alerta (obrigatório) |
| `titulo` | `str` | — | Título do popup (obrigatório) |
| `texto` | `str` | `""` | Mensagem descritiva |
| `icone` | `str` | `"info"` | Ícone: `"success"`, `"error"`, `"warning"`, `"info"`, `"question"` |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Popup informativo ao clicar em um botão

```python
from pytohtml import html, botao, alerta_ao_clicar

pagina = html(
    botao("O que é pytohtml?", variante="fantasma", classes='id="btn-info"'),
    alerta_ao_clicar(
        "#btn-info",
        "pytohtml",
        "Biblioteca Python para gerar HTML com Tailwind CSS.",
        icone="info",
    ),
    titulo_pagina="Info",
)
```

**Script gerado:**

```html
<script>
document.querySelector("#btn-info").addEventListener("click", function() {
    Swal.fire({icon: "info", title: "pytohtml", text: "Biblioteca Python para gerar HTML com Tailwind CSS."});
});
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Botões de ajuda com ícones diferentes

```python
from pytohtml import html, linha, botao, alerta_ao_clicar

pagina = html(
    linha(
        botao("Ajuda",    variante="texto",     classes='id="btn-ajuda"'),
        botao("Sobre",    variante="texto",     classes='id="btn-sobre"'),
        botao("Contato",  variante="texto",     classes='id="btn-contato"'),
    ),
    alerta_ao_clicar("#btn-ajuda",   "Precisa de ajuda?", "Acesse a documentação em /wiki.", icone="question"),
    alerta_ao_clicar("#btn-sobre",   "Sobre o pytohtml",  "Versão 1.0 — MIT License.",       icone="info"),
    alerta_ao_clicar("#btn-contato", "Contato",           "Abra uma issue no GitHub.",       icone="success"),
    titulo_pagina="Demo",
)
```

> 💡 **Dica:** Use `icone="question"` para informações de ajuda, `icone="warning"` para alertas sobre consequências de ações, e `icone="success"` para confirmações visuais.

---

### 🟡 Nível 3 — Difícil

> Alerta ao clicar em itens de uma lista

```python
from pytohtml import html, cartao, lista, alerta_ao_clicar

pagina = html(
    cartao(
        lista(
            '<span id="item-python" class="cursor-pointer hover:text-blue-600">Python</span>',
            '<span id="item-tailwind" class="cursor-pointer hover:text-blue-600">Tailwind CSS</span>',
            '<span id="item-brython" class="cursor-pointer hover:text-blue-600">Brython</span>',
        ),
    ),
    alerta_ao_clicar("#item-python",  "Python",      "Linguagem principal da lib.", icone="info"),
    alerta_ao_clicar("#item-tailwind","Tailwind CSS", "Framework CSS via CDN.",     icone="info"),
    alerta_ao_clicar("#item-brython", "Brython",      "Python no browser.",         icone="info"),
    titulo_pagina="Tecnologias",
)
```

---

### 🟣 Nível 4 — Profissional

> Alertas com HTML rico no texto (via SweetAlert2 direto)

```python
from pytohtml import html, botao

# Para popups com HTML customizado, use JS puro com html: ao invés de text:
popup_rico = '''
<script>
document.querySelector("#btn-premium").addEventListener("click", function() {
    Swal.fire({
        icon: "warning",
        title: "Funcionalidade Premium",
        html: `
            <p class="text-gray-600">Esta funcionalidade requer o <strong>Plano Pro</strong>.</p>
            <p class="text-sm text-gray-400 mt-2">A partir de R$ 49/mês.</p>
        `,
        confirmButtonText: "Ver planos",
        showCancelButton: true,
        cancelButtonText: "Agora não",
        confirmButtonColor: "#2563eb",
    }).then(result => {
        if (result.isConfirmed) window.location.href = "/planos";
    });
});
</script>
'''

pagina = html(
    botao("Funcionalidade premium", variante="primario", classes='id="btn-premium"'),
    popup_rico,
    titulo_pagina="Premium",
)
```

---

## Referência Rápida

| `icone=` | Uso típico |
|---------|-----------|
| `"info"` | Informações sobre um item |
| `"success"` | Confirmação de ação |
| `"warning"` | Aviso sobre consequências |
| `"error"` | Operação bloqueada |
| `"question"` | Dúvidas e ajuda |

---

← [notificacao-rapida](notificacao-rapida) · **alerta-ao-clicar** · [pedir-confirmacao →](pedir-confirmacao)
