# `pedir_confirmacao()`

> Vincula um diálogo "Tem certeza?" ao clique de um elemento — exibe botões Confirmar/Cancelar via SweetAlert2.

`interatividade.py` · `sweetalert2` · **Não requer `brython=True`**

---

## Assinatura

```python
pedir_confirmacao(
    seletor: str,
    titulo: str = "Tem certeza?",
    texto: str = "",
    texto_confirmar: str = "Sim",
    texto_cancelar: str = "Cancelar",
    codigo_confirmado: str = "",
) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `seletor` | `str` | — | Seletor CSS do elemento que dispara o diálogo (obrigatório) |
| `titulo` | `str` | `"Tem certeza?"` | Título do popup |
| `texto` | `str` | `""` | Mensagem descritiva |
| `texto_confirmar` | `str` | `"Sim"` | Label do botão de confirmação |
| `texto_cancelar` | `str` | `"Cancelar"` | Label do botão de cancelamento |
| `codigo_confirmado` | `str` | `""` | Código JavaScript a executar ao confirmar |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Confirmação antes de excluir

```python
from pytohtml import html, botao, pedir_confirmacao

pagina = html(
    botao("Excluir item", variante="perigo", classes='id="btn-excluir"'),
    pedir_confirmacao(
        "#btn-excluir",
        titulo="Excluir item?",
        texto="Esta ação não pode ser desfeita.",
        texto_confirmar="Sim, excluir",
        texto_cancelar="Cancelar",
    ),
    titulo_pagina="Confirmação",
)
```

**Script gerado (estrutura):**

```html
<script>
document.querySelector("#btn-excluir").addEventListener("click", function() {
    Swal.fire({
        icon: "warning",
        title: "Excluir item?",
        text: "Esta ação não pode ser desfeita.",
        showCancelButton: true,
        confirmButtonText: "Sim, excluir",
        cancelButtonText: "Cancelar",
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
    }).then(function(result) {
        if (result.isConfirmed) {
            Swal.fire({icon: "success", title: "Confirmado!", timer: 1500, showConfirmButton: false});
        }
    });
});
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Confirmação com texto e botão customizados

```python
from pytohtml import html, botao, pedir_confirmacao

pagina = html(
    botao("Cancelar assinatura", variante="perigo", classes='id="btn-cancelar"'),
    pedir_confirmacao(
        "#btn-cancelar",
        titulo="Cancelar assinatura?",
        texto="Você perderá acesso a todas as funcionalidades Premium imediatamente.",
        texto_confirmar="Sim, cancelar",
        texto_cancelar="Manter assinatura",
    ),
    titulo_pagina="Assinatura",
)
```

> 💡 **Dica:** O ícone `"warning"` (amarelo) é sempre usado automaticamente em `pedir_confirmacao()` — ideal para ações destrutivas ou irreversíveis. Após confirmar, um popup de sucesso é exibido automaticamente com `timer: 1500ms`.

---

### 🟡 Nível 3 — Difícil

> Confirmação com redirect JavaScript após confirmar

```python
from pytohtml import html, botao, pedir_confirmacao

pagina = html(
    botao("Sair da conta", variante="fantasma", classes='id="btn-logout"'),
    pedir_confirmacao(
        "#btn-logout",
        titulo="Sair da conta?",
        texto="Você precisará fazer login novamente.",
        texto_confirmar="Sair",
        texto_cancelar="Ficar",
        codigo_confirmado="window.location.href = '/logout';",
    ),
    titulo_pagina="Logout",
)
```

---

### 🟣 Nível 4 — Profissional

> Múltiplas confirmações na mesma página (CRUD)

```python
from pytohtml import html, cartao, titulo, grade, botao, pedir_confirmacao, alerta_ao_clicar

pagina = html(
    grade(
        cartao(
            titulo("Item #1", tamanho="pequeno"),
            botao("Editar",  variante="fantasma", classes='id="btn-edit-1"'),
            botao("Excluir", variante="perigo",   classes='id="btn-del-1"'),
        ),
        cartao(
            titulo("Item #2", tamanho="pequeno"),
            botao("Editar",  variante="fantasma", classes='id="btn-edit-2"'),
            botao("Excluir", variante="perigo",   classes='id="btn-del-2"'),
        ),
        colunas=2,
    ),
    # Editar — apenas informa
    alerta_ao_clicar("#btn-edit-1", "Editar Item #1", "Abrindo formulário de edição...", icone="info"),
    alerta_ao_clicar("#btn-edit-2", "Editar Item #2", "Abrindo formulário de edição...", icone="info"),
    # Excluir — pede confirmação
    pedir_confirmacao("#btn-del-1", "Excluir Item #1?", "Esta ação não pode ser desfeita.", "Excluir", "Cancelar"),
    pedir_confirmacao("#btn-del-2", "Excluir Item #2?", "Esta ação não pode ser desfeita.", "Excluir", "Cancelar"),
    titulo_pagina="Lista",
)
```

---

## Referência Rápida

| Parâmetro | Padrão | Quando customizar |
|-----------|--------|------------------|
| `titulo` | `"Tem certeza?"` | Especificar a ação: "Excluir post?" |
| `texto` | `""` | Detalhar consequências |
| `texto_confirmar` | `"Sim"` | "Sim, excluir", "Confirmar", "Sair" |
| `texto_cancelar` | `"Cancelar"` | "Manter", "Voltar", "Não" |
| `codigo_confirmado` | `""` | Redirect, chamada AJAX, etc. |

---

← [alerta-ao-clicar](alerta-ao-clicar) · **pedir-confirmacao** · [alerta-ao-enviar →](alerta-ao-enviar)
