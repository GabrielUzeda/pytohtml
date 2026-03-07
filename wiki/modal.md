# `modal()`

> Gera um modal flutuante usando a tag nativa `<dialog>` do HTML5 — sem bibliotecas externas.

`layout.py` · `layout`

---

## Assinatura

```python
modal(id_modal: str, titulo_texto: str, *conteudo: str, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `id_modal` | `str` | — | Atributo `id` único do `<dialog>` (obrigatório) |
| `titulo_texto` | `str` | — | Título exibido no cabeçalho do modal (obrigatório) |
| `*conteudo` | `str` | — | Elementos filhos exibidos no corpo do modal |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Modal simples com texto e botão para abrir

```python
from pytohtml import modal, botao, abrir_modal_ao_clicar, paragrafo

modal(
    "meu-modal",
    "Informação importante",
    paragrafo("Este é o conteúdo do modal."),
)
botao("Abrir modal", variante="primario", classes='id="btn-abrir"')
abrir_modal_ao_clicar("#btn-abrir", "meu-modal")
```

**Para abrir o modal via JavaScript:**

```javascript
document.getElementById('meu-modal').showModal()
```

**Para fechar (já incluído automaticamente):**

```html
<button onclick="document.getElementById('meu-modal').close()">✕</button>
```

---

### 🔵 Nível 2 — Intermediário

> Modal de confirmação com dois botões

```python
from pytohtml import html, modal, botao, linha, paragrafo, abrir_modal_ao_clicar

pagina = html(
    # O modal fica oculto até ser aberto
    modal(
        "confirmar-exclusao",
        "Confirmar exclusão",
        paragrafo("Esta ação não pode ser desfeita. Deseja continuar?"),
        linha(
            botao("Cancelar",  variante="fantasma",   classes='onclick="document.getElementById(\'confirmar-exclusao\').close()"'),
            botao("Excluir",   variante="perigo"),
            centralizado=False, distanciamento=2,
            classes="justify-end mt-4",
        ),
    ),

    # Botão que abre o modal
    botao("Excluir item", variante="perigo", classes='id="btn-excluir"'),
    abrir_modal_ao_clicar("#btn-excluir", "confirmar-exclusao"),

    titulo_pagina="Demo Modal",
)
```

> 💡 **Dica:** O botão `✕` para fechar já é gerado automaticamente no cabeçalho do modal. Para botões adicionais de cancelamento no rodapé, use `onclick="document.getElementById('id-do-modal').close()"`.

---

### 🟡 Nível 3 — Difícil

> Modal de formulário (edição inline)

```python
from pytohtml import html, modal, formulario, rotulo, entrada, botao, abrir_modal_ao_clicar

pagina = html(
    modal(
        "editar-perfil",
        "Editar Perfil",
        formulario(
            rotulo("Nome", para="nome"),
            entrada(nome="nome", placeholder="Seu nome", valor="Gabriel Uzeda"),
            rotulo("Email", para="email"),
            entrada(tipo="email", nome="email", placeholder="seu@email.com", valor="gabriel@exemplo.com"),
            linha(
                botao("Cancelar", variante="fantasma",  classes='onclick="document.getElementById(\'editar-perfil\').close()"'),
                botao("Salvar",   variante="primario",  tipo="submit"),
                centralizado=False, distanciamento=2, classes="justify-end",
            ),
            acao="/perfil/editar",
            metodo="post",
        ),
    ),

    botao("Editar perfil", variante="primario", classes='id="btn-editar"'),
    abrir_modal_ao_clicar("#btn-editar", "editar-perfil"),

    titulo_pagina="Editar Perfil",
)
```

---

### 🟣 Nível 4 — Profissional

> Múltiplos modais com `pedir_confirmacao()`

```python
from pytohtml import html, modal, botao, paragrafo, abrir_modal_ao_clicar, pedir_confirmacao

pagina = html(
    # Modal de termos
    modal(
        "termos",
        "Termos de Uso",
        paragrafo("Ao usar o pytohtml, você concorda com a licença MIT..."),
        botao("Li e aceito", variante="primario", classes='id="btn-aceitar-termos"'),
    ),

    # Modal de suporte
    modal(
        "suporte",
        "Contatar Suporte",
        paragrafo("Abra uma issue no GitHub para reportar bugs ou solicitar funcionalidades."),
    ),

    # Botões
    botao("Ver termos",     variante="fantasma",   classes='id="btn-termos"'),
    botao("Suporte",        variante="secundario",  classes='id="btn-suporte"'),
    botao("Excluir conta",  variante="perigo",      classes='id="btn-excluir"'),

    # Vinculações
    abrir_modal_ao_clicar("#btn-termos",  "termos"),
    abrir_modal_ao_clicar("#btn-suporte", "suporte"),
    pedir_confirmacao(
        "#btn-excluir",
        titulo="Excluir conta?",
        texto="Esta ação é permanente e não pode ser desfeita.",
        texto_confirmar="Sim, excluir",
        texto_cancelar="Cancelar",
    ),

    titulo_pagina="Demo Modais",
)
```

---

## Referência Rápida

| Ação | Como fazer |
|------|-----------|
| Abrir modal | `abrir_modal_ao_clicar("#btn", "id-modal")` ou JS: `.showModal()` |
| Fechar modal | Botão `✕` automático no cabeçalho, ou JS: `.close()` |
| Backdrop | Automático via CSS `backdrop:bg-gray-800/60 backdrop:backdrop-blur-sm` |
| Múltiplos modais | Cada um precisa de um `id_modal` único |

---

← [destaque](destaque) · **modal** · [ao-clicar →](ao-clicar)
