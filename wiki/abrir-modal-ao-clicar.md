# `abrir_modal_ao_clicar()`

> Vincula a abertura de um modal nativo `<dialog>` ao clique de um elemento, sem JavaScript manual.

`interatividade.py` · `sweetalert2` · **Não requer `brython=True`**

---

## Assinatura

```python
abrir_modal_ao_clicar(seletor_abrir: str, id_modal: str) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `seletor_abrir` | `str` | — | Seletor CSS do botão/elemento que abrirá o modal (obrigatório) |
| `id_modal` | `str` | — | Atributo `id` do `<dialog>` a ser aberto (obrigatório) |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Botão que abre um modal simples

```python
from pytohtml import html, modal, botao, abrir_modal_ao_clicar, paragrafo

pagina = html(
    modal(
        "info-modal",
        "Sobre o pytohtml",
        paragrafo("Biblioteca Python para gerar HTML com Tailwind CSS."),
    ),
    botao("Saiba mais", variante="primario", classes='id="btn-info"'),
    abrir_modal_ao_clicar("#btn-info", "info-modal"),
    titulo_pagina="Modal Demo",
)
```

**Script gerado:**

```html
<script>
document.addEventListener("DOMContentLoaded", function() {
    const botoes = document.querySelectorAll("#btn-info");
    const modal = document.getElementById("info-modal");
    if (modal) {
        botoes.forEach(btn => btn.addEventListener("click", () => modal.showModal()));
    }
});
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Múltiplos botões abrindo o mesmo modal

```python
from pytohtml import html, modal, grade, cartao, titulo, botao, abrir_modal_ao_clicar, paragrafo

pagina = html(
    # Modal compartilhado
    modal(
        "detalhes-modal",
        "Detalhes do plano",
        paragrafo("Acesso ilimitado a todos os recursos por 30 dias grátis."),
    ),

    # Vários cards com botão que abrem o mesmo modal
    grade(
        cartao(titulo("Plano A", tamanho="medio"), botao("Ver detalhes", classes='id="btn-a"')),
        cartao(titulo("Plano B", tamanho="medio"), botao("Ver detalhes", classes='id="btn-b"')),
        cartao(titulo("Plano C", tamanho="medio"), botao("Ver detalhes", classes='id="btn-c"')),
        colunas=3,
    ),

    abrir_modal_ao_clicar("#btn-a", "detalhes-modal"),
    abrir_modal_ao_clicar("#btn-b", "detalhes-modal"),
    abrir_modal_ao_clicar("#btn-c", "detalhes-modal"),
    titulo_pagina="Planos",
)
```

> 💡 **Dica:** O `seletor_abrir` usa `querySelectorAll` internamente, então suporta múltiplos elementos com a mesma classe: `abrir_modal_ao_clicar(".btn-abrir", "meu-modal")`.

---

### 🟡 Nível 3 — Difícil

> Modal de formulário de edição

```python
from pytohtml import html, cartao, coluna, linha, titulo, paragrafo, botao, modal, formulario, rotulo, entrada, abrir_modal_ao_clicar

pagina = html(
    # Modal com formulário
    modal(
        "editar-modal",
        "Editar informações",
        formulario(
            rotulo("Nome", para="edit-nome"),
            entrada(nome="edit-nome", placeholder="Novo nome", valor="Gabriel Uzeda"),
            rotulo("Email", para="edit-email"),
            entrada(tipo="email", nome="edit-email", placeholder="Novo email"),
            linha(
                botao("Cancelar", variante="fantasma", classes='onclick="document.getElementById(\'editar-modal\').close()"'),
                botao("Salvar",   variante="primario",  tipo="submit"),
                centralizado=False, distanciamento=2, classes="justify-end mt-2",
            ),
            acao="/perfil/editar",
            metodo="post",
        ),
    ),

    # Card de perfil com botão editar
    cartao(
        coluna(
            titulo("Gabriel Uzeda", tamanho="medio"),
            paragrafo("gabriel@exemplo.com", classes="text-gray-400 text-sm"),
            botao("Editar perfil", variante="primario", classes='id="btn-editar"'),
            centralizado=False, distanciamento=2,
        ),
    ),

    abrir_modal_ao_clicar("#btn-editar", "editar-modal"),
    titulo_pagina="Perfil",
)
```

---

### 🟣 Nível 4 — Profissional

> Sistema de modais com abertura por classe (múltiplos itens)

```python
from pytohtml import html, grade, cartao, titulo, paragrafo, botao, modal, abrir_modal_ao_clicar

pagina = html(
    # Um modal único para todos os produtos (conteúdo seria atualizado via Brython)
    modal(
        "produto-modal",
        "Detalhes do produto",
        paragrafo("Carregando...", classes='id="modal-descricao"'),
    ),

    grade(
        *[
            cartao(
                titulo(f"Produto {i}", tamanho="pequeno"),
                botao("Ver mais", variante="fantasma", classes=f'class="btn-produto"'),
            )
            for i in range(1, 5)
        ],
        colunas=4,
    ),

    # Abre o modal ao clicar em qualquer ".btn-produto"
    abrir_modal_ao_clicar(".btn-produto", "produto-modal"),

    titulo_pagina="Catálogo",
)
```

---

## Referência Rápida

| Cenário | Código |
|---------|--------|
| Um botão → um modal | `abrir_modal_ao_clicar("#btn", "modal-id")` |
| Vários botões → mesmo modal | `abrir_modal_ao_clicar(".btn-classe", "modal-id")` |
| Fechar modal | Botão `✕` automático, ou `onclick="document.getElementById('id').close()"` |
| Abrir modal via JS | `document.getElementById('id').showModal()` |

---

← [alerta-ao-enviar](alerta-ao-enviar) · **abrir-modal-ao-clicar** · [Início](Home)
