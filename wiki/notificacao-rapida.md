# `notificacao_rapida()`

> Exibe um toast — notificação pequena e não intrusiva que aparece no canto da tela e some automaticamente.

`interatividade.py` · `sweetalert2` · **Não requer `brython=True`**

---

## Assinatura

```python
notificacao_rapida(
    titulo: str,
    icone: str = "success",
    posicao: str = "top-end",
    duracao: int = 3000,
) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `titulo` | `str` | — | Texto do toast (obrigatório) |
| `icone` | `str` | `"success"` | Ícone: `"success"`, `"error"`, `"warning"`, `"info"`, `"question"` |
| `posicao` | `str` | `"top-end"` | Posição na tela — veja tabela abaixo |
| `duracao` | `int` | `3000` | Duração em milissegundos antes de sumir |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Toast de sucesso no canto superior direito

```python
from pytohtml import html, notificacao_rapida

pagina = html(
    notificacao_rapida("Salvo com sucesso!"),
    titulo_pagina="App"
)
```

**Script gerado:**

```html
<script>
Swal.mixin({toast: true, showConfirmButton: false, timerProgressBar: true}).fire({
    icon: "success", title: "Salvo com sucesso!", position: "top-end", timer: 3000
});
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Toasts com diferentes posições e ícones

```python
# Canto superior direito (padrão)
notificacao_rapida("Item adicionado ao carrinho!", icone="success", posicao="top-end")

# Inferior centralizado
notificacao_rapida("Conexão perdida.", icone="error", posicao="bottom")

# Superior centralizado, mais longo
notificacao_rapida("Processando sua solicitação...", icone="info", posicao="top", duracao=5000)

# Inferior direito, mais curto
notificacao_rapida("Link copiado!", icone="success", posicao="bottom-end", duracao=1500)
```

> 💡 **Dica:** Diferente de `alerta_sucesso()` que exibe um popup centralizado que bloqueia a interação até ser fechado, `notificacao_rapida()` aparece no canto, não bloqueia nada e some sozinho. Ideal para confirmações rápidas e não críticas.

---

### 🟡 Nível 3 — Difícil

> Toast após ação do usuário (via alerta_ao_enviar + notificacao)

```python
from pytohtml import html, formulario, rotulo, entrada, botao

# Exibe um toast após o formulário ser submetido com sucesso
pagina = html(
    formulario(
        rotulo("Email", para="email"),
        entrada(tipo="email", nome="email", placeholder="seu@email.com"),
        botao("Inscrever", variante="primario", tipo="submit", classes='id="btn-inscricao"'),
        acao="#",
    ),
    # JS puro para o combo: interceptar submit + mostrar toast
    '''<script>
    document.querySelector("form").addEventListener("submit", function(ev) {
        ev.preventDefault();
        Swal.mixin({toast: true, showConfirmButton: false, timerProgressBar: true}).fire({
            icon: "success",
            title: "Inscrito com sucesso!",
            position: "top-end",
            timer: 3000
        });
        this.reset();
    });
    </script>''',
    titulo_pagina="Newsletter",
)
```

---

### 🟣 Nível 4 — Profissional

> Sistema de notificações com fila (via HTML puro)

```python
from pytohtml import html, botao

# Simulando diferentes notificações em sequência
notifs_js = '''
<script>
const Toast = Swal.mixin({
    toast: true,
    showConfirmButton: false,
    timerProgressBar: true,
    position: "top-end"
});

async function mostrarNotificacoes() {
    await Toast.fire({ icon: "info",    title: "Verificando sistema...", timer: 1500 });
    await Toast.fire({ icon: "warning", title: "Atualizando dados...",   timer: 1500 });
    await Toast.fire({ icon: "success", title: "Sistema pronto!",        timer: 2000 });
}

document.getElementById("btn-demo").addEventListener("click", mostrarNotificacoes);
</script>
'''

pagina = html(
    botao("Demonstrar notificações", variante="primario", classes='id="btn-demo"'),
    notifs_js,
    titulo_pagina="Demo Notificações",
)
```

---

## Referência Rápida

| `posicao=` | Aparece em |
|------------|-----------|
| `"top"` | Topo centralizado |
| `"top-start"` | Topo esquerdo |
| `"top-end"` | Topo direito (padrão) |
| `"center"` | Centro da tela |
| `"bottom"` | Base centralizada |
| `"bottom-start"` | Base esquerda |
| `"bottom-end"` | Base direita |

---

← [alerta](alerta) · **notificacao-rapida** · [alerta-ao-clicar →](alerta-ao-clicar)
